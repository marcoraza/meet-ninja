import base64
import re
from typing import Optional
from email.mime.text import MIMEText

from googleapiclient.discovery import build


_DOC_ID_PATTERN = re.compile(r"https://docs\.google\.com/document/d/([a-zA-Z0-9_-]+)")


class GmailClient:
    def __init__(self, credentials):
        self._service = build("gmail", "v1", credentials=credentials, cache_discovery=False)

    def search(self, query: str, max_results: int = 25) -> list[str]:
        resp = self._service.users().messages().list(
            userId="me", q=query, maxResults=max_results
        ).execute()
        return [m["id"] for m in resp.get("messages", [])]

    def get_message(self, message_id: str) -> dict:
        return self._service.users().messages().get(
            userId="me", id=message_id, format="full"
        ).execute()

    def get_header(self, message: dict, name: str) -> Optional[str]:
        for h in message.get("payload", {}).get("headers", []):
            if h["name"].lower() == name.lower():
                return h["value"]
        return None

    def get_body_text(self, message: dict) -> str:
        return _walk_parts_for_text(message.get("payload", {}))

    def extract_doc_ids(self, message: dict) -> list[str]:
        body = self.get_body_text(message)
        return list(dict.fromkeys(_DOC_ID_PATTERN.findall(body)))

    def ensure_label(self, name: str) -> str:
        existing = self._service.users().labels().list(userId="me").execute()
        for lbl in existing.get("labels", []):
            if lbl["name"] == name:
                return lbl["id"]
        created = self._service.users().labels().create(
            userId="me",
            body={"name": name, "labelListVisibility": "labelShow", "messageListVisibility": "show"},
        ).execute()
        return created["id"]

    def add_label(self, message_id: str, label_name: str) -> None:
        label_id = self.ensure_label(label_name)
        self._service.users().messages().modify(
            userId="me", id=message_id, body={"addLabelIds": [label_id]}
        ).execute()

    def remove_label(self, message_id: str, label_name: str) -> None:
        label_id = self.ensure_label(label_name)
        self._service.users().messages().modify(
            userId="me", id=message_id, body={"removeLabelIds": [label_id]}
        ).execute()

    def send(self, to: str, subject: str, body: str) -> None:
        msg = MIMEText(body)
        msg["to"] = to
        msg["subject"] = subject
        raw = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        self._service.users().messages().send(userId="me", body={"raw": raw}).execute()


def _walk_parts_for_text(part: dict) -> str:
    mime = part.get("mimeType", "")
    body = part.get("body", {})
    data = body.get("data")
    if data and mime.startswith("text/"):
        return base64.urlsafe_b64decode(data).decode("utf-8", errors="replace")
    chunks = []
    for sub in part.get("parts", []):
        chunks.append(_walk_parts_for_text(sub))
    return "\n".join(c for c in chunks if c)
