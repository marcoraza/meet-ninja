# Schemas

Contratos de dados do Meet Ninja.

Objetivo:

- impedir saída solta de LLM;
- permitir teste de regressão;
- manter receipts auditáveis;
- estabilizar integração com vault e GitHub.

Schemas iniciais:

- `meeting-extraction.schema.json`
- `receipt.schema.json`

Toda mudança de schema precisa atualizar specs e fixtures correspondentes.
