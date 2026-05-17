import base64
from typing import Optional

import requests
import yaml

from src.core.contracts import Project


_API = "https://api.github.com"


class GitHubClient:
    def __init__(self, token: str, repo: str):
        self._repo = repo
        self._session = requests.Session()
        self._session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            }
        )

    def get_file(self, path: str, ref: str = "main") -> Optional[dict]:
        url = f"{_API}/repos/{self._repo}/contents/{path}"
        resp = self._session.get(url, params={"ref": ref}, timeout=30)
        if resp.status_code == 404:
            return None
        resp.raise_for_status()
        return resp.json()

    def read_text(self, path: str, ref: str = "main") -> Optional[str]:
        meta = self.get_file(path, ref=ref)
        if not meta:
            return None
        content_b64 = meta.get("content", "")
        return base64.b64decode(content_b64).decode("utf-8")

    def load_projects(self, projects_yaml_path: str) -> list[Project]:
        raw = self.read_text(projects_yaml_path)
        if not raw:
            raise RuntimeError(
                f"projects.yaml not found in {self._repo}:{projects_yaml_path}"
            )
        data = yaml.safe_load(raw) or []
        return [Project(**item) for item in data]

    def list_dir(self, path: str, ref: str = "main") -> list[dict]:
        url = f"{_API}/repos/{self._repo}/contents/{path}"
        resp = self._session.get(url, params={"ref": ref}, timeout=30)
        if resp.status_code == 404:
            return []
        resp.raise_for_status()
        data = resp.json()
        return data if isinstance(data, list) else []

    def put_file(
        self,
        path: str,
        content: str,
        message: str,
        branch: str = "main",
    ) -> str:
        existing = self.get_file(path, ref=branch)
        body = {
            "message": message,
            "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
            "branch": branch,
        }
        if existing:
            body["sha"] = existing["sha"]
        url = f"{_API}/repos/{self._repo}/contents/{path}"
        resp = self._session.put(url, json=body, timeout=30)
        resp.raise_for_status()
        return resp.json()["content"]["sha"]
