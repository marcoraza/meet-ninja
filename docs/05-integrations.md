# Integrations

## E-mail

Integração inicial prevista: Gmail via OAuth.

Responsabilidades:

- autenticar com escopo mínimo;
- buscar mensagens por query;
- extrair anexos e corpo;
- preservar metadados;
- não marcar como lido, arquivar ou responder no MVP.

## Vaults

Integração inicial: escrita em pastas locais configuradas.

Responsabilidades:

- resolver vault alvo;
- gerar caminho determinístico;
- criar nota Markdown;
- mostrar diff antes de escrever;
- manter frontmatter estável.

## GitHub

Integração inicial: GitHub API com dry-run obrigatório.

Responsabilidades:

- localizar repositório alvo;
- criar issue draft;
- preparar comentário draft;
- listar branches e PRs relevantes;
- aplicar escrita só com autorização explícita.

## Modelo de capability

Cada integração expõe capabilities pequenas:

- `email.search`
- `email.fetch_transcript`
- `vault.render_note`
- `vault.write_note`
- `github.render_issue`
- `github.create_issue`
- `github.render_comment`
- `github.create_comment`

O agente compõe capabilities. Ele não acessa APIs diretamente.
