# Prompt: Transcript Extraction

Use este prompt como contrato inicial para extrair dados de transcritos.

## Instrução

Você recebe um transcrito de reunião. Extraia apenas informações sustentadas pelo texto.

Retorne JSON compatível com `schemas/meeting-extraction.schema.json`.

## Regras

- Não inventar dono.
- Não inventar prazo.
- Marcar baixa confiança quando o trecho estiver ambíguo.
- Preservar evidência textual curta para decisões e ações.
- Separar decisão de tarefa.
- Links citados devem ir em `links`.

## Saída

Somente JSON válido.
