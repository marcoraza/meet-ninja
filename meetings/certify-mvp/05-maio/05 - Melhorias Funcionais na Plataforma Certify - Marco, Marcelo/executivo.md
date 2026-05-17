---
kind: executivo
project: certify-mvp
confidence: 0.95
title: "Melhorias Funcionais na Plataforma Certify"
meeting_datetime: 2026-05-05T14:22:00
people: ["Marco", "Marcelo"]
tags: [kind/executivo, projeto/certify-mvp, pessoa/marco, pessoa/marcelo]
gmail_message_id: 19df9c05ef7cfa28
gmail_thread_id: 19df9c05ef7cfa28
notes_doc_id: 1oyZ13oacGblJtlLEUdVaY0sBClMfRJCFnmyS4UGVjws
---

# Executivo: Melhorias Funcionais na Plataforma Certify

**Projeto:** certify-mvp  
**Participantes:** [[Marco]], [[Marcelo]]  
**Data:** 05/05/2026 14:22

## Contexto
A reunião foi realizada para alinhar melhorias funcionais e correções técnicas na plataforma Certify. O foco principal foi a estabilização do MVP, a limpeza de dados legados que causavam anomalias no sistema e a otimização do fluxo de trabalho dos recrutadores. [[Marco]] e [[Marcelo]] revisaram pendências de interface, sincronização de dados entre módulos e a necessidade de uma base documental mais robusta e organizada.

## Decisões
*   Definiu-se o Centro de Comando como a tela inicial padrão da plataforma.
*   Determinou-se a limpeza total do catálogo V3 e a migração para uma nova matriz de documentos zerada.
*   Estabeleceu-se que a aba "Biblioteca" ficará visível apenas para usuários com perfil de supervisor.
*   Priorizou-se o uso de agentes de IA para monitoramento e follow-ups em vez de integrações via API.
*   Aprovou-se a implementação de botões de aprovação rápida na tela de revisão.
*   Definiu-se que a carga horária será um campo de primeira classe na criação de matrizes.

## Ações
- [ ] Limpar base de dados e catálogo V3 (responsável: [[Marco]], prazo: sem prazo)
- [ ] Vincular recrutador logado por padrão na criação de novas vagas (responsável: [[Marco]], prazo: sem prazo)
- [ ] Sincronizar funil de triagem com a barra superior do card do candidato (responsável: [[Marco]], prazo: sem prazo)
- [ ] Implementar botões de aprovação rápida e registro automático de histórico (responsável: [[Marco]], prazo: sem prazo)
- [ ] Adicionar botão de exportação para planilha na tela de documentos (responsável: [[Marco]], prazo: sem prazo)
- [ ] Ajustar busca de documentos para funcionamento semântico (responsável: [[Marco]], prazo: sem prazo)
- [ ] Elaborar lista de recrutadores com nomes e e-mails (responsável: [[Marcelo]], prazo: sem prazo)
- [ ] Notificar [[Marco]] sobre disponibilidade para continuidade (responsável: [[Marcelo]], prazo: sem prazo)

## Próximos passos
*   Reunião de acompanhamento agendada para sexta-feira, às 11:00.
*   Finalização da migração da base do catálogo para a biblioteca.
*   Desenvolvimento da nova logo da plataforma.
*   Testes de estabilidade do N8N e suporte técnico.

## Riscos e pendências
*   Instabilidade operacional no N8N identificada como gargalo.
*   Necessidade de correção de layout e nomenclatura de títulos perdidos em commits anteriores.
*   Dúvida sobre a necessidade de suporte a múltiplos recrutadores por vaga.
*   Bloqueios técnicos na tela de revisão de dois painéis.
