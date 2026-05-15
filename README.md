# Meet Ninja

Meet Ninja é o agente pessoal do Marco para transformar transcritos de reuniões em ativos úteis: captura no e-mail pessoal, tratamento estruturado, passagem pelos vaults de conhecimento e operação no GitHub.

O projeto começa local-first por segurança. O agente deve conseguir ler, classificar, normalizar, registrar evidência e propor ações antes de ganhar qualquer permissão de escrita em e-mail, vaults ou GitHub.

## Escopo inicial

- Encontrar transcritos de reunião no e-mail pessoal.
- Preservar o transcrito original sem edição.
- Extrair pauta, decisões, tarefas, donos, prazos, riscos e links.
- Gerar saídas em Markdown compatíveis com os vaults do Marco.
- Criar ou atualizar issues, PRs e comentários no GitHub quando autorizado.
- Manter trilha de auditoria para cada reunião processada.

## Estrutura

```text
.
├── AGENTS.md
├── README.md
├── .env.example
├── adr/
├── config/
├── data/
│   ├── inbox/
│   ├── processed/
│   └── exports/
├── docs/
├── evals/
├── ops/
│   └── runbooks/
├── prompts/
├── schemas/
├── specs/
├── src/
│   ├── agents/
│   ├── cli/
│   ├── connectors/
│   ├── core/
│   └── services/
├── tasks/
└── tests/
```

## Documentos principais

- [docs/00-index.md](docs/00-index.md): mapa de leitura.
- [docs/01-product-brief.md](docs/01-product-brief.md): problema, usuários, escopo e não escopo.
- [docs/02-architecture.md](docs/02-architecture.md): arquitetura do agente e limites dos módulos.
- [docs/03-workflows.md](docs/03-workflows.md): fluxos ponta a ponta.
- [docs/04-data-and-security.md](docs/04-data-and-security.md): privacidade, dados e permissões.
- [docs/05-integrations.md](docs/05-integrations.md): e-mail, vaults e GitHub.
- [specs/mvp.md](specs/mvp.md): critério de saída do primeiro MVP.
- [schemas/README.md](schemas/README.md): contratos de dados iniciais.
- [tasks/todo.md](tasks/todo.md): backlog vivo.

## Princípio de implementação

O primeiro milestone não é automação total. É prova confiável do fluxo com dry-run, dados realistas e zero escrita destrutiva. Depois disso, cada permissão de escrita entra como uma capability explícita, testada e reversível.
