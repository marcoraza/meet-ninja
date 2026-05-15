# Vault Routing Spec

## Objetivo

Gerar notas consistentes para os vaults do Marco sem espalhar arquivos em lugares errados.

## Entrada

- reunião processada;
- projeto detectado;
- pessoas citadas;
- tags;
- configuração de vaults.

## Roteamento

Prioridade:

1. projeto explícito;
2. repositório GitHub explícito;
3. cliente explícito;
4. vault padrão;
5. pendente de revisão.

## Frontmatter mínimo

```yaml
type: meeting
source: meet-ninja
date:
project:
repo:
participants: []
status: processed
confidence:
receipt:
```

## Segurança

Dry-run deve mostrar caminho final e diff antes da escrita.
