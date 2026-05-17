---
kind: sumario
project: certify-mvp
confidence: 0.85
title: "Melhorias Técnicas e Operacionais no Certify"
meeting_datetime: 2026-05-07T11:01:00
people: ["Marco", "Marcelo", "Letícia"]
tags: [kind/sumario, projeto/certify-mvp, pessoa/marco, pessoa/marcelo, pessoa/leticia]
gmail_message_id: 19e033e6a64bb72b
gmail_thread_id: 19e033e6a64bb72b
notes_doc_id: 1KjxNAgjB7UXaeFcgIPoS-QIlPQFY54wRmS_IztNha4s
---

# Melhorias Técnicas e Operacionais no Certify

**Participantes:** Marco, Marcelo, Letícia

# 📝 Observações

mai. 7, 2026

## Reunião em 7 de mai. de 2026 às 11:01 GMT-03:00

Registros da reunião [Transcrição](https://docs.google.com/document/d/1KjxNAgjB7UXaeFcgIPoS-QIlPQFY54wRmS_IztNha4s/edit?usp=drive_web&tab=t.8b3gds97kk6) 

### Resumo

Reunião abordou melhorias técnicas, estratégias de marketing de influência e implementação de agentes de inteligência artificial.

**Ajustes na plataforma Certify**  
Implementação de filtros por candidato e matriz foi concluída com sucesso. O foco atual reside na otimização do feedback de status de documentos e correção de fluxos pendentes.

**Estratégia de marketing digital**  
Discussão focou na construção de autoridade através do YouTube e na análise de engajamento via dados. Decisão prioriza parcerias de longo prazo integradas ao cotidiano das influenciadoras.

**Automação com inteligência artificial**  
Planejamento foca na criação de uma camada de inteligência artificial para automação de relatórios e diagnósticos logísticos. Decisão final prioriza automação de processos manuais críticos do cliente.

### Próximas etapas

- [ ] \[Off Digital\] Lógica Documento: Implementar lógica para que documentos rejeitados migrem para status pendente e documentos incorretos sigam para excedentes.

- [ ] \[Off Digital\] Detalhe Parcial: Adicionar no detalhe do candidato o motivo explícito para o documento continuar com status parcial.

- [ ] \[Off Digital\] Fluxo Desenvolvimento: Fazer todo o desenvolvimento em ambiente local antes de realizar o deploy para a URL pública.

- [ ] \[Marcelo Costa\] Conferir Base: Acessar a base de dados para confirmar se o requisito de 12 horas está correto nos documentos OPITO 4650\.

- [ ] \[Off Digital\] Adicionar Rolagem: Implementar a funcionalidade de rolagem (scrolling) na interface geral do sistema.

- [ ] \[Marcelo Costa\] Proposta Emily: Fechar o contrato atual com a Rampinelli e tentar incluir a próxima influenciadora (Emily) em uma proposta futura.

- [ ] \[Off Digital\] Logística Aulão: Fazer as preparações logísticas necessárias para o aulão de bolo de cenoura no Zoom.

- [ ] \[Letícia\] Replicar Vídeo: Letícia deve refazer o vídeo do Pão Pita, utilizando os mesmos takes e estilo para postar e analisar o resultado.

- [ ] \[Marcelo Costa\] Mostrar Trabalho: Apresentar o trabalho atual que está desenvolvendo.

- [ ] \[Marcelo Costa\] Compartilhar Recurso: Enviar para Off Digital o recurso da Meta sobre análise de vídeo (com base em ressonância magnética).

- [ ] \[Marcelo Costa\] Enviar Materiais: Mandar para Off Digital as duas chamadas de cliente e a mensagem prévia enviada ao cliente.

- [ ] \[O grupo\] Analisar Bloqueios: Abrir um agente para entender os motivos e padrões dos bloqueios de documentos.

- [ ] \[Off Digital\] Ajustar Nomes: Pedir ao desenvolvedor para corrigir os nomes das colunas do Kanban (Certificação, Aprovação, DP, Embarque).

- [ ] \[Off Digital\] Excluir Usuário: Implementar funcionalidade para exclusão de usuário.

- [ ] \[Off Digital\] Excluir Tudo: Implementar recurso para exclusão completa do item em teste.

- [ ] \[Off Digital\] Comentar Alterações: Comentar alterações no código para visualização de Marcelo Costa.

- [ ] \[Marcelo Costa\] Teste Matriz: Incluir nova matriz usando documentos conhecidos e testar o caminho completo do fluxo. Anotar observações durante o teste.

- [ ] \[Marcelo Costa\] Revisar Ralf: Olhar detalhes sobre o projeto Ralf em paralelo.

- [ ] \[O grupo\] Conversar Ralf: Cruzarem ideias e falarem sobre o projeto Ralf à noite.

### Detalhes

* **Discussão Preliminar e Preocupações Técnicas**: Off Digital iniciou a reunião com uma breve discussão sobre como testar ângulos de gravação usando o Zoom ([00:00:00](#00:00:00)). O foco da conversa mudou rapidamente para problemas técnicos relacionados ao uso de serviços de desenvolvimento, onde Off Digital relatou que uma sessão aberta no Codex, usando Playwright, consumiu 70% de seu plano semanal em 5 horas, apesar de não terem usado nada ([00:10:33](#00:10:33)). Também foi relatado que um limite estourado no Cloud Design resultou no consumo de 700 unidades de crédito extra ([00:13:40](#00:13:40)).

* **Atualização sobre Mordida de Cão**: Marcelo Costa e Off Digital discutiram um incidente envolvendo uma mordida de cão que Off Digital sofreu ao tentar proteger o cão de morder um graveto ([00:08:00](#00:08:00)). Off Digital relatou que o ferimento só arranhou, mas está passando por tratamento diário no posto de saúde para troca de curativo e uso de antibióticos, pois mordidas de cão frequentemente infeccionam e não podem ser suturadas. Off Digital espera que a ferida cicatrize em cerca de 7 dias ([00:09:40](#00:09:40)).

* **Melhorias e Ajustes na Ferramenta de Revisão (Certify)**: Off Digital compartilhou a conclusão de que é mais eficaz resolver problemas de programação um a um, em vez de tentar lidar com vários itens simultaneamente ([00:14:57](#00:14:57)). Foram apresentadas atualizações na ferramenta de revisão de documentos (Certify), incluindo a implementação de filtros por candidato e matriz ([00:16:04](#00:16:04)). Também foi confirmado que as funções de "Aprovar," "Rejeitar," e "Parcial" já estão funcionando no backend ([00:17:29](#00:17:29)).

* **Sincronização do Status de Documentos na Revisão**: Foi discutida a necessidade de melhor sincronização e feedback no sistema de revisão de documentos. Ao rejeitar um documento, ele deve ir para a lista de "Revisados como rejeitado" e o candidato deve ver o documento como "parcial rejeitado," esperando correção ou um novo envio ([00:18:47](#00:18:47)). Foi identificado que, após a rejeição, o documento deveria retornar à lista de pendentes do candidato para um novo envio, enquanto o documento incorreto deveria ir para excedentes ([00:20:01](#00:20:01)) ([00:24:09](#00:24:09)).

* **Personalização de Notificações e Otimização do Desenvolvimento**: Off Digital e Marcelo Costa concordaram que o sistema de registros e notificações precisa ser mais detalhado, exibindo a mensagem do que aconteceu, quem rejeitou, e o motivo ([00:20:01](#00:20:01)). Off Digital também observou que trabalhar em ambiente de produção gerou confusão devido à necessidade constante de \*deploy\*, concluindo que o ideal é desenvolver em ambiente local antes de realizar o \*deploy\* para a URL pública ([00:24:09](#00:24:09)).

* **Verificação da Funcionalidade de Filtro de Carga Horária**: Foi realizado um teste na funcionalidade de busca por carga horária ([00:28:53](#00:28:53)). Off Digital notou que, ao buscar por "12 horas," o filtro exibia documentos que continham essa informação, mesmo que não estivesse no título, como o opito 4650 ([00:30:20](#00:30:20)). Marcelo Costa confirmou, consultando a base de dados, que o documento opito 4650 realmente tinha uma carga horária de 12 horas, indicando que o filtro está funcionando corretamente ao puxar informações da base ([00:31:32](#00:31:32)).

* **Processo de Cadastro de Documentos e Regras Canônicas**: Off Digital demonstrou a nova interface de cadastro de documentos no catálogo ([00:31:32](#00:31:32)). Ao cadastrar um novo documento, é necessário que o usuário selecione a "regra canônica" correta antes de prosseguir, uma medida implementada para garantir a conformidade dos documentos enviados ([00:32:30](#00:32:30)).

* **Oportunidades de Negócios e Marketing de Influência**: Marcelo Costa informou que fechou um contrato de um mês com uma marca de arroz, Rampinelli, por nove mil, embora considere que o período de um mês seja insuficiente para medir o impacto da campanha ([00:42:17](#00:42:17)). Off Digital e Marcelo Costa discutiram a importância de construir relacionamentos mais longos e considerar pacotes de colaboração com múltiplas influenciadoras, como um combo com a Letícia e a Emily ([00:44:26](#00:44:26)). A estratégia de marketing deve focar em integrar o produto na vida da influenciadora, e não apenas em propagandas cruas ([00:43:24](#00:43:24)).

* **Estratégia de Crescimento e Autoridade em Mídias Sociais**: Foi destacado o crescimento da influenciadora Emily, que está próxima de 41 mil seguidores ([00:49:45](#00:49:45)). A discussão focou na necessidade de investir no YouTube para construir autoridade, mencionando que figuras proeminentes no Instagram, como Julima, constroem sua autoridade real através de conteúdo mais profundo no YouTube e da participação em podcasts com outras figuras importantes ([00:51:46](#00:51:46)). Eles concluíram que a verdadeira conexão com o público vem da intimidade, onde a influenciadora compartilha aspectos de sua vida diária ([00:55:59](#00:55:59)).

* **Análise de Conteúdo de Sucesso e Próximos Passos**: Foi analisado o sucesso de um vídeo da Emily sobre o pão pita, que viralizou e possui alta audiência. Eles concluíram que o sucesso se deve ao estilo do vídeo, incluindo \*takes\* visuais atrativos, como o pão inflando, e o uso de áudio de narração. Marcelo Costa sugeriu que a Letícia recrie esse vídeo exatamente com os mesmos \*takes\* para analisar os fatores de sucesso e replicar o modelo ([00:57:09](#00:57:09)).

* **Análise de Conteúdo e Engajamento da Emily Zaremba**: Marcelo Costa e Off Digital discutiram o Instagram de Emily Zaremba, notando a simplicidade e a falta de legendas em um vídeo que utilizava apenas áudio. Off Digital mencionou que o perfil é promissor, apesar de ainda haver espaço para melhorias que eles ajudam a orientar. Eles destacaram o potencial para Emily Zaremba ganhar um alto valor mensal com marcas ([00:59:03](#00:59:03)).

* **Conteúdo Viral e Engajamento de Haters**: O tópico mudou para a natureza imprevisível do conteúdo viral, notando que um vídeo de sucesso de Emily Zaremba não tinha relação com o momento atual ([01:01:22](#01:01:22)). Off Digital compartilhou que os vídeos de sucesso dela geraram engajamento significativo por meio de haters e comentários de defesa, o que o Instagram usa para aumentar a entrega. Eles observaram que esse engajamento alimenta a loucura e ajuda o conteúdo a "bombar" ([01:02:12](#01:02:12)).

* **Estratégias de Crescimento de Alcance (Reel Test)**: Off Digital mencionou o uso do recurso "Reel Test" para crescimento de seguidores, que entrega o conteúdo para usuários fora da base de seguidores. Eles citaram um caso de 3 milhões de seguidores ganhos através dessa estratégia. Marcelo Costa introduziu uma ferramenta da Meta para analisar o engajamento de vídeos, usando ressonância magnética para identificar momentos em que os usuários desestimulam e saem, prometendo enviar o repositório para Off Digital analisar ([01:03:23](#01:03:23)).

* **Otimização da Interface de Usuário e Agenda de Reuniões**: Houve uma breve discussão sobre a interferência de uma notificação ou elemento do sistema Insperflow na tela, que Off Digital considerou que deveria ser movido para a barra superior para ser menos intrusivo ([01:04:31](#01:04:31)). Eles confirmaram uma reunião agendada para o dia seguinte às 11h ([01:06:06](#01:06:06)).

* **Proposta de Camada de Inteligência Artificial para Cliente**: Marcelo Costa sugeriu implementar uma camada de IA que analise os dados de logística e processos do cliente, como o exemplo de dados de obras e produtividade em períodos de chuva, para fornecer \*insights\* ([01:06:06](#01:06:06)). Off Digital solicitou o transcrito da chamada anterior para analisar e sugeriu que a IA se concentre em cruzamento de dados para gerar \*insights\* e diagnósticos que o cliente não consegue obter manualmente. Eles notaram que o cliente não possui nenhuma camada de IA atualmente ([01:08:55](#01:08:55)).

* **Implementação de Agentes de IA para Automação de Relatórios**: Off Digital propôs focar a solução em uma camada de IA após a geração de relatórios, criando diagnósticos e \*insights\* sobre como melhorar esses relatórios e distribuindo-os de forma automatizada ([01:10:25](#01:10:25)). Eles sugeriram vender a comodidade de receber relatórios e informações relevantes (como a comunicação interna) via Telegram ou WhatsApp ([01:11:39](#01:11:39)). O objetivo seria atuar como uma camada de agente que opera o sistema do cliente, eliminando a necessidade de cliques manuais ([01:12:50](#01:12:50)).

* **Agregação de Valor e Escopo do Projeto**: Marcelo Costa concordou que o foco deve ser em agregar valor com uma camada superior em vez de modificar o sistema principal do cliente. Off Digital reforçou que a ideia é construir uma peça para plugá-la no sistema, sendo uma malha de análise e distribuição com IA ([01:14:04](#01:14:04)). Eles ressaltaram que a informação precisa ser embalada de forma diferente para cada público (gerentes, clientes, donos), otimizando a entrega ([01:15:15](#01:15:15)).

* **Análise de Produtividade Interna com IA**: A discussão se aprofundou na análise do uso do sistema pela equipe interna, usando a Lidiane como exemplo, para medir o tempo gasto em atividades específicas e identificar áreas de melhoria na produtividade ([01:16:30](#01:16:30)). Marcelo Costa destacou que essa otimização poderia revelar problemas como cobrança inadequada ou gasto excessivo em desenvolvimento ([01:17:34](#01:17:34)). Off Digital enfatizou que o valor da automação é enorme, independentemente de quem faz ou como faz o trabalho hoje ([01:14:04](#01:14:04)).

* **Prioridade de Relatórios e Estratégia de Vendas**: Off Digital lembrou que o cliente expressou maior interesse em um relatório específico que é muito manual e requer IA, o que deve ser o foco inicial ([01:18:27](#01:18:27)). Eles concordaram que o objetivo é mostrar que eles podem automatizar tudo o que precisa ser automatizado na empresa do cliente, dando exemplos do valor dessa automação ([01:19:29](#01:19:29)).

* **Desenvolvimento e Ajustes em Andamento**: Marcelo Costa enviou a Off Digital os áudios da reunião anterior para análise e Off Digital detalhou três ajustes que estão sendo feitos no sistema atual (barra de rolagem, lógica de aprovação/rejeição e tratamento de pendentes). Eles concordaram em limitar os ajustes a três por vez ([01:20:39](#01:20:39)).

* **Exemplo de Aplicação de IA em Sistemas de Transporte**: Marcelo Costa compartilhou exemplos de como uma empresa de transporte na Noruega usa a IA, incluindo processamento de pedidos, otimização de rotas e detecção de atrasos em tempo real. Eles observaram que essa abordagem de IA complementa a tomada de decisão humana, destacando \*insights\* e exigindo aprovação para ações finais ([01:25:54](#01:25:54)).

* **Estratégia de Implementação e Considerações Financeiras**: Off Digital sugeriu fragmentar o projeto de IA em fases, com um crescimento mês a mês, para que o cliente sinta o valor gradualmente ([01:34:37](#01:34:37)). Eles discutiram se o produto seria uma consultoria, um produto próprio entregue ao cliente ou uma implementação personalizada, observando que esta última seria mais cara devido à exclusividade ([01:35:56](#01:35:56)).

* **Segurança de Dados e LLMs Internas**: A questão da segurança dos dados e o uso de Large Language Models (LLMs) internos foi levantada por Marcelo Costa, que notou que o cliente se preocupou com o NDA ([01:36:59](#01:36:59)). Off Digital considerou que a questão da LLM interna é muito aprofundada para o momento ([01:38:25](#01:38:25)). Eles concordaram que a preocupação com a segurança deve ser abordada mostrando que eles oferecem níveis de \*compliance\* e segurança escaláveis com o orçamento do cliente ([01:39:50](#01:39:50)).

* **Progresso e Reflexões sobre o Envolvimento em Projetos Corporativos**: Marcelo Costa descreveu a eficiência de seu setup pessoal de IA em tarefas como redação de e-mails, acessando o Google Drive e e-mails. Off Digital observou que estão investindo pouco tempo nesse desenvolvimento, devido a estarem focados em outros projetos, mas acumulando material ([01:42:07](#01:42:07)). Marcelo Costa expressou dúvidas sobre o envolvimento em projetos corporativos de grande escala devido à pressão e ao potencial de retorno financeiro em projetos pessoais ([01:43:02](#01:43:02)).

* **Revisão e Teste de Funcionalidades do Sistema**: Off Digital e Marcelo Costa revisaram o \*deploy\* e as funcionalidades, confirmando a barra de rolagem funcionando ([01:46:06](#01:46:06)) ([01:50:39](#01:50:39)). Eles testaram o processo de aprovação de documentos no sistema de certificação, notando problemas com a duplicação de documentos bloqueados e a necessidade de limpar os dados de teste ([01:47:44](#01:47:44)) ([01:50:39](#01:50:39)). Eles observaram que o sistema de \*Kanban\* e a filtragem de vagas estão funcionando, embora com pequenos erros de nomenclatura nos termos ([01:55:19](#01:55:19)).

* **Uso e Entendimento do Processo Manual**: Marcelo Costa sugere permitir o uso manual para que as pessoas compreendam o processo. Eles estão trabalhando em zerar os dados no \*cloud\* e observam que a alteração para atualizar o detalhe na mudança de revisão ainda não foi carregada. Off Digital está deixando a equipe trabalhar enquanto eles revisam o assunto com Ralf ([01:57:59](#01:57:59)).

* **Relatório de Acompanhamento da Obra (RDO)**: Off Digital explica que o RDO é um padrão de mercado consolidado para o setor de construção, abrangendo informações como número de pessoas por cargo, equipamentos presentes, clima, ocorrências, acidentes de trabalho, faltas e tempo médio de trabalho ([01:57:59](#01:57:59)). Lidiane reforçou que o padrão do RDO é muito similar entre os clientes, indicando uma forte dor no setor, embora a coleta de dados de presença e equipamentos na obra não seja feita em tempo real. Marcelo Costa sugere que o registro poderia ser feito com um cartão de ponto ou um RFID ([02:03:21](#02:03:21)).

* **Expectativas de Conversa com Ralf**: Marcelo Costa acredita que a conversa com Ralf pode ser mais franca e detalhada sobre os desafios operacionais, pois ele tem um profundo conhecimento da construção. Off Digital questiona se Ralf estaria tão a par do operacional, mas Marcelo Costa afirma que ele tem uma grande experiência, tendo construído a operação desde o início ([02:04:31](#02:04:31)).

* **Funcionalidade de Exclusão e Testes**: Eles discutem a funcionalidade de exclusão de documentos e matrizes, com Marcelo Costa apontando que seria útil poder excluir um documento. Eles confirmam que o candidato já pode ser excluído ([02:04:31](#02:04:31)). Off Digital precisa que o recurso de exclusão de usuário também seja implementado e sugere que Marcelo Costa inclua uma matriz e faça um teste completo do fluxo, anotando os pontos observados ([02:06:33](#02:06:33)).

* **Problemas com o Cloud e Planos Futuros**: Off Digital menciona que o \*cloud\* tem apresentado erros de API diariamente, o que tem desanimado o seu uso. Eles observam que a parceria do Cloud com Elon Musk pode ter sido para compensar essas falhas. Devido aos problemas, eles têm dependido muito do \*Codex\* ([02:10:46](#02:10:46)). Ambos concordam em focar no trabalho pendente e discutir as questões com Ralf à noite, com o objetivo de ter um caminho de conversa e coletar mais informações antes de preparar a reunião ([02:08:46](#02:08:46)).

*Revise as anotações do Gemini para checar se estão corretas. [Confira dicas e saiba como o Gemini faz anotações](https://support.google.com/meet/answer/14754931)*

*Como está a qualidade de **destas observações?** [Responda a uma breve pesquisa](https://google.qualtrics.com/jfe/form/SV_9vK3UZEaIQKKE7A?confid=gzQ8UzOewlxpxPhu-iVrDxITOAIIigIgABgFCA&detailid=standard&screenshot=false) para nos dar seu feedback, incluindo o quanto as observações foram úteis para o que você precisa.*

# 📖 Transcrição

7 de mai. de 2026

## Reunião em 7 de mai. de 2026 às 11:01 GMT-03:00 \- Transcrição

### 00:00:00 {#00:00:00}

   
**Off Digital:** e ele vai dar o endereço ela conseguindo ele volta Tudo bem. seu story? Ah, tô tentando pensar para escrever, sair porque eu queria pensar para escrever e o homem vem atrás. falando que nem um papagaio. mesmo aqui para fazer fazer umas massas de bolo ali para deixar pronto. Você podia testar os ângulos, né, da gravação. Instala o Zoom no teu computador, leva o teu computador, instala o Zoom, o aplicativo do Zoom, daí abre. Eu prefiro que a gente faça isso junto depois, entendendo as coisas que eu posso fazer cozinha, que eu tenho que fazer outro mesm conversa com o pessoal diferença por dois. E aí eu senti a necessidade. Ela falou que se a Ia conseguisse fazer isso, ela ela falou: "Não fala pro Marcos Consegui fazer o que eu gastei 4 anos estudando. Eu quero comprar esse negócio da EA aí porque olha aqui. Primeiro você tem que me responder da outra proposta. Primeiro vou entrar aqui no na reunião. Você me mostra. Pelo amor de Deus. Não sei o que fazer. Preciso entrar. Mãe. Não sei o que fazer. Alê,  
**Marcelo Costa:** Pera aí,  
**Off Digital:** priminho.  
   
 

### 00:08:00 {#00:08:00}

   
**Marcelo Costa:** priminho.  
**Off Digital:** Beleza,  
**Marcelo Costa:** Bom, pera um segundo só. É só responder.  
**Off Digital:** velho.  
**Marcelo Costa:** Pera aí. Дали priminho, e aí meteu uns pontos aí, primo,  
**Off Digital:** Priminho, não, não deu. Não pode dar ponto, velho. Acredita?  
**Marcelo Costa:** por conta de infecção?  
**Off Digital:** Uhum.  
**Marcelo Costa:** p\*\*\* que m\*\*\*\*,  
**Off Digital:** Não pode dar ponto,  
**Marcelo Costa:** hein,  
**Off Digital:** velho. O cara me entupiu de antibiótico aqui.  
**Marcelo Costa:** p\*\*\*\*, velho. Mas deu uma abrida legal, né, velho? c\*\*\*\*\*\*, mano. p\*\*\* que pariu, velho. Foi pegou o dentão de trás assim na  
**Off Digital:** Deu agonia para mim quando você viu. Não, velho. Foi o o esse aqui mesmo que é o mais comprido.  
**Marcelo Costa:** lateral.  
**Off Digital:** Só que assim, ele não ele não me bocanhou, ele só raspou o dente assim, como se fosse uma colher, sabe?  
**Marcelo Costa:** Sim, puxou.  
**Off Digital:** que ele foi, ele foi seco no graveto, eu tirei o graveto e pegou meu braço,  
**Marcelo Costa:** Hum,  
**Off Digital:** entendeu?  
**Marcelo Costa:** entendi. Ele passou voando assim  
   
 

### 00:09:40 {#00:09:40}

   
**Off Digital:** É, ele passou voando porque eu vi que a madeira tava cheia de farpa e ele ia machucar.  
**Marcelo Costa:** para  
**Off Digital:** Aí eu tirei o graveto para ele não morder o graveto. Aí ele já tava no ar, ele foi no passou. É,  
**Marcelo Costa:** bateu no braço.  
**Off Digital:** aí só arranhou, mano. Aí na hora já  
**Marcelo Costa:** Nossa, f\*\*\*. Imagina se o bicho pegar para destruir mesmo,  
**Off Digital:** não esquece,  
**Marcelo Costa:** né,  
**Off Digital:** esquece, esquece. É doideira total.  
**Marcelo Costa:** velho?  
**Off Digital:** Aí, cara, aí é isso aí, bicho. Só fez um curativo. Eu tô tendo que todo dia no posto trocar o curativo para avaliar, né? Porque essa p\*\*\*\*  
**Marcelo Costa:** Meter um passando uns produtinh aí.  
**Off Digital:** é que essa p\*\*\*\* infecciona, né, velho? Falou, cara, né?  
**Marcelo Costa:** É por causa  
**Off Digital:** sempre infecciona a mordida de cão assim, por isso que não pode dar ponto. E aí tomando antibiótico e tal,  
**Marcelo Costa:** p\*\*\*,  
**Off Digital:** mas uns s dias eu acho que já tá bom. Ele falou que vai com s dias já fecha já.  
**Marcelo Costa:** c\*\*\*\*\*\*. O bicho ficou meio na não é ficou.  
   
 

### 00:10:33 {#00:10:33}

   
**Off Digital:** É,  
**Marcelo Costa:** Ele viu que ele fez a m\*\*\*\*  
**Off Digital:** é, ele viu,  
**Marcelo Costa:** depois.  
**Off Digital:** ele ficou coitado, ficou cabis baixo.  
**Marcelo Costa:** É, mas pô,  
**Off Digital:** Falei:  
**Marcelo Costa:** acontece brincadeira,  
**Off Digital:** "É safado,  
**Marcelo Costa:** né, velho? Brincadeira de homem,  
**Off Digital:** o negócio é bruto, né, para mim. Ô, velho,  
**Marcelo Costa:** né?  
**Off Digital:** eu tava resolvendo aqui um tava não, tô resolvendo um bo aqui, velho. Você acredita? ficou uma sessão aberta minha do Codex, velho. O bagulho comeu meu meu plano inteiro, 70% da minha semana, velho.  
**Marcelo Costa:** Mas ele tava usando o quê?  
**Off Digital:** Cara, ele falou que tinha uma sessão super pesada usando um negócio de playw, que é quando ele usa para para ver no Braga,  
**Marcelo Costa:** para acessar  
**Off Digital:** mano. Comeu meu minha semana inteira,  
**Marcelo Costa:** o  
**Off Digital:** velho. E eu tava vendo aqui. Aí eu aí eu acordei hoje, fui ver sessão 57% usada da sessão da de de 5 horas. Eu não tinha usado  
**Marcelo Costa:** por que ele tá mesmo que ele esteja com o playbite aberto,  
**Off Digital:** nada.  
**Marcelo Costa:** por que que ele tá fuçando, velho?  
**Off Digital:** Não, eu não entendi também,  
   
 

### 00:11:39

   
**Marcelo Costa:** sozinha.  
**Off Digital:** velho. Eu sei que ele, eu aí eu abri um outro Codex aqui e falei: "Meu irmão, descobre aí que que essa p\*\*\*\* tá me drenando". Aí ele falou: "É isso, tem uma sessão eh no que tá no Playride, que tá aberto há não sei quanto tempo, dois dias, e tá sugando o  
**Marcelo Costa:** É, eu vejo às vezes aqui que eu tô,  
**Off Digital:** rolê.  
**Marcelo Costa:** por exemplo, se eu fico numa conversa muito longa, aí o contexto é muito longo, toda hora ele lê o contexto, né? Talvez ele tá lendo esse contexto para fazer outras coisas,  
**Off Digital:** Não, cara, não,  
**Marcelo Costa:** né?  
**Off Digital:** não. Ele,  
**Marcelo Costa:** Ele tá rodando mesmo alguma alguma coisa que você mandou rodar e  
**Off Digital:** eu deixei o eu deixei os navegador com playrght aberto e aí eu acho que ele tá contando,  
**Marcelo Costa:** ficou  
**Off Digital:** tipo, como se ele tivesse passando pelo navegador desde desde lá então que ele estivesse fazendo esse job, entendeu? Deixa eu atender aqui um segundo rapidão.  
**Marcelo Costa:** sim. M.  
**Off Digital:** Eh, então, pois é, priminho. Aí eu até fui lá no Open Cloud, mandei cortar todos os Chrom, falei: "Velho, deve ser Open Cloud".  
   
 

### 00:13:40 {#00:13:40}

   
**Off Digital:** Aí, aí agora eu vim com ele aqui, ele falou: "Já cortei aqui as sessões antigas, tinha 28 conversas ativas.  
**Marcelo Costa:** No  
**Off Digital:** Enfim, velho,  
**Marcelo Costa:** pentron  
**Off Digital:** acabou com a minha com a minha parada aqui da semana. Agora vai resetar em 5 dias. Eu já usei 70% do Codex.  
**Marcelo Costa:** bichinho tá na  
**Off Digital:** Bichinho tá na Mas beleza,  
**Marcelo Costa:** colau.  
**Off Digital:** mas vamos que vamos, cara. E o bagulho do cloud também comeu meus créditos aqui para mim. De um jeito eu tava aquele cloud design deu deu  
**Marcelo Costa:** aqueles créditos a mais para você aí.  
**Off Digital:** 10000 de crédito, mas um dia ele comeu 700 pila de crédito.  
**Marcelo Costa:** Mas você precisa precisa fazer alguma coisa para pegar os créditos. Ele  
**Off Digital:** Não, quando você tá sem limite ele usa. Só que velho,  
**Marcelo Costa:** já  
**Off Digital:** eu estouri o limite do cloud design e eu deixei rolando lá. Fui dormir e deixei rolando. Aí ele estourou o limite e ficou com menos crédito, velho.  
**Marcelo Costa:** f\*\*\*, né, velho?  
**Off Digital:** Comeu 700 de crédito do de um de um dia paraa noite no  
**Marcelo Costa:** no design.  
   
 

### 00:14:57 {#00:14:57}

   
**Off Digital:** cl.  
**Marcelo Costa:** Ah, mas você deixou fazendo o que lá?  
**Off Digital:** Eu deixei fazendo umas telas lá  
**Marcelo Costa:** Uma apresentação, alguma coisa?  
**Off Digital:** do do aplicativo, porque assim, eu tava com 0% usado, ia resetar no outro dia.  
**Marcelo Costa:** Fala,  
**Off Digital:** Aí eu falei:  
**Marcelo Costa:** vou usar essa bosta,  
**Off Digital:** "Vou usar".  
**Marcelo Costa:** né?  
**Off Digital:** Só que aí, velho, ele acabou os créditos antes de resetar e ficou usando do meu extra. E acabou com o meu extra, mano. Quase de 100 que eu tinha, comeu 700 pila. Imagina, mano, se é no cartão,  
**Marcelo Costa:** p\*\*\*\*,  
**Off Digital:** se não fosse crédito extra,  
**Marcelo Costa:** é não. O cara fala, o cara vocês dá dão,  
**Off Digital:** tem que ficar muito,  
**Marcelo Costa:** mas o cara já arruma um jeito de pegar,  
**Off Digital:** é,  
**Marcelo Costa:** né?  
**Off Digital:** velho, tem que ficar muito ligado com essas com esse com esse rolê, viu, priminho? Mas bom, mas beleza. Aí, como é que nós estamos aqui, cara? É aquele dia, velho, eu botei para rodar várias paradas, mas eu vou te falar, velho, é f\*\*\*, porque começou a dar vários conflitos. É melhor fazer de um por um mesmo.  
   
 

### 00:16:04 {#00:16:04}

   
**Off Digital:** Eu vou, tô chegando cada vez mais essa conclusão, mano.  
**Marcelo Costa:** quando entra no detalhe, né?  
**Off Digital:** É,  
**Marcelo Costa:** você diz,  
**Off Digital:** velho, você tem que fazer  
**Marcelo Costa:** eh, eu eu é o que eu prefiro sempre fazer também quando eu vou fazendo as coisas aqui,  
**Off Digital:** porque  
**Marcelo Costa:** tipo assim, você faz um promptizão, um negocão gigante que ele vai, p\*\*\*\*, consolida. Depois os detalhinho, você vai indo um a um, matando, ele não resolve vários juntos detalhinho, né?  
**Off Digital:** aqui na revisão Eu já já ajustamos aqui, ó. Você vê que tá diferente já aqui, né? Aqui, ó. A gente já tem o filtro agora pro candidato. Tá vendo aí? Tá dando para ver aí?  
**Marcelo Costa:** Aham.  
**Off Digital:** A gente já tem o filtro agora pro candidato,  
**Marcelo Costa:** Sim.  
**Off Digital:** ó. Se bota aqui o Alfredini, vai ficar só Alfredini, entendeu?  
**Marcelo Costa:** Ah.  
**Off Digital:** aqui por matriz e aqui por os tipos de certificado ou opito vai ter os tipos aqui. Eh, e só que eu vou mudar esse layout aqui. O layout ele não ficou legal não, mas tá, o back end tá funcionando já eh, do filtro, né?  
**Marcelo Costa:** Tá.  
**Off Digital:** Aí você vê que aqui, ó, aqui ele já tá correspondendo aqui do outro lado.  
   
 

### 00:17:29 {#00:17:29}

   
**Off Digital:** Lembra que a gente tava resolvendo isso aqui,  
**Marcelo Costa:** Uhum.  
**Off Digital:** ó? N34 já tá aqui. Nr34.  
**Marcelo Costa:** Não confere mobilidade LR. Pá, tá  
**Off Digital:** Aí aqui, por exemplo,  
**Marcelo Costa:** beleza.  
**Off Digital:** se eu mudo para para esse documento aqui, ó, aí ele mudou aqui para um curso de manuseio de produtos perigosos da West Group. Botou aqui já em primeiro,  
**Marcelo Costa:** Tá  
**Off Digital:** entendeu? Ó, quando eu clico aqui,  
**Marcelo Costa:** perfeito.  
**Off Digital:** Ci,  
**Marcelo Costa:** Tá.  
**Off Digital:** entendeu?  
**Marcelo Costa:** Boa.  
**Off Digital:** Então, eu acho que é isso, né?  
**Marcelo Costa:** É, aí não, aí tá perfeito. Acho que é isso aí pro cara ir aprovando aí e ter essa visibilidade.  
**Off Digital:** Aí aqui eu já eu já liguei esses botões, então aprovar, rejeitar e parcial já tá funcionando.  
**Marcelo Costa:** Eh,  
**Off Digital:** Ó, se eu der eh ó, aqui ele já aparece revisão parcial registrada. Necessário ajuste antes da aprovação final. Eu posso registrar aqui parcial, ele já vai pro revisado como parcial.  
**Marcelo Costa:** mantém ainda imparcial.  
**Off Digital:** Ant parcial porque já tava parcial, entendeu?  
**Marcelo Costa:** Tá.  
**Off Digital:** Mas se eu aprovar,  
   
 

### 00:18:47 {#00:18:47}

   
**Marcelo Costa:** Agora se eu quiser se  
**Off Digital:** é, aprovei, ele já aprovou, ó. Já foi aqui, ó. Documento aprovado.  
**Marcelo Costa:** aprovar,  
**Off Digital:** Ele já foi aqui como aprovado, entendeu? Aí depois eu vou botar aqui, ó, aprovado pro revisor  
**Marcelo Costa:** tá? Beleza.  
**Off Digital:** e rejeitar também. Mesmo esquema.  
**Marcelo Costa:** Quando eu rejeito, é o que acontece?  
**Off Digital:** Quando rejeita, ele vai ficar aqui nos revisados como rejeitado.  
**Marcelo Costa:** E lá no cara,  
**Off Digital:** lá no cara, ele vai continuar como como parcial rejeitado.  
**Marcelo Costa:** tá? Porque aí, por exemplo, vamos pensar, o cara mandou uma NR e tal e eu rejeitei, tava errada. Aí ele vai mandar uma outra agora que ele fez a correta. Mandou a correta.  
**Off Digital:** Correta. É,  
**Marcelo Costa:** Aí ele tem que sair da posição,  
**Off Digital:** ó,  
**Marcelo Costa:** né,  
**Off Digital:** ó.  
**Marcelo Costa:** que ele  
**Off Digital:** Eh, documento rejeitado em revisão manual. Solicitar correção ou não.  
**Marcelo Costa:** tava  
**Off Digital:** Rejeitar aí. Beleza. Qual que foi que rejeitou aqui? Rejeitado por revisor. Documento rejeitado em revisão manual. Solicitar correção ou novo envio.  
   
 

### 00:20:01 {#00:20:01}

   
**Marcelo Costa:** ver o reflexo lá no cara, né?  
**Off Digital:** Qual que era o documento? Deixa eu ver aqui. O da oeste é o que manuseio.  
**Marcelo Costa:** curso manuseio produtos perigosos.  
**Off Digital:** É.  
**Marcelo Costa:** É, aí ele não vai tá porque aí não tem documento, certo? Ele ou tá no no nos parciais, deveria tá aí,  
**Off Digital:** Mas o certo era ele ir paraa pendente,  
**Marcelo Costa:** ó.  
**Off Digital:** porque o cara tem que enviar de novo,  
**Marcelo Costa:** Se eu recusei, né? Recusei.  
**Off Digital:** né?  
**Marcelo Costa:** Esse documento não vale. Ele deveria ir lá para baixo dos documentos. Não, não.  
**Off Digital:** Qual que era mesmo, primo? É curso  
**Marcelo Costa:** Curso de manuseio. Produto perigoso.  
**Off Digital:** de  
**Marcelo Costa:** Agora é que eu acho que, p\*\*\*\*, ele tá trazendo esse cara da antiga, velho. Para mim, eu fazia o seguinte, velho. zerava tudo e começava a subir um cara novo, documento novo, matriz nova, subi de um em um documento e vamos ver o que que que ele que acontece no operacional,  
**Off Digital:** Não, isso aí nós vamos fazer,  
**Marcelo Costa:** entendeu?  
**Off Digital:** mas eh eu quero afinar essas funcionalidades paraa gente ver o negócio já já funcional, porque senão, ó, aqui, por exemplo, tá nesses registros, tá aparecendo aqui, aí ele aparece qual documento já, mas essa notificação aqui não tá personalizada, então é coisa que você só vê quando você começa a apertar os botãos.  
   
 

### 00:21:56

   
**Off Digital:** né?  
**Marcelo Costa:** É isso aí.  
**Off Digital:** Então, por exemplo,  
**Marcelo Costa:** Ele registra,  
**Off Digital:** aqui,  
**Marcelo Costa:** mas ele não fala o que é para você saber o que aconteceu,  
**Off Digital:** eh, aqui tem que ter a mensagem,  
**Marcelo Costa:** né?  
**Off Digital:** ó, fulano de tal eh eh rejeitou tal horas, entendeu?  
**Marcelo Costa:** Fulana exertou tal hora e se ele botou o motivo lá ainda aparece o motivo  
**Off Digital:** Então isso aqui, exatamente.  
**Marcelo Costa:** aí.  
**Off Digital:** Eh, ó, por exemplo, NR34 aqui,  
**Marcelo Costa:** Vem, põe em revisão ali. Você não mexeu nisso ainda, né?  
**Off Digital:** não. NR34. Cadê? É essa aqui, né? Da Helion. Esse aqui, NR34 quente,  
**Marcelo Costa:** Não,  
**Off Digital:** é NR34 quente,  
**Marcelo Costa:** é isso aí.  
**Off Digital:** aprovado. Então essa aqui ela teria que trabalho a quente.  
**Marcelo Costa:** Ela  
**Off Digital:** Ela teria que tá em confere.  
**Marcelo Costa:** teria que ter passado para ir, né?  
**Off Digital:** Mas é,  
**Marcelo Costa:** Põe e quando você aperta revisar,  
**Off Digital:** mas é porque isso não, isso não tá feito, entendeu?  
**Marcelo Costa:** ele não tá sincronizando, né?  
**Off Digital:** Ah, então vamos ter que  
**Marcelo Costa:** Ó, veja que o que eu tô falando, o que nós estamos fazendo agora de trocar de tela,  
   
 

### 00:23:11

   
**Off Digital:** vamos  
**Marcelo Costa:** ir lá, voltar para cá para ver, isso é o dia a dia do cara. Por isso, por isso que eu falo, eu, eu, por isso que eu acho que a gente teria que ter essa aprovação,  
**Off Digital:** exatamente,  
**Marcelo Costa:** ela vai tá aqui, né? Mas pro cara trabalhar dentro do cara aprovando as coisas dele, entendeu? Não ter que sair lá na outra a baixar o cara, filtrar pro cara, voltar nele. Opa, pera aí, deixa eu ver, né?  
**Off Digital:** mas isso Isso aí, primo, é um opcional. Ele, se ele quiser ficar nessa tela mais simples, ele fica. Se ele quiser ir pro detalhe, ele vai. Entendeu? Eh,  
**Marcelo Costa:** Tá.  
**Off Digital:** essa é a ideia pelo  
**Marcelo Costa:** É que quando ele quando tiver sincronizado aí,  
**Off Digital:** menos,  
**Marcelo Costa:** beleza, ele não vai ficar indo e voltando porque ele fez num lugar já tá feito,  
**Off Digital:** não. E nós estamos aqui entendendo ainda nós mesmos o sistema,  
**Marcelo Costa:** né?  
**Off Digital:** né? Porque quando você vai na prática mesmo que você Mas assim,  
**Marcelo Costa:** É.  
**Off Digital:** vamos fazer diferente hoje, velho. Vamos, vamos, vamos de um por um, vamos fazendo e vamos arrumando. Em vez de passar vários itens,  
   
 

### 00:24:09 {#00:24:09}

   
**Marcelo Costa:** Sim.  
**Off Digital:** vamos, vamos.  
**Marcelo Costa:** Vai,  
**Off Digital:** É, eu vou ligar aqui.  
**Marcelo Costa:** eu acho que é isso, sincronizar esse bicho aí agora,  
**Off Digital:** É, vamos já vamos fazer aqui o  
**Marcelo Costa:** né?  
**Off Digital:** rolê.  
**Marcelo Costa:** M.  
**Off Digital:** Cara, você acha que ele vai para pendente ou vai para excedente?  
**Marcelo Costa:** Quando eu recuso  
**Off Digital:** Quando eu recuso, ele precisaria ir para pendentes e o documento errado vai para excedentes, entendeu?  
**Marcelo Costa:** aí,  
**Off Digital:** Porque aí o  
**Marcelo Costa:** porque ali não fica documento em pendente, pendente é para subir, né? É isso  
**Off Digital:** É e aí o documento vai para  
**Marcelo Costa:** aí.  
**Off Digital:** excedentes. Ah, e o então confere rejeitado e parcial. Quando quando eu coloco parcial na revisão, tem que explicitar no detalhe do candidato o motivo dele continuar parcial. Além disso, já tínhamos um sistema. Eu não vou misturar as coisas aqui, senão eh, além  
**Marcelo Costa:** Ele meu acesso tá ele já tá no no versão nova aí dessas alterações.  
**Off Digital:** como assim?  
**Marcelo Costa:** O que você alterou já tá aqui refletindo pro meu aqui aquele meu acesso supervisor.  
**Off Digital:** Sim, sim, sim. Já. E isso é um problema também, porque ficar trabalhando, ficar trabalhando tudo em produção é f\*\*\*, porque você tem que comitar, puxar, fazer deploy, ele tem que mandar no Versel para mandar não sei das quantas.  
   
 

### 00:28:53 {#00:28:53}

   
**Off Digital:** É muito melhor trabalhar em local. Eh, isso também deu um p\*\*\* de um de uma confusão aqui, porque toda hora tinha que ficar fazendo deploy. Então, o melhor é fazer tudo em local e depois fazer o deploy, que é o que manda pro pra URL pública.  
**Marcelo Costa:** né? Uma só. Não precisa ficar,  
**Off Digital:** É,  
**Marcelo Costa:** não precisa  
**Off Digital:** velho. E isso isso deu uns bug aqui, mas já tá já que a gente fez agora.  
**Marcelo Costa:** ficar.  
**Off Digital:** Deixa eu ver aqui. Ó, a busca já tá funcionando. horas. As horas, cara, ele não tá.  
**Marcelo Costa:** Ja.  
**Off Digital:** Você pode fazer um teste aí. Quando eu vou na busca na hora de criar o documento lá na de criar a matriz, eu ponho 12 horas, ele me aparece vários documentos filtrados, só que ele não aparece o título que é 12 horas. Então eu acho que ele tá reconhecendo 12 horas dentro do documento, mas não o título, entendeu?  
**Marcelo Costa:** É, mas como título, o cara não vai puxar como título 12 horas, entendeu? Ele vai puxar NR e tal. Aí a NR aparece várias, a 12,  
**Off Digital:** Então, mas vê aí se tá funcional,  
**Marcelo Costa:** a 24\.  
   
 

### 00:30:20 {#00:30:20}

   
**Off Digital:** porque, por exemplo, ele tá me falando aqui que, por exemplo, NR05, grau de risco 2\. Ah, esse aqui tem 12 horas, sim. Mas, por exemplo, quando eu boto 12 horas, ele me aparece aqui, por exemplo, opito 4650 dentro do filtro de 12 horas. Então tem que conferir se esse opito ele é 12 horas mesmo para ver se esse filtro tá correto, entendeu? Porque se tiver, beleza, não tá no título, mas ele tá pegando todos os documentos que estão 12 horas, melhor ainda.  
**Marcelo Costa:** É beleza. Ele puxa, ele tá aqui, tá puxando tudo que é 12, vai todos que tem carga horária,  
**Off Digital:** Exato.  
**Marcelo Costa:** 12, ele tá puxando  
**Off Digital:** É, então só tem que conferir se realmente esse,  
**Marcelo Costa:** aqui,  
**Off Digital:** porque como não tem no título, se realmente esses documentos é 12 horas, entendeu?  
**Marcelo Costa:** mas aí vai tá conferindo com a base dele, com a  
**Off Digital:** Então, a gente tem que ir lá na base,  
**Marcelo Costa:** base.  
**Off Digital:** abrir o documento e ver se o requisito é 12 horas mesmo, entendeu?  
**Marcelo Costa:** Tá? Então vamos ver aqui. Um pá.  
**Off Digital:** Por exemplo, tem esse opito 4650\.  
   
 

### 00:31:32 {#00:31:32}

   
**Marcelo Costa:** É aqui para mim ele nem aparece, nem que eu ponho 4:30, nem 12 horas não aparece o pit aqui para mim é que eu tô,  
**Off Digital:** Mas aonde você tá?  
**Marcelo Costa:** é o que eu tô só na, eu tenho que ir na aba todos, né?  
**Off Digital:** É, eu digitei 12 horas 12 h tudo junto.  
**Marcelo Costa:** Aí 4650,  
**Off Digital:** Aham.  
**Marcelo Costa:** né?  
**Off Digital:** Aí, só que aí você tem que ir na base. Ah, você já tá na  
**Marcelo Costa:** É,  
**Off Digital:** base.  
**Marcelo Costa:** então aí na base a base a base diz aqui, né?  
**Off Digital:** A base tá dizendo que é 12  
**Marcelo Costa:** 12 horas. Sim.  
**Off Digital:** horas.  
**Marcelo Costa:** Lá naquele lá naquele negócio que é o a ficha cadastral do produto,  
**Off Digital:** Sim, sim.  
**Marcelo Costa:** né?  
**Off Digital:** Porque eu tô na matriz. Deixa eu abrir na base agora também aqui para ver.  
**Marcelo Costa:** Não, a base tá mostrando 12 horas. Perfeito.  
**Off Digital:** Ah, então tá. Então, ótimo.  
**Marcelo Costa:** Tá puxando da  
**Off Digital:** Então, perfeito. Então,  
**Marcelo Costa:** base.  
**Off Digital:** é isso. Ah, agora no catálogo, se liga, põe aí cadastrar documento para você ver como é que tá agora o  
   
 

### 00:32:30 {#00:32:30}

   
**Marcelo Costa:** Catálogo tá zerado,  
**Off Digital:** cadastro.  
**Marcelo Costa:** né?  
**Off Digital:** É, põe aí o catálogo tá zerado. Põe cadastrar documento para você ver agora.  
**Marcelo Costa:** Certo? Nome do  
**Off Digital:** Aí você clica ali, ó, regra canônica. Clica ali para você ver.  
**Marcelo Costa:** documento. Onde tá a regra canônica?  
**Off Digital:** embaixo do nome do  
**Marcelo Costa:** Ah, beleza.  
**Off Digital:** documento.  
**Marcelo Costa:** Esse aqui, p\*\*\*\*, ele puxa. Puxa o quê? Todas as regras.  
**Off Digital:** Exato. Então, meu irmão, para você criar o documento, você tem que botar ele na regra certa, entendeu?  
**Marcelo Costa:** É, isso é um negócio que, tipo, os caras não vão saber nem que você dê. Pode falar, beleza, vou subir aqui uma NR34. O cara não sabe nem primeiro não sabe nem o que é canônica. Depois quando ele olha essas regras para ele, isso aqui também não é, mas beleza, mas é assim, fala trava o cara, senão você vai se fazer m\*\*\*\*, né?  
**Off Digital:** É, então é isso.  
**Marcelo Costa:** Agora eu posso importar o modelo aqui, referência. Aí ele vai fazer essa extração.  
**Off Digital:** Como assim?  
**Marcelo Costa:** Se eu pegar um modelo, tô criando um documento e eu pegar uma NR que já existe jogar aqui, aí ele vai puxar quem é esse cara.  
   
 

### 00:34:07

   
**Marcelo Costa:** Ele tem aqui anexar o modelo de referência. Será que se eu anexar o modelo ele faz ele preenche o  
**Off Digital:** Hum.  
**Marcelo Costa:** resto?  
**Off Digital:** Cadastro salva os campos suportados pelo catálogo. É, aí ele já preenche o resto. PDF de exemplo template, regras. Regras de upload pelo recrutador. Obrigatoriedade nas matrizes que usam esse documento.  
**Marcelo Costa:** Ja.  
**Off Digital:** O CR automático. Extrair campos do arquivo via CR. Formatos aceitos. validade.  
**Marcelo Costa:** É, depois a gente pode testar, mas não é nem a prioridade aqui.  
**Off Digital:** Sim, mas isso foi uma mudança que ele fez aí. Não sei porquê, não sei se foi por causa do do que a gente pediu lá do catálogo da base, ele organizou isso aqui,  
**Marcelo Costa:** É porque você vê que ele deixa até travado,  
**Off Digital:** entendeu?  
**Marcelo Costa:** tipo, sobe o documento aqui, eu vou fazer tudo.  
**Off Digital:** Exato.  
**Marcelo Costa:** A regra é essa, né?  
**Off Digital:** Exato.  
**Marcelo Costa:** Ficou bom. Você sobe um documento certo que você tem a base ou você sobe um e deixa  
**Off Digital:** Eh, sim.  
**Marcelo Costa:** comigo  
**Off Digital:** Aí na base agora tá filezinha, velho. Categoria, carga.  
**Marcelo Costa:** base.  
   
 

### 00:35:38

   
**Marcelo Costa:** Agora STCWR pito  
**Off Digital:** Vencimento 60 meses, 36 meses,  
**Marcelo Costa:** cliente.  
**Off Digital:** 48 meses. Só falta botar a rolagem, né? Isso aqui eu consigo fazer no paralelo.  
**Marcelo Costa:** Eh, até que você vê, ele tá em todos, ó. Eu tô em todos. Ah, que eu tô filtrando aqui. Beleza. Tiro o filtro. É, vamos botar uma rolagem em zona geral aí, senão ele fica muita tela, né?  
**Off Digital:** Vamos ver. Rê desconexão fix do override humano que sumar espelhar que total introduzir distinção. Reject ausente ver reject. Deixa logo isso aqui.  
**Marcelo Costa:** E aqui a gente precisava cadastrar o dos clientes, né? Ja. Marcelo, bom dia. Tudo bem? O orçamento tá lá, a Calinca que trabalha mais agora vai dar andamento a esse processo, tá? eh toda parte de documentação, eh, de autorização, notícia, você vão agora com ela passando esse contato para ela.  
**Off Digital:** Amor. Oi. Aham. Você depois me dá um copo aqui pela janela.  
**Marcelo Costa:** Ó, para mim, acabei de fechar aqui, tava namorinho aqui há um tempo com a com uma marca de arroz aqui, Rampinell.  
   
 

### 00:42:17 {#00:42:17}

   
**Off Digital:** Hum. que você tinha falado que eles estavam  
**Marcelo Costa:** É, é. Fiquei aqui, bati o pé, nega, veio pá pá pá, eu falei: "Vého não dá para mexer no preço que é entrega não sei o quê". Foi nove pau para um mês. Ela falou: "Ó, vamos fazer o teste um mês e tal e aí a gente vê". Eu falei: "Beleza, vamos testar aí". É, para mim não funciona um mês, né, velho? fazer um mês um negócio com dois RS, não sei o que, é difícil de medir uma um impacto, mas você vê as marcas como o cara tá assim,  
**Off Digital:** Yeah.  
**Marcelo Costa:** você vê que é, p\*\*\*, eu fui ver, é uma marca familiar grande até a marca, velho, tão fazendo um monte de coisa os cara, você vê que a indústria grande e tal e aquele tiozinho familiar que tá achando que agora precisa  
**Off Digital:** M.  
**Marcelo Costa:** contratar os influenciadores. E aí tá tomando tomando bid, né, de todo lado, né? E aí tá fazendo isso um mês por pessoa, tá ligado? Por por influenciador, onde eu acho que tá, eu vou até conversar com a agência aqui, eu acho que é muito mais negócio você ter um pelo menos três, se meses com alguém que você trabalha, porque senão fica muito propaganda, a galera não vai, né, cara?  
   
 

### 00:43:24 {#00:43:24}

   
**Marcelo Costa:** Você tem que inserir na vida da pessoa, tal. Mas você vê, eu acho que é um negócio muito mais para Emily do que do que para Letícia.  
**Off Digital:** E qual que é o escopo que vocês vão fazer com E qual que é o escopo que vocês vão fazer com  
**Marcelo Costa:** Hã,  
**Off Digital:** a  
**Marcelo Costa:** vamos fazer agora uma primeira reunião. Na verdade, ela já deu o escopo que a gente fechou é um eh dois  
**Off Digital:** marca?  
**Marcelo Costa:** resories. Acho que é isso. Sem muito briefing, foi esse o o negócio, né? Lógico, a gente falou: "Ah, vamos dar para fazer receita, dá para não sei o quê".  
**Off Digital:** Mas que tipo de conteúdo?  
**Marcelo Costa:** Mas agora,  
**Off Digital:** Tipo, a Letícia só vai falar da marca,  
**Marcelo Costa:** cara, é,  
**Off Digital:** tipo,  
**Marcelo Costa:** então, a gente vai fazer um briefing agora, primeiro briefing, mas eu já falei, pô, a gente nada especificado.  
**Off Digital:** só tipo dois  
**Marcelo Costa:** A gente falou, pô, a gente consegue, pode, dar para fazer receita, dá para fazer, cara,  
**Off Digital:** resolver,  
**Marcelo Costa:** vamos pensar o que que vocês querem. Ah, quer, você quer que direcione pro site da empresa, quer link, não quer? A gente não foi bem, pô, uma agência cuidando, mas cara, foi um briefing bem cru.  
   
 

### 00:44:26 {#00:44:26}

   
**Marcelo Costa:** Deu para ver que os caras assim tão bem cru, né?  
**Off Digital:** né?  
**Marcelo Costa:** É, fala, velho, não, quanto é que é dois res tal cara, p\*\*\*, vou, vamos conversar. Pretendo entregar muito mais que isso, né,  
**Off Digital:** H  
**Marcelo Costa:** velho? Por isso que depois, pô, você pegar agora, apresentar uma uma proposta, fazer um trabalho massa, você estica mais uns meses, entrega pro cara o qual que foi a visibilidade, quanto atingiu, não sei o quê, o que que tá fazendo, mostra a campanha, fala que tá impulsionando, mostra um pouco do que a gente tá fazendo, cara. É, mas você vê o quanto o cara tá disposto para botar em dinheiro, né, velho?  
**Off Digital:** p\*\*\*\*, assim, fácil não, né? Mas digo assim, cru, né? Cruzão, o cara já tá soltando. Imagina se  
**Marcelo Costa:** se organizar, né? Por isso que eu falo, eu já vou se ela falar: "Ah, não, tá fazendo esse picado,  
**Off Digital:** mirado.  
**Marcelo Costa:** eu já vou falar: "Agora tem mais uma outra influencer para vocês aqui pro mês, pro próximo mês, velho,  
**Off Digital:** Aí dá para você jogar no combo.  
**Marcelo Costa:** que vai fazer já faz  
**Off Digital:** Fala: "Ó, velho, se levar as duas é tanto, entendeu? joga no combo.  
   
 

### 00:45:27

   
**Marcelo Costa:** uma porque,  
**Off Digital:** Ah,  
**Marcelo Costa:** p\*\*\*\*,  
**Off Digital:** fala.  
**Marcelo Costa:** é muito mais negócio pro arroz, né, velho? fazer uma receita  
**Off Digital:** Ah, aí você fala, eu tô cuidando também. Eh, a Emily é uma influenciadora que eu tô cuidando também aqui do,  
**Marcelo Costa:** bagulho.  
**Off Digital:** né? Tô cuidando pro meu, eh, namorado do meu sócio, só tô cuidando. E a gente faz o combo, faz as colab das duas juntas, entendeu? Elas postam em collab, vai sair no perfil das duas ao mesmo tempo, fazem vídeo juntas. Aí a Letícia grava uma parte,  
**Marcelo Costa:** Eh,  
**Off Digital:** manda para cá, a Emily grava outra e junta tudo num vídeo só, entendeu? E aí e aí fala: "Então aí lógico que duas vai ficar mais caro, né?  
**Marcelo Costa:** é, mas aí você vai esticar,  
**Off Digital:** Então aí já mete lá vai 25",  
**Marcelo Costa:** você tá c\*\*\*\*\*\* para outras aí, né?  
**Off Digital:** entendeu?  
**Marcelo Costa:** Até que os caras tão fazendo no até  
**Off Digital:** Exato. Fala, ó. E a gente aí a gente vai ter uma chefe e uma nutricionista.  
**Marcelo Costa:** ver.  
**Off Digital:** Perfeito para vocês, entendeu? O combo. Aí vocês amarram a a parte nutricional com a parte de de especialidade de cozinha.  
   
 

### 00:46:22

   
**Marcelo Costa:** Deixa eu achar até o vou achar o o Instagram para ver como é que eles estão. Eu vi na época, mas Rampinelli. Pinelli. É, eu tinha agora tô lembrando aqui. Você vê aqui, ó, o Instagramzinha 29.000 os cara tem estão fazendo sim no tunelo. Vamos ver parceria. Acho que a filha do velho é uma das  
**Off Digital:** Fanciadora.  
**Marcelo Costa:** influenciadora.  
**Off Digital:** M.  
**Marcelo Costa:** Só falando. Você ouve meu áudio aí?  
**Off Digital:** Hã,  
**Marcelo Costa:** meu áudio que eu tô ouvindo no  
**Off Digital:** não,  
**Marcelo Costa:** Instagram.  
**Off Digital:** só se você compartilhar a tela, a aba do Chrome, aí sai para mim.  
**Marcelo Costa:** Agora tá travou o seu. Fala aí agora.  
**Off Digital:** Oi, tá ouvindo? Então, eh, para escutar o seu áudio, você tem que compartilhar a aba do Chrome.  
**Marcelo Costa:** Ah,  
**Off Digital:** Aí é,  
**Marcelo Costa:** porque eu tô olhando aí, ele  
**Off Digital:** aí sai o  
**Marcelo Costa:** vai,  
**Off Digital:** som.  
**Marcelo Costa:** mas dá para ver aqui. Indústria grande, tá ligado? Os cara grande. E de mandar aí para você dar uma olhada. Eu vou fechar esse aqui que nós estamos evoluindo para fechar aqui o contratinho e tal e depois já vou tentar enfiar o próximo aí para mim.  
   
 

### 00:49:45 {#00:49:45}

   
**Marcelo Costa:** Vai você ver, cara. Não tô focando nada nas marcas aí. As marcas vem pingando aqui. Se dá uma focada ali para cima,  
**Off Digital:** É, prim, é o que eu tô falando. Às vezes a gente pensa longe e o negócio tá mais próximo.  
**Marcelo Costa:** velho.  
**Off Digital:** E mano, a mina não para de crescer, velho. A Emily já tá com tá quase batendo 41\. Na semana passada que eu falei com você, ela tava com 38 daquele é,  
**Marcelo Costa:** Tá voando,  
**Off Digital:** velho,  
**Marcelo Costa:** né?  
**Off Digital:** já tá rumo aos 50\. E meu irmão, essa semana nós vamos fazer o o aulão lá do bolo de cenoura no Zoom. Inclusive, eu tenho que fazer umas paradas mais tarde disso e, mano, se atacar, porque, cara, além de tudo, a gente tem o poder da Iá junto para botar junto com as com as  
**Marcelo Costa:** Não, velho. Eu tava, eu fico pensando aqui, primo.  
**Off Digital:** marcas.  
**Marcelo Costa:** Eu tava toda hora rodeando e pensando, pô, preciso ter um produtinho. Nós temos um produtinho para ficar rodando, velho. Tá ligado? É o clube das minas rodando. Porque, p\*\*\*\*, a Letícia já faz a aula semanal aqui, velho.  
   
 

### 00:50:45

   
**Marcelo Costa:** Já faz, tá? 1000 pessoas ou ou uma, é a mesma coisa. Então, é só tacar pressão para vender isso.  
**Off Digital:** S.  
**Marcelo Costa:** As receitas da Emily, p\*\*\*\*, botar pressão para vender aí para cima das marcas. Eu acho, cara, tem um dinheiro grande aí, viu, primo? Um dinheiro grande aí na mesa que que eu tô deixando, pô. Eu não fui para cima, fui para cima da E você vê essa marca aqui, ela me procurou, daí ela largou mão, aí tava lá morta. Ah, eu tô vendo aqui ontem que eu lembrei, falei: "Deixa eu ir para cima aqui". Ela: "Ô, então vamos fechar para você ver que tava no tava só esperando alguém  
**Off Digital:** Hum. Só esperando um chute, né?  
**Marcelo Costa:** chegar junto, velho. O negócio tava lá mortão, eu, p\*\*\*\*, bati uma, duas vezes, beleza, vamos fechar." E é a parte comercial, né, velho? Tem que ficar em cima. É aquela coisa, né, velho? O cara vai lembrar de quem tiver de quem tiver na cola,  
**Off Digital:** Mas qualquer coisa tem o comercial.  
**Marcelo Costa:** né?  
**Off Digital:** Nós estamos desenvolvendo um negócio aqui, mas depois vai ter que ter a parte comercial porque,  
   
 

### 00:51:46 {#00:51:46}

   
**Marcelo Costa:** Tudo bem,  
**Off Digital:** né?  
**Marcelo Costa:** né?  
**Off Digital:** É, tudo tem. Então assim,  
**Marcelo Costa:** É.  
**Off Digital:** mas é o que a gente conversou aquele dia para mim, é que eu tô, nós estamos realmente fundo nesse negócio aqui do certify, mas cara, eu acho que depois a gente tem que fazer esse clube,  
**Marcelo Costa:** Да.  
**Off Digital:** esse produto que seja um clube com várias profissionais e e botar foco nisso, porque a gente vai conseguir fazer um funil, velho, que vai jorrar para pro lado de todo mundo e vai ter uma parada que porque, tipo assim, Por exemplo, eu tô querendo investir forte agora com a Emily, com o YouTube, velho, porque eu já entendi que não tem para onde  
**Marcelo Costa:** É, não. E outra, e ali é e o negócio,  
**Off Digital:** correr,  
**Marcelo Costa:** p\*\*\*\*, acima de 5 minutos, o cara vai ver no Instagram, um teaser, vai gostar e, pô, quero consumir mais.  
**Off Digital:** não. Por exemplo, a gente tava vendo um podcast daquela Julima, sabe?  
**Marcelo Costa:** Eh,  
**Off Digital:** Que a mina lá do churrasco, tá ligado? Ela tá com sete 7 pon.5 5 milhões no Insta.  
**Marcelo Costa:** SP  
**Off Digital:** Eh, e cara, aí ela tava falando, tipo assim, ela tem 7 milhões e meio no Insta,  
**Marcelo Costa:** Eu  
   
 

### 00:52:56

   
**Off Digital:** mas ela tem 900.000 no YouTube, que tipo ela é muito maior no Instagram, mas a autoridade forte dela tá no YouTube, porque, por exemplo, ela foi no podcast agora, ela fez um podcast lá na no sítio dela agora com o Flávio Augusto. Flávio Augusto foi lá comer churrasco com ela. Aí ela fez o o um outro podcast com aí fez com com Thiago Negro,  
**Marcelo Costa:** vi que o Thiago Negro se bobear fez com os cara, né?  
**Off Digital:** aí fez com outro maluco lá também, aí fez com o Joel J, entendeu? Então, se você não tá no YouTube,  
**Marcelo Costa:** Eh,  
**Off Digital:** velho, você não entra nesse circuito. E é esse circuito que dá autoridade braba mesmo, que fala tipo assim,  
**Marcelo Costa:** é,  
**Off Digital:** tá, agora você pode pedir caro porque você tá com os cara caro,  
**Marcelo Costa:** é. E assim,  
**Off Digital:** né?  
**Marcelo Costa:** e os cara e e os caras estão sempre procurando porque chega uma hora que não tem mais podcast para gravar,  
**Off Digital:** Não tem,  
**Marcelo Costa:** velho.  
**Off Digital:** velho.  
**Marcelo Costa:** Então,  
**Off Digital:** Não tem mais podcast,  
**Marcelo Costa:** né, velho?  
**Off Digital:** faz mesma figura. É, Cariane, eh, não sei das quantas. Então, é aquela mesma galera que domina a audiência, entendeu?  
   
 

### 00:53:53

   
**Off Digital:** Aí põe lá o TK, aí põe lá o aí o Joel, não sei das coisas.  
**Marcelo Costa:** É, aí entraram com os fanqueiros,  
**Off Digital:** Aí eu é aí os fanqueiros sujeira todo sendo preso lá no  
**Marcelo Costa:** aí tiraram os fanqueiros aí no É,  
**Off Digital:** bagulho de bet,  
**Marcelo Costa:** tira os car.  
**Off Digital:** n rolos aí já não sujeira não dá.  
**Marcelo Costa:** Não, esse daí não  
**Off Digital:** É. Aí, então assim, velho, e e cara,  
**Marcelo Costa:** é  
**Off Digital:** é um é um negócio de tipo assim vender e essa essa conexão mesmo que a mina, mano, por exemplo, ela se formou lá na na Lecod Blan lá de Paris, só que, mano, ela faz churrasco, velho. Você acha que ela aprendeu churrasco em Paris na Lecodobama?  
**Marcelo Costa:** não, ela só foi lá para pegar o título e poder falar,  
**Off Digital:** Entendeu?  
**Marcelo Costa:** né?  
**Off Digital:** E então assim, eh, no fim das contas,  
**Marcelo Costa:** Ela  
**Off Digital:** o que ela faz é basicamente a conexão com o público, porque não é por causa de uma receita. Aí ela inventa lá carne com goiabada, carne com doce de  
**Marcelo Costa:** ela acertou, ela acertou no nicho ali,  
**Off Digital:** leite.  
**Marcelo Costa:** né, primo, porque assim, ela pegou um nicho universal assim, né, que é p\*\*\*\* uma mulher bonita falando de churrasco, cara.  
   
 

### 00:54:57

   
**Marcelo Costa:** Você para para ver, velho.  
**Off Digital:** É, então, mas com certeza,  
**Marcelo Costa:** Entend  
**Off Digital:** mas é o que eu tava até falando com a Emily ontem, é churrasco, é um subnicho, beleza? Mas embaixo de, em cima de churrasco, a gente tá falando de receita.  
**Marcelo Costa:** que é é um é um dos maiores nichos que tem.  
**Off Digital:** Porque no fim das contas o que ela passa do churrasco é uma receita, é o beabá do churrasco. Então ela ela dominou o o churrasco. A Emily Velha tem ela pode ir para pão, para doce, para qualquer coisa, mas é receita, entendeu?  
**Marcelo Costa:** É,  
**Off Digital:** Então, só que o  
**Marcelo Costa:** você vê,  
**Off Digital:** o  
**Marcelo Costa:** primo. E eu acho que agora é a hora do Elness, tá ligado, cara? É,  
**Off Digital:** Sim,  
**Marcelo Costa:** tá impressionante o movimento, o jeito que tá,  
**Off Digital:** é, eu sei.  
**Marcelo Costa:** cara.  
**Off Digital:** Tá muito grande corrida tá  
**Marcelo Costa:** ontem eu fui correr aqui, velho. É,  
**Off Digital:** bizarra.  
**Marcelo Costa:** cara, você tem que 5 horas da manhã você tem que desviar da galera, velho. Tá cheio, lotado, lotado.  
**Off Digital:** Sim,  
**Marcelo Costa:** Todo  
**Off Digital:** sim. Não, aqui também, velho.  
   
 

### 00:55:59 {#00:55:59}

   
**Off Digital:** Aqui eu fico vendo a rua aqui de frente pra rua, meu irmão. É nego passando correndo toda hora, correndo de bike.  
**Marcelo Costa:** mundo  
**Off Digital:** É, cara, é, é, é, tá muito grande. Só que assim, o que que eu vejo para mim que fura bolha, independente do nicho, eh, é você saber conectar com a galera de um jeito que a galera velha intimidade com você. Então, por exemplo, cara, você vai dormir, você terminou seu dia de trampo e tal, desligou dos computador e tal, aí você tá encostado no sofá ali, 11 da noite, você pega, velho, e abre um vídeo da pessoa, mano, olha a conexão, entendeu? É um bagulho muito forte, entendeu? Porque aí aí a pessoa mostra a casa dela, mostra a vida, aí passa os filhos correndo, aí chega o marido do nada. Então, é isso que gera era essa conexão tão grande, não é o nicho, não é o entregável. Aí, lógico, aí, lógico, você tá entregando valor. Independente de qualquer coisa, você tem que entregar valor. Então, p\*\*\*\*, entregou uma receita lá, mano, a pessoa fez e tal, isso ela já tá entregando. Tanto é que o vídeo que furou a bolha dela, o último, mano, é um vídeo muito simples.  
   
 

### 00:57:09 {#00:57:09}

   
**Off Digital:** É um pompita, mano.  
**Marcelo Costa:** aquele pão lá você me mandou.  
**Off Digital:** Pô, velho, o pompita, mano.  
**Marcelo Costa:** Mas mas muito bom e fácil,  
**Off Digital:** É o bagulho,  
**Marcelo Costa:** né? Você olha,  
**Off Digital:** o bagulho,  
**Marcelo Costa:** fala: "Pô,  
**Off Digital:** o bagulho é água só e farinha,  
**Marcelo Costa:** nós tinha que fazer,  
**Off Digital:** primo. Literalmente. Não, não,  
**Marcelo Costa:** eu tinha que fazer, refazer essa,  
**Off Digital:** não.  
**Marcelo Costa:** essa coisa, a Letícia fazer aqui pra gente ver, eh,  
**Off Digital:** Né?  
**Marcelo Costa:** pra gente ver o que dá." ela refazer exata, velho. A mesma coisa pra gente ver o que que para entender,  
**Off Digital:** Aham.  
**Marcelo Costa:** velho. Se é, sei lá, se pegou  
**Off Digital:** O o o Aham.  
**Marcelo Costa:** no  
**Off Digital:** foi o estilo do vídeo, foi a o jeito que ela fala em cima na narração.  
**Marcelo Costa:** É, a gente precisava destruir esse negócio para entender o que que que o que que foi que pegou,  
**Off Digital:** Mas ela mas ela tem um mas ela tem uns trickzinho, velho,  
**Marcelo Costa:** né?  
**Off Digital:** de de take. Por exemplo, o primeiro take do vídeo é o pão inflano. E aí é um é uma parada que é porque  
   
 

### 00:57:59

   
**Marcelo Costa:** Sim, que o bagulho te dá fome, você fala: "Quero comer esse bagulho, vou  
**Off Digital:** ele infla e aí você fala: "Hum,  
**Marcelo Costa:** escutar.  
**Off Digital:** nunca nunca imaginei que um pão pita infla". E aí, aí tem um um take também que fica um em cima do outro, assim, tipo uma escadinha assim de vários palpites, que é um take também que, tipo, isso aí, ela manja, que ela pega referência f\*\*\* de take e aí o jeito que ela grava faz o produto final ficar  
**Marcelo Costa:** Ô primo, vamosar.  
**Off Digital:** muito.  
**Marcelo Costa:** Não dá pra gente adaptar, pegar esse vídeo, adaptar aqui e e fazer ele.  
**Off Digital:** Ah, velho, é muito fácil. Fala pra Letícia fazer igual.  
**Marcelo Costa:** Vamos.  
**Off Digital:** faz os mesmos take do mesmo jeito e posta igual, entendeu? E vamos ver.  
**Marcelo Costa:** Pode até de repente você mandar porque aparece a Emily nesse coiso. Não,  
**Off Digital:** Não, só a mão dela.  
**Marcelo Costa:** só a mão.  
**Off Digital:** Aham.  
**Marcelo Costa:** Mas o áudio dela, alguma coisa? Depois eu vou ver.  
**Off Digital:** O áudio é.  
**Marcelo Costa:** Ela falando, ela  
**Off Digital:** Põe aí para você ver,  
**Marcelo Costa:** narrando.  
**Off Digital:** mano. O vídeo tá com vai bater 12 milhões, primo.  
   
 

### 00:59:03 {#00:59:03}

   
**Marcelo Costa:** Então é  
**Off Digital:** Sem 1 centavo de tráfego.  
**Marcelo Costa:** isso.  
**Off Digital:** Ah.  
**Marcelo Costa:** P é Emily com Y,  
**Off Digital:** Não é Emily com I. Emily Zaremba,  
**Marcelo Costa:** primo.  
**Off Digital:** tudo junto.  
**Marcelo Costa:** Eu segui aqui. Por que que sumiu? aqui tava seguindo ele tá fixado aqui, né? Primeiro  
**Off Digital:** Ah, é o primeiro. É.  
**Marcelo Costa:** aqui Ó, curtinho, simplinho. Pá, pá,  
**Off Digital:** Mano, muito simples, velho. Tipo, muito simples.  
**Marcelo Costa:** pá.  
**Off Digital:** E inclusive esse vídeo você vê que ela não botou nem legenda, é só o áudio. Não tem legenda.  
**Marcelo Costa:** Mas tá bonito o Insta, hein, velho?  
**Off Digital:** Tá, velho. Não. E e ainda dá para melhorar bastante. Tipo assim, eu ajudo ela com uma tamb ou outra, ela me pergunta: "Amor, que que eu ponho aqui de capa e tal?" Eu falo: "Não, corta mais aqui, amplia mais aqui". Mas tem muita coisa assim que ela faz sozinha que que ainda dá para melhorar. Tipo assim, eh, cara, o potencial é muito  
**Marcelo Costa:** Eh, não. E aqui, velho, você vê, cara,  
**Off Digital:** grande.  
**Marcelo Costa:** é, você vê as marcas aí, priminho, quantos caras estão dispostos a pagar para fazer 50, 60 pau com marca no mês.  
   
 

### 01:01:22 {#01:01:22}

   
**Marcelo Costa:** Não é difícil,  
**Off Digital:** Pois é,  
**Marcelo Costa:** velho.  
**Off Digital:** mano. Eu também acho.  
**Marcelo Costa:** Não é difícil.  
**Off Digital:** Eu também acho. Então a gente precisa dar o É,  
**Marcelo Costa:** Vamos acabar esse certifio.  
**Off Digital:** então eu acho que a gente precisa dar uma folga aí de tempo e dar uma focada, dar uma estudada, passar uma semana reunindo todo dia, pesquisando,  
**Marcelo Costa:** É,  
**Off Digital:** vendo como é que a gente junta,  
**Marcelo Costa:** eu te mostro tudo que eu tô fazendo aqui. Tem coisa que eu  
**Off Digital:** como é que a gente junta os pauzinhos, o que que tá bombando. Eu acho que a gente tem que pegar o que tá bombando agora.  
**Marcelo Costa:** tô  
**Off Digital:** Tipo, agora que eu digo assim, pô, semana que vem vamos fazer reunião, vamos ver o que tá bombando no dia e e trabalhar em cima disso, entendeu? Tentar pegar o o time do momento em vez de tipo ficar pegando o que para  
**Marcelo Costa:** mas você vê que Mas você vê, por exemplo, p\*\*\*\*, velho,  
**Off Digital:** trás.  
**Marcelo Costa:** esse que bombou aqui, ele não tem, falando em conteúdo, né?  
**Off Digital:** Aham.  
**Marcelo Costa:** Ele não tem nada a ver com o momento, né?  
**Off Digital:** Não, não  
**Marcelo Costa:** Nada a ver com momento, tem nada a ver com nada,  
   
 

### 01:02:12 {#01:02:12}

   
**Off Digital:** tem  
**Marcelo Costa:** velho. É uma p\*\*\*\*, beleza. Eh, tem muita coisa de momento  
**Off Digital:** não. E aí, cara, uma coisa que aconteceu nos dois vídeos dela que bombaram,  
**Marcelo Costa:** K.  
**Off Digital:** eh, que, velho, tem hater para c\*\*\*\*\*\* nos vídeos. O neguinho falou: "Não, porque ela fala no ele ela fala nesse vídeo que ela fala que o pão pita é o pão mais antigo do mundo." Aí vários nego falando: "Não, não é o mais antigo do mundo, porque o mais antigo é isso". Aí outros aí vem vários caras comentando embaixo defendendo, fala: "Velho, você não sabe de nada, deixa a menina falar, não sei o qu". Aí já vem outros e fala não porque e mano  
**Marcelo Costa:** É, é um negócio que, p\*\*\*\*,  
**Off Digital:** cois  
**Marcelo Costa:** a gente não quer isso, né? A mulher, principalmente a Alia não queria nunca qualquer hater, nem tem. Só que é o que faz o bagulho bombar,  
**Off Digital:** mano,  
**Marcelo Costa:** velho.  
**Off Digital:** em 5 minutos já tinha tipo assim 80 90 comentários e nego tretando no vídeo. Aí fica vindo e ela não fala nada, ela não comenta nada nos posts, fica só um falando, aí vem um defende, aí o outro apoia e aí o outro tá falando se defende de novo.  
   
 

### 01:03:23 {#01:03:23}

   
**Off Digital:** E aí, mano? E ela fica dando risada, vem me mostrar, falou: "Mano, olha isso aqui, velho." Aí vem um falando que glúten faz mal, aí vem outro falando: "Velho, você não sabe de nada porque glúten não faz mal". Aí já, mano, é maior loucura.  
**Marcelo Costa:** Eh,  
**Off Digital:** E isso engaja muito porque o Insta fala:  
**Marcelo Costa:** É, não é aí onde vira a doideira,  
**Off Digital:** "Velho, é o Insta fala". Aí começa a entregar, velho, o bagulho,  
**Marcelo Costa:** né?  
**Off Digital:** entendeu? E a Ju falou no podcast também eh, do negócio do R test, manja. Tem agora,  
**Marcelo Costa:** Não,  
**Off Digital:** cara, um negócio chama res de test, eh, que você posta,  
**Marcelo Costa:** você põe o vídeo para ver se ele vai bombar.  
**Off Digital:** não, você posta o resgue, só vai entregar para nego fora da sua base. E aí, cara, ela falou que de 7 milhões de seguidores que ela tá,  
**Marcelo Costa:** Eh,  
**Off Digital:** 3 milhões, ela ganhou só de real teste. Ela fez uma estratégia pro R test que é só que entrega para fora da sua base.  
**Marcelo Costa:** p\*\*\*\*, e eu vi um outro agora priminho, até mandei pra Letícia ontem, vou te mandar aí, que é um negócio que a Meta lançou para você botar seu vídeo e ele foi treinado.  
   
 

### 01:04:31 {#01:04:31}

   
**Marcelo Costa:** com com cara assistindo vídeo dentro de uma daquelas máquinas de ressonância. Então ele vê onde estimula. Então você bota seu vídeo lá, ele vai falar em que momento seu vídeo tá desestimulando e tá fazendo a pessoa sair.  
**Off Digital:** c\*\*\*\*\*\*.  
**Marcelo Costa:** Tá esse tá treta. Eu mandei ontem pra Letícia, vou te mandar aqui para você ver. É da meta, velho. Aí eu não vi, não entendi ainda como é que é. Eu acho que é um repositório do Git que você precisa baixar alguma coisa assim. Te mandei aí depois você vê. Deixa eu só responder a negra. Tá, tá trampando aí no paralelo para mim. O bichinho tá  
**Off Digital:** Tô velho. Tô tô metendo ficha aqui. Tirar validade. Deixa observação.  
**Marcelo Costa:** indo. Esse p\*\*\*\* desse negocinho do Insperflow, ele um negocinho bem no meio da tela, né?  
**Off Digital:** Sim, às vezes me atrapalha também.  
**Marcelo Costa:** Tir já tentou tirar  
**Off Digital:** Não dá, velho.  
**Marcelo Costa:** ele.  
**Off Digital:** Aí o meu eu ia fazer que em vez de ficar no meio da tela, ele ficasse lá na barrinha de cima.  
**Marcelo Costa:** É,  
**Off Digital:** Eu acho muito melhor,  
   
 

### 01:06:06 {#01:06:06}

   
**Marcelo Costa:** pô, aqui ele você tem que ficar reduzindo a tela.  
**Off Digital:** velho.  
**Marcelo Costa:** Você tá no WhatsApp, ele fica bem onde você quer digitar ali,  
**Off Digital:** Eu ia botar na tela de cima que fica muito mais legal.  
**Marcelo Costa:** né?  
**Off Digital:** F.  
**Marcelo Costa:** Deixa eu ver a minha agenda aqui. Primo, amanhã nós temos aquela reunião com o cara,  
**Off Digital:** Sim,  
**Marcelo Costa:** né?  
**Off Digital:** às 11 lá.  
**Marcelo Costa:** É.  
**Off Digital:** Temos que mexer nisso, né? Dá uma  
**Marcelo Costa:** Eh, cara, eu tava dando,  
**Off Digital:** olhada.  
**Marcelo Costa:** eu tava pensando aqui, eu acho que pode ser que, né, daqu a gente falando daquelas camadas, botar uma camada de IA ali, eh, é mesmo uma camada para usar os dados dele e trazer em site.  
**Off Digital:** Угуm.  
**Marcelo Costa:** Por exemplo, ela não mostrou lá o cara da equatorial lá que tem todos os os as obras, né? Então o cara tem lá, p\*\*\*\*, tô fazendo trecho daqui aqui, não sei o quê, ele vai monitorando essas obras e ali tem informação de quem é o cara e tal, p\*\*\*\*, não, essa obra não funcionou e ou atrasou, não sei o quê. Esses dados que ela tem tudo ali, uma poderia fazer o cruzamento, por exemplo. p\*\*\*\*, cara, eh, tantos dias desse mês foram perdidos por causa da chuva.  
   
 

### 01:08:55 {#01:08:55}

   
**Marcelo Costa:** Então você vê que período de chuva a obra a a produtividade cai tanto aí, p\*\*\*\*, análise de do funcionário, p\*\*\*\*, o Marco eh não produziu esse por causa disso, isso, chegou atrasado, não fez ver que todos os erros foram por causa do mais acarretado em cima do mar,  
**Off Digital:** Угу.  
**Marcelo Costa:** porque não sei o quê. Então, pegar os dados dele e trazer insightes que normalmente o cara tem que ter esse insite e ele pega lá o relatório e ele fica criando esse insite, né? Beleza, eu pego um relatório, aí eu cruzo alguns dados aleatórios ali que não tão nesse nesse dado principal, que é os capis que eu meço, mas que são coisas que podem às vezes tá dando uma indicação que os caras não estão vendo, né?  
**Off Digital:** Sim. Você tem o o transcrito daquela call? Vamos jogar ela na IA aqui.  
**Marcelo Costa:** Tenho.  
**Off Digital:** Vamos vamos pedir um resumo visual pra gente lembrar alguns pontos que ela passou do sistema.  
**Marcelo Costa:** Deixa eu pegar  
**Off Digital:** Cara, eu acho que a gente tem que vir com uma camada. Eles não têm nenhuma camada de a.  
**Marcelo Costa:** aqui.  
**Off Digital:** Então, cara, o relatório é a ponta final, né, basicamente. Então, todo o sistema deles funciona para eh logística, né, ou seja, eh, monitoramento da da logística do dia a dia das obras.  
   
 

### 01:10:25 {#01:10:25}

   
**Marcelo Costa:** processo de obra, né? Monitoramento de processo de  
**Off Digital:** Processo processo logística. Isso tudo acaba onde?  
**Marcelo Costa:** obra.  
**Off Digital:** fora a logística ali do meio de campo que o cara tá vendo dentro do sistema, o cara que foi, o cara que não foi, quanto que ele gastou na obra, quantos dias tá atrasado, etc., que é o o a tocada da obra mesmo, o ponto final é o relatório. Então, quando a quando você entrega os relatórios em PDF, tá na mão do cliente, tá na mão do tá na mão também do time interno e ali morreu. Então, qual que é, qual que a minha ideia? a gente implementar uma camada do relatório pra frente. Então, o que que você faz? Você não tem hoje trabalhando esses relatórios. Então, a gente criar uma camada de a que pega esses relatórios e te dá insites, além de insites, te dá eh diagnósticos. do que, cara, pô, por que que esse relatório pode melhorar, né? O que que a gente não tá medindo nesse relatório que a gente pode medir? O que que a gente tá medindo que a gente não precisa medir? Quais são os insightes valiosos que a gente tem dentro de de desse relatório para cada cliente? E o workflow de como você recebe isso.  
   
 

### 01:11:39 {#01:11:39}

   
**Off Digital:** Então, vender essa comodidade pros caras, falar: "Cara, você vai receber tudo no Telegram, você vai". e aí criar essa malha de agentes para eles. Ó, como é que a comunicação interna de vocês? É viail. Eu vou criar um agente aqui que faz isso, isso e isso. Como é que a eh como é que esse relatório é entregue dentro do time? Como é que ele é entregue pro cliente? E a gente criar essa malha,  
**Marcelo Costa:** de consulta, né,  
**Off Digital:** essa não,  
**Marcelo Costa:** de  
**Off Digital:** essa malha de um time de agentes para tocar do relatório paraa  
**Marcelo Costa:** É. E além do relatório, eh,  
**Off Digital:** frente.  
**Marcelo Costa:** talvez que eu veja, por exemplo, tava vendo aqui fuçando um software aqui de de gestão, emissão de nota, não sei o quê. Aí fui e tal, já tava, já tinha visto, já caí naquele homem, sabe? É um pá, é tipo um conta azul e você tem ali emissão de nota e você põe contas a pagar, contas a receber.  
**Off Digital:** Tá.  
**Marcelo Costa:** É um RP, tá? Mas ele emite nota, ele faz o só sincroniza com o seu banco, né? Então eu tava fazendo, criando um meu aqui, falei: "Velho, fica criando essa p\*\*\*\*, eu vou pegar um que já existe, emito nota, c\*\*\*\*\*\*, não tem para que criar um negócio desse, velho." Aí falei,  
   
 

### 01:12:50 {#01:12:50}

   
**Marcelo Costa:** o que tem que fazer é botar uma camada em cima. Dados estão lá, emissão da nota já tá lá, o cara já tem integração com o banco. Eu não quero me meter nisso. Quero uma camada em cima para tocar tudo pelo Telegram, para puxar, para fazer todas as função de botãozinho que ele tem. Entra aqui, entra aqui. Eu não quero clicar em nada,  
**Off Digital:** Exato.  
**Marcelo Costa:** velho. Eu quero. Então, aí eu fui ver o homem que eu tá tinha olhado, tal, acabei de ver o lançamento deles, WhatsApp, para fazer exatamente isso. Então, você para de executar o sistema e você pode executar ele via WhatsApp ou via Telegram. Então, o cara tinha cinco botões para apertar, ele não aperta mais cinco botão. Ó, preciso do relatório tal para reunião, pum, acabou. Então, todos os botões que ele já tem organizado, eu tiro a tração do cara e ponho uma camada do agente que opera o sistema dele, né?  
**Off Digital:** Exatamente.  
**Marcelo Costa:** Então, é, é, opera seus dados e vai trazer em site que você não consegue ver. Você não pega 10 relatórios do último ano e fica tendo insite.  
**Off Digital:** Exatamente.  
**Marcelo Costa:** Talvez o gerente pegue isso, um cara lá em cima, que é o que o cara faz, ele olha e fala: "p\*\*\*\*, velho, esse ano nós fizemos isso, deixa eu ver, pega o outro relatório lá, o cara vai cruzando, mas se ele jogar hoje tudo aí, às vezes vai trazer uns insightes que o cara não  
   
 

### 01:14:04 {#01:14:04}

   
**Off Digital:** Não, independente do que ele faz e não faz,  
**Marcelo Costa:** viu."  
**Off Digital:** independente dos insites, só o valor de automação disso é enorme, entendeu?  
**Marcelo Costa:** É.  
**Off Digital:** Tipo, não interessa quem faz ou como faz, interessa é que isso hoje é manual, entendeu? Se eu faço isso ser automatizado para você, então acho que a gente tem que vender para ele automação e, lógico valor dos gaps do que hoje ele não tem. Então esse combo, então cara, eu vou automatizar o o que você já tem hoje do relatório para frente, porque a gente não quer entrar no sistema. Esse é o ponto. Eu acho que a gente quer criar uma sofisticação numa ponta do sistema que ele ainda não mexe, que vai tá atrelado ao sistema. Tipo,  
**Marcelo Costa:** que ele vai falar, pô, que a gente agregue valor,  
**Off Digital:** a gente exato,  
**Marcelo Costa:** não para ir lá mexer no que já tem, né, velho?  
**Off Digital:** a gente entra por cima, a gente não entra dentro. A gente vai construir uma peça que ele vai plugar no sistema.  
**Marcelo Costa:** Senão,  
**Off Digital:** É basicamente isso, entendeu? E aí essa peça é uma malha de análise com IA e uma malha de distribuição disso com IA. Então, como que, velho, essa informação chega na gerência?  
   
 

### 01:15:15 {#01:15:15}

   
**Off Digital:** Como que essa informação chega no cliente? Como que essa informação chega no dono? Porque cada um precisa da informação embalada de um jeito. O gerente precisa de algo muito mais eh fragmentado a  
**Marcelo Costa:** Sim.  
**Off Digital:** nível portfólio de cliente.  
**Marcelo Costa:** É tipo,  
**Off Digital:** Então, ele precisa ver lá, cara,  
**Marcelo Costa:** que momento esse cara consulta esse relatório?  
**Off Digital:** o que que eu tenho?  
**Marcelo Costa:** Que momento ele tá usando? Ah, p\*\*\*, ele usa para uma reunião, não, ele mensalmente quer olhar, ele ó, vamos automatizar esse processo de chegar na mão dele essa informação.  
**Off Digital:** por exemplo,  
**Marcelo Costa:** Lidian  
**Off Digital:** por exemplo, A, como que é o nome da menina lá?  
**Marcelo Costa:** Lani  
**Off Digital:** Lidiane. A Lidiane, provavelmente, ela tem que entrar todo dia na plataforma para gerenciar várias coisas, né? Beleza? Não que ela vai deixar de entrar, porque com certeza tem coisas que acontecem durante o dia que ela precisa est a pá, que ela precisa tá interagindo, mas no final do dia, se ela tiver um p\*\*\* de um relatório cincado de tudo que rolou no dia, tudo separadinho, enviado para ela dentro do WhatsApp, cara, é um consolidado que, tipo assim, é o trampo que ela tá fazendo todo dia, mas que ela não mede.  
   
 

### 01:16:30 {#01:16:30}

   
**Off Digital:** Ela não mede. Ó, hoje eu fui lá e mexi nisso aqui, depois eu mexi naquilo ali e o resultado disso foi isso e foi aquilo. Ela tá só fazendo trampo,  
**Marcelo Costa:** É,  
**Off Digital:** ela não tá medindo.  
**Marcelo Costa:** ela não tá medindo o tempo dela gasto nisso. Aí nós estamos falando de outra frente que é uma a gestão dele de software dele, né? Na minha gestão de atividades dentro da minha empresa mesmo. O que que meus minhas pessoas fazem? O que que elas precisam pegar do sistema de insite para esse negócio continuar andando. Que que eu vejo já o problema com o cliente? Travou a tela, tal, eu tenho que entrar aqui, não sei o quê. O que que disso ele consegue otimizar utilizando agentes ali para como uma camada, né? Isso olhando para ele como  
**Off Digital:** É, por exemplo, por exemplo, Exemplo, a Lidiane ficou logada eh 6 horas hoje no sistema e dentro  
**Marcelo Costa:** empresa.  
**Off Digital:** dessas 6 horas ela abriu essa e essa aba, ela aprovou isso, isso, isso, ela rejeitou isso, isso e isso, ela enviou isso, isso, isso, ela solicitou isso, isso, isso. Você tem todos esses dados lá dentro do sistema, mas ninguém deve parar para olhar e falar, velho,  
   
 

### 01:17:34 {#01:17:34}

   
**Marcelo Costa:** analisar  
**Off Digital:** hoje analisar isso de 24 em 24 horas e embalar isso no relatório. Ninguém, tipo, eles não têm esse relatório de,  
**Marcelo Costa:** isso.  
**Off Digital:** velho, o que que a Lidiane fez? Porque isso já destrinche em várias coisas. Então tá, eu sei que o tempo da Lidiane tá sendo gasto 4 horas em equatorial, meia hora em tal cliente, meia hora em tal cliente. Por que que ela tá gastando 4 horas em equatorial? Dá para diminuir essas horas? Por que que a gente tá tendo tanto problema recorrente com a equatorial, entendeu?  
**Marcelo Costa:** Estamos cobrando certo às vezes, p\*\*\*\*. Dá  
**Off Digital:** Como cobrando certo ou estamos pedalando no quê? Que que ela gastou nessas 4 horas?  
**Marcelo Costa:** para  
**Off Digital:** Aí você já entra no detalhe. gastou nisso, nío, nisso. Pô, então nosso setor de de presença do cara da obra tá defasado, porque todo dia ela tá gastando 4 horas nisso,  
**Marcelo Costa:** É. Ou ou nós estamos pouco,  
**Off Digital:** certo?  
**Marcelo Costa:** estamos cobrando aqui do cara e estamos gastando muito tempo em desenvolvimento enquanto deveria ser não sei o quê.  
**Off Digital:** Uhum.  
**Marcelo Costa:** Aí o cara começa a ter do negócio  
   
 

### 01:18:27 {#01:18:27}

   
**Off Digital:** Sempre o próprio o próprio eh processo deles de brifar  
**Marcelo Costa:** dele.  
**Off Digital:** e de criar, com certeza tem um monte de ponta solta de tipo, cara, como é que o cliente chega para com uma com uma sugestão de algo que precisa ser implantado e como é que esse meio de campo acontece. Não tem lá no meio organizando o brief do cliente, né?  
**Marcelo Costa:** Vendo,  
**Off Digital:** distribuindo.  
**Marcelo Costa:** cruzando com o que ele tem de steack,  
**Off Digital:** Exato.  
**Marcelo Costa:** trazendo a solução pro cara.  
**Off Digital:** Exato. Então assim, só que isso aí a gente ainda entra um pouco mais dentro.  
**Marcelo Costa:** dentro do negócio dele, porque aí pensa que isso seria um custo para ele,  
**Off Digital:** Exato.  
**Marcelo Costa:** não tá agregando valor  
**Off Digital:** Você vê que o que ela o que ela mais interessou foi naquele relatório que ela precisa,  
**Marcelo Costa:** Да.  
**Off Digital:** que é justamente precisaria de uma IA, que ela falou o nome do relatório lá, que cara é muito manual, que é mais ou menos o que a gente tá falando. Por isso que é bom você pegar aí o o o transcrito que a gente vai ter o OAD, sei lá. Ela falou o nome de um relatório lá, ela falou: "Cara, lembra que eu perguntei, falei: "Qual que é a dor que vocês têm aí, mano?  
   
 

### 01:19:29 {#01:19:29}

   
**Off Digital:** Que hoje tá difícil de resolver." Aí ela falou:  
**Marcelo Costa:** É, ela falou,  
**Off Digital:** "p\*\*\*\*,  
**Marcelo Costa:** é isso aqui,  
**Off Digital:** hoje é esse relatório".  
**Marcelo Costa:** né?  
**Off Digital:** Entendeu? Então, se a gente resolver isso e trazer mais uma malha de agente para operar em várias frentes, velho, a gente vai falar: "Ó,  
**Marcelo Costa:** E eu acho que dele também nós vamos tirar mais informação,  
**Off Digital:** vou  
**Marcelo Costa:** né, do cara cabeça mais acima,  
**Off Digital:** sim,  
**Marcelo Costa:** né, do que que ele vê,  
**Off Digital:** sim. Sim. Aí o que que a gente prepara?  
**Marcelo Costa:** né?  
**Off Digital:** A gente fala, ó, que a gente já viu de gap. É isso. Agora a gente precisa entender da sua parte para conseguir fechar esse esse escopo, esse escopo geral. Mas cara, eu já acho que é muita porta só de malha. O que que que a gente que que que o cara tem que entender? que a gente vai olhar a empresa dele e vai automatizar tudo que precisa ser automatizado. Eu acho que esse seria o objetivo da gente passar na conversa,  
**Marcelo Costa:** Sim.  
**Off Digital:** entendeu? E dar exemplos do que precisaria ser automatizado e qual que é o valor que ele tem de automatizar essas frentes, entendeu?  
**Marcelo Costa:** É, acho que é um primeiro.  
   
 

### 01:20:39 {#01:20:39}

   
**Marcelo Costa:** Tô baixando aqui um São dois call. Lembra que a gente saiu em um, entrou em outro e acabou o tempo. Vou mandar pro seu.  
**Off Digital:** Sim.  
**Marcelo Costa:** Eu já tinha feito isso até para mandar mensagem para ele. Eu eu já tinha mastigado. Ó, tem uma nega me ligando aqui. Tem coisa errada, velho. Não é? Eh, eu te mandei aí, vou mandar a mensagem que eu mandei para ele.  
**Off Digital:** O sea,  
**Marcelo Costa:** He. Mandei mandei a mensagem que eu mandei para ele para st  
**Off Digital:** a estante com a, né?  
**Marcelo Costa:** é esse mudo, né?  
**Off Digital:** อ  
**Marcelo Costa:** Ja. sobre o que que ele tá executando aí.  
**Off Digital:** Ele tá executando a barra de rolagem eh da aba de rolagem. o cambincado com a com a barrinha lá no no detalhe do candidato. E aqui e aqui o negócio de quando ele aprova rejeita e e dá pendente lá no no detalhe do candidato também.  
**Marcelo Costa:** M.  
**Off Digital:** Seas três, três ajustes. Aí matando os três, a gente vai pros próximos, porque eu acho que mais de três já começa.  
**Marcelo Costa:** É, não. Tá bom. Acho que é o tamanho aí.  
**Off Digital:** S  
   
 

### 01:25:54 {#01:25:54}

   
**Marcelo Costa:** Deixa um segundo aí para mim. Já vem.  
**Off Digital:** M. botando ele para desenvolver aqui o material da reunião já no outra janela.  
**Marcelo Costa:** Quer ver? Vou achar um negócio que eu queria ver. Eita, fechei a do zap. M.  
**Off Digital:** Ah.  
**Marcelo Costa:** Primeiro eu tive uma reunião com os cara de de Londres, de Londres não, de de da Noruega, que é uma empresa de de transporte lá, né? Na verdade, ele faz uma, ele é um sistema para transportadora. Então, ele organiza os fretes, organiza a documentação, eh, ele une ascos de transporte e tal. Aí eu vi aqui que ele tem uma camada de de a que ele botou aqui, né? Ele botou uma camada, tipo assim, ó, nossos agentes de A são projetados para complementar a tomada de decisão humana, não para substituí-la. Eles propõem planos, redigem comunicados e destacam informações críticas, mas sempre exigem aprovação humana para ações finais. Isso garante que você mantenha o controle total enquanto se beneficia da eficiência dos insites proporcionados pela IA. Então aí ele tem aqui uma alguns coisas, né? Por exemplo, processo de pedido por IA, importação, processamento, automatização de pedidos, extração de PDF, Excel, eh, e outros formatos.  
   
 

### 01:33:20

   
**Marcelo Costa:** Então, coisa que, por exemplo, o cara faz lá, né? O cara tem, p\*\*\*\*, às vezes um material, hoje ele já tá bem automatizado, que tudo vai no no aplicativo dele ali, né? Eh, mas ó, agente de planejamento, otimização de pistas e slot, balanceamento de capacidade para operação, eh, otimização de rotas. Então, pô, ele tá olhando para transporte aqui, né? Mas, por exemplo, você pode ver, pô, otimização de rota de dos caras de obra. Pô, se tem uma obra que tá aqui nesse nesse momento, a outra tá lá em tal momento, essa otimização pro cliente é uma é um negócio que com certeza os caras fazem isso já, mas não devem usar IA no no total, né? Fala: "Pô, você tá indo com, sei lá, fio não sei o que para aquela obra, velho. Você tem outras três que estão lá, não sei o quê. Você deveria fazer uma outra alternativa aqui para você otimizar essa rota. tratamento de exceção, detecção automática de atraso, sugestão e remarcações e notificações automáticas das partes interessadas. Ou seja, ele faz detecção, classifica os atrasos em tempo real, notificação inteligente, né? Então, por, pô, o cara consegue mapear isso também em tempo real, né?  
   
 

### 01:34:37 {#01:34:37}

   
**Marcelo Costa:** Por que a obra tá, por que que tá atrasada, por que que o negócio não tá andando? algumas detecções que o cara demora para ver só no relatório lá na frente que aconteceu, que ele poderia tá tomando ação em tempo real, né? Então isso pode ser um também um ponto. e agentes de atendimento ao cliente. Respostas instantâneas sobre status, remessa e documentos. Suporte ao cliente 24x7, resposta contextual com base nos dados, compreensão consultiva e linguagem natural. Então assim, é é assim, é mais ou menos isso, né? uma camada, velho. Nós vamos pegar seus dados e vamos trazer insite, trazer automação pro por processo,  
**Off Digital:** Sim.  
**Marcelo Costa:** né?  
**Off Digital:** É, cara, é é muito grande o que dá para fazer em termos de possibilidade. O que a gente tem que pensar é e fragmentar esse valor de uma forma que a gente consiga colocar em meses um crescimento desse projeto, entendeu? Então, a gente tentar mostrar pro cara, ó, isso aqui é o objetivo final, a gente vai destrinchar esse trabalho em meses para eles irem sentindo o valor dessas mudanças passo a passo e incorporando isso. Porque se a gente vem e p\*\*\*\*, vamos criar um negócio aqui, vamos te transformar numa numa Google,  
**Marcelo Costa:** Ne.  
   
 

### 01:35:56 {#01:35:56}

   
**Off Digital:** aonde todo mundo  
**Marcelo Costa:** Bom, e até a gente,  
**Off Digital:** entendeu?  
**Marcelo Costa:** né, primou assim, beleza, mas como é que faz isso aqui, né, velho? Vamos lá, nós vamos ter que estudar, nós vamos cair para cima,  
**Off Digital:** É,  
**Marcelo Costa:** nós vamos, então não dá para sair prometendo que dá para falar assim, cara, hoje nós estamos construindo até podemos mostrar,  
**Off Digital:** isso é o que a gente mapeou.  
**Marcelo Costa:** né, o que a gente tá  
**Off Digital:** Isso é o que a gente mapeou. Isso é o que a gente mapeou,  
**Marcelo Costa:** fazendo.  
**Off Digital:** identificou que a gente consegue atacar. Qual que é o timeline disso?  
**Marcelo Costa:** Como é,  
**Off Digital:** Ne.  
**Marcelo Costa:** como é o formato disso também? discutir, porque a gente, o que a gente tá fazendo é produto pra gente, né? Pode ser consultoria,  
**Off Digital:** Aham.  
**Marcelo Costa:** pode ser. Aí a gente pode pensar,  
**Off Digital:** Sim.  
**Marcelo Costa:** né?  
**Off Digital:** Exato. Se a gente vai criar, se a gente vai criar esse esse produto e vai entregar para eles funcionando ou se a gente vai implementar em cima do da estrutura deles, né? O que no fim das contas para pra gente não faz tanta diferença, porque o que a gente implementa para eles vai tá salvo para pra gente, então pode virar um produto para fora.  
   
 

### 01:36:59 {#01:36:59}

   
**Off Digital:** Agora, eh, tem o peso também do financeiro, né? Então, se a gente vai criar um produtos em cima da estrutura dele 100% customizado,  
**Marcelo Costa:** que a gente não vai utilizar para as outras coisas.  
**Off Digital:** se supõe exclusivo, se supõe que é um trabalho mais caro,  
**Marcelo Costa:** né?  
**Off Digital:** né? Porque se a gente tá tem, já criou o produto, tá disponibilizando para eles, né?  
**Marcelo Costa:** É, se é um negócio personalizado que vai, ele que vai usar é outra coisa, né?  
**Off Digital:** Exato.  
**Marcelo Costa:** Agora é pensar aí também nessa questão de dados que eu acho que é, p\*\*\*\*, vamos lá, vou criar uma base aqui para começar a entregar uns insightes pro cliente dele. Cara, nós vamos começar a mastigar dados da equatorial que é que a gente garante que esse dado tá tá sendo tratado dentro de casa, né? Então essa é uma preocupação, tanto o cara para uma reunião com a gente assinou o NDA porque ia abrir dois detalhes dos clientes. Então isso com certeza é uma preocupação que é geral também de o cara quando vai botar qualquer processo  
**Off Digital:** Ah.  
**Marcelo Costa:** de IAP para dentro de casa, onde é que eu trato, né? Tô jogando isso para uma LLM. Então, talvez, eu acho que esse é um outro ponto de de se atacar no geral, que é a criação das LLMs internas, entendeu, pra  
   
 

### 01:38:25 {#01:38:25}

   
**Off Digital:** É,  
**Marcelo Costa:** empresa.  
**Off Digital:** mas aí aí é muita aí primiel o buraco é muito muito embaixo.  
**Marcelo Costa:** Mas não, não acho que embaixo. Eu acho que é se e e bobear é simples, velho, que é a questão de assim você pegar o o negócio e e travar ela dentro do servidor, entendeu? você travar, você bota um um uma LLM trabalhando, você tem um monte que você baixa que ela trabalha  
**Off Digital:** Não,  
**Marcelo Costa:** offline.  
**Off Digital:** mas aí para você chegar no nível de resultado que você tá imaginando, você precisa de muito poder computacional. muito  
**Marcelo Costa:** Eh, depende, depende, depende. Eu acho, cara, eu vi, eu vi alguns casos aí que os caras estão titulou, cara. É basicamente você falar assim, eh, você travar ele como se botasse o GPT lá ou um notebook LM que você fala, você vai trabalhar só com esses dados aqui. Isso aqui é interno. Isso aqui você não tá jogando para fora, entendeu? Para consultar. você só tá usando e essa base que você tá trabalhando, você não tá trabalhando informação externa e e conectando, né? A Dávio tinha conversado uma vez, a gente falou sobre isso da ele falou que tinha umas coisas de plugar LLM interna que ela que ela produz bem também, que eu acho que é uma preocupação das empresas.  
   
 

### 01:39:50 {#01:39:50}

   
**Marcelo Costa:** Com certeza vamos cair nisso, né?  
**Off Digital:** Sim, mas eu acho que é cedo ainda, primo. Assim, cara, eu sigo uns caras aí que tão tão trabalhando a nível corporativo e nego tá instalando 300, 500 OpenCloud em empresa aí, velho. E tá empresa grande, empresa séria e tá rolando e é isso, entendeu? NVIDIA, tem a malha da Nvidia lá para corporativo que ela lançou só pro OpenCloud que você instala lá o negócio da Nvidia e ele e ele faz uma um um audit lá de segurança que trata os dados e cara, tem muita coisa. Só que a gente só vai cair, só que a gente só vai cair para dentro sob demanda,  
**Marcelo Costa:** É,  
**Off Digital:** entendeu? Não vó, p\*\*\*\*, ficar me pesquisando e  
**Marcelo Costa:** é, é. E entrando e imaginando o que o cara quer.  
**Off Digital:** vendo.  
**Marcelo Costa:** Nós precisamos falar com as pessoas, né, velho? É isso. Não adianta também a gente ficar supondo, tem que ver o momento do cara, o que que ele tá querendo pra  
**Off Digital:** É, eu acho que se o cara entrar nesse papo, velho, de ah, como é que é a segurança dos dados? Aí a gente joga, a gente a gente dá um uma objeção nele de, tipo assim, ó, cara, a segurança dos dados, a gente tem várias camadas, vários níveis para trabalhar, né?  
   
 

### 01:40:59

   
**Off Digital:** Aí a gente vai te oferecer, a gente fechando a solução, a gente vai te oferecer níveis de compliance, de segurança dos teus dados, que aí o que vai definir é o quanto você vai ter de budget para segurança. Você vai ter de um nível mais simples um nível mais avançado de secir dos dados.  
**Marcelo Costa:** A gente é,  
**Off Digital:** É isso aí.  
**Marcelo Costa:** pode é fala,  
**Off Digital:** Você você já joga o negócio para depois, entendeu? Tipo aqui, ó, cara,  
**Marcelo Costa:** cara, tem que analisar o que que você quer dividir de dados e tal,  
**Off Digital:** a gente tem todos,  
**Marcelo Costa:** a gente entender como estava, depois a gente montar um plano.  
**Off Digital:** é, a gente tem tem a gente tem níveis para trabalhar com isso, cara, do nível mais sofisticado ao nível mais simples. Aí a gente vai entender quais dados vão ser tratados e e o quão eh o o quanto de eh confidencialidade e blindagem você quer para esses dados, né? Se você quiser blindagem máxima, vai ter o custo de blindagem máxima. Se você quiser blindagem média, é o custo de blindagem média. Blindagem simples é o custo de blindagem simples,  
**Marcelo Costa:** É. E e você, p\*\*\*\*,  
**Off Digital:** né?  
**Marcelo Costa:** agora um open cloud trampando para você dentro da sua empresa é outra parada, né, velho?  
   
 

### 01:42:07 {#01:42:07}

   
**Marcelo Costa:** É maor, p\*\*\*\*. É o que eu que eu digo, cara.  
**Off Digital:** Entendeu?  
**Marcelo Costa:** O meu aqui eu fiz eu botei umas atualizações aqui para ele ficar para sempre ele salvar o meu trabalho no cloud, no memory diário lá no Git e e qualquer trabalho dele também aqui, todas. p\*\*\*\*, velho, ele tá máquina, velho. Onde você falar, ele tá sabendo, velho. Pedi aqui uns e-mail, p\*\*\*\*, pega lá meu drive, não sei o quê, cara. Tem não sei o qu no drive. Recebi um e-mail, dá uma olhada no e-mail, faz um e-mail para esse cara, mas assim e é pro cara da Noruega, não sei o quê, cara. Ele destroçou, velho. Meteu o e-mail já com os link, com os negócios, ó, tal, pá, pá, pá. Tirei essa abordagem, falei: "p\*\*\*\*, velho, top". Isso é vida, né, velho? É o cara que tem  
**Off Digital:** Não, e olha que a gente tá investindo pouquíssimo tempo, né, velho? É o que eu tô falando. Eu tô há três semanas,  
**Marcelo Costa:** 200\.  
**Off Digital:** velho, debruçado só nos projetos para mais, velho.  
   
 

### 01:43:02 {#01:43:02}

   
**Off Digital:** Acho que eu tô um mês aí que eu não mexo em nada de setup. É só projeto, projeto, projeto, projeto. Quando eu parar aqui, que eu afinar minhas skills, que eu afinar meu setup, que eu afinar obsídia, que eu afinar os bagulho, aí já é pum, mais um nível, entendeu?  
**Marcelo Costa:** É.  
**Off Digital:** Porque o que eu eu tô só juntando material,  
**Marcelo Costa:** E eu  
**Off Digital:** velho. Todo dia eu tô vendo tudo que tá saindo,  
**Marcelo Costa:** é,  
**Off Digital:** separando, selecionando, mas eu não tenho tempo, velho, porque eu vou parar para  
**Marcelo Costa:** eu não sei, eu fico pensando, cara, se eu queria me envolver em pegar um projeto com com uma empresa assim,  
**Off Digital:** fazer  
**Marcelo Costa:** tá ligado? Porque, cara, eu sei como é que, você vê, eh, eh, neguinho fica na cola, tipo, o o Marcelo aqui, eu falei que ia desenvolver, o cara já tá E aí quando me apresenta, cara, cadê o negócio? Os caras estão usando aqui, queria usar já o novo não sei o quê, cara. É uma pressão que que p\*\*\*\*  
**Off Digital:** Uhum.  
**Marcelo Costa:** nem tem essa pressão do cara aqui, porque é meu meu brother aqui  
**Off Digital:** Sim,  
**Marcelo Costa:** agora.  
**Off Digital:** mas a gente tem que ter um cara na nessa linha de frente futuramente para trabalhar com isso.  
   
 

### 01:44:01

   
**Off Digital:** Tem o cara da, o cara que vai ficar sob pressão, velho, é o, é o R, não é a gente, entendeu? Tem que ter um red ali na  
**Marcelo Costa:** É aí. Aí vamos lá, reflexão. Vamos falar, pô,  
**Off Digital:** frente.  
**Marcelo Costa:** o cara fech vai fechar um negócio com nós ele quer fazer, velho. Vai falar, ó, vamos começar um desenho, vou pagar R$ 20.000 por mês para vocês. Beleza,  
**Off Digital:** Aham.  
**Marcelo Costa:** vai demandar. Se a gente gastar um tempo com as minas, a gente ó, eu tô botando 10 aqui num marquinha de arroz. Se nós gastar tempo, nós bota 50 em vez de 20 com o tempo que nós vamos gastar lá com o cara, entendeu?  
**Off Digital:** Sim,  
**Marcelo Costa:** Lógico, é um crescimento profissional para nós olhar e ver e a mão,  
**Off Digital:** sim, sim, sim,  
**Marcelo Costa:** mas mas eu fico eu eu fico um pouco  
**Off Digital:** sim.  
**Marcelo Costa:** nessa nessa dúvida, velho,  
**Off Digital:** Cara, eu eu também.  
**Marcelo Costa:** de  
**Off Digital:** E você vai ver que o bagulho é mais embaixo, né? Quando você vai fazer mesmo, tipo, no detalhe do detalhe do detalhe, é muito detalhe,  
**Marcelo Costa:** vê aí, velho.  
   
 

### 01:44:59

   
**Marcelo Costa:** E como, né,  
**Off Digital:** mas  
**Marcelo Costa:** onde nós estamos agora aí é coisa, velho, para fazer. É um mês trampando e tem coisa,  
**Off Digital:** não,  
**Marcelo Costa:** velho.  
**Off Digital:** mano, tem uns dois meses aqui já para mim. E mas assim,  
**Marcelo Costa:** É.  
**Off Digital:** beleza, cara. A gente tá fazendo um negócio do zero a gente grande, né, também. Então tem que entender que assim, beleza, mas todas as frentes, né, mano? Tá fazendo layout,  
**Marcelo Costa:** Isso aí,  
**Off Digital:** tá fazendo negócio.  
**Marcelo Costa:** isso aí era projeto de um ano no mínimo, assim,  
**Off Digital:** Não,  
**Marcelo Costa:** no  
**Off Digital:** isso aqui é projeto para várias pessoas,  
**Marcelo Costa:** mínimo.  
**Off Digital:** né, mano? Não v o projeto, pô, estamos tocando em dois aqui, sendo que  
**Marcelo Costa:** É, tocando em dois, não tá tocando aí,  
**Off Digital:** tipo,  
**Marcelo Costa:** né? Tô só dando o pitaco, né?  
**Off Digital:** é, mas tudo eu tenho que conferir com você. Imagina se eu não tivesse ninguém para conferir como é que qual a base, né, de  
**Marcelo Costa:** É, ou você tivesse, pô, tem que falar com o cliente, tem que falar, eu já tô trazendo isso mastigado e tal,  
**Off Digital:** tipo  
**Marcelo Costa:** mas tem todas essas, você pensar que você tá dois, mas para esse negócio chegar nisso aí já foi, eh, eu já botei um um MVP lá rodando, eu já vi as dor, não sei o quê,  
   
 

### 01:46:06 {#01:46:06}

   
**Off Digital:** exato.  
**Marcelo Costa:** eu tô eu tô eu tô eu tô um  
**Off Digital:** Se fosse do zero, do zero, mano, ia ser muito mais, entendeu?  
**Marcelo Costa:** ano aí, eu tô um ano aí pra gente chegar nesse ponto pensar é um ano já. Lógico que não foi não foi uma linha reta,  
**Off Digital:** Exato.  
**Marcelo Costa:** né? Definir, vamos para cima, já temos o time, não foi indo, né? Mas é uma é umas crise  
**Off Digital:** V3 do gold con dados. V3 para ser fonte de verdade. Admin home admin vai para usuários operacional não visível legada. Beleza, isso aqui tudo foi comitado, então vamos ver aqui já o que tem de mudança, tá? Vamos ver aqui quando eu aprovo. Então vamos pegar aqui Alfredini  
**Marcelo Costa:** Eu tô  
**Off Digital:** NR37.  
**Marcelo Costa:** vendo só sua tela do Cláudio aí. Depois você quiser dividir essa sua  
**Off Digital:** Eu  
**Marcelo Costa:** aí. Ele comentou para mim também.  
**Off Digital:** acho que sim. Ele fez o deploy já. Eh, ó, inclusive a recomendação da IA parece que já tá dando a mensagem também, ó. Decisão automática não confere. NR37 básico não substitui curso complementar de Guindast. Decisão automática não confere.  
   
 

### 01:47:44 {#01:47:44}

   
**Off Digital:** NR37 básico não substitui movimentação de cargas. Documento conforme. Esse aqui tá validado que tá aqui.  
**Marcelo Costa:** Hum.  
**Off Digital:** Mas beleza. Ele tá mandando todos para cá. É  
**Marcelo Costa:** Declaração, a decisão automática não confere.  
**Off Digital:** isso.  
**Marcelo Costa:** Treinamento básico, plataforma não substitui com marc. Não, isso é outra.  
**Off Digital:** Tá, vamos pegar um documento fácil aqui. Vamos pegar aqui NR37. Ele tá em parcial, certo?  
**Marcelo Costa:** tá parcial, por isso que ele tá aí,  
**Off Digital:** parcial.  
**Marcelo Costa:** né?  
**Off Digital:** Beleza? Então, se eu aprovar, ele tem que ir para confere, né? NR37. Aprovei. Vamos ver então aqui. Na verdade, eu nem preciso vir nos candidatos. Se eu clicar aqui no Alfredin ele já vai.  
**Marcelo Costa:** Hum.  
**Off Digital:** Então, NR37 tá OK.  
**Marcelo Costa:** Isso é avançado. Tem várias aí, né? Tem,  
**Off Digital:** Tem  
**Marcelo Costa:** ó, supementar paraindast,  
**Off Digital:** vários.  
**Marcelo Costa:** ela já não tá mais aí, né?  
**Off Digital:** Tá. Vamos pegar aqui uma outra então.  
**Marcelo Costa:** Pega essa 35 aí, ó. Vamos ver.  
   
 

### 01:49:16

   
**Off Digital:** Cadê ela? Treinamento básico. NR37. Aprovar.  
**Marcelo Costa:** Então essa você tinha provado já igual,  
**Off Digital:** Aprovada. Tem duas. Tá duplicado.  
**Marcelo Costa:** né?  
**Off Digital:** OK. Aprovado.  
**Marcelo Costa:** Básico ali, ó. OK. Tem um OK já básico aí, ó.  
**Off Digital:** Cadê?  
**Marcelo Costa:** Segunda fila, terceiro. Aí, ó.  
**Off Digital:** aqui.  
**Marcelo Costa:** Vamos tirar mais um aí de cima, ó. Essa é,  
**Off Digital:** É, mas aqui tá com  
**Marcelo Costa:** mas ele tá trabalha quente 34,  
**Off Digital:** oito.  
**Marcelo Costa:** ó. Tá vendo?  
**Off Digital:** Trabalho aqui de 34\. Não, mas foi a 37, né, que nós aprovamos agora aqui.  
**Marcelo Costa:** Foi 37\. Tá certo.  
**Off Digital:** Tava com oito, continua com oito,  
**Marcelo Costa:** É. E ó ela aí, ó. É, vamos tentar esse sera aí, ó.  
**Off Digital:** certo? Aqui tinha que ter o nome do documento, tá vendo?  
**Marcelo Costa:** Eh,  
**Off Digital:** Não, o nome do cara. que aqui fica difícil de achar o nome do  
**Marcelo Costa:** cima do cara, mas embaixo em vez de regra não equivalente, aí ele tem o número do documento aí também.  
   
 

### 01:50:39 {#01:50:39}

   
**Off Digital:** documento.  
**Marcelo Costa:** Qual é, né?  
**Off Digital:** Treinamento avançado. Parece que tem documento repetido aqui.  
**Marcelo Costa:** Eh, vamos subir um cara novo, primo. Vamos  
**Off Digital:** É, vamos, vamos.  
**Marcelo Costa:** apagar  
**Off Digital:** Deixa eu pegar aqui o Joel.  
**Marcelo Costa:** que esses documentos já não tão batendo com a matriz. Aí eu acho que a gente já tá, eu limparia todos esses caras e botaria um novo aí.  
**Off Digital:** Deixa eu ver aqui. Eu tô delegando pro cara aqui para fazer a limpeza. Deixa eu ver se já foi a aqui, ó, para mim. Agora a rolagem aqui,  
**Marcelo Costa:** Hum,  
**Off Digital:** ó.  
**Marcelo Costa:** boa. Pois esses documentos do cliente a gente precisa subir alguns.  
**Off Digital:** É  
**Marcelo Costa:** Aí a gente tenta testar aquela importação lá  
**Off Digital:** exato.  
**Marcelo Costa:** também. Esse bloqueio, primo, eh,  
**Off Digital:** O que que é também?  
**Marcelo Costa:** temos que ele dá, ó,  
**Off Digital:** É que eu acho que ele quando tem bloqueio é que ele não aprova automático porque tem  
**Marcelo Costa:** tem alguma regra específica? fica em cima, né? É, perfurante, ionizante e biológico. Talvez são coisas  
**Off Digital:** Exato.  
**Marcelo Costa:** diferentes.  
**Off Digital:** Serviço de saúde genérica bloqueada.  
   
 

### 01:53:43

   
**Off Digital:** Mas aqui, ó, o perfuro cortante, ele aprova proteção radiológica, ele  
**Marcelo Costa:** Então,  
**Off Digital:** aprova.  
**Marcelo Costa:** quando você for jogar na matriz, você não pode jogar ela aberta, você tem que escolher um desses, né? Agora ela,  
**Off Digital:** Exato.  
**Marcelo Costa:** por que que ela aparece? Ela não precisava nem aparecer bloqueado. Vai um aí esses dois. Tem  
**Off Digital:** É porque ela existe, existe a genérica, entendeu?  
**Marcelo Costa:** outras  
**Off Digital:** O que eu quero entender é porque que tem essas duplicatas aqui, ó. Naval genérica tem duas.  
**Marcelo Costa:** tudo que tá bloqueado,  
**Off Digital:** Geralmente é as que tá bloqueada,  
**Marcelo Costa:** tá?  
**Off Digital:** que tem duas,  
**Marcelo Costa:** É.  
**Off Digital:** as outras não tem. Mas você vê que é minoria ainda, né? Ó, limpeza urbana e todas as bloqueadas tem duplicada. Depois a gente abre um agente para entender esses bloqueios.  
**Marcelo Costa:** complicado.  
**Off Digital:** Se eu clicar aqui, tem que botar para quando clicar aqui, eh, separar por status ou por vencimento ou por carga.  
**Marcelo Costa:** É, não acho que nem tem essa necessidade não, viu primo. Precisa botar mais botão não.  
**Off Digital:** Ó, oito tá certinho. STCW também não tem um bloqueio aqui bloqueado.  
   
 

### 01:55:19 {#01:55:19}

   
**Off Digital:** Bloqueios e não equivalência sem não equivalência específicessa regra. Continua valendo bloqueio geral contra título genérico, família parecida e modalidade divergente. Quando não aprova a área automática enviar para pendente quando houver apena descrição genérica do curso marítimo. Regra SCCW ausente. Código DPC divergente certificado fora da validade calculada. Eu acho que o bloqueio é é quando ele não tem regra de aprove automático. Depois, mas depois a gente dá uma esmiçada nisso aqui.  
**Marcelo Costa:** Так.  
**Off Digital:** Eh, então beleza, a paginação tá funcionando aqui. A gente tá testando para ver se muda lá, né? Ainda não deu para entender. Eu vou pedir para ele aqui, ó.  
**Marcelo Costa:** M.  
**Off Digital:** falou que quando eu mudo aqui Alfredini para entrevista, ó, já tá funcionando. Quando eu mudo para certificação aqui, ele voltou aqui.  
**Marcelo Costa:** Mas tá usando, ele tá usando termos  
**Off Digital:** É, mas beleza, isso aí é só só mandar ele mudar o nome lá.  
**Marcelo Costa:** diferentes.  
**Off Digital:** E aqui ele tá botando vaga recrutamento, certificação, aprovação, DP, Barp. Aqui tá vaga recrutamento.  
**Marcelo Costa:** Acho que é só entre a  
**Off Digital:** Certificação aqui é aprovação entrevista DP embarque.  
   
 

### 01:56:38

   
**Marcelo Costa:** aprove.  
**Off Digital:** Aqui tá aprovação entrevista DP embarque e lá tá certificação aprovação DP embarque.  
**Marcelo Costa:** Tem uma mais, né?  
**Off Digital:** Não. 2 3 4 5 6\.  
**Marcelo Costa:** A aprovação é  
**Off Digital:** Só tá errado o nome. É aqui seria certificação,  
**Marcelo Costa:** certificação.  
**Off Digital:** aprovação, DP, embarque e lá tá certificação, aprovação, entendeu? Era para ser aprovação entrevista, mas o certo é esse, né?  
**Marcelo Costa:** Não, o certo é esse aí.  
**Off Digital:** O certo é esse  
**Marcelo Costa:** Certificação, aprovação, que aprovação é a mesma coisa que entrevista,  
**Off Digital:** DP.  
**Marcelo Costa:** né? Ele vai pra entrevista,  
**Off Digital:** Isso,  
**Marcelo Costa:** mas eu acho que a aprovação é  
**Off Digital:** isso, isso. Então,  
**Marcelo Costa:** melhor.  
**Off Digital:** só o Camban que tá errado no nome, mas se eu voltar para recrutamento aqui, ó, ele volta para recrutamento.  
**Marcelo Costa:** Ótimo.  
**Off Digital:** Se eu voltar pra vaga, ele volta pra vaga.  
**Marcelo Costa:** Maravilha.  
**Off Digital:** Depois tem que botar para mudar automático também que ainda não  
**Marcelo Costa:** Eu eu não mudaria agora,  
**Off Digital:** tá.  
**Marcelo Costa:** não. Deixa os caras usar.  
**Off Digital:** É coisa, né, primo?  
**Marcelo Costa:** É,  
**Off Digital:** É coisa,  
   
 

### 01:57:59 {#01:57:59}

   
**Marcelo Costa:** mas deixa, eu deixaria os cara usar, entendeu?  
**Off Digital:** velho.  
**Marcelo Costa:** Para ver. O cara vai passando manual até que os caras vão entendendo o processo,  
**Off Digital:** Sim.  
**Marcelo Costa:** né?  
**Off Digital:** Vamos ver aqui. Mandei no cloud aqui para ele zerar os dados. Não foram os dois comidos ainda estão só na na branch. É, mas ainda não subiu essa essa alteração lá não. Agora que eu vi do de mudar quando muda na revisão de mudar no detalhe ainda não subiu não. Tá,  
**Marcelo Costa:** Tá,  
**Off Digital:** eu tô deixando os bichos trampar aqui. Enquanto isso, eu tô vendo o negócio do Ralf.  
**Marcelo Costa:** beleza. Bel,  
**Off Digital:** Vamos ver aqui.  
**Marcelo Costa:** eu daqui a pouco vou ter que partir aqui porque eu tenho  
**Off Digital:** É, eu vou parar para almoçar quando você for latente. Ó, v botar o cloud aqui. M.  
**Marcelo Costa:** Ah.  
**Off Digital:** Ora Oh f\*\*\*. Nossa, agora entender, cara, esse RDO,  
**Marcelo Costa:** H L D O, né?  
**Off Digital:** RDO, né? É,  
**Marcelo Costa:** R.  
**Off Digital:** RDO é o relatório de acompanhamento da obra gerada no dia ou ou semanalmente que consolida quantas pessoas estão na obra separadas por por cargo, equipamentos presentes na obra e a quantidade de cada clima do dia ocorr ocorrências e acidentes de trabalho, faltas quando as pessoas faltaram e tempo médio de trabalho da equipe na obra.  
   
 

### 02:03:21 {#02:03:21}

   
**Off Digital:** é um padrão de mercado bem consolidado. A própria Lidiane reforçou o padrão RDO é muito parecido entre clientes, muda o layout, mas as informações são parecidas, ou seja, acomode funcionalidade no setor da construção. E ela tem esses dados, cara. Ela  
**Marcelo Costa:** ela mas lembra que ela falou que a questão do p\*\*\*  
**Off Digital:** tem  
**Marcelo Costa:** a os equipamentos na na na no coisa não consegue medir na hora, né? os equipamentos que estão na obra, não sei o quê,  
**Off Digital:** e a presença,  
**Marcelo Costa:** é a presença dos caras assim,  
**Off Digital:** né?  
**Marcelo Costa:** não é, não é online, né? Mas o cara podia botar lá, né? Com certeza o cara tem, p\*\*\*\*, eu não tenho um cartão de ponto na obra,  
**Off Digital:** O que a gente é,  
**Marcelo Costa:** não tem um RFSID que pode ser um caminho,  
**Off Digital:** é que a gente não entrou muito no detalhe,  
**Marcelo Costa:** né?  
**Off Digital:** né? A gente falou um pouco, ela explicou que é uma dor forte, explicou um pouquinho, mas a gente teria que fazer um Meet só para falar de  
**Marcelo Costa:** Não, e assim,  
**Off Digital:** RDO.  
**Marcelo Costa:** eu acho também, eu acho que ela foi bem, ela não tava brifada para isso, né? Que ela ia ter que falar sobre essas dores e tal,  
   
 

### 02:04:31 {#02:04:31}

   
**Off Digital:** Uhum.  
**Marcelo Costa:** então acho que ela também não abriu tudo,  
**Off Digital:** Uhum.  
**Marcelo Costa:** muita coisa, né? Eu acho que com ele talvez a conversa seja mais franca um pouco, né?  
**Off Digital:** Se Mas será que ele tá tão por dentro do operacional?  
**Marcelo Costa:** Ele manja, velho. O cara que construiu a parada toda. É ele que construiu de moleque. Dei de moleque na obra,  
**Off Digital:** É,  
**Marcelo Costa:** velho. Conhece para c\*\*\*\*\*\*. Ele que fez tudo. Então ele sabe.  
**Off Digital:** se depois local confirmação do candidato coluna observação. Deixa eu ver se tá funcionando mesmo. Candidato. É melhor, velho, eu compartilhar com você minha minha tela aqui do que Ah, cadê Ja.  
**Marcelo Costa:** Um ponto que não tem para mim, que seria bom é tipo excluir o  
**Off Digital:** Hum.  
**Marcelo Costa:** documento, subir.  
**Off Digital:** Sim.  
**Marcelo Costa:** Quero excluir esse documento,  
**Off Digital:** Não, na verdade tem excluir nada,  
**Marcelo Costa:** cara.  
**Off Digital:** velho. Não tem excluir candidato. Tipo, o que tá Ah, o candidato já tem.  
**Marcelo Costa:** candidato, você colocou.  
**Off Digital:** Deixa eu ver se funciona. Funciona.  
**Marcelo Costa:** É verdade. Você nem precisava pedir para excluir.  
   
 

### 02:06:33 {#02:06:33}

   
**Off Digital:** p\*\*\*, mas agora também eu não vou conseguir ver o a mudança que ele tava fazendo lá.  
**Marcelo Costa:** Vamos inserir um cara aí.  
**Off Digital:** Tem que botar para excluir o usuário também. Cadê as matrizes aqui? Vamos excluir as matrizes,  
**Marcelo Costa:** Ja.  
**Off Digital:** então. Soldador. Excluir. Excluir e a empresa. Mas não excluiu. E aí?  
**Marcelo Costa:** exclui tudo.  
**Off Digital:** Vai dar e volta. Aí já voltou.  
**Marcelo Costa:** Priminho, faz o seguinte, ó. Bota esse bicho para excluir tudo. Se você depois que puder comentar aí para eu para eu visualizar aqui, eu incluo uma matriz, vou incluir uma que eu já sei os documentos, vou criar uma aqui que eu já sei que eu tenho documento e tal e pra gente testar. E aí a gente come a gente passa por esse caminho todo de desde criação da matriz. Eu vou passar por esse caminho aqui e vou anotando aqui o que que o que que eu vi.  
**Off Digital:** Então, velho, eu quero, eu, eu, eu preciso bater. Vamos fazer o seguinte, enquanto ele exclui lá o negócio, vamos colocar o negócio aqui. Fredin  
**Marcelo Costa:** Deixa eu pegar aqui.  
**Off Digital:** Soares,  
**Marcelo Costa:** Alfredini Pinheiro de Alcântara.  
   
 

### 02:08:46 {#02:08:46}

   
**Off Digital:** p\*\*\*\*. Cadê a matriz, c\*\*\*\*\*\*? Agora não tem mais a matriz.  
**Marcelo Costa:** Cria uma e bota dois documentos, velho, que é documentos que eu sei que eu tenho dele aqui.  
**Off Digital:** Mas a matriz tá aqui, velho.  
**Marcelo Costa:** Então você tem que criar a vaga, né?  
**Off Digital:** Oh. Não tem a matriz.  
**Marcelo Costa:** Vou sair  
**Off Digital:** Vai lá,  
**Marcelo Costa:** priminho,  
**Off Digital:** primo. Eu vou almoçar aqui. A gente a gente volta aí depois  
**Marcelo Costa:** cara. Hoje eu tô, hoje eu tenho, tô enroscado com um negócio à tarde,  
**Off Digital:** ou  
**Marcelo Costa:** velho. Tem uma reunião às 2as e às 4 horas combinei com o meu sogro de ver umas paradas aqui na obra. Então, hoje vai dar uma f\*\*\*\*\*,  
**Off Digital:** tá? Deixa comigo.  
**Marcelo Costa:** velho.  
**Off Digital:** Eu vou eu vou eu tenho uma reunião 6:30 e eu vou ficar hoje 100% em cima disso. A gente tinha que preparar as coisas com o Ralf lá, mas eu  
**Marcelo Costa:** Vamos. À noite a gente fala do Ralf. Eu vou também olhar, eu olho no paralelo, a gente cruza as as ideias.  
**Off Digital:** vou  
**Marcelo Costa:** Mas, cara, vamos, eu acho que assim, eh, é bate-papo com ele, velho, trocar uma ideia, falar o que a gente tá vendo, o que que tem possibilidade, vamos tentar sugar dele mais coisa e depois a gente prepara.  
   
 

### 02:10:46 {#02:10:46}

   
**Marcelo Costa:** Não precisa, não adianta a gente ficar também se matando muito, né, velho?  
**Off Digital:** não, não, tranquilo.  
**Marcelo Costa:** Entendeu?  
**Off Digital:** Só para ter um velho.  
**Marcelo Costa:** É só para ter um caminho de conversa, né?  
**Off Digital:** Olha, tá vendo o Cloud, mano? Todo dia tá dando isso aqui para mim, mano.  
**Marcelo Costa:** Que que é API?  
**Off Digital:** Ah, erro de API, tipo, sei lá, que p\*\*\*\* é essa.  
**Marcelo Costa:** É, o meu tava meu deu uns erros de API aqui,  
**Off Digital:** Pois é, mano. Isso é tá desanimando de usar o Cloud por causa disso aí,  
**Marcelo Costa:** velho.  
**Off Digital:** viu, mano? Sei se você viu os caras fizeram a parceria com o Elon Musk lá para usar os computador dele. Você  
**Marcelo Costa:** Aí deu deu crédito para c\*\*\*\*\*\*,  
**Off Digital:** viu?  
**Marcelo Costa:** mas por talvez porque ia dar pau, né?  
**Off Digital:** Tava ia dar pau? Não, tava dando pau, mano. Tava dando pau. Não para de dar pau. Eu não tô conseguindo. Se não fosse o Codex, a gente tava parado, P. Porque se fosse depender só do do do cloud esses dias aí.  
**Marcelo Costa:** Eh,  
**Off Digital:** Mas beleza, vai lá. Eu vou eu vou eu vou aproveitar para ficar hoje bem focado aqui para resolver essas coisas direito,  
**Marcelo Costa:** tá,  
**Off Digital:** certô  
**Marcelo Costa:** eu vou est das duas agora até umas 4,  
**Off Digital:** trabalhando.  
**Marcelo Costa:** eu vou estar numa apresentação aqui da da BMV que vai mostrar lá uma plataforma nova, se ouvem falar não sei o quê, Mas é só escutando, então dá para eu interagir aí,  
**Off Digital:** Beleza,  
**Marcelo Costa:** tá? Vamos falando.  
**Off Digital:** valeu para mim.  
**Marcelo Costa:** Valeu para mim. Estamos junto.  
   
 

### A transcrição foi encerrada após 02:12:33

*Esta transcrição editável foi gerada por computador e pode conter erros. As pessoas também podem alterar o texto depois que ele for criado.*
