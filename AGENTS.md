# AGENTS.md local do Meet Ninja

Este arquivo adiciona contexto técnico do projeto. O contrato global do Marco continua valendo.

## Natureza do sistema

Meet Ninja é um agente pessoal com acesso potencial a e-mail, transcritos, vaults e GitHub. A superfície é sensível por padrão.

## Regras locais

- Nunca commitar transcritos reais, e-mails reais, tokens, exports privados ou conteúdo de vault pessoal.
- Toda integração externa começa em modo read-only ou dry-run.
- Escrita em e-mail, GitHub ou vault pessoal exige comando explícito do Marco para aquela ação.
- O transcrito original é fonte primária. Resumos, tarefas, issues e notas são derivados.
- Toda reunião processada deve gerar receipt local com fonte, data, hash do conteúdo original, saídas geradas e ações propostas.
- Não criar UI antes do pipeline CLI estar validado com fixtures realistas.
- Preferir módulo pequeno e testável a agente monolítico.

## Qualidade mínima

- Fixture realista para cada tipo de transcrito aceito.
- Teste de extração para decisões, ações, donos e prazos.
- Teste de roteamento para vault e GitHub em modo dry-run.
- Smoke local antes de qualquer deploy ou automação agendada.
