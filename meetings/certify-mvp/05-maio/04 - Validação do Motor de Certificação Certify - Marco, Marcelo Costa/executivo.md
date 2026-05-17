---
kind: executivo
project: certify-mvp
confidence: 1.00
title: "Validação do Motor de Certificação Certify"
meeting_datetime: 2026-05-04T16:35:00
people: ["Marco", "Marcelo Costa"]
tags: [kind/executivo, projeto/certify-mvp, pessoa/marco, pessoa/marcelo-costa]
gmail_message_id: 19df4e030b4e77be
gmail_thread_id: 19df4e030b4e77be
notes_doc_id: 1M-xnR28LCgtgWt5jdAkh-Y7u3ExUdfXZOrme4UF18Hg
---

# Executivo: Validação do Motor de Certificação Certify

**Projeto:** certify-mvp  
**Participantes:** [[Marco]], [[Marcelo Costa]]  
**Data:** 04/05/2026 16:35

## Contexto
A reunião teve como objetivo validar o novo motor de certificação do projeto Certify, comparando sua performance com a versão anterior através de 81 casos de teste. O foco foi garantir que o motor identifique corretamente documentos expirados e divergências de dados, superando a assertividade do sistema atual.

[[Marco]] e [[Marcelo Costa]] discutiram ajustes necessários na matriz de documentos e na interface do sistema para reduzir a latência e melhorar a experiência do usuário durante o processamento de candidatos.

## Decisões
*   Padronizou-se a ingestão da matriz de documentos conforme enviada pelo cliente para eliminar divergências de dados.
*   Definiu-se a implementação de um indicador visual de carregamento para exibir o status de análise dos documentos em tempo real.
*   Determinou-se a criação de uma funcionalidade para exclusão de candidatos, com a remoção automática de seus documentos vinculados no banco de dados.
*   Validou-se a necessidade de espelhar exatamente as colunas do Super Base com as colunas exibidas no frontend.

## Ações
- [ ] Corrigir erro na geração do relatório Alfredini e remover frases indevidas (responsável: [[Marco]], prazo: sem prazo)
- [ ] Ajustar e revisar relatórios restantes para evitar inconsistências (responsável: [[Marco]], prazo: sem prazo)
- [ ] Resolver pendências específicas das normas NR1 347 e NR37 (responsável: [[Marco]], prazo: sem prazo)
- [ ] Salvar documentos do Alfredini para realização de testes manuais (responsável: [[Marcelo Costa]], prazo: sem prazo)
- [ ] Implementar funcionalidade de exclusão de candidatos e documentos (responsável: [[Marco]], prazo: sem prazo)
- [ ] Sincronizar frontend e backend para reduzir latência (responsável: [[Marco]], prazo: sem prazo)
- [ ] Limpar base de dados no Super Base e testar botões de edição e exclusão (responsável: [[Marco]], prazo: sem prazo)
- [ ] Assegurar espelhamento das colunas do Super Base no frontend (responsável: [[Marco]], prazo: sem prazo)
- [ ] Preparar versão final para apresentação (responsável: [[Marco]], prazo: sem prazo)
- [ ] Estruturar manual de treinamento para usuários (responsável: [[Marcelo Costa]], prazo: sem prazo)

## Próximos passos
*   Realizar testes manuais com os documentos do Alfredini após as correções no motor.
*   Ajustar o motor para processar matrizes de clientes com dados inconsistentes ou sem códigos.
*   Apresentar a versão final do motor para Marcelo.

## Riscos e pendências
*   Divergências entre a matriz esperada e os documentos fornecidos pelos clientes (ex: falta de códigos ou carga horária).
*   Latência no processamento de uploads de candidatos.
*   Inconsistências pontuais entre o frontend e o backend que ainda precisam de sincronização.
*   Necessidade de validação final sobre a classificação de documentos sem data de validade.
