# MVP Spec

## Objetivo

Provar o fluxo completo de reunião para execução sem escrita externa automática.

## Critério de saída

O MVP está pronto quando:

- aceita um transcrito local de fixture;
- simula busca de e-mail com payload realista;
- gera extração estruturada;
- gera nota Markdown para vault;
- gera issue draft para GitHub;
- salva receipt local;
- roda teste automatizado do fluxo completo;
- roda comando CLI em modo dry-run.

## Entregáveis

- CLI `meet-ninja process`.
- Fixture artificial em `tests/fixtures`.
- Snapshot de Markdown esperado.
- Snapshot de payload GitHub esperado.
- Receipt esperado.
- Docs de setup local.

## Não fazer no MVP

- Escrita automática em Gmail.
- Escrita automática em GitHub.
- UI web.
- Agendamento recorrente.
- Processamento de todos os formatos possíveis de transcrito.
