from pathlib import Path
from google.oauth2 import service_account

SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/drive",
]


def build_credentials(sa_file: Path, delegated_user: str):
    creds = service_account.Credentials.from_service_account_file(
        str(sa_file), scopes=SCOPES
    )
    return creds.with_subject(delegated_user)
