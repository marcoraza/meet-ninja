# Architecture

## Visão

Meet Ninja é um pipeline local-first com conectores externos bem isolados.

```text
E-mail ou arquivo local
  -> ingestão
  -> normalização
  -> extração estruturada
  -> roteamento para vault
  -> propostas GitHub
  -> receipt auditável
```

## Camadas

### `src/connectors`

Adaptadores para sistemas externos. Nenhum conector deve conter regra de negócio.

- `email`: busca mensagens, anexos e metadados.
- `vaults`: escreve ou simula escrita em vaults locais.
- `github`: prepara issues, comentários, labels e PR metadata.

### `src/core`

Regras centrais do domínio.

- `transcripts`: parsing, normalização, segmentação e classificação.
- `workflows`: orquestração dos fluxos.
- `memory`: receipts, histórico de reuniões e idempotência.

### `src/agents`

Composição das capacidades do agente. Aqui entram prompts, ferramentas permitidas e políticas de decisão.

### `src/services`

Serviços de aplicação que conectam core, conectores e CLI.

### `src/cli`

Entrada operacional inicial. O primeiro produto deve ser testável por CLI antes de qualquer UI.

## Modelo de permissão

Cada ação externa usa um modo:

- `read`: lê fonte externa.
- `dry_run`: calcula saída sem escrever.
- `propose`: gera diff, issue draft ou nota pendente.
- `write`: executa escrita real com autorização explícita.

## Fonte da verdade

- Fonte primária: transcrito original e metadados de origem.
- Fonte processada: JSON estruturado extraído.
- Fonte operacional: Markdown de vault, issue draft e receipt.

Markdown nunca substitui o transcrito original.
