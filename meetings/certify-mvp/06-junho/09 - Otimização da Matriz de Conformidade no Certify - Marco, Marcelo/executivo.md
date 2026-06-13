---
kind: executivo
project: certify-mvp
confidence: 1.00
title: "Otimização da Matriz de Conformidade no Certify"
meeting_datetime: 2026-06-09T15:17:00
people: ["Marco", "Marcelo"]
tags: [kind/executivo, projeto/certify-mvp, pessoa/marco, pessoa/marcelo]
gmail_message_id: 19eae75bfb9477b6
gmail_thread_id: 19eae75bfb9477b6
notes_doc_id: 1pxwDETpu6gYdttsLvnKq9V9SKlDlINcW7W0XSgUj77g
---

# Executivo: Otimização da Matriz de Conformidade no Certify

**Projeto:** certify-mvp  
**Participantes:** [[Marco]], [[Marcelo]]  
**Data:** 09/06/2026 15:17

## Contexto
A reunião foi realizada para otimizar a performance do sistema Certify e ajustar a matriz de conformidade documental, visando a correção de falhas na classificação de certificados (como os STCW). O projeto busca aumentar a robustez do processamento de documentos e a precisão na validação de requisitos, utilizando novas capacidades de automação via Codex e integração de ferramentas de IA.

## Decisões
- Zerou-se a exigência de carga horária na matriz de conformidade para evitar rejeições indevidas de documentos.
- Definiu-se a implementação de um "resolvedor de perfil documental" para tratar documentos que caem em categorias genéricas.
- Estabeleceu-se a priorização de códigos específicos (ex: 3/1, 3/2) na lógica de classificação em vez de depender apenas do contexto do documento.
- Decidiu-se pela limpeza da base de dados e dos registros de candidatos anteriores para iniciar uma nova rodada de testes sistêmicos.

## Ações
- [ ] Criar resolvedor de perfil documental por evidências (responsável: [[Marco]], prazo: sem prazo)
- [ ] Subir novos candidatos para teste (responsável: [[Marcelo]], prazo: sem prazo)
- [ ] Recriar matriz de classificação (responsável: [[Marco]] e [[Marcelo]], prazo: sem prazo)
- [ ] Definir termo "parser" e seu contexto de uso no projeto (responsável: [[Marcelo]], prazo: sem prazo)
- [ ] Finalizar pendência financeira do projeto (responsável: [[Marco]], prazo: próxima sexta-feira)
- [ ] Ajustar interface de revisão para espelhar detalhes do candidato (responsável: [[Marco]], prazo: sem prazo)
- [ ] Enviar arquivo zip com documentos dos candidatos Loran e Igor (responsável: [[Marcelo]], prazo: sem prazo)
- [ ] Reprocessar candidato Mateus (responsável: [[Marcelo]], prazo: sem prazo)
- [ ] Corrigir erros no motor de comparação e processamento (responsável: [[Marco]], prazo: sem prazo)

## Próximos passos
- Realizar testes de carregamento da matriz de conformidade diretamente via planilha.
- Executar testes de processamento cruzado (enviar documentos de um candidato para o perfil de outro) para validar o comportamento do sistema.
- Monitorar o lançamento de novos modelos de IA e a atualização dos limites de uso para continuidade dos testes.

## Riscos e pendências
- Identificada duplicidade na leitura de arquivos e falhas de processamento em certificados de competência (STCW).
- Necessidade de correção no motor de comparação para evitar que documentos sejam classificados como genéricos ou excedentes.
- Divergência nos custos de consumo de recursos (APIs vs. tokens) entre as ferramentas utilizadas.
- Bloqueios técnicos na automação de login via Google (pop-ups) exigindo contornos manuais.
