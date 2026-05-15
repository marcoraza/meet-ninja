import hashlib
import re
import unicodedata
from datetime import datetime
from typing import Optional

from src.core.contracts import (
    Classification,
    MeetingContent,
    MeetingSource,
    RenderedOutput,
)


def slugify(text: str, max_len: int = 60) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if len(text) > max_len:
        text = text[:max_len].rstrip("-")
    return text or "untitled"


def build_filenames(
    meeting_date: Optional[datetime],
    title: str,
    received_at: datetime,
) -> tuple[str, str]:
    when = meeting_date or received_at
    date_str = when.strftime("%Y-%m-%d")
    slug = slugify(title)
    base = f"{date_str}_{slug}"
    return f"{base}__notes.md", f"{base}__transcript.md"


def _frontmatter(
    classification: Classification,
    source: MeetingSource,
    content: MeetingContent,
    kind: str,
) -> str:
    when = content.meeting_datetime or source.received_at
    lines = [
        "---",
        f"kind: {kind}",
        f"project: {classification.project_slug}",
        f"confidence: {classification.confidence:.2f}",
        f"title: {_yaml_escape(content.title)}",
        f"meeting_datetime: {when.isoformat()}",
        f"gmail_message_id: {source.gmail_message_id}",
        f"gmail_thread_id: {source.gmail_thread_id}",
        f"notes_doc_id: {source.notes_doc_id}",
    ]
    if source.transcript_doc_id:
        lines.append(f"transcript_doc_id: {source.transcript_doc_id}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def _yaml_escape(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def render(
    content: MeetingContent,
    classification: Classification,
    source: MeetingSource,
) -> RenderedOutput:
    notes_filename, transcript_filename = build_filenames(
        content.meeting_datetime, content.title, source.received_at
    )
    notes_body = _frontmatter(classification, source, content, "notes") + content.notes_markdown
    transcript_body = ""
    if content.transcript_markdown:
        transcript_body = (
            _frontmatter(classification, source, content, "transcript")
            + content.transcript_markdown
        )
    return RenderedOutput(
        notes_filename=notes_filename,
        transcript_filename=transcript_filename,
        notes_content=notes_body,
        transcript_content=transcript_body,
    )


def sha256_hex(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()
