# Runbook: Local Setup

## Objetivo

Rodar o Meet Ninja localmente sem tocar contas reais por acidente.

## Passos previstos

1. Copiar `.env.example` para `.env`.
2. Manter `MEET_NINJA_DRY_RUN=true`.
3. Configurar fixture local antes de OAuth.
4. Rodar teste de processamento.
5. Rodar CLI em dry-run.
6. Revisar outputs em `data/exports`.

## Gate para habilitar e-mail real

- Fixture completa passando.
- Receipt gerado.
- Logs sem secrets.
- Query de e-mail revisada.
- Escopos OAuth documentados.

## Gate para habilitar GitHub write

- Payload dry-run revisado.
- Repo alvo correto.
- Labels e assignees corretos.
- Confirmação explícita do Marco para aquela ação.
