import json
from typing import Optional

from google import genai
from google.genai import types

from src.core.contracts import Project


_TITLE_PEOPLE_SYSTEM = (
    "Você analisa anotações e transcrição de uma reunião e extrai dois dados: "
    "(1) um título descritivo curto da reunião, em português, com capitalização "
    "correta (palavras importantes em maiúscula, artigos/preposições em minúscula). "
    "MÁXIMO 50 caracteres, sem ponto final, sem aspas, sem datas, sem horários. "
    "Frase nominal curta, foco no TEMA central da conversa. Prefira descrever a "
    "atividade (ex: 'Validação do Motor de Compliance') a nomear produtos.\n"
    "REGRA DE NOMES (estrita): NUNCA invente nome de produto ou variação. Se um "
    "nome canônico de projeto for fornecido, use exatamente como está, OU não "
    "mencione o produto e descreva só a atividade. Não derive 'Certifier' de "
    "'Certify' nem invente sufixos. Em dúvida, omita o nome do produto.\n"
    "(2) lista de pessoas reais que participaram, com primeiro nome ou nome curto. "
    "Renomeie 'Off Digital' para 'Marco'. Se o speaker aparecer só como 'Eu' ou "
    "'Speaker 1', omita. Use o nome real quando aparecer no diálogo. "
    "Responda em JSON estrito conforme schema."
)

_TITLE_PEOPLE_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "people": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["title", "people"],
}


_CLEAN_TRANSCRIPT_SYSTEM = (
    "Você reescreve a transcrição bruta de uma reunião em um formato turn-by-turn "
    "limpo e legível, como roteiro. Regras estritas:\n"
    "- Mantenha os timestamps no formato '### HH:MM:SS' no início de cada bloco.\n"
    "- Cada turno de fala em linha separada, com o speaker em negrito: '**Nome:** texto'.\n"
    "- Quebre blocos longos em sub-turnos lógicos por mudança de assunto, mantendo "
    "o mesmo timestamp do bloco original.\n"
    "- Renomeie 'Off Digital' para 'Marco'. Outros speakers, use o nome real "
    "quando o contexto permitir; senão mantenha o display name original.\n"
    "- Remova fillers e ruído: 'ahm', 'uhh', 'eh', 'tipo assim' isolado, repetições "
    "como 'testando, testando, testando', monossílabos perdidos ('M.'), confirmações "
    "vazias soltas ('uhum', 'aham').\n"
    "- Remova palavrões.\n"
    "- Corrija erros óbvios de transcrição (palavras claramente erradas pelo contexto).\n"
    "- NÃO resumir, NÃO interpretar, NÃO adicionar conteúdo. Preserve o que foi dito.\n"
    "- Pontue e capitalize corretamente em português.\n"
    "- Se identificar contexto fora da call (fala paralela com filhos, alguém de fora), "
    "remova esses trechos.\n"
    "Retorne markdown puro, começando pelo primeiro '### HH:MM:SS', sem cabeçalho extra."
)


_EXECUTIVE_SYSTEM = (
    "Você produz um resumo executivo de 1 página em markdown a partir das anotações "
    "e da transcrição limpa de uma reunião. Estrutura obrigatória, todas as seções "
    "presentes (use 'Nenhum.' se vazio):\n"
    "## Contexto\n"
    "Um a dois parágrafos: por que a reunião aconteceu e o que estava em jogo.\n\n"
    "## Decisões\n"
    "Bullets com decisões tomadas. Cada decisão começa com verbo no passado.\n\n"
    "## Ações\n"
    "Bullets no formato '- [ ] Ação (responsável: Nome, prazo: data ou \"sem prazo\")'.\n"
    "Só inclua ação que tenha responsável claro do diálogo.\n\n"
    "## Próximos passos\n"
    "Bullets com próximas reuniões, follow-ups, marcos de curto prazo.\n\n"
    "## Riscos e pendências\n"
    "Bullets com bloqueios, dúvidas em aberto, riscos identificados.\n\n"
    "Regras: tudo em português, frases curtas, sem repetir o que está em outra "
    "seção, sem marketing, sem floreio. Se a informação não está na fonte, "
    "não invente.\n"
    "REGRA DE NOMES (estrita): em qualquer menção (responsável de ação, "
    "narrativa do contexto, etc.) use sempre 'Marco' no lugar de 'Off Digital'. "
    "Nunca escreva 'Off Digital' no executivo. Use só os nomes da lista de "
    "PARTICIPANTES fornecida.\n"
    "Retorne só o markdown, sem cabeçalho extra."
)


_RETRY_OPTIONS = types.HttpRetryOptions(
    attempts=5,
    initial_delay=2.0,
    max_delay=30.0,
    exp_base=2.0,
    jitter=1.0,
)


class GeminiEnricher:
    def __init__(self, api_key: str, model: str):
        self._client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(retry_options=_RETRY_OPTIONS),
        )
        self._model = model

    def extract_title_and_people(
        self,
        notes_markdown: str,
        transcript_markdown: Optional[str],
        gmail_subject: str,
        project: Optional[Project] = None,
    ) -> tuple[str, list[str]]:
        transcript_excerpt = (transcript_markdown or "")[:8000]
        if project is not None:
            project_line = (
                f"NOME CANÔNICO DO PROJETO (use exatamente assim ou omita): "
                f"{project.name}\n\n"
            )
        else:
            project_line = "PROJETO: não identificado (não mencione produto no título)\n\n"
        prompt = (
            f"{project_line}"
            f"ASSUNTO ORIGINAL DO E-MAIL: {gmail_subject}\n\n"
            f"ANOTAÇÕES DA REUNIÃO:\n{notes_markdown[:6000]}\n\n"
            f"TRECHO DA TRANSCRIÇÃO:\n{transcript_excerpt}\n\n"
            "Extraia title (máx 50 chars, descritivo) e people (lista de nomes)."
        )
        response = self._client.models.generate_content(
            model=self._model,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=_TITLE_PEOPLE_SYSTEM,
                response_mime_type="application/json",
                response_schema=_TITLE_PEOPLE_SCHEMA,
                temperature=0.2,
            ),
        )
        data = json.loads(response.text or "{}")
        title = str(data.get("title", "")).strip() or "Reunião sem título"
        people = [str(p).strip() for p in data.get("people", []) if str(p).strip()]
        return title, people

    def clean_transcript(
        self,
        transcript_raw_markdown: str,
        people: list[str],
    ) -> str:
        people_hint = ", ".join(people) if people else "não identificados"
        prompt = (
            f"PARTICIPANTES CONHECIDOS: {people_hint}\n\n"
            f"TRANSCRIÇÃO BRUTA:\n{transcript_raw_markdown}\n\n"
            "Reescreva em formato turn-by-turn limpo conforme as regras."
        )
        response = self._client.models.generate_content(
            model=self._model,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=_CLEAN_TRANSCRIPT_SYSTEM,
                temperature=0.2,
            ),
        )
        return (response.text or "").strip()

    def executive_summary(
        self,
        notes_markdown: str,
        transcript_clean_markdown: str,
        title: str,
        project: Project | None,
        people: list[str],
    ) -> str:
        if project is not None:
            project_line = (
                f"PROJETO: {project.name} ({project.slug}). {project.description}"
            )
        else:
            project_line = "PROJETO: não identificado"
        people_line = "PARTICIPANTES: " + (", ".join(people) if people else "não identificados")
        prompt = (
            f"TÍTULO: {title}\n"
            f"{project_line}\n"
            f"{people_line}\n\n"
            f"ANOTAÇÕES BRUTAS DO GEMINI:\n{notes_markdown[:8000]}\n\n"
            f"TRANSCRIÇÃO LIMPA:\n{transcript_clean_markdown[:20000]}\n\n"
            "Produza o executivo em markdown conforme a estrutura."
        )
        response = self._client.models.generate_content(
            model=self._model,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=_EXECUTIVE_SYSTEM,
                temperature=0.2,
            ),
        )
        return (response.text or "").strip()
