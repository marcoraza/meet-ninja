---
kind: executivo
project: certify-mvp
confidence: 0.95
title: "Alinhamento Técnico do Projeto Certify"
meeting_datetime: 2026-05-12T14:00:00
people: ["Marcelo", "Marco", "Dá", "Letícia", "Nil", "Sandoval", "Fernando"]
tags: [kind/executivo, projeto/certify-mvp, pessoa/marcelo, pessoa/marco, pessoa/da, pessoa/leticia, pessoa/nil, pessoa/sandoval, pessoa/fernando]
gmail_message_id: 19e1e322bff85b51
gmail_thread_id: 19e1e322bff85b51
notes_doc_id: 1fz5bVg-jiuh7PLPtiTGGQ6s-5kih-xKUocnzfJap-a4
---

# Executivo: Alinhamento Técnico do Projeto Certify

**Projeto:** certify-mvp  
**Participantes:** [[Marcelo]], [[Marco]], [[Dá]], [[Letícia]], [[Nil]], [[Sandoval]], [[Fernando]]  
**Data:** 12/05/2026 14:00

## Contexto
A reunião teve como objetivo o alinhamento técnico do projeto Certify, focando na otimização do motor de validação documental e na resolução de gargalos operacionais. A equipe discutiu a necessidade de expandir a matriz de documentos para aumentar a precisão do sistema e solucionar falhas de consumo de API que estavam interrompendo o processamento dos candidatos.

## Decisões
- Definida a inclusão de novos documentos na matriz de "Marinheiro de Convés" para ampliar o repertório de validação.
- Estabelecido o processamento individual de documentos por candidato para facilitar a identificação de erros.
- Decidida a migração para o uso do Open Router para centralizar o gerenciamento de chaves de API e evitar o esgotamento de saldo.
- Definida a utilização do modelo Gemini 3.1 Flash para as próximas etapas de processamento.

## Ações
- [ ] Separar candidato para submissão (responsável: [[Marcelo]], prazo: sem prazo)
- [ ] Confirmar documentos da matriz grande (responsável: O grupo, prazo: sem prazo)
- [ ] Verificar e questionar documento MCIA (STCW DPC 1034/ALF) (responsável: [[Marcelo]], prazo: sem prazo)
- [ ] Configurar Codex para seleção de candidato do backup (responsável: [[Marco]], prazo: sem prazo)
- [ ] Adicionar botões de reprocessamento individual por documento (responsável: [[Marco]], prazo: sem prazo)
- [ ] Realizar testes com 10 a 20 usuários focando em DP e formulários (responsável: O grupo, prazo: sem prazo)
- [ ] Adicionar fundos à conta Bin (responsável: [[Marcelo]], prazo: sem prazo)
- [ ] Investigar falha de classificação do documento CBSN (responsável: O grupo, prazo: sem prazo)
- [ ] Revisar documentos individualmente para depuração (responsável: [[Marco]], prazo: sem prazo)

## Próximos passos
- Realizar testes de carga com o modelo GPT configurado para maior robustez.
- Agendar reunião com [[Letícia]] e parceiro da agência para apresentação de perfil de influenciador.
- Monitorar o processamento da fila de workers após as alterações na infraestrutura.
- Criar grupo no Telegram para monitoramento do projeto Certify.

## Riscos e pendências
- Limitações de concorrência no processamento de workers causando travamentos.
- Inconsistências na leitura de documentos via OCR que impactam a classificação automática.
- Dependência de saldo em APIs externas para a continuidade dos testes.
- Necessidade de validação científica e definição de patrocinadores para o motor de IA.
