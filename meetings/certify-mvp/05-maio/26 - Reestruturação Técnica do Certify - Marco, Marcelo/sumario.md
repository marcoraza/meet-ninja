---
kind: sumario
project: certify-mvp
confidence: 1.00
title: "Reestruturação Técnica do Certify"
meeting_datetime: 2026-05-26T14:19:00
people: ["Marco", "Marcelo"]
tags: [kind/sumario, projeto/certify-mvp, pessoa/marco, pessoa/marcelo]
gmail_message_id: 19e65a476116a3b0
gmail_thread_id: 19e65a476116a3b0
notes_doc_id: 1AS54md4YaEmZYaZbyisWUMAIeAxiR25IckRcSnf6FVY
---

# Reestruturação Técnica do Certify

**Participantes:** Marco, Marcelo

# 📝 Observações

mai. 26, 2026

## Reunião em 26 de mai. de 2026 às 14:19 GMT-03:00

Registros da reunião [Transcrição](https://docs.google.com/document/d/1AS54md4YaEmZYaZbyisWUMAIeAxiR25IckRcSnf6FVY/edit?usp=drive_web&tab=t.jlauz34ah6kl) 

### Resumo

Reestruturação técnica do sistema Certify priorizando robustez e escalabilidade via arquitetura de agentes e desenvolvimento local.

**Arquitetura e Segurança Técnica**  
O motor Certify adotou abordagem determinística e estrutura de subagentes para garantir auditoria, segurança e resiliência no processamento. Decidiu-se centralizar o desenvolvimento no ambiente local para evitar latência e instabilidade da nuvem.

**Interface e Expansão Produto**  
A interface foi consolidada em um fluxo de admissão intuitivo com recursos operacionais avançados para gestão de documentos. O sistema possui potencial para comercialização autônoma como um produto white label.

**Estratégia e IA Corporativa**  
A equipe prioriza a estabilidade do MVP atual enquanto explora a integração de IA para automação de tarefas e análise de dados. A estratégia foca em manter uma estrutura enxuta com alta alavancagem tecnológica.

O que achou deste resumo? [Sim](https://google.qualtrics.com/jfe/form/SV_4YkxrBAaiTVqYCi?isGoogler=false&isHelpful=true) ou [Não é útil](https://google.qualtrics.com/jfe/form/SV_4YkxrBAaiTVqYCi?isGoogler=false&isHelpful=false)?

### Próximas etapas

- [ ] \[Off Digital\] Apresentar relatório comparação: Apresentar o relatório de comparativo entre o fluxo do N8N e o motor Certify para detalhar os pontos de melhoria identificados.

- [ ] \[Off Digital\] Atualizar layout revisão: Redesenhar o layout da interface de visualização de informações dos documentos na tela de revisão.

- [ ] \[Off Digital\] Integrar LLM interface: Configurar um modelo de linguagem na interface do chat para processar as informações dos documentos.

- [ ] \[Off Digital\] Confirmar exportação: Verificar se a exportação de documentos contempla somente itens validados.

- [ ] \[Off Digital\] Implementar upload em massa: Criar funcionalidade para upload geral de documentos na interface de revisão.

- [ ] \[Marcelo Costa\] Testar exportação: Validar o comportamento do sistema ao exportar pacotes de arquivos.

- [ ] \[Off Digital\] Recomendar perfis Twitter: Enviar lista de usuários recomendados para seguir na plataforma Twitter.

- [ ] \[Off Digital\] Preparar demonstração recrutamento: Finalizar os ajustes no motor de busca e configurar uma demonstração com dados simulados.

- [ ] \[Marcelo Costa\] Testar fluxo recrutamento: Executar testes práticos no sistema de recrutamento assim que o acesso for liberado.

- [ ] \[Marcelo Costa\] Realizar transferência financeira: Efetuar o pagamento do valor combinado assim que os recursos financeiros estiverem disponíveis.

- [ ] \[O grupo\] Reunião acompanhamento: Realizar uma reunião de alinhamento na quinta-feira para revisar o progresso das atividades.

### Detalhes

* **Problemas técnicos e latência**: Foi discutido o desafio contínuo com a lentidão dos serviços de nuvem, especificamente o Cloud, que tem apresentado comportamento instável e latência elevada, levando os participantes a desenharem novas estruturas para migrar parte do processamento para evitar dependência total ([00:00:00](#00:00:00)).

* **Processo de desenvolvimento e ambiente local**: Para evitar atrasos no ciclo de implantação, a decisão foi tomada de trabalhar inteiramente no ambiente local (localhost) em vez de realizar deploys constantes, o que economiza tempo e recursos de infraestrutura ([00:02:51](#00:02:51)).

* **Refatoração do frontend**: O design da aplicação foi reestruturado para fragmentar as telas em componentes independentes, permitindo que cada tela gerencie seu próprio roteamento e funcionalidades, o que reduz o risco de quebrar o sistema ao realizar alterações específicas ([00:02:51](#00:02:51)).

* **Automação de agentes e testes**: Foi implementada uma arquitetura de agentes autônomos que inclui um supervisor e subagentes encarregados de validar o código, executar testes e questionar as próprias decisões, permitindo que o processo rode por longos períodos sem intervenção manual ([00:05:35](#00:05:35)).

* **Comparação com o N8N e evolução do produto**: Foi feita uma análise do fluxo do N8N comparando-o com a nova arquitetura do "Certify", destacando que a nova estrutura evoluiu de um MVP para um produto construído com critérios mais rigorosos de engenharia e processamento ([00:06:30](#00:06:30)).

* **Arquitetura de subagentes**: O sistema foi configurado para invocar "esquadrões" de agentes específicos para cada parte do plano de desenvolvimento, preservando o contexto e garantindo que cada agente cumpra um papel definido dentro do processo de execução ([00:09:53](#00:09:53)).

* **Sincronização de repositórios**: Para manter a consistência entre diferentes ambientes (como Codex e Cloud), os participantes utilizam um repositório central ("Agent Hub") que sincroniza configurações e skills, garantindo que mudanças no Cloud sejam refletidas no Codex ([00:15:09](#00:15:09)).

* **Auditoria técnica do motor Certify**: Foi realizada uma revisão detalhada do motor Certify comparando-o ao fluxo anterior, identificando falhas críticas de segurança, como chaves de API expostas em texto simples e falta de autenticação em webhooks, as quais foram corrigidas na nova versão ([00:17:19](#00:17:19)).

* **Lógica determinística vs. LLMs**: O sistema migrou para uma abordagem determinística para a comparação de documentos, evitando a dependência exclusiva de LLMs, o que garante que a mesma entrada sempre produza o mesmo resultado, essencial para a escalabilidade e auditoria ([00:20:54](#00:20:54)).

* **Regras e catálogo de documentos**: A nova estrutura utiliza tabelas de regras de conformidade (compliance rules) e equivalências catalogadas, permitindo que ajustes sejam feitos via banco de dados sem a necessidade de reescrever prompts ou reconfigurar o motor em tempo de execução ([00:22:39](#00:22:39)).

* **Histórico de decisões e auditoria**: Diferente do sistema anterior que sobrescrevia decisões, o novo motor mantém um histórico eterno de todas as decisões, permitindo que auditorias identifiquem exatamente quem decidiu e por que, utilizando códigos de razão (reason codes) padronizados ([00:24:56](#00:24:56)).

* **Gerenciamento de filas e resiliência**: O sistema abandonou o processamento sequencial que travava em caso de erro, adotando uma estrutura de jobs no PostgreSQL com workers paralelos e mecanismos de "heartbeat" para reprocessar jobs travados sem duplicar resultados ([00:25:47](#00:25:47)).

* **Reconciliação e revisão humana**: Foi implementada uma camada de reconciliação onde múltiplos modelos de LLM atuam em paralelo, e um terceiro modelo atua como juiz; além disso, foi criada uma tela dedicada para revisão humana obrigatória em casos de pontuação ambígua ([00:26:57](#00:26:57)).

* **Análise do impacto da mudança**: A transição para o novo modelo sacrificou parte da agilidade trivial de mudanças do N8N em prol de uma maior segurança e robustez, eliminando falhas de pré-produção como falta de observabilidade e custo não controlado ([00:29:49](#00:29:49)).

* **Redesign da tela de admissão**: A interface do sistema foi consolidada, integrando funcionalidades de documentos pessoais, formulários e KYC em uma única área de "Admissão", facilitando a gestão operacional ([00:36:53](#00:36:53)) ([00:39:00](#00:39:00)).

* **Interface de admissão e fluxos**: O novo design introduziu uma interface colapsável para as 11 etapas do processo de admissão, melhorando a experiência de navegação e permitindo o controle de progresso do candidato de forma mais intuitiva ([00:40:00](#00:40:00)).

* **Gestão de links e comunicação**: O sistema agora permite gerenciar links de candidatos (expiração, revogação) e agendar lembretes automatizados via WhatsApp e e-mail com mensagens personalizáveis, otimizando o follow-up operacional ([00:42:35](#00:42:35)) ([00:44:44](#00:44:44)).

* **Revisão e exportação de documentos**: Foi implementada uma funcionalidade para revisão de documentos que permite solicitar reprocessamento, aprovar com observação ou rejeitar com justificativa, além de opções para exportar documentos validados (zip) ([00:46:32](#00:46:32)).

* **Perspectiva de produto e expansão**: Os participantes concordaram que o novo fluxo de admissão possui valor como um produto autônomo, podendo ser ofertado para operações que necessitam de processos de contratação e documentação sem depender estritamente dos certificados de marítimos ([00:51:02](#00:51:02)) ([00:59:08](#00:59:08)).

* **Estratégia de implantação**: A estratégia definida é manter o foco na estabilidade do MVP atual, deixando funcionalidades complexas de upload em lote para uma fase posterior, priorizando o uso do sistema em produção para coletar feedback antes de novas expansões ([00:56:51](#00:56:51)).

* **Desenvolvimento de Software de Admissão (White Label)**: Off Digital sugere a criação de uma versão "white label" da ferramenta de admissão, removendo o código da aba atual, duplicando-o e adaptando o design para comercialização como um novo produto. Marcelo Costa concorda com essa estratégia, enfatizando que essa é a direção a ser seguida ([01:00:00](#01:00:00)).

* **Análise do Modelo de Negócios do G4**: Marcelo Costa analisa o modelo de negócios do G4, observando o uso de grandes eventos para vendas, com preços de entrada elevados (exemplo: 12 parcelas de 2.997). Eles destacam a transição do G4 para o conceito de "G4 OS", que utiliza anamnese para sugerir trilhas personalizadas de treinamento em vez de cursos avulsos, além de integrar CRM e ERP para consolidar dados corporativos e atuar como um copiloto baseado em um grande volume de dados de empresas ([01:03:23](#01:03:23)).

* **Visão sobre Estrutura Empresarial e IA**: Marcelo Costa expressa o desejo de manter uma estrutura de empresa enxuta, com poucos agentes, em vez de escalar para uma organização massiva ([01:05:35](#01:05:35)). Ambos concordam que existe uma distinção clara entre profissionais que utilizam ferramentas avançadas de IA (como Cloud Code, Cursor, ChatGPT, Gemini, Grok) e aqueles que não as utilizam, sendo que a primeira categoria possui uma vantagem competitiva significativa no mercado atual ([01:06:30](#01:06:30)).

* **Nível de Competência Técnica**: Off Digital e Marcelo Costa comparam seu nível técnico com o de Alan, do G4. Off Digital afirma estar em um nível de competência similar, atribuindo essa habilidade a uma bagagem prévia em produção musical, que exigia o uso constante de terminais e ferramentas complexas para instalação de sistemas ([01:07:56](#01:07:56)).

* **Ferramentas de Desenvolvimento e Custos**: Off Digital relata o uso de ferramentas de IA para desenvolvimento, mencionando um gasto de 36% do plano do Codex nos últimos 7 dias (com uso de 7 bilhões de tokens) e 24% do plano do Grok ([01:10:33](#01:10:33)).

* **Automação de Marcadores do Twitter**: Off Digital está desenvolvendo uma ferramenta que utiliza uma Interface de Linha de Comando (CLI) e a API do Twitter para extrair marcadores (bookmarks) a cada 24 horas. O objetivo é transformar esses salvos em um formato de jornal estruturado em português, utilizando Modelos de Linguagem de Grande Escala (LLMs) para adicionar diagramas, insights e permitir o treinamento de agentes como o Claude para replicar a voz do usuário em futuras comunicações ([01:12:47](#01:12:47)) ([01:19:09](#01:19:09)).

* **Desenvolvimento do Projeto "Marco OS"**: Off Digital descreve o desenvolvimento paralelo do "Marco OS", onde utilizam IA para gerar modelos (mockups) de interface em HTML e variações de abas. O foco atual do desenvolvimento está na aba de agentes do sistema ([01:20:41](#01:20:41)) ([01:26:21](#01:26:21)).

* **Configuração de Hardware e Equipamentos**: Os participantes discutem seus setups de trabalho, mencionando o uso de teclados mecânicos compatíveis com Mac, a preferência pelo trackpad em vez de mouse convencional, e a integração de dispositivos como iPad e computadores. Off Digital menciona o uso de um MacBook Pro com chip M1, adquirido há aproximadamente quatro anos e meio ([01:21:40](#01:21:40)) ([01:24:21](#01:24:21)).

* **Próximos Passos e Administração**: Em relação à ferramenta de admissão, Off Digital planeja finalizar os testes do motor, remover os candidatos de teste, e preparar uma demonstração com dados simulados (mock) para apresentar a Marcelo Costa. Eles combinam de se falar novamente na quinta-feira para testar o fluxo completo. Marcelo Costa menciona que está aguardando o recebimento de fundos para auxiliar com as despesas mensais ([01:26:21](#01:26:21)).

*Revise as anotações do Gemini para checar se estão corretas. [Confira dicas e saiba como o Gemini faz anotações](https://support.google.com/meet/answer/14754931)*

*Como está a qualidade de **destas observações?** [Responda a uma breve pesquisa](https://google.qualtrics.com/jfe/form/SV_9vK3UZEaIQKKE7A?confid=uoimMbQnRIUX-Lro-itmDxIROAIIigIgABgFCA&detailid=standard&screenshot=false) para nos dar seu feedback, incluindo o quanto as observações foram úteis para o que você precisa.*

# 📖 Transcrição

26 de mai. de 2026

## Reunião em 26 de mai. de 2026 às 14:19 GMT-03:00 \- Transcrição

### 00:00:00 {#00:00:00}

   
**Off Digital:** О.  
**Marcelo Costa:** É is doideira, hein,  
**Off Digital:** Doideira, primo.  
**Marcelo Costa:** primão?  
**Off Digital:** Eu tive que trocar do o da agência aqui, velho. Senão ele não pega.  
**Marcelo Costa:** Não grava as  
**Off Digital:** É,  
**Marcelo Costa:** parada  
**Off Digital:** eu montei um pipelinezinho automático aqui e aí ele depende de de ir pro meu e-mail desse Gmail, tá ligado?  
**Marcelo Costa:** para ele sugar e fazer o corre.  
**Off Digital:** É, ele já pega de lá, já ativa todo o resto do os  
**Marcelo Costa:** do  
**Off Digital:** pruxinho.  
**Marcelo Costa:** Fruxo.  
**Off Digital:** E aí, fritando as mente aí,  
**Marcelo Costa:** p\*\*\*\*,  
**Off Digital:** primo?  
**Marcelo Costa:** tô aqui xingando o Cloud. O Cloud tá lento, tá devagar esse f\*\*\*\*\*\*\*\*\*\*\*\*.  
**Off Digital:** Para toda hora,  
**Marcelo Costa:** É, velho,  
**Off Digital:** né?  
**Marcelo Costa:** tá lento, lento, velho. E aí falando umas m\*\*\*\*\*, respondendo igual uma mula.  
**Off Digital:** Tá horrível, mano. Cloud.  
**Marcelo Costa:** p\*\*\*\*, velho. GPT no chat tá melhor que ele. v\*\*\*\*\*\*\*\*\*\*\*.  
**Off Digital:** Não vou te falar, mano. Se eu tivesse dependendo do  
**Marcelo Costa:** Não, eu vou ter que,  
**Off Digital:** Cláudio,  
**Marcelo Costa:** eu já, já desenhei a estrutura aqui para mudar dele e vou ter que  
   
 

### 00:02:02

   
**Off Digital:** é de ver.  
**Marcelo Costa:** fazer.  
**Off Digital:** Tem dia que o bicho tá bom, velho. Aí eu aproveito. Mas, mano, ó, para você ter ideia, essa semana eu morri com 50% do Cloud.  
**Marcelo Costa:** É, e eu tô deixando ordem para ele agora. Agora tem hora que ele vai e gira,  
**Off Digital:** Semox  
**Marcelo Costa:** né? Não, agora ele começou a girar legalzinho aqui numa tarefinha que eu dei para ele aqui.  
**Off Digital:** para você ver, velho. Resetou tem dois dias já. Eu tô com 36  
**Marcelo Costa:** E ele é máquina. Eu testei aqui,  
**Off Digital:** usado.  
**Marcelo Costa:** velho. Ele é muito rápido. Bateu o dedo, ele parece nem deu tempo dele ler, velho.  
**Off Digital:** É outra, é outra pegada,  
**Marcelo Costa:** É. Tá,  
**Off Digital:** priminho.  
**Marcelo Costa:** tá. Agora em outra pegada, né? Daqui a pouco os cara volta, né?  
**Off Digital:** Isso é isso aí. É, tem que tem que tá dos dois lados. No lado que tá ganhando, a gente a gente vira pro lado que tá ganhando.  
**Marcelo Costa:** Isso que a estrutura é a estrutura tem que tá pronta para poder jogar todo mundo,  
**Off Digital:** É, é exato.  
   
 

### 00:02:51 {#00:02:51}

   
**Marcelo Costa:** né?  
**Off Digital:** Não vou ficar de de conversa fiada não. Ô priminho. Eh, beleza, velho. Hoje eu vou ter que sair mais ou menos umas 3 e 3:30, 3:40 no máximo ali, mas hoje é mais para te dar um follow-up aqui.  
**Marcelo Costa:** Tranquilo.  
**Off Digital:** Eh, cara, tô trabalhando bastante. Peguei uma, eu até derrubei lá o o que tava no ar. Eu tô trabalhando tudo no local agora. Tô trabalhando tudo local host porque não,  
**Marcelo Costa:** Sim, para não ter que ficar comentando toda hora, né?  
**Off Digital:** mano, tá louco. Tava me atrasando demais, velho. Mandando tudo pro pro site lá e gastando uma porrada de GitHub, Versel, enfim. Aí eu derrubei, tô tô trampando tudo no local. Eh, fiz um trampo grande ontem, velho, com Codex de que que acontece quando eu fiz o o o design, ele ele meio que criou todas as telas endereçadas num só componente, ou seja, é um componente que roteia tudo. Agora eu fragmentei, então todas,  
**Marcelo Costa:** Certo.  
**Off Digital:** cada tela tem um roteamento específico, eh, e cada tela responde por si por si só. Ou seja, se eu preciso mudar alguma coisa numa tela X, ele não corre risco de quebrar nenhum outro endereçamento de  
   
 

### 00:04:21

   
**Marcelo Costa:** Ele não tá,  
**Off Digital:** nada.  
**Marcelo Costa:** ele não tá amarrado junto com alguma outra ponta, né?  
**Off Digital:** É. Aí, cara,  
**Marcelo Costa:** Tem um conector que faz esse esse connecto,  
**Off Digital:** foi sim.  
**Marcelo Costa:** mas cada tipo é tipo os botão, cada botão o seu componente sozinho.  
**Off Digital:** É, antes era tipo assim, chega a API ou chega alguma função nesse bloco e esse bloco distribui para cada tela. Agora não, agora não tem mais esse bloco. Agora cada tela recebe individualmente. E aí se eu peço para mudar alguma coisa numa tela, ele mantém as outras intactas porque ele só vai mexer naquilo, entendeu?  
**Marcelo Costa:** Entendi.  
**Off Digital:** Então foi um processo de uns dois, três dias executando isso, porque como é que eu monto? Eu monto para cada tela, ele faz todo o o ele cria uma paralela. Aí ele valida, faz todos os testes. Aí se der certo todos os testes, ele desativa a outra. Aí ele assume essa, conecta essa, faz todos os testes de novo e aí ele ele vê se ele pode apagar a outra. Então, cada processo desse é 4, 5 horas para ele fazer todos os  
**Marcelo Costa:** Nossa,  
**Off Digital:** tal,  
**Marcelo Costa:** e queima e queima toque, velho. 4 5 horas trampando,  
   
 

### 00:05:35 {#00:05:35}

   
**Off Digital:** mano.  
**Marcelo Costa:** né?  
**Off Digital:** Só que é sem parar, para mim. Eu rodei um gol aqui, velho, que foi deu mais de dois dias o gol rodando direto.  
**Marcelo Costa:** sem botar  
**Off Digital:** E e o meu, sem botar a mão. E o meu gol é o seguinte,  
**Marcelo Costa:** mão.  
**Off Digital:** é um supervisor disparando três agentes, um reviewer e quando ele termina o trampo, ele dispara outro codex com contexto limpo para questionar ele sobre as todas as decisões dele,  
**Marcelo Costa:** Aí os caras ficam se falando,  
**Off Digital:** né,  
**Marcelo Costa:** né?  
**Off Digital:** irmão? E aí é uma patifaria. E agora estou terminando. Só que o outro agente, mano, hoje eu fiquei rindo. O outro agente tá terminando de fazer os testes. É chato mesmo. Ele mandou assim: "O outro agente tá terminando de fazer os testes". Aí embaixo ele botou assim: "E é chato mesmo, três pontinhos". Aí depois ele veio assim: "É chato no bom sentido. Ele tá fazendo os testes porque tem que fazer porque não sei das quantas,  
**Marcelo Costa:** Velho,  
**Off Digital:** não sei das quantas".  
**Marcelo Costa:** fica tranquilo, meu irmão. Vai tocando sua vida aí,  
**Off Digital:** Irmãzã, tá?  
   
 

### 00:06:30 {#00:06:30}

   
**Off Digital:** Ninguém tá com prazo aqui, tá tudo certo, vai em paz aí. E aí, beleza?  
**Marcelo Costa:** velho.  
**Off Digital:** Então, tava rodando isso. Eh, cara, fiz várias mudanças no motor, boa. Eh, implementei várias coisas aqui, tá tudo documentado, mas eh vários pontos que eu ainda não juntei tudo para depois eu vou mostrar, né?  
**Marcelo Costa:** Sì.  
**Off Digital:** Não vou vou montar um relatório certify certify e o que que era antes. Mas tinham vários gaps assim no naquela coisa da semântica do motor, eh, e não ter uma LLM ali. Então, assim, eu eu mexi no setup das LLMs também. o GPT 5.2 tava dando latência para caramba no no processo. Eh, eu fiz fiz várias mudanças e eu passei aquele fluxo de novo. Cara, eu fiz um bagulho muito louco. Eu peguei aquele fluxo do N8N que você me mandou, criei uma conta do do N8N, subi o fluxo lá, conectei o cloud no N8N, fiz ele passar fluxo por fluxo e entender o que que tem de bom, o que que tem de ruim e o que que tem de bom no nosso e o que que tem de ruim e cruzar depois as duas paradas.  
**Marcelo Costa:** e fazer uma parada só.  
   
 

### 00:07:44

   
**Off Digital:** Aí ele falou: "Velho,  
**Marcelo Costa:** c\*\*\*\*\*\*.  
**Off Digital:** aí até te mostro aqui depois, mano.  
**Marcelo Costa:** Não,  
**Off Digital:** Ele falou: "Velho,  
**Marcelo Costa:** eu não quero nem ver.  
**Off Digital:** é assim". Hã,  
**Marcelo Costa:** Quero nem ver.  
**Off Digital:** não, ele fala: "Velho, no resumo da ópera, ele falou assim: "Velho, vocês saíram de uma ideia de um MVP para um produto construído, mano. Ali naqueles fluxos você tinha eu, deixa eu achar aqui, ó. Deixa eu ver se eu acho aqui o chat aqui. Foi tanta coisa já,  
**Marcelo Costa:** Aquele fluxo tava,  
**Off Digital:** velho.  
**Marcelo Costa:** aquele fluxo tava,  
**Off Digital:** Que cadê?  
**Marcelo Costa:** cara, é um fluxo porco assim, vamos dizer, velho, todo construído.  
**Off Digital:** Não, velho, não é nem que era pouco, mas ele ele falou: "Cara, ó, funciona bem nisso, níso daquilo. Deixa eu ver aqui. Aqui é tanto documento, é tanta coisa. Deixa eu ver onde é que eu vou. Eu não sei se tava no cloud, se tava no Codex. Deixa eu ver se eu acho para te mostrar, velho. Eh, deixa eu voltar a tela aqui para você. Aí eu quero te mostrar as coisas que eu tô fazendo agora, velho, que vai dar um pump master no no no projeto na parte funcional.  
   
 

### 00:08:42

   
**Off Digital:** Não, partil dando errado. Só que é tempo, mano. É tempo.  
**Marcelo Costa:** É,  
**Off Digital:** Eu que eu entendi,  
**Marcelo Costa:** eu tô  
**Off Digital:** o que eu entendi é que se for fazer direito do jeito que eu tô fazendo agora,  
**Marcelo Costa:** ligado.  
**Off Digital:** com review, com teste, com a gente para lá, gente para cá, um mandando pro outro,  
**Marcelo Costa:** Não adianta ter pressa,  
**Off Digital:** c\*\*\*\*\*\*.  
**Marcelo Costa:** velho.  
**Off Digital:** Não, velho, não dá para ter pressa, senão ele faz código porco, entendeu? Não é nem tipo questão de ter pressa. Você tem que eh não adianta, se você abre mais tela dá ruim. Então agora eu faço tudo numa tela só. Eu faço tudo numa tela só,  
**Marcelo Costa:** E vai até o final,  
**Off Digital:** só que é só que é uma tela que invoca vários agentes,  
**Marcelo Costa:** né? Sim,  
**Off Digital:** entendeu?  
**Marcelo Costa:** mas beleza. A central de controle tá num lugar só,  
**Off Digital:** Por exemplo,  
**Marcelo Costa:** né?  
**Off Digital:** cara, quer ver? Ó, Codex computador tá lento, eu preciso reiniciar. Eh, por exemplo, ó, o trampo que eu fiz do codex aqui, ó. Você tá vendo aqui do lado?  
**Marcelo Costa:** Aham.  
   
 

### 00:09:53 {#00:09:53}

   
**Off Digital:** Esses caras são todos subagentes que participaram  
**Marcelo Costa:** Já estão aí skill.  
**Off Digital:** que participar. Ó, isso aqui é toda a galera que trabalhou nesse Gol, tá vendo?  
**Marcelo Costa:** Tá. E esses caras,  
**Off Digital:** Então aqui, ó,  
**Marcelo Costa:** você com você que trouxe ou quando você pediu, ele fala,  
**Off Digital:** não tá tudo no plano.  
**Marcelo Costa:** vou trazer um agente,  
**Off Digital:** No plano, no plano eu monto,  
**Marcelo Costa:** tal.  
**Off Digital:** eu faço ele montar um squad para cada parte do plano e aí durante o desenvolvimento ele vai invocando os caras. Cada um tem uma função, cada um tem um modelo. Então aqui, ó, você vê, velho, todos esses caras trabalharam no rolê. E se eu clico aqui, eu vejo o que que esse cara fez. Então, aqui, ó, o pierce, ó, aqui o trampo dele aqui, ó. Ele pegou aqui, ó. Você é o reviewer. Pá, pá, pá. Ele pegou, verifiquei e tal, fez extrair. Beleza, terminei. Aí se eu pego aqui o o Einstein, tem aqui, ó, o trampo dele, entendeu? Se eu pego aqui o plato aqui, ó, tem o trampo dele e tem todos.  
   
 

### 00:10:56

   
**Off Digital:** E se eu quiser falar com ele, eu falo com ele também. E tem todos aqui,  
**Marcelo Costa:** sobre o trampo que ele  
**Off Digital:** ó. Entendeu?  
**Marcelo Costa:** fez.  
**Off Digital:** Todo mundo tem os trampos dele aqui. Então, tipo, ó lá o Explorer. Então,  
**Marcelo Costa:** E se ele automático quando entra outros agentes que ele que ele põe,  
**Off Digital:** velho,  
**Marcelo Costa:** ele já entra aí nesse subagentes na lateral ou você é já é a  
**Off Digital:** tudo entra aqui. Tudo entra aqui.  
**Marcelo Costa:** visualização dele assim,  
**Off Digital:** Só que você vê o tanto que ele é fragmentado,  
**Marcelo Costa:** né?  
**Off Digital:** velho. O cara fez uma tarefa de 9 minutos. Tá vendo aqui, ó? Ó. Então, aqui, ó,  
**Marcelo Costa:** Sim.  
**Off Digital:** você executou da wave W0 do plano em tal, front end default. Trabalhe no rep. O contexto é o objetivo é criar um bounder de guard inventário executado das dependências B2 sem mudança visual, sem API, sem produção. Não faça deploy comit pá, não rever o trabalho de outros. Sua tarefa é inspeccionar o código. Propõe implementará. Aí tá aqui, ó. O cara recebeu. Vou tratar ele.  
   
 

### 00:11:47

   
**Off Digital:** Pá, pá, pá, o que ele fez? Criou, editou, editou, editou. Implementado, funcionando. Arquivos alterados. Ele dá o reporte aqui pro cara, que é esse cara aqui,  
**Marcelo Costa:** Sim,  
**Off Digital:** que é o supervisor.  
**Marcelo Costa:** certo.  
**Off Digital:** E aí, mano, por que disso aqui? Porque você preserva contexto. Ó o tamanho, ó o tamanhinho do contexto que ele girou aqui. Ele girou com contexto limpo,  
**Marcelo Costa:** Sim, fica mais contundente.  
**Off Digital:** então você não você não degrada contexto,  
**Marcelo Costa:** Você quer voltar, você volta  
**Off Digital:** entendeu?  
**Marcelo Costa:** ali.  
**Off Digital:** Porque você manda o cara executar um plano gigante, ele começa a alucinar no meio do trampo e aí ele começa a botar que a tarefa foi feita,  
**Marcelo Costa:** Sim.  
**Off Digital:** mas foi errado, os testes tá errado, tá tudo errado. No final das contas você vai ter um lixo. Então,  
**Marcelo Costa:** Apesar do plano ser bom,  
**Off Digital:** velho,  
**Marcelo Costa:** a execução foi uma bosta,  
**Off Digital:** exatamente.  
**Marcelo Costa:** né?  
**Off Digital:** Exatamente. Então, não adianta fazer um plano,  
**Marcelo Costa:** Aí quando você fragmenta e esse fragmentar ele que te fala,  
**Off Digital:** não adianta fazer um plano bom se você não consegue,  
   
 

### 00:12:36

   
**Marcelo Costa:** ó, isso aqui tem que  
**Off Digital:** se você não montar o processo de execução,  
**Marcelo Costa:** fragmentar.  
**Off Digital:** não adianta plano bom, velho. Tá ligado? Aqui, ó, eu já eu já vim com com com prompt da execução, ó. Executar o plano vivo de extração das telas defult. Papá, fonte principal, já com plano pronto. Objetivo tirar o front end, regra de execução. Codex atua com supervisor. Se houver ferramenta real de muito agente disponível, montar squad, blá blá blá. Se não houver, não simular agentes fictícios, executar os papéis, pá, pá, pá. Lá esquisas obrigatórios para ele usar aqui. Pá, pá. Execução, ler, começar e tal, tal, tal, não sei o quê. critérios aí, cara.  
**Marcelo Costa:** Esse foi o trampo.  
**Off Digital:** Você vê,  
**Marcelo Costa:** Aí ele já invocou,  
**Off Digital:** cara,  
**Marcelo Costa:** todo mundo veio  
**Off Digital:** essa janela aqui, priminho,  
**Marcelo Costa:** fazendo.  
**Off Digital:** foi foi um trampo de quase dois dias só essa janela  
**Marcelo Costa:** c\*\*\*\*\*\*. Ô Primir aí,  
**Off Digital:** aqui.  
**Marcelo Costa:** por exemplo, você tá, esse é o front, você tá dentro de uma pasta de um projeto que você criou ali, onde tá essa projeto tá na sua máquina.  
   
 

### 00:13:36

   
**Off Digital:** Tá na minha máquina e tá no Git também, né? Tá sempre sincado aqui. É certify, né?  
**Marcelo Costa:** Tudo do certifi tá aí nessa pasta,  
**Off Digital:** Tá aí eu só  
**Marcelo Costa:** mas essa que você tá trampando,  
**Off Digital:** aqui essa que eu tô trampando,  
**Marcelo Costa:** ela é uma dessas aí.  
**Off Digital:** eu só fixei ela aqui, né?  
**Marcelo Costa:** Ah, você fixou,  
**Off Digital:** Posso?  
**Marcelo Costa:** por isso que ela tá em cima.  
**Off Digital:** Ah, é, eu posso fixar.  
**Marcelo Costa:** Entendi.  
**Off Digital:** Exato. E deixa eu ver se foi aqui que eu  
**Marcelo Costa:** Esse esse projetos ele não aparece no cloud,  
**Off Digital:** falei,  
**Marcelo Costa:** né?  
**Off Digital:** pô, parece, pô. igualzinho, só que no code, não, no nok.  
**Marcelo Costa:** No app, né? No app no Ah, no no no code.  
**Off Digital:** faz no na janela do code. É,  
**Marcelo Costa:** Hum.  
**Off Digital:** deixa eu ver aqui para mim onde que foi. Pô, eu queria achar, velho, o que o o que eu fiz lá versus do fluxo N8N. Deixa eu te pesquisar aqui. Sech. Ah, não, foi no foi no cloud  
**Marcelo Costa:** Aí, ó, no code. Cadê as as cadê a sua pasta?  
   
 

### 00:15:09 {#00:15:09}

   
**Off Digital:** aqui,  
**Marcelo Costa:** Suas pastas.  
**Off Digital:** ó. Esse projeto aqui,  
**Marcelo Costa:** Ah,  
**Off Digital:** ó.  
**Marcelo Costa:** ele tá apagadinho. E é o mesmo que tá lá, a mesma pasta que tá lá.  
**Off Digital:** Me pasta.  
**Marcelo Costa:** Você abre o chat, o mesmo chat, ele vai para lá também. Você fez aquele syc.  
**Off Digital:** Não, eu não fiz não, primo. Ó lá. Eh, eu fui montando a do Codex e eu fui montando a do Cloud, porque cada um trabalha de um jeito. Na verdade, eu vou te explicar depois. Eu tenho um repositório chama agent Hub, que ele sinca o Connects e o cloud sempre na mesma página, com as mesmas skills, com as mesmas configurações,  
**Marcelo Costa:** Então o Cláudio fez,  
**Off Digital:** sacou?  
**Marcelo Costa:** ele faz isso, ele pelo menos ele disse que fez, né? Eu não trabalhei no Codex ainda lá numa lá na no Codex você puxa todo o seu  
**Off Digital:** Dá para puxar,  
**Marcelo Costa:** cloud.  
**Off Digital:** dá para importar, mas eu não fiz isso. Eu tenho um repositório lá no git que sinca toda minha parada, minhas, por exemplo, se eu mudar o meu cloud.md no cloud, ele vai mudar o do codex também.  
**Marcelo Costa:** Entendi. Deixa  
   
 

### 00:16:16

   
**Off Digital:** Ó, achei aqui primeiro. Ele me deu aqui, ó.  
**Marcelo Costa:** paradinho.  
**Off Digital:** Eu botei aqui, ó. Ele botou aqui, ó, fluxo certify em uma frase recebe PDF. Tá vendo aí? Dá para ler.  
**Marcelo Costa:** Tô tô  
**Off Digital:** Recebe PDF de um candidato, identifica cada documento de PDF, decide automaticamente se entende ou não as vagas. Aí ele botou aqui, ó,  
**Marcelo Costa:** vendo.  
**Off Digital:** o que faz de bom. A ambição tava certa, cobra cinco famílias de certificados que importam RH marítimo, STCW, pito, tal, tal. Arquitetura síncrona correta. O web Hook responde: "Recebi na hora". O processamento pesado vai para uma fila do Rabbit MQ. É o jeito certo de fazer. O cliente quem chama não fica esperando 30 segundos. Pipeline em etapas separadas. Eh, o fluxo de víde trabalha em fases claras, ler o PDF, classificar, etc. Múltiplos modelos de a com fallura o gemido como primário, open, um openhouter ou PNI como reserva. Trata PDF com vários documentos juntos. Candidato manda o arquivo com 10 certificados escaneado de sequência. O fluxo quebra por página.  
   
 

### 00:17:19 {#00:17:19}

   
**Off Digital:** Pá, pá, pá. Decisão rica não binária, não é só aprovada ou reprovada. Tem confere parcial, pendente, compara a conta a matriz da vaga. Cada vaga tem suas próprias exigências. Distingue declaração temporária de certificado definitivo. Renomeio o arquivo no storage com nome semântico e tem a lógica de comparação adaptada por família. Para NR, o nome do curso é a fonte da verdade, porque NR35 sozinho não diz se é trabalho em altura ou básico, tal, tal, tal. Beleza?  
**Marcelo Costa:** A parte boa.  
**Off Digital:** parte boa que o isso é o que a gente sabe, né, que o projeto faz.  
**Marcelo Costa:** Sim.  
**Off Digital:** É tanto é que é o que tá de pé.  
**Marcelo Costa:** Eh  
**Off Digital:** Aí o que ele mapeou que é a parte ruim, né? Ah,  
**Marcelo Costa:** Ja.  
**Off Digital:** o Frankst 900 293 peças e tem mais metade do fluxo é cópia da outra metade. Quem manteve copiou o pipeline inteiro para processar dois caros diferentes. As duas cópias já dever giram e pontos sutis. Qualquer correção precisa ser aplicada em dois lugares. Eh, as chaves de acesso estão escritas no manual. chave da PI do Google e token aparece texto puro.  
   
 

### 00:18:17

   
**Off Digital:** Eh, aceita documento de qualquer um. Webook não tem autenticação. Qualquer pessoa que descobre o link consegue enviar PDF. Eh, permite que alguém destrua o banco pelo nome do arquivo. As consultas ao banco são montadas grudando o texto. Se eu mandar um arquivo chamado Drop table PDF, isso vira comando real executável. Eh, quando uma peça falha, a fila trava. Sem fallback humano em momento algum.  
**Marcelo Costa:** Угуm.  
**Off Digital:** Ah, quando o documento não bate, desaparece em silêncio. Busca o documento pro nome de arquivo, não por ID. Manda PDF inteiro para vários terceiros sem contrato de dados da LGPD aqui, né? Sem instrumentação. Não dá para saber quantos documentos passaram por dia, quantos falharam, quanto custou LLM. Está guardado num boleano mais string solto. Tem a mínima ideia de que p\*\*\*\* é essa. Engenharia de prompt por intimidação e um dos agentes está escrito literalmente se não chamar a ferramenta irei excluir permanentemente.  
**Marcelo Costa:** Como  
**Off Digital:** Promia de prompt por intimidação.  
**Marcelo Costa:** é?  
**Off Digital:** Em um dos agentes está escrito literalmente: "Se não chamar a ferramenta, irei te excluir permanentemente."  
**Marcelo Costa:** É isso aí. Foi nós que fizemos, eu lembro, velho.  
   
 

### 00:19:30

   
**Marcelo Costa:** Vamos agressivo.  
**Off Digital:** Gargala.  
**Marcelo Costa:** Falou, seja agressivo com esse f\*\*\*\*\*\*\*\*\*\*\*\*. Ele tava errando para c\*\*\*\*\*\*. Parou de errar, viu?  
**Off Digital:** p\*\*\*\*, é isso, é isso aí.  
**Marcelo Costa:** Mas foi assim.  
**Off Digital:** Beleza. Aí aqui ele deu o comparativo. Eh, tal, tal, tal. Beleza. Para comparar. Tá, tá, tal. Agora analisa o motor de certif, ele disse o que temos de bom versus que temos de ruim. Ele botou aqui, ó, motor que o Certifiem linguagem simples. Recebe o PDF, calcula um hash para evitar duplicatas, cria um job na fila do banco e um dos 32 workers paralelos pega esse job. worker passa o documento por quatro fases. Classifica o PDF, CF STCW OPIT normas pessoais e outros usando Open com visão. Faz o OCR no documento inteiro com Google Cloud Vision. Extrai os campos. Data de validade. Siga código técnico, modalidade rodando de e openar em paralelo, reconciliando o resultado. Compara o documento extraído contra cada linha da matriz de exigências da vaga, aplicando uma sequência fixa de quatro testes determinísticos: identidade, sigla bate, código técnico, código bate, validade, vencido, modalidade, tipo de aula e carga horário, OK?  
   
 

### 00:20:54 {#00:20:54}

   
**Off Digital:** O resultado de cada par é gravado como linha em nesse arquivo com a decisão confere parcial pendente no exigido declaração. Motivo, prova do CR, quem decidiu e a flag se é a decisão atual. Aonde o certify ganha do certify? A decisão é determinística, não LLM. Não certif agente Lchain lia o documento extraído e devolveu uma string. Confere parcial pendente. Mesmo documento podia ser decidido diferentemente em dois dias.  
**Marcelo Costa:** Uhum.  
**Off Digital:** Acho que esse era o maior problema para escala,  
**Marcelo Costa:** S.  
**Off Digital:** né? No certify, a função compare docum é 100% determinística e pura.  
**Marcelo Costa:** Sim.  
**Off Digital:** Dado o mesmo documento, mesma matriz devolve sempre a mesma decisão. Audita-se o código, não, o módulo do ll.  
**Marcelo Costa:** Ótimo.  
**Off Digital:** Por isso que dá mais trabalho, sacou?  
**Marcelo Costa:** Uhum. Não é porque a vari você tem que ter muito mais variável porque senão ele não tem não,  
**Off Digital:** Quê?  
**Marcelo Costa:** ele não vai interpretar.  
**Off Digital:** E não é só isso, velho. Você tem que afinar os scripts para c\*\*\*\*\*\*, velho. Todos os scripts tm que est perfeito, porque se um script tá com problema, a decisão vai sair errada.  
   
 

### 00:21:57

   
**Off Digital:** Então, exige muito mais trabalho de,  
**Marcelo Costa:** Sim,  
**Off Digital:** que é o que a gente tá fazendo, do que você põ um LLM lá e fala:  
**Marcelo Costa:** muito mais refino.  
**Off Digital:** "Velho,  
**Marcelo Costa:** Muito mais refino,  
**Off Digital:** você põe um LLM lá e falar,  
**Marcelo Costa:** velho.  
**Off Digital:** velho, contextualiza aí". Só que ele nunca vai contextualizar igual,  
**Marcelo Costa:** É, é, é. São momentos.  
**Off Digital:** entendeu?  
**Marcelo Costa:** Esse é o momento. Como a gente tem um catálogo conhecido, a gente tem que ser determinístico, velho. Não tem para onde correr para ser certo.  
**Off Digital:** Velho, para ter um produto para ir para mercado,  
**Marcelo Costa:** Agora  
**Off Digital:** não tem como. Não sei. Imagina você botar uma heléix lá,  
**Marcelo Costa:** é isso.  
**Off Digital:** um cara, e jogar na mão de um GPT alucinando. Tá louco? Não  
**Marcelo Costa:** Cada hora você subia um cara aqui,  
**Off Digital:** existe.  
**Marcelo Costa:** ele dava 23\. Confere. Aí eu apagava e subia ele de novo, dava 26\. Aí você p\*\*\*\*, velho,  
**Off Digital:** Exatamente.  
**Marcelo Costa:** pera aí, velho.  
**Off Digital:** Exatamente.  
**Marcelo Costa:** Pode tem que dar 23\.  
**Off Digital:** Então,  
   
 

### 00:22:39 {#00:22:39}

   
**Marcelo Costa:** Tem que dar 23 de novo, velho.  
**Off Digital:** exatamente. Então, esse é o ponto, velho. Aí,  
**Marcelo Costa:** Ja.  
**Off Digital:** ó. Catálogo de compliado. Não, prompt certifi a tabela mestra opit copiada dentro do prompt classificador. Mudar uma regra para editar o prompt muda uma equivalência era reescrever instruções por LLM. O certifi tem seis tabelas vivas, compliance rules, compliance rules, aliás. Então ele tem as siglas canônicas, os sinônimos, o as equivalências, ou seja, CBSN substitui CBSP, ele tem eh as diferenciações, ou seja, não equivalências, ele tem o refinamento por cliente e isso cria o documentos catalog, né? Ou seja, o catálogo de documentos.  
**Marcelo Costa:** M.  
**Off Digital:** Editar uma equivalência a uma linha de migration, não redesenha motor leis run time. Ou seja, qualquer ajuste de equivalência você tá mudando um pontinho, você não tá mudando o prompt, entendeu?  
**Marcelo Costa:** Sim.  
**Off Digital:** Eh, em variantes de negócio são código no Esperança. O certifi rezava pro LLM lembrar que CBSN substituiu o CBSP. CFI tem variantes hard coded que rodam antes de qualquer comparação. Violação detectada, pendente imediato.  
   
 

### 00:23:49

   
**Off Digital:** Auditoria pode olhar linha de código confiar. Ou seja, se você for bater numa empresa que tem um dev, o cara vai vai querer ver isso aqui para entender como o nosso sistema de de  
**Marcelo Costa:** É,  
**Off Digital:** auditoria  
**Marcelo Costa:** e outro é onde você confiança, né,  
**Off Digital:** classifica.  
**Marcelo Costa:** velho? Você não tá dependendo de de o cloud não tá funcionando bem, entendeu?  
**Off Digital:** Exato. Exatamente. Eh,  
**Marcelo Costa:** Ele pode em algum momento te ajudar no processo,  
**Off Digital:** hisó.  
**Marcelo Costa:** mas não todo, né? A gente tava tudo na mão deles,  
**Off Digital:** Sim, sim. Ah,  
**Marcelo Costa:** né?  
**Off Digital:** histórico de decisões é preservado não sobrescrito. No certify processão documento sobrescrevia a decisão anterior histórico perdia. No certify, cada nova decisão pro mesmo candidato vaga exigência insere uma nova linha em documento de comparons e marca o anterior como scurrent false mais superseded at, ou seja, ele tira o próximo e coloca como antigo marca scurrent, né? Ou seja, eh, ele não é mais no momento o o dono do negócio, então ele bota false. Então, esse aqui não é mais o dono e ele põe o outro como dono e os outros ficam para baixo.  
**Marcelo Costa:** Sim, mas fica anotado, né?  
   
 

### 00:24:56 {#00:24:56}

   
**Off Digital:** O histório fica eterno. A auditoria pergunta: "Por que mudou?" Você mostra os dois registros lado a lado com Indiver e Decided by. Ou seja,  
**Marcelo Costa:** A decisão quem mudou,  
**Off Digital:** qual que é a o versionamento e por foi a decisão.  
**Marcelo Costa:** né?  
**Off Digital:** Eh, decisão tem mais de 30 motivos canônicos, não texto livre. Certify gravava observations, contexto livre que LLM cuspia. Filtrar por motivo era impossível. O CF tem reason code com 30 mais valores. Validade espirada, data de validade ausente, data ambígua, código não corresponde, carga horário suficiente, etc. Dashboard, a gente pode mostrar casos com dato ambígua nas últimas 24 horas e a gente consegue analisar. Ou seja, isso é para uma auditoria nossa interna do motor,  
**Marcelo Costa:** Sim,  
**Off Digital:** um dashboard nosso.  
**Marcelo Costa:** já é conhecido as respostas, velho.  
**Off Digital:** Exato.  
**Marcelo Costa:** Não vem alguma coisa nada a ver.  
**Off Digital:** De produto. Exatamente de produto.  
**Marcelo Costa:** Às vezes vi umas respostas que você falava: "p\*\*\*\*, essa foi boa". Aí tinha umas que vinha você, p\*\*\*\*,  
**Off Digital:** Porque você pensa, cara, imagina a gente num volume de 10.000 casos por dia,  
   
 

### 00:25:47 {#00:25:47}

   
**Marcelo Costa:** que  
**Off Digital:** você entender lá, velho, cara, o que que tá dando pau por data de validade ausente? A gente vai lá num search dentro do nosso sistema e vai baixar tudo que deu data de validade ausente,  
**Marcelo Costa:** sim.  
**Off Digital:** entendeu? Eh, fila profissional com claim token, beiter. O certifi você vê, velho, eu não soube responder pro cara, por isso que eu saí da reunião aqui, eu falei: "Mano, deixa eu entender essa p\*\*\*\*, porque eu sei que a gente tá na frente e eu não consigo falar".  
**Marcelo Costa:** Eh,  
**Off Digital:** Então, velho, o Certif usava R MQ com paralel message um uma mensagem por vez. processo morria, a mensagem voltava paraa filha e ficava em loop infinito.  
**Marcelo Costa:** Eh  
**Off Digital:** O certifing jobs no post GRE com select for updates keep locked 32 workers paralelos cada job tem um client token, o uid worker donal hat bit a cada 60 segundos e um hiper que volta pra fila qualquer job sem hatit por 20 minutos. Work que morre no meio não bloqueia ninguém e não duplica resultado. Hbit a cada 60 segundos é a cada 60 segundos ele dispara. um uma higiene de ver se tem alguma coisa travada na fila, ele reprocessa,  
   
 

### 00:26:57 {#00:26:57}

   
**Marcelo Costa:** Ele entendi.  
**Off Digital:** entendeu?  
**Marcelo Costa:** Top  
**Off Digital:** Dual provider com reconciliação.  
**Marcelo Costa:** duas.  
**Off Digital:** Certifi mostrar o documento para LLM por vez. Um documento por vez. Gemini com openhout de fallback. Os certifieds para GENY e Openi em paralelo no extrator se discordarem campo a campo um terceiro modelo GPT 5.2 entra como juiz reduz o erro de provider úônico sem custo proibitivo. Ah, tá. para casos onde a sigla não bate diretamente, por exemplo, treinamento de emergência avançado versus AGT, o Certifi tem um uma camada de julgamento que é esse esse script aqui, que é um LLM propõe a equivalência, um segundo ll verifica e só persiste como aliás se a confiança for mais de 0.9. Tudo gravado nesse log com o resto do input, o motor aprende ao longo do tempo sem decisão cega. O certifi esse prompt, se não chamar a ferramenta clube permanentemente. Então é como a gente substituir esse prompt basicamente. Ah, independência real certifá dois candidatos com certificado. PDF colidia, ou seja, com o mesmo nome e no certify, índice único, mesmo arquivo, candidatos diferentes, sem colisão. Até o pil do mesmo conteúdo pelo mesmo candidato é detectado antes mesmo de subir pro storage.  
   
 

### 00:28:25

   
**Off Digital:** Máquina de estado displío tem quatro níveis. Tá t tal. Você tinha esses quatro níveis aqui no Supas e a gente tem esses níveis aqui. Ah, revisão humana de verdade. Certify não tinha revisão humana. Ll decidia ponto final. Certify trigger automático score 0.7 flag requere revisão humana. Tela dedicada em revisão com PDF mais matriz mais campos. Quatro ações de aprovar, rejeitar, ajustar e reprocessar com justificativa obrigatória. Audi apende tal quando quem por e quando manda aprova equivalência nova. Ele vira aprendizado no  
**Marcelo Costa:** Top.  
**Off Digital:** catálogo.  
**Marcelo Costa:** Muito bom para mim. Tá, p\*\*\*\*, velho. É isso. Foi é um um aprendizado, né? Vai que agora vai ficar,  
**Off Digital:** Exato. Aí ele deu aqui, ó, onde o N8N certifi algo que o certifi ainda não tem ou perdeu.  
**Marcelo Costa:** né?  
**Off Digital:** Eh, visualização do fluxo do início ao fim, que você via o fluxo inteiro lá. Isso a gente pode até montar um N8N que simula o fluxo ou uma um HTML que tenha o os diagramas certinho do fluxo inteiro. Eh, classificação via visão do documento inteiro. Eh, o certify já quebrava o documento em várias páginas.  
   
 

### 00:29:49 {#00:29:49}

   
**Off Digital:** Isso aqui eu não tinha colocado ainda. Eh, retrai de OCR com ei de 60 segundos entre entre tentativas. Ele tinha quatro tentativas. Eh,  
**Marcelo Costa:** Quando dava pau, ele ficava rodando,  
**Off Digital:** eh, e a gente não tem aqui esses quatro,  
**Marcelo Costa:** né?  
**Off Digital:** essas quatro tentativas de ler o mesmo documento que errou,  
**Marcelo Costa:** Sim.  
**Off Digital:** entendeu?  
**Marcelo Costa:** Isso é bom porque às vezes travava e ficava por aí.  
**Off Digital:** Exato.  
**Marcelo Costa:** Eu  
**Off Digital:** Detectão explícito de lista de presença.  
**Marcelo Costa:** lembro.  
**Off Digital:** Certifi uma classe lista no classificador para detectar planilhas de presenças coletivas não comparáveis. O CFI também tem its lista de presença no classificador, então isso tá coberto em parte aqui. Eh, tempo até primeiro MVP. O N8N permitiu que o produto saísse do zero em semanas com o construtor visual. Certify exigiu engenharia de meses para validar a hipótese. N8N ganha para escalar perde feio. Então é basicamente é é basicamente isso, né?  
**Marcelo Costa:** É o que nós estamos fazendo, né, velho?  
**Off Digital:** É basicamente isso.  
**Marcelo Costa:** Foi sem querer, mas foi.  
**Off Digital:** É isso. Ah, então, ó, curva de mudança para mudança simples.  
   
 

### 00:31:01

   
**Off Digital:** Editar um prompt no N8N é abrir o nó e digitar no CFY editar comportamento. Exige PR, monore, deploy no fly, talvez até migration. Para mudanças triviais, o N8N era mais ágil. para mudanças seguras, o certifi melhor. Ou seja, com essa estrutura a gente vai fazer mudanças mais sólidas sem sem  
**Marcelo Costa:** Fica mais engessado, né? Mas é mais seguro, né?  
**Off Digital:** dar pau.  
**Marcelo Costa:** velho,  
**Off Digital:** É,  
**Marcelo Costa:** senão senão qualquer um muda,  
**Off Digital:** mas ao mesmo tempo a gente tem um agente plugado lá.  
**Marcelo Costa:** velho.  
**Off Digital:** É.  
**Marcelo Costa:** Ja.  
**Off Digital:** E aí ele deu aqui, ó, veredito em uma frase. O certify é produto, certify era um experimento. As ideias boas que valia migrar, pipeline faz, decisão de partida, matriz por vaga, blá blá blá, foram migradas. As ideias ruins, LLM decidindo, chaves hardcoder, pá pá pá, foram trocadas por engenharia mais séria. As lacunas que sobram no certify, observalidade, custo controlado, alerta, DPA documentado, são gaps típicos de pré-produção, não falhas de fundamento. E aí eu já tirei daqui, já tracei um plano com tudo isso aqui e já voltei para andar,  
   
 

### 00:32:06

   
**Marcelo Costa:** Top. Não, para mim o negócio vai ficar casca,  
**Off Digital:** entendeu? É isso aí.  
**Marcelo Costa:** né?  
**Off Digital:** de mim, onde é que nós estamos no momento atual, eh, arrumando a tela de admissão, que é o que a gente tem que trazer de novo, né? Então eu tô eu tô investindo bastante aqui. Eu tô lendo dentro do cursor, eu já fiz toda isso, tudo isso aqui em local e agora eu já tô com opos aqui implementando. Então você pegar aqui, ó. Problema de conexão.  
**Marcelo Costa:** É f\*\*\*\*\*\*\*\*\*\*\*\*.  
**Off Digital:** Problema de conexão. Problema de conexão. Problema de conexão. Isso aqui tá rodando, cara, desde sei lá,  
**Marcelo Costa:** f\*\*\*.  
**Off Digital:** tem muito tempo que isso aqui tá rodando e aí toda hora para. Aí eu tenho que vir aqui. Segue. Beleza. Mas eu tô aqui no cursor que eu montei o MOC aqui porque o cloud tava impossível e eu tava sem limite do Codex. Aqui é certificados, então eu não mexi porque certificados vai manter certificados vai manter como já tá,  
**Marcelo Costa:** Certo.  
**Off Digital:** né? Então aqui certificados a gente já tem, vai manter isso aqui, né? Eu já eu vou arrumar algumas coisas aqui, mas eu já arrumei bastante, ó.  
   
 

### 00:33:29

   
**Off Digital:** Tá vendo que o requisito já tá bem polido,  
**Marcelo Costa:** Uhum.  
**Off Digital:** ó? Tudo polidinho. A sigla agora tá falando a sigla correta e o código tá falando o código correto.  
**Marcelo Costa:** Perfeito.  
**Off Digital:** Então tá aqui, ó, NR3. Aqui vai ter aí aqui o tipo, ó, emergência, salvamento, trabalho quente, módulo geral, observador trabalha quente. Então, já ajeitei isso. Eh, vamos ver um candidato que que tem pendente parcial. Quer dizer, ó, aqui agora. Ah, não tá funcionando, p\*\*\*\*, velho. Na na parada de refazer as telas lá, ele ele tirou. Mas basicamente quando eu clico na lixeira agora, ele abre vários pontinhos para você selecionar vários documentos de uma vez.  
**Marcelo Costa:** se quiser excluir  
**Off Digital:** Excluir tudo. Isso não é nem pela galera,  
**Marcelo Costa:** tudo.  
**Off Digital:** mais pela gente aqui nos testes. Porque, pô, velho, eu quero excluir tudo, eu tenho que excluir um a um, entendeu? Então, tem que mandar o cloud excluir. Mas beleza, já tá aqui, ó. Quando você abre, ele já fala: "Ó, esse envio será arquivado, removido das listas,  
**Marcelo Costa:** Sì.  
**Off Digital:** o requisito voltará a ficar pendente". E uma coisa que eu entendi é que,  
   
 

### 00:34:51

   
**Off Digital:** por exemplo, quando a gente subia um novo candidato, ficava uma porrada de pendente aqui, né?  
**Marcelo Costa:** Sim, dos do que tinha do que tem na matriz,  
**Off Digital:** Aí é aqui é exatamente o que a matriz  
**Marcelo Costa:** né?  
**Off Digital:** exige, entendeu?  
**Marcelo Costa:** É exato. É o que a matriz exige, tá tudo aí.  
**Off Digital:** Tá tudo aqui. Exato.  
**Marcelo Costa:** Eles vão subindo,  
**Off Digital:** Eles vão subindo ou eles vão indo para Eles vão indo para parcial ou vão indo para confere.  
**Marcelo Costa:** ou eles vão indo para parcial ou eles vão indo.  
**Off Digital:** Exatamente. Aí aqui no no revisão eu já dei uma ajeitada legal aqui.  
**Marcelo Costa:** Isso.  
**Off Digital:** Perdeu o Ah, não, tá colando o zoom do mouse, ó. Tá vendo que agora o zoom já tá bem melhor, ó?  
**Marcelo Costa:** Boa.  
**Off Digital:** Tá filezinho já.  
**Marcelo Costa:** Ele já direitinho falar só do documento,  
**Off Digital:** Você mexe com o mouse aqui,  
**Marcelo Costa:** né?  
**Off Digital:** pá. Se você mexer pro lado, ó, ele não buga.  
**Marcelo Costa:** Aí tinha um negocinho que era clicava no nome, ele ia lá pro cara. Eu acho que você tirou isso.  
**Off Digital:** É, ainda tem.  
**Marcelo Costa:** Não, não nesse nome, no nome do documento.  
   
 

### 00:35:50

   
**Off Digital:** Não, aqui eu tirei. Aqui eu tirei.  
**Marcelo Costa:** Boa,  
**Off Digital:** Aqui você só clica só pro documento. Aqui ele já tá dando as informações reais,  
**Marcelo Costa:** boa.  
**Off Digital:** mas ainda não vai ficar assim. Ainda vou mudar esse. Não vai ficar esse layout. Mas já tá dando as informações corretas, só que ele tá dando a informação bruta, né? Ainda eh tudo determinístico. Eu vou botar um um esquema mais eh um LLM e para até para botar esse chat para  
**Marcelo Costa:** uma LLM aí para  
**Off Digital:** funcionar aqui que é simples. Eh,  
**Marcelo Costa:** lá no Aí você tava falando dos documentos do de entrada,  
**Off Digital:** isso aí eu vou voltar lá pra admissão. É aí só para você entender.  
**Marcelo Costa:** né?  
**Off Digital:** Então, candidatos vai continuar igual. Por isso que eu não montei a tela. Aí como é que tava aqui? Documentos pessoais, formulários, que aqui você criava o link, né? Pá, aqui tinha os link para gerar as fichas de cadastro que tinha entrado também. Então, do da ficha cadastral, ficha emergência, o ASO,  
**Marcelo Costa:** Na verdade,  
**Off Digital:** tava tudo aqui em geral.  
**Marcelo Costa:** esse link dos formulários é aquele KYC. Aí você tá depois de  
   
 

### 00:36:53 {#00:36:53}

   
**Off Digital:** Isso aqui é o Kyc e aqui era o das fichas.  
**Marcelo Costa:** pego todos os documentos, você gerava  
**Off Digital:** Exato. Exato. Exato.  
**Marcelo Costa:** esse,  
**Off Digital:** Aí aqui era aquela revisão, aqui era o histórico, aqui é observação, né? Isso isso é o que a gente já tinha ali naquele dia da reunião do ADAV,  
**Marcelo Costa:** tá?  
**Off Digital:** mais ou menos. Aí o que eu implementei aqui é o seguinte, eu juntei tudo agora priminho, não tem mais aquele monte de aba certificados é certificados. admissão incorporou toda aquela parte de documentos pessoais,  
**Marcelo Costa:** О,  
**Off Digital:** formulários, Kyc, tudo tá dentro de admissão e atividade virou aquela aba de observação barrah histórico, virou uma aba só, atividade.  
**Marcelo Costa:** tudo que foi feito numa sequência,  
**Off Digital:** Então tudo que foi feito tá aqui,  
**Marcelo Costa:** tá bom?  
**Off Digital:** velho. Então aqui, ó, pá e tal. Aí você tem aqui tudo eventos, por exemplo, aqui é o nome do recruta, né? Então, o recruta rejeitou o documento na segunda tentativa. É um evento. Sistema marcou pá pá.  
**Marcelo Costa:** Beleza.  
**Off Digital:** É um evento. Sistema enviou o lembrete,  
**Marcelo Costa:** Ótimo.  
   
 

### 00:38:00

   
**Off Digital:** é um evento.  
**Marcelo Costa:** É os  
**Off Digital:** Notas aqui as notas que que o cara coloca. Uma observação.  
**Marcelo Costa:** logzinho.  
**Off Digital:** Motor aqui é e eh notificação do motor automática e aqui é tudo que mistura tudo junto. Então ficou tipo uma timelinezinha. de atividade, horário,  
**Marcelo Costa:** Perfeito.  
**Off Digital:** dia colapsável e tal, dá para fechar, não sei das quantas.  
**Marcelo Costa:** É que os cara aí pouco vão trabalhar.  
**Off Digital:** E aqui,  
**Marcelo Costa:** Isso aí é um histórico para ter aí se precisar  
**Off Digital:** cara, na verdade, eu acho que isso aqui vai ser muito importante,  
**Marcelo Costa:** saber,  
**Off Digital:** primo, porque isso aqui é onde o Marcelo vai entender a operação.  
**Marcelo Costa:** é para ver quem tá fazendo, quem não tá e pra gente também ver o que tá  
**Off Digital:** É, tá tudo aqui, velho. Ó, velho, aprovou o candidato tá aqui, marcou, tá aqui.  
**Marcelo Costa:** acontecendo.  
**Off Digital:** Aqui tá escrito IA, documento, nota, status. Então, velho, e a é o motor falando,  
**Marcelo Costa:** Aham.  
**Off Digital:** entendeu? Beleza. Aí aqui a gente tem tal, aqui a gente tem os dias. Que dia? Então, pô, que que tem segunda, que que tem quinta? Que que tem quarta?  
   
 

### 00:39:00 {#00:39:00}

   
**Off Digital:** Aqui você vai mudando. Aqui você vai mudar a semana. Botei por semana. Então, dá para mudar um calendariozinho do mês também,  
**Marcelo Costa:** Так.  
**Off Digital:** mas é por semana. Então, velho, que que foi feito quarta? Qual é a atividade no club? É quarta. Qual a atividade no club? É quinta. Qual atividade no club é terça? né? Assim por diante. E aqui observação, você quer botar uma observação, você põe aqui, ó. É de contato, é de decisão, é de pendência, é interno, você põe aqui, registra, já vai aparecer aqui.  
**Marcelo Costa:** Tá beleza,  
**Off Digital:** Beleza? Então, eu tirei duas telas e juntei uma.  
**Marcelo Costa:** perfeito. Melhor. Consolidou. E aí na admissão,  
**Off Digital:** Aqui eu mudei a interface também.  
**Marcelo Costa:** como é que ficou admissão?  
**Off Digital:** Hã, então a admissão aqui dentro. Aí aqui em cima eu mudei a interface também. Então era assim, ó. Lembra que era assim com as linhas?  
**Marcelo Costa:** Uhum.  
**Off Digital:** Eu deixei assim agora. É um botão.  
**Marcelo Costa:** Sim.  
**Off Digital:** Então você clica em certificação, ele vai te dar uma mensagem.  
   
 

### 00:40:00 {#00:40:00}

   
**Off Digital:** Cer eh eh você quer mudar o o candidato paraa fase de certificação? Sim ou não? Sim. Pum. Aí ele vai mudar ele no sistema inteiro,  
**Marcelo Costa:** Tá.  
**Off Digital:** lá no Camban, em todo lugar ele vai pra certificação, entendeu?  
**Marcelo Costa:** Tá.  
**Off Digital:** no clique, eh, e a admissão. Agora você tem um colapsável que abre todas as partes da  
**Marcelo Costa:** Угуm.  
**Off Digital:** admissão. Eh, que que é aqui? Aqui você tem três páginas, link, revisão, que seria que vai ser basicamente DP e formulários, certo? São três abas. Então, a admissão é só o nome do grupo, digamos assim, porque é a aba de link, a aba de DP e aba de formulários na prática. Só que a admissão é a aba que colapsa os três.  
**Marcelo Costa:** Certo.  
**Off Digital:** Quando eu abrir a admissão, eu abri em link. Se eu abrir em formulários e fechar, ele vai abrir em formulários. Ó, ele sempre abre em link, mas se eu vir em formulários e fechar, ele tá em formulários, entendeu?  
**Marcelo Costa:** Tá  
**Off Digital:** Então,  
**Marcelo Costa:** livre.  
**Off Digital:** beleza. Link aqui você gera o link, copia e cola o link, certo?  
   
 

### 00:41:17

   
**Off Digital:** Atividade do link.  
**Marcelo Costa:** Uhum.  
**Off Digital:** Fulano recruta gerou o link. Fulano recruta copiou o link. Candidato, tal hora abriu no telefone mobile, candidato ficou na parte de boas-vindas, fechou sem avançar. Sistema, agendou o lembrete automático para amanhã. Então aqui é uma atividade do link. Sim,  
**Marcelo Costa:** Так.  
**Off Digital:** simples, mas efetiva. Aqui é um gráficozinho só para compor o visual, né? Então, o dia que foi criado, na quarta-feira foi criado, ele avançou duas etapas, na quinta-feira avançou três.  
**Marcelo Costa:** E as etapas estão lá em cima que ele vai avançando.  
**Off Digital:** Isso são 11 etapas. São 11 etapas aqui de 1 a 11, tá? Você tem aqui onboard, boas-vindas, ID, identidade, CPF, CPF, CTPS, residência, selfie, ficha um, ficha dois, ficha 3, ficha 4, ficha 5\.  
**Marcelo Costa:** E essas fichas elas vão sendo preenchidas, só vai sobrar para ele o que não o que não tem de dado.  
**Off Digital:** É, elas vai, ela vai voltar pronta pra gente, toda preenchida aqui agora.  
**Marcelo Costa:** Tá, mas o cara, a evolução dele, quando ele vai subindo os documentos, ele vai evoluindo aqui, certo?  
   
 

### 00:42:35 {#00:42:35}

   
**Off Digital:** Ele vai evoluindo aqui.  
**Marcelo Costa:** Certo. Aí você vê,  
**Off Digital:** Vai tá tudo dentro do mesmo link.  
**Marcelo Costa:** por exemplo, você entra lá,  
**Off Digital:** Tudo dentro.  
**Marcelo Costa:** deixa eu ver a selfie do cara,  
**Off Digital:** Tudo do dentro do mesmo link. Agora, antes era separado,  
**Marcelo Costa:** tá?  
**Off Digital:** entendeu? Então agora ele vai matar todos esses etapas. Chegar aqui, ele vai preencher nessa ficha o que falta preencher. Chegar aqui, ele vai preencher nessa o que falta preencher, entendeu?  
**Marcelo Costa:** o cara via link,  
**Off Digital:** No mesmo link no celular, vai passando nas telinhas, entendeu?  
**Marcelo Costa:** tá?  
**Off Digital:** Então beleza. O cara parou aqui na na ficha de emergência. Ah, retoma daqui. Ah, o cara parou aqui no ASO.  
**Marcelo Costa:** E aí você vai conseguir ver o que que ele fez quando eu clicar aí,  
**Off Digital:** vai conseguir ver o que que ele fez. Exatamente.  
**Marcelo Costa:** tá?  
**Off Digital:** Eh, tem aí ações rápidas. Aqui você tem que copiar o RL do link, pré-visualizar como candidato. Então você vê na tela dele lá do do celular, vai abrir o mocapzinho do celular, você vai ver onde ele tá, onde ele parou, renovar o prazo, se tiver inspirando, e revogar o link aqui, criar um link adicional.  
   
 

### 00:43:42

   
**Off Digital:** Se vamos dizer que o cara perdeu o link, ah, mudei de telefone, velho, me manda o link aí. Você quer manter o atual sem excluir o o que já tava antes para não  
**Marcelo Costa:** O que já foi  
**Off Digital:** perder tudo.  
**Marcelo Costa:** feito  
**Off Digital:** Você cria um adicional e aqui regenerar o link. Aí se você precisar gerar outro. Ah, deu pau aqui, botei as coisas erradas, não tô conseguindo apagar.  
**Marcelo Costa:** aí vai pagar  
**Off Digital:** Vai apagar. Exato. Eh, aqui vai tá se tá em aberto ou não. Quantos dias tá em aberto. E aqui os detalhes. Qual o passo que ele tá que tá junto com isso aqui? tá no passo há tanto tempo, foi criado tal dia, inspira tal dia.  
**Marcelo Costa:** Ótimo. p\*\*\*\*, velho. Aí ficam  
**Off Digital:** É, é operacional, velho. Isso aqui é operacional. E aí, beleza? Lembrete agendado para amanhã.  
**Marcelo Costa:** p\*\*\*\*.  
**Off Digital:** Você tem essa telinha aqui de agendar lembrete. Clicou em agendar lembrete, você põe aqui a data do lembrete, o horário, personalizar a mensagem. Olá, Cléber. Seu link de admissão na certifo. Conclu para seguir o processo.  
   
 

### 00:44:44 {#00:44:44}

   
**Off Digital:** Canal do lembrete, WhatsApp, e-mail agendar.  
**Marcelo Costa:** Mas você já pretende estar aí já com os dados para fazer esse esse envio pro cara no WhatsApp também?  
**Off Digital:** Você tem que ter o WhatsApp, o e-mail dele, né,  
**Marcelo Costa:** Não, eu digo,  
**Off Digital:** velho?  
**Marcelo Costa:** mas já ter o Vai vai mandar pelo WhatsApp web, né, que você abre já inicialmente manual,  
**Off Digital:** Sim. WhatsApp, e-mail. Vamos mandar dentro do sistema mesmo.  
**Marcelo Costa:** né? Inicialmente  
**Off Digital:** Você põe aqui canal de WhatsApp, canal de e-mail.  
**Marcelo Costa:** manual,  
**Off Digital:** Se você botar os dois, ele vai abrir primeiro o WhatsApp, depois o e-mail ou os dois de uma vez. Abre duas novas,  
**Marcelo Costa:** tá?  
**Off Digital:** duas novas abas, uma vai pro WhatsApp Web e outra vai pro  
**Marcelo Costa:** É que você tá agendando aí,  
**Off Digital:** Gmail.  
**Marcelo Costa:** ele é um processo manual. Você agendar para amanhã, ele amanhã vai abrir na sua  
**Off Digital:** Então,  
**Marcelo Costa:** cara  
**Off Digital:** minha ideia é agendou com a mensagem personalizada, ele vai enviar direto no horário que  
**Marcelo Costa:** no dia que for.  
**Off Digital:** for.  
**Marcelo Costa:** Então, mas aí você vai ter que que construir um falou  
**Off Digital:** o disparo, igual o o coisa, igual falou,  
**Marcelo Costa:** lá.  
**Off Digital:** isso aqui só vai ser a personalização do disparo, entendeu?  
   
 

### 00:45:46

   
**Off Digital:** Agora, se você quiser mandar em tempo real,  
**Marcelo Costa:** Sim.  
**Off Digital:** tipo, não quero agendar, quero mandar agora, ó, velho, preciso falar que o cara quero mandar WhatsApp, já tem a mensagem pronta aqui, enviar. Aí já abre o o WhatsA,  
**Marcelo Costa:** Sim,  
**Off Digital:** mesma coisa.  
**Marcelo Costa:** sim.  
**Off Digital:** Já tem o e-mail pronto. Se você quiser alterar o e-mail,  
**Marcelo Costa:** É,  
**Off Digital:** você pode alterar.  
**Marcelo Costa:** eu nesse momento não colocaria o negócio agendado para fazer, deixava os caras manual, pr os cara ir vendo, mas a gente deixa ele bloqueado aí em breve,  
**Off Digital:** Beleza,  
**Marcelo Costa:** tá  
**Off Digital:** pode ficar aqui em breve,  
**Marcelo Costa:** ligado?  
**Off Digital:** mas já tá aqui a função para que que, né? Isso aqui quando eu refiz lá no cloud design, ele já me deu aqui essa opção, eu já falei: "Beleza, não custa".  
**Marcelo Costa:** Sim,  
**Off Digital:** Isso aqui é custo zero, mano. Isso aqui é muito tranquilo de fazer.  
**Marcelo Costa:** é fácil fazer o ponto. É só se o dos prazos aí,  
**Off Digital:** Não, o de o chato é fazer o Iren,  
**Marcelo Costa:** que dia que vai.  
**Off Digital:** velho. O Iring já tá pronto. Agora é só mandar o botão enviar pro lugar certo,  
   
 

### 00:46:32 {#00:46:32}

   
**Marcelo Costa:** Sim.  
**Off Digital:** entendeu? Não tem.  
**Marcelo Costa:** Ótimo. Ficou top essa parte  
**Off Digital:** Eh, aí beleza.  
**Marcelo Costa:** aí.  
**Off Digital:** Link eh, revisão de documento. Então, é uma tela igual a revisão lá, mais ou menos, mais simples ainda.  
**Marcelo Costa:** Isso se tiver algum parcial,  
**Off Digital:** Não, velho,  
**Marcelo Costa:** alguma coisa,  
**Off Digital:** isso é tipo assim, o cara mandou a identidade, o cara mandou o CPF,  
**Marcelo Costa:** tá?  
**Off Digital:** cara. Tá aqui.  
**Marcelo Costa:** Você vai você vai checar.  
**Off Digital:** Tá  
**Marcelo Costa:** E outra, quando o cara é contratado, eu preciso enviar tudo isso.  
**Off Digital:** aqui  
**Marcelo Costa:** É bom ter um botão de exportar aí tudo. Como ele vai exportar os certificados, ele precisa exportar isso também para mandar pro cliente.  
**Off Digital:** os os documentos, né?  
**Marcelo Costa:** Isso.  
**Off Digital:** Sim. Isso. Sim, sim,  
**Marcelo Costa:** Pensa nisso aí depois para deixar esse no certificado.  
**Off Digital:** sim, sim. Botando já tem aqui, ó.  
**Marcelo Costa:** Nem sei se a gente já colocou isso.  
**Off Digital:** Prim, já tem. Só que é só de um documento. Tem que botar um de todos.  
**Marcelo Costa:** eh exportar tudo num zip, entendeu?  
**Off Digital:** É sim.  
**Marcelo Costa:** que eu acho que pode ter um  
   
 

### 00:47:28

   
**Off Digital:** Ah, já tem aqui, ó. Você revisa os documentos,  
**Marcelo Costa:** global  
**Off Digital:** aí ele vai gerar os formulários preenchidos e aí você baixa o zip com a  
**Marcelo Costa:** com formulário, com  
**Off Digital:** ficha,  
**Marcelo Costa:** tudo.  
**Off Digital:** as ficha pronta, a ficha cadastral, ficha de emergência, ASO, relação de documentos, cadastral  
**Marcelo Costa:** É que cada um aí é que depois, beleza, ele abre o coiso e ele manda,  
**Off Digital:** expatriado.  
**Marcelo Costa:** mas cada um vai para um cara diferente, entendeu? Por exemplo, a ficha de AS vai para um cara, o ficha de emergência  
**Off Digital:** Tá, a gente pode botar cada botão de enviar para ir para um lugar diferente ou baixa o pacote zip e aí ele  
**Marcelo Costa:** vaiador.  
**Off Digital:** pega cada parte e manda pro seu respectivo.  
**Marcelo Costa:** Sim,  
**Off Digital:** Ou eu posso botar um botão de baixar para ele baixar aqui o cadastrar ou ele  
**Marcelo Costa:** mas deixa os caras começar a viver o Vamos viver o dia lá,  
**Off Digital:** baixa.  
**Marcelo Costa:** vamos ver o processo para falar. Beleza.  
**Off Digital:** É isso aqui você pergunta pro Marcelo.  
**Marcelo Costa:** Só aqui  
**Off Digital:** Quando a gente mostrar para ele, você pergunta,  
**Marcelo Costa:** precisa  
**Off Digital:** velho, você quer que o cara baixe aqui um a um? Você quer que ele baixe o pacote ou você quer que ele envida aqui direto pro cara?  
   
 

### 00:48:24

   
**Off Digital:** Entendeu?  
**Marcelo Costa:** o certificado hoje já tem se baixar aí o pacote?  
**Off Digital:** Hã,  
**Marcelo Costa:** O certificado já tem o baixar o  
**Off Digital:** certificado. Eu acho que já.  
**Marcelo Costa:** pacote?  
**Off Digital:** Deixa eu ver aqui. Já exportar,  
**Marcelo Costa:** Exportar válidos todos.  
**Off Digital:** voltar e  
**Marcelo Costa:** Tá beleza.  
**Off Digital:** subir.  
**Marcelo Costa:** Depois você testa aí esse para ver o que que ele exporta, porque talvez ele podia exportar só os confere e  
**Off Digital:** Os válidos, né?  
**Marcelo Costa:** eh hã  
**Off Digital:** Os válidos é é os confere, eu acho. Mas vou vou confirmar.  
**Marcelo Costa:** é ô ficou  
**Off Digital:** Eu vou confirmar isso aí. Eh, eu acho que isso é isso,  
**Marcelo Costa:** top. Essa parte aí ficou boa,  
**Off Digital:** eu acho que isso é a última parte. Quando tiver tudo,  
**Marcelo Costa:** velho.  
**Off Digital:** tudo rodando, motor aprovando, tudo subindo, tudo certinho, aí a gente vai nesse detalhe de como a galera vai pegar os documentos,  
**Marcelo Costa:** É. E tem dar operação,  
**Off Digital:** entendeu?  
**Marcelo Costa:** veio ali. Agora é entender porque eu acho que nós vamos mexer na estrutura dele, entendeu? na estrutura de pessoas dele,  
**Off Digital:** Sim,  
**Marcelo Costa:** falar: "Cara, você não precisa mais desse cara, você não precisa mais desse  
   
 

### 00:49:26

   
**Off Digital:** mano, esse essa parte do link aqui você tá entendendo tanto que já resolve,  
**Marcelo Costa:** aqui.  
**Off Digital:** né? Porque velho, você já tem aqui o o lembrete agendado, você já tem aqui todo o esquema, tipo, aí você vê aqui,  
**Marcelo Costa:** Agora o uma  
**Off Digital:** aqui vai aparecer, velho, a foto que o cara tirou vai aparecer aqui, ó, CPTF, comprovante residência,  
**Marcelo Costa:** agora uma pergunta aí. Nessa nesse revisão de documento,  
**Off Digital:** etc.  
**Marcelo Costa:** ele vai est usando aí um um OCR para ver se o documento é, se não é, se é o original,  
**Off Digital:** Uhum.  
**Marcelo Costa:** se não é e tal.  
**Off Digital:** Uhum.  
**Marcelo Costa:** Ele já vai estar fazendo essa validação aí, certo?  
**Off Digital:** Sim.  
**Marcelo Costa:** Ele vai ter algum algum coisa de parcial ou vai ter alguma alguma  
**Off Digital:** Não, conferido,  
**Marcelo Costa:** informação?  
**Off Digital:** vencido, refazer. Refazer é tipo,  
**Marcelo Costa:** Ah, tá bom.  
**Off Digital:** ó,  
**Marcelo Costa:** Tá  
**Off Digital:** página borrada na segunda tentativa, cara. Tem que refazer.  
**Marcelo Costa:** apagadinho.  
**Off Digital:** Comprovante, eh, fora do prazo de 90 dias, tá vencido. Que que você quer fazer com isso? Aprovar? Vai aprovar com observação,  
   
 

### 00:50:19

   
**Marcelo Costa:** Ah,  
**Off Digital:** vai solicitar para refazer.  
**Marcelo Costa:** beleza,  
**Off Digital:** Eh, self não bate com a identidade,  
**Marcelo Costa:** entendi.  
**Off Digital:** cara. Vai, vai, entendeu? Então, é,  
**Marcelo Costa:** Revisa,  
**Off Digital:** é.  
**Marcelo Costa:** vê se é o cara, se é aprova aí ou não,  
**Off Digital:** É isso fica pro cara.  
**Marcelo Costa:** né?  
**Off Digital:** Não adianta querer fazer o negócio 100% automá porque não existe. O cara fez errado.  
**Marcelo Costa:** Não, não. Sim.  
**Off Digital:** O que que você quer fazer? Você quer,  
**Marcelo Costa:** Eu eu não tinha olhado esse ladinho aí que tava também fazendo essa revisão aí.  
**Off Digital:** entendeu? É,  
**Marcelo Costa:** Aí ele pode tá dando confere,  
**Off Digital:** então é,  
**Marcelo Costa:** confere, confere e pau,  
**Off Digital:** tá conferido. Beleza, velho. Tem, não tem o que fazer. Então, confere,  
**Marcelo Costa:** né?  
**Off Digital:** entendeu? Agora selfie aqui, ó, ele dá sugestão aqui. Aqui é sugestão, ó. Self não bate com identidade. Sugestão revisar. Comprovante de renda fora do prazo, vencido. Aí você tem as ações aqui,  
   
 

### 00:51:02 {#00:51:02}

   
**Marcelo Costa:** Mhm.  
**Off Digital:** ó. Conta fora do prazo. Quer aprovar? Ó, esse CPTS já foi aí. Aqui, aqui é MOC, né? Tá errado. Mas, ó, do CPTS, ó, esse CPTS já foi enviado duas vezes. Rejeitado a primeira, última rejeição, dia 19/05 por Fernando Pinheiro, motivo página borrada, aprovar, aprovar com observação ou solicitar  
**Marcelo Costa:** E quando e quando,  
**Off Digital:** refazer.  
**Marcelo Costa:** por exemplo, beleza, o cara passou o processo todo, tenho que refazer só o CTPS, ele vai voltar para trás no fluxo.  
**Off Digital:** Seitar refazer, vai mandar mensagem pro cara, ó, fulano, você precisa refazer.  
**Marcelo Costa:** Só manda esse. Ele vai abrir no link só esse e e  
**Off Digital:** Vai abrir na parte certinha. Ainda tem aqui, ó, template de justificativa.  
**Marcelo Costa:** fecha.  
**Off Digital:** Documento cortado, foto cortou o par de documento, enviar a página inteira na próxima, solicitar, refazer. Vai abrir o link do whats, pum, manda pro cara,  
**Marcelo Costa:** Top. p\*\*\*\*. animal, velho.  
**Off Digital:** entendeu?  
**Marcelo Costa:** Mas esse processo, esse processo, primo, vai ser um outro produto pra empresa de um brother aí que já me pediu que é pra logística que ele tá fazendo e ele precisa contratar lá, velho.  
   
 

### 00:52:08

   
**Marcelo Costa:** Ele tá contratando não sei quantas pessoas, ele precisa fazer esse processo só de documentação. não tem certificado,  
**Off Digital:** Não,  
**Marcelo Costa:** mas esse  
**Off Digital:** isso aqui já vai virar só isso aqui,  
**Marcelo Costa:** processo  
**Off Digital:** priminho. Quanto é que já vale pro Marcelo, velho, que ele te pediu o DP. Olha o que que nós vamos entregar de DP para ele, fora o resto do sistema,  
**Marcelo Costa:** né,  
**Off Digital:** entendeu?  
**Marcelo Costa:** eu tô louco para mostrar para ele.  
**Off Digital:** Então aqui é por isso que não,  
**Marcelo Costa:** O bichinho tá ansioso lá, velho.  
**Off Digital:** nós estamos no over delivery,  
**Marcelo Costa:** E é por isso que eu tô  
**Off Digital:** velho, gigante aqui, mas é isso, é isso. Vamos  
**Marcelo Costa:** de boa. Tô quietinho, velho.  
**Off Digital:** embora.  
**Marcelo Costa:** A hora que ele ver, ele vai falar: "c\*\*\*\*\*\*, velho. Não, a hora que ele ver, vai ficar louco. E velho,  
**Off Digital:** Entendeu?  
**Marcelo Costa:** tô louco para ele ver porque ele vai sair no corre para vender isso aí,  
**Off Digital:** Não vai dar bom para c\*\*\*\*\*\* para mim. Aí, velho,  
**Marcelo Costa:** velho.  
**Off Digital:** eu tô botando a parada fazendo com carinho, mano, porque realmente eu é isso, é para todo mundo se motivar e a gente andar pra frente, entendeu?  
   
 

### 00:52:56

   
**Off Digital:** Então assim, é isso. p\*\*\*\*,  
**Marcelo Costa:** Não vai.  
**Off Digital:** o visual você vê aqui só de mudar a barrinha aqui já ficou mais clean. Então assim,  
**Marcelo Costa:** Ah,  
**Off Digital:** depois eu vou dar uma lapidada  
**Marcelo Costa:** é para mim eu era é um projeto que eu falava assim:  
**Off Digital:** na  
**Marcelo Costa:** "Ah, beleza, vamos fazendo aí. É um projeto, mas eu agora tá o negócio vai ficar louco, velho.  
**Off Digital:** não,  
**Marcelo Costa:** Nós vamos para cima dele como se fosse um business,  
**Off Digital:** primo. Tá doido. Não, velho. Eu não vou entrar na parada para fazer um negocinho,  
**Marcelo Costa:** né?  
**Off Digital:** entendeu, primo, nós já fomos, já metemos. Eu falei: "Não, já tô atolado, já tive que entender o negócio. Agora que eu entendi o negócio, eu não vou fazer qualquer porcaria".  
**Marcelo Costa:** É, foi, cara, você passou a mesma jornada que eu, primo, parecia fácil. Daí eu vou fazer. Aí você vê, p\*\*\*\*, tenho que fazer, tenho que entender. Hoje se o cara perguntar das coisas, nós sabe mais que qualquer um do time  
**Off Digital:** Exatamente. Eu ainda não sei dar as regras porque eu não entrei tanto nisso no dia a dia de entender que marinheiro te  
   
 

### 00:53:38

   
**Marcelo Costa:** dele.  
**Off Digital:** conv é SNR e tal, mas mano, do processo de contratação e de como tratar o cara e de como e de como andar lá dentro, meu irmão, eu já tô já tô craco.  
**Marcelo Costa:** E uma coisa, né, esse processo de admissão, ele ele poderia funcionar no no certificado, né? Imagina que você vai pedindo os certificados e o cara vai mandando. Só que os caras não querem fazer isso, né? O cara quer mandar de lote, entendeu? Era cam mandar de lote. O que acontece também, essa que é uma, tem uma das das preocupações, só que aqui o cara já foi contratado, meu irmão, você já foi contratado. Agora segue o fluxo, velho.  
**Off Digital:** Eh, É,  
**Marcelo Costa:** Aqui você não vai me mandar 200 documentos.  
**Off Digital:** contratado. Não tem conversa. É, não tem conversa.  
**Marcelo Costa:** Aqui você é contratado. Você quer trampar ou não quer, velho? Me fala aí. Não vem, não me mande documento.  
**Off Digital:** Sim,  
**Marcelo Costa:** É aqui esse aí o fluxo.  
**Off Digital:** sim,  
**Marcelo Costa:** assim o processo da empresa,  
**Off Digital:** sim,  
**Marcelo Costa:** velho.  
**Off Digital:** sim. Mas nos certificados aqui, velho, a gente eh já tá nesse nível só a interface não tá tão solidificada para isso.  
   
 

### 00:54:44

   
**Off Digital:** Mas, por exemplo, p\*\*\*\*, temos aqui, vamos pegar um cara aqui que tem pendente, ô Alfredini aqui, cara. Solicitar 21 pendências. Pum. Clicou, vai solicitar, vai abrir a mesma janelinha do com a mensagem pronta que a gente tem aqui no essa janelinha que eu não botei ainda, mas vai ter, ó, essa aqui, ó. Vai ter, ó,  
**Marcelo Costa:** Sim. E aí ele manda pro WhatsApp.  
**Off Digital:** já com a mensagem.  
**Marcelo Costa:** WhatsApp ele manda e aí o cara tem que subir manual, né, no primeiro momento.  
**Off Digital:** Ah, entendi. Do negócio do do KYC que você tá  
**Marcelo Costa:** Não,  
**Off Digital:** falando.  
**Marcelo Costa:** eu tô falando, é, tô pensando no certificado. Quando o cara, por exemplo, eh, pô, tá faltando dois documentos,  
**Off Digital:** Entendi.  
**Marcelo Costa:** ele vai, ele não tá no processo link, ele vai ter que pegar aquele documento e subir, certo?  
**Off Digital:** Sim. Certo.  
**Marcelo Costa:** Mas eu acho que é assim mesmo. O começo, o começo é esse, é esse mesmo.  
**Off Digital:** Não, vamos.  
**Marcelo Costa:** Olhando pro  
**Off Digital:** Eu entendi, eu entendi, eu não tinha pensado nisso de fazer tipo o que a gente tá fazendo em admissão com link pro  
**Marcelo Costa:** lado.  
**Off Digital:** cara fazer também os certificados,  
   
 

### 00:55:53

   
**Marcelo Costa:** É só que o que acontece, eu já sei que isso acontece,  
**Off Digital:** né?  
**Marcelo Costa:** que já é assim, os caras mandam 200 e f\*\*\*-se. Eu não vou fazer, não me manda aqui, eu tô f\*\*\*\*\*  
**Off Digital:** Ah,  
**Marcelo Costa:** no bar.  
**Off Digital:** então aí não adianta fazer o link do do Kyc pro cara mandar de um por um, tirar foto de um por um,  
**Marcelo Costa:** Agora o que vai acontecer,  
**Off Digital:** entendeu?  
**Marcelo Costa:** que eu acho que é bom a gente pensar aí é no processo de admissão, tá? Pensa o seguinte, eu tô fazendo um compli, eu preciso fazer um compli de 20 pessoas aqui e esses caras já me mandaram documento e eu tô com uma pasta de cada um deles aqui. Eu quero subir esses documentos para fazer uma validação.  
**Off Digital:** Aham.  
**Marcelo Costa:** Então a gente poderia ter um automático aí de subir tudo e ele passar o cara no processo que já é  
**Off Digital:** Tá sim.  
**Marcelo Costa:** liso, mas ele ter essa  
**Off Digital:** Aí ele vai vir para essa tela aqui,  
**Marcelo Costa:** opção  
**Off Digital:** ó, de revisar. Ele não vai usar o link, ele vai usar a tela de revisão,  
**Marcelo Costa:** e faz um upload geral aí.  
**Off Digital:** entendeu? p\*\*\*, ele tá no tá no negócio errado aqui agora.  
   
 

### 00:56:51 {#00:56:51}

   
**Off Digital:** Qual que é o Aqui, ó? Pronto, ele faz o upload aqui. Eu ponho uma tela de um botão de upload aqui e ele vai poder aí vai atualizar todos os documentos aqui.  
**Marcelo Costa:** Isso. Pensando no cara assim, vai, vamos que o cara, p\*\*\*\*, tô enroscado aqui, velho.  
**Off Digital:** aqui.  
**Marcelo Costa:** ou todos os documentos ou uma os caras que vão querer fazer, que era o que a Hélix queria fazer, que é uma revisão geral para ver tudo como é que tá o documento dos cards. Então ela vai, ela não vai chamar o cara, ela vai pegar os documentos da pasta, vai jogar tudo aí e vai fazer uma varredura inteira, entendeu? O que pode acontecer?  
**Off Digital:** Vou pensar, vou pensar qual é a melhor forma da gente fazer isso,  
**Marcelo Costa:** É, pense que o  
**Off Digital:** mas eu acho que pro, eu acho que pro MVP,  
**Marcelo Costa:** seguinte,  
**Off Digital:** pra gente pô no ar, eu acho que isso pode ficar pra segunda fase,  
**Marcelo Costa:** não,  
**Off Digital:** porque como você me falou,  
**Marcelo Costa:** não mexa, não mexa agora. Deixa o negócio ir.  
**Off Digital:** não, mas de boa, já tá anotado na reunião aqui na na no  
**Marcelo Costa:** Deixa é pensar pensar porque tá fácil de pôr ele  
**Off Digital:** tranquilo de mim.  
**Marcelo Costa:** no fluxo, né?  
   
 

### 00:57:59

   
**Marcelo Costa:** Mas é só pra  
**Off Digital:** Depois, velho, vai ser a gente fazendo reunião, pegando a reunião, transformando em PR,  
**Marcelo Costa:** gente.  
**Off Digital:** que é em em em PR, não, em issues, né, que é em em em problemas e transformando em iss e mandando pro agente começar a desenvolver esses coldar e eu ficar resolvendo isso lá no Geek Hub e entrando essas atualizações,  
**Marcelo Costa:** É isso.  
**Off Digital:** entendeu?  
**Marcelo Costa:** E eu quero a gente depois pegar a gente a hora que tiver redondia fazer esse treinamento e ir lá em loco e ver o como é que os caras operam e ver o que que tem de particularidade e o que que a gente vai melhorar do processo dele. É até bom fazer sem olhar o processo dele, porque ele tem muito mais burocracia que não  
**Off Digital:** Não,  
**Marcelo Costa:** precisa.  
**Off Digital:** a gente tá redesenhando o processo dele com embasamento global. Esse aqui é o ponto. Tudo tá referenciado. Toda. Por exemplo, essa tela mesmo. Eu fui ver, falei, velho, cara, vê como é que o o Hackman faz e vê como é que é, como é que a gente pode montar esse essa admissão aqui para ele que me sugeriu, ele falou: "Cara, tem que ser admissão. Eh, isso aqui é processo de admissão, você tem que montar uma tela só". Aí ele montou com um monte de botão.  
   
 

### 00:59:08 {#00:59:08}

   
**Off Digital:** Eu eu que aí eu que fiquei pensando, falei: "Cara, esses botão tá um monte de botão um embaixo do outro, confusão". Não, velho. E se a admissão for colapsável? Você clicar, virar tipo um grupinho que abre. p\*\*\*\*, maravilha. Isso aqui a gente já vai pegar de padrão para várias outras telas para em vez de ficar um monte de botão,  
**Marcelo Costa:** Sim.  
**Off Digital:** você clica, já abre, entendeu?  
**Marcelo Costa:** Aí é aí é um processo de K YC,  
**Off Digital:** Então,  
**Marcelo Costa:** velho. Serve para qualquer coisa. O cara quer depois falar assim: "p\*\*\*\*, preciso eh tô abrindo um banco aqui,  
**Off Digital:** mim,  
**Marcelo Costa:** preciso do processo K YC."  
**Off Digital:** só isso aqui é o produto. Só isso aqui, ó, de admissão até formulários é o produto.  
**Marcelo Costa:** É. E a gente pode liberar só essa só essa coisa pro cliente,  
**Off Digital:** Passou.  
**Marcelo Costa:** né? O cara não tem certificado, o cara, pô,  
**Off Digital:** Sim,  
**Marcelo Costa:** libera só isso aqui e aí ele pode construir.  
**Off Digital:** sim.  
**Marcelo Costa:** Ah, não, mas eu tenho aqui um, sei lá, eu preciso que o cara tenha treinamento em abertura de porta. Ah, beleza.  
   
 

### 01:00:00 {#01:00:00}

   
**Marcelo Costa:** Cadastra aqui o treinamento.  
**Off Digital:** Não, a gente a gente pega essa ferramenta,  
**Marcelo Costa:** Como é que é?  
**Off Digital:** a gente tira essa aba de admissão do código, duplica, pega essa aba de admissão, monta um it label, muda o design do white label, deixa a mesma funcionalidade com a mesma estrutura, com outra cara e a gente começa a vender isso para processo de admissão,  
**Marcelo Costa:** Não,  
**Off Digital:** entendeu?  
**Marcelo Costa:** bora para mim. Nós vamos, é isso que nós temos que fazer, cara. Ontem eu vi, ontem eu vi isso, ó, mudando um pouco aí o tem um grupinho aqui do G4, né? Como eu fiz lá.  
**Off Digital:** para mim me dá. Eu preciso,  
**Marcelo Costa:** Os cara Vai,  
**Off Digital:** tô no banheiro rapidão, velho.  
**Marcelo Costa:** vai,  
**Off Digital:** Dá um segundo aí que eu tô apertador.  
**Marcelo Costa:** vai lá. O  
**Off Digital:** Voltei.  
**Marcelo Costa:** Pera aí. tava para mim, tava falando o eh tem um grupo aqui,  
**Off Digital:** Não, o dia  
**Marcelo Costa:** né, quem participou lá, eles vira e mexe manda os negócios onde foi aniversário do G4 e os caras tavam lá zona para 20.000 23.000 pessoas e os cara vendendo, né? E aí aquela mesma coisa,  
   
 

### 01:03:23 {#01:03:23}

   
**Off Digital:** Aha.  
**Marcelo Costa:** velho, igualzinho, não tem não tem, pô, é tal, é aquele negócio, preço, isso aqui tudo, todos os cursos online eternamente valeria 89.000, mas não sei o quê,  
**Off Digital:** Угуm.  
**Marcelo Costa:** b pá. Quando ele começou a falar os números 89, eu falei: "É 2999". Aí errei porque foi 2997 em 12\. Eh, mas no final que que os caras fizeram? Eh, eles criaram lá o G4 OS, que é basicamente o você entra,  
**Off Digital:** M.  
**Marcelo Costa:** então agora, ao invés de você entrar e escolher, ah, eu quero fazer o curso tal, eu preciso do curso tal, você vai passar por um uma namnese que ele vai entender seu negócio e vai te dar qual é a trilha que você precisa fazer, que é o que o Alan faz no curso dele ali. você passa primeiro no anamnese, o cara entende o que você precisa, você não vai sair, ah, eu preciso fazer o o o gestão,  
**Off Digital:** M.  
**Marcelo Costa:** eu preciso fazer, não, ele vai te dar esse esse construção. Além disso, eles construíram um motor que você vai plugar seu CRM, seus dados, seu RP, não sei o quê, e vai consolidar todas as informações da sua empresa em um único local.  
   
 

### 01:04:35

   
**Marcelo Costa:** Então você vai falar: "p\*\*\*\*, que que eu preciso falar o time de venda? Ô, que que foi os?" Então assim, eles organizaram para que você consigu como se fosse um MCP ali que você pluga tudo e ele vai fazer um e vai usar, lógico, cruzando as informações de tudo que eles têm de de treinamento de empresa. Então, construir uma base sólida ali, ele fala com 100.000 empresas, com que deu certo, que não deu, todos os negócios. Então você vai ter tipo um copiloto treinado com 100.000 negócios e tal. Então assim,  
**Off Digital:** com os dados dele.  
**Marcelo Costa:** hã, achei massa a ideia e tal,  
**Off Digital:** Aham.  
**Marcelo Costa:** mas é basicamente é o que todo tá todo mundo fazendo, né, primo, consolidando  
**Off Digital:** É o aí, aí vamos lá,  
**Marcelo Costa:** dados.  
**Off Digital:** né, prim? Guerra dos dados, né? Quem tem dados e quem sabe organizar os dados vai ser sobre isso, né?  
**Marcelo Costa:** Exatamente, velho. E é e não é difícil, nada difícil assim de fazer. Os caras t dados, né? Eles têm muita informação, os caras são marqueteiro para c\*\*\*\*\*\*, né? Mas a galera fissurada no no chat, né?  
   
 

### 01:05:35 {#01:05:35}

   
**Marcelo Costa:** Você vê quem quer os car eu, eu, e eu e eu os caras, velho, devem ter feito ontem brincando ali uns deve ter vendido uns 1000 fácil de 20.000 pessoas, velho. A 299 eh 12 de 299, meteram 3 4 milho. Ali fácil,  
**Off Digital:** É,  
**Marcelo Costa:** mas uma estrutura que eu não quero ter, velho, tá ligado? Não tenho.  
**Off Digital:** né?  
**Marcelo Costa:** Antes eu antes eu tinha o tesão de, p\*\*\*\*, quero ter uma empresa, pá. Não sei o que hoje eu não falo, velho.  
**Off Digital:** Não, para, velho.  
**Marcelo Costa:** Quero ter dois agentes,  
**Off Digital:** É,  
**Marcelo Costa:** velho.  
**Off Digital:** cara, é mais uma vez ontem eu vi um post e eu e eu sempre vejo esse post de alguns e alguns dias de  
**Marcelo Costa:** Eu  
**Off Digital:** pessoas diferentes postando a mesma coisa. E aí eu sempre vejo, eu falo: "Hum, é aquela confirmação, a galera falando, velho, cada vez mais caindo gap entre uma empresa de 10.000 pessoas e uma empresa de uma pessoa e cada vez mais cai." E cada vez mais cai, entendeu? A gente tá chegando no  
**Marcelo Costa:** vi, eu vi um cara também,  
**Off Digital:** momento,  
   
 

### 01:06:30 {#01:06:30}

   
**Marcelo Costa:** um post também de um cara que teve várias empresas e agora tá construindo uma sozinha.  
**Off Digital:** não é? É, primi, nós estamos no caminho certo, velho. Eu vi um cara muito quente ontem falando, galera, tem dois tipos de pessoas atualmente que estão no mercado de trabalho. a pessoa que usa cloud code, cursor, eh, lobbel, eh, as ferramentas de sofisticadas e que tá construindo com elas, as pessoas que usam chat GPT, eh, gemina e e Iá da meta e as pessoas que não usa IA. Se você tá na primeira categoria, não se preocupe mais na sua vida que vai, você vai ganhar muito dinheiro, independente do que você faça.  
**Marcelo Costa:** É,  
**Off Digital:** E tipo, é um cara muito casca, ele não  
**Marcelo Costa:** é porque a galera não vai dar,  
**Off Digital:** é  
**Marcelo Costa:** a galera não vai chegar ali, né, primo? Não vai chegar, não vai olhar, não vai conseguir. A galera não evolui pro que nós estamos fazendo, né?  
**Off Digital:** não vai ter uma galera ou outra que vai acabar migrando ao longo do tempo e tal, mas a gente, como a gente tá pegando o acontecimento do negócio, a gente vai est sempre um passo na frente, porque imagina o cara, ele entra lá na frente, mas até ele entender o que é MCP, o que é CLI, como que ele Ele monta o obsidian, como que ele faz no seu das quantas?  
   
 

### 01:07:56 {#01:07:56}

   
**Off Digital:** Nós já estamos aqui,  
**Marcelo Costa:** É do anos. É dois anos,  
**Off Digital:** ó.  
**Marcelo Costa:** velho,  
**Off Digital:** Nós já estamos explodindo a boca do balão. Então, mano, sinceramente,  
**Marcelo Costa:** estudando.  
**Off Digital:** primo, eu vi uma live do Alan ontem. Ontem não, ante esses dias, anteontem. E eu vi ele mexendo nas coisas. Eu vi os projetos dele aparecendo no codex, eu vi as configurações, eu vi ele abrindo o prompt que ele usa de configuração, tá ligado?  
**Marcelo Costa:** Eu vi essa,  
**Off Digital:** Porque ele ele vai mexendo,  
**Marcelo Costa:** eu vi essa aula aí.  
**Off Digital:** ele vai mexendo ali, você vai vendo os detalhes, né, para mim, pela primeira vez eu vi o Alan e eu falei: "Velho, eu tô para pau com o cara".  
**Marcelo Costa:** É, ele não  
**Off Digital:** Pela primeira vez eu vi e eu falei:  
**Marcelo Costa:** tá.  
**Off Digital:** "Velho, top pau a pau". Tá ligado? É  
**Marcelo Costa:** E ele é que ele decidiu mostrar,  
**Off Digital:** isso  
**Marcelo Costa:** né, e tá ali fazendo porque beleza, conseguiu fazer dinheiro disso agora,  
**Off Digital:** não, eu acho que há uns meses atrás ali todo aquele trampo que ele tinha do Obsidian, do não sei o quê, de parará, era uma parada que deixava ele com uma vantagem maior e tal,  
   
 

### 01:08:39

   
**Marcelo Costa:** Mais  
**Off Digital:** mas eu acho que hoje assim de verdade, mano, eu vi o eu vi o setup dele, eu vi, dá para ver quando, tipo, quando você vê aqui os projetos aqui do lado, o prompt que o cara usa, o jeito como ele usa as skills, você vê Qual que é o nível do cara? Entendeu? Como eu vejo alguns caras que eu assisto os vídeos, eu falo: "Put, esse cara tá na frente". Eu vejo o sistema dele, eu falo: "p\*\*\* que pariu, sistema do cara, nem se eu nem se eu der um gás aqui dois meses todo dia eu não chego." O Alan não foi um cara que eu bati  
**Marcelo Costa:** Eh,  
**Off Digital:** o olho e falei: "p\*\*\*, já cheguei".  
**Marcelo Costa:** o que ele tá fazendo dá, tô fazendo aqui,  
**Off Digital:** Tô falando ele com a máquina,  
**Marcelo Costa:** né?  
**Off Digital:** né? Não tô falando empresa,  
**Marcelo Costa:** Não é o que o cara conseguiu,  
**Off Digital:** não tô falando que tá dentro da É,  
**Marcelo Costa:** que o cara conseguiu fazer,  
**Off Digital:** não tô falando network,  
**Marcelo Costa:** né?  
**Off Digital:** não tô falando que ele sabe por trás dos panos, não tô falando que tá dentro da cabeça do cara, mas tô falando assim: "Põe um computador na minha frente e e um computador na frente dele, põe os dois sentados e põe uma tesque, mano.  
   
 

### 01:09:44

   
**Off Digital:** É competição na mesma categoria, é é o mesmo peso,  
**Marcelo Costa:** É,  
**Off Digital:** entendeu? A mesma liga,  
**Marcelo Costa:** é, eu não,  
**Off Digital:** sacou?  
**Marcelo Costa:** eu acho que você já evoluiu mais. Eu não consigo ainda não tô nisso, mas eu vejo que eh é é isso, tem que ficar enfiando a mão na massa e fazendo. Você é escola, velho. Isso aí, esse projeto, velho, isso aí é uma escola, velho.  
**Off Digital:** É a escola.  
**Marcelo Costa:** Você fez aí  
**Off Digital:** É porque para mim eu tenho esse background,  
**Marcelo Costa:** é  
**Off Digital:** né, velho, de produção musical. Produção musical você tem que ser muito noia, velho. É muita noia para você.  
**Marcelo Costa:** fluxo, fluxo de coisa,  
**Off Digital:** Muita noia,  
**Marcelo Costa:** né?  
**Off Digital:** velho. Você tem que manjar de um monte de coisa, cara. Você tem ferramenta para fazer um monte de coisa para me caras para instalar as coisas é maior pica. Eu mexo com terminal há muitos anos só para instalar coisa de áudio, velho. Tudo você tem que abrir o terminal, botar lá os códigos para craquear o negócio,  
**Marcelo Costa:** É,  
**Off Digital:** para fazer acontecer.  
**Marcelo Costa:** já é uma vivência,  
**Off Digital:** É, eu já tenho esse essa essa carcaça de de  
   
 

### 01:10:33 {#01:10:33}

   
**Marcelo Costa:** né?  
**Off Digital:** de não de dev, mas de tipo assim, de cara que vai fundo no nas ferramentas.  
**Marcelo Costa:** Sim.  
**Off Digital:** Então, por causa da produção, então isso acelera muito o jogo, né, velho? E ainda mais quando você tem os copilotos que, tipo, te não te faz perder tempo, né? Eh, e aquela coisa, né, priminho, e botando o bolso para jogo, né, velho? Tá aqui, ó, na minha tela. Você tá vendo aí, ó,  
**Marcelo Costa:** É não, velho.  
**Off Digital:** 36% do Codex. Vamos ver quanto que nós gastamos últimos 7 dias. 7 bilhões de tokens aqui no Codex, ó. Cloud Code 2.8 B, foi pouco. Cursor, o cursor não tem os tokens aqui, mas, ó, já gastei 38% do meu do meu plano de um mês. Aqui demora um mês para resetar, falta 26 dias. E o meu plano já é o de 60 do cursor aqui.  
**Marcelo Costa:** Eh,  
**Off Digital:** O Grock, meu planinho de 30 aqui também do Grock,  
**Marcelo Costa:** vai  
**Off Digital:** ó, 24% usado. Eu tô usando o Grock aqui, ó. Mostrar. Tá vendo? Aqui é o Grock, ó.  
   
 

### 01:11:49

   
**Off Digital:** Como é que ele é no terminal? Diferente a parada dele.  
**Marcelo Costa:** sim.  
**Off Digital:** Você clica nos bagulhos, ó. Tá vendo? Você clica nas parad. É maior, é toda diferente ele.  
**Marcelo Costa:** É, ele é desenroladão, né?  
**Off Digital:** E eu tô usando porque o Hello Musk, pô, eu montei um bagulho aqui, priminho. Deixa eu deixa eu ver se já dá para te se dá para mostrar. Daqui a pouco eu vou ter que aqui, ó. Tô montando ainda,  
**Marcelo Costa:** Só  
**Off Digital:** mas é um negócio que tá ligado aqueles os salvos.  
**Marcelo Costa:** perí.  
**Off Digital:** Quando você salva o post,  
**Marcelo Costa:** Hã,  
**Off Digital:** que vai aquele iconezinho do salvo,  
**Marcelo Costa:** sei sim.  
**Off Digital:** vai salvando, poxa, né? Você vai ver no Instagram,  
**Marcelo Costa:** Vai para o salvar,  
**Off Digital:** vai pro salvo.  
**Marcelo Costa:** vai para alguma coisa.  
**Off Digital:** O Twitter tem o salvar também, chama Bookmark, o do Twitter. E eu salvo muita coisa de valor,  
**Marcelo Costa:** Eh,  
**Off Digital:** velho. Muita coisa, muita coisa. E muitas das vezes eu não tenho tempo de olhar as coisas que eu salvei, p\*\*\*\*. Eu sei que tem uns negócios monstro lá que eu falo,  
   
 

### 01:12:47 {#01:12:47}

   
**Marcelo Costa:** sempre.  
**Off Digital:** velho, c\*\*\*\*\*\*, p\*\*\* que pariu. E aí, velho, o cara do Open Cloud, o Stay Pit lá, lançou uma ferramenta que consegue acessar teus bookmark do Twitter através de um CLI maluco com API do Twitter, mais uns negócios aí. Enfim, eu tô usando a ferramenta dele e eu tô construindo uma camada em cima e é uma toda uma automação maluca que a cada 24 horas ele vai trazer os bookmarks para mim, basicamente. E aí eu tô montando isso no estilo New York Times. Então ele vai dar para mim um jornal do dia dos meus  
**Marcelo Costa:** dos do que seja. já  
**Off Digital:** salvos. Dos meus salvos.  
**Marcelo Costa:** marcou.  
**Off Digital:** Exatamente. E aí, p\*\*\*\*, velho, eh, ele vai vir aqui, cara, filezão com conteúdo em português.  
**Marcelo Costa:** Ele podia juntar por categoria, né, velho?  
**Off Digital:** Hã,  
**Marcelo Costa:** Podia juntar por categoria,  
**Off Digital:** depois eu vou, é, depois eu vou começar a lapidar essas coisas,  
**Marcelo Costa:** né?  
**Off Digital:** tipo, por causa coluna e salva, interagir, LLM, que que LLM faz por cima. Mas o que eu quero, mano, é abrir uma página tipo essa, como se fosse um jornal. Imagina, em vez de ler o jornal, eu vou abrir o meu jornal.  
   
 

### 01:13:59

   
**Off Digital:** E o meu jornal vai ser o meu salvos das últimas 24 horas.  
**Marcelo Costa:** Sim.  
**Off Digital:** E aí você vai ter aqui a headline, você vai ter aqui o que é o post traduzido, porque é tudo em inglês. Aí vai ter uma chavinha para inglês e português. E velho, já aí aqui,  
**Marcelo Costa:** Você tipo você salva para ver depois e aí tem uma hora que você vai ver depois. Ele vai apresentar para você tal dia.  
**Off Digital:** só que eu não quero ir lá no meu salvo ver um monte de post,  
**Marcelo Costa:** Sim. Isso aqui ele é organizadinho.  
**Off Digital:** eu quero aqui ver o bagulho clean, velho, visual.  
**Marcelo Costa:** Не.  
**Off Digital:** E aqui tá o conteúdo do post. Esse aqui é o conteúdo do post já e em português. Esse aqui é o post. Esse aqui é um post que fala sobre, ó, consegui fazer o cloud soar como eu e tá meio que arruinando minha capacidade de distinguir qual quais rascunhos eu mesmo escrevi, se é o post que eu salvei, né? Aí ele botou aqui, ó, único arquivo voice DNA substitui setups complexos. 95% já vem pronto. Pá, pá, pá. Aí o aqui era o a camada de texto do post do cara, né?  
**Marcelo Costa:** Já.  
   
 

### 01:14:56

   
**Off Digital:** conseguir fazer o cloud soar como eu e também o que tá é apenas um arquivo. Eu tô dando conteúdo complexo abaixo. Você copia e cola no contexto do cork do cloud para pá pá onde achar suas amostras tal tal tal tal tal. Aí aqui tá o prompt a foto do prompt que ele postou entendeu? Beleza. Aí aqui ele já me deu o passo a passo que não tinha no post.  
**Marcelo Costa:** Ага.  
**Off Digital:** Aí depois eu vou botar e o esquema de diagrama para você ver aqui, ó. Cadê? Ó, o Grock aqui, ó.  
**Marcelo Costa:** Grock. mesmo que já já tem. Ah, você pegou esse negócio dele, mas tem que rodar no Grock.  
**Off Digital:** Cadê o preview? É, eu tô usando o Grock para fazer esse tram, porque como ele manja de Twitter, ele tá me ajudando a fazer da melhor forma que funciona com o Twitter,  
**Marcelo Costa:** Isso.  
**Off Digital:** tá ligado? Então aqui, ó, cadê? Deixa eu ver se tem um link aqui que ele tinha subido no local host aqui, ó. Você vê um link aí, você me aqui, ó, servidor aqui. Aqui é o esquema que eu tô criando com ele de diagrama, ó. Aqui ele vai trazer, ele vai dividir em parágrafos e vai trazer, ó, a maioria das pessoas tenta ensinar o cloud na hora.  
   
 

### 01:16:13

   
**Off Digital:** Joga alguns exemplos de comércio, pede para ele limitar o tom, tóce para dar certo. Funciona mais ou menos até a próxima sessão. Aí diagrama, saída genérica do cloud, voice DNA, saída com a sua voz filtrada. Então ele vai inserir, depois de fazer todo isso aqui, ele vai pegar isso aqui e vai ler e vai botar vários diagramas e vai botar várias eh insightes de LLM em cima. Isso. Eu tô eu tô fazendo a parte para depois  
**Marcelo Costa:** É, depois tem que fazer uma newsletter e começar a fazer conteúdo para  
**Off Digital:** eu  
**Marcelo Costa:** mim.  
**Off Digital:** Exatamente.  
**Marcelo Costa:** É, esse é  
**Off Digital:** Exatamente. Só que isso aqui, velho,  
**Marcelo Costa:** o  
**Off Digital:** é isso aqui, cara, é pro meu consumo, porque é muito conteúdo de valor, cara. Hoje eu não consigo mais consumir conteúdo,  
**Marcelo Costa:** É,  
**Off Digital:** porque eu não tenho tempo.  
**Marcelo Costa:** não, não dá tempo de olhar,  
**Off Digital:** O tempo que eu tenho é para passar a timeline e salvar as coisas,  
**Marcelo Costa:** né?  
**Off Digital:** mas eu não tenho tempo para consumir o conteúdo de verdade,  
**Marcelo Costa:** para olhar. Ué, não dá.  
**Off Digital:** tá ligado?  
**Marcelo Costa:** Você tem que escolher, né, para onde vai,  
**Off Digital:** Exato, mano. Então aqui, pô, eu tô fazendo alinhado pro mobile.  
   
 

### 01:17:05

   
**Marcelo Costa:** né?  
**Off Digital:** Então, pô, quando eu tiver ali de boa, com tempo, eu vou abrir isso aqui. Em vez de ficar abrindo a a rede social para passar para baixo, eu vou abrir isso aqui já estruturado para consumir o negócio direito, entendeu?  
**Marcelo Costa:** Sim.  
**Off Digital:** E aí eu tô montando, já tá tudo automatizado. O pipeline eh, tá no meu servidor, tudo configurado já pela ferramenta. Então ele pega o o bookmark dos 24 das 24 horas e me dá aqui, ó. Esses aqui foram oito postos que eu salvei nas nas últimas 24 horas. Então tá aqui.  
**Marcelo Costa:** Top.  
**Off Digital:** Aí eu vou ter os  
**Marcelo Costa:** Ô, depois me manda. Eu tô querendo, eu tô querendo. Eu sempre olho, eu fico às vezes fico fuçando no Instagram, né?  
**Off Digital:** dias.  
**Marcelo Costa:** Aí tem os carinhas que eu sigo aqui e tal, mas é tudo você vê os carinhas falando, eu vejo umas coisas legal e tal de fazer, mas é do Brasil, os caras estão fazendo exatamente isso, pegando alguma coisa lá e fazendo aqui, né? Agora tem que pegar as fonte direta lá. Depois me passa uns uns caras para eu seguir que eu quero, eu não uso Twitter, velho, mas eu quero migrar, tipo, não olhar mais para Instagram, velho, que eu acho uma bosta aquilo.  
   
 

### 01:18:13

   
**Off Digital:** p\*\*\*\*, prim, eu eu tenho muitos anos já, né, que eu sou só Twitter. Mas, velho, é p\*\*\*\*, é outra vida. Você sente que, pô, eu tô na rede social assim que eu tô sendo produtivo, velho. Eu falo: "c\*\*\*\*\*\*, isso aqui é da hora para c\*\*\*\*\*\*. p\*\*\*, isso aqui é da hora". Aí vem uma notícia, aí vem algum insite de cripto, aí vem alguma coisa, tipo, não é nada. Não tem, mano. Ficar vendo conhecido, ficar vendo o fulano que tá na festa,  
**Marcelo Costa:** É, não, não, eu nem vejo conhecido.  
**Off Digital:** fulano que tá em tal lugar, ah,  
**Marcelo Costa:** Ah, né?  
**Off Digital:** porque fulano teve filho,  
**Marcelo Costa:** Saí.  
**Off Digital:** não teve nada disso, velho. É só, meu irmão, cloud, crirypto, tá ligado? Notícia da hora. Exato. Então eu tô montando esse negocinho aqui, velho, porque eu cheguei no ponto que eu falo, velho, eu eu tô com tanta coisa de valor, velho. Tipo, esse aqui mesmo, é para ele ele ele monta um pipeline que é para você exportar todos os seus e-mails, todo o seu WhatsApp e várias paradas para você treinar o Cláudio a falar igual você.  
   
 

### 01:19:09 {#01:19:09}

   
**Off Digital:** Cara, o negócio besta. Você fala assim: "Pô, mas isso aí eu já sei, cara,  
**Marcelo Costa:** Não,  
**Off Digital:** beleza,  
**Marcelo Costa:** mas ele é p\*\*\*\*, velho. Aí você vai falar com o bicho,  
**Off Digital:** mas velho,  
**Marcelo Costa:** ele já tá fala igual, responde igual você,  
**Off Digital:** então, mas aí você fala: "Pô, isso aí eu já sei fazer,  
**Marcelo Costa:** né?  
**Off Digital:** é só eu pegar lá, fazer caraus, se você aponta um material desse pro teu cloud, ele já vai falar: "Cara, eu só preciso que você me providencie isso, isso isso você não vai ter que explicar para ele, ó, velho,  
**Marcelo Costa:** É outra.  
**Off Digital:** eu quero fazer um negócio para você falar igual eu,  
**Marcelo Costa:** Você já pega mastigado, já tá, já tá  
**Off Digital:** entendeu? Então, velho,  
**Marcelo Costa:** pronto.  
**Off Digital:** eu eh eu quero ter esse acervo para eu ler e para eu poder mandar os meus agentes para ele e falar:  
**Marcelo Costa:** Sim. falou, ó,  
**Off Digital:** "Velho,  
**Marcelo Costa:** dá uma olhada lá e vejo isso  
**Off Digital:** quero fazer isso, mano. Quero fazer o Cláudio falar com a minha voz. Vamos lá, vou tenho meia hora para fazer isso.  
**Marcelo Costa:** aqui.  
**Off Digital:** Tá aqui o o meu o meu jornal que diz: "O que que você tem que fazer, como os insightes, vai lá, bora, vamos trabalhar, que que você precisa de mim. Ah,  
   
 

### 01:19:57

   
**Off Digital:** isso, isso, isso, beleza, vamos testar. Testei, tá dando certo, beleza, aí já vai pro git, aí já é outra história, entendeu? Mas é f\*\*\*  
**Marcelo Costa:** Sim.  
**Off Digital:** porque você lembra da ideia, você fala: "Pô, velho, deixa eu ir lá no naquele post do Twitter".  
**Marcelo Costa:** Não, você nunca mais volta. Nunca mais volta.  
**Off Digital:** Aí você abre o o o teu salvos. Aí antes de você chegar nesse, você já vê cinco outros que você fala: "Pô, mas eu também tenho que fazer isso aqui,  
**Marcelo Costa:** E outra e era massa,  
**Off Digital:** velho.  
**Marcelo Costa:** né? E era massa os outros que você salvou também.  
**Off Digital:** Também.  
**Marcelo Costa:** Então aí,  
**Off Digital:** Aí você fala: "Pô, velho,  
**Marcelo Costa:** aí o cara TDHzão já era,  
**Off Digital:** aí no meio do aí no meio do caminho entre achar o bagulho,  
**Marcelo Costa:** meu irmão.  
**Off Digital:** você já tá fazendo outro bagulho que também é massa, mas não era isso." Então, velho, eh, é isso. E o, pô, e o Marco S lá, mano,  
**Marcelo Costa:** Depois ele vai ter isso,  
**Off Digital:** o bagulho tá exato,  
**Marcelo Costa:** newsletter dele,  
**Off Digital:** velho. Depois tudo vai integrar nele.  
   
 

### 01:20:41 {#01:20:41}

   
**Marcelo Costa:** né?  
**Off Digital:** Então, assim, velho, o bagulho tá ficando, Deixa eu ver se eu tenho ele aqui para para te mostrar aqui.  
**Marcelo Costa:** Eu  
**Off Digital:** Dev no electro. Vou te mostrar como é que tá a cara dele para você ter uma ideia. Eu tô trampando nele no paralelo,  
**Marcelo Costa:** vi aquela,  
**Off Digital:** por exemplo.  
**Marcelo Costa:** você me mandou, você me mostrou ele,  
**Off Digital:** Não, já mudou demais, já é outra coisa.  
**Marcelo Costa:** né?  
**Off Digital:** Por exemplo, ontem eu tinha 50% do cloud sobrando, velho. Eu abri vários projetos e fiquei mandando tesque no celular para ele, velho. Abri umas quatro abas porque,  
**Marcelo Costa:** Faz aí, né, velho?  
**Off Digital:** tipo assim, no certify eu já tava indo num bagulho muito sério. Eu não podia mexer com nada, tem que esperar ele terminar de rodar porque senão é comit em cima de comit, não sei das quantas. em outros projetos que tão parado, velho. Eu mandei ele falou: "Velho, pesquisa sem repo do GitHub que encaixa aqui com meu  
**Marcelo Costa:** É, outro dia eu também fui dormir aqui.  
**Off Digital:** projeto.  
**Marcelo Costa:** Velho, pega aqui minhas reunião toda, faz uma análise, vê minhas reunião, faz um não sei o quê,  
**Off Digital:** Vai trabalha aí,  
   
 

### 01:21:40 {#01:21:40}

   
**Marcelo Costa:** faz alguma coisa,  
**Off Digital:** irmão. Vai, vai, vai se mexe." Então, nessas nessas viradas de semana é que eu tô andando no Marco OS,  
**Marcelo Costa:** velho.  
**Off Digital:** entendeu? que eu tô tomando para ele. Falo, velho, faz 50 mocap aí de de aba nova para mim, velho. Põe aí, abre um HTML aí para mim com três variação de cada tela, cara.  
**Marcelo Costa:** É,  
**Off Digital:** Uma diferente da outra.  
**Marcelo Costa:** faz alguma coisa aí.  
**Off Digital:** Fé, faz aí o negócio.  
**Marcelo Costa:** Ô priminho, você trampa, você trampa com o com o teclado do computador?  
**Off Digital:** Computador.  
**Marcelo Costa:** Ele fica embaixo. Então, sua tela maior tá  
**Off Digital:** eu fico com o notebook aberto aqui na minha frente usando a a eu não uso o mouse,  
**Marcelo Costa:** em  
**Off Digital:** eu uso tudo no trackpad,  
**Marcelo Costa:** você usar um trackzinho.  
**Off Digital:** no computador e e o e o monitor conectado no  
**Marcelo Costa:** É, é que eu eu gosto de usar o bichinho.  
**Off Digital:** computador.  
**Marcelo Costa:** Tá mais alto aqui na tela. Eu uso um tecladinho, mas eu comprei um que chegou hoje, velho. Tecladinho top, ó.  
**Off Digital:** Deixa eu ver o Logitechzinho.  
**Marcelo Costa:** É,  
   
 

### 01:22:35

   
**Off Digital:** Hum. bala.  
**Marcelo Costa:** p\*\*\*\*. E ele e aí ele eu tava com um que era aquele é uns mais porcariazinha da Microsoft  
**Off Digital:** Perdão.  
**Marcelo Costa:** aqui, que ele não era igual Mac, né? Usava no PC. Aí agora esse aqui tem as todas as teclas do Mac.  
**Off Digital:** Aham. Ah,  
**Marcelo Costa:** Agora ele fou é ele,  
**Off Digital:** ele ele vem paraa Mac da  
**Marcelo Costa:** p\*\*\*\*,  
**Off Digital:** Logitech.  
**Marcelo Costa:** ele é exatamente a mesma, ele tem os mesmos botãozinho, né? Ó.  
**Off Digital:** p\*\*\*\*, priminho. Animal.  
**Marcelo Costa:** E ele acende, ele acende as luzinhas,  
**Off Digital:** É, esse é um tesão,  
**Marcelo Costa:** talquinho.  
**Off Digital:** eu tô ligado.  
**Marcelo Costa:** E ele é tipo o mecanismo dele é gostosinho,  
**Off Digital:** Esse esse esse é mecânicozinho,  
**Marcelo Costa:** sabe? É tipo um É,  
**Off Digital:** pô. Top demais. Top de cara, eu eu também eu era nó.  
**Marcelo Costa:** eu uso esse mouse aqui, já viu esse mouse?  
**Off Digital:** Já já tá bom ficar mais assim.  
**Marcelo Costa:** Isso aqui também tem vários botão embaixo, tal.  
**Off Digital:** É,  
**Marcelo Costa:** Você abre umas  
**Off Digital:** é. Esse a galera tá usando muito, primi.  
   
 

### 01:23:21

   
**Off Digital:** Eu,  
**Marcelo Costa:** telas.  
**Off Digital:** eu, eu era dessa pegada. Eu quando eu produzia, eu tinha trackpad, aquele de bolinha. trackpad, não, aquele mouse que tem a bolona, que ele fica parado,  
**Marcelo Costa:** Sim,  
**Off Digital:** porque ainda no estúdio eu trabalhava com mesa de som e aí você não tem espaço para girar o mouse.  
**Marcelo Costa:** sim.  
**Off Digital:** Então eu ficava com o mousezão parado só no trackpad e o tecladinho da Apple aqui. E aí em casa eu tinha o setup gamer, eu tinha o PCzão com o mouse, teclado mecânico, mouse com aqueles mousepad gigantesco e era velho cszão comendo  
**Marcelo Costa:** Sì.  
**Off Digital:** pôker Poker Stars, mano. a ficha. Só que aí quando eu fiz o projeto lá, que eu lancei a música com Vintage, que eu comecei a viajar, a tocar, eu, mano, vi que os produtor tava na noia de produzir só no laptop, porque quando você tá no hotel você não fica dependente, mano. E é f\*\*\* porque imagina,  
**Marcelo Costa:** É,  
**Off Digital:** você tá todo acostumado lá com os teclado, com base cheio de parafernalha, quando você fica no tecladinho,  
**Marcelo Costa:** a vida muda,  
**Off Digital:** você a vida muda.  
**Marcelo Costa:** velho.  
   
 

### 01:24:21 {#01:24:21}

   
**Off Digital:** Então, eu me acostumei, velho. Me acostumei a ficar no perrengue porque para mim é o natural, entendeu? Então eu com o meu laptop, velho, qualquer lugar do mundo, eu performo a mesma coisa, sacou?  
**Marcelo Costa:** É, senão você tem que levar, né?  
**Off Digital:** Só que hoje isso não faz tanto sentido para mim,  
**Marcelo Costa:** Senão você tem que levar.  
**Off Digital:** porque eu já não viajo tanto,  
**Marcelo Costa:** É,  
**Off Digital:** não tenho essa parada de vida de  
**Marcelo Costa:** eu tô 95 99% do tempo no computador,  
**Off Digital:** hotel.  
**Marcelo Costa:** então eu comecei a montar aqui uma estruturinha, né? O legal desse desse coisinho aqui também que eu tenho o iPad aqui também e ele e você conecta ele ele e o mouse nos dois nos dois no nos dois. Então, tipo, eu quero digitar no iPad, ele eu só aperto um botãozinho aqui,  
**Off Digital:** Hum.  
**Marcelo Costa:** ele já cai pro iPad, entendeu? Já tá já tá no Bluetooth do iPad,  
**Off Digital:** É mesmo,  
**Marcelo Costa:** o mouse também.  
**Off Digital:** c\*\*\*\*\*\*. Velho, esse negócio tá muito moderno,  
**Marcelo Costa:** Então o bichinho fica,  
**Off Digital:** mano. Você é louco.  
**Marcelo Costa:** bichinho fica monstro.  
**Off Digital:** Você é louco.  
   
 

### 01:25:12

   
**Off Digital:** Eu tenho que me atualizar nisso. Eu eu nem tô olhando para isso agora para mim. Eu tô, velho, constrói, constrói, porque, mano, por exemplo, meu computador, velho, eu comprei há 5 anos atrás, 4 anos e meio atrás, eu comprei em Nova York quando saiu o M1, o primeiro que saiu. Paguei 29 pau nesse computador na época. Comprei o top, botei 1 ta de SSD.  
**Marcelo Costa:** Car,  
**Off Digital:** Na época os SSD de notebook era 128\. Eh, eu botei 1 ta de SSD.  
**Marcelo Costa:** é o pro, né?  
**Off Digital:** É o, é o Pro M1. Foi o primeiro que saiu antes. Ele era i7, ele não tinha M1, entendeu? Calma aí. Subiu só a janela aqui. Não sei o que que foi. p\*\*\*\*, velho. Eu quero te mostrar um negócio aqui, ó. Priminho. Eu tô construindo nesse nesse negócio aí, ó, no Electron. Cadê? Deixa só.  
**Marcelo Costa:** Tá aberto um electro aqui para mim. Eu tô vendo  
**Off Digital:** É, mas ele não tá servindo.  
**Marcelo Costa:** eléctro.  
**Off Digital:** A, Cadê o cursor, velho?  
   
 

### 01:26:21 {#01:26:21}

   
**Off Digital:** Eu  
**Marcelo Costa:** Para mim, eu vou ter que entrar umas 16 aqui,  
**Off Digital:** também. Então,  
**Marcelo Costa:** velho.  
**Off Digital:** a gente vai receber uma visita agora 16\. Eu preciso me liberar aqui. Mas beleza, depois eu te mostro com calma. Mas o bichinho tá velho.  
**Marcelo Costa:** Tá bom.  
**Off Digital:** Aqui, ó. Só o cheirinho dele para você ver.  
**Marcelo Costa:** Ah, ele ficou mais nervoso agora.  
**Off Digital:** Eh, não, o bichinho tá ficando embaçado. Essa aba aqui é a aba dos agentes. Você abre aqui. Vixe, velho. Você vai ver,  
**Marcelo Costa:** Ah,  
**Off Digital:** mano. Tô fazendo um bagulho em mim.  
**Marcelo Costa:** agora ficou escurinho.  
**Off Digital:** Vamos embora. Vamos trabalhar, velho.  
**Marcelo Costa:** Tá bom, valeu.  
**Off Digital:** Vamos trabalhar aqui.  
**Marcelo Costa:** Valeu, o papo aí. Vamos para cima, ó. Que você precisar aí me avisa aí. Eu tô precisar de ajuda  
**Off Digital:** Tá bom. Tá bom. Eu queria depois quando você puder você manda aquele troquinho lá para mim para ajudar a pagar  
**Marcelo Costa:** aí, mano. Eu tô esperando, eu tô esperando entrar uma grana aqui,  
**Off Digital:** os cartão aqui.  
**Marcelo Costa:** primo, que eu tô achando o cara me empurrou por dia 3\.  
   
 

### 01:27:22

   
**Off Digital:** Hum.  
**Marcelo Costa:** Então,  
**Off Digital:** Tá bom.  
**Marcelo Costa:** eu acho que não vai entrar antes,  
**Off Digital:** Tá o fim da semana aí. Hoje é 26\.  
**Marcelo Costa:** não vai entrar antes disso, velho.  
**Off Digital:** Tá não, de boa. Tranquilo. Sem sem noia.  
**Marcelo Costa:** Tá.  
**Off Digital:** Eh, só que vai ajudar na fatura mesmo desse mês  
**Marcelo Costa:** É,  
**Off Digital:** que  
**Marcelo Costa:** eu também. aquele dinheirinho que entrou do certificou assim, não tinha  
**Off Digital:** não, mas mas relaxa,  
**Marcelo Costa:** nem  
**Off Digital:** não tô tão preocupado com isso não. É só para para ajudar esse mês mesmo e e vamos e vamos paraa frente.  
**Marcelo Costa:** Tá bom.  
**Off Digital:** Beleza, cara. Tô andando. Vou terminar essa aba de admissão aí.  
**Marcelo Costa:** É, e vamos botar e vamos ver que a gente fechar e botar nos cara lá pra gente até começar a faturar mesmo,  
**Off Digital:** Sim,  
**Marcelo Costa:** velho.  
**Off Digital:** eu vou excluir os candidatos agora e vou subir de novo que eu fiz vários ajustes no motor. Vou dar esse teste final no motor e aí eu acho que vel já preparar o demo pra gente apresentar pro  
**Marcelo Costa:** E a hora que você quiser me solta para eu testar.  
**Off Digital:** Marcelo, eu vou fazer uma versão com MOC e uma versão zerada, entendeu? Depois de testar o motor,  
**Marcelo Costa:** Tá.  
**Off Digital:** de subir mais candidato, mais matriz, tudo mais, aí eu vou remover tudo, vou deixar zerado e vou subir uma versão com MOC, com ele todo preenchido. Aí a gente mostra pro Marcelo ele preenchido para ele entender o sistema e depois a gente abre ele zerado e sobe do zero um candidato com ele ou sei lá, como você achar  
**Marcelo Costa:** Tá, mas veja, a hora que você falar que para testar,  
**Off Digital:** melhor.  
**Marcelo Costa:** se quiser me mandar para eu testar uns candidatos, aí eu vou testando o fluxo mesmo para ver onde que Bom,  
**Off Digital:** Não, vamos aí, priminho. Quinta-feira a gente se fala de novo. Pode ser?  
**Marcelo Costa:** fechado. Fechado.  
**Off Digital:** Beleza.  
**Marcelo Costa:** É, nós tamos junto.  
**Off Digital:** Falou para mim.  
**Marcelo Costa:** Valeu, primo.  
   
 

### A transcrição foi encerrada após 01:28:52

*Esta transcrição editável foi gerada por computador e pode conter erros. As pessoas também podem alterar o texto depois que ele for criado.*
