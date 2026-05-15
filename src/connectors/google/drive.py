import io
from typing import Optional

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload


class DriveClient:
    def __init__(self, credentials):
        self._service = build("drive", "v3", credentials=credentials, cache_discovery=False)

    def export_doc_as_markdown(self, file_id: str) -> str:
        data = self._service.files().export(
            fileId=file_id, mimeType="text/markdown"
        ).execute()
        if isinstance(data, bytes):
            return data.decode("utf-8", errors="replace")
        return data

    def get_file_metadata(self, file_id: str) -> dict:
        return self._service.files().get(
            fileId=file_id,
            fields="id,name,mimeType,createdTime,modifiedTime,parents",
            supportsAllDrives=True,
        ).execute()

    def find_folder(self, name: str, parent_id: str) -> Optional[str]:
        safe_name = name.replace("'", "\\'")
        query = (
            f"name = '{safe_name}' and "
            f"'{parent_id}' in parents and "
            f"mimeType = 'application/vnd.google-apps.folder' and "
            f"trashed = false"
        )
        resp = self._service.files().list(
            q=query,
            fields="files(id,name)",
            includeItemsFromAllDrives=True,
            supportsAllDrives=True,
        ).execute()
        files = resp.get("files", [])
        return files[0]["id"] if files else None

    def find_or_create_folder(self, name: str, parent_id: str) -> str:
        existing = self.find_folder(name, parent_id)
        if existing:
            return existing
        created = self._service.files().create(
            body={
                "name": name,
                "mimeType": "application/vnd.google-apps.folder",
                "parents": [parent_id],
            },
            fields="id",
            supportsAllDrives=True,
        ).execute()
        return created["id"]

    def upload_markdown(self, filename: str, content: str, parent_id: str) -> str:
        media = MediaIoBaseUpload(
            io.BytesIO(content.encode("utf-8")),
            mimetype="text/markdown",
            resumable=False,
        )
        created = self._service.files().create(
            body={"name": filename, "parents": [parent_id]},
            media_body=media,
            fields="id",
            supportsAllDrives=True,
        ).execute()
        return created["id"]
