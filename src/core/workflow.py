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
    MeetingContent,
    MeetingSource,
    Project,
    Receipt,
    RenderedOutput,
)
from src.services import parser, receipts
from src.services.alerts import send_failure_alert
from src.services.classifier import GeminiClassifier, apply_threshold
from src.services.renderer import render, sha256_hex


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
    receipts_dir = settings.data_dir / "receipts"

    message_ids = gmail.search(settings.email_query, max_results=limit)
    log.info("messages_found", count=len(message_ids), query=settings.email_query)

    out: list[Receipt] = []
    for mid in message_ids:
        receipt = _process_one(
            mid, gmail, drive, github, classifier, projects, settings, receipts_dir
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
    projects: list[Project],
    settings: Settings,
    receipts_dir: Path,
) -> Receipt:
    receipt_id = receipts.new_receipt_id()
    log.info("processing_start", receipt_id=receipt_id, message_id=message_id)

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

        title = parser.extract_title(notes_md, subject)
        meeting_dt = parser.extract_meeting_datetime(notes_md)
        summary = parser.extract_summary_block(notes_md) or notes_md[:2000]

        source = MeetingSource(
            gmail_message_id=message_id,
            gmail_thread_id=thread_id,
            notes_doc_id=notes_doc_id,
            transcript_doc_id=transcript_doc_id,
            received_at=received_at,
        )
        content = MeetingContent(
            notes_markdown=notes_md,
            transcript_markdown=transcript_md,
            summary_block=summary,
            title=title,
            meeting_datetime=meeting_dt,
        )

        classification = classifier.classify(title, summary, projects)
        classification = apply_threshold(classification, settings.confidence_threshold)
        log.info(
            "classified",
            receipt_id=receipt_id,
            slug=classification.project_slug,
            confidence=classification.confidence,
        )

        rendered = render(content, classification, source)
        notes_hash = sha256_hex(rendered.notes_content)
        transcript_hash = sha256_hex(rendered.transcript_content) if rendered.transcript_content else None

        receipt = Receipt(
            receipt_id=receipt_id,
            created_at=datetime.now(timezone.utc),
            source=source,
            notes_hash=notes_hash,
            transcript_hash=transcript_hash,
            classification=classification,
            status="rendered",
            dry_run=settings.dry_run,
        )

        if settings.dry_run:
            _write_preview(rendered, receipt_id, settings.data_dir)
            log.info("dry_run_preview_written", receipt_id=receipt_id)
        else:
            drive_notes_id, drive_transcript_id = _publish_drive(drive, rendered, classification, settings)
            gh_notes_sha, gh_transcript_sha = _publish_github(github, rendered, classification)
            gmail.add_label(message_id, settings.label_processed)
            gmail.remove_label(message_id, settings.label_pending)
            receipt = receipt.model_copy(
                update={
                    "drive_notes_id": drive_notes_id,
                    "drive_transcript_id": drive_transcript_id,
                    "github_notes_sha": gh_notes_sha,
                    "github_transcript_sha": gh_transcript_sha,
                    "status": "published",
                }
            )

        receipts.write_receipt(receipt, receipts_dir)
        log.info("processing_done", receipt_id=receipt_id, status=receipt.status)
        return receipt

    except Exception as exc:
        err = f"{type(exc).__name__}: {exc}\n{traceback.format_exc()}"
        log.error("processing_failed", receipt_id=receipt_id, message_id=message_id, error=str(exc))
        failed = _build_failure_receipt(receipt_id, message_id, err, settings.dry_run)
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
    rendered: RenderedOutput,
    classification: Classification,
    settings: Settings,
) -> tuple[Optional[str], Optional[str]]:
    folder_name = classification.project_slug or _UNKNOWN_SLUG
    project_folder = drive.find_or_create_folder(folder_name, settings.drive_root_folder_id)
    notes_id = drive.upload_markdown(rendered.notes_filename, rendered.notes_content, project_folder)
    transcript_id: Optional[str] = None
    if rendered.transcript_content:
        transcript_id = drive.upload_markdown(
            rendered.transcript_filename, rendered.transcript_content, project_folder
        )
    return notes_id, transcript_id


def _publish_github(
    github: GitHubClient,
    rendered: RenderedOutput,
    classification: Classification,
) -> tuple[Optional[str], Optional[str]]:
    slug = classification.project_slug or _UNKNOWN_SLUG
    notes_path = f"meetings/{slug}/{rendered.notes_filename}"
    msg = f"meet-ninja: add {rendered.notes_filename} ({slug})"
    notes_sha = github.put_file(notes_path, rendered.notes_content, msg)
    transcript_sha: Optional[str] = None
    if rendered.transcript_content:
        transcript_path = f"meetings/{slug}/{rendered.transcript_filename}"
        msg_t = f"meet-ninja: add {rendered.transcript_filename} ({slug})"
        transcript_sha = github.put_file(transcript_path, rendered.transcript_content, msg_t)
    return notes_sha, transcript_sha


def _write_preview(rendered: RenderedOutput, receipt_id: str, data_dir: Path) -> None:
    preview_dir = data_dir / "previews" / receipt_id
    preview_dir.mkdir(parents=True, exist_ok=True)
    (preview_dir / rendered.notes_filename).write_text(rendered.notes_content, encoding="utf-8")
    if rendered.transcript_content:
        (preview_dir / rendered.transcript_filename).write_text(
            rendered.transcript_content, encoding="utf-8"
        )


def _build_failure_receipt(receipt_id: str, message_id: str, error: str, dry_run: bool) -> Receipt:
    placeholder_source = MeetingSource(
        gmail_message_id=message_id,
        gmail_thread_id="",
        notes_doc_id="",
        received_at=datetime.now(timezone.utc),
    )
    placeholder_classification = Classification(
        project_slug="unknown", confidence=0.0, reasoning="failed before classification"
    )
    return Receipt(
        receipt_id=receipt_id,
        created_at=datetime.now(timezone.utc),
        source=placeholder_source,
        notes_hash="",
        classification=placeholder_classification,
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
