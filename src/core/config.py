import os
from pathlib import Path
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    env: str
    data_dir: Path
    dry_run: bool

    sa_file: Path
    delegated_user: str

    email_query: str
    label_pending: str
    label_processed: str
    label_failed: str

    drive_root_folder_id: str

    gemini_api_key: str
    gemini_model: str
    confidence_threshold: float

    github_token: str
    github_repo: str
    github_projects_yaml_path: str

    alert_email_to: str


def _required(key: str) -> str:
    value = os.environ.get(key, "").strip()
    if not value:
        raise RuntimeError(f"Missing required env var: {key}")
    return value


def load_settings() -> Settings:
    return Settings(
        env=os.environ.get("MEET_NINJA_ENV", "local"),
        data_dir=Path(os.environ.get("MEET_NINJA_DATA_DIR", "./data")).resolve(),
        dry_run=os.environ.get("MEET_NINJA_DRY_RUN", "true").lower() == "true",
        sa_file=Path(_required("GOOGLE_SERVICE_ACCOUNT_FILE")).resolve(),
        delegated_user=_required("GOOGLE_DELEGATED_USER"),
        email_query=_required("MEET_NINJA_EMAIL_QUERY"),
        label_pending=os.environ.get("MEET_NINJA_LABEL_PENDING", "meet-pending"),
        label_processed=os.environ.get("MEET_NINJA_LABEL_PROCESSED", "meet-processed"),
        label_failed=os.environ.get("MEET_NINJA_LABEL_FAILED", "meet-failed"),
        drive_root_folder_id=_required("DRIVE_ROOT_FOLDER_ID"),
        gemini_api_key=os.environ.get("GEMINI_API_KEY", ""),
        gemini_model=os.environ.get("GEMINI_MODEL", "gemini-3.1-flash-lite"),
        confidence_threshold=float(os.environ.get("CLASSIFICATION_CONFIDENCE_THRESHOLD", "0.7")),
        github_token=os.environ.get("GITHUB_TOKEN", ""),
        github_repo=_required("GITHUB_REPO"),
        github_projects_yaml_path=os.environ.get("GITHUB_PROJECTS_YAML_PATH", "projects.yaml"),
        alert_email_to=_required("ALERT_EMAIL_TO"),
    )
