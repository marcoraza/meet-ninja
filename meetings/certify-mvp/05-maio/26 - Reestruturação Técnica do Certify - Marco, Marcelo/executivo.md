---
kind: executivo
project: certify-mvp
confidence: 1.00
title: "Reestruturação Técnica do Certify"
meeting_datetime: 2026-05-26T14:19:00
people: ["Marco", "Marcelo"]
tags: [kind/executivo, projeto/certify-mvp, pessoa/marco, pessoa/marcelo]
gmail_message_id: 19e65a476116a3b0
gmail_thread_id: 19e65a476116a3b0
notes_doc_id: 1AS54md4YaEmZYaZbyisWUMAIeAxiR25IckRcSnf6FVY
---

# Executivo: Reestruturação Técnica do Certify

**Projeto:** certify-mvp  
**Participantes:** [[Marco]], [[Marcelo]]  
**Data:** 26/05/2026 14:19

## Contexto
A reunião teve como objetivo realizar o acompanhamento técnico da reestruturação do sistema Certify. O projeto evoluiu de um MVP experimental para um produto robusto, com foco em escalabilidade, segurança e auditoria, abandonando a dependência de fluxos instáveis em nuvem em favor de uma arquitetura determinística e processamento local.

O desenvolvimento atual prioriza a fragmentação da interface em componentes independentes e a implementação de uma arquitetura de agentes autônomos. A estratégia visa consolidar o Certify como uma solução de alta alavancagem tecnológica, com potencial de comercialização *white label* para processos de admissão e conformidade.

## Decisões
- Migrou-se o ambiente de desenvolvimento para *localhost* para eliminar latência e instabilidade de serviços em nuvem.
- Adotou-se uma lógica determinística para a comparação de documentos, substituindo a dependência exclusiva de LLMs.
- Fragmentou-se o *frontend* em componentes independentes para isolar o roteamento e reduzir riscos de quebra do sistema.
- Implementou-se uma estrutura de *jobs* no PostgreSQL com *workers* paralelos e mecanismos de *heartbeat* para garantir resiliência.
- Consolidou-se a interface de admissão, integrando documentos pessoais, formulários e KYC em um fluxo único e intuitivo.

## Ações
- [ ] Apresentar relatório comparativo entre o fluxo do N8N e o motor Certify (responsável: [[Marco]], prazo: sem prazo)
- [ ] Redesenhar o layout da interface de visualização de documentos (responsável: [[Marco]], prazo: sem prazo)
- [ ] Configurar LLM na interface de chat para processamento de documentos (responsável: [[Marco]], prazo: sem prazo)
- [ ] Verificar se a exportação de documentos contempla apenas itens validados (responsável: [[Marco]], prazo: sem prazo)
- [ ] Implementar funcionalidade de upload em massa na interface de revisão (responsável: [[Marco]], prazo: sem prazo)
- [ ] Validar o comportamento do sistema na exportação de pacotes de arquivos (responsável: [[Marcelo]], prazo: sem prazo)
- [ ] Executar testes práticos no sistema de recrutamento (responsável: [[Marcelo]], prazo: sem prazo)
- [ ] Realizar transferência financeira (responsável: [[Marcelo]], prazo: sem prazo)

## Próximos passos
- Realizar reunião de alinhamento na próxima quinta-feira para revisar o progresso das atividades.
- Finalizar demonstração do motor de busca com dados simulados.
- Avançar no desenvolvimento do "[[Marco]] OS" em paralelo às entregas do Certify.

## Riscos e pendências
- Necessidade de otimização contínua do consumo de *tokens* durante o desenvolvimento com agentes.
- Dependência de ajustes manuais na interface de revisão para suportar o volume de upload em massa.
- Monitoramento da estabilidade dos serviços de nuvem utilizados para sincronização de repositórios.
- Nenhum.
