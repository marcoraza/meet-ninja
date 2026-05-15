import json
import logging
import sys
from pathlib import Path

import click
import structlog

from src.core.config import load_settings
from src.core.workflow import run as run_workflow


def _setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(message)s", stream=sys.stderr)
    structlog.configure(
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(level),
    )


@click.group()
def cli() -> None:
    """meet-ninja CLI."""


@cli.command()
@click.option("--dry-run/--live", default=None, help="Override MEET_NINJA_DRY_RUN.")
@click.option("--limit", default=25, type=int, help="Max messages to process.")
@click.option("-v", "--verbose", is_flag=True)
def process(dry_run: bool | None, limit: int, verbose: bool) -> None:
    """Process pending meetings from Gmail."""
    _setup_logging(verbose)
    settings = load_settings()
    if dry_run is not None:
        from dataclasses import replace
        settings = replace(settings, dry_run=dry_run)
    click.echo(f"meet-ninja: dry_run={settings.dry_run} limit={limit}", err=True)
    receipts = run_workflow(settings, limit=limit)
    summary = {
        "total": len(receipts),
        "by_status": _count_by(receipts, "status"),
        "by_slug": _count_by_slug(receipts),
        "dry_run": settings.dry_run,
    }
    click.echo(json.dumps(summary, indent=2))


@cli.command()
def doctor() -> None:
    """Show resolved config and verify env."""
    settings = load_settings()
    info = {
        "env": settings.env,
        "dry_run": settings.dry_run,
        "data_dir": str(settings.data_dir),
        "sa_file_exists": Path(settings.sa_file).exists(),
        "delegated_user": settings.delegated_user,
        "drive_root_folder_id": settings.drive_root_folder_id,
        "gemini_model": settings.gemini_model,
        "confidence_threshold": settings.confidence_threshold,
        "github_repo": settings.github_repo,
        "github_projects_yaml_path": settings.github_projects_yaml_path,
        "alert_email_to": settings.alert_email_to,
        "gemini_api_key_set": bool(settings.gemini_api_key),
        "github_token_set": bool(settings.github_token),
        "email_query": settings.email_query,
    }
    click.echo(json.dumps(info, indent=2))


def _count_by(items, attr):
    out: dict[str, int] = {}
    for it in items:
        v = getattr(it, attr)
        out[v] = out.get(v, 0) + 1
    return out


def _count_by_slug(items):
    out: dict[str, int] = {}
    for it in items:
        slug = it.classification.project_slug
        out[slug] = out.get(slug, 0) + 1
    return out


if __name__ == "__main__":
    cli()
