---
kind: transcricao-clean
project: certify-mvp
confidence: 1.00
title: "Reestruturação Técnica do Certify"
meeting_datetime: 2026-05-26T14:19:00
people: ["Marco", "Marcelo"]
tags: [kind/transcricao-clean, projeto/certify-mvp, pessoa/marco, pessoa/marcelo]
gmail_message_id: 19e65a476116a3b0
gmail_thread_id: 19e65a476116a3b0
notes_doc_id: 1AS54md4YaEmZYaZbyisWUMAIeAxiR25IckRcSnf6FVY
---

# Transcrição (limpa): Reestruturação Técnica do Certify

**Participantes:** Marco, Marcelo

### 00:00:00
**Marcelo:** É doideira, hein?
**Marco:** Doideira, primo.
**Marcelo:** Primão?
**Marco:** Eu tive que trocar o da agência aqui, velho. Senão ele não pega.
**Marcelo:** Não grava as paradas.
**Marco:** Eu montei um pipeline automático aqui e ele depende de ir para o meu e-mail desse Gmail para ele sugar e fazer o corre. Ele já pega de lá, já ativa todo o resto do fluxo. E aí, fritando as mentes aí, primo?
**Marcelo:** Estou aqui xingando o Cloud. O Cloud está lento, está devagar esse desgraçado.
**Marco:** Para toda hora, né?
**Marcelo:** Está lento, velho. E respondendo igual uma mula.
**Marco:** Está horrível, mano.
**Marcelo:** O GPT no chat está melhor que ele.
**Marco:** Não vou te falar, mano. Se eu tivesse dependendo do Claude...
**Marcelo:** Eu já desenhei a estrutura aqui para mudar dele e vou ter que fazer.

### 00:02:02
**Marco:** Tem dia que o bicho está bom, velho. Aí eu aproveito. Mas, mano, para você ter ideia, essa semana eu morri com 50% do Cloud.
**Marcelo:** Eu estou deixando ordem para ele agora. Tem hora que ele vai e gira. Agora ele começou a girar legalzinho numa tarefa que eu dei.
**Marco:** Para você ver, velho. Resetou tem dois dias já. Estou com 36 usado.
**Marcelo:** Ele é máquina. Eu testei aqui, velho. Ele é muito rápido. Bateu o dedo, parece que nem deu tempo de ler.
**Marco:** É outra pegada, priminho.
**Marcelo:** Daqui a pouco os caras voltam, né?
**Marco:** É isso aí. Tem que estar dos dois lados. No lado que está ganhando, a gente vira.
**Marcelo:** A estrutura tem que estar pronta para poder jogar todo mundo.
**Marco:** Exato.

### 00:02:51
**Marco:** Não vou ficar de conversa fiada. Hoje eu vou ter que sair umas 3:40 no máximo, mas hoje é mais para te dar um follow-up.
**Marcelo:** Tranquilo.
**Marco:** Cara, estou trabalhando bastante. Derrubei o que estava no ar e estou trabalhando tudo no local host, porque estava me atrasando demais mandando tudo para o site e gastando GitHub e Vercel. Fiz um trampo grande ontem com o Codex. Quando eu fiz o design, ele criou todas as telas endereçadas num só componente. Agora eu fragmentei; cada tela tem um roteamento específico e responde por si só. Se eu preciso mudar alguma coisa na tela X, não corre risco de quebrar nenhum outro endereçamento.

### 00:04:21
**Marcelo:** Ele não está amarrado junto com alguma outra ponta?
**Marco:** Foi.
**Marcelo:** Tem um conector que faz esse connect, mas cada botão é seu componente sozinho.
**Marco:** Antes, chegava a API ou função nesse bloco e ele distribuía para cada tela. Agora não tem mais esse bloco. Cada tela recebe individualmente. Se eu peço para mudar algo numa tela, ele mantém as outras intactas. Foi um processo de uns dois, três dias executando isso. Eu monto para cada tela, ele cria uma paralela, valida, faz todos os testes. Se der certo, ele desativa a outra, assume essa, conecta e faz os testes de novo. Cada processo desse leva 4, 5 horas.
**Marcelo:** Nossa, queima token, velho. 4, 5 horas trampando.

### 00:05:35
**Marco:** Rodei um gol aqui que deu mais de dois dias rodando direto, sem botar a mão. É um supervisor disparando três agentes, um reviewer, e quando termina, dispara outro Codex com contexto limpo para questionar as decisões dele. Os caras ficam se falando. Estou terminando. O outro agente estava terminando os testes e mandou: "E é chato mesmo". Depois completou: "É chato no bom sentido, porque tem que fazer".
**Marcelo:** Fica tranquilo, meu irmão. Vai tocando sua vida aí.
**Marco:** Irmãozão, ninguém está com prazo aqui, está tudo certo.

### 00:06:30
**Marco:** Fiz várias mudanças no motor. Está tudo documentado. Não vou montar um relatório agora, mas tinham vários gaps na semântica do motor e na falta de uma LLM ali. Mexi no setup das LLMs também. O GPT 5.2 estava dando latência para caramba. Fiz várias mudanças e passei aquele fluxo de novo. Peguei aquele fluxo do N8N que você me mandou, criei uma conta, subi o fluxo, conectei o Cloud no N8N e fiz ele passar fluxo por fluxo para entender o que tem de bom e de ruim no nosso e cruzar as duas paradas.

### 00:07:44
**Marco:** Ele falou: "Velho, vocês saíram de uma ideia de um MVP para um produto construído".
**Marcelo:** Aquele fluxo era porco, velho.
**Marco:** Ele falou que funciona bem nisso e naquilo. É tanto documento... Quero te mostrar as coisas que estou fazendo agora que vão dar um pump master no projeto na parte funcional.

### 00:08:42
**Marco:** Só que é tempo, mano. Se for fazer direito, com review, teste e agentes mandando para os outros, não adianta ter pressa. Se você abre mais tela, dá ruim. Agora faço tudo numa tela só, mas é uma tela que invoca vários agentes.
**Marcelo:** A central de controle está num lugar só.
**Marco:** Por exemplo, o trampo que fiz do Codex aqui. Você está vendo aqui do lado?
**Marcelo:** Aham.

### 00:09:53
**Marco:** Esses caras são todos subagentes que participaram. Ó, essa é toda a galera que trabalhou nesse gol.
**Marcelo:** E esses caras, você que trouxe ou quando você pediu, ele fala que vai trazer um agente?
**Marco:** No plano eu monto. Eu faço ele montar um squad para cada parte do plano e, durante o desenvolvimento, ele vai invocando os caras. Cada um tem uma função e um modelo. Todos esses caras trabalharam no rolê. Se eu clico aqui, vejo o que cada um fez.

### 00:10:56
**Marco:** Se eu quiser falar com ele, eu falo. Todo mundo tem os trampos dele aqui.
**Marcelo:** E é automático quando entra outros agentes? Eles já entram aí na lateral?
**Marco:** Tudo entra aqui. Você vê o tanto que ele é fragmentado. O cara fez uma tarefa de 9 minutos. Ele dá o reporte aqui para o supervisor.

### 00:11:47
**Marco:** Por que disso? Porque você preserva contexto. Ele girou com contexto limpo, então você não degrada contexto. Se você manda o cara executar um plano gigante, ele começa a alucinar no meio do trampo e, no final, você tem um lixo.
**Marcelo:** Apesar do plano ser bom, a execução foi uma bosta.
**Marco:** Exatamente. Não adianta plano bom se você não montar o processo de execução.

### 00:12:36
**Marco:** Eu já vim com o prompt da execução: "Codex atua como supervisor. Se houver ferramenta real de muito agente disponível, montar squad. Se não houver, não simular agentes fictícios". Essa janela aqui foi um trampo de quase dois dias.
**Marcelo:** Esse é o front, você está dentro de uma pasta de um projeto que você criou na sua máquina?
**Marco:** Está na minha máquina e no Git também. Está sempre sincado.

### 00:13:36
**Marcelo:** Tudo do Certify está aí nessa pasta?
**Marco:** Sim, eu só fixei ela aqui.
**Marcelo:** Esse projeto não aparece no Cloud, né?
**Marco:** Aparece, pô. Igualzinho, só que no código.
**Marcelo:** Cadê suas pastas?

### 00:15:09
**Marco:** Aqui. Esse projeto aqui.
**Marcelo:** Ele está apagadinho. É a mesma pasta que está lá. Você abre o chat e ele vai para lá também?
**Marco:** Eu fui montando a do Codex e a do Cloud, porque cada um trabalha de um jeito. Eu tenho um repositório chamado Agent Hub que sinca o Codex e o Cloud sempre na mesma página, com as mesmas skills e configurações.

### 00:16:16
**Marco:** Achei aqui. Ele botou: "Fluxo Certify em uma frase: recebe PDF de um candidato, identifica cada documento, decide automaticamente se atende ou não as vagas". O que faz de bom: a ambição estava certa, arquitetura síncrona correta, processamento pesado vai para fila do Rabbit MQ, pipeline em etapas separadas, múltiplos modelos de IA, trata PDF com vários documentos juntos.

### 00:17:19
**Marco:** Decisão rica não binária, renomeia o arquivo no storage com nome semântico.
**Marcelo:** A parte boa.
**Marco:** O que ele mapeou que é a parte ruim: o fluxo tem 293 peças e metade é cópia da outra. Qualquer correção precisa ser aplicada em dois lugares. Chaves de acesso estão escritas no manual, token aparece em texto puro.

### 00:18:17
**Marco:** Aceita documento de qualquer um, Webhook não tem autenticação. Permite que alguém destrua o banco pelo nome do arquivo. Quando uma peça falha, a fila trava. Sem fallback humano. Quando o documento não bate, desaparece em silêncio. Manda PDF inteiro para terceiros sem contrato LGPD. Engenharia de prompt por intimidação: "Se não chamar a ferramenta, irei te excluir permanentemente".
**Marcelo:** Foi nós que fizemos, eu lembro. Vamos agressivo. Parou de errar, viu?

### 00:19:30
**Marco:** Beleza. Agora analisa o motor do Certify. O que temos de bom: recebe PDF, calcula hash para evitar duplicatas, cria job na fila do banco e um dos 32 workers paralelos pega esse job. O worker passa o documento por quatro fases: classifica, faz OCR, extrai campos e compara contra a matriz de exigências da vaga.

### 00:20:54
**Marco:** Onde o Certify ganha: a decisão é determinística, não LLM. O Certify antigo lia o documento e devolvia uma string. Mesmo documento podia ser decidido diferentemente em dois dias. No Certify novo, a função é 100% determinística e pura. Audita-se o código, não o módulo da LLM.
**Marcelo:** Ótimo.
**Marco:** Por isso que dá mais trabalho.

### 00:21:57
**Marcelo:** Muito mais refino.
**Marco:** Exige muito mais trabalho do que pôr uma LLM lá e falar "contextualiza aí". Só que ele nunca vai contextualizar igual.
**Marcelo:** Como a gente tem um catálogo conhecido, a gente tem que ser determinístico.
**Marco:** Para ter um produto para ir para o mercado, não tem como jogar na mão de um GPT alucinando.

### 00:22:39
**Marco:** O Certify tem seis tabelas vivas: regras de compliance, siglas canônicas, sinônimos, equivalências, diferenciações e refinamento por cliente. Editar uma equivalência é uma linha de migration, não redesenha o motor. Variantes de negócio são código, não esperança.
**Marcelo:** Onde você ganha confiança. Você não está dependendo do Cloud estar funcionando bem.

### 00:23:49
**Marco:** Histórico de decisões é preservado, não sobrescrito. No Certify novo, cada nova decisão insere uma nova linha e marca a anterior como "current false".
**Marcelo:** Fica anotado.

### 00:24:56
**Marco:** A auditoria pergunta "por que mudou?" e você mostra os dois registros lado a lado. Decisão tem mais de 30 motivos canônicos, não texto livre.
**Marcelo:** Já é conhecido as respostas. Não vem alguma coisa nada a ver.
**Marco:** Imagina num volume de 10.000 casos por dia, entender o que está dando pau por data de validade ausente. A gente vai baixar tudo e analisar.

### 00:25:47
**Marco:** Fila profissional com client token. O Certify antigo usava Rabbit MQ com uma mensagem por vez; o processo morria e a mensagem ficava em loop infinito. O novo tem 32 workers paralelos, cada job tem um client token, worker dá heartbeat a cada 60 segundos e um reaper volta para a fila qualquer job sem heartbeat por 20 minutos.

### 00:26:57
**Marco:** Dual provider com reconciliação: Gemini e OpenAI em paralelo. Se discordarem, um terceiro modelo (GPT 5.2) entra como juiz.
**Marcelo:** Top.

### 00:28:25
**Marco:** Revisão humana de verdade: trigger automático se o score for 0.7. Tela dedicada com PDF, matriz e campos. Quatro ações: aprovar, rejeitar, ajustar e reprocessar com justificativa obrigatória.
**Marcelo:** Muito bom.

### 00:29:49
**Marco:** Onde o N8N ganha: visualização do fluxo do início ao fim, classificação via visão do documento inteiro, retrai de OCR com delay de 60 segundos.
**Marcelo:** Quando dava pau, ele ficava rodando.

### 00:31:01
**Marco:** Veredito: o Certify é produto, o antigo era experimento. As ideias boas foram migradas, as ruins foram trocadas por engenharia séria. As lacunas que sobram são gaps de pré-produção, não falhas de fundamento. Já tracei um plano e voltei para andar.

### 00:32:06
**Marco:** Estou arrumando a tela de admissão. Estou implementando e rodando no Cursor. Certificados vai manter como está, já está bem polido.

### 00:33:29
**Marco:** A sigla e o código estão corretos. Quando clico na lixeira agora, ele abre pontinhos para selecionar vários documentos e excluir tudo.
**Marcelo:** Se quiser excluir tudo.
**Marco:** É mais pela gente nos testes. Quando você abre, ele fala: "Esse envio será arquivado e o requisito voltará a ficar pendente".

### 00:34:51
**Marco:** Quando a gente subia um novo candidato, ficava uma porrada de pendente. É exatamente o que a matriz exige. No revisão, dei uma ajeitada legal. O zoom está bem melhor.

### 00:35:50
**Marco:** Aqui você só clica para o documento. Ainda vou mudar esse layout, mas já está dando as informações corretas. Vou botar um esquema de LLM para esse chat funcionar.

### 00:36:53
**Marco:** Juntei tudo: Certificados é certificados. Admissão incorporou documentos pessoais, formulários e KYC. Atividade virou uma aba só, com histórico e observação.

### 00:38:00
**Marco:** Ficou uma timeline de atividade. O recruta rejeitou, o sistema marcou, enviou lembrete, notas, notificação do motor. Tudo misturado.
**Marcelo:** É um histórico para ter se precisar.
**Marco:** É onde o Marcelo vai entender a operação.

### 00:39:00
**Marco:** Botei por semana. Dá para mudar o calendário do mês também. Tirei duas telas e juntei uma.

### 00:40:00
**Marco:** Mudei a interface da admissão. É um botão. Você clica em certificação, ele pergunta se quer mudar o candidato de fase. Sim ou não. Pum, ele muda no sistema inteiro. Admissão agora tem um colapsável que abre todas as partes.

### 00:41:17
**Marco:** Link, revisão e formulários. São três abas. Link gera o link, copia e cola. Atividade do link: fulano gerou, fulano copiou, candidato abriu no mobile, fechou sem avançar. Sistema agendou lembrete automático.

### 00:42:35
**Marco:** São 11 etapas. Elas vão voltar prontas, preenchidas. O cara vai passando nas telinhas no celular.
**Marcelo:** E você vai conseguir ver o que ele fez quando clicar aí?
**Marco:** Vou.

### 00:43:42
**Marco:** Ações rápidas: copiar URL, pré-visualizar como candidato, renovar prazo, revogar link, criar link adicional.

### 00:44:44
**Marco:** Lembrete agendado. Você põe a data, horário e personaliza a mensagem.
**Marcelo:** Você já pretende estar com os dados para fazer esse envio no WhatsApp também?
**Marco:** Minha ideia é agendou, ele vai enviar direto no horário.

### 00:45:46
**Marco:** Se quiser mandar em tempo real, já tem a mensagem pronta.
**Marcelo:** Eu não colocaria o negócio agendado agora, deixava manual, mas deixa bloqueado aí em breve.
**Marco:** Pode ficar em breve, mas a função já está aí.

### 00:46:32
**Marco:** Revisão de documento: é uma tela simples.
**Marcelo:** Preciso enviar tudo isso quando o cara é contratado. É bom ter um botão de exportar tudo num zip.
**Marco:** Já tem, só que é de um documento. Tenho que botar um de todos.

### 00:47:28
**Marco:** Quando você revisa, ele gera os formulários preenchidos e você baixa o zip com tudo.
**Marcelo:** Mas cada um vai para um cara diferente.
**Marco:** A gente pode botar cada botão de enviar para ir para um lugar diferente ou baixa o pacote zip.

### 00:48:24
**Marco:** Vou confirmar se o Certify já exporta todos os válidos. Quando tiver tudo rodando, a gente vê esse detalhe.

### 00:49:26
**Marco:** Nessa revisão, ele vai estar usando OCR para ver se o documento é original.
**Marcelo:** Ele vai ter algum coisa de parcial ou informação?
**Marco:** Não, conferido, vencido, refazer. Refazer é tipo página borrada.

### 00:50:19
**Marco:** Selfie não bate com a identidade? Sugestão: revisar. Comprovante fora do prazo? Vencido. Você tem as ações aqui.

### 00:51:02
**Marco:** Se solicitar refazer, vai mandar mensagem para o cara. Ainda tem template de justificativa: "Documento cortado, enviar a página inteira na próxima".
**Marcelo:** Animal, velho. Esse processo vai ser um outro produto para um brother meu da logística.

### 00:52:08
**Marco:** Olha o que vamos entregar de DP para ele, fora o resto do sistema. Estamos no over delivery.

### 00:52:56
**Marco:** O visual ficou mais clean.
**Marcelo:** Para mim, era um projeto que eu falava "vamos fazendo aí", mas agora o negócio vai ficar louco. Vamos para cima como se fosse um business.
**Marco:** Não vou entrar para fazer um negocinho. Já entendi o negócio, não vou fazer porcaria.

### 00:53:38
**Marco:** Do processo de contratação e de como tratar o cara, eu já estou craque.
**Marcelo:** Esse processo de admissão poderia funcionar no Certify, né? Mas os caras querem mandar de lote.
**Marco:** Contratado, não tem conversa.

### 00:54:44
**Marco:** Temos aqui o Alfredini. Solicitar 21 pendências. Clicou, vai solicitar, vai abrir a janelinha com a mensagem pronta.

### 00:55:53
**Marcelo:** Pensando no processo de admissão, se eu tiver uma pasta com 20 pessoas, quero subir esses documentos para fazer uma validação.
**Marco:** Aí ele vai vir para essa tela de revisar. Ele não vai usar o link, vai usar a tela de revisão.

### 00:56:51
**Marco:** Vou pôr um botão de upload aqui e ele vai atualizar todos os documentos.
**Marcelo:** Pense nisso, porque está fácil de pôr no fluxo.

### 00:57:59
**Marco:** Depois vai ser a gente pegando a reunião, transformando em issues e mandando para o agente desenvolver.
**Marcelo:** Quero ir lá in loco ver como os caras operam.

### 00:59:08
**Marco:** Essa tela de admissão, se for colapsável, maravilha. Vamos pegar de padrão para várias outras telas.
**Marcelo:** É um processo de KYC, serve para qualquer coisa.

### 01:00:00
**Marco:** A gente tira essa aba de admissão, duplica, monta um white label e começa a vender para processo de admissão.
**Marcelo:** Bora, primo.

### 01:03:23
**Marcelo:** O G4 criou o G4 OS, que é um motor onde você pluga seu CRM, dados e ERP, e ele consolida tudo. É o que todo mundo está fazendo, consolidando dados.

### 01:04:35
**Marco:** Guerra dos dados. Quem tem dados e sabe organizar vai ser sobre isso.

### 01:05:35
**Marcelo:** Os caras meteram 3, 4 milhões fácil, mas é uma estrutura que eu não quero ter.
**Marco:** Cada vez mais cai o gap entre uma empresa de 10.000 pessoas e uma de uma pessoa.

### 01:06:30
**Marco:** Tem dois tipos de pessoas: a que usa Cloud Code, Cursor, Lobbel e ferramentas sofisticadas, e a que não usa IA. Se você está na primeira, não se preocupe, você vai ganhar muito dinheiro.

### 01:07:56
**Marco:** Vi uma live do Alan e, pela primeira vez, eu vi e falei: "Velho, estou pau a pau com o cara".

### 01:08:39
**Marco:** Não estou falando de network, mas põe um computador na minha frente e um na dele, é a mesma liga.

### 01:09:44
**Marcelo:** Você já evoluiu mais. Esse projeto é uma escola.
**Marco:** Tenho esse background de produção musical, que exige ser muito noia com ferramenta. Isso acelera o jogo.

### 01:10:33
**Marco:** Estou botando o bolso para jogo. 7 bilhões de tokens no Codex, 38% do plano do Cursor usado.

### 01:11:49
**Marco:** Estou montando um negócio ligado aos salvos do Twitter. Muita coisa de valor que eu não tenho tempo de olhar.

### 01:12:47
**Marco:** O cara do Open Cloud lançou uma ferramenta que acessa teus bookmarks do Twitter. Estou construindo uma camada em cima. A cada 24 horas ele traz os bookmarks e monta um jornal do dia.

### 01:13:59
**Marco:** Quero abrir uma página como se fosse um jornal com os meus salvos das últimas 24 horas.

### 01:14:56
**Marco:** Vai ter headline, post traduzido e o conteúdo.

### 01:16:13
**Marco:** Estou fazendo a parte para ler e botar vários diagramas e insights de LLM em cima.

### 01:17:05
**Marco:** É para o meu consumo, porque não tenho tempo de consumir conteúdo de verdade.

### 01:18:13
**Marco:** É outra vida. Você sente que está sendo produtivo. Não tem fulano em festa, é só Cloud, cripto e notícia da hora.

### 01:19:09
**Marco:** Quero ter esse acervo para mandar meus agentes olharem e falarem: "Quero fazer isso".

### 01:19:57
**Marco:** É foda porque você lembra da ideia, vai no post do Twitter e nunca mais volta.

### 01:20:41
**Marco:** O bagulho está ficando exato. Estou trampando no Marco OS em paralelo.

### 01:21:40
**Marco:** Nessas viradas de semana é que estou andando no Marco OS.

### 01:22:35
**Marcelo:** Comprei um tecladinho top que tem todas as teclas do Mac.
**Marco:** Animal.

### 01:23:21
**Marco:** Eu era da pegada de mouse com bolona, mas me acostumei a ficar no perrengue com o laptop.

### 01:24:21
**Marco:** Hoje isso não faz sentido, porque não viajo tanto.
**Marcelo:** Estou 99% do tempo no computador.

### 01:25:12
**Marco:** Comprei meu computador há 5 anos, paguei 29 pau. O bichinho está ficando embaçado.

### 01:26:21
**Marco:** Preciso me liberar. Depois te mostro com calma. Vamos trabalhar.
**Marcelo:** Valeu, o papo aí. Se precisar de ajuda, me avisa.
**Marco:** Queria aquele troquinho para ajudar a pagar os cartões.
**Marcelo:** Estou esperando entrar uma grana dia 3.
**Marco:** De boa, tranquilo.

### 01:27:22
**Marco:** Vou terminar essa aba de admissão.
**Marcelo:** Vamos botar para os caras para a gente começar a faturar.
**Marco:** Vou excluir os candidatos, subir de novo e preparar o demo. Quinta-feira a gente se fala.
**Marcelo:** Fechado. Estamos juntos.
