from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field


class Project(BaseModel):
    slug: str
    name: str
    aliases: list[str] = []
    description: str = ""


class MeetingSource(BaseModel):
    gmail_message_id: str
    gmail_thread_id: str
    notes_doc_id: str
    transcript_doc_id: Optional[str] = None
    received_at: datetime


class MeetingContent(BaseModel):
    notes_markdown: str
    transcript_markdown: Optional[str] = None
    summary_block: str
    title: str
    meeting_datetime: Optional[datetime] = None


class Classification(BaseModel):
    project_slug: str
    confidence: float = Field(ge=0.0, le=1.0)
    reasoning: str = ""


class RenderedOutput(BaseModel):
    notes_filename: str
    transcript_filename: str
    notes_content: str
    transcript_content: str


class Receipt(BaseModel):
    receipt_id: str
    created_at: datetime
    source: MeetingSource
    notes_hash: str
    transcript_hash: Optional[str] = None
    classification: Classification
    drive_notes_id: Optional[str] = None
    drive_transcript_id: Optional[str] = None
    github_notes_sha: Optional[str] = None
    github_transcript_sha: Optional[str] = None
    status: Literal["pending", "classified", "rendered", "published", "failed"] = "pending"
    error: Optional[str] = None
    dry_run: bool = True
