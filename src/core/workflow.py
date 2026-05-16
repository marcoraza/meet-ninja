import traceback
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Optional

import structlog

from src.connectors.github_repo import GitHubClient
from src.connectors.google.auth import build_credentials
from src.connectors.google.drive import DriveClient
from src.connectors.google.gmail import GmailClient
from src.core.config import Settings
from src.core.contracts import (
    Classification,
    Enrichment,
    MeetingContent,
    MeetingSource,
    Project,
    Receipt,
    RenderedBundle,
)
from src.services import parser, receipts
from src.services.alerts import send_failure_alert
from src.services.classifier import GeminiClassifier, apply_threshold
from src.services.enricher import GeminiEnricher
from src.services.renderer import (
    _extract_transcription_section,
    render,
    sha256_hex,
)


log = structlog.get_logger(__name__)


_UNKNOWN_SLUG = "unknown"


def run(settings: Settings, limit: int = 25) -> list[Receipt]:
    creds = build_credentials(settings.sa_file, settings.delegated_user)
    gmail = GmailClient(creds)
    drive = DriveClient(creds)
    github = GitHubClient(settings.github_token, settings.github_repo) if settings.github_token else None

    if github is None and not settings.dry_run:
        raise RuntimeError("GITHUB_TOKEN required when dry_run=false")

    projects = _load_projects(github, settings)
    log.info("projects_loaded", count=len(projects), slugs=[p.slug for p in projects])

    classifier = GeminiClassifier(settings.gemini_api_key, settings.gemini_model)
    enricher = GeminiEnricher(settings.gemini_api_key, settings.gemini_model)
    receipts_dir = settings.data_dir / "receipts"

    message_ids = gmail.search(settings.email_query, max_results=limit)
    log.info("messages_found", count=len(message_ids), query=settings.email_query)

    out: list[Receipt] = []
    for mid in message_ids:
        receipt = _process_one(
            mid, gmail, drive, github, classifier, enricher, projects, settings, receipts_dir
        )
        out.append(receipt)
    return out


def _load_projects(github: Optional[GitHubClient], settings: Settings) -> list[Project]:
    if github is None:
        return []
    return github.load_projects(settings.github_projects_yaml_path)


def _process_one(
    message_id: str,
    gmail: GmailClient,
    drive: DriveClient,
    github: Optional[GitHubClient],
    classifier: GeminiClassifier,
    enricher: GeminiEnricher,
    projects: list[Project],
    settings: Settings,
    receipts_dir: Path,
) -> Receipt:
    receipt_id = receipts.new_receipt_id()
    log.info("processing_start", receipt_id=receipt_id, message_id=message_id)

    partial_source: Optional[MeetingSource] = None
    partial_classification: Optional[Classification] = None
    partial_enrichment: Optional[Enrichment] = None

    try:
        message = gmail.get_message(message_id)
        subject = gmail.get_header(message, "Subject") or ""
        date_header = gmail.get_header(message, "Date") or ""
        received_at = _parse_received_at(date_header)
        thread_id = message.get("threadId", "")

        doc_ids = gmail.extract_doc_ids(message)
        if not doc_ids:
            raise RuntimeError("No Google Doc IDs found in message body")
        notes_doc_id = doc_ids[0]

        notes_md = drive.export_doc_as_markdown(notes_doc_id)
        transcript_doc_id = parser.extract_transcript_doc_id(notes_md, notes_doc_id)
        transcript_md: Optional[str] = None
        if transcript_doc_id:
            transcript_md = drive.export_doc_as_markdown(transcript_doc_id)

        fallback_title = parser.extract_title(notes_md, subject)
        meeting_dt = parser.extract_meeting_datetime(notes_md)
        summary = parser.extract_summary_block(notes_md) or notes_md[:2000]

        source = MeetingSource(
            gmail_message_id=message_id,
            gmail_thread_id=thread_id,
            notes_doc_id=notes_doc_id,
            transcript_doc_id=transcript_doc_id,
            received_at=received_at,
        )
        partial_source = source
        content = MeetingContent(
            notes_markdown=notes_md,
            transcript_markdown=transcript_md,
            summary_block=summary,
            title=fallback_title,
            meeting_datetime=meeting_dt,
        )

        classification = classifier.classify(fallback_title, summary, projects)
        classification = apply_threshold(classification, settings.confidence_threshold)
        partial_classification = classification
        log.info(
            "classified",
            receipt_id=receipt_id,
            slug=classification.project_slug,
            confidence=classification.confidence,
        )

        project_obj = next(
            (p for p in projects if p.slug == classification.project_slug), None
        )
        title, people = enricher.extract_title_and_people(
            notes_md, transcript_md, subject, project_obj
        )
        log.info("enriched_title_people", receipt_id=receipt_id, title=title, people=people)

        transcript_raw = transcript_md or _extract_transcription_section(notes_md)
        clean = enricher.clean_transcript(transcript_raw, people) if transcript_raw.strip() else ""
        executive = enricher.executive_summary(notes_md, clean, title, project_obj, people)

        enrichment = Enrichment(
            title_descriptive=title,
            people=people,
            transcript_clean_markdown=clean,
            executive_markdown=executive,
        )
        partial_enrichment = enrichment

        bundle = render(content, classification, enrichment, source)
        artifact_hashes = {a.kind: sha256_hex(a.content) for a in bundle.artifacts}
        folder_path = "/".join(bundle.folder_path_parts)

        receipt = Receipt(
            receipt_id=receipt_id,
            created_at=datetime.now(timezone.utc),
            source=source,
            folder_path=folder_path,
            classification=classification,
            enrichment=enrichment,
            artifact_hashes=artifact_hashes,
            status="rendered",
            dry_run=settings.dry_run,
        )

        if settings.dry_run:
            _write_preview(bundle, receipt_id, settings.data_dir)
            log.info("dry_run_preview_written", receipt_id=receipt_id, folder=folder_path)
        else:
            drive_folder_id, drive_file_ids = _publish_drive(drive, bundle, settings)
            github_file_shas = _publish_github(github, bundle)
            gmail.add_label(message_id, settings.label_processed)
            gmail.remove_label(message_id, settings.label_pending)
            receipt = receipt.model_copy(
                update={
                    "drive_folder_id": drive_folder_id,
                    "drive_file_ids": drive_file_ids,
                    "github_file_shas": github_file_shas,
                    "status": "published",
                }
            )

        receipts.write_receipt(receipt, receipts_dir)
        log.info("processing_done", receipt_id=receipt_id, status=receipt.status)
        return receipt

    except Exception as exc:
        err = f"{type(exc).__name__}: {exc}\n{traceback.format_exc()}"
        log.error("processing_failed", receipt_id=receipt_id, message_id=message_id, error=str(exc))
        failed = _build_failure_receipt(
            receipt_id,
            message_id,
            err,
            settings.dry_run,
            partial_source=partial_source,
            partial_classification=partial_classification,
            partial_enrichment=partial_enrichment,
        )
        receipts.write_receipt(failed, receipts_dir)
        if not settings.dry_run:
            try:
                gmail.add_label(message_id, settings.label_failed)
                send_failure_alert(
                    gmail,
                    to=settings.alert_email_to,
                    subject_prefix="[meet-ninja] falha:",
                    gmail_message_id=message_id,
                    error=err,
                )
            except Exception as alert_exc:
                log.error("alert_failed", error=str(alert_exc))
        return failed


def _publish_drive(
    drive: DriveClient,
    bundle: RenderedBundle,
    settings: Settings,
) -> tuple[str, dict[str, str]]:
    parent = settings.drive_root_folder_id
    for part in bundle.folder_path_parts:
        parent = drive.find_or_create_folder(part, parent)
    file_ids: dict[str, str] = {}
    for artifact in bundle.artifacts:
        file_id = drive.upload_markdown(artifact.filename, artifact.content, parent)
        file_ids[artifact.kind] = file_id
    return parent, file_ids


def _publish_github(
    github: GitHubClient,
    bundle: RenderedBundle,
) -> dict[str, str]:
    base = "/".join(bundle.folder_path_parts)
    shas: dict[str, str] = {}
    for artifact in bundle.artifacts:
        path = f"meetings/{base}/{artifact.filename}"
        msg = f"meet-ninja: add {artifact.filename} ({base})"
        shas[artifact.kind] = github.put_file(path, artifact.content, msg)
    return shas


def _write_preview(bundle: RenderedBundle, receipt_id: str, data_dir: Path) -> None:
    preview_dir = data_dir / "previews"
    for part in bundle.folder_path_parts:
        preview_dir = preview_dir / part
    preview_dir.mkdir(parents=True, exist_ok=True)
    for artifact in bundle.artifacts:
        (preview_dir / artifact.filename).write_text(artifact.content, encoding="utf-8")


def _build_failure_receipt(
    receipt_id: str,
    message_id: str,
    error: str,
    dry_run: bool,
    partial_source: Optional[MeetingSource] = None,
    partial_classification: Optional[Classification] = None,
    partial_enrichment: Optional[Enrichment] = None,
) -> Receipt:
    source = partial_source or MeetingSource(
        gmail_message_id=message_id,
        gmail_thread_id="",
        notes_doc_id="",
        received_at=datetime.now(timezone.utc),
    )
    classification = partial_classification or Classification(
        project_slug="unknown", confidence=0.0, reasoning="failed before classification"
    )
    return Receipt(
        receipt_id=receipt_id,
        created_at=datetime.now(timezone.utc),
        source=source,
        classification=classification,
        enrichment=partial_enrichment,
        status="failed",
        error=error,
        dry_run=dry_run,
    )


def _parse_received_at(date_header: str) -> datetime:
    if not date_header:
        return datetime.now(timezone.utc)
    try:
        dt = parsedate_to_datetime(date_header)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return datetime.now(timezone.utc)
