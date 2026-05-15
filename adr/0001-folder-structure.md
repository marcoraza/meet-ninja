# ADR 0001: Estrutura Inicial Do Repositório

## Status

Aceita.

## Contexto

Meet Ninja começa como agente pessoal com dados sensíveis. O projeto precisa separar documentação, specs, código, fixtures, dados locais e operações antes de integrar contas reais.

## Decisão

Usar estrutura por responsabilidade:

- `docs`: entendimento do produto e arquitetura.
- `specs`: contratos executáveis do MVP.
- `src`: código futuro.
- `tests`: testes e fixtures artificiais.
- `evals`: avaliação de qualidade das extrações.
- `prompts`: prompts versionados e revisáveis.
- `ops`: runbooks.
- `data`: dados locais ignorados pelo Git.
- `tasks`: backlog e lessons.

## Consequências

- Fica mais fácil evoluir sem agente monolítico.
- Integrações externas ficam isoladas.
- Dados privados têm caminho claro e ignorado.
- O MVP pode ser validado por CLI e testes antes de automação real.
