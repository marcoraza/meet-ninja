import json
from typing import Optional

from google import genai
from google.genai import types

from src.core.contracts import Classification, Project


_SYSTEM_INSTRUCTION = (
    "Você classifica reuniões em projetos. Dado o título e um resumo da reunião, "
    "escolha o slug do projeto mais provável dentre a lista canônica. "
    "Se nenhum projeto encaixar com confiança razoável, retorne slug='unknown' "
    "com confidence baixo. Sempre retorne JSON estrito conforme schema."
)


_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "project_slug": {"type": "string"},
        "confidence": {"type": "number"},
        "reasoning": {"type": "string"},
    },
    "required": ["project_slug", "confidence", "reasoning"],
}


class GeminiClassifier:
    def __init__(self, api_key: str, model: str):
        self._client = genai.Client(api_key=api_key)
        self._model = model

    def classify(
        self,
        title: str,
        summary: str,
        projects: list[Project],
    ) -> Classification:
        catalog = _format_catalog(projects)
        prompt = (
            f"PROJETOS DISPONÍVEIS:\n{catalog}\n\n"
            f"TÍTULO DA REUNIÃO: {title}\n\n"
            f"RESUMO DA REUNIÃO:\n{summary}\n\n"
            "Retorne JSON com project_slug, confidence (0.0-1.0) e reasoning curto."
        )
        response = self._client.models.generate_content(
            model=self._model,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=_SYSTEM_INSTRUCTION,
                response_mime_type="application/json",
                response_schema=_RESPONSE_SCHEMA,
                temperature=0.0,
            ),
        )
        raw = response.text or "{}"
        data = json.loads(raw)
        return Classification(
            project_slug=str(data.get("project_slug", "unknown")).strip() or "unknown",
            confidence=float(data.get("confidence", 0.0)),
            reasoning=str(data.get("reasoning", "")).strip(),
        )


def _format_catalog(projects: list[Project]) -> str:
    lines = []
    for p in projects:
        aliases = ", ".join(p.aliases) if p.aliases else ""
        desc = p.description.strip()
        line = f"- slug: {p.slug}\n  name: {p.name}"
        if aliases:
            line += f"\n  aliases: {aliases}"
        if desc:
            line += f"\n  description: {desc}"
        lines.append(line)
    lines.append("- slug: unknown\n  name: (não identificado)")
    return "\n".join(lines)


def apply_threshold(c: Classification, threshold: float) -> Classification:
    if c.confidence < threshold:
        return Classification(
            project_slug="unknown",
            confidence=c.confidence,
            reasoning=f"Below threshold {threshold}: {c.reasoning}",
        )
    return c
