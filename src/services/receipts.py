import json
import uuid
from datetime import datetime
from pathlib import Path

from src.core.contracts import Receipt


def new_receipt_id() -> str:
    return f"r-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}"


def write_receipt(receipt: Receipt, base_dir: Path) -> Path:
    base_dir.mkdir(parents=True, exist_ok=True)
    path = base_dir / f"{receipt.receipt_id}.json"
    path.write_text(receipt.model_dump_json(indent=2), encoding="utf-8")
    return path
