---
kind: sumario
project: certify-mvp
confidence: 1.00
title: "Otimização da Matriz de Conformidade no Certify"
meeting_datetime: 2026-06-09T15:17:00
people: ["Marco", "Marcelo"]
tags: [kind/sumario, projeto/certify-mvp, pessoa/marco, pessoa/marcelo]
gmail_message_id: 19eae75bfb9477b6
gmail_thread_id: 19eae75bfb9477b6
notes_doc_id: 1pxwDETpu6gYdttsLvnKq9V9SKlDlINcW7W0XSgUj77g
---

# Otimização da Matriz de Conformidade no Certify

**Participantes:** Marco, Marcelo

# 📝 Observações

jun. 9, 2026

## Reunião em 9 de jun. de 2026 às 15:17 GMT-03:00

Registros da reunião [Transcrição](https://docs.google.com/document/d/1pxwDETpu6gYdttsLvnKq9V9SKlDlINcW7W0XSgUj77g/edit?usp=drive_web&tab=t.rvbrv8zfmzvj) 

### Resumo

Reunião técnica focada na otimização da performance do sistema com ajuste definitivo da matriz de conformidade documental.

**Otimização de ferramentas internas**  
Discussões focaram na integração de fluxos no modelo e na automação de processos via navegador. O uso de novas habilidades automatizadas visa expandir as capacidades operacionais do sistema.

**Ajuste na matriz documental**  
A exigência de carga horária na matriz original foi zerada para evitar rejeições indevidas de documentos. Esta mudança simplifica a validação e corrige inconsistências na classificação técnica dos certificados.

**Depuração e testes sistêmicos**  
Testes contínuos revelaram falhas de processamento e duplicidade na leitura de arquivos. A implementação de uma revisão automática busca aumentar a robustez do código durante os deploys.

### Próximas etapas

- [ ] \[Off Digital\] Criar resolvedor perfil: Implementar um resolvedor de perfil documental por evidências para melhorar a categorização de documentos.

- [ ] \[Marcelo Costa\] Subir candidatos: Realizar o upload de novos candidatos para testar o funcionamento do sistema atualizado.

- [ ] \[The group\] Recriar matriz: Elaborar uma nova matriz para o sistema de classificação substituindo a versão anterior.

- [ ] \[Marcelo Costa\] Definir termo: Pesquisar o significado e o contexto de uso do termo parcer dentro do projeto.

- [ ] \[Off Digital\] Resolver financeiro: Finalizar a pendência financeira do projeto até a próxima sexta-feira.

- [ ] \[O grupo\] Testar matriz: Realizar testes para o carregamento da matriz de conformidade diretamente a partir de uma planilha.

- [ ] \[O grupo\] Ajustar matriz: Criar nova estrutura sem a exigencia de 40 horas.

- [ ] \[Off Digital\] Adicionar regra de horas: Implementar validacao para que documentos sem carga horaria emitida nao sejam reprovados pela exigencia da matriz.

- [ ] \[Off Digital\] Corrigir tela de revisao: Ajustar a interface de revisao para que espelhe corretamente os detalhes do candidato.

- [ ] \[O grupo\] Testar processamento de documentos: Realizar testes enviando documentos de um candidato para o perfil de outro e verificar o comportamento do sistema.

- [ ] \[Marcelo Costa\] Enviar documentos: Enviar o arquivo zip contendo os documentos dos candidatos Loran e Igor para análise técnica.

- [ ] \[Marcelo Costa\] Reprocessar Mateus: Excluir e realizar o upload novamente do candidato Mateus para verificar a consistência do sistema.

- [ ] \[Off Digital\] Corrigir motor: Realizar a correção dos erros identificados no processamento dos documentos e no motor de comparação.

### Detalhes

* **Monitoramento de Limites e Metas de Desenvolvimento**: Off Digital e Marcelo Costa discutem a necessidade de melhorias na estrutura de código, com a meta estabelecida de otimizar a performance em cinco vezes. Durante a verificação de limites, Off Digital relata ter 25% de uso restante no Codex, enquanto Marcelo Costa monitora o consumo do seu próprio limite, que se encontra em 75% ([00:04:34](#00:04:34)).

* **Discussão sobre Custos e Consumo de Recursos**: Marcelo Costa expressa preocupação com o custo de 50 unidades de moeda nos últimos 30 dias, uma divergência em relação ao valor esperado de 20, o que gera uma conversa sobre a diferença de cobrança entre APIs e tokens dentro das ferramentas Codex e Cloud ([00:05:59](#00:05:59)).

* **Análise de Desempenho e Possíveis Bugs na Interface**: Os participantes avaliam o consumo da ferramenta de design, notando que o ponteiro de uso permanece em 100% de disponibilidade, o que leva a uma discussão sobre a possibilidade de um bug na interface ou uma falha na contagem de créditos ([00:07:08](#00:07:08)).

* **Fluxo de Trabalho com Codex e Cloud**: Off Digital demonstra a integração do Cloud Code dentro do ambiente do Codex, utilizando a funcionalidade de browser para gerenciar ferramentas, definindo o conceito de "harness" como um conjunto de ferramentas integradas sobre o modelo que expande suas capacidades além de simples prompts ([00:09:08](#00:09:08)) ([00:14:16](#00:14:16)).

* **Estratégias de Automação e Login**: Off Digital descreve a metodologia de utilizar o Codex como copiloto, que orquestra o trabalho em vez de apenas executar comandos; uma das inovações mencionadas é o processamento de logins via e-mail dentro do ambiente do Codex para contornar bloqueios de pop-ups ([00:13:19](#00:13:19)) ([00:16:34](#00:16:34)).

* **Uso de Ferramentas de Edição de Vídeo com IA**: Off Digital introduz o uso da ferramenta Vid para edição de vídeos, destacando funcionalidades avançadas como legendas automáticas posicionadas atrás da pessoa e transições por IA, sugerindo que esses processos sejam integrados ao fluxo de trabalho do Codex para otimização ([00:18:58](#00:18:58)).

* **Urgência de Monetização e Continuidade de Testes**: Marcelo Costa enfatiza a necessidade urgente de monetizar as soluções desenvolvidas, enquanto ambos concordam em manter o papel de testadores, aguardando o lançamento de novos modelos e a atualização dos limites de uso ([00:23:26](#00:23:26)).

* **Preparação para Novos Testes de Verificação**: Os participantes decidem limpar a matriz de dados e os registros de candidatos anteriores para iniciar uma nova rodada de testes, buscando validar as mudanças feitas no código na véspera ([00:25:14](#00:25:14)).

* **Debugging de Classificação de Documentos**: Durante a execução dos testes, a dupla identifica falhas na classificação de certificados de competência (STCW), onde documentos estão sendo classificados como genéricos ou excedentes, indicando um possível problema no commit ou na lógica de extração ([00:41:46](#00:41:46)) ([00:54:13](#00:54:13)).

* **Implementação de Resolução de Perfil Documental**: Off Digital explica a criação de uma nova "skill" (habilidade) armazenada em um repositório Git, que utiliza diagramas para facilitar a explicação lógica; é proposto um novo fluxo no sistema chamado "resolvedor de perfil documental" para tratar documentos que caem em categorias genéricas ([00:58:05](#00:58:05)).

* **Refinamento da Lógica de Validação**: Marcelo Costa argumenta que a lógica de classificação deve priorizar códigos específicos (como 3/1 ou 3/2) em vez de depender apenas do contexto do documento, simplificando o sistema e evitando gargalos na validação de certificados ([01:00:50](#01:00:50)).

* **Interação com Browser e Código**: Marcelo Costa e Off Digital discutiram a implementação de código para automatizar interações com o navegador, com o objetivo de evitar a necessidade de inferência excessiva por parte da IA. Off Digital observou que a interação direta com a Cloud exige uma configuração precisa do navegador para garantir o funcionamento correto da automação ([01:02:05](#01:02:05)).

* **Definição de "Parser" e IA no React**: A conversa abordou a definição técnica de um "parser", com Marcelo Costa utilizando uma analogia de organização de peças para explicar sua função como um componente que lê dados não estruturados. Off Digital explorou a aplicação dessa tecnologia em um projeto React de compliance, descrevendo a IA como um assistente que organiza requisitos complexos de segurança de maneira estruturada ([01:05:58](#01:05:58)).

* **Segurança e Contexto Político**: A discussão transitou para preocupações com segurança de dados e privacidade, mencionando incidentes de monitoramento. O diálogo incluiu observações sobre o cenário político atual envolvendo figuras como o presidente Lula, o ex-presidente Trump e Nicolás Maduro, relacionando essas questões de instabilidade com as necessidades de monitoramento e controle de sistemas ([01:07:55](#01:07:55)).

* **Validação de Agentes e Decisões de Produto**: Off Digital e Marcelo Costa revisaram o feedback emitido por agentes de IA, que apontaram três gaps operacionais no plano. Foi tomada a decisão de produto de que documentos SCW contendo vários códigos oficiais devem cumprir automaticamente múltiplos requisitos na matriz, e que o sistema deve ser instruído a aceitar documentos de "nível superior" quando exigido ([01:11:25](#01:11:25)).

* **Gestão Financeira e Prazos**: Marcelo Costa e Off Digital alinharam o cronograma para a emissão de notas fiscais no início do mês. Off Digital comprometeu-se a concluir as apresentações necessárias para o outro Marcelo até a sexta-feira, dispondo-se a trabalhar fora do horário habitual para garantir a transição da gestão financeira ([01:13:56](#01:13:56)).

* **Produtividade com Linear e ClickUp**: Off Digital detalhou o plano de reestruturar a produtividade utilizando o Linear para tarefas operacionais e o ClickUp para a gestão de prazos. A estratégia envolve a integração dessas ferramentas com a agenda pessoal, visando um sistema onde um assistente de IA solicite apenas aprovações curtas (frases de até cinco palavras) para manter o foco operacional ([01:14:58](#01:14:58)).

* **Escopo do Projeto Certify e Ferramentas Pessoais**: Foi feita uma distinção entre a complexidade do projeto profissional "Certify" e o desenvolvimento de ferramentas pessoais. Off Digital apresentou uma solução desenvolvida para automatizar o download, a extração de áudio instrumental e a renomeação de arquivos, resolvendo uma necessidade cotidiana que anteriormente envolvia processos manuais ineficientes e sites arriscados ([01:19:55](#01:19:55)).

* **Implicações Legais de Ferramentas de Download**: A viabilidade comercial da ferramenta de download de mídia foi debatida, com considerações sobre modelos de negócio como venda "one time" ou monetização por anúncios. Off Digital e Marcelo Costa avaliaram estratégias de distribuição, incluindo o uso de VPNs e pagamentos via criptomoedas, para mitigar riscos relacionados a direitos autorais e possíveis bloqueios legais ([01:24:02](#01:24:02)).

* **Depuração de Erros no Upload de Documentos**: Marcelo Costa e Off Digital realizaram testes de depuração no upload de documentos no sistema "Certify" devido a erros recorrentes de "carga horária insuficiente". Identificou-se que a matriz configurada exigia 40 horas, mas o documento em questão não possuía tal informação, gerando divergências e ambiguidades na leitura realizada pela IA ([01:31:37](#01:31:37)).

* **Governança de Matrizes e Processos de Compliance**: Ficou definido que a alteração de matrizes e documentos críticos deve ser restrita para evitar erros de conformidade. Off Digital e Marcelo Costa planejam realizar testes futuros para a submissão de matrizes diretamente via planilha, garantindo que o sistema de diagnóstico seja mantido com validações sólidas e evitando modificações não autorizadas em parâmetros essenciais ([02:00:15](#02:00:15)).

* **Correção de commits e carga horária do certificado**: Off Digital informou que realizou o "cherry pick" de três commits para corrigir um problema na branch principal. Foi identificado um problema de extração no documento de capitania de Cabo Frio, onde a carga horária não era impressa, mas a regra do CAS exigia 40 horas, causando uma marcação incorreta de "parcial". Após ajustes e novos testes, a equipe verificou que o motor de processamento conseguiu processar corretamente os documentos sem carga horária, embora o documento CCK ainda tenha sido barrado pela regra de horário ([02:04:22](#02:04:22)).

* **Ajuste na Matriz para exigência de horas**: A equipe discutiu a necessidade de modificar a matriz, pois documentos como CBSN e CBSP estavam passando pelo sistema mesmo sem a informação de carga horária, enquanto outros eram rejeitados ([02:08:13](#02:08:13)). Marcelo Costa e Off Digital debateram se a regra de 40 horas deveria ser mantida na matriz se os documentos não possuem essa informação nativa ([02:13:20](#02:13:20)).

* **Regulamentação de horas e alteração na Matriz**: Marcelo Costa e Off Digital discutiram as diferenças de exigência de carga horária entre o STCW, que geralmente não especifica horas, e a NR, que detalha as horas nos documentos ([02:14:40](#02:14:40)). Para evitar rejeições indevidas, Marcelo Costa decidiu zerar a exigência de horas na matriz original ([02:15:47](#02:15:47)).

* **Teste de candidato com Matriz V2**: Foi criado um novo candidato, Fábio Pestana da Silva, utilizando a "V2" da matriz com as horas zeradas ([02:17:07](#02:17:07)). A equipe realizou testes e observou que o sistema processou os documentos corretamente, sem pendências indevidas por falta de carga horária, validando a eficácia da alteração ([02:19:47](#02:19:47)).

* **Teste de integridade e propriedade de documentos**: A equipe testou o comportamento do sistema ao subir documentos de um candidato no perfil de outro (Mateus e Fábio) para verificar se o sistema detectaria a divergência de titularidade ([02:21:21](#02:21:21)). Off Digital esclareceu que o sistema processa os documentos na base, mas não os endereça automaticamente a um candidato se os metadados do documento não corresponderem ([02:24:26](#02:24:26)).

* **Detecção de divergência de titularidade**: Durante os testes, discutiu-se a necessidade de o sistema notificar quando o titular do documento não corresponde ao candidato. A equipe observou que, embora o sistema processasse o arquivo, não havia uma notificação clara de "titular divergente" sem uma regra específica, levando o documento para a base sem um endereçamento correto ([02:25:56](#02:25:56)).

* **Discussão sobre colunas "Parcial" vs "Não Confere"**: Houve um debate sobre a estrutura das colunas no sistema, avaliando se seria necessário criar uma coluna específica para "Não Confere" ou se deveria manter apenas a coluna "Parcial" ([02:33:42](#02:33:42)). Off Digital argumentou que adicionar novas colunas aumentaria a complexidade do motor de regras, enquanto Marcelo Costa pontuou que "Parcial" acaba sendo usado para muitos casos diferentes, o que pode confundir o usuário ([02:36:07](#02:36:07)). A decisão foi manter a estrutura atual por enquanto para evitar complexidade excessiva ([02:38:41](#02:38:41)).

* **Correção de erro de interface na revisão**: Marcelo Costa e Off Digital identificaram um erro de interface (front-end) na tela de revisão, onde o sistema exibia "Identidade confere" mesmo quando o titular do documento era diferente do candidato ([02:39:37](#02:39:37)). Off Digital comprometeu-se a corrigir essa exibição para garantir que o espelhamento visual esteja alinhado com a validação realizada pelo motor de regras ([02:40:48](#02:40:48)).

* **Classificação de documentos como excedentes**: A equipe analisou documentos classificados como "excedente" (não exigidos). Foi verificado que um documento com código semelhante a um exigido (3/1) foi corretamente marcado como excedente porque o conteúdo do documento (referente a gerenciamento de praça de máquinas) não era o solicitado na matriz ([02:43:21](#02:43:21)).

* **Debugging de duplicidade de documentos**: Marcelo Costa relatou que o sistema estava duplicando ou triplicando a sigla "CAC" para documentos que, na verdade, eram "CBSN" ([02:51:00](#02:51:00)). A equipe levantou a hipótese de que o comportamento poderia ser resultado de testes anteriores com outros candidatos, fazendo com que o sistema buscasse dados antigos na base ([02:56:23](#02:56:23)).

* **Gestão de Testes e Candidatos**: Marcelo Costa e Off Digital discutem o gerenciamento de máquinas e o processamento de candidatos, focando nos testes com os perfis de Igor e Mateus. Durante a interação, coordenam a exclusão e o reenvio de dados para verificar a consistência do sistema, enquanto gerenciam o fluxo de trabalho ([03:01:57](#03:01:57)).

* **Lógica de Status de Requisitos**: Off Digital aponta uma falha na lógica do sistema, onde o motor de processamento reclassifica incorretamente requisitos como "parcial" em vez de mantê-los como "pendente" nos casos em que o documento enviado não cobre o requisito exigido pela matriz. Eles discutem que a interface deve exibir corretamente o status como "pendente" acompanhado de uma nota informando que o documento não cobre o requisito, em vez de gerar uma classificação parcial ([03:18:17](#03:18:17)).

* **Problemas de Processamento e CAC**: Analisando o feedback do sistema, Off Digital relata que o motor falha ao processar o CAC em relação aos requisitos CBSN e CBSP, resultando em classificações incorretas ([03:28:33](#03:28:33)). Marcelo Costa observa que o sistema está carregando o mesmo documento diversas vezes de forma errônea, o que gera erros nas validações, apesar de ser um processo de upload simples ([03:30:33](#03:30:33)).

* **Identificação de Documentos e Erros de Código**: Marcelo Costa e Off Digital identificam que o sistema falha ao processar documentos dos candidatos Igor e Loran porque se baseia cegamente em códigos de identificação ([03:34:42](#03:34:42)). Mesmo que os documentos possuam nomes diferentes, o motor os confunde por terem códigos idênticos, resultando em classificações incorretas e falhas na verificação de validade dos documentos ([03:36:45](#03:36:45)).

* **Implementação de Auto Review**: Off Digital explica que o tempo de deploy aumentou para mais de 6 minutos devido à implementação de um novo sistema chamado "Auto Review". Este sistema, que integra três repositórios Git do OpenCloud, executa testes reais no VPS, realiza commits e verifica riscos de código automaticamente antes de concluir o processo, buscando maior robustez no código ([03:38:59](#03:38:59)).

* **Plano de Correção e Próximos Passos**: Como o sistema continua apresentando erros de leitura e duplicidade nos uploads, Off Digital solicita que Marcelo Costa envie os arquivos zip dos documentos dos candidatos Loran e Igor para possibilitar a depuração ([03:42:16](#03:42:16)). Marcelo Costa concorda em enviar os arquivos e se prepara para continuar os testes com outros candidatos, como Fábio e Renan, aguardando um feedback de Off Digital sobre as correções necessárias ([03:43:35](#03:43:35)).

*Revise as anotações do Gemini para checar se estão corretas. [Confira dicas e saiba como o Gemini faz anotações](https://support.google.com/meet/answer/14754931)*

*Como está a qualidade de **destas observações?** [Responda a uma breve pesquisa](https://google.qualtrics.com/jfe/form/SV_9vK3UZEaIQKKE7A?confid=2AgmbV3ukFFeUjz-RIUWDxIWOBABMgUIigIgABgFCA&detailid=standard&screenshot=false) para nos dar seu feedback, incluindo o quanto as observações foram úteis para o que você precisa.*

# 📖 Transcrição

jun. 9, 2026

## Reunião em 9 de jun. de 2026 às 15:17 GMT-03:00 \- Transcrição

### 00:04:34 {#00:04:34}

**Off Digital:** Ó o cara aí.

**Marcelo Costa:** Grande priminho.

**Off Digital:** E aí,

**Marcelo Costa:** Pera aí que o bichinho tá abrindo uns bicos aqui,

**Off Digital:** priminho?

**Marcelo Costa:** primo. Ah, deixa eu ver. Pá, pá, pode ser. Beleza, pera aí.

**Off Digital:** E aí, Primi? Sempre que nós vamos falar, os caras lançam um modelo novo. É isso. Então,

**Marcelo Costa:** É, os caras tão para cima, né, priminho? Já tá podendo meter a

**Off Digital:** meu irmão, tá, p\*\*\*\*. Já tô.

**Marcelo Costa:** mão.

**Off Digital:** Primeira tarefa que eu falei foi, mandei o certifi estrutura de código aí e melhorem pelo menos cinco vezes.

**Marcelo Costa:** É, fala,

**Off Digital:** Já mand,

**Marcelo Costa:** velho. É o mínimo que você tem para fazer aí.

**Off Digital:** já mandei pro bicho aqui

**Marcelo Costa:** Fala,

**Off Digital:** com

**Marcelo Costa:** quero ver o que você vai fazer.

**Off Digital:** e eu tô botei umas tescas aqui do Codex, né, que vai virar hoje meu meu limite. Eu tô com 25% sobrando

**Marcelo Costa:** p\*\*\*\*, o meu, eu vou comendo ele devagarzinho e depois paro ele. Ó, ele já tá nos 75%.

**Off Digital:** ainda.

### 00:05:59 {#00:05:59}

**Marcelo Costa:** O meu tá ol custo dos 30 dias e bota custo dos 30 dias 50 conto. 50 eu não pago isso.

**Off Digital:** Ok.

**Marcelo Costa:** Tô aqui, tô vendo num acho que é se fosse por token. Eu baixei uma extensãozinha que fica lá em cima, ele fica mostrando para você qual como que você tá nas sessões, né?

**Off Digital:** Aham.

**Marcelo Costa:** Aí o Cloud também tá até a tampa.

**Off Digital:** Custo dos últimos 30 dias.

**Marcelo Costa:** É,

**Off Digital:** o seu

**Marcelo Costa:** ele tá dando 50 conto, mas eu pago 20\. Como é que pode tá dando 50?

**Off Digital:** é porque se fosse em API,

**Marcelo Costa:** É,

**Off Digital:** né?

**Marcelo Costa:** se fosse em token. É isso que ele tá mostrando,

**Off Digital:** Ô louco, prêmio,

**Marcelo Costa:** né?

**Off Digital:** você paga 20 o do Cloud.

**Marcelo Costa:** O do Codex eu fico, eu tô ficou, né? Porque eu não dou conta de comer ele,

**Off Digital:** Ah, o codex você paga 20,

**Marcelo Costa:** velho. É porque eu não,

**Off Digital:** entendeu?

**Marcelo Costa:** eu eu fico mais no cloud,

**Off Digital:** Não,

**Marcelo Costa:** né?

**Off Digital:** eu pensei que você pagava 20 do Cláudio. Eu ia falar, pô, para mim tá fazendo mágica.

### 00:07:08 {#00:07:08}

**Marcelo Costa:** Não, aí não tem o que fazer mais. Agora quem tá

**Off Digital:** Ó aí, priminho. Ó como é que,

**Marcelo Costa:** rendendo,

**Off Digital:** ó como é que tá o dos meus 30 dias do Codex. Mandar para você aí no no

**Marcelo Costa:** quem tá rendendo é o é o design,

**Off Digital:** zap.

**Marcelo Costa:** hein, primo.

**Off Digital:** Design tá brilhando, né?

**Marcelo Costa:** Nossa. Seis pa. Isso é se fosse, mas aí é a de aí ele for só hoje. Mas isso aqui se fosse tok.

**Off Digital:** É se API, né? É o meu consumo de token, velho. Meu consumo de

**Marcelo Costa:** É, mas é assim, o cara já vai dando a letra pro seu irmão.

**Off Digital:** token

**Marcelo Costa:** Vê se isso aqui faz sentido pro seu trampo, né? Porque daqui a pouco a hora que virar para toque, meu irmão.

**Off Digital:** é o velho,

**Marcelo Costa:** Agora o seu,

**Off Digital:** se tô com

**Marcelo Costa:** você tá usando bastante o design. Para mim,

**Off Digital:** estrada

**Marcelo Costa:** ele nem ele não aparece mais no ele não come mais, velho. Tá sempre 100% e toca pau, velho.

**Off Digital:** sério. Cuidado, velho.

**Marcelo Costa:** É,

**Off Digital:** Porque o meu quando ficou assim, ele tava comendo do dos créditos.

### 00:08:09

**Marcelo Costa:** ele não tem onde pegar.

**Off Digital:** Não

**Marcelo Costa:** Ele pode até tentar, velho. Se ele achar algum fundo,

**Off Digital:** tem,

**Marcelo Costa:** ele que me fale onde é que tá.

**Off Digital:** rapaz.

**Marcelo Costa:** Cara,

**Off Digital:** Primív aí direitinho em cima.

**Marcelo Costa:** eu tô metendo ficha,

**Off Digital:** Não tá ligado em algum cartão,

**Marcelo Costa:** fazendo apresentação, metendo louco e ele não mexe,

**Off Digital:** velho.

**Marcelo Costa:** velho.

**Off Digital:** E mas tá no 100\.

**Marcelo Costa:** 100% left. Ele mostra aqui para mim.

**Off Digital:** Ah, 100% left.

**Marcelo Costa:** É, ou seja, tá livre, né? Tem sobrando, não é isso?

**Off Digital:** Uhum.

**Marcelo Costa:** E ele não mexe o ponteiro do design, velho.

**Off Digital:** Que doideira. Para mim bugou,

**Marcelo Costa:** Bugou, man. Que bom,

**Off Digital:** mano. Você não tá ligado que que eu tô fazendo com o design.

**Marcelo Costa:** né?

**Off Digital:** Não, velho, eu eu velho eu tô eu vou preciso criar um Twitter para começar a postar as paradas, porque Nego vai desacreditar.

**Marcelo Costa:** Vai chover de negro, velho.

**Off Digital:** É, Nego vai, mano. Eu eu velho, eu eu procurei todo mundo, os cara mais pica que eu sigo, velho.

### 00:09:08 {#00:09:08}

**Off Digital:** Ninguém tá fazendo isso, tá ligado? Calma aí, 6%. Ô louco. Ô louco. Reset em 35 minutos.

**Marcelo Costa:** tá comendo você pelas beiradas, primo.

**Off Digital:** c\*\*\*\*\*\*, velho. Nunca eu nunca estouri o limite de 5 horas do Não, mas beleza, daqui a pouco libera de novo. Será que eu mandei alguma coisa muito muito punk aqui, velho?

**Marcelo Costa:** Não foi o mitos aí que você já mandou ele comer com token

**Off Digital:** Não, não, não. No, no,

**Marcelo Costa:** aí?

**Off Digital:** no priminha. Eu tô muito quente aqui na parada, velho. Eh, eh, mano, várias coisas que eu nunca vi ninguém usando. Por exemplo, tá vendo minha tela aí?

**Marcelo Costa:** Deixa eu jogar ela maior aqui. Tô vendo agora.

**Off Digital:** Se liga, por exemplo, eu tô no Codex, né?

**Marcelo Costa:** Certo?

**Off Digital:** Só que eu tô usando o cloud Code dentro do Codex.

**Marcelo Costa:** Sim. Abriu o outro terminalzinho do lado

**Off Digital:** É, então, tipo assim, eu tô usando basicamente,

**Marcelo Costa:** ali.

**Off Digital:** velho, só o Codex, tá ligado? Vou deixar ele escuro aqui.

**Marcelo Costa:** Fica mais fácil de visual, né?

**Off Digital:** Vamos ver deixar ele no buraquezão aqui.

### 00:10:50

**Off Digital:** Não ficar muito escuro. Vou deixar aqui aí, priminho. Olha só que bagulho louco. Codex tem o browser aqui, né,

**Marcelo Costa:** Quando você vai ali do lado, você escolhe browser.

**Off Digital:** cara? Essa eu não vi ninguém fazendo para mim.

**Marcelo Costa:** Beleza.

**Off Digital:** Você abre aqui, ó. Bra.

**Marcelo Costa:** Abriu o cloud no browser.

**Off Digital:** Abriu o cloud no browser. Só que aí eu vou botar o

**Marcelo Costa:** Eh,

**Off Digital:** design.

**Marcelo Costa:** e aí bota ele para torar. Aí, em vez de você ficar no chat do design, você fica no chat desse, mandando ele fazer as paradas.

**Off Digital:** Aí eu vou pegar aqui, por exemplo, eu vou abrir Eh, cadê? Eu quero criar um novo, pô.

**Marcelo Costa:** É, aí tá novo sem

**Off Digital:** Okay.

**Marcelo Costa:** nada. Ah, agora eu já entendi. É porque você depois você pode mexer nele no edit, né?

**Off Digital:** Vou ver se meu me crédito vai aguentar aqui que ele tá tá metendo o pau. Mas só para você ver, só para você ver o o básico aqui. Ô, velho, é muito louca a parada.

**Marcelo Costa:** É porque aí depois você mexe nele no edit. Você mexe no edit depois,

### 00:13:19 {#00:13:19}

**Off Digital:** Hã,

**Marcelo Costa:** porque mexer no

**Off Digital:** não, velho. Eu tô eu tô usando o cloud design,

**Marcelo Costa:** edit

**Off Digital:** só que eu tô usando o Cordex para dar os prompt para ele.

**Marcelo Costa:** ao invés de vou, porque você poderia dar o prompt para ele lá embaixo, mas é que ele melhora o prompt para acertar lá,

**Off Digital:** Poderia, só que, velho,

**Marcelo Costa:** né?

**Off Digital:** eu tô usando o cara como meu copiloto, né? Não tô fazendo sozinho, tá fazendo eu e o Codex.

**Marcelo Costa:** Entendi.

**Off Digital:** É outra parada, né?

**Marcelo Costa:** E outra, ele quando você, por exemplo,

**Off Digital:** Ó,

**Marcelo Costa:** você cria um negócio,

**Off Digital:** ó, ele já tá mexendo. Quer ver? Hã, pode falar.

**Marcelo Costa:** você cria uma parada no design, aí você pode mexer no edit lá mexer na no tamanho da fonte,

**Off Digital:** Sim,

**Marcelo Costa:** mexer no negócio.

**Off Digital:** eu mexo em qualquer coisa

**Marcelo Costa:** Então agora ou você,

**Off Digital:** aqui.

**Marcelo Costa:** se você fica mexendo pelo chat, ele fica comendo. Agora se você vai no edit e vai mexer, ele não fica comendo saldo enquanto você tá mexendo.

**Off Digital:** Ah, sim, sim, sim,

**Marcelo Costa:** Então você põe ele para mexer na mão.

### 00:14:16 {#00:14:16}

**Off Digital:** sim.

**Marcelo Costa:** Você não vai ficar você indo live e dando dando dando ordem no chat dele.

**Off Digital:** Ah, sim. Eu posso mandar ele mexer na mão ou mandar ele mexer no prompt,

**Marcelo Costa:** M.

**Off Digital:** mas o ponto, velho, é tipo o Codex é a melhor harness atualmente. O aplicativo é o melhor aplicativo que tem, independente do modelo que você usa. Só que, mano, você poder utilizar outras coisas com harness do Codex, que é tipo, p\*\*\*\*, não é só o prompt, por exemplo, eu posso usar qualquer skill aqui, eu posso usar o browser, computer use, github, posso usar os plugins dele, posso usar, pô,

**Marcelo Costa:** Ага.

**Off Digital:** todas as skins que eu tenho aqui do Codex, entendeu? Eh, então, tipo, o harness é a palavra que a galera fala muito hoje em dia.

**Marcelo Costa:** Ela

**Off Digital:** O harness é tipo, é o conjunto de ferramentas que você tem em cima do modelo, ó. Ó ele digitando o Cloud. Eu não ia digitar esse propt assim, nem f\*\*\*\*\*\*,

**Marcelo Costa:** nunca e nem nessa velocidade você ia tá ditando e tudo torto.

**Off Digital:** ó.

**Marcelo Costa:** Vou fazer isso logo menos, velho. Tô montando um media kit aqui que já ficou muito bom, velho. Já é muito Já. Ele já tá nervoso, né,

### 00:15:43

**Off Digital:** Não, para mim,

**Marcelo Costa:** velho?

**Off Digital:** ó, velho, isso aqui, velho, eu vou te falar, cada coisa que eu tô descobrindo aqui esses dias que eu tô falando, velho, aí eu vou no Twitter, eu fico procurando a galera e falou: "Mano, ninguém tá falando disso, ninguém tá fazendo isso". Ou nego tá guardando para si ou nego ainda não. É porque é tanta coisa, né, priminho? Tanta coisa, neguinho.

**Marcelo Costa:** É muita coisa,

**Off Digital:** Só que aqui,

**Marcelo Costa:** velho.

**Off Digital:** ó,

**Marcelo Costa:** E e

**Off Digital:** eu vou botar o modelo novo, ó. Fabo. Fabo,

**Marcelo Costa:** oh,

**Off Digital:** galera, não é mais off. Aqui é o Fabão, entendeu? Fabão aí, ó. Deixa eu ver se acabou meus créditos.

**Marcelo Costa:** os cara já tão no outro naipe do

**Off Digital:** Acabou. 100% usado. Deu, acabou. Beleza,

**Marcelo Costa:** quê?

**Off Digital:** acabou meus acabou meus codex aqui. Reseta em 28 minutos. Beleza, mas já digitou,

**Marcelo Costa:** M.

**Off Digital:** já deu para você ver. Era isso que eu queria. Queria só te mostrar aí.

### 00:16:34 {#00:16:34}

**Off Digital:** Beleza, vamos mandar aqui, ó. Só que o que que é mais f\*\*\*? Eu dou promp. Eu falo assim: "Você vai ser o orquestrador e o Codex é teu designer". Então, meu, você só termina com ele quando fica, p\*\*\*\*, imagina você criar várias páginas de produto, tá ligado? Você fala: "Velho, você vai criar essa parte depois essa, depois você monta o plano com ele e ele vai delegando pro Cloud".

**Marcelo Costa:** É, é, pô, cara,

**Off Digital:** Entendeu?

**Marcelo Costa:** eu acabei de eu acabei de é o para produto, né? Você vai montando as páginas, vai montando tudo, né,

**Off Digital:** Não,

**Marcelo Costa:** velho?

**Off Digital:** é loucura, velho. É loucura. O jeito que, pô, velho, o jeito que eu tô usando as paradas aqui, o próprio Gmail, velho. Eu abro, por exemplo, eh, eu abri meu Gmail aí para você logar nas coisas no Codex, ele bloqueia login via Google. Aí, porque ele não abre popup. Tudo que abre popup não rola dentro do Codex. Aí eu tive que logar via e-mail mesmo.

**Marcelo Costa:** Так.

**Off Digital:** Aí manda os códigos, né? Aí, pô, eu loguei numa parada, ele mandou o código pro e-mail, eu tenho que pegar o código, copiar, botar lá para logar.

### 00:17:39

**Off Digital:** Aí ele mandou um, aí eu fui logar em outra coisa, ele mandou outro. Aí eu falei, quer saber de uma coisa? Logo aqui no meu e-mail, deixei uma aba de e-mail aberto e falei: "Tudo que você for logar, você manda pro e-mail, você pega no meu e-mail e você mesmo loga".

**Marcelo Costa:** E toca pau, meu irmão.

**Off Digital:** Olha, cara, mano, cara,

**Marcelo Costa:** Segurança 100%,

**Off Digital:** é muito louco,

**Marcelo Costa:** meu irmão.

**Off Digital:** cara.

**Marcelo Costa:** Pega tudo aí.

**Off Digital:** É muito louco, velho. Todo dia eu tô trabalhando e eu fico tendo umas ideias assim. Não, esse cara esse aí, pô, botei ele para editar um vídeo hoje. Abri o bagulho porque tem o esse negócio que eu uso aqui, ó. Isso aqui, ó, é tipo como se fosse um capcut, só que ele é diferente, ele tem umas paradas de A e tal. Aí, beleza. Esse aqui, né? Aí, p\*\*\*\*, ele tem uns negócios aqui animal. É que eu falei para você até no telefone. Ele tem uns negócios tipo,

**Marcelo Costa:** Sim,

**Off Digital:** velho, ele tem umas legendas f\*\*\*. Quer ver?

### 00:18:58 {#00:18:58}

**Off Digital:** Deixa eu pegar um vídeo aqui.

**Marcelo Costa:** você tem que aprender a mexer. né?

**Off Digital:** Não, ele é tipo cut,

**Marcelo Costa:** Aí se ele bota aí para fazer

**Off Digital:** mano. Só que ele é ele é mais highch de a, tá ligado? Ele tem umas partes, tipo, por exemplo, eh, deve tá saindo o som para você, mas, por exemplo, aqui,

**Marcelo Costa:** Bom,

**Off Digital:** ó, botar aqui para ele criar as legendas. Ele cria igual no Capcant, né? Normal. Já deve ter mexido alguma vez com ah,

**Marcelo Costa:** Sim, já vi, já

**Off Digital:** só que tipo,

**Marcelo Costa:** vi.

**Off Digital:** eu vou te mostrar, deixa ele gerar as legendas que eu vou te mostrar que ele tem uns negócios diferentes. Ele tem várias coisas de A, inclusive ele tem aquele Sidence que é o modelo chinês lá mais pica de todos, ele já vem os créditos aqui, entendeu? Se você quiser criar as paradas, ó, ele vem aqui, ó, legendinha. Só que p\*\*\*\*, olha os modelos de legenda que ele tem aqui diferentão, ó.

**Marcelo Costa:** Ne.

**Off Digital:** Calma aí. Você põe aqui, ó. Como é que é o negócio? Você põe aqui, ó. Ó,

### 00:19:53

**Marcelo Costa:** Eh

**Off Digital:** põe aqui, ó. É parada. to timeline aqui. Você põe aquele põe o texto atrás da pessoa, tá ligado?

**Marcelo Costa:** tô ligado.

**Off Digital:** Tentando é,

**Marcelo Costa:** Eu vi, deu para ver a imagem aí que apareceu igual a mina

**Off Digital:** ele põe o texto atrás da pessoa, mano. Faz, velho,

**Marcelo Costa:** ali.

**Off Digital:** é, ele faz uns bagulhos muito louco. Ele tem umas legendas muito f\*\*\*, tá ligado? Tipo que a galera nem tá usando aqui ainda no Brasil. Eu só não tô não tô lembrando o que que tem que fazer, mas tem um bagulho aqui que você libera que ele coloca. Deixa eu ver se é isso aqui. Dette. p\*\*\*\*, velho. No outro, no outro eu consegui usar, velho. Add eclipse your timeline to. Aqui, ó. Tá aplicando aqui, ó.

**Marcelo Costa:** É,

**Off Digital:** App text behind.

**Marcelo Costa:** se tivesse com a agência hoje, né, Priminh?

**Off Digital:** Ah, mas eu não fico, vou fazer ficar fazendo isso para cliente, mano. Tá louco agora paraa mina, sacou? Eu faço tal. Ah, pô, faz aí, eu faço. Aí tem várias coisas,

### 00:21:08

**Marcelo Costa:** É.

**Off Digital:** priminho. Tem umas transição muito louca aqui do Ei transitions. Tem as transição aqui, ó. Você fazia, p\*\*\*\*, velho. Uns bagulhos f\*\*\*, tá ligado? Ó,

**Marcelo Costa:** Você

**Off Digital:** essa aqui tem várias paradas treta aí. Que que eu faço?

**Marcelo Costa:** abre ali dentro do Codex,

**Off Digital:** É, velho, eu abro ele dentro do CD que manda ele editar para mim a parada, sacou,

**Marcelo Costa:** fala:

**Off Digital:** velho?

**Marcelo Costa:** "Faz isso, vê o que dá para

**Off Digital:** Fala, velho, põe a legenda para mim, exclui. Eh,

**Marcelo Costa:** fazer".

**Off Digital:** seleciona o PR dinâmico aí, manda manda botar por trás do do do velho da pessoa, faz o p\*\*\*\*, velho,

**Marcelo Costa:** É.

**Off Digital:** doideira.

**Marcelo Costa:** E aí você vai dando ideia e ele vai metendo a

**Off Digital:** E aí, mano, o que que eu posso fazer?

**Marcelo Costa:** mão.

**Off Digital:** Eu posso pegar do celular aqui no aplicativo do Codex e ficar ditando para ele, entendeu? p\*\*\*\*, tô indo passear com o dog. Eu falo: "Velho, edita o vídeo aí para mim". A Emily, p\*\*\*\*,

**Marcelo Costa:** É só tá a única coisa que tá faltando para mim é começar a editar vídeo,

### 00:22:07

**Off Digital:** mandou.

**Marcelo Costa:** prima. Aí eu tô

**Off Digital:** p\*\*\*\*, não, velho. Tá lá no e-mail, tá lá no e-mail. A Emily já mandou lá no e-mail.

**Marcelo Costa:** f\*\*\*\*\*.

**Off Digital:** Só abre lá no Gmail, sobe lá no víde, entendeu? Jabó é aquela legenda lá que a gente gosta daquele jeito. Eh, corta o silêncio dos áudios, pá, mano. Isso para tudo, primim. Imagina,

**Marcelo Costa:** Como é que chama? Ele é vid.

**Off Digital:** tipo,

**Marcelo Costa:** É

**Off Digital:** é com dois e v e d.

**Marcelo Costa:** V.

**Off Digital:** Eh,

**Marcelo Costa:** Dar um salvar nele aqui para eu dar uma olhada depois. Mas ele é essa tela preta mesmo. Vid ai

**Off Digital:** I I não ved.

**Marcelo Costa:** ved. Só que aí ele entra num outro site. Acho que os caras copiaram ele aqui. É o de baixo, ó.

**Off Digital:** É vídeo. Mm.

**Marcelo Costa:** E e é que teve um cara que usou o nome dele,

**Off Digital:** V. Se você botar

**Marcelo Costa:** mas ele pulou lá na frente. Agora já achei ele aqui.

**Off Digital:** no

**Marcelo Costa:** Deixa eu botar salvar ele aqui em AI. É, priminho, o bagulho tá louco.

### 00:23:26 {#00:23:26}

**Marcelo Costa:** Nós precisamos monetizar, velho.

**Off Digital:** M.

**Marcelo Costa:** Nós precisamos monetizar urgente. О.

**Off Digital:** Só ver se tá tudo inteiro aqui, velho. que eu mandei o bicho mexendo as paradas lá, não sei nem o que que deu. Eh, vamos testando aqui, primo.

**Marcelo Costa:** Vamos.

**Off Digital:** rapaz. E bateu 100% mesmo. 20 minutos. Certeza que eles vão lançar um

**Marcelo Costa:** alguma coisa,

**Off Digital:** certeza que eles vão lançar um GPT novo também.

**Marcelo Costa:** né?

**Off Digital:** Agora que o Cláudio lançou, eles já vão lançar também. Com certeza.

**Marcelo Costa:** E nós estamos aí de testador, meu irmão. Conte conosco, né? Kquil

**Off Digital:** Eh, Mateus, vou botar aqui para saber que é o teste do Mateus.

**Marcelo Costa:** nós.

**Off Digital:** Beleza, nós estamos sem crédito, não dá nada que eu não vou precisar agora. Show de bola. E aí nós vamos subir de novo,

**Marcelo Costa:** Aí que eu perdi o você.

**Off Digital:** não é isso?

**Marcelo Costa:** Eh, vamos começar a subir o cara.

**Off Digital:** Eu

**Marcelo Costa:** Deixa eu ver que que eu Pera aí que eu perdi. Onde é que eu tô? Às vezes o cara se perde,

### 00:25:14 {#00:25:14}

**Off Digital:** vou eu vou apagar tudo aqui então, priminho.

**Marcelo Costa:** apaga tudo e vamos subir esse cabra aí, não é isso?

**Off Digital:** Isso.

**Marcelo Costa:** Deixa eu voltar nas minhas páginas correta aqui para eu ver onde é que nós estamos. Cadê o cara? V,

**Off Digital:** E vamos fazer a matriz também de novo.

**Marcelo Costa:** vamos criar uma pagando aquelas porras, né?

**Off Digital:** Vamos, vamos, porque lembra que a gente ficou com o 92 e o 95 lá. Excluir. Você quer que eu crie a matriz aqui enquanto você vai vai criando o candidato?

**Marcelo Costa:** Ó, deixa eu só conseguir abrir aqui. Eu me perdi. Não tô achando onde que tá os Onde é que tá a p\*\*\*\* aqui. Cadê o f\*\*\*\*\*\*\*\*\*\*\*\*?

**Off Digital:** Bom, eu vou exclu, já excluí, prim, já excluí, já excluí a matriz também.

**Marcelo Costa:** Aí, achei, tava perdido aqui as

**Off Digital:** Também eu disparei 30 agentes aqui.

**Marcelo Costa:** telas.

**Off Digital:** Todos os 30 agentes já foram disparados ao longo das rodadas. Ah\!

**Marcelo Costa:** Vamos lá. Vou entrar no certify agora. Deixa eu apagar essa p\*\*\*\* aqui que eu não preciso disso agora, nem disso. Isso aqui vai ficar para depois.

### 00:26:46

**Marcelo Costa:** Esse aqui eu vou falar depois também. Você vão falar depois. Agora eu vou para cá. Nós vamos pegar lá. Vamos mexer na matriz. Você apagou tudo os caras?

**Off Digital:** Paguei tudo, os cara e e a matriz já

**Marcelo Costa:** Vai criar então a matriz nova. Você não você apagou ela

**Off Digital:** paguei. Vamos criar

**Marcelo Costa:** inteira.

**Off Digital:** novo.

**Marcelo Costa:** Então vamos lá, priminho. Quer quer ir na matriz, eu vou criando. Como é que você quer fazer?

**Off Digital:** Não, vocêou vou vou deixar você subir aí para para você sentir se agora ficou legal com os códigos novos lá do que eu botei ontem.

**Marcelo Costa:** Ah.

**Off Digital:** Mandar só no banheiro aqui.

**Marcelo Costa:** Приме. certificar agora apareceu aqui.

**Off Digital:** Ja.

**Marcelo Costa:** Beleza. Okay. F

**Off Digital:** M. Ja.

**Marcelo Costa:** อ

**Off Digital:** E aí, prim?

**Marcelo Costa:** Ora matriz. criada aqui. Belê, matriz criada. Agora vamos lá no candidato.

**Off Digital:** quer pôr sua tela

**Marcelo Costa:** Pera,

**Off Digital:** aí?

**Marcelo Costa:** deixa eu só dar um limpo aqui nos meus download para ele Aí, que que eu vou fazer? Vou vir aqui no certifi de máquina.

### 00:38:25

**Marcelo Costa:** V abrir esse coisa aqui. Ó, esse cara aqui no certify, ele tá completo e o mesmo cara de ontem. Então, já vou baixar o zip aqui dele,

**Off Digital:** Tá.

**Marcelo Costa:** ó, que vem só os documentos completos, apesar dele ter subido um monte de outra coisa, né? Era bom subir tudo isso também, né?

**Off Digital:** Tem aí para baixar esse também.

**Marcelo Costa:** Dur, deixa eu ver se ele vai exportar. Como é que ele exporta tudo isso aqui? É só que esse aqui vem em CVS.

**Off Digital:** Vamos subir esses aí para confirmar o que a A gente fez ontem melhor.

**Marcelo Costa:** Ele ele manda só com um link pro download,

**Off Digital:** Ja.

**Marcelo Costa:** né? Aí teria que fazer os download aqui. Mas então vamos subir, vamos subir esse primeiro aqui. Então vamos criar o

**Off Digital:** Ja.

**Marcelo Costa:** Você

**Off Digital:** É, vai ser um teste bom, porque tá mexendo no código aqui, nem sei se quebrou alguma coisa.

**Marcelo Costa:** mexeu o que que era que a gente tinha parado ontem mesmo? Era no finalzinho, né?

**Off Digital:** Tá demorando muito já, hein, mim?

**Marcelo Costa:** Não. Aí, ó. Agora ele tem que dar no meio. Tem um que tá vencido, né?

**Off Digital:** Tem um que tá vencido.

### 00:41:46 {#00:41:46}

**Marcelo Costa:** Lembra?

**Off Digital:** Você botou agora o 5195 ou 5198?

**Marcelo Costa:** Botei 595\.

**Off Digital:** Então ele tem que dar um pendente e o resto confere. Não,

**Marcelo Costa:** É exato.

**Off Digital:** um parcial e o resto confere.

**Marcelo Costa:** Que é um parcial que é aquele da vencido,

**Off Digital:** é o vencido.

**Marcelo Costa:** né? O resto era para bater.

**Off Digital:** Boa.

**Marcelo Costa:** Boa.

**Off Digital:** E o pendente ali,

**Marcelo Costa:** Tem um excedente.

**Off Digital:** documento não classificado.

**Marcelo Costa:** Vamos ver o que houve. É aquele certificado de

**Off Digital:** Não,

**Marcelo Costa:** competência,

**Off Digital:** classificado. Pode ter dado problema no comite aqui, velho, da da da mudança que eu fiz.

**Marcelo Costa:** ó. Porque veja esse aqui tinha e ele deu parcial nesse por causa da data, ó. Documento vencido.

**Off Digital:** Sim.

**Marcelo Costa:** Beleza.

**Off Digital:** Vê qual que tá pendente ali, primo.

**Marcelo Costa:** Esse aqui você tá falando.

**Off Digital:** Não tem um pendente.

**Marcelo Costa:** É, então que é o ele não reconheceu.

**Off Digital:** Ah, tá. que foi esse que ele não reconheceu ali de baixo.

**Marcelo Costa:** É,

**Off Digital:** Ele jogou para excedente.

**Marcelo Costa:** vamos apagar e subir de novo só para ver o que

### 00:44:15

**Off Digital:** Não, não, pera aí. Dá,

**Marcelo Costa:** acontece.

**Off Digital:** vai dar, tá dando um minuto para resetar meu codex aqui. Eu já vou, eu tô com a tela aberta do do negócio de ontem. Eu acho que foi algum problema de comit. Deve ter comitado alguma coisa por cima e não pegou o Mas na base tinha lá para você colocar, né?

**Marcelo Costa:** Tinha coque aqui, ó.

**Off Digital:** Tá. Deixa eu já perguntar para ele antes da gente subir de novo. Deixa eu abrir aqui também. Pera aí. Se eu te falei,

**Marcelo Costa:** Deixa eu ver uma parada no gêno que eu tava vendo ontem.

**Off Digital:** ele foi para Ah, não, esse aqui foi.

**Marcelo Costa:** Ah. Ага.

**Off Digital:** Beleza, liberou aqui. Já tô botando ele para ver. Так.

**Marcelo Costa:** Ah, beleza. Tá certinho esse aqui.

**Off Digital:** p\*\*\*\*, isso é bom aí, prim, pra gente pegar esses bug pelo por dentro do Codex aqui pelo browser. Eu não tinha pensado isso, velho.

**Marcelo Costa:** para ele já ir vendo e já falando.

**Off Digital:** Já viu, já abriu o documento aqui, falou: "Velho, tá correto?

**Marcelo Costa:** Primo, quando você recebe um, você recebe um documento lá, um Word, quando você abre no Mac, não dá para ele abrir direto no no drive, ele abrir já

### 00:50:46

**Off Digital:** p\*\*\*\*, velho,

**Marcelo Costa:** Não.

**Off Digital:** tem um jeito se você botar com o botão direito, botar para sempre abrir, só que é meio estranho. Ele abre o navegador.

**Marcelo Costa:** Porque sempre eu baixo aí quer jogar no no palê direito,

**Off Digital:** Isso é um pau que eu é isso é um pau que eu tenho também,

**Marcelo Costa:** senão ele abre naquele

**Off Digital:** velho. Tipo,

**Marcelo Costa:** mesmo.

**Off Digital:** p\*\*\*\*, você tem que jogar no navegador para subir ele no drive para abrir. É maior saco, né, velho?

**Marcelo Costa:** Pelo menos é bom que você já organiza e bota no drive, senão ele fica solto, né?

**Off Digital:** É. M tá vendo aqui, ele não falou nada ainda, mas pelo rolê que ele tá fazendo, eu acho que é porque não tem a coluna ainda criada nos péis desse código.

**Marcelo Costa:** Mas ontem ele leu,

**Off Digital:** M.

**Marcelo Costa:** né? Elek.

**Off Digital:** É, mas ele leu forçado, né? Eu eu foi o agente que perguntou se eu queria que ele reprocessasse e ele mesmo reprocessou, não foi a gente que subiu. Hum. A pagininha que ele fez, primo, no

**Marcelo Costa:** No quê?

**Off Digital:** prompt que a gente mandou lá do cloud design.

**Marcelo Costa:** Cadê? É que eu não tô com sua tela aí.

### 00:54:13 {#00:54:13}

**Off Digital:** Mandar o print aqui. Mandei aí para você.

**Marcelo Costa:** Ah, você pediu para fazer uma página de venda, tipo

**Off Digital:** Falei só Hero. É, faz só a hero de uma página para só para para te mostrar, né? Só de teste.

**Marcelo Costa:** O bagulho é cabuloso,

**Off Digital:** Não especifiquei nada,

**Marcelo Costa:** né?

**Off Digital:** né? Só falei, velho, faz aí, entra no entra no na pasta do projeto, veja aí e pede para ele fazer uma

**Marcelo Costa:** Não. E a hora que você tem os os layout já definido,

**Off Digital:** rio.

**Marcelo Costa:** que você já cria ali, p\*\*\*\*, para você só

**Off Digital:** É, priminho, produtinho vai ficar bala. Esse produtinho vai ficar bala, meu irmão. Vamos ver. Observado. Tá tá tá. O que aconteceu? A CR lê o documento. Vê depois. Classificação gravou o arquivo como siglo STCW. Regra genérica não como requisito coqu tá normalização ainda marcou inferido como documento não virou médico cató resultado o coco ficou pendente o arquivo caiu em excedentes crios é fácil Eu já vou chamar é o brabo aqui.

**Marcelo Costa:** Vai, bota para ver o que ele vai fazer.

**Off Digital:** Cadê Fabão.

### 00:58:05 {#00:58:05}

**Off Digital:** Vou matar esse primo. Vai preparando uma outra matriz aí.

**Marcelo Costa:** Vamos, vamos subir mais candidatos nessa, né?

**Off Digital:** Subir mais nessa

**Marcelo Costa:** É, subir mais uns candidatos nessa. Deixa eu pegar, vou pegar mais uma casca aqui.

**Off Digital:** observador faz o fiz skillzinha aqui da hora também para mim de quando ele precisar me explicar, ele usar diagrama. Ó, se liga

**Marcelo Costa:** Deixa eu sou, deixa eu parar aqui.

**Off Digital:** aqui.

**Marcelo Costa:** Ja.

**Off Digital:** Ó, ele falou aqui, eu falei: "Ah, já tinha arrumado isso antes. Por que que tá rolando esse gargalo?" Ele falou: "Verifiquei".

**Marcelo Costa:** Ja.

**Off Digital:** Sim, o fix anterior existia, ele corrigia a matriz, não esse ponto do fluxo. A matriz da vaga tá correta. O item qual que virou? Tal tal tal. O documento também eh tem sinais no CR. O gargalo tá antes da comparação. O extrator gravou o documento como sigla STCW. Código bruto. A normalização caiu no genérico coque STCWg e não no específico coque engine lá inferido. O fix anterior resolveu quando a matriz pede coco específico. Esse caso exige outro fix. Quando o documento chega como certificado de competência genérica usar 3/1 mais capacidade pá para promover o coque específico.

### 00:59:49

**Off Digital:** Tem um guardio segurando isso. Blá blá blá. Eu falei qual o fixo definitivo, não só pro coque, mas para todos os documentos similares da mesma família. Aí ele já veio tudo com com o esquema da skill que eu criei, ó. Nem pedi,

**Marcelo Costa:** Mas aí você nem pediu para ele usar a skill.

**Off Digital:** nem pedi. Ele já usou no automático. Aí eu a skill é velho,

**Marcelo Costa:** E cadê a skill?

**Off Digital:** toda vez

**Marcelo Costa:** Como é que vocêou ela?

**Off Digital:** hã a skill fica no

**Marcelo Costa:** Cadê ela? A skill fica onde?

**Off Digital:** meu, no repositório do Git que fica todas minhas skills, que eu compartilho ela com Cloud, com Codex e com os agentes.

**Marcelo Costa:** E você que criou essa ou já pegou uma prontinha?

**Off Digital:** Eu que criei.

**Marcelo Costa:** Meia

**Off Digital:** Eu que criei. que uma hora ele me explicou,

**Marcelo Costa:** pronta.

**Off Digital:** aí eu falei para ele, velho, me explica de forma mais simples, com diagrama, não sei das quantas. Aí ele me explicou, aí ficou legal. Falei, faz uma skill disso, tá ligado? E aí ele ele, ó, fix definitivo,

**Marcelo Costa:** Sim.

**Off Digital:** tirar a decisão da segraída e colocar no resolvedor de perfil documental por evidências.

### 01:00:50 {#01:00:50}

**Off Digital:** Hoje o pipelines traz sigla, nome e código, tenta catalogar, depois comparar com a matriz. Quando o documento chega como STCW, ele para em qual que STCW G, o fix antigo resolve a matriz e tal, tal. O gargala é estrutural. Documentos STCW, DPC, COC certificados com múltiplas regras, MR com inicial, tal, tal. Ahã podem depender só de aliás ou sigla, eles precisam de um resolvedor de perfil. Aliás, ideia, né? Então, PDF OCR, extrair fatos, resolvedor de perfil, compara com a matriz, confere parcial revisão. Então, nós vamos criar um novo, uma nova parada no fluxo, que é o resolvedor de

**Marcelo Costa:** É, é só que veja um um ponto assim,

**Off Digital:** perfil.

**Marcelo Costa:** ó, ele tem que o STCW, o código é o que manda. Então, cara, o código, por exemplo, esse código, o ah, 3/1 é a 3/1, velho. O outro que é gerencial é a 3/2. Cara, você não precisa mais alguém, cara. É o código, velho. O código é esse que eu escolhi. Olha o código e acabou. Não tem mais o que você ficar olhando. Diferente da NR que eu tenho que ter um contexto, tal.

### 01:02:05 {#01:02:05}

**Marcelo Costa:** Isso aí é código. É código, velho. Senão ele vai inventando muita coisa, né?

**Off Digital:** Será que o código ele já ele Já.

**Marcelo Costa:** Por exemplo, o operacional é o 3/1, o gerencial é 3/2. Então ele, p\*\*\*\*, os códigos dele, cara, sim. Ó, se dá o código regulatório.

**Off Digital:** Outra coisa que é da hora também, se liga.

**Marcelo Costa:** Então, mas então ele resolveu lá no código, né?

**Off Digital:** O quê?

**Marcelo Costa:** Ele tá resolvendo no código, não é isso que ele falou

**Off Digital:** Não, ele vai ele vai planejar como a gente vai resolver isso.

**Marcelo Costa:** aí? Ah,

**Off Digital:** Manda pro chefão aí. Vamos ver.

**Marcelo Costa:** e aí você tem que marcar o browser para ele ir para lá, né?

**Off Digital:** Tem que tá

**Marcelo Costa:** Mas esse browser que você botou,

**Off Digital:** aberto.

**Marcelo Costa:** você colocou, você teve que dar um @browser para ele ir para lá ou ele já

**Off Digital:** Ah, sim. sempre. Eu não sei

**Marcelo Costa:** identifica?

**Off Digital:** Isso é muito roubar no jogo, né? Porque, velho, os caras não quer de jeito nenhum que você interaja com Cloud, mano. Você tá agindo com Cloud do jeito mais puro, ó lá.

### 01:05:58 {#01:05:58}

**Off Digital:** Tipo assim, você tá literalmente botando ele para interagir.

**Marcelo Costa:** Se explica lá pro cara, meu irmão.

**Off Digital:** É,

**Marcelo Costa:** Se explica pro cara,

**Off Digital:** é,

**Marcelo Costa:** né?

**Off Digital:** velho. Você explica pro cara, troca uma ideia. Ó lá, vou escrever pro Cláudio pelo caminho direto no browser. E eu nunca falo, ó. Ó ele escrevendo pro Cláudio. Faz ideia que o bicho tá

**Marcelo Costa:** Eh

**Off Digital:** mandando.

**Marcelo Costa:** Eh, que que é parcer? Ele sempre fala essa p\*\*\*\*. Parcer. Eh, criar um parcer. É o quê?

**Off Digital:** Não sei o que é, mas ele fala bastante mesmo.

**Marcelo Costa:** É, vou perguntar o que é isso aqui. Analisador sintético sintático é um programa ou componente que lê uma sequência de dados não estruturados como texto, código HTML.

**Off Digital:** fala,

**Marcelo Costa:** Beleza.

**Off Digital:** me explica como se eu tivesse 5 anos.

**Marcelo Costa:** É que aqui eu botei no Google mesmo. Ele já foi na

**Off Digital:** Põe no Google IA, pô. Moda pro modo pro modo

**Marcelo Costa:** docer.

**Off Digital:** I.

**Marcelo Costa:** É como se fosse um tutor, um organizador super rápido. Imagine que você tem uma caixa cheia de peças de montar toda a bagunça.

### 01:07:55 {#01:07:55}

**Marcelo Costa:** Par é o ajudante que pega as peças, lê as instruções e arruma tudo bonitinho para você saber exatamente onde tá a caixa.

**Off Digital:** fala em um em um projeto em um projeto React em um projeto React de compliance com IA, como o parcer funciona? explica em linguagem simples.

**Marcelo Costa:** Imaginem que você está brincando em montar blocos com Lego. onde cada bloco é uma parte da sua tela. O React é um super conjunto de blocos que ajuda a criar o visual do nosso programa. E a IA é como se fosse um amigo robô muito inteligente que trabalha junto com a gente ajudando a organizar as difíceis déficits de segurança. Os cara viaja, né, velho? Os caras são bão, né, primo? p\*\*\*\*, velho. Tô vendo aqui, tá estudando umas umas mo que tão fazendo homeschooler com as crianças, tá ligado? Você viu que teve um rolo aí, mandaram prender o cara e o c\*\*\*\*\*\*?

**Off Digital:** Tô ligado. Tô ligado.

**Marcelo Costa:** Só alarmou mais para nós fazer isso, né, velho?

**Off Digital:** É lógico.

**Marcelo Costa:** Você comentou daquela mina que tá com o Cláudio fazendo, não sei o quê, não foi? Você comentou de uma mina.

**Off Digital:** Foi. Então eu tava com o pencla

### 01:09:32

**Marcelo Costa:** É,

**Off Digital:** fazendo.

**Marcelo Costa:** mas precisa ser muito organizado, né? Eu tava vendo umas paradas aqui, mas aí você tem que fazer na hora da vida, né, velho?

**Off Digital:** Pois é. O f\*\*\* seria conseguir arrumar um grupo de pessoas próximas, né? Tipo quatro.

**Marcelo Costa:** É aí que prende mesmo. Se o seu filho não pode, velho, imagina você fazer um grupo. Os caras tão

**Off Digital:** Ah, mas eu acho que não tá nesse nível não, velho.

**Marcelo Costa:** vindo.

**Off Digital:** Que ali o cara deve ter pegado uma carne de pescoço mesmo, pesada,

**Marcelo Costa:** É,

**Off Digital:** né?

**Marcelo Costa:** mas os caras tão querendo, os caras querem botar para f\*\*\*\*. Mas tá, tá bagunçado, né, priminho? Tá bagunçado o bagulho, né?

**Off Digital:** Ah, como assim?

**Marcelo Costa:** Tô meio Mas tá caindo muita casa, né, velho?

**Off Digital:** Ah, eu só fiquei sabendo desse aí, mano. Para

**Marcelo Costa:** Não,

**Off Digital:** mim,

**Marcelo Costa:** não desse caso de tá caindo a casa de nego para c\*\*\*\*\*\* aí com PCC e o c\*\*\*\*\*\* agora,

**Off Digital:** Ah, velho, p\*\*\*\*, esse negócio do Trump aí,

**Marcelo Costa:** né,

**Off Digital:** ele tá, ele ele chegou de fininho ali, dando a mão pro Lula.

### 01:10:35

**Off Digital:** Mas meu

**Marcelo Costa:** velho? Maduro já botou no rabo do Lula,

**Off Digital:** irmão,

**Marcelo Costa:** velho. Os caras vão pegar ele, velho. Eu acredito que os caras vão pegar ele ainda,

**Off Digital:** eu acredito que eles vão pegar também, velho.

**Marcelo Costa:** velho.

**Off Digital:** O o o o Trump tá sangue no ouro, já pipocou guerra, já derreteu os mercados. O que que mais para ele pode piorar?

**Marcelo Costa:** Lá buscar o Maduro, velho. Você acha que ele não vai vir? Maduro tá falando que o a rota aqui do do tráfico é aqui, velho. O cara foi lá pegar o cara por causa disso.

**Off Digital:** É lógico não.

**Marcelo Costa:** Ele meteu,

**Off Digital:** E mano,

**Marcelo Costa:** falou

**Off Digital:** você e você acha que ele engoliu, velho? Toda aquelas paradas do do do do tariface,

**Marcelo Costa:** que

**Off Digital:** ele não engoliu ainda não, velho. O bicho tá tipo assim: "Ah, beleza, você quer jogar? Vamos, vamos com calma. Eu vou te cercar pelo lado que te toca.

**Marcelo Costa:** é que é inteligente,

**Off Digital:** Primeiro eu vou aprovar o negócio do PCC,

**Marcelo Costa:** né?

**Off Digital:** porque aí eu posso entrar no Brasil, eu posso vincular todos vocês com PCC, todo mundo vai virar terrorista.

### 01:11:25 {#01:11:25}

**Off Digital:** E aí, meu amigão?

**Marcelo Costa:** Acabou. Aí eu pego um por um. O cara é esperto,

**Off Digital:** Cheque,

**Marcelo Costa:** né,

**Off Digital:** cheque mate. Os caras não tão de bobeira, velho.

**Marcelo Costa:** velho?

**Off Digital:** Aí para mim. Vamos lá. O bichão já deu aval aqui, ó. E olha que louco, ele já pegou o aval e já tá aqui, ó, respondendo.

**Marcelo Costa:** Eh, fala. É isso que o devia botar o professor de ontem. para ver. Fale, é assim, seus agentes, ele se fala assim,

**Off Digital:** E aí, profícia?

**Marcelo Costa:** velho.

**Off Digital:** E nós não precisamos construir nada, velho. Só usar inteligência. A parada tá

**Marcelo Costa:** É,

**Off Digital:** construída.

**Marcelo Costa:** é lógico. Se virar se virar automático, aí você cria, né, velho?

**Off Digital:** Validação recebida. Outra agente concordou com a direção, mas apontou três gaps reais. Aí, meu irmão, múltiplos códigos dentro de um tipo documental junto com código documento pode cumprir mais de um

**Marcelo Costa:** Ah.

**Off Digital:** requisito. Antes de fechar o plano, preciso travar duas decisões de produto. Um documento SCW com vários códigos oficiais pode cumprir vários itens a matriz automaticamente.

### 01:12:33

**Marcelo Costa:** Sim. Se ele cumprir, se o cara pede um, porque ele pode ter um um vamos falar assim, ele fez dois cursos juntos e o certificado tem os dois.

**Off Digital:** Uhum.

**Marcelo Costa:** Então, beleza,

**Off Digital:** Uhum. Sim. Quando o documento tem nível superior exigido,

**Marcelo Costa:** né?

**Off Digital:** qual a regra o certifi deve aplicar? Aceitar. Aceitar

**Marcelo Costa:** Sim.

**Off Digital:** superior. Boa, meu irmão. Agora nós estamos falando a mesma língua, rapaz. Mano, isso é muito bom. Não ficar usando vários agentes na execução, mas você validar o plano de um com outro é muito bom, velho. É muito bom. Principalmente dessa forma onde você não tem copia e cola e aonde o cara ele não pode se esquivar e falar: "Não, mas tal, ele tipo assim, ele sabe que você tá vendo em tempo real, então tipo ele tem que falar: "É, meu irmão,

**Marcelo Costa:** Não dá para errar.

**Off Digital:** realmente aqui e ó,

**Marcelo Costa:** Se ele tomar uma dor que nem ele fez.

**Off Digital:** velho, aqui o cara me corrigiu aqui e nós vamos ter que ir,

**Marcelo Costa:** Aí é,

**Off Digital:** entendeu?

**Marcelo Costa:** o cara corrigiu e eu tive que realmente é falar. É, então, c\*\*\*\*, o Adávio que chamou hoje.

### 01:13:56 {#01:13:56}

**Marcelo Costa:** Ô, e aí, vamos dar uma olhada na parada aí, velho. Vamos para cima. Falei, vamos, porque ele tá, estamos precisando emitir a outra nota, né, que a gente normalmente emite logo no começo do mês.

**Off Digital:** Entendi.

**Marcelo Costa:** E aí eu falei, dá uma segurada, velho, porque a gente, p\*\*\*\*, precisava ser a gente apresenta pro, queria apresentar pro Marcelo daqui a pouco, sei lá, nem que seja na, a gente segura aí nos próximos dias, dá uma apresentada para eu já tentar virar essa chave com ele,

**Off Digital:** Não, mas se se é se é para virar a chave do financeiro,

**Marcelo Costa:** velho.

**Off Digital:** nós vamos dar um jeito por mim até o até sexta-feira aí nem que eu preciso virar a noite todo dia, nós nós vamos dar um jeito,

**Marcelo Costa:** Tamamo junto,

**Off Digital:** entendeu? Validei com a gente no browser. Ele confirmou a direção, mas apontou com o plano inicial.

**Marcelo Costa:** velho.

**Off Digital:** Vamos expandir o p\*\*\*\*. Isso é legal. O jeito que ele dá o plano aqui também no Codex. Eu curto. Ah, corrigir a caus fix definitivo. Beleza, velho. Vamos embora. Chega de conversa que eu já tô no extra high no modo fast.

### 01:14:58 {#01:14:58}

**Off Digital:** Tô sentando o cabelo para mim.

**Marcelo Costa:** É, ô priminho, você não usa os os automações dele ali,

**Off Digital:** uso.

**Marcelo Costa:** né?

**Off Digital:** Eu tô usando poucas aqui, mas eu uso sim. É que eu tô montando uns negócios com calma, priminho. Por exemplo, isso aqui, ó, velho, eu peguei e fiz um uma raspagem no meu WhatsApp nos últimos 4 anos, velho. Mandei ele ler todas as minhas conversas que tinha mais de cinco interações. O bicho, velho, eu tô mapeando minha comunicação, tô mapeando várias coisas, só que eu não tô tendo cabeça, mano, para fazer esses bagulhos. Eu vou gerar várias automações em cima disso. Vou deixar ele com o meu whats ligado, catando várias coisas para mim. Eu vou, mano, eu tô com um bagulho muito f\*\*\* na cabeça, só que eu eu eu enquanto eu tiver enquanto eu não finalizar o setfi, velho, eu não tô fazendo nada,

**Marcelo Costa:** Ah, e outro aí não dá porque senão você fica abrindo muita ideia também,

**Off Digital:** tá ligado? Não.

**Marcelo Costa:** velho.

**Off Digital:** E é e a cabeça, velho, a cabeça ela não aguenta em muito em muitos assuntos ao mesmo tempo com qualidade.

**Marcelo Costa:** É.

### 01:16:05

**Off Digital:** Então eu tô eu tô mantendo tô mantendo desse jeito,

**Marcelo Costa:** Eh,

**Off Digital:** entendeu?

**Marcelo Costa:** já nós vamos mudar.

**Off Digital:** Não, nós vamos, eu quero botar o linear em prática, velho. Muito bom esse programa. Eu quero sincronizar com click também. Tudo, tudo vai ficar por trás. Eu não vou ver nada. Tudo isso vai, vai virar um agente que eu converso no que ele vai falar comigo poucas palavras. Ele vai falar comigo assim: "Velho, preciso que você aproveit subiram tal coisa no linear aqui, tá de acordo? Ele vai falar comigo, tipo assim, a regra vai ser, velho, você pode falar no máximo cinco palavras na frase, entendeu? Só que eu vou ter várias estruturas por trás,

**Marcelo Costa:** Sì.

**Off Digital:** cada uma para uma coisa, entendeu? linear área para isu e PR de código, comit, essas coisas para organizar tudo lá no camban, tudo no esquema. Eu não vou ficar olhando, entendeu? Só que se uma se alguma vez eu se alguma vez eu me perder,

**Marcelo Costa:** É só para organizado a hora que precisar até para

**Off Digital:** eu tenho como ir lá e ver, entendeu? Se eu precisar chegar e falar, velho, em que ponto nós estamos aqui do projeto, eu tenho como ir lá e ver o click.

### 01:17:20

**Off Digital:** Eu quero que seja um negócio mais grosso no sentido de não as microtarefas do projeto igual eu tava fazendo de tipo assim, cara, front end, back end, isso vai ficar tudo no líha. O click, eu quero deixar ele mais seco no sentido de, velho, que que eu tenho que fazer essa semana de tesque, p\*\*\*\*? tem uma reunião com fulano, tem que preparar o briefing da reunião com o cara, tem que montar uma proposta tal, esse tipo de de de granul, granulamento, granulação, granulagem, sei lá. Eh, mas uma parada mais compacta de tesques, entendeu? De tipo, cara, o que que são realmente as tesques que eu tenho que fazer aí? Beleza? Você pode ter subtesk lá de tipo assim, tá para eu montar o brief pro cara, eu preciso de disso, disso, daquilo, tá beleza? Mas não é o detalhe do detalhe do detalhe do detalhe do detalhe do detalhe, entendeu? Que é o que tava ficando confuso para mim.

**Marcelo Costa:** Sim.

**Off Digital:** Então eu vou levar toda a parte operacional pro linear, eu vou deixar as tesques de forma simples no click e tudo isso se encra com a minha agenda. E aí,

**Marcelo Costa:** Você

**Off Digital:** cara? O esse assistente ele só bate a agenda e pede aprovação.

### 01:18:43

**Off Digital:** Então, ó, velho, você tem uma tesque assim assim assado, velho. Tá tá tá tá certo essa data aqui. Tá certo isso aqui, esse briefing tá tá correto aí.

**Marcelo Costa:** sabe que tem que responder ele, né,

**Off Digital:** É.

**Marcelo Costa:** velho?

**Off Digital:** Então, só que, velho, para esse front ficar simples, você tem que ter um back end, que é o linear, que é o click, que é a agenda, que é várias coisas alinhadas, muito bem feitas e muito bem montadas pro teu agente conseguir falar poucas palavras e organizar de verdade a parada para você, entendeu?

**Marcelo Costa:** Sim.

**Off Digital:** Então eu quero criar e aí o o a o front depois vai ser o o macOS no sentido visual de juntar todos os ambientes e uma coisa só. Mas eh eu não consigo olhar para isso agora, velho.

**Marcelo Costa:** É muita coisa,

**Off Digital:** Tá ligado?

**Marcelo Costa:** né, que precisa ir com ir encostando, né,

**Off Digital:** Eu quero parar para fazer isso, tá ligado?

**Marcelo Costa:** velho?

**Off Digital:** Tipo, não é que eu vou parar parar, mas é tipo assim, cara, eu não tenho nenhum projeto que tem deadline assim que eu preciso ficar mexendo com código e com tal. Beleza? Então, tá. Então, vai, vou tirar aqui um mês para montar esse sistema que é muito importante, né, velho?

### 01:19:55 {#01:19:55}

**Off Digital:** É uma parada que, tipo assim,

**Marcelo Costa:** É,

**Off Digital:** que gera

**Marcelo Costa:** mas tem que mas tem que rodar o que tá rodando aí para você saber o que você vai pôr lá,

**Off Digital:** mais.

**Marcelo Costa:** né? Também tem que experienciar as p\*\*\*\* toda para falar, velho, isso aqui vale a pena

**Off Digital:** É, não é verdade, cara. O CF para mim tá sendo uma grande escola de velho como é que funciona para você entregar um

**Marcelo Costa:** pôr

**Off Digital:** projeto profissional, entendeu? Tô falando de um projeto profissional, mano. Não tô falando de, tipo assim, você fazer um MVPzinho ali e e e

**Marcelo Costa:** mas o o que que eu vejo também pensando, né? p\*\*\*\*, eu acho que, cara, e você vê que dá trampo para fazer isso, né? Por isso que você tem que definir se você vai, se é um negócio que vale a pena fazer mesmo. E se você for fazer pros outros, é dinheiro que tem que colocar. Eh, mas eu acredito, tem muita coisinha simples que não precisa ter toda essa complexidade que nós estamos fazendo,

**Off Digital:** Sim.

**Marcelo Costa:** tá ligado? Que às vezes é, talvez não é duradouro como esse negócio, né? Mas alguns tipos uns pluginzinho,

**Off Digital:** Uhm.

**Marcelo Costa:** uns negócios que p\*\*\*\*

### 01:20:54

**Off Digital:** Sim.

**Marcelo Costa:** resolve uma

**Off Digital:** Por exemplo, ó, esse bagulhinho enquanto tá rodando aqui,

**Marcelo Costa:** solução.

**Off Digital:** ó. Esse bagulhinho eu tô usando todo dia, mano. Porque que que acontece? Esse aqui eu que criei, ó. Eu acho que eu já até te mostrei, mas é,

**Marcelo Costa:** É o do áudio lá.

**Off Digital:** eu tô usando todo dia. Porque que é que acontece? Minha mina chega para mim sempre, fala assim: "Amor, põe uma música para mim no vídeo, porque, né, eu manjo de música e tal, eu sempre escolho umas músicas legal". Que que eu tenho que fazer? Eu tenho que abrir o Spotify, escutar as músicas, achar uma que eu gosto. Aí eu pego, levo pro YouTube para achar a música no YouTube. Do YouTube eu tinha que abrir um algum site de download do YouTube que tem um monte de vírus, um monte de coisa, propaganda, você não sabe onde é que clica para conseguir fazer o download.

**Marcelo Costa:** Sim.

**Off Digital:** Fazer o download. Só que as músicas que eu uso no vídeo dela, eu gosto de tirar o vocal para usar só o instrumental, porque ele não fica batendo com a voz. E aí eu abro o programa de produção.

### 01:21:50

**Marcelo Costa:** Sim.

**Off Digital:** Dentro do programa de produção, eu tenho um plugin que tira, extrai a parada. Que que eu fiz agora, mano? Eu pego aqui uma música qualquer, ó. Vou botar aqui, pegar qualquer música aqui. Vamos botar essa

**Marcelo Costa:** Não tem aquela questão de de produção,

**Off Digital:** aqui.

**Marcelo Costa:** primo, de poder usar,

**Off Digital:** De quê?

**Marcelo Costa:** de você poder usar a a música é direito

**Off Digital:** De direito autoral. Cara, tem,

**Marcelo Costa:** autoral.

**Off Digital:** mas como tá só com instrumental e com a voz por cima no Instagram, é muito difícil de pegar, entendeu? Então, ah, eu venho aqui, ó,

**Marcelo Costa:** M.

**Off Digital:** peguei o link do YouTube, eu ponho aqui MP3 porque eu quero áudio, não quero vídeo. Download. Aí ele já carregou aqui, já veio com o nome. Aí ele me dá três opções: baixar, instrumental ou vocal. Então eu criei um algoritmo por trás,

**Marcelo Costa:** p\*\*\*\*, já fez o corre, tudo que você

**Off Digital:** velho. Em um minuto, velho, eu peguei o bagulho,

**Marcelo Costa:** fazia.

**Off Digital:** botei aqui, tá? Quero só o instrumental, que é geralmente o que eu quero. Aí ele baixa primeiro o som, baixou 100% e agora ele vai para separando o áudio.

### 01:23:00

**Off Digital:** Aí ele vai separar o áudio e já baixa renomeado com nome eh artista, música, instrumental para minha pasta downloads. Eu só pego esse arquivo e jogo lá no editor de

**Marcelo Costa:** p\*\*\*\*,

**Off Digital:** vídeo.

**Marcelo Costa:** é isso aí, p\*\*\*\*, velho. negocinho que se você fizer o Marte explicar,

**Off Digital:** p\*\*\*\*, velho. É um bagulho que eu tô, eu eu usei hoje isso. Usei, eu usei hoje, usei ontem.

**Marcelo Costa:** velho.

**Off Digital:** Então é um negócio que eu construí porque eu toda vez fala: "c\*\*\*\*\*\*, que saco, mano, eu tenho que parar agora para ver e tal, baixar". Aí eu entrava no Google, YouTube para MP3. Aí aparecia um monte de site diferente porque eles eles ficam dando takeedown, né?

**Marcelo Costa:** É, o cara

**Off Digital:** Nesses sites. Aí, p\*\*\*\*. Ah, esse não funciona, que m\*\*\*\*. Aí vai, procura outro, aí fica clicando nas paradas, aí baixa vírus.

**Marcelo Costa:** fica.

**Off Digital:** Entendeu? Então, tipo assim, aí eu, p\*\*\*\*, já criei essa ferramenta. Agora o que eu preciso ver é quais são as implicações legais, né? Se eu posso lançar isso no mercado, se eu terei que lançar com VPN de outro lugar para, tipo, se derrubarem, beleza, não vai dar nada para mim.

### 01:24:02 {#01:24:02}

**Off Digital:** Eh, eu tenho que entender como é que é o legal, mas

**Marcelo Costa:** E o que os caras hoje fazem é isso.

**Off Digital:** mesmo

**Marcelo Costa:** Os cara lança o pluginzinho e quem vai pagar é é anúncio, né?

**Off Digital:** Sim.

**Marcelo Costa:** Aí o cara fica pipocando anúncio em todo lado para ele faturar nos anúncios,

**Off Digital:** Isso aqui é um bagulho que eu venderia one time.

**Marcelo Costa:** né?

**Off Digital:** Você compra uma vez, paga 30 conto, paga mexaria e você e é e você pode usar para sempre. Você baixa o bagulho, tem a licença, é seu, entendeu? Beleza? Então, tipo assim, eh, se eu não puder botar no ar de forma interessante, é uma ferramenta que eu construí para mim, velho, que eu vou aprimorar ela com o tempo, cada vez mais ela vai adiantar mais o meu lado e eu vou estar sempre

**Marcelo Costa:** Sim,

**Off Digital:** usando.

**Marcelo Costa:** vai virando uma skillzinha, né? Como se fosse uma skillzinha,

**Off Digital:** É, velho,

**Marcelo Costa:** né?

**Off Digital:** uma ferramentinha minha que eu criei aqui porque eu tinha necessidade, entendeu? Então, p\*\*\*\*, esse é um projetinho que eu que eu gastei uns dois dias para fazer ele. E aí agora essa parada de converter, porque aí eu baixava a música, eu falava: "Pô, agora eu tenho que abrir o programa. Eu tinha que abrir o programa,

### 01:25:07

**Off Digital:** jogar a música lá para dentro,

**Marcelo Costa:** Trampo,

**Off Digital:** clicar em converter, exportar de novo, escolher a pasta que eu queria exportar." Eu falei: "Não, velho, eu já tenho que baixar a parada e já na próprio programa ele já converte". Aí eu implementei. Aí como que como que é hoje? É uma é um é um algoritmo que roda na minha máquina que ele dá o processamento da minha GPU para separar o áudio. Se eu quiser fazer isso ser comercial, eu tenho que alongar o servidor com GPU, botar na nuvem e aí ele vai girar, entendeu?

**Marcelo Costa:** Eh

**Off Digital:** Então, tipo assim, eu tô usando, vou implementando. Quando eu achar que tá muito bom,

**Marcelo Costa:** Ja.

**Off Digital:** é porque eu não fiz a pesquisa ainda do compliance, se eu posso botar, como é que eu poderia botar isso aqui para jogo, mas se eu fizer e eu ver que o compliance é de boa, que tem uma forma de colocar, já é um produtinho que dá para colocar no ar, entendeu?

**Marcelo Costa:** É,

**Off Digital:** E eu não tipo assim, negócio

**Marcelo Costa:** mas é isso aí.

**Off Digital:** besta,

**Marcelo Costa:** Mas isso aí é um negocinho que vai dando umas entradinhas, né? Você bota ali um tráficozinho para ficar rodando, velho, direto.

### 01:26:25

**Off Digital:** cara. E e não tem, priminho, não tem essas não tem, velho.

**Marcelo Costa:** Onde

**Off Digital:** O cara lançou uma open source lá que deu mais de 6.000 1 salvos a que ele fez dessa aqui de de baixar de porque ele não baixa só do YouTube, ele baixa de todos os sites. Ó, ele baixa do Facebook, baixa do Insta, baixa do TikTok, baixa da Twitch, baixa do SoundCloud, baixa do Pinterest, baixa do Vim, baixa de tudo,

**Marcelo Costa:** tiver?

**Off Digital:** velho, tá ligado? E aí eu peguei o projeto open source do cara, modelei em cima e criei esse que é muito mais completo que o do cara, com interface muito mais f\*\*\* e com essa ferramenta nova. Não tem, mano. O o open source do cara deu 7.000 1 bookmarks, todo mundo falando, mano, c\*\*\*\*\*\*, não tem, não tem, não tem, que f\*\*\* e tal, tô usando. Então, é um produto que, tipo, não tem no mercado, não existe esse produto no mercado. Você procurar eh eh downloader de várias redes

**Marcelo Costa:** É,

**Off Digital:** social,

**Marcelo Costa:** eu acho que é porque por conta do do de ter é do Ligam,

**Off Digital:** né? Sim. Então, mas mas com certeza tem um work around,

**Marcelo Costa:** né?

### 01:27:31

**Off Digital:** você lança lá do da Rússia, tá ligado? Põe o VPN russo lá, não sei aonde e mete pau.

**Marcelo Costa:** E f\*\*\*-se fala: "Manda em Bitcoin,

**Off Digital:** É, velho.

**Marcelo Costa:** né?

**Off Digital:** Exato. Paga em cripto para para VTN lá na Rússia e vamos embora. E no máximo que os caras vão fazer é é derrubar, entendeu? Difícil de chegar num ponto de porque é diferente, velho. Uma coisa é você facilitar o download de uma mídia pro cara, outra coisa é você usar a obra do cara num copyright, entendeu? Tipo, o cara não vai te processar só porque você facilitou o download,

**Marcelo Costa:** Yeah.

**Off Digital:** não chega nesse nível, entendeu?

**Marcelo Costa:** E aí, o bichinho

**Off Digital:** Bom, tá quase fechando aqui, Piti. Já tá nos testes. Já fez o job,

**Marcelo Costa:** tá

**Off Digital:** tá fazendo os testes aqui. Agora ficou pica, hein, primi. É o condexão brabo com o Fabão do lado.

**Marcelo Costa:** agora os caras vai se falando,

**Off Digital:** Senhora,

**Marcelo Costa:** né,

**Off Digital:** velho.

**Marcelo Costa:** velho?

**Off Digital:** Vai brincando com os meninos.

**Marcelo Costa:** Deixa eu começar uma parada aqui também.

**Off Digital:** Vou mijar ali que eu tô tomando água para caramba.

### 01:31:37 {#01:31:37}

**Off Digital:** M. Aí depois tá trazendo aqui, cachorro isso. no meio do rolê olhando. Seja que estudo do pet me de remoto já começou tá só fazendo o deploy aqui. É peri se esse vídeo não acontece não limpar um pouco M. Você já tem um cara aí da mesma matriz?

**Marcelo Costa:** Tem Só um segundo, pera aí. Você já quer já é para subir o outro primo. M.

**Off Digital:** P nova no ar. A criativa passoução vai abrir segundo plano. Vamos, vamos subir de novo. Vamos apagar e subir já. R

**Marcelo Costa:** Bora. Vamos lá. Vai subir o cara novo ou mesmo?

**Off Digital:** Vamos o mesmo.

**Marcelo Costa:** Você

**Off Digital:** Deixa a matriz. Agora só sobe o cara de novo.

**Marcelo Costa:** apagou ele?

**Off Digital:** Não,

**Marcelo Costa:** Primia apagar. Lembra que você falou que ia dar uma opção de apagar os documentos? Os confere e não dá para apagar.

**Off Digital:** confere.

**Marcelo Costa:** É isso.

**Off Digital:** Não apaga o candidato direto.

**Marcelo Costa:** Então vamos lá.

**Off Digital:** Na verdade, você não quer só subir o o o

**Marcelo Costa:** Eu vou apagar os dois documentos que

**Off Digital:** o

**Marcelo Costa:** é até para testar.

**Off Digital:** excedente dá para pagar.

**Marcelo Costa:** Vou excluir o envio e vou subir de novo.

### 01:37:15

**Marcelo Costa:** Pera aí, vamos ver o que ele fez. Pera aí que tá dando uma, ele tá dando umas pipocada aqui.

**Off Digital:** Tá dando o quê?

**Marcelo Costa:** BR umas

**Off Digital:** Coisa aí. Compartilha aí.

**Marcelo Costa:** piscada aqui. Pera aí, eu tá vendo aí que ele tá piscando?

**Off Digital:** Não, aqui tá normal selecionar arquivos. Ué, onde que você tá? no upload ali do lado.

**Marcelo Costa:** É mesmo mesmo. Ó, tá aberto no candidato aqui. Ele tá fazendo isso,

**Off Digital:** Dá um refresh

**Marcelo Costa:** ó.

**Off Digital:** aí.

**Marcelo Costa:** Então eu apaguei aqui pendente. Ah,

**Off Digital:** Deixa eu ver aqui,

**Marcelo Costa:** não,

**Off Digital:** primo, se tá tá dando pau aqui também.

**Marcelo Costa:** parou. tentar fazer o upload só daquele documento. Beleza, tô fazendo de um só. Eu excluí

**Off Digital:** Ele tava em excedentes ainda ou você conseguiu excluir lá em

**Marcelo Costa:** o excedente de dá para excluir.

**Off Digital:** excedente?

**Marcelo Costa:** He. M.

**Off Digital:** Foi Confere

**Marcelo Costa:** Show de bola, primo.

**Off Digital:** 100%,

**Marcelo Costa:** Vamos apagar o cara e vamos subir ele de

**Off Digital:** então.

**Marcelo Costa:** novo.

**Off Digital:** Uhum.

### 01:41:31

**Marcelo Costa:** Então, vamos lá. que as vagas t várias aqui, sendo que a gente só tem uma matriz lá.

**Off Digital:** Não aparece para mim aqui, primo. Quando você

**Marcelo Costa:** Hum.

**Off Digital:** clica

**Marcelo Costa:** Всё.

**Off Digital:** Oh.

**Marcelo Costa:** Ora foi.

**Off Digital:** Documento vencido. Autete agora ele deu data ambigua de novo. Pera aí.

**Marcelo Costa:** cargo horário insuf f\*\*\* é isso. Cada hora ler de um jeito é f\*\*\*, velho. Aqui não tem hora, entendeu?

**Off Digital:** no carga horária,

**Marcelo Costa:** E aí cada hora ele pega na matriz o K que deve tá

**Off Digital:** na matriz, velho.

**Marcelo Costa:** pedindo hora, mas uma hora ele passa batida,

**Off Digital:** Estranho.

**Marcelo Costa:** outra hora não. Que aqui não tem hora o CAC. Aí vamos ver se o K tem lá na matriz. 40 horas, ó. Matriz tá pedindo

**Off Digital:** E o documento? E o

**Marcelo Costa:** 40

**Off Digital:** documento?

**Marcelo Costa:** e o documento não tem.

**Off Digital:** Será que é isso?

**Marcelo Costa:** Documento não tem horário, já tô vendo aqui. Ele não tem.

**Off Digital:** Será que é por isso que ele tá bloqueando? Mas por que que não bloqueou antes?

**Marcelo Costa:** É, então e antes ele passou, entendeu?

### 01:48:09

**Marcelo Costa:** Aqui uma hora ele vai, ele pega uma regrinha e usa, outra

**Off Digital:** Mas é porque esse a gente arrumou agora,

**Marcelo Costa:** hora.

**Off Digital:** né? O AV1/3 foi esse que a gente arrumou

**Marcelo Costa:** Não, não, esse aqui já tinha ele na outra,

**Off Digital:** agora.

**Marcelo Costa:** na outra leitura ele tinha

**Off Digital:** Tá, eu tô mandando para agente aqui,

**Marcelo Costa:** passado.

**Off Digital:** mas deixa, deixa ele ler e a gente já exclui e já sobe de novo. Pera aí.

**Marcelo Costa:** Aí, esse aqui, lembra? Ele tinha dado isso, né? passou aí, agora ele pegou de novo, que era um ponto que a gente ficou na dúvida que até tudo bem ele ficar aqui, que deu uma aquela questão de ambiguidade, né? Ó,

**Off Digital:** Não, não dá. Ele tem que ler da mesma forma

**Marcelo Costa:** não, mas isso a gente tinha acertado com a data.

**Off Digital:** sempre.

**Marcelo Costa:** Se você tem a data certa, não tem ambíg você tem a a final, né?

**Off Digital:** Não, a gente já Beleza, esse era o pau que deu, mas a gente tinha arrumado já.

**Marcelo Costa:** Ja.

**Off Digital:** Vamos ver. Joguei no cara aqui. Deixa ele só ele ler. E aí?

### 01:49:25

**Off Digital:** Porque aí a gente já pode excluir. Deixa só ele puxar certinho e aí a gente pode excluir já e subir de novo.

**Marcelo Costa:** Isso, p\*\*\*\*, acontece no outro também, que é assim, cara, a Iaca da hora ela ela ler de um jeito, velho. Onde tem

**Off Digital:** Não era para acontecer,

**Marcelo Costa:** i

**Off Digital:** porque e essa parte não é Iar.

**Marcelo Costa:** mas aqui, por exemplo, o aí que é o porque o que que a gente não consegue ver, né? Por exemplo, cadê o OCR desse documento aqui? Você consegue ver o OCR? O que que ele lá no N8N ele pega e ele varreca o o o OCR. E aí você vê, pô, quantas horas ele puxou aqui. Você não sabe o que que ele puxou. Não sei o que que ele puxou de se ele botou horas, não puxou e do outro ele pegou a hora, não pegou. Que ele deveria validar o campo hora também no outro, né?

**Off Digital:** Eu nunca pedi para ver o OCR, mas eu acho que se eu pedir aqui, ele vai abrir para mim no SPAS,

**Marcelo Costa:** É,

**Off Digital:** né?

**Marcelo Costa:** ele deve jogar nos campos, né? Teria que ter pego o outro e esse para falar assim: "Por que que o outro passou?" Então você não fez o OCR da da da

### 01:51:05

**Marcelo Costa:** data hora,

**Off Digital:** Ele tá terminando só de fazer o o M aqui.

**Marcelo Costa:** tá?

**Off Digital:** Eu vou pedir o CR.

**Marcelo Costa:** E se ele tá cargo horário insuficiente, ele deveria ter aqui a opção, porque esse documento, eu acho que ele não tem carga horária, ele nunca mostra mesmo, não vem com carga horária, mas já é, vamos dizer assim, de prche que esse curso exclusivo ele só tem 40, entendeu? Aqui eu não consigo baixar esse documento, primo, direto ele. Se eu quiser, ah, eu baixo aqui, será?

**Off Digital:** Não, aí é para eh fazer upload. Seria em exportar, mas ele só exporta os que conferem, eu acho. Testa aí. É. Eu pedi o CR aqui. Vamos ver.

**Marcelo Costa:** Ja. Ó, esse aqui era o prompt que eu que eu usava lá, ó, para testar. Quer ver, ó? Não, um promp de distração. Então ele vai lá, ó, eu botava qual que é a categoria, quais são os códigos, certificado e competência, bala pala. Data, data de validade. Aí, ó, carga horária. Ele não tem carga horária, né?

**Off Digital:** Cara, que engraçado. Por que que a matriz exige, né?

### 01:54:00

**Off Digital:** Será que tá errada a base?

**Marcelo Costa:** E eu coloquei na mão, viu? Porque eu vi na outra aqui pedindo,

**Off Digital:** Então,

**Marcelo Costa:** mas a matriz em si não pede. É verdade. Peguei, eu peguei o horário do outro certify, por isso que eu coloquei, mas na matriz não tá pedindo. Ja. Quer ver? Deixa eu dar uma olhada nisso aqui. Quer ver? Ó.

**Off Digital:** Você

**Marcelo Costa:** Ó, veja aqui, não fala de horário, tá vendo, primo? E eu botei lá porque tinha no outro, mas não precisaria ter colocado,

**Off Digital:** acha que vale da gente fazer o teste de criar a matriz sem a a o horário subir de novo para ver se ele

**Marcelo Costa:** velho.

**Off Digital:** bloqueia

**Marcelo Costa:** Vamos fazer. Vamos lá,

**Off Digital:** o da data. Eu eu tô pedindo para ele ver os dois

**Marcelo Costa:** ó.

**Off Digital:** já. E eu pedi para ele mandar, ó, o OCR aqui, ó. Te mandar aí.

**Marcelo Costa:** Stra tudo,

**Off Digital:** Ó, um vez aqui para você

**Marcelo Costa:** né?

**Off Digital:** ver.

**Marcelo Costa:** Ele faz, ele puxa o mesmo, mesmo Jzon lá, ele puxou o mesmo modelo que a gente fazia, né? Eu só coloquei 40 horas porque lá no outro certifi, mas a matriz não tá falando, velho.

### 01:58:13

**Marcelo Costa:** Não deveria botar.

**Off Digital:** É porque assim, se a gente tá tá pedindo na matriz 40 horas e não tem hora, não tá, não tá errado ele bloquear,

**Marcelo Costa:** Não, ele tá certo de bloquear.

**Off Digital:** mas vamos conferir que é isso

**Marcelo Costa:** O documento não tem, velho. Só que o duro é que ele passou da outra vez.

**Off Digital:** mesmo.

**Marcelo Costa:** Esse que é o problema, né?

**Off Digital:** Sim, mas antes eu acho que você não botou as horas na outra vez.

**Marcelo Costa:** Hum. A gente só apagou e subiu de novo, velho. A gente tinha validado tudo, a gente apagou e subiu de novo, o cara. Então o ponto é esse. Ele agora ele tá certo, mas o problema é que ele passou errado na outra. Então problema é a divergência, não é nem no outro caso, dependendo. Quer ver? Deixa eu até ver aqui, ó. Se ele respondeu para mim. Permitido por reger. Opa. Sky

**Off Digital:** Me passa o print desse Jon aí.

**Marcelo Costa:** v que é o print ou quer copiar.

**Off Digital:** o print.

**Marcelo Costa:** Você

**Off Digital:** É, mas tô vendo aqui não tem nada muito diferente

**Marcelo Costa:** vê aqui ele falando CAC padrão da autoridade marítima brasileira. Forme Alc padrão.

### 02:00:15 {#02:00:15}

**Marcelo Costa:** Possui cargoária regulamentar superior a 40 horas, geralmente 52 ou 60, dependendo do ano DPC. Abaixo de 40 horas, a única hipótese encontrar pá. Ja. Você deu o certificado de de competência. Ele não é um curso de conclusão, ele é um diploma, então ele não precisa de horário, entendeu? Se você tem o o coisa que nem a CNH, não tem quantas horas você dirigiu lá. Se tem CNH, você tem CNH, velho. Então não deveria ter colocado a hora lá, entendeu? Ele tá certo de ter barrado.

**Off Digital:** Porque você colocou hora na matriz,

**Marcelo Costa:** É,

**Off Digital:** né?

**Marcelo Costa:** agora o certo certo mesmo era ele não deixar eu colocar hora, porque falar assim, isso aqui não tem hora na no regulamento, né? Mas aí também fica muito amarrado,

**Off Digital:** Sim.

**Marcelo Costa:** né?

**Off Digital:** Velho, os maiores erros vão acontecer na criação das matrizes. O cara criou um detalhe errado na matriz.

**Marcelo Costa:** É por isso que eu falei para você,

**Off Digital:** Vai dar

**Marcelo Costa:** por isso que eu falei para você desde o começo, que é o que eu vinha falando pro Adá.

**Off Digital:** pau.

**Marcelo Costa:** Então não pode deixar os caras mexer em matriz e em documento.

### 02:02:59

**Marcelo Costa:** Isso aí não se mexe. Isso aí é o complice da parada, velho. Se o cara quer mexer numa matriz, ele manda pra gente isso, a gente faz aqui,

**Off Digital:** É,

**Marcelo Costa:** né?

**Off Digital:** não, durante um tempo vai ter que ser, porque até a gente conseguir, cara, vamos ver, vamos testar depois. É um teste que eu quero fazer com você depois. É, é esse, isso que eu tô criando de subir a matriz direto da planilha. Aí a já fez os testes aqui, já validou, falou que tá funcionando, mas né,

**Marcelo Costa:** Dá para subir um outro cara aqui, primo, enquanto ele tá olhando aí. Então,

**Off Digital:** dá bora.

**Marcelo Costa:** vou subir outro cara enquanto isso. Deixa esse Mateus aí.

**Off Digital:** Atualmente sumiu aqui, cara. Pelo que eu tô entendendo do agente aqui,

**Marcelo Costa:** Ab.

**Off Digital:** o fix de ontem não entrou.

**Marcelo Costa:** Hã.

**Off Digital:** O fix de ontem não entrou na data.

**Marcelo Costa:** Ah.

**Off Digital:** É,

**Marcelo Costa:** É.

**Off Digital:** a gente fez, mas num diagnóstico fechado nos dois casos. O fix do do Territá PR, Terrilt da Tambía, porque voltou. O fix existe hoje, ontem desde às 16 horas com teste cobrindo exatamente isso.

### 02:04:22 {#02:04:22}

**Off Digital:** Só que ele ficou preso nessa branch misturado com outros 12 comits e nunca chegou na main. Verifiquei produção tal que fiz cherry pick dos três comits tal. C carga horário caso diferente. Não é bug de extração. Verifiquei no texto extraído do certificado. O documento de capitania de cabo frio não imprime carga horária nenhuma e a regra catalogada do do CAS exige 40 horas. O motor não acha horas no documento e marca parcial.

**Marcelo Costa:** Mas quem tá falando 40,

**Off Digital:** É, ele entendeu que ele entendeu que foi o foi o documento aqui,

**Marcelo Costa:** eh,

**Off Digital:** né? Mas foi a gente que colocou usado hoje pela aplicar casa decisão da regra de comp.

**Marcelo Costa:** eh,

**Off Digital:** Por isso te pergunto antes. Mesmo pr tá correto emitido 2019 venceu em agosto, cara. Beleza. Então, um foi meio que erro nosso e o outro não tinha entrado ontem. Agora para certificado.

**Marcelo Costa:** Bom,

**Off Digital:** Aceita a

**Marcelo Costa:** então manda ele fazer. Vamos subir de

**Off Digital:** cargos.

**Marcelo Costa:** novo.

**Off Digital:** Beleza, ele já tá subindo de novo aqui. Só que se esse cara tem a mesma matriz, teoricamente ele teria que dar pau nesse mesmo documento, né?

### 02:06:26

**Marcelo Costa:** É, vamos ver como ele vai reagir aí, né? Deixa eu ver. Tem seis documentos. Deixa eu ver se Fábio aqui quantos ele tem. Tá certo. Tá faltando um. Ele deu confere em tudo aqui também. Vamos ver agora até esse aqui, ó. Já vamos entender, ó. 5195 é o que tá na nossa matriz lá, né? Oi. Ó, faltou só um. Vamos ver quem foi que não bateu. O CCK, mesma coisa, ó.

**Off Digital:** carga horária, né? Boa.

**Marcelo Costa:** Tá aqui bateu no horário.

**Off Digital:** Então ele bateu igual. Tá

**Marcelo Costa:** Tá certo. Só isso aqui bateu aqui.

**Off Digital:** certo.

**Marcelo Costa:** Ele foi completo, primo. Bateu certinho. Esse aqui documento não tinha mesmo, não foi. E o K ele barrou no horário.

**Off Digital:** Show de bola.

**Marcelo Costa:** Só que aí você vê quem que ele passou, que foi o outro que não tinha passado lá, que era o foi aquele outro que ele não passou ali que não tinha comitado

**Off Digital:** do Mateus.

**Marcelo Costa:** lá

**Off Digital:** Era o era o da data.

**Marcelo Costa:** na data. Que beleza. Aí não tem.

### 02:08:13 {#02:08:13}

**Marcelo Costa:** Tá. Então agora vamos fazer o seguinte, vamos apagar de novo esses cara aqui. Podemos apagar todo mundo.

**Off Digital:** Pode, pode apagar.

**Marcelo Costa:** Beleza, vamos

**Off Digital:** Mas calma aí que não entrou 100% ainda não.

**Marcelo Costa:** apagar

**Off Digital:** Ele tá, tá subindo aqui, ó.

**Marcelo Costa:** o quê?

**Off Digital:** Tá subindo. Ele ainda não entrou as mudanças, não.

**Marcelo Costa:** É, então vamos esperar e eu vou e vamos mexer na

**Off Digital:** É, vamos subir um terceiro cara.

**Marcelo Costa:** matriz.

**Off Digital:** Vamos subir um terceiro cara. Aliás, na verdade, a gente podia criar a matriz agora sem a exigência lá de 40 horas,

**Marcelo Costa:** Isso.

**Off Digital:** né?

**Marcelo Costa:** Vamos, vamos mexer na matriz aqui,

**Off Digital:** Vou já de novo.

**Marcelo Costa:** ó.

**Off Digital:** F. Depois você olha se tem comida no pote dela. Tá em cima. E aí para mim?

**Marcelo Costa:** Ele descobriu uma fita errada aqui também, viu primo?

**Off Digital:** Qual

**Marcelo Costa:** É o seguinte, ó.

**Off Digital:** foi?

**Marcelo Costa:** Vê, ele tá barrando o cara aí por 40 horas. Aí aqui eu tava criando outra matriz.

**Off Digital:** Uhum.

**Marcelo Costa:** O CBSN também tá 40 horas e o documento não tem horas

**Off Digital:** Mhm.

### 02:13:20 {#02:13:20}

**Marcelo Costa:** e passou.

**Off Digital:** Mhm.

**Marcelo Costa:** CBSP também tá 40 horas e passou B também.

**Off Digital:** Uhum. Mas ele

**Marcelo Costa:** Não tem não tem essa informação nos documentos, mas tá na

**Off Digital:** Bom, hum,

**Marcelo Costa:** matriz.

**Off Digital:** mas a matriz tá exigindo, correto? Se ele tá exigindo 40 horas e não tem os documentos.

**Marcelo Costa:** Ele tá exigindo igual igual o CC. O C tava aqui 40 horas, aí ele barrou lá, falou: "Ó, você tá exigindo 40, não tem no documento. Agora os outros dois, eu também tô pedindo 40\. E ele tá passando batida e não tem no documento. Ele deveria barrar

**Off Digital:** Mas o que o agente me falou aqui,

**Marcelo Costa:** também.

**Off Digital:** que eu li para você foi que a regra da a regra catalogada no CACI exige 40 horas, cargo oficial do pré-pom. Ele não não deu exatamente que foi porque porque assim, como é que a matriz pode pedir 40 horas num documento que não vem com hora?

**Marcelo Costa:** Ah, porque ele pode, na regra pode pode existir 40 horas,

**Off Digital:** Então,

**Marcelo Costa:** entendeu?

**Off Digital:** então se a regra exige 40 horas e o documento não vem com horas, então é porque todo documento é 40 horas.

### 02:14:40 {#02:14:40}

**Off Digital:** Não,

**Marcelo Costa:** Pode, pode ser.

**Off Digital:** porque se o documento não vem com hora

**Marcelo Costa:** Então aí o ponto aí o ponto é, por exemplo, essas regrinhas que é f\*\*\*, velho,

**Off Digital:** Ne.

**Marcelo Costa:** porque vamos lá, o coque lá, por exemplo, ou tem uns que é tipo é carteira de registro, então o cara não, pô, eu tenho documento, quantas horas foi, se foi 40, 50, não sei quantas foi. O importante é o ter o documento, né? Agora, onde é que ele tá barrando aqui, né? Se eu botei o C, ele tá vindo, ele tá puxando da onde? Vamos fazer o seguinte, ó. Vamos fazer o

**Off Digital:** Não, mas eu acho que isso não é uma questão muito relevante não,

**Marcelo Costa:** seguinte.

**Off Digital:** por tipo assim, eh, eu acho que tava com problema no CAC mesmo. Vamos ver se a gente se a gente resolve. Mas fora isso, eu acho que não tem porque a gente O que você quer saber o que se quando você especifica as horas aí ele funciona. É isso?

**Marcelo Costa:** Se ele barra as horas

**Off Digital:** Eu acho que não,

**Marcelo Costa:** aqui,

**Off Digital:** velho. Eu acho que esse negócio das horas aí não tá ligado

**Marcelo Costa:** é que na no STCW ele não tem muito essa parada de horas,

### 02:15:47 {#02:15:47}

**Off Digital:** não.

**Marcelo Costa:** mas quando você vai para para NR,

**Off Digital:** Mas as NR já tem as horas na nos documentos.

**Marcelo Costa:** eh, Eu vou zerar tudo aqui porque na matriz original não tem p\*\*\*\*

**Off Digital:** É isso aí.

**Marcelo Costa:** nenhuma de hora. Então eu vou zerar

**Off Digital:** Não, essas horas elas não estão valendo,

**Marcelo Costa:** todas.

**Off Digital:** eu tenho quase certeza. Ó, põe ali adicionar documento, põe uma NR aí que tem hora, só pra gente ver. Não abre para mim aqui o popup.

**Marcelo Costa:** É, é, não abre, mas eu sei que ela

**Off Digital:** Aí põe aí NR, sei lá, 37\. 37 não,

**Marcelo Costa:** tem.

**Off Digital:** 33\. Aí põe 8 horas, sei lá. Ó, ele lembra que ele já tava configurado para o que for o quando você digita a hora, ele já aparece os documentos das

**Marcelo Costa:** Sim. É.

**Off Digital:** horas.

**Marcelo Costa:** E aqui, ó. Vamos lá. Quando eu venho, eu vou excluir esse CAC aqui, tá? Ó, excluir o CAC. Aí eu vou vir de

**Off Digital:** Uhum.

**Marcelo Costa:** novo.

**Off Digital:** Tá.

**Marcelo Costa:** Que que ele trouxe,

**Off Digital:** Beleza. É isso. Não colocou nada.

**Marcelo Costa:** ó?

### 02:17:07 {#02:17:07}

**Marcelo Costa:** Ó, ele trouxe automático 40 horas,

**Off Digital:** Sem.

**Marcelo Costa:** ó.

**Off Digital:** Hum,

**Marcelo Costa:** Tá vendo? Porque lá na base dá

**Off Digital:** entendi,

**Marcelo Costa:** 40\.

**Off Digital:** entendi.

**Marcelo Costa:** Mas aí vamos zerar.

**Off Digital:** Zera para ver se zerando funciona.

**Marcelo Costa:** Vou zerar.

**Off Digital:** Ele tá ainda tá subindo aqui as outras coisas.

**Marcelo Costa:** É. Aí eu vou. Beleza. Zerei. Criei uma matriz. Ele vai criar V2. V2. Aí nós vamos lá nos cara. Vou criar novo candidato que vai ser aquele Fábio.

**Off Digital:** Так.

**Marcelo Costa:** Fábio Pestana da Silva. V2. M.

**Off Digital:** Eu tô adicionando uma regra aqui que se o documento não tem carga horária emitida, você não pode reprovar ele por hora, entendeu?

**Marcelo Costa:** Se pera aí, se ele não tem

**Off Digital:** Se no documento ele não ele não tem emissão de carga horária dentro do

**Marcelo Costa:** No

**Off Digital:** documento, você não pode barrar ele por hora exigida na

**Marcelo Costa:** não, mas aí não,

**Off Digital:** matriz.

**Marcelo Costa:** porque é o seguinte, os caras pode ser às vezes tem umas umas coisinha umas na NR quando você entra tem bastante divergência.

### 02:19:47 {#02:19:47}

**Marcelo Costa:** Aí, por exemplo, você pega um carinha que, sei lá, uma certificadora bosta que o cara não põe a hora.

**Off Digital:** Não, ST STCW ou Pito. Tô falando,

**Marcelo Costa:** STCW Pito. Gente, eu acho que eles nenhum vem hora em SCW pito.

**Off Digital:** então. Porque a NR a gente já tem, a gente já trabalhou esse rolê das horas.

**Marcelo Costa:** Bora ver o Fábio. Passou geral. Não ficou um pendente.

**Off Digital:** Passou,

**Marcelo Costa:** Tá certo.

**Off Digital:** passou. É,

**Marcelo Costa:** Agora ele passou geral.

**Off Digital:** é, já entrou aqui já o E não tem mesmo,

**Marcelo Costa:** Passou só o que não tinha agora.

**Off Digital:** né?

**Marcelo Costa:** Hã, não,

**Off Digital:** Não tem esse BCT.

**Marcelo Costa:** esse aqui não tem documento. Tá certo. Tá perfeito.

**Off Digital:** Tá beleza. Vamos mais um.

**Marcelo Costa:** Agora vamos vamos excluir o cara e voltar o Mateus lá para

**Off Digital:** Tem mais um aí?

**Marcelo Costa:** ver.

**Off Digital:** Vamos.

**Marcelo Costa:** Excluir. Eita. Excluiu tudo aí, será? sem

**Off Digital:** Não, não mexi

**Marcelo Costa:** querer.

**Off Digital:** não. Põe no nas matrizes aí para Ah, é que ele tava mexendo na PI aqui.

### 02:21:21 {#02:21:21}

**Marcelo Costa:** Oi, Quando eu faço a V2, ele já some. Ele nem deixa a V1 aqui. Só fica o rastro lá, né? Ué. Eita,

**Off Digital:** Qual foi?

**Marcelo Costa:** pegou um que eu tinha exportado do próprio Certify. Aqui, lembra que só tinha quatro documentos que estavam lá?

**Off Digital:** Quer cancelar? Cancela. Exclui, exclui e cria de novo.

**Marcelo Costa:** Aqui ele cancela.

**Off Digital:** Cancela. digo, ele não vai cancelar, ele vai processar os documentos,

**Marcelo Costa:** Então, pera aí,

**Off Digital:** Так.

**Marcelo Costa:** deixa eu ver aqui.

**Off Digital:** Rapaz, a chinela tá cantando aqui, velho. Já foi 10% do Cláudio. Quase 7% aqui. Só de nessa primeira brincadeira, bicho. É rasgador.

**Marcelo Costa:** Comedou, comedor, comedor de toque. Так. Beleza. Uma coisa que a gente não, que eu queria até e até testar é pegar os documentos de outro cara e jogar com o nome do outro para ver o que vai dar.

**Off Digital:** Não, ele não influencia nada o nome do documento.

**Marcelo Costa:** Mas deveria, né?

**Off Digital:** Não, o nome, o

**Marcelo Costa:** Não, eu abri a eu abri o Mateus e joguei o documento do Fábio.

### 02:24:26 {#02:24:26}

**Off Digital:** título.

**Marcelo Costa:** Ele vai falar: "Ó, esse documento não é do Mateus, ele deve falar,

**Off Digital:** Eu acho que ele vai processar o documento e não vai jogar para lugar nenhum dentro do Mateus,

**Marcelo Costa:** né?"

**Off Digital:** vai jogar para um pro vai ficar dentro do Super base, não vai acontecer nada.

**Marcelo Costa:** Vamos testar depois para ver.

**Off Digital:** Porque ele não tem como saber. saber de automático de quem que é o documento, só depois que ele processar, entendeu?

**Marcelo Costa:** Sim, mas ele lembra que a gente falou isso lá lá no começo que era assim, pô, como se eu subir, porque ele pode pegar lá, ah, o CPSP do Fábio e dá validar. Você nem viu. Ele validou no Mateus. Ele não conferiu se é do Mateus o documento.

**Off Digital:** Não, mas ele não vai validar se não bater o nome.

**Marcelo Costa:** Então é isso que eu é é esse que é o que a gente imagina, né?

**Off Digital:** Não. Documento repetido eu já testei também. Se eu subir o documento repetido, ele

**Marcelo Costa:** Aí vamos pro Vamos vamos pro pau.

**Off Digital:** não

**Marcelo Costa:** Vai meninão. Boa. Só ficou o horário agora. Passou geral. Aê.

**Off Digital:** tá lá,

**Marcelo Costa:** Agora sim.

**Off Digital:** tá lá.

### 02:25:56 {#02:25:56}

**Off Digital:** Então essa matriz a gente

**Marcelo Costa:** Eh, vamos fazer um teste aqui,

**Off Digital:** zerou.

**Marcelo Costa:** ó. Vamos subir um arquivo do Pera aí, deixa eu ver aqui. Esse esse cara é o Qual que tá faltando dele? EB EBCP. Vamos dar uma dar uma bugada na cabeça dele agora. Ah, o MVC bem o que não tem. Vamos ver, vamos dar um bug na cabeça dele aqui para ver o que ele vai fazer. Cadê a p\*\*\*\* do documento, meu irmão? fez o download, não aparece aqui para eu subir, cara. velho. Agora é para sacanear mesmo. Vamos ver o que ele vai. Eu

**Off Digital:** Meu palpite é que ele carrega o documento e ele não vai aparecer aí na na no junto com os outros.

**Marcelo Costa:** acho que ele já vai dar um não não bate o nome. Ele para mim ele já vai avisar em algum canto. vai jogar no deveria jogar lá no Extra,

**Off Digital:** É porque, velho,

**Marcelo Costa:** né?

**Off Digital:** ele não, se você não criar essa notificação de que não bate, ele não vai ter essa notificação, tá ligado? Eu acho que essa é

**Marcelo Costa:** Mas eu acho que a gente criou lá atrás porque esse era um dos primeiros filtro que

**Off Digital:** a

**Marcelo Costa:** tinha.

### 02:29:22

**Off Digital:** Eu acho que a notificação não. Vamos ver. que eu não lembro de ter criado isso.

**Marcelo Costa:** Porque os caras fazem isso, velho. Pega documento dos outros e sobe.

**Off Digital:** Угуm.

**Marcelo Costa:** Porque vem sem nome, vem com foto do WhatsApp, o cara se confunde lá e pá.

**Off Digital:** ver resultado. É, não foi para lugar nenhum, foi o que eu imaginei. Ele vai pra base, velho. ele vai pra base enquanto você não. Agora, se você adicionar esse candidato lá, provavelmente que ele já vai pegar o documento e vai endereçar para esse candidato.

**Marcelo Costa:** Será?

**Off Digital:** Eh, é o que faz mais sentido para mim, porque ele lê o documento, manda pra base, mas ele não vai endereçar pro cliente que é outro cara, entendeu?

**Marcelo Costa:** É, e se a gente fizer, vamos fazer só um teste aqui, então, do seguinte, ó. Vamos pegar, vamos, deixa eu pegar um outro último cara aqui. Igor Linhares tem mais uns documentos aqui, então vamos puxar os documentos do Igor.

**Off Digital:** quatro confere três pendente.

**Marcelo Costa:** Ne. Só que aí vou trazer um documento do Fábio.

**Off Digital:** อ

**Marcelo Costa:** Eu

**Off Digital:** Que que você tá subindo,

**Marcelo Costa:** abri o outro cara,

### 02:32:19

**Off Digital:** mim?

**Marcelo Costa:** mas subi o documento do Fábio. Um cara novo, mas subi outro documento de outro cara. Só para ver se ele vai também ocultar,

**Off Digital:** Entendi.

**Marcelo Costa:** que que ele vai

**Off Digital:** Entendi. Eu acho que ele vai fazer a mesma coisa.

**Marcelo Costa:** fazer.

**Off Digital:** Ele vai carregar e vai ficar zerado no no do cara.

**Marcelo Costa:** Era bom em algum momento ele informar só porque você imagina o seguinte, isso acontece, o cara mandou três documentos sem nome, eu não tô abrindo os documentos, eu vou subir. Aí eu subi, o documento sumiu. Falou: "p\*\*\*\*, subi 10 documentos, velho, por que que sumiu três?" p\*\*\*\*, não era o documento do cara. Aí eu fico sem saber, entendeu? Porque o cara ele não vai abrir cada um dos documentos, né? Ele tem lá 20 documentos, ele não tem por talvez ele ele pudesse já nessa primeira extração, porque aqui ele faz o OCR, né?

**Off Digital:** Vai

**Marcelo Costa:** Ele deve ele já cruza com o com o com o nome. Vamos ver o que ele fez aqui. Decisão automática. Não confere. Ó, titular, documento divergente do candidato.

**Off Digital:** Aonde tá isso?

**Marcelo Costa:** Aqui, ó.

### 02:33:42 {#02:33:42}

**Marcelo Costa:** É que tá no popup. Ele tá subindo um pop-up aqui.

**Off Digital:** Ah, põe na revisão aí

**Marcelo Costa:** Titular documento diferente do candidato, data de emissão, validade e tal,

**Off Digital:** para

**Marcelo Costa:** não sei o quê. Então, só que aí ele tá ficando imparcial, né?

**Off Digital:** é porque o parcial é o único lugar que a gente tem para não confere hoje,

**Marcelo Costa:** É.

**Off Digital:** né? Por isso que eu te falei que era legal ter uma aba de não confere. Porque tem muitos erros que não tem nada a ver com o parcial, entendeu?

**Marcelo Costa:** Então, mas o excedente, o excedente ele não confere, certo? é igual a esse aqui. Esse documento aqui,

**Off Digital:** É,

**Marcelo Costa:** ele é um ele é um excedente

**Off Digital:** é, é, a gente já, já fez essa,

**Marcelo Costa:** é nosso nessa reflexão,

**Off Digital:** essa reflexão assim na prática,

**Marcelo Costa:** né?

**Off Digital:** se você for extremamente assim no sentido de eh exclusão, se você for por exclusão. Sim, se ele não é parcial, o que sobra é excedente, mas na prática não é que ele é excedente, eh, para mim excedente é o que a matriz não pediu. Agora, isso é um documento que é de outra pessoa, mas a matriz pediu, entendeu?

### 02:35:08

**Off Digital:** Então ele é

**Marcelo Costa:** É, mas ele podia ser e se ele fosse um de outra pessoa que a matriz não pediu?

**Off Digital:** um Aí ele tem que dar um excedente

**Marcelo Costa:** Ele vai para excedente, então falar: "Tá bom, a matriz pediu isso aqui, só que ele não confere,

**Off Digital:** só que tá errado.

**Marcelo Costa:** velho. É errado,

**Off Digital:** Só que tá errado. Exato.

**Marcelo Costa:** né?

**Off Digital:** Porque o excedente a cada coluna tem uma regra do que mostra ação. Então, parcial é a única coluna que você tem essa observação, porque pendente você não precisa de observação e confere também não.

**Marcelo Costa:** excedente não tem observação.

**Off Digital:** O cedente não tem observação.

**Marcelo Costa:** Entendi.

**Off Digital:** Cedente é tipo,

**Marcelo Costa:** Aí, beleza. Aí,

**Off Digital:** cara,

**Marcelo Costa:** aí o consegue ver,

**Off Digital:** ah,

**Marcelo Costa:** tá

**Off Digital:** tipo a matriz.

**Marcelo Costa:** certo?

**Off Digital:** Agora parcial é um nome que fica muito assim naquela parcial. O que a gente pode é mudar parcial para não confere. Independente se eh um não confere pequeno ou não confere grande, não confere. Se é porque deu um probleminha na data ou whatever, tipo, não

**Marcelo Costa:** É, mas é é que eu acho que o na hora no na execução,

### 02:36:07 {#02:36:07}

**Off Digital:** confere.

**Marcelo Costa:** eu acho que vale um mais um não conf no no dia a dia, quando você começa a subir um monte de candidato, você tá olhando a a coisa, o parcial ele é um momento que deve atenção, porque tem caras, tem horas lá na decisão do cara que ele vai falar assim, ó: "Ó, esse cara tem o 20 horas, só vale o a matriz pediu 40". Ele vai falar: "Cara, ele é parcial". O cliente às vezes fala: "Beleza, velho, tô precisando do cara, manda ele assim mesmo, depois ele faz o resto."

**Off Digital:** É, eu entendo o que você tem, o que você tem que pensar, primo, é, é nesse tipo de comodidade versus complexidade.

**Marcelo Costa:** Então,

**Off Digital:** Porque pra gente ter duas colunas não confere parcial, a gente vai ter que criar várias subdivisões do que vai para parcial, que vai para não confere. Então o que que é melhor?

**Marcelo Costa:** é mais regra, né?

**Off Digital:** Complexidade de motor ou o cara entender que o que não confere não confere? Beleza, velho. Você pede 20, tem, você pede 40, tem 20\. Não confere. Você quer aprovar, você aprova. Até porque do jeito que o motor tá indo aí, vai ficar muito mais documento pendente do que

### 02:37:20

**Marcelo Costa:** Eh,

**Off Digital:** imparcial.

**Marcelo Costa:** agora o problema é que quando você manda ele para não confere, imagina que eu subi 20 documentos, aí eu tenho lá.

**Off Digital:** Uhum.

**Marcelo Costa:** Ah, tudo bem. Eu não confere que ele é não

**Off Digital:** Confere. É, tá aprovado. Não confere,

**Marcelo Costa:** confere

**Off Digital:** não tá aprovado. Basicamente isso. E pendente é que falta e excedente é o que não pediu.

**Marcelo Costa:** não confere. É o que ou não vai ser o parcial hoje, né?

**Off Digital:** Não confere seria o parcial, só que é mais abrangente, porque parcial ele é um não confere, mas dá para aprovar,

**Marcelo Costa:** Dá para provar. É

**Off Digital:** né? Então assim, são duas opções,

**Marcelo Costa:** isso.

**Off Digital:** ou uma coluna nova, ou troca tudo para não confere e aí depois aos poucos vai criando as regras do que é parcial, né? seria uma opção. Eu não sei se é tão complexo a gente ter duas, mas eu só tô te falando que a gente já tá num ponto de complexidade tão grande que a gente tem que pensar um

**Marcelo Costa:** É, não,

**Off Digital:** pouco,

**Marcelo Costa:** qualquer coisa mais tem que pensar, velho.

**Off Digital:** a gente tem que pensar um pouco mais na gente agora,

### 02:38:41 {#02:38:41}

**Marcelo Costa:** Porque assim,

**Off Digital:** entendeu? Porque a gente já tá, já tá dando muito.

**Marcelo Costa:** não,

**Off Digital:** Então,

**Marcelo Costa:** e outra, se a gente põe mais uma,

**Off Digital:** p\*\*\*\*.

**Marcelo Costa:** é um monte de teste mais que ele começa, aí ele começa, ah, mas é que não sei o quê. É um monte de regrinha, velho, que tem que

**Off Digital:** Exato. Então aí ele vai dar e não confere o que era para ser parcial e aí o cara vai confiar nisso e e

**Marcelo Costa:** criar,

**Off Digital:** entendeu? Então assim,

**Marcelo Costa:** ó. Mas vamos pensar o seguinte,

**Off Digital:** mas beleza, do jeito que tá já funciona.

**Marcelo Costa:** aí eu é do jeito do jeito que tá funciona em outro cara

**Off Digital:** Se tá imparcial é porque não

**Marcelo Costa:** que você não tá vendo,

**Off Digital:** não

**Marcelo Costa:** mas quando eu ponho aqui, ó, decisão automática não confere titular

**Off Digital:** e outra, essa observação,

**Marcelo Costa:** doente.

**Off Digital:** ela ainda não tá do jeito que eu tô criando na tela nova, que vai ficar a taginha com, lembra que eu te mostrei que vai ficar uma tag mais clara do que foi a parada? Então, em vez de est assim, eh,

**Marcelo Costa:** Sim.

**Off Digital:** conformidade, decisão automática, não confere, vai tá escrito assim, nome divergente,

### 02:39:37 {#02:39:37}

**Marcelo Costa:** É, mas olha, olha o popup aí que tá aqui,

**Off Digital:** ponto decisão automática,

**Marcelo Costa:** ó. Mandei no zap aí, ó.

**Off Digital:** não confere titular documento div P do candidato da admissão. Pá, pá, pá. Isso aí vai est na revisão. Isso aí vai tá no detalhe da revisão e ali na tela vai tá assim: candidato divergente,

**Marcelo Costa:** Então, deixa eu ver se ele foi paraa revisão. Esse cara

**Off Digital:** porque

**Marcelo Costa:** aqui

**Off Digital:** não, ele Oi,

**Marcelo Costa:** ele veio paraa revisão, ó. Identidade confere. Aí fodeu. Ó,

**Off Digital:** calma aí.

**Marcelo Costa:** esse é do Fábio.

**Off Digital:** Mas qual que é o nome do cara?

**Marcelo Costa:** O nome do cara é Igor, ó. Igor

**Off Digital:** E qual é o nome do cara do documento?

**Marcelo Costa:** Fábio.

**Off Digital:** Tá. É, então é porque a revisão ela não tá não,

**Marcelo Costa:** Não, é que aqui nós estamos truncando ele, né, velho? Nós estamos também

**Off Digital:** mas beleza, mas isso é tudo erro de fronte, velho. Não é de back.

**Marcelo Costa:** fazendo,

**Off Digital:** A revisão ela, a o detalhe do candidato tá julgando certo, mas a revisão não tá espelhando isso.

### 02:40:48 {#02:40:48}

**Off Digital:** Beleza,

**Marcelo Costa:** ó.

**Off Digital:** deixa eu já arrumar isso aí,

**Marcelo Costa:** Porque ficou parcial.

**Off Digital:** vai.

**Marcelo Costa:** Resultado ficou parcial porque o titular do documento diverge do

**Off Digital:** É só fronte,

**Marcelo Costa:** candidato.

**Off Digital:** velho. O que tá escrito ali não tá correto com com o motor.

**Marcelo Costa:** Isso,

**Off Digital:** Pera aí.

**Marcelo Costa:** isso aqui,

**Off Digital:** Exato. Então, pera aí,

**Marcelo Costa:** né?

**Off Digital:** já vou arrumar agora. Só que eu não tô muito muito na noia porque eu vou mudar a tela lá. Então, deixa eu ver

**Marcelo Costa:** É, mas isso é um é um reflexo que independente de você mudar a tela,

**Off Digital:** aqui.

**Marcelo Costa:** é importante que você esquece esse detalhe aí, né?

**Off Digital:** Não, já vou aproveitar, já arrumo agora. Pera aí.

**Marcelo Costa:** E até, por exemplo, o código dele. Aí ele botou aqui a identidade confere o código divergente, não, o código bate.

**Off Digital:** Passa. Posso falar? Não, não. Você pode passar para lá. Volta lá para mim rapidão. Ô, tá rodando aqui

**Marcelo Costa:** Tá.

**Off Digital:** já.

**Marcelo Costa:** Então aí eu queria ver. Bom, vamos rodar, vamos botar agora os documentos dele mesmo.

### 02:43:21 {#02:43:21}

**Marcelo Costa:** Aí eu queria ver como que que ele vai fazer se eu subir o coque do cara certo agora. Se ele vai substituir aqui. Vamos ver se o Igor tem. Ele tem. Então vamos fazer assim, ó. Vamos subir diretamente aqui. Você entendeu? Eu subi um errado, ele foi lá no parcial. Agora eu tô subindo certo para ver se ele

**Off Digital:** Uhum. Fou certo.

**Marcelo Costa:** Aí ele não, ó, fora da exigência, ele não leu,

**Off Digital:** Tá.

**Marcelo Costa:** ó.

**Off Digital:** Apaga aí, apaga os dois aí pra gente ver e sobe de novo.

**Marcelo Costa:** Só ver qual que é o documento. Pera aí. Eu tô achando que esse documento é outra coisa. É 1/3. 1 bar é 1 barra é 3/1. Então tá certo. Não vamos excluir os documentos todos, né? Так.

**Off Digital:** Tinha ido errado para mim. tinha ido

**Marcelo Costa:** Hã,

**Off Digital:** errado,

**Marcelo Costa:** não, ele foi para excedente, né?

**Off Digital:** mas era o documento certo

**Marcelo Costa:** Era,

**Off Digital:** mesmo.

**Marcelo Costa:** ele deveria ter substituído aquele lá, né? Agora apaguei tudo.

**Off Digital:** Uhum.

### 02:47:06

**Marcelo Costa:** Vamos ver o que que ele vai

**Off Digital:** Oi,

**Marcelo Costa:** Não classificou.

**Off Digital:** Ô,

**Marcelo Costa:** Então vamos ter certeza que documento é

**Off Digital:** mesma coisa, velho. Pera aí.

**Marcelo Costa:** esse.

**Off Digital:** Qual documento é esse? Ele, a gente já tinha subido

**Marcelo Costa:** Não,

**Off Digital:** ele,

**Marcelo Costa:** esse aqui é do outro cara, do cara novo que é o Igor,

**Off Digital:** mas é um documento que a gente já tinha

**Marcelo Costa:** ó. Não, ele é diferente um pouco,

**Off Digital:** subido.

**Marcelo Costa:** ó. Ele tá aqui. Ele é, ó, tá vendo o código aqui? 3/1 3/3/1

**Off Digital:** Tá, não exclui ele não. Tô pedindo pro cara ver aqui o que que é.

**Marcelo Costa:** 3/3. O pendente aqui, ó, o que eu imaginei que ele vem aqui, ó, 3/1.

**Off Digital:** É porque esse erro aí, que que ele disse no erro não

**Marcelo Costa:** É, ele só dá que não

**Off Digital:** classificado?

**Marcelo Costa:** é não classificado, tipo, não exigido na matriz, né? Não, não tá exigido. Mas aqui o código, ó, ele bate. Pode ser que esse documento aqui tem alguma, ó, gerenciamento de praça de máquina.

### 02:48:59

**Marcelo Costa:** Ó, o curso é gerenciamento de praça de máquina. Eu quando eu vou lá no outros carinha, vamos no Mateus. Ó, quando bateu o cara aqui é esse, ó. é outro documento certificado emitido de acordo convenção. Então aquele documento não é o é

**Off Digital:** Ele é excedente mesmo,

**Marcelo Costa:** excedente, porque apesar dele ter a mesma regra aqui,

**Off Digital:** mas

**Marcelo Costa:** ele ele tem o mesmo número, mas ele eles entendem lá que é às vezes é tabela, é não sei o quê, mas enfim, tá certo o que ele fez aqui.

**Off Digital:** tá, mas ele mesmo assim não tem que aparecer não classificado.

**Marcelo Costa:** É, não classificado, não foi exigido, velho. Não preciso nem folhar para ele, certo? Só que aqui nesse no certifi nosso, ele bateu como se fosse, ó. Mas não é, que isso aqui é gerenciamento de praça e de máquinas.

**Off Digital:** E ele pede o quê? Oficial de máquina é operacional, é outra

**Marcelo Costa:** É outra

**Off Digital:** coisa.

**Marcelo Costa:** coisa. Então, beleza. O nosso tá certo ali. Vamos subir mais coisa desse cara.

**Off Digital:** Mas não exclui esse excedente não que eu tô vendo aqui.

**Marcelo Costa:** Não vou deixar. Vou subir só outros documentos dele.

### 02:51:00 {#02:51:00}

**Marcelo Costa:** Meninas, mostrar para vocês minha. É isso. para uma mulher aí cada momento se é para foi aqui. Vamos ver agora. Indoidou. Ele passou um CAC, passou um C.

**Off Digital:** Mas tem

**Marcelo Costa:** Mostrar elas porque tá chovendo.

**Off Digital:** K

**Marcelo Costa:** Elas estão lá na escola. Tá bom.

**Off Digital:** passou dois K para

**Marcelo Costa:** Não,

**Off Digital:** mim.

**Marcelo Costa:** mas ó, ele tá botando cicla CAC. Mas ó, ó o requisito CBSP. e o outro CBSN. Então são os dois documentos que eu subi,

**Off Digital:** О.

**Marcelo Costa:** mas ele trouxe a a sigla CAC. E aqui ambío também no na na p\*\*\*\* É o ambigo aqui, ele tá ficando doido, né? Isso aqui já tinha resolvido, né?

**Off Digital:** Vého, eu acabou de falar aqui para mim mim. Olha só, os dois problemas do candidato Mateus já estão resolvidos. A data ambiga do Terrilt e o bloqueio de carga horária do do K não acontecem mais. O fix das datas antigas que da Big já existia, mas nunca tinha chegado em produção, foi resgatado, mergeado para que possou aceitar a carga oficial. Verifiquei estado real 13\. Isso aqui.

### 02:54:33

**Off Digital:** Pera aí, deixa eu copiar a imagem para ele aqui para ver se deu algum bizio, porque foi bem na hora que ele botou a a a parada no ar aqui que você subiu de novo, que deu essa que deu essa

**Marcelo Costa:** É, eu acho que ele deu.

**Off Digital:** pau.

**Marcelo Costa:** Vamos apagar tudo esses loucos aqui, né?

**Off Digital:** Não, deixa, deixa aí para ele, para ele ver.

**Marcelo Costa:** É, tá falando que não substitui o CAC. Mas quem que tá falando que é CAC, meu irmão? Ah, já sei.

**Off Digital:** Mm.

**Marcelo Costa:** Não, não, não. Eu subi, eu subi aqui no upload normal.

**Off Digital:** Não, mesmo assim, pô.

**Marcelo Costa:** Aí ele já bateu um curso avançado, ele já bateu o sir, ele beleza, bateu aí ele subiu o CDSN, mas tá falando que a sigla é CAC, só que o código V13 e também AV13.

**Off Digital:** O código tá certo,

**Marcelo Costa:** Aí o código do debaixo V13

**Off Digital:** só que não é CAC.

**Marcelo Costa:** especial avançado com bate a incêndio. Aqui ele duplicou aqui. Ele duplicou o CAC.

**Off Digital:** Então, esses dois K são a mesma

**Marcelo Costa:** Não, ó, esse esse aqui é o CBSN.

**Off Digital:** coisa.

### 02:56:23 {#02:56:23}

**Marcelo Costa:** Deixa eu ver. Não é TAC também. Ele duplicou, triplicou,

**Off Digital:** Como triplicou?

**Marcelo Costa:** ó.

**Off Digital:** Um é avançado

**Marcelo Costa:** Então, os dois,

**Off Digital:** incêndio.

**Marcelo Costa:** ô, o nome que ele tá trazendo aqui não tem nada a ver. Os dois são c os documentos. Mas eu não subi três CAC,

**Off Digital:** Subiu só um.

**Marcelo Costa:** subi só um.

**Off Digital:** E aqueles antigos que você tinha subido era do Igor? Aqueles que você tava testando errado era

**Marcelo Costa:** Hum.

**Off Digital:** dele.

**Marcelo Costa:** Era, mas eu tinha subido do Fábio

**Off Digital:** Mas antes você tinha subido do Igor no nos outros

**Marcelo Costa:** aqui.

**Off Digital:** candidatos, porque às vezes se ele se não tinha esse candidato criado, mas já tinha documento dele na base,

**Marcelo Costa:** Ele puxou agora tudo.

**Off Digital:** ele puxou agora. É possível,

**Marcelo Costa:** É,

**Off Digital:** mas vamos

**Marcelo Costa:** mas não tem a ver, né? Aqui, ó.

**Off Digital:** ver.

**Marcelo Costa:** Você tá, ele tá vindo falando que é CAC e tá puxando CBSN. Não tem nada a ver. Ó, o documento é CAC. Aí, que que ele tá falando? CBSN ou CBSP. Esse o documento é CAC.

### 02:57:55

**Marcelo Costa:** Quebra cabeça, doido, né, para mim? na casa do meu irmão, deixei a criança dentro do carro. Aí falei: "Vou voltar a porta não abre porque a criança se trancou lá dentro porque a chave não trava, mas ela só se apertar que trava. Abre aqui pro papai, ó. Aperta o botão aqui. Aperta aqui, ó. Cadê a chave? Pega a chave do papai. A chave. Pega a chave. Pega ela. Aperta o botão nela. Aperta o botão. Aperta. Muito bem. Eu queria muito ter tido mais isso. Eu nunca vi alguém com a difícil desabafo e repetir grande essa semana que ele faz aqui a grande maioria das pessoas fazendoes que é daquele os filhos a gente consegue bancar. O problema é que essa não considera simples. Ela muda, as coisas mudam, tudo mudam. É importante a gente ter responsabilidade, tá? Mas deixa eu fazer uma pergunta para você. Uma, você gosta? Você quer continuar fazendo balé ou você quer fazer só? Você não quer fazer mais balé? Eia, você só quer fazer balé ou você quer fazer judô também? Você não quer mais fazer judô?

### 03:00:00

**Marcelo Costa:** desse resultado. Esse resultado não tchau. Desconstrução. É isso. Eles não querem respeitar a escolha natural das crianças. Eles querem descomando para avisar que o aniversário do não músicana. Você que é linda, que chama autonomia, o quarto fica bonito, ficou bem p Mas ela nem de conta. Se eu fui dialético lá, meu marido é um gênio e eu só descobri isso depois de casar. A única coisa que ele tem de dantista é uma cara que coloca o cabelo é brocha. Caraca,

**Off Digital:** О.

**Marcelo Costa:** é brocha. Se você tem plano de saúde se chegava aqui para não é para existe uma escola nos Estados Unidos consegue ver a tela bem esta é Rose. Nunca imaginei que uma coisa tão simples que a gente tem em casa e esse físico agrodamento. Hoje eu uso soro fisiológico no lugar de pentear o sabedo fica muito mais leve, brilhoso, sem aquele aspecto de sabe e olha como fica alinhado, penteado sem esposo.

**Off Digital:** Eu

**Marcelo Costa:** Meninas, testem isso. Nunca imaginei que uma coisa tão simples que a gente tem em casa e a gente perderam. tá deixando ele falar aí, PR?

**Off Digital:** vou О.

**Marcelo Costa:** É, mas agora eu tô vendo uma parada aqui, meu irmão.

### 03:01:57 {#03:01:57}

**Marcelo Costa:** Fiz uma parada. Beleza. Se beleza. Cque cque gerenciamento de máquinas gerenciamento de máquinas CAC a ID. Угу.

**Off Digital:** Mano, o bicho já já executou vários comandos aqui, já fez várias coisas, não me deu uma resposta até agora.

**Marcelo Costa:** Deixa eu ver se a bebê bebê chegou aqui,

**Off Digital:** 13 minutos.

**Marcelo Costa:** tá gritando aqui. Deixa eu ver.

**Off Digital:** Vai lá para mim.

**Marcelo Costa:** Tá chorando. Lavou. Ele lavou tudo. Prim.

**Off Digital:** E aí, GR?

**Marcelo Costa:** Vamos voltar logo menos aí. Como é que você tá aí? Depois, daqui a pouco vai seguir

**Off Digital:** Tô de boa.

**Marcelo Costa:** aí,

**Off Digital:** Vou vou seguir mexendo

**Marcelo Costa:** tá?

**Off Digital:** aqui.

**Marcelo Costa:** Só vou dar um dar uma assistência aqui rapidinho. Eh, a hora que tiver OK, me fala que eu quero. Vou pegar mais tem 18 cara dessa vaga. Aí eu vou subir subir mais gente aí dessa vaga e testando,

**Off Digital:** Aham.

**Marcelo Costa:** vendo o que que vai

**Off Digital:** Tá.

**Marcelo Costa:** bater.

**Off Digital:** Eh, tá. Eu acho que a gente pode fazer o seguinte, cara. Perta

**Marcelo Costa:** Vamos excluir esse Igor aqui.

### 03:09:00

**Off Digital:** só

**Marcelo Costa:** Ele tá olhando esse cara.

**Off Digital:** você me manda um zips aí do do do dos caras dessa matriz para eu ir apagando e subindo até dar OK aqui. Aí depois eu te falo e você sobe os outros, entendeu? Só aí você sobe uma porrada para ver se tá consistente. Pode ser até dos mesmos primo ali do Mateus, do do dos cara,

**Marcelo Costa:** Vamos pegar alguns aqui. Eu

**Off Digital:** Пото

**Marcelo Costa:** acho que vai cheg, acho que chegou alguém aqui em casa aí do das crianças que vai dar uma atenção ali para mim. Deixa eu ver. Pera aí. Chegou seu colega. Seu colega chegou aí. Você parou de chorar, foi? vai tomar banho. Beleza, chegou um coleguinha aqui, vai dar para dar uma segurada aqui para

**Off Digital:** Boa.

**Marcelo Costa:** ele.

**Off Digital:** tá quase terminando aqui, primo, de subir

**Marcelo Costa:** Pera aí um segundo.

**Off Digital:** A, pera aí, antes de você apagar um teste aqui. Ja.

**Marcelo Costa:** Oh.

**Off Digital:** Ô priminho, o que a gente poderia fazer é ir montando uma outra matriz. Tá quaseando já,

**Marcelo Costa:** Bora.

**Off Digital:** velho.

**Marcelo Costa:** Hã.

**Off Digital:** falando a gente montar uma outra matriz enquanto termino aqui.

### 03:18:17 {#03:18:17}

**Marcelo Costa:** Vamos. Deixa eu ver

**Off Digital:** He.

**Marcelo Costa:** aqui. Ah. É umas paradas de endosso que eu tô vendo aqui. Yeah. Ja. curando uma matriz aqui com com NR.

**Off Digital:** M.

**Marcelo Costa:** Vou colocar uma outra aqui.

**Off Digital:** Yeah.

**Marcelo Costa:** Так.

**Off Digital:** Ка. Kom. Priminho, ele tá mexendo aqui nas outras alterações. Ele caiu naquele ponto que a gente tava discutindo. Eh, deixa eu voltar na reunião aqui. Aqui, ó. falou, ó, contratar a apresentação das comparações que não conferem, por exemplo, o requisito catalogado como não equivalente, ajustar na na interface, ou seja, a tela passa a mostrar essas linhas como requisito pendente com a nota documento enviado não cobre este requisito em vez de parcial. ou muda só no motor para ele rebaixar de pendente para parcial. Para de rebaixar pendente para parcial. Ah, entendi. Decide o motor para de rebaixar pendente paraa parcial. que ele tá querendo dizer é exatamente que nesse caso deveria estar impendente, não imparcial,

**Marcelo Costa:** O quê?

**Off Digital:** quando o documento não cobre o requisito.

**Marcelo Costa:** pendente ao documento exigido pela matriz.

**Off Digital:** Sim,

**Marcelo Costa:** Certo?

### 03:28:33 {#03:28:33}

**Off Digital:** o que ele tá dizendo aqui é que na lógica correta e que parcial é o que exige correção, certo?

**Marcelo Costa:** Isso.

**Off Digital:** Ele tá perguntando como é que a gente quer tratar, por exemplo, nesse caso do C ficou três vezes, ou

**Marcelo Costa:** Porque subiu três documentos iguais.

**Off Digital:** seja,

**Marcelo Costa:** Será?

**Off Digital:** ó, deixa eu compartilhar aqui para você entender o feedback dele. Olha, falei que falou aqui, ó. Hum. Detalhe operacional. O veto de reprocessamento continua valendo. Mesmo config produção. O terroate do Igor só atualiza se for reprocessado enviado. Beleza. O K se apresentando três vezes, o motor decidiu certo. A tela conta a história errada. As três linhas são três comparações diferentes do mesmo documento. Eh, o CAC versus requisito CAC da matriz confere a linha verde com validade do 21/10/20130. O CAC versus requisitos CBSN e o CAC versus requisitos CBSP não confere porque existe regra catalogada dizendo que o treinamento básico de combate não substitui avançado. Decisão correta. O problema o problema o motor marca essas duas como pendente internamente e uma conversão automática na saída rebaixa tudo para parcial.

**Marcelo Costa:** Não, velho.

### 03:30:33 {#03:30:33}

**Marcelo Costa:** Você eh você tá pegando um documento que é o CAC e botou no lugar do outro, velho.

**Off Digital:** Mas na matriz ele tá pedindo CBSP e

**Marcelo Costa:** Sim, sim.

**Off Digital:** CBSN.

**Marcelo Costa:** E ele duplicou. Não sei por quê. Porque eu não subi todas as vezes daquele documento tudo junto. Vamos excluir aquele cara e subir de novo para ver o que acontece. Eu acho que ele fica, cara, ele dá muita nova, velho. Faz um monte de regra, p\*\*\* que pariu. E fala: "Velho, o bagulho é simples, meu irmão. Você subiu duas vezes, tá botando três vezes o documento errado nessa p\*\*\*\*". Vou apagar esse c\*\*\*\* aqui, ó, Igor. Ó, ele tá botando CAC, falando que é CAC no lugar de outro documento. Subiu três vezes o mesmo documento, então tem coisa errada. Vou apagar esse Igor aqui. Igor Rodrigues Linhares. Subi um CAC, um C, um documento que é praça e máquinas, que eu acho que esse tá errado, e um gerencial. Vamos ler

**Off Digital:** Põe, põe.

**Marcelo Costa:** agora.

**Off Digital:** Compartilhe aí.

**Marcelo Costa:** Sì.

**Off Digital:** Ja. ไป É

**Marcelo Costa:** Mesma história.

**Off Digital:** Aí

### 03:34:42 {#03:34:42}

**Marcelo Costa:** Sir bateu. Beleza. Eu subi quatro documentos,

**Off Digital:** Brasília,

**Marcelo Costa:** tá?

**Off Digital:** eu acho que tão perto sem trânsito é meia hora para ir em todo lugar.

**Marcelo Costa:** Sirik bateu.

**Off Digital:** Eh,

**Marcelo Costa:** Aí ele vem aqui,

**Off Digital:** mas você quando

**Marcelo Costa:** ó. Esse documento ele subiu um CA de novo que eu não mandei. Ele subiu um CAC de novo. Então ele subiu três vezes o CAC. Um ele confirmou, outros dois ele subiu e tá jogando no lugar errado. O Tertilt faz isso mesmo. Ele pira um dia antes do do período que ele fez. Então, em vez de um Ah,

**Off Digital:** Não subiu ainda o fix, primo. Ó.

**Marcelo Costa:** não.

**Off Digital:** Mas beleza, vamos subir outro candidato com os mesmos documentos, só para ver se tá sendo no Igor.

**Marcelo Costa:** Vamos lá pegar um outro

**Off Digital:** Да.

**Marcelo Costa:** cara. p\*\*\*\*, vamos ver o que ele vai fazer com esse cara aqui. Loran Aragão.

**Off Digital:** Esse só tem dois

**Marcelo Costa:** É,

**Off Digital:** documentos.

**Marcelo Costa:** mas tem uns parcial, ó. Sir, ó o sir, como o cara mandou, ó. Tá vendo?

**Off Digital:** Me deu passe por qu

**Marcelo Costa:** Seg.

### 03:36:45 {#03:36:45}

**Off Digital:** aí

**Marcelo Costa:** Atende por código sigla.

**Off Digital:** validade não

**Marcelo Costa:** validade não verificar não conseguiu verificar

**Off Digital:** verificável

**Marcelo Costa:** validade.

**Off Digital:** esses Esses caras tem BO com validade, né, velho?

**Marcelo Costa:** Pera aí, vamos ver o que acontece aqui. Não, é que cada um é tudo. Os cara manda, cada um manda um mais lazarento que o outro, velho. f\*\*\*. Ó, tem quatro documentos do Loran que subiu, então. 1 2 3 e 4\. Enc. Beleza, vamos ver se bate aqui. Curso especial de operação, sistema marítimo, alta tensão. Não tem nada a ver. Esse é alta tensão. É que ele tá batendo os códigos, ó. O código é o mesmo, eh, aqui, ó, f\*\*\*. Nome diferente. Código e alta tensão.

**Off Digital:** Mas é o mesmo

**Marcelo Costa:** É o mesmo código,

**Off Digital:** código.

**Marcelo Costa:** mas o documento é outro, velho.

**Off Digital:** É,

**Marcelo Costa:** nome.

**Off Digital:** esse aqui é o perigo de deixar ele cego no código, né?

**Marcelo Costa:** Ó, Loran,

**Off Digital:** Isso é STCW,

**Marcelo Costa:** eh, instruções básicas,

**Off Digital:** né?

**Marcelo Costa:** sobrevivência pessoal, combate, incêndio, primeiro socorro, segurança pessoal, responsabilidade social.

### 03:38:59 {#03:38:59}

**Marcelo Costa:** Esse aqui já é um

**Off Digital:** Para mim, eu implantei um bagulho aqui que é bem sinistro.

**Marcelo Costa:** que é ocurção

**Off Digital:** Depois eu te explico.

**Marcelo Costa:** Não,

**Off Digital:** Por isso que tá demorando uma eternidade para subir o fix.

**Marcelo Costa:** e o que que é, prim?

**Off Digital:** Cara, é um sistema que eu peguei do criador da OpenCloud, velho. Demorou uma semana para conseguir implementar. E agora que eu tô, eu nem lembrava que eu tinha colocado essa parada, mas agora que eu tô vendo na prática que ele tá ele tá atuando. Pera aí, voltar nessa tela. Deixa te mostrar aqui. Tá vendo que ele tá fazendo? Comit, p\*\*\*\*. Tá vendo que ele tá fazendo o commit aqui?

**Marcelo Costa:** Eh

**Off Digital:** Pera aí, deixa eu tirar aqui. Aí ele começou aqui, eu falei, p\*\*\*\*, 6,26 para fazer o o push, o me e o deploy. Geralmente isso aqui ele faz em 2, 3 minutos. Ele faz o o préflight e pá me deploya. Ó, são 6,58 e ele ainda não terminou de fazer. Aí você fala, velho, por quê? Ó, se liga. Eu instalei um negócio chama auto review, que é um mix de três skills, que uma chama Crab Box, a outra chama, enfim, é três repositórios diferentes do Git, tudo criado pelo dono do OpenCloud lá, o Stay Pit.

### 03:41:08

**Off Digital:** E aí você bota essas skills para rodar no teu VPS com codex

**Marcelo Costa:** Se

**Off Digital:** autenticado. E aí todo todo toda hora de de fazer deploy, ele sobe lá no no VPS o projeto e ele roda de verdade fazendo os testes. E aí ele fica aqui, ó. Ó, review vivo. 60 segundos de execução. Continua aguardando. Sem achado ainda. Ainda sem sinal. Auto review saudável 120 segundos. Sem resultado. 180 segundos, 240 segundos ainda rodando. Ó, auto review pegou dois riscos reais no OCR. Validade podia pegar data com demissão. Papá, vou implementar o FBEC. Código ajustado. Regressões adicionados extractor teste passou. Gates focados. Comite do CR. Tal tal reviewou. Type check. Tal tal. Auto review rodando no pacote já corrigido. Review vivo. 60 segundos. 120 segundos. 180 segundos. 240 segundos, 300 segundos. Review, pegou mais uma variação real. O rótulo validade em linha própria. Papá, beleza. Código ajustado. Regressão adicionada.

### 03:42:16 {#03:42:16}

**Off Digital:** Pá, beleza. Review 60 segundos, 120 segundos. Review tá correto de novo. Código endurecido.

**Marcelo Costa:** fica rodando não no

**Off Digital:** Negativo, velho. Ó lá, pá, bebê comit feito. Rodando. 60 segundos, 120, 180\. Revi encontrou mais dois pontos.

**Marcelo Costa:** pa

**Off Digital:** Vou deixar o fallback. Pá. Beleza, ó. 160 review vivo, 60, 120 e tá rodando. E o bicho só para quando, mano, o negócio fica filé, mano. Bizarro, tá ligado?

**Marcelo Costa:** deu aqui, primo.

**Off Digital:** Vai, volta lá.

**Marcelo Costa:** Só confirmou o EBSP que tá certo. Curso Base sobrevivência produção de Navio.

**Off Digital:** EBCP,

**Marcelo Costa:** Esse beleza. Ó,

**Off Digital:** né?

**Marcelo Costa:** agora ele tá ele ele endoidou mesmo, ó. Tá vendo? Tá trazendo três documentos iguais, ó. Um é CAC, trouxe CPSO, o outro é é CPSN. Trouxe o mesmo mesma, ele tá puxando o mesmo código, mesma

**Off Digital:** Tá,

**Marcelo Costa:** sigla.

**Off Digital:** faz um favor para mim, priminho.

### 03:43:35 {#03:43:35}

**Off Digital:** Pera aí, deixa eu tirar um print disso aqui. Deixa esse candidato aí parado. Eh, vamos subir o Mateus de novo. Exclui o Mateus e sobe ele de novo. Só para eu ver como é que vai, porque, p\*\*\*\*, tava perfeito, velho. Mateus e o e o Igor.

**Marcelo Costa:** É, eu acho que deu alguma

**Off Digital:** Foi alguma coisa que a gente fez aí, velho.

**Marcelo Costa:** Всё. Lá, falta só mais um. Bater esse cara aqui e vou ir para mim que eu preciso dar um um grau aqui na na bebê que tá na horinha dela. Vamos ver. Aí bateu.

**Off Digital:** Tá. Me manda me manda os documentos desses últimos dois cara aí no zap para mim do esses dois últimos que você subiu aí que tá dando pau. Manda o zip aí para mim.

**Marcelo Costa:** f\*\*\* que o cara não sabe da onde vem,

**Off Digital:** Não,

**Marcelo Costa:** né,

**Off Digital:** eu vou arrumar isso aqui hoje, velho.

**Marcelo Costa:** pegar mais um cara aqui, ó. Esse cara tem bastante. Confere. Tem 1 2 3 4\. Confere. E você vê que é uns documentos diferente, ó. Essa tabela que tá me me ferrando aqui, ó. Level.

**Off Digital:** Que

**Marcelo Costa:** É, essa aqui todo mundo vem,

**Off Digital:** tabela?

**Marcelo Costa:** tem vários documentos com essa mesmo. 3/1, só que é 3/1, 3/3. Aí é o que muda, entendeu? É o o 3/1 é é igual, mas o 3/3 que vem na sequência é o que muda. Esse é um que eu não criei ainda, esse Renan aí. Te mandei três cara, Loran e Igor é os que tá dando pau. Tem o Fábio também, né?

**Off Digital:** E o Mateus Fáil aí

**Marcelo Costa:** Fábio,

**Off Digital:** também.

**Marcelo Costa:** tem aí também.

**Off Digital:** Beleza. Vai lá, priminho. Vou vou mandar bala aqui.

**Marcelo Costa:** Tá bom. Te dou te dou um toque a hora que liberar.

**Off Digital:** Depois qualquer coisa mais tarde você me chama.

**Marcelo Costa:** Qualquer coisa aí, se você ajeitar alguma coisa, quiser que eu subo mais cara, eu vou subindo outras matrizes, me fala aí, só me dá um toque que eu vou testando.

**Off Digital:** te dou um feedback.

**Marcelo Costa:** Mais braço.

**Off Digital:** Valeu,

### A transcrição foi encerrada após 03:49:43

*Esta transcrição editável foi gerada por computador e pode conter erros. As pessoas também podem alterar o texto depois que ele for criado.*
