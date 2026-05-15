# Email Ingestion Spec

## Entrada

- Query configurada.
- Janela de tempo.
- Provedor de e-mail.
- Credencial local.

## Saída

- Lista de candidatos.
- Metadados da mensagem.
- Conteúdo bruto ou anexo.
- Identificador estável da fonte.

## Regras

- Não alterar estado da mensagem no MVP.
- Não baixar anexos que não sejam texto, PDF ou formatos explicitamente permitidos.
- Não processar mensagem sem receipt.
- Permitir allowlist e blocklist por remetente.

## Checks

- Query vazia falha com erro claro.
- Mensagem sem transcrito vira candidato rejeitado com motivo.
- Anexo duplicado não gera item novo.
