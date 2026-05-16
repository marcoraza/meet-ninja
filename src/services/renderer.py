import hashlib
import re
import unicodedata
from datetime import datetime
from typing import Optional

from src.core.contracts import (
    Classification,
    Enrichment,
    MeetingContent,
    MeetingSource,
    RenderedArtifact,
    RenderedBundle,
)


_PT_MONTHS = {
    1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
    5: "maio", 6: "junho", 7: "julho", 8: "agosto",
    9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro",
}


_FS_RESERVED = re.compile(r"[\\/:*?\"<>|]")


def sanitize_for_path(text: str, max_len: int = 80) -> str:
    """Limpa um texto pra usar como nome de arquivo/pasta, mantendo acentos e capitalização."""
    text = text.replace("/", "-").replace("\\", "-")
    text = _FS_RESERVED.sub("", text)
    text = re.sub(r"\s+", " ", text).strip()
    text = text.strip(". ")
    if len(text) > max_len:
        text = text[:max_len].rstrip(" -")
    return text or "Sem título"


def slugify_ascii(text: str, max_len: int = 60) -> str:
    """Slug ASCII pra fallback técnico (não usado nas pastas legíveis)."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if len(text) > max_len:
        text = text[:max_len].rstrip("-")
    return text or "untitled"


def month_folder(meeting_dt: datetime) -> str:
    return f"{meeting_dt.month:02d}-{_PT_MONTHS[meeting_dt.month]}"


def meeting_folder_name(meeting_dt: datetime, title_descriptive: str, people: list[str]) -> str:
    day = f"{meeting_dt.day:02d}"
    title = sanitize_for_path(title_descriptive, max_len=50)
    if people:
        head = people[:3]
        people_str = ", ".join(head)
        if len(people) > 3:
            people_str += f" +{len(people) - 3}"
        people_str = sanitize_for_path(people_str, max_len=40)
        return sanitize_for_path(f"{day} - {title} - {people_str}", max_len=100)
    return sanitize_for_path(f"{day} - {title}", max_len=100)


def _yaml_escape(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def _frontmatter(
    kind: str,
    classification: Classification,
    enrichment: Enrichment,
    source: MeetingSource,
    content: MeetingContent,
) -> str:
    when = content.meeting_datetime or source.received_at
    lines = [
        "---",
        f"kind: {kind}",
        f"project: {classification.project_slug}",
        f"confidence: {classification.confidence:.2f}",
        f"title: {_yaml_escape(enrichment.title_descriptive)}",
        f"meeting_datetime: {when.isoformat()}",
        f"people: [{', '.join(_yaml_escape(p) for p in enrichment.people)}]",
        f"gmail_message_id: {source.gmail_message_id}",
        f"gmail_thread_id: {source.gmail_thread_id}",
        f"notes_doc_id: {source.notes_doc_id}",
    ]
    if source.transcript_doc_id:
        lines.append(f"transcript_doc_id: {source.transcript_doc_id}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def _render_sumario(
    content: MeetingContent,
    classification: Classification,
    enrichment: Enrichment,
    source: MeetingSource,
) -> str:
    fm = _frontmatter("sumario", classification, enrichment, source, content)
    body_parts = [f"# {enrichment.title_descriptive}\n"]
    if enrichment.people:
        body_parts.append(f"**Participantes:** {', '.join(enrichment.people)}\n")
    body_parts.append(content.notes_markdown.strip())
    return fm + "\n".join(body_parts).strip() + "\n"


def _render_executivo(
    content: MeetingContent,
    classification: Classification,
    enrichment: Enrichment,
    source: MeetingSource,
) -> str:
    fm = _frontmatter("executivo", classification, enrichment, source, content)
    body = (
        f"# Executivo: {enrichment.title_descriptive}\n\n"
        f"**Projeto:** {classification.project_slug}  \n"
        f"**Participantes:** {', '.join(enrichment.people) or 'não identificados'}  \n"
        f"**Data:** {(content.meeting_datetime or source.received_at).strftime('%d/%m/%Y %H:%M')}\n\n"
        f"{enrichment.executive_markdown.strip()}\n"
    )
    return fm + body


def _render_transcricao_clean(
    content: MeetingContent,
    classification: Classification,
    enrichment: Enrichment,
    source: MeetingSource,
) -> str:
    fm = _frontmatter("transcricao-clean", classification, enrichment, source, content)
    body = (
        f"# Transcrição (limpa): {enrichment.title_descriptive}\n\n"
        f"**Participantes:** {', '.join(enrichment.people) or 'não identificados'}\n\n"
        f"{enrichment.transcript_clean_markdown.strip()}\n"
    )
    return fm + body


def _render_transcricao_bruta(
    content: MeetingContent,
    classification: Classification,
    enrichment: Enrichment,
    source: MeetingSource,
) -> str:
    fm = _frontmatter("transcricao-bruta", classification, enrichment, source, content)
    raw = content.transcript_markdown or _extract_transcription_section(content.notes_markdown)
    body = (
        f"# Transcrição (bruta): {enrichment.title_descriptive}\n\n"
        f"{raw.strip()}\n"
    )
    return fm + body


_TRANSCRIPT_HEADER = re.compile(r"^#\s+.*Transcri[çc][ãa]o", re.MULTILINE)


def _extract_transcription_section(notes_markdown: str) -> str:
    """Extrai o bloco de transcrição do doc do Gemini (após '# 📖 Transcrição')."""
    match = _TRANSCRIPT_HEADER.search(notes_markdown)
    if not match:
        return ""
    return notes_markdown[match.end():].strip()


def render(
    content: MeetingContent,
    classification: Classification,
    enrichment: Enrichment,
    source: MeetingSource,
) -> RenderedBundle:
    when = content.meeting_datetime or source.received_at
    folder_parts = [
        classification.project_slug or "unknown",
        month_folder(when),
        meeting_folder_name(when, enrichment.title_descriptive, enrichment.people),
    ]
    artifacts = [
        RenderedArtifact(
            filename="executivo.md",
            kind="executivo",
            content=_render_executivo(content, classification, enrichment, source),
        ),
        RenderedArtifact(
            filename="sumario.md",
            kind="sumario",
            content=_render_sumario(content, classification, enrichment, source),
        ),
        RenderedArtifact(
            filename="transcricao-clean.md",
            kind="transcricao-clean",
            content=_render_transcricao_clean(content, classification, enrichment, source),
        ),
        RenderedArtifact(
            filename="transcricao-bruta.md",
            kind="transcricao-bruta",
            content=_render_transcricao_bruta(content, classification, enrichment, source),
        ),
    ]
    return RenderedBundle(folder_path_parts=folder_parts, artifacts=artifacts)


def sha256_hex(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()
