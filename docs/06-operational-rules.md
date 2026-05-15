# Operational Rules

## Primeiro comportamento esperado

O agente deve ser útil antes de ser autônomo. A ordem correta é:

1. observar;
2. estruturar;
3. propor;
4. aplicar com autorização;
5. automatizar o que já ficou previsível.

## Idempotência

Rodar o mesmo transcrito duas vezes não pode duplicar nota, issue ou receipt. O hash do original e o identificador da fonte devem guiar deduplicação.

## Baixa confiança

Quando uma decisão, dono ou prazo não estiver claro, o agente deve marcar como baixa confiança. Nunca converter leitura fraca em certeza operacional.

## Escrita externa

Toda escrita externa deve ter preview:

- caminho da nota no vault;
- diff do Markdown;
- título e corpo da issue;
- comentário GitHub;
- labels ou assignees sugeridos.

## Falhas

Falha parcial não pode apagar evidência. Se a etapa GitHub falhar, a nota e o receipt seguem preservados. Se a extração falhar, o transcrito bruto segue preservado.
