---
kind: executivo
project: certify-mvp
confidence: 1.00
title: "Validação Técnica e Configuração do Certify"
meeting_datetime: 2026-06-11T11:14:00
people: ["Marcelo", "Marco", "Letícia", "Loran"]
tags: [kind/executivo, projeto/certify-mvp, pessoa/marcelo, pessoa/marco, pessoa/leticia, pessoa/loran]
gmail_message_id: 19eb7844b5d7148c
gmail_thread_id: 19eb7844b5d7148c
notes_doc_id: 1y0_qA_KmjN1RR9wgMaQcs6NVi76SaX26jGzEu7KjgBw
---

# Executivo: Validação Técnica e Configuração do Certify

**Projeto:** certify-mvp  
**Participantes:** [[Marcelo]], [[Marco]], [[Letícia]], [[Loran]]  
**Data:** 11/06/2026 11:14

## Contexto
A reunião teve como objetivo validar a estabilidade técnica do sistema Certify e realizar ajustes finos na lógica de processamento de documentos e matrizes de conformidade. O foco principal foi a resolução de gargalos de desempenho da API e a correção de inconsistências na leitura de normas regulamentadoras (NRs) e equivalências de cursos, garantindo que o motor esteja pronto para a implementação definitiva.

## Decisões
*   Excluídos todos os candidatos atuais para reprocessamento completo utilizando a matriz V2, visando garantir a integridade dos testes.
*   Mantida a lógica atual de tratamento de documentos com nomes genéricos, priorizando o foco no motor de validação em vez de complexidade de interface.
*   Definida a classificação de documentos que divergem do candidato como "parcial", mantendo a visibilidade para o usuário final.
*   Iniciada a configuração da matriz de requisitos para a empresa SBM (Operador de Manutenção), incluindo NRs específicas como NR33, NR35 e NR13.

## Ações
- [ ] Criar dashboard de monitoramento de falhas internas (responsável: [[Marco]], prazo: sem prazo)
- [ ] Ajustar textos de notificações de erro para facilitar a identificação de problemas (responsável: [[Marco]], prazo: sem prazo)
- [ ] Desenvolver MVP para o projeto do curso (responsável: [[Marco]], prazo: sem prazo)
- [ ] Estruturar e executar gestão de tráfego para anúncios (responsável: [[Marcelo]], prazo: sem prazo)
- [ ] Revisar resultados da matriz de documentos e corrigir inconsistências (responsável: A equipe, prazo: sem prazo)
- [ ] Formalizar parceria com o professor (responsável: A equipe, prazo: sem prazo)
- [ ] Realizar ajustes operacionais para a reunião de segunda-feira (responsável: A equipe, prazo: segunda-feira)

## Próximos passos
*   Reprocessar todos os candidatos conforme a matriz oficial de máquina.
*   Verificar a aceitação de treinamento periódico como substituto para o treinamento inicial junto aos clientes.
*   Validar a disponibilidade do professor para o curso de Cloud Code.
*   Analisar a estrutura do novo projeto de organização para identificar integrações necessárias.

## Riscos e pendências
*   Alto consumo de recursos da API do Gemini, com risco de travamento do sistema por limite de cota diária.
*   Inconsistência na lógica de equivalência entre o "teste de estanqueidade" e a NR34.
*   Necessidade de revisão na matriz de condutor de máquinas devido a discrepâncias nos requisitos (ex: CBSP ausente).
*   Ausência de alertas automáticos para falhas críticas no sistema.
