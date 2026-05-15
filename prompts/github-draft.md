# Prompt: GitHub Draft

Use este prompt para transformar ações extraídas em payload GitHub.

## Instrução

Você recebe uma ação de reunião com evidência. Gere um issue draft objetivo.

## Regras

- Não criar issue se `confidence` for `low`.
- Não prometer execução já feita.
- Incluir contexto suficiente para outro dev executar.
- Incluir critério de aceite verificável.
- Citar receipt ou fonte derivada quando disponível.

## Saída

JSON com `repo`, `title`, `body` e `labels`.
