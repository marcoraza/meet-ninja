import re
from datetime import datetime
from typing import Optional


_DOC_ID = re.compile(r"https://docs\.google\.com/document/d/([a-zA-Z0-9_-]+)")
_DATE_PT = re.compile(
    r"(\d{1,2}) de (jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)[a-zç.]*\s*"
    r"de\s+(\d{4})(?:\s*[àa]s\s*(\d{1,2}):(\d{2}))?",
    re.IGNORECASE,
)
_PT_MONTH = {
    "jan": 1, "fev": 2, "mar": 3, "abr": 4, "mai": 5, "jun": 6,
    "jul": 7, "ago": 8, "set": 9, "out": 10, "nov": 11, "dez": 12,
}


def extract_transcript_doc_id(notes_markdown: str, notes_doc_id: str) -> Optional[str]:
    for match in _DOC_ID.findall(notes_markdown):
        if match != notes_doc_id:
            return match
    return None


def extract_title(notes_markdown: str, gmail_subject: Optional[str]) -> str:
    for line in notes_markdown.splitlines():
        s = line.strip()
        if s.startswith("## "):
            return s[3:].strip()
    if gmail_subject:
        return gmail_subject.strip()
    return "Reunião sem título"


def extract_meeting_datetime(notes_markdown: str) -> Optional[datetime]:
    match = _DATE_PT.search(notes_markdown)
    if not match:
        return None
    day = int(match.group(1))
    month = _PT_MONTH.get(match.group(2).lower()[:3])
    year = int(match.group(3))
    hour = int(match.group(4)) if match.group(4) else 0
    minute = int(match.group(5)) if match.group(5) else 0
    if not month:
        return None
    try:
        return datetime(year, month, day, hour, minute)
    except ValueError:
        return None


def extract_summary_block(notes_markdown: str) -> str:
    lines = notes_markdown.splitlines()
    out: list[str] = []
    capturing = False
    for line in lines:
        s = line.strip()
        if s.startswith("### "):
            heading = s[4:].strip().lower()
            if heading.startswith("resumo"):
                capturing = True
                continue
            if capturing:
                break
        if capturing:
            out.append(line)
    return "\n".join(out).strip()
