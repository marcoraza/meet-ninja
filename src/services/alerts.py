from src.connectors.google.gmail import GmailClient


def send_failure_alert(
    gmail: GmailClient,
    to: str,
    subject_prefix: str,
    gmail_message_id: str,
    error: str,
) -> None:
    subject = f"{subject_prefix} {gmail_message_id}"
    body = (
        f"Falha ao processar mensagem do Gmail.\n\n"
        f"message_id: {gmail_message_id}\n"
        f"error:\n{error}\n"
    )
    gmail.send(to=to, subject=subject, body=body)
