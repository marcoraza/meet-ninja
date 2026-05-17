---
kind: executivo
project: certify-mvp
confidence: 1.00
title: "Revisão de Matrizes e Padronização do Certify"
meeting_datetime: 2026-04-23T15:40:00
people: ["Marco", "Marcelo", "Cláudio"]
tags: [kind/executivo, projeto/certify-mvp, pessoa/marco, pessoa/marcelo, pessoa/claudio]
gmail_message_id: 19dbc211085d2e8f
gmail_thread_id: 19dbc211085d2e8f
notes_doc_id: 1QShuJR6_6PSduwy4GEKtYH_cTLYbrZNHv5SpfoGksQ4
---

# Executivo: Revisão de Matrizes e Padronização do Certify

**Projeto:** certify-mvp  
**Participantes:** [[Marco]], [[Marcelo]], [[Cláudio]]  
**Data:** 23/04/2026 15:40

## Contexto
A reunião foi realizada para alinhar a padronização da base documental do projeto Certify e otimizar a interface de criação de matrizes de conformidade. O objetivo central é eliminar inconsistências na nomenclatura de documentos (como NRs e certificados STCW) e garantir que o sistema suporte a diversidade de formatos de matrizes enviadas por diferentes clientes, como Hélix, Possidônia e SBM.

A equipe busca profissionalizar a estrutura de dados para evitar que usuários criem documentos duplicados ou incorretos manualmente, garantindo que a IA atue como um validador robusto de conformidade e validade documental.

## Decisões
*   Restringiu-se a criação manual de itens na interface para assegurar a integridade da base de dados.
*   Definiu-se a implementação de um modelo "guarda-chuva" para agrupar variações de normas e certificados sob uma nomenclatura única.
*   Estabeleceu-se que a IA atuará como um *worker* para validar datas de validade e classificar documentos, mesmo quando estes possuírem apenas a data de emissão.
*   Padronizou-se o campo de validade para entrada de tempo (ex: 1 ano, 5 anos) em substituição ao formato de *checkbox*.

## Ações
- [ ] Atualizar base de normas e documentos faltantes (responsável: [[Marco]], prazo: sem prazo)
- [ ] Desenvolver motor de IA para classificação de matrizes e unificação de nomenclatura (responsável: [[Marco]], prazo: 5 a 7 dias)
- [ ] Montar matriz de teste com 50 documentos da Hélix para validar o motor (responsável: [[Marcelo]], prazo: sem prazo)
- [ ] Coletar modelos oficiais de documentos (NR3, NR34, OPIT, STCW) para alimentar a base (responsável: [[Marcelo]], prazo: sem prazo)
- [ ] Ajustar sistema e conectar back-end para verificação de status (pendente/aprovado) (responsável: [[Marco]], prazo: sem prazo)
- [ ] Definir estrutura de categorização "guarda-chuva" com [[Cláudio]] (responsável: [[Marco]], prazo: sem prazo)

## Próximos passos
*   Finalizar a atualização da interface de matrizes no ambiente de desenvolvimento.
*   Executar o teste de carga com a matriz da Hélix para validar a eficácia do motor de IA.
*   Realizar o *deploy* da nova estrutura de interface após a estabilização dos componentes.

## Riscos e pendências
*   Inconsistência na nomenclatura de documentos entre diferentes clientes (ex: variações de nomes em inglês e português para a mesma NR).
*   Risco de usuários inserirem textos livres ou documentos não validados na base caso a interface não restrinja adequadamente o *upload*.
*   Dependência de coleta de documentos oficiais para alimentar a base de dados antes da entrega do MVP.
