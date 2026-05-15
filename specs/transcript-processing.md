# Transcript Processing Spec

## Extração mínima

- título provável;
- data;
- participantes;
- tópicos;
- decisões;
- ações;
- donos;
- prazos;
- riscos;
- perguntas abertas;
- links citados.

## Evidência

Cada decisão e ação deve apontar para trecho ou timestamp quando disponível.

## Confiança

Campos extraídos recebem confiança:

- `high`: texto explícito;
- `medium`: dedução forte;
- `low`: ambíguo ou incompleto.

Itens `low` não podem virar issue automática sem revisão.

## Saídas

- JSON estruturado.
- Markdown de reunião.
- Bloco de follow-up.
- Receipt.
