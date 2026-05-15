# Data and Security

## Classe dos dados

Transcritos de reunião, e-mails e vaults pessoais são dados privados. O repositório não deve conter conteúdo real desses materiais.

## Política de armazenamento

- `data/inbox`: entrada bruta local, ignorada pelo Git.
- `data/processed`: extrações locais, ignoradas pelo Git.
- `data/exports`: saídas locais, ignoradas pelo Git.
- `tests/fixtures`: apenas exemplos artificiais ou anonimizados.

## Secrets

Secrets ficam em `.env` ou no keychain do sistema. `.env.example` documenta nomes de variáveis sem valores.

## Receipts

Cada processamento deve registrar:

- identificador da fonte;
- data de captura;
- hash do original;
- versão do pipeline;
- arquivos gerados;
- ações propostas;
- ações aplicadas;
- erros e baixa confiança.

## Red lines

- Não commitar transcrito real.
- Não enviar conteúdo de e-mail para serviço externo sem decisão explícita.
- Não escrever em GitHub sem prévia visualização do payload.
- Não apagar nota de vault ou issue por automação no MVP.
