---
kind: executivo
project: certify-mvp
confidence: 1.00
title: "Estruturação Técnica do Motor Certify"
meeting_datetime: 2026-04-27T14:43:00
people: ["Marco", "Marcelo"]
gmail_message_id: 19dd0a32fb659105
gmail_thread_id: 19dd0a32fb659105
notes_doc_id: 18LXdp-LgfwGcQdpvhADyueJ6D_1jUVOfkUcOK2t8Qq8
---

# Executivo: Estruturação Técnica do Motor Certify

**Projeto:** certify-mvp  
**Participantes:** Marco, Marcelo  
**Data:** 27/04/2026 14:43

## Contexto
A reunião teve como objetivo definir a estruturação técnica do motor de compliance do projeto Certify e alinhar a estratégia de apresentação do produto aos sócios. O foco principal foi a estabilização do motor de validação documental e a definição de fluxos para garantir a aderência precisa às matrizes normativas.

A discussão também abordou a necessidade de profissionalizar o produto para testes, estabelecendo um padrão de dados e a criação de uma versão limpa (V3) do sistema. Marco e Marcelo alinharam expectativas sobre a origem dos dados, a automação de processos e a gestão de exigências específicas de clientes.

## Decisões
* Priorizou-se a estabilização do motor de validação em detrimento de ajustes estéticos.
* Definiu-se que o sistema deve validar a correspondência entre o nome do candidato e o documento apresentado.
* Estabeleceu-se a criação de uma aba específica para exigências de treinamentos internos de clientes.
* Determinou-se que a "modalidade" será tratada como uma informação extraída do documento, enquanto variações de normas serão classificadas como "variação".
* Consolidou-se a utilização de fontes oficiais (gov.br) como base indiscutível para as regras de compliance.

## Ações
- [ ] Desenvolver versão V3 do sistema (base limpa para testes) (responsável: Marco, prazo: sem prazo)
- [ ] Remover a empresa de teste "Marcelo" da base de dados (responsável: Marco, prazo: sem prazo)
- [ ] Realizar scan nos 52 candidatos ativos para identificar falhas de vínculo com empresas/vagas (responsável: Marco, prazo: sem prazo)
- [ ] Implementar validação de nome do candidato versus documento (responsável: Marco, prazo: sem prazo)
- [ ] Implementar campo de detalhamento de status (por que está parcial ou em revisão) (responsável: Marco, prazo: sem prazo)
- [ ] Ativar botões de interface: Aprovar para DP, Solicitar Revisão e Rejeitar Candidato (responsável: Marco, prazo: sem prazo)
- [ ] Enviar lista de pontos, arquivos de lista de presença, logo da MDE e exemplo com QR Code (responsável: Marcelo, prazo: sem prazo)
- [ ] Realizar auditoria e cruzamento entre resultados do motor e base real (responsável: Marcelo, prazo: sem prazo)
- [ ] Enviar manual de uso do OpenCloud com GPT (responsável: Marcelo, prazo: sem prazo)

## Próximos passos
* Agendar encontros diários de acompanhamento ao meio-dia para o desenvolvimento final.
* Executar hotfix nos dados para transformar o caso "Laudis" em teste padrão (golden test).
* Preparar estrutura nas matrizes para upload de exigências de treinamento específicas por cliente.

## Riscos e pendências
* Inconsistência de dados: 52 candidatos ativos sem vínculo com empresas ou vagas.
* Necessidade de padronização de nomenclatura para documentos, matrizes e candidatos.
* Risco de confusão entre treinamentos internos de clientes e normas oficiais (ex: Opito) caso não haja segregação clara.
* Pendência na correção de falhas de promoção de metadados extraídos e uso de alias.
