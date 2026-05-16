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


class Enrichment(BaseModel):
    title_descriptive: str
    people: list[str] = []
    transcript_clean_markdown: str = ""
    executive_markdown: str = ""


class RenderedArtifact(BaseModel):
    filename: str
    content: str
    kind: Literal["sumario", "executivo", "transcricao-clean", "transcricao-bruta"]


class RenderedBundle(BaseModel):
    folder_path_parts: list[str]
    artifacts: list[RenderedArtifact]


class Receipt(BaseModel):
    receipt_id: str
    created_at: datetime
    source: MeetingSource
    folder_path: str = ""
    classification: Classification
    enrichment: Optional[Enrichment] = None
    artifact_hashes: dict[str, str] = {}
    drive_folder_id: Optional[str] = None
    drive_file_ids: dict[str, str] = {}
    github_file_shas: dict[str, str] = {}
    status: Literal["pending", "classified", "rendered", "published", "failed"] = "pending"
    error: Optional[str] = None
    dry_run: bool = True
