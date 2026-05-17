---
kind: transcricao-clean
project: certify-mvp
confidence: 1.00
title: "Estruturação Técnica do Motor Certify"
meeting_datetime: 2026-04-27T14:43:00
people: ["Marco", "Marcelo"]
gmail_message_id: 19dd0a32fb659105
gmail_thread_id: 19dd0a32fb659105
notes_doc_id: 18LXdp-LgfwGcQdpvhADyueJ6D_1jUVOfkUcOK2t8Qq8
---

# Transcrição (limpa): Estruturação Técnica do Motor Certify

**Participantes:** Marco, Marcelo

### 14:43:00
**Marco:** Bora que bora. Deixa eu ver aqui o que o bicho já rodou. Importar, excluir, duplicar. Agora tá funcionando. Depois eu paro para fazer aqui. Primo, vamos voltar de volta aqui mesmo. Eu vou fazer depois uma versão do zero pra gente testar. Pode ser até mais tarde quando eu terminar a reunião com o brother, umas 8:30, ou amanhã cedo também, porque demora um tempo. Tá vendo que aqui tá V2? A URL tá v.cercerfy.cllaudia.com.br. O V1, aquele douradinho, tá com a URL salva ainda, normal, porque eu não apaguei. E aí eu vou criar um V3 para fazer esse teste sem nada na base.

**Marcelo:** Vai criar um Supabase novo também?

### 14:45:48
**Marco:** No V3 ele não precisa apontar nenhum dado de candidato, de matriz, de nada. Eu quero que ele mantenha a base lá.

**Marcelo:** Pra gente importar inserido do zero.

**Marco:** A base continua intacta, só que eu não quero que isso espelhe no produto. Aí tem que apontar domínio, tem que ir lá no Gold configurar no Vercel, são coisas que tem que fazer manual. Se não, fazia agora mesmo, mas demora uma horinha para fazer o rolê.

**Marcelo:** Tá bom. Vamos usar do jeito que tá aí no populado, que ainda é até melhor para nós.

**Marco:** Então, acho que aqui, primo, agora é mais coisa cosmética de produto mesmo. Por exemplo, essas coisas aqui de cobertura baixa, tem que decidir exatamente o que que vai definir aqui. Se a gente deixa a cobertura baixa...

**Marcelo:** Deu uma cortada aí, primo.

### 14:47:00
**Marco:** Internet tá... cara, a minha tá com sinal cheio aqui.

**Marcelo:** A minha também tá dando uma cortada até na câmera.

**Marco:** Se cortar de novo, você fala aí e a gente vê.

**Marcelo:** Voltou. Beleza, agora tá bom.

**Marco:** Então aqui, por exemplo, hoje a utilidade que eu arrumei para esses cards é esse lance da cobertura baixa, né? Mas isso aqui a gente pode mudar, pode ser alguma outra coisa. Mas é o que eu falei, eu acho que pro inicial já tá...

**Marcelo:** Eu acho que o importante é a gente estar com o coração funcionando, porque senão a gente deixa muita coisa e vai adicionando aos poucos.

**Marco:** Exato. Agora é muito cosmético. As vagas já estão aqui, ó.

### 14:48:02
**Marco:** Já atualizou as empresas. Só esse Marcelo aqui que foi aquela que a gente criou teste.

**Marcelo:** Acho que se bobear fui eu.

**Marco:** Deixa eu pedir para ele tirar a empresa Marcelo.

**Marcelo:** E aí você tá trazendo os dados de lá?

**Marco:** Agora eu já trouxe, as matrizes já estão aqui. Só não tem os documentos dos candidatos, porque a gente tá fazendo a limpeza para ele entrar no padrão que o sistema exige. Nós vamos validar no motor também.

**Marcelo:** Tá.

**Marco:** Eu tô com a aba aberta aqui. Depois eu vou ver certinho o que ele me dá e como a gente vai organizar isso. Ainda não tá definido. Ele deu ideias de como podemos fazer, mas tem que seguir aí coisa cosmética, tipo botar o loguinho da empresa.

### 14:49:35
**Marcelo:** E também não depende... é isso.

**Marco:** Tem vários candidatos que estão sem empresa. Tem que ver isso no sistema, quem que é esse candidato, por que ele tá sem empresa.

**Marcelo:** Parece que todos estão sem empresa ali.

**Marco:** Não, a maioria tem, mas tem vários que estão. Tem que ver de onde ele tá puxando esse dado.

**Marcelo:** Ele tá puxando do Supabase desde o início. Teve uma época que eu pedi para mudar, ter um campo só para empresa e nós mudamos porque estava dando erro. Pode ser nesse momento que não tinha ainda.

### 14:50:43
**Marco:** Sim. A gente tá meio que nessa parte agora, de ter um monte de dado, tá puxando tudo, tá mandando pro lugar certo, mas tem dado que não tá endereçado. Deixa eu pegar aqui, por exemplo, vou tirar um print. Na aba triagem temos vários dados que não estão interessados para nenhuma empresa e para nenhuma vaga. Quero que você faça um scan em todos os candidatos. São 52 candidatos ativos. Quero que você faça um scan nesses 52 e entenda porque eles não estão vinculados à vaga e à empresa.

### 14:52:44
**Marcelo:** Primo, um segundo que eu vou ver só uma parada aqui.

**Marco:** Tranquilo. Priminho, tem um negócio para melhorar sua visualização. Se você segurar o Command no Mac e jogar a barra de rolagem, ou colocar dois dedos no trackpad e arrastar para cima...

**Marcelo:** É na segunda tela não rola.

**Marco:** Rola também. Ó, tá vendo aí na minha tela o zoom que vai dando?

**Marcelo:** Ah, aqui eu tenho um maiszinho dentro do Zoom, velho. Consigo aproximar e ir mexendo.

**Marco:** Puta, irado. Ótimo. Mas faz isso para você aprender quando precisar dar zoom em qualquer coisa no Mac.

### 15:01:19
**Marco:** Tira do full screen. Não pode estar em full screen. Tem que estar tipo o meu, que tem várias telas.

**Marcelo:** Agora o meu funciona, mas não correndo os dedos assim. Ele funciona dando zoom mesmo de celular.

**Marco:** E ele abre?

**Marcelo:** Ele abre, nem preciso estar no Command.

**Marco:** O meu não vai.

**Marcelo:** Deve ser alguma configuração. Mas ficou bom, porque aí você não depende de pedir para o outro aumentar o negócio.

**Marco:** Isso aqui eu fiz uma lista de coisas que eu queria fazer ontem. Corrigir matriz, implementado e funcionando. Remover a empresa Marcelo.

### 15:03:18
**Marcelo:** Primo, você sabe uma parada que com certeza está previsto aí, mas eu lembrei: ele fazia toda a validação, beleza? Ele só não validava o nome do cara, porque eu crio o candidato, posso pôr seu nome inteiro ou pela metade, e depois o documento tem que ter esse cheque. Senão eu pego lá, tô criando Marcelo, mas subiu um documento do Marco e ele vai falar: "Ó, o documento tá OK". É um cheque simples, mas que eu tive que falar lá do outro lado.

**Marco:** Entendi.

**Marcelo:** Eu não sei se já está previsto, mas lembrei para ver se as...

**Marco:** É isso, a gente vai conseguir ver fácil no teste. Manda no WhatsApp isso que você me falou. Garante que o nome do candidato esteja atrelado com o documento na validação.

### 15:04:41
**Marcelo:** Já tá na minha listinha. Um outro ponto é modalidade. Eu vi que você tem uma nomenclatura modalidade. Ele entende modalidade, por exemplo, numa NR, como ele não separa em camadas?

**Marco:** Aqui, ó, tem aqui a classificação. Deixa eu compartilhar.

**Marcelo:** Modalidade é o curso ou exigência específica dentro da NR.

### 15:05:54
**Marco:** Aqui modalidade, por exemplo, dá o zoom aí. Você vê que ele tá aqui: documento 55 horas, CAP eventual, CAP inicial, EAD semipresencial, CIPA, 12 meses. Ele puxa a modalidade do próprio documento, conforme o documento explicita.

**Marcelo:** Certo. Aí quando eu vou colocar a matriz, você vai definir qual modalidade você quer, certo?

**Marco:** Não. Modalidade para você seria, por exemplo, NR3 e a modalidade seria 6 horas de salvamento. Aqui não é essa lógica. Ele tá lendo dentro do documento o que o documento mostra como modalidade. O que você vê hoje como modalidade no nosso sistema é só uma variação da NR.

### 15:07:25
**Marco:** Tanto é que tem documento aqui que é uma NR que a modalidade ficou "documento", porque não tem nada que explicita. E aqui é outra NR, mas já tem "hiperb", porque ela explicita.

**Marcelo:** E essa modalidade que você tá mostrando aí, ela não tem muito assim, não é um negócio de relevância que o cara bate o olho. A modalidade que eu tinha lá no Certify é outro.

**Marco:** Isso continua. Você tem EAD semipresencial, só que a própria NR já fala: NR01 é EAD semipresencial.

### 15:08:34
**Marcelo:** Então é porque essa regra já existe. O que pode ser EAD, o que não pode ser EAD.

**Marco:** Exatamente.

**Marcelo:** Então antes eu tinha isso separado, só que isso me travava. A empresa não quer saber, ela quer saber se o cara tem NR10, se foi presencial ou semipresencial.

**Marco:** O que mudou para a gente é que a modalidade passou a ser só uma informação e o que era modalidade para você virou variação. Variação de NR, variação de óbito, variação de SCW. Não é mais modalidade.

**Marcelo:** Podemos deixar completo, não muda nada. Ter ou não ter não muda.

### 15:09:29
**Marco:** E às vezes são informações pertinentes. Tipo, aqui tá dizendo que é 12 meses. É legal você bater o olho e saber.

**Marcelo:** 12 meses deve ser o quê? Será? Essa NR5 CIPA eu nunca vi.

**Marco:** De repente 12 meses é o tempo que demora para tirar ela.

**Marcelo:** Essas informações são trazidas de lá já?

**Marco:** Da nossa base. A nossa base tá trazendo da norma verídica.

**Marcelo:** Ah, p***, agora entendi, primo. Ele já tá trazendo o que a norma diz sobre isso aqui.

### 15:10:24
**Marco:** Isso aqui é indiscutível. Clica aí para você ver de onde eu tô consultando.

**Marcelo:** Vem no gov, que é onde é a base.

**Marco:** Link oficial aqui, ó. Fonte: gov.br/trabalho/conselhos.

**Marcelo:** Ótimo. Agora matou na fonte.

**Marco:** Depois da nossa última reunião que você falou da fonte, eu falei: "Cara, esse é o único jeito".

### 15:11:11
**Marcelo:** Vamos falar de um outro ponto: renomear os documentos. Você quer que eu te mando ou você já sabe?

**Marco:** O que é renomear os documentos mesmo?

**Marcelo:** É para ele pegar depois os documentos e renomear conforme ele lê.

**Marco:** Sim, criar nomenclatura padrão de renome de documentos. Matrizes, candidatos, tudo tem que estar no padrão.

### 15:12:12
**Marco:** Isso eu quis deixar por último, porque é legal ver o sistema inteiro para entender como a gente cria essa nomenclatura. Igual eu tô criando do brother aqui, o projeto que eu te falei que tá ficando irado. Redesenhei todas as telas, tá vendo as telas azulzinhas aí de novo?

**Marcelo:** Você fez no design, ele tá pica, né, velho?

**Marco:** Tá f***, mano.

**Marcelo:** Mas consome, né?

**Marco:** Não, consome para c*****. Isso eu já dei para ele tudo pronto, ele só melhorou as telas.

### 15:14:22
**Marco:** Subi server. Mudanças principais implementadas e funcionando. Mudei esses botões aqui, botei para ficar transparente.

**Marcelo:** Esse é o quê?

**Marco:** Esse é o do brother do estoque dos eventos que eu te falei. A gestão do estoque dele. Ele tem 600 e poucos itens. Já calcula qual que é o patrimônio com os eventos dele aqui. Aqui os RFIDs, que são as tagzinhas que ele vai ligar nos equipamentos. Quando ele tira do estoque, já dá baixa automática.

### 15:16:49
**Marco:** No catálogo dele, eu criei aqui os itens disponíveis, em campo, em manutenção, o que tá crítico, o que tá novo, o que tá regular. E aqui criou um código de nomenclaturas: MMDU 004. Quer dizer que é um equipamento de iluminação. Todos de iluminação ficam ILU.

**Marcelo:** Bate o olho já sabe o que é, né?

**Marco:** Aqui eu botei só iluminação. Aí fica MMDAUD 001, 002. Você tá criando um código de catálogo interno.

### 15:17:57
**Marcelo:** E depois que o cara for montar o pedido, ele vai ticando lá no site dele.

**Marco:** Exato. Pô, o que que tá na rua? Tá o AUD 004, 005, 007. Mandei para aquele evento. É o mesmo esquema que eu quero fazer de catálogo com a gente. NR001, tal, tal, tal. Tudo tem um catálogo.

**Marcelo:** É o que as empresas hoje, como a Maesco ou a Reli, fazem. Elas têm o código delas para cada um dos itens.

**Marco:** Exato. Código interno do nosso compliance.

### 15:18:50
**Marcelo:** Que ele tem um depara na real. O nosso 001 é o 203 dele.

**Marco:** Então não importa a organização do cara aqui para dentro de casa. O nosso 001 é isso, o 002 é isso. E a gente vai se referenciar em cima disso.

**Marcelo:** Vê que os padrões são próximos à forma de desenvolver.

**Marco:** Olha aí, você clica aqui, já aparece o QR Code para o cara. O bagulho tá ficando animal.

**Marcelo:** É da hora, né, velho?

**Marco:** Parece aquelas luzes de evento aqui, roxo, azul. Simplesinho, mas o bagulho filé.

### 15:19:37
**Marcelo:** Vai trazer uma inteligência para o cara do negócio dele.

**Marco:** Filé, simples, mas fácil de usar, fácil de mastigar.

**Marcelo:** O cara vai olhar e entender: "P***, velho, tô perdendo dinheiro porque tá ficando um negócio na rua".

**Marco:** O cara tem 1 milhão de itens. O cara faz uns eventos grandes, mano. Tava fazendo um negócio agora lá pro Shark Tank.

**Marcelo:** Depois você mostrar isso para ele, ele vai querer com certeza.

**Marco:** Eu faço bem feitinho porque tudo depois vira produto. Eu tenho um produto de controle de estoque.

### 15:20:32
**Marco:** Aí os caras só vão ter o login dele lá no produto e boa. Tem um que eles pagam que chama "Rang". É igual o Hackman.

**Marcelo:** O cara pega o Green e aí vai acabar.

**Marco:** Aí, priminho, ficou muito mais chique, sabia? Vou jogar de volta para o nosso.

**Marcelo:** Voltando aqui, tem uma parada que a gente precisa pensar, que hoje o outro trata meio grosseiramente: existem alguns treinamentos da Helix, por exemplo, que é um treinamento interno deles, e ela exige que a MDE controle esses treinamentos também. Só que isso é muito particular.

### 15:21:47
**Marco:** Tá.

**Marcelo:** Porque não tem uma regra. Cada cliente tem os treinamentos internos. O que eu construí é o seguinte: eu botava lá como "outros" ou "cliente" quando eu cadastrava um negócio. Vou abrir um para você ver.

**Marco:** Abre aí.

**Marcelo:** Tá vendo aí? Tenho aqui: "Cliente - treinamento de linha de fogo". É da Helix. Ela mesma treina o cara internamente. E às vezes, antes do cara entrar, ele tem que passar por esses.

### 15:23:06
**Marcelo:** Só que isso aqui é um pouco solto. Eles até fizeram EAD através de um EAD do Drake. Nem sabia que o Drake tinha um EAD. O que acontece? Isso aqui não é um padrão. A Helix tem um, a Petrobras tem outro, a nomenclatura é diferente. Não é norma, mas é interno do cliente. Aqui, como eu botei em "outros", às vezes dá pau porque o cliente tem um interno, mas o Opito também tem um treinamento de gás. E ele pegou um Opito e jogou lá, que tá errado.

**Marco:** E linkou com isso que você criou?

**Marcelo:** Porque esse é interno do cliente, não deveria ser o Opito.

### 15:24:16
**Marco:** Como é que chega para você? Quem que tá fazendo? É o Marcelo?

**Marcelo:** A matriz já vem exigindo para ele e o candidato vai fazendo. Antes de ser contratado, a Helix falou: "Vou contratar o Marco". Agora o Marco precisa fazer esses treinamentos internos. Ele vai lá no Drake, faz, manda para ele, ele valida e manda para o cliente: "Terminou, tá OK com os treinamentos, inclusive os seus".

**Marco:** Isso então é depois de certificados, antes de documento pessoal?

**Marcelo:** É, tá dentro dos certificados. É mais uma leva, só que é exigência do cliente.

### 15:25:21
**Marco:** Qual seria a forma disso ficar amarrado legal? A gente vai ter que criar de cliente para cliente uma aba de exigências do cliente. Ele tem que mandar pra gente a base. Toda vez que tiver um cliente novo, ele vai ter que solicitar essa parte.

**Marcelo:** É isso aí. O cliente manda pra gente um esboço. Me manda quatro aí. Eu vou ver aqui, vou botar internamente, falar para a Helix. Ela tem esses treinamentos? Me manda toda a informação pra gente imputar aqui.

**Marco:** Deixa eu ver aqui no Codex. Helix Energy Solutions.

### 15:26:30
**Marcelo:** É esse o primeiro cara que nós vamos vender a solução. Eles têm 3.000 funcionários no mundo. Brasil é uma ponta, mas os caras estão em Houston, Louisiana, Barém... só nos picos de óleo e gás. É dinheiro com força.

**Marco:** É mineração de dinheiro.

**Marcelo:** Singapura... os caras estão em todo lugar.

**Marco:** Nós temos que ser competitivos globalmente.

**Marcelo:** Essa solução aqui é embaçada. Eu acho que você não vai ter esses treinamentos.

### 15:28:19
**Marco:** Que que tem aqui?

**Marcelo:** Te mandei no chat aí, depois você dá uma olhada.

**Marco:** Vê se alguém bate aí com os que você já deu entrada.

**Marcelo:** Deixa eu abrir aqui. Orientação, familiarização de embarcação, segurança operacional, não corrupção... não tem esses que eu te falei. Esses aqui estão mais offshore.

**Marco:** Fala exemplos de alguns aí.

**Marcelo:** Treinamento de linha de fogo, pense na segurança do processo, teste de gás autorizado.

### 15:31:18
**Marcelo:** Aqui deve ter um negócio de treinamento também, mas tá longe dessa...

**Marco:** Cara, isso aí é fácil. A gente recebe o modelo e a gente entende.

**Marcelo:** O cliente manda. Se eu preciso que ele faça, me fala qual é. O cliente tem isso. Acabou. É só a gente pensar como a gente sobe isso, deixar um espaço pra gente subir o do cliente.

**Marco:** A gente deixa a estrutura pronta nas matrizes de subir treinamento específico do cliente e quando ele subir, já endereça o cliente certo e já abre ali dentro na aba de certificados.

### 15:32:39
**Marco:** Beleza? Então, o que eu tô fazendo aqui é endereçando aqueles candidatos que estão sem empresas e sem vagas direcionadas.

**Marcelo:** Tô procurando uma outra parada. Agora tem uns documentos novos.

**Marco:** Aí, priminha, aqui no detalhe do candidato, você não tinha pegado um exemplo ainda que tem "confere", tá vendo? Fica um bloco com vários. Tudo clicável.

**Marcelo:** Top.

**Marco:** Só não tá aparecendo os pendentes, tem que aparecer.

### 15:38:40
**Marcelo:** E aí a aba revisão, você vai lá ver ele, ele traz o detalhe do que...

**Marco:** Você clica em revisão, aí ele vai mandar ele para a fila de revisão.

**Marcelo:** Ele não fala por que tá em revisão?

**Marco:** É para enviar ele para a revisão. Por que que ele vai para a revisão? Porque ele tá parcial.

**Marcelo:** Certo. Mas por que ele tá parcial?

**Marco:** Aí lá na aba de revisão vai aparecer.

### 15:40:54
**Marcelo:** Seria bom ele aparecer aí, porque o cara fica a maioria do tempo trabalhando no próprio candidato. Tô subindo os documentos dele, quero entender esse cara. Seria bom ter esse campo aí para você bater o olho.

**Marco:** É, tem que ser aqui do lado. Quando eu clico aqui, muda aqui do lado. Tem que ter o porquê.

**Marcelo:** Pode.

**Marco:** Beleza. Aí você tem isso aqui também, quanto por cento o cara tá de aderência com a matriz.

### 15:41:48
**Marco:** Nesse caso, ele tá com 38%, porque ele tem quatro parcial e seis pendente.

**Marcelo:** Uhum.

**Marco:** Saúde tá 100%, operacional tá 100%. Provavelmente isso aqui não tá correto, não tá informando. Mas você vai ter aqui, pô, o cara tá ruim no marítimo aqui. Beleza. Aprovar para DP, isso aqui também, solicitar revisão de NR, rejeitar candidato. Tudo tem que ligar esses botões. Aprovar para DP é o final de tudo.

**Marcelo:** Ele pode ter uma trava. Só aprova se tiver OK.

### 15:42:56
**Marco:** Essa aprovação é quando você tem parcial revisão humana. Vamos dizer que o cara tivesse tudo batendo, ele já ia estar em DP. Agora, o cara tem 15 confere e um parcial, vai ter que vir alguém aqui e ver e falar: "Não, beleza, pode aprovar".

**Marcelo:** O que acontece normalmente é que eles vão lá e mandam o cara fazer. Então, não é agora, mas num próximo momento a gente vai poder até plugar quem faz e quem não faz. Ô primo, declaração você tem, você botou aquele, ele já sai falando que é uma declaração, né?

### 15:44:20
**Marco:** Declaração já.

**Marcelo:** O que poderia aumentar aí é declaração e lista de presença. Às vezes vem um negócio que é uma declaração, o cara fez, mas ainda não recebeu o certificado. Essa declaração vale por 30 dias. Já a lista de presença, às vezes você tem um curso, fez 10 funcionários, aí o cara assina a lista. E os documentos que vêm junto, minha lista de presença que eu tava no curso mais o certificado. Isso às vezes vem, que era um que você tá abrindo ali.

### 15:45:31
**Marco:** Você tem que me mandar alguns arquivos de lista de presença. Aí eu jogo para ele mastigar, entender e criar um parâmetro de triagem.

**Marcelo:** Tô anotando aqui. Daqui a pouco vou te mandando tudo no Zap.

**Marco:** Beleza, eu já tô resolvendo o link aqui dos candidatos com as empresas. Agora tem que ver direitinho, botar o nome do produto, ver o domínio, botar uma logo.

**Marcelo:** Não, eu acho que não tem que pôr, não. É a solução.

### 15:47:08
**Marco:** A gente põe a logo dele aqui, ó, no nome de cada recruta, põe MDE. Em vez de pôr a foto do recruta, põe a logo do MDE. Vai ficar vários MDE aparecendo no sistema inteiro.

**Marcelo:** Boa. Eu tenho logo aqui já.

**Marco:** Você vai ver vários MDE operando dentro do sistema. O que que a gente tem mais? Tem um documento específico de rádio operador que eu não sei se...

### 15:48:55
**Marcelo:** LPNL, em algum momento você cruzou com ele?

**Marco:** Ô primo, você tem um login do Drake?

**Marcelo:** Tenho.

**Marco:** Em algum momento você já puxou essa regra aí?

**Marcelo:** Um dos documentos desses caras aqui vem com QR Code. Então vem o documento, mas você precisa ler o QR Code para mostrar a validade. É um documento exclusivo, mas em algum momento a gente vai passar por ele.

**Marco:** O fato de ler QR Code é muito tranquilo, é só a gente plugar mais. Vai adicionando regra, priminho.

### 15:52:01
**Marcelo:** Nessa relação de conferência, um ponto que a própria Helix pediu para eles olharem é que os documentos vêm assinados, tem assinatura do órgão lá e tal. E às vezes tem um outro documento que vem sem assinatura, sem carimbo. Era bom a gente pensar nisso também para ele fazer essa checagem na leitura do OCR.

**Marco:** Anota para mim, anota tudo.

**Marcelo:** Técnico segurança do trabalho e engenheiro segurança do trabalho.

**Marco:** Aí, priminho, já tá pegando tudo aqui, ó, no Kanban. Pegando as empresas, os documentos aqui.

### 15:56:47
**Marco:** Vamos ver se eu tô com eles abertos.

**Marcelo:** Vamos pegar uns casos aí.

**Marco:** Só que aqui no teu eu não consigo ver o número de documentos.

**Marcelo:** Qualquer um, ou o olhinho ou o outro, tá na mesma.

**Marco:** Documentos cinco, confere três, parcial um, pendente. Aqui ele tem nove documentos. Aqui só tem sete.

**Marcelo:** Deixa eu dar uma analisada nele.

### 15:59:56
**Marco:** Não, aqui tem nove. Sete confere, dois parcial.

**Marcelo:** Só que ele tem muito mais documento que ele não tá somando tudo que tem do cara aí, que é os documentos que não exigível, que estão lá embaixo.

**Marco:** Sim, tá botando só os da matriz. Agora pendente, ele tem um STCW pendente.

**Marcelo:** Vamos dizer aqui. Ele não leu nenhum daqueles que bateu aí, então ele nem conferiu nada.

**Marco:** Eu tô querendo entender o pendente, para onde o que ele não tinha subido, como que ele classificou.

### 16:01:48
**Marco:** Curso de embarcação rápida de resgate.

**Marcelo:** Pendente é que ele nem subiu, não existe, não veio o documento ainda.

**Marco:** Então é os que... esse aqui e esse aqui.

**Marcelo:** Os dois parcial ele bateu.

**Marco:** Ele deu esses dois aqui pendente, ele bateu parcial. Quer dizer, esse e esse ele bateu parcial.

**Marcelo:** E mas e no seu?

**Marco:** Só que esse parcial ele deu confere.

### 16:03:26
**Marcelo:** Aonde você tá dizendo?

**Marco:** Tô dizendo no novo.

**Marcelo:** O seu conferiu.

**Marco:** Conferiu.

**Marcelo:** Deixa eu abrir também esse cara aqui, só para eu conseguir ver melhor como que chama esse cara aí.

**Marco:** É o Laudci.

**Marcelo:** Laudestir tem um parcial que é o CAC EAEC, né?

**Marco:** Uhum.

**Marcelo:** Ele tá dando parcial. Carga horária não informada no documento ou não atende.

### 16:05:26
**Marco:** Aqui ele deu confere.

**Marcelo:** Então vamos ver o que acontece aqui se ele tem a carga horária aqui, porque no meu ele não validou porque disse que não tinha 40 horas.

**Marco:** Não é por causa do vencimento que ele não tem a data de vencimento?

**Marcelo:** Veja que ele tá falando aí no canto: "Carga horária não informada no documento", ou seja, não encontrou 40 horas. E ele pede 40 horas na matriz.

**Marco:** Não atende a exigência.

**Marcelo:** Ele falou: "Você falou 40 horas, eu não encontrei". Só que esse documento não existe, um CAC 20 horas. A norma é o CAC, pode ser que demore, tenha os 40 horas para fazer, mas eu acho que isso tá na norma.

### 16:07:30
**Marco:** O que eu quero entender é que tem um pendente que é o CRR, curso de embarcação rápida e resgate.

**Marcelo:** Então esse documento ele ainda não mandou.

**Marco:** E sim, mas aqui ele tá dando como confere.

**Marcelo:** Ah, ele tá dando um confere aí, então.

**Marco:** Eu vou abrir o PDF aqui. CRC, habilitação profissional para gerenciamento dos recursos de praça de máquinas. Onde que aparece a sigla dele aqui?

**Marcelo:** Na maioria das vezes não vem.

### 16:09:48
**Marco:** Então, abre aí no teu e vê aí o que que é exatamente.

**Marcelo:** Não, tá certo. Esse é quase certeza que esse é o documento. Deixa eu ver o código dele aqui. Ele tá dando regras não especificadas anteriormente. Esse é um SER mesmo, eu acredito.

**Marco:** Aonde priminho?

**Marcelo:** Vai lá no mesmo, na aba. Pode descendo.

**Marco:** Esse é um...

**Marcelo:** Isso. Eu achei que pode ser esse que ele deu um confere.

### 16:11:26
**Marco:** Esse é um aquaviário.

**Marcelo:** Não, não. Pode ser esse, ó. Não é nenhum desses aí.

**Marco:** Quer que eu pergunte na IA aqui?

**Marcelo:** É, o meu aqui tá com vários erros, velho. Tá dando uns confere, tá subindo o mesmo documento.

**Marco:** Você quer que eu confirmo aqui se isso é um SER aí?

**Marcelo:** Confirma, mas com certeza é. Agora você vê o meu, o nosso aqui, o Certify tá dando maior vacilo em tudo aqui, velho. Tá lendo uns bagulhos nada a ver.

**Marco:** É, é um STCW CR.

### 16:13:29
**Marcelo:** Eu achei ele aqui. Esse documento que você tá falando aí, aqui ele bateu com EGPM. Deixa eu ver se é isso. Ele bateu com habilitação profissional para gerenciamento de recurso. Beleza, achei esse documento aqui, só que ele bateu aqui como um gerenciamento dos recursos para máquina, um STCW que não tem código.

**Marco:** Tá.

**Marcelo:** Agora eu tô na dúvida, porque tem um documento aqui que é muito parecido, um STCW que não tem código.

**Marco:** Eu joguei na IA. Vamos ver.

**Marcelo:** Ele já bateu com outros aqui.

### 16:16:49
**Marco:** Eu tô falando aqui que pelo certificado ele diz que é habilitação profissional para gerenciamento dos recursos de praça de máquinas.

**Marcelo:** Então, tem um documento que é conhecido como EGPM. Eu acho que é esse. Certificado emitido... padrões internacionais. É, eu acho que esse não é o CES.

**Marco:** Eu tô achando que ele não é também. Eu vou pedir para ele analisar o candidato como um todo.

**Marcelo:** Ele não é o CES, tá? Porque o CES é curso especial de embarcação e sobrevivência e salvamento.

### 16:18:27
**Marco:** Mas é o CRR, né? O documento que tava faltando pendente é o CRR, o CES tá confere.

**Marcelo:** Curso especial de embarcação e resgate rápido. É esse que você tá falando.

**Marco:** Isso, isso.

**Marcelo:** Ele tem uma tabela específica no STCW, só que nessa certificadora aí não está aparecendo a tabela. Esse documento em específico não tem tabela.

**Marco:** Ó o que que ele deu aqui para mim: confirmado que esse candidato existe, tem o PDF PGM Engine Room Resource Manager. Agora vou olhar a comparação que colocou isso como CER, porque isso é falso positivo. No banco a comparação desse candidato não tem nenhum confere para o item CER. O HPGM aparece como declaração ou não exigindo, não como aprovado. O erro provavelmente está na camada de exibição do detalhe do candidato.

### 16:20:25
**Marco:** O banco gravou declaração, mas a UI tá colocando declaração dentro de confere. Isso tá errado para uso real. Vou ajustar.

**Marcelo:** É, mas não tem nada a ver com declaração.

**Marco:** Vamos ver isso aqui.

**Marcelo:** Fala, não tem nada a ver com declaração.

**Marco:** Declaração vai para revisão parcial, porque na verdade esse documento é porque não tinha o documento, não é isso?

**Marcelo:** Aqui para mim ele tá pendente porque o cara não tinha mandado.

### 16:22:13
**Marco:** Exato.

**Marcelo:** Não existe esse documento na base. Ele aí do seu lado, ele pegou um documento e validou um documento que não...

**Marco:** Na verdade, ele não validou. Ele não tem confere para o item CER.

**Marcelo:** Mas o front que tá mostrando é isso?

**Marco:** O front tá mostrando como declaração, só que também não é declaração. Então vamos entender o que que...

**Marcelo:** Esse HPGM, na verdade, para mim é EGPM. Esse documento que você lê aí na minha matriz aqui do Certify, ele tá dizendo que é EGPM.

### 16:24:13
**Marco:** Então foi que o cara subiu esse documento no lugar de SER.

**Marcelo:** Não, não. Aqui, na verdade, esse documento, o seu aí pegou e jogou no lugar do CES. Aqui ele leu certo no lugar que é o documento certo mesmo, que é esse EGPM. Eu acho, primo, que o caminho pra gente testar o motor era a forma que eu mais testava aqui: pega um candidato, sobe um a um e vê o que ele lê. Aí a gente vai: "P***, beleza, validou". Porque quando você pega um bloco muito grande, a gente fica perdido no que tem que arrumar.

**Marco:** Sim, isso aí a gente tem que fazer, vai ser a validação final. Mas cara, já foi um positivo muito bom, porque de todos os documentos ele errou um basicamente.

### 16:25:27
**Marcelo:** É.

**Marco:** No automático, sem upload, porque o motor foi feito enrijecido na matriz. Esses documentos a gente importou sem passar pela matriz.

**Marcelo:** Então, mas ele tá batendo contra...

**Marco:** Tá batendo direto nas bases de norma.

**Marcelo:** Mas aí como é que ele tá dando? Porque vamos pensar, ele tá subindo numa vaga. A vaga tá pedindo o EGPM, beleza? Ele tá pedindo também o SER, ele pegou o documento e botou esse como SER.

**Marco:** Sim, mas é que eu acho que tá acontecendo, como a matriz não foi criada dentro das regras...

### 16:26:53
**Marcelo:** É, mas então se não tem matriz no...

**Marco:** Não tem a matriz, mas é uma matriz importada, não é uma matriz criada.

**Marcelo:** Então aí você não tá pegando na raiz, né? Para você montar a matriz aí dentro, você vai pegar a matriz só dos documentos validados, velho. Se não é um documento validado, eu tenho que entender o que que esse é.

**Marco:** Exatamente. Que o problema tá na hora de criar a matriz.

**Marcelo:** É, mas esse erro dele aí, ele validou um documento errado. Não tá batendo com a matriz, não tem nada a ver de amarra com a matriz.

### 16:27:57
**Marco:** Acho.

**Marcelo:** Ele pegou um documento e falou: "Ó, isso aqui confere no CES". Não, não pode conferir isso no CES.

**Marco:** Pois é. Vamos ver isso aqui.

**Marcelo:** Você pediu... ele tá rodando.

**Marco:** Tá rodando, tá rodando. Aí por isso que eu não mandei nada, porque tem que esperar ele parar para que ele não leia. Se eu mandar agora no meio, ele não vai ler.

**Marcelo:** Não, deixa ele olhar aí.

**Marco:** Então, mas é isso, primo. A gente só vai conseguir ver mesmo fazendo o teste real.

### 16:29:02
**Marcelo:** É, cara, o teste real e não com 1000 documentos, tá ligado? Porque 1000, velho, a chance dele errar... ele tem que ir no caminho: sobe 10 documentos, vai ver como ele se porta. Aqui ele se porta totalmente diferente quando eu subo 10 documentos, quando eu subo 50.

**Marco:** Sim.

**Marcelo:** Ele pegou aí de porrada, né?

**Marco:** Teoricamente não era para dar bug porque ele tem muitos workers funcionando e o trabalho já é dividido.

**Marcelo:** E cara, é os guardrails que o cara tem que ir colocando, entendeu?

### 16:30:19
**Marco:** Exatamente. Você só vai ver na prática. Agora o bom é que quando deu pau, nós vamos abrir um terminal e vamos resolver. Nós não vamos ter que abrir lá o emaranhado, né, velho?

**Marcelo:** Pelo amor de Deus.

**Marco:** Plugga o negócio e fala: "Ó, velho, deu pau aqui, o que que é?".

**Marcelo:** E outra, só nesse cara aí tem erro para c***** de outras coisas aqui que ele leu errado.

**Marco:** O cara já abriu uma aba aqui para mim do nada. O banco gravou declaração, mas a UI tá colocando declaração dentro de confere. Isso tá errado para uso real. Vou ajustar.

### 16:31:55
**Marco:** Deixa eu dar um refresh aqui para ver como é que ele vai ficar agora. Agora ele tá dando um confere e oito parciais. Eu vou tirar um print da tela e mandar para ele. Olha só, nesse print que eu te enviei, a validação do motor do Certify MVP, que é a versão antiga, classificou os documentos dessa forma. Você tem aí no status o que confere, o que tá parcial e pendente. Então, teoricamente a gente não teria esse documento na base e ele tá entrando como parcial agora e entrou como confere na última. Então eu preciso que você faça aí uma auditoria e um cruzamento minucioso entre esse resultado e o que a gente tem na base de fato.

### 16:33:54
**Marco:** Ele falou aqui para mim: "Existe link público para alguns conteúdos, mas o catálogo Helix My Drake é fechado pro login. Não encontrei uma página pública". Então já dá para entender que, cara...

**Marcelo:** É, mas não é um padrão. Cada um cria e bota lá. A gente vai ter que construir um a um aí nesse caso, né?

**Marco:** É, velho, pedir para o cliente o documento, a gente imputar um por um, fazer uma análise e imputar no sistema. Beleza? Vamos ver aqui então. Motor 2.0. Bom, é isso aí, priminho. Você já viu aí onde a gente tá, agora é realmente a gente fazer na prática, entender os probleminhas e ajustando. Aí eu não sei se você quer manter com o Marcelo ou se você quer jogar um dia para frente.

### 16:35:47
**Marcelo:** Eu prefiro que a gente mate do que mostrar e depois isso aqui vai ficar... segura aí, já tá rodando com outro até agora. Porque senão eu fazer duas reuniões para fazer uma.

**Marco:** Exato. E tipo assim, não tem porquê. O negócio já tá filé. Agora é mais essas afinadas aí de motor mesmo.

**Marcelo:** Não tô com pressa disso.

**Marco:** Beleza. Amanhã a gente segue aí.

### 16:37:02
**Marcelo:** Cortou aqui, primo.

**Marco:** Eu acho que agora a gente tem que ter um encontro todo dia para a gente dar um gás aí nessa reta final. Então amanhã a gente já deixa um horário aí, esse mesmo horário do meio-dia eu acho que é bom.

**Marcelo:** Tá, eu tenho só essa questão, né? 1:30 eu levo o bebê.

**Marco:** Não, não tem problema. A gente para até a hora de... eu paro para almoço também. Então vamos deixar esse horário e vamos aí todo dia. Se amanhã já não tiver, eu acho que amanhã já tá pronto para o teste, velho.

### 16:38:30
**Marco:** Eu já vou fazer isso aqui, já vou delegar para ele fazer um V3 sem dado nenhum para a gente abrir o negócio clean.

**Marcelo:** Mete um V3 sem dado nenhum para a gente já falar: "Ó, vincula esses documentos da matriz e vamos fazer um passo real mesmo".

**Marco:** Exatamente. E aí a gente já fica aqui na call mesmo resolvendo.

**Marcelo:** Tá bom, fechado.

**Marco:** Mas falta pouco, prima. P***, eu tô louco para botar isso para os caras funcionar também, velho.

**Marcelo:** Eu nem tô ansioso, tá ligado? O cara vai olhar e outra, o Marcelão é o cara tem cabeça de negócio, né, velho?

### 16:39:23
**Marcelo:** Nós vamos mostrar para o Marcelo e não falamos com o Dávio, né? Porque eu não vejo ainda assim... o Dávio conhece de Supabase e o c*****. Acho que eu não sei em que momento a gente bota ele nessa parada, né?

**Marco:** Cara, eu acho que validou com o Marcelo, decidiu que vai botar para rolar, aí pode fazer uma reunião com ele. Fala: "Ó, velho, a gente pegou o aval do Marcelo porque não adianta ficar passando item a item com você". Chegar lá, o Marcelo não aprova, a gente tem que mexer de novo. Então, aprovamos com o Marcelo e agora estamos sentando para te passar o produto. Os caras já vão entrar em uso e como é que a gente pode contar com você no dia a dia para manutenção?

### 16:40:31
**Marco:** Tudo, velho. Tudo ele que vai ficar com a bola. É o único sentido que faz daqui para frente.

**Marcelo:** Eu acho que só pensar no tipo... ele não tem ideia que nós estamos fazendo tudo isso, né? Porque inicialmente eu falei para o cara: "Ó, passei para um brother aqui que trampa com processo e tá mexendo aqui, criando umas estruturas legais". Aí fala: "Não, montamos um". Então, às vezes o cara não tá esperando que fizeram um produto novo, não falaram nada. Agora chega aqui, quanto eu quero só para fazer a manutenção?

### 16:41:45
**Marcelo:** Então assim, a minha conversa com ele sempre foi: "Você é meu sócio aqui nessa parada". Então eu tô, talvez a gente faça uma... vamos dizer assim, consultivo: "Vem aí, ó, o que nós fizemos, velho". Nós mexemos nisso aqui, estruturamos assim, mapeamos linha a linha do processo. Isso ele não fez e era o que eu espero. Tipo, você manja daí, você vai atrás da regra. Isso que você fez para mim é onde tá o maior valor do negócio que ele não parou para fazer.

**Marco:** Não. E...

### 16:42:45
**Marcelo:** Eu tenho certeza.

**Marco:** E o ponto principal que começou a conversa não é nem o front e não é nem o peso do trabalho completo de entrar no negócio, é tirar vocês do N8N. O cara já tinha que ter tido a proatividade assim, pelo amor de Deus, mano. Não tô querendo botar um dedo no cara que eu nem conheço, muito pelo contrário, porque eu já entendi que ele é ponta firme. E primo, nesse negócio aqui, eu nem quero dar muito pitaco no sentido de como é que vai ser o modelo de negócio, porque é um negócio que você criou. Eu tô entrando somando, eu tô investindo meu tempo e minhas habilidades no negócio que eu sei que eu confio para onde você pode levar a gente. E quem vai ditar nesse negócio até então, como é que funciona, é você.

### 16:44:10
**Marco:** E eu confio exatamente em como você vai direcionar, seja de composição, seja de crescimento do negócio, eu confio 100%. Então eu não quero ficar impondo nem dando opinião com peso em nada. Mas assim, a minha forma de pensar é: p***, nós já estamos há um ano aonde você consegue fazer as paradas com cloud muito bem feito e tal.

### 16:45:10
**Marco:** E seria legal ter tido uma preocupação do lado dele de falar: "P***, vamos fazer um sprint aqui para tirar a gente desse motor barulhento de p*** de fiarada para lá". E aí eu entendo o cara ser pai de família e estar correndo atrás das contas e estar atolado lá no trampo dele e saber que dá um trampo, é uma pica. Não é um negócio assim que você faz também, tipo, ah, sento ali e estalo os dedos.

**Marcelo:** É, mas o seguinte, primo, além disso, onde que é o onde eu acho que eu assim, tô trilhando aqui, abrindo com você, como é o caminho que eu tô pensando com o cara para também deixar o cara confortável e ele reconhecer que: "P***, velho, virei 10% do negócio". Eu quero que ele tenha essa percepção, mas não eu falando: "Ó, você tem 10 porque o cara fez isso". Eu quero mostrar para ele, porque eu sei que ele não tem a capacidade de organização e de chegar no detalhe do detalhe, porque ele é um cara de N8N, velho.

### 16:46:19
**Marco:** Tem o saudosismo ali, né?

**Marcelo:** Então você falar: "Saímos do N8N", para ele, ele vai falar: "P***, velho, saiu do que eu domino a minha vida inteira".

**Marco:** Entendi.

**Marcelo:** Então, eu prefiro ir pro lado e falar assim pro cara: "Velho, olha aqui as normas, sabe onde tava dando pau? Porque a gente não categorizou". Quando você mostrar isso, o cara vai falar: "Cara, ele não tinha nem a capacidade de se falar: tira 100% do seu tempo e vai olhar ele". Não, eu acho que ele não faria isso porque entra muito em modelo de negócio. Então, a gente mostrando isso para ele, eu vou conseguir deixar explícito que ele virou 10% do negócio.

### 16:47:15
**Marco:** Total. E essa é uma reunião que eu acho que você tem que fazer com ele. Você vai ter o acesso de supervisor, você dá um acesso para ele e você troca essa ideia com ele, apresenta o produto, troca a ideia com o cara aberto, chega numa conclusão com ele e aí depois dessa conclusão você faz uma reunião para apresentar a gente.

**Marcelo:** É lógico.

**Marco:** Com a data.

**Marcelo:** No último ponto, primo, assim, eu sou o dono da parada, eu sou o dono do cliente, eu sou o dono da ideia, tal. O cara foi um cara que eu trouxe. Então assim, eu tenho o poder de falar: "Vai a chave aqui, tô mandando minha nota, Marcelo, agora minha nota vem daqui". Mas é lógico, não é isso que eu quero e eu quero que ele chegue nessa conclusão.

### 16:48:16
**Marco:** Sim, e você precisa entender o posicionamento dele também, o que que o cara vai se propor. Porque é o que eu tô falando, tudo questão de posicionamento. Se o cara chega e fala: "P***, que animal, velho, pô, agora o negócio foi para outro nível, vamos fazer, vamos acontecer".

**Marcelo:** Eu acho que quando ele vê isso, com certeza vai ser pelo que eu vi dele. Ele vai sentir isso porque assim, ele não teve a cabeça que você teve de olhar pro negócio e falar: "C*****, isso aqui é um business grande, tem óleo e gás envolvido, cara". Você me conhece há mais tempo, você sabe que eu fuço numas gavetas grandes e tal. Então, o cara tem uma gaveta. Ele não teve isso porque senão ele parava para olhar, velho. Então para ele a gente tem mais uma solução aí, velho.

### 16:49:19
**Marco:** É um jovem, né?

**Marcelo:** Tem mais outras pequenininhas com os parceiros e tal. P***, você é diferente de você que olhou e falou: "Cara, vou gastar meu tempo, vou botar meu tempo, meu dinheiro aqui, vou parar para fazer isso". Então tá claro isso, né, velho?

**Marco:** Beleza, não é tarde. Se o cara entender até que tarde e falar: "P***, beleza, entendi só agora o que eu já deveria ter entendido".

### 16:50:19
**Marco:** É o que eu falei, velho, quanto mais a gente potencializa o negócio, melhor. Tem um cara que vai assumir várias broncas e vai entrar de cabeça na parada, velho. A gente se divide para multiplicar.

**Marcelo:** E ainda, primo, nós fizemos, nós demos uma reformulada na parada que profissionalizou de um nível e ainda dá tempo dele olhar, falar: "Cara, vou largar umas coisas e vou montar com esses caras". Porque tem, entendeu? É isso que eu tô esperando, que eu acredito que ele vai olhar e vai falar: "P***, velho, eu achei que não ia para esse lado. Os caras fizeram um bagulho f***".

### 16:51:11
**Marco:** E foi a visão que eu tive quando você começou a me falar e me mostrar o negócio.

**Marcelo:** Encostar...

**Marco:** Eu falei: "Não, velho, esse negócio tem muito mais potencial para estar do jeito que ele tá, velho. Eu vou tentar botar minha mão aqui para elevar o negócio, pra gente poder dar mais um passo, para aí dar mais outro passo e assim ir".

**Marcelo:** E assim, eu acho, primo, que ele é um cara que esses pauzinhos que vai dando, ele tem uma... ele conhece tempos mexendo, ele vai saber: "Cara, isso é LLM. Não, cara, isso é Supabase". Em vez da gente ficar batendo cabeça, testando, ele já tem. Então, é um cara que soma, eu tenho certeza, cara.

### 16:52:11
**Marco:** Total. E tipo assim, com certeza eu ainda vou, quando eu conhecer ele, eu ainda vou ter mais visão do que mais ele pode somar, fora o que você já sabe. Então assim, é só questão de você entender a postura, você conduzir, entender a postura do cara para você entender como ele entra na composição e quem vai tomar essa decisão é você. Então tá tudo certo.

**Marcelo:** Sim, mas eu acho que vale a gente... depois eu vou preparar a hora que tiver redondinho. Acho que nem preciso falar que a gente validou com o Marcelo e tal para ele não sentir que a gente talvez atravessou alguma coisa assim.

**Marco:** É, faz um, troca uma ideia com o cara, faz um call com ele, mostra tudo, manda para ele mexer. Às vezes ele mesmo acha algumas coisas que a gente ainda não achou.

### 16:53:58
**Marco:** É, não, isso aí é problema bom, velho. Problema bom. É o que importa, velho, o negócio tá evoluindo. Você ainda nem começou a bater nas portas que vai dar para bater, né? Isso é um V1, porque o que você tinha, primo, era um MVP, né? Agora a gente não é MVP rodando. Então agora a gente tá saindo do... a gente agora a gente tá indo para um MVP profissional do V1 do produto.

### 16:55:03
**Marco:** Quando a gente validar depois de um mês, ele vai ser um V1 rodando. E aí a gente ainda vai ter um gap aí de alguns meses para a gente profissionalizar ele realmente no nível alto, que aí é ver rodando, melhorar a latência, de repente migrar um Supabase para um negócio mais pro.

**Marcelo:** Sim.

**Marco:** Quando você quer botar um negócio com a segurança mais forte para ficar mais rápido num servidor mais f***, aí vai entrando várias outras coisas. Então a gente vai olhar para a estrutura, depois vai falar: "Cara, beleza, o negócio tá funcionando, tá bom, tá promissor, tá bonito, tá atendendo o que a gente precisa. Agora vamos começar a bater em outras portas".

### 16:56:02
**Marco:** E aí vai entrar...

**Marcelo:** Mas nós fizemos muito baseado na estrutura de um MVP rápido, saindo da solução e pau. Beleza, agora... vai, mas já pensando em uma auditoria, já olhando como é que eu, p***, catalogando os processos.

**Marco:** Não, parte de compliance, parte de negócio já tá maduro. É mais a estrutura técnica de produto, código, de cara depois plugar um dev para falar: "Cara, o que que tem de segurança? O que que pode vazar? Como é que o cara pode me hackear?". Esse tipo de coisa que não vale a pena a gente olhar agora.

### 16:57:02
**Marco:** E o mapeamento de todo o processo que você tem aí. O que que faz? O que? Em que momento? O desenhinho. Aquela sua primeira reunião hoje foi aquilo, velho. Ali para mim é onde tá o valor da parada, velho.

**Marco:** É que sem aquilo você não tem como conversar com o cara, porque o cara não é técnico nem você. E aí como é que você vai explicar que "funcinho de porco"? Você vai falar: "P***, mas mano, eu joguei na IA aqui que ele montou uma básica e tal". Não, mano, tá aqui, ó, tudo que eu tenho coberto, o que não cobre, por quê, o que aprova no automático, por quê, como é que meu motor pensa? Como é que a gente integra as duas coisas? Beleza, legal. O cara vai falar: "P***, é isso mesmo".

### 16:57:52
**Marco:** Enquanto a gente conversava, ele me deu... Confirmei. O problema aqui não é só o SER. Esse caso do Laudis põe uma falha maior. A base atual tem vários PDFs reais, mas a parte da extração ficou gravada certo no metadata e errado/vazia nos campos que o motor usa para decidir. Também confirmei uma coisa importante: no Supabase atual, o Laudis não tem nenhum item confere. O print antigo mostra cinco conferes. Então vamos lá, passando item a item. Resumo direto, o print antigo está mais próximo ao resultado operacional correto. A base atual não tem SER. A base atual não encontrou CES, apesar do print antigo de cinco confere. O motor atual está falhando em três pontos: não promoveu campos extraídos do metadata para os campos estruturados, não usou de forma correta os alias compostos da matriz e deixou a declaração também contaminar outros itens da matriz quando deveria ter sido isolado e não substituto de documento. Próximo passo correto é fazer o hotfix dos dados para esse caso virar nosso golden test.

### 16:59:31
**Marco:** Lud precisa fechar como confere, confere, confere, parcial, parcial, CES pendente ou reimportar.

**Marcelo:** Pode meter bronca, priminha. É isso mesmo.

**Marco:** Mas o bom da gente estar plugado com a IA é isso, porque além dele rodar esse golden test, ele vai extrair o padrão e a gente vai replicar em tudo.

### 17:00:50
**Marco:** A regra é isso, a regra é aquilo, entendeu? Aí você consolida. Agora ele não tá consolidado porque, cara, toda hora mudando de layout, toda hora mudando o nome de botão, toda hora tirando um botão daqui, botando aqui. Então, não adianta você consolidar.

**Marcelo:** É isso aí, velho. É a forma de construindo.

**Marco:** E deve ser isso, né, velho? Você imagina o cara lá no terminal fazendo no código lá, velho. Você acha que o cara sobe um negócio já igual no "loambadinho", bonitinho?

**Marcelo:** Não, não, velho. Hoje em dia o bagulho tá muito mais fácil para fazer, né, velho?

### 17:01:37
**Marco:** O cara é... entendeu?

**Marcelo:** E é complexo. E é por isso que os caras tão ficando louco, que ele fala: "Velho, a gente não... os caras nunca imaginaram que o bagulho tão complexo do que eles sabiam fazer ia ficar tão fácil, né, velho?". E uns carinhas, uns dev, tem uns devzinho que eu vi outro dia, o cara: "Velho, o bagulho tá muito louco, realmente". Antes eu achava que eu não ia perder meu emprego, agora eu já perdi. Por sorte eu tô olhando isso aqui como uma oportunidade e tô aprendendo. Mas assim, o que eu sabia fazer, esquece, velho. Acabou.

### 17:02:28
**Marco:** Que louco.

**Marcelo:** Nós pegamos os caras, raspamos os caras no meio do caminho, né, primo?

**Marco:** Porque hoje, mano, você só precisa ter tempo, porque assim, você vai resolver, mas se você não for pro caminho certo, você vai dar volta. Então, esse é que é o lance. Então, assim, quanto volta você vai dar, é o que vai diferenciar quem tem velocidade e quem não tem. Por exemplo, eu passei por três fronts para chegar no que a gente tem hoje.

**Marcelo:** Mas com certeza no seu próximo desenvolvimento você não vai fazer isso.

**Marco:** Exatamente. Então, assim, por quê? Porque eu achei que o motor era tão importante que eu ia fazer o motor inteiro primeiro e depois eu ia fazer o front. Tava errado meu pensamento? Não, mas eu fui muito curto aqui em olhar para a parada. Primeiro eu tive que ter desenhado a experiência para fazer um wireframe de como ia ser o uso do produto para criar o motor pensado no uso.

### 17:03:43
**Marcelo:** Cara, não, eu não sei porque eu acho que o motor era o mais importante do que precisa validar depois. Era... é que é meio, p***, meio junto, né?

**Marco:** Mas o motor ele é determinístico. Como é que você vai plugar o motor a experiência? Primeiro você tem que saber a experiência.

**Marcelo:** É, mas pensando, p***, para mim o importante você falar assim: "Eu vou jogar os certificados aqui, ele vai lendo o motor, vai me devolver uma planilha", já resolve a vida dos caras lá. E nunca ninguém resolveu isso. Jogar numa planilha com confere, não confere, tudo na mesma ordem, desnomeado, porque que p*** só na linha já é p***. Aí é o motor só trabalhando, falando: "Cara, vê a regra, vê se bate". Isso aí para mim é coraçãozão. Aí depois o resto vai vindo perfumaria, um monte de coisa que aí vai facilitando mesmo a vida do cara.

### 17:04:31
**Marco:** É, mas aí a gente entra no ponto, velho, do profissional. Então o profissional ele tem que atender tudo. Por mais que o seu apelo ele seja o motor, fala: "Beleza, velho, esse negócio é o motor, é o compliance, é a certeza". OK. Só que para ele ser profissional, o visual vai ter que estar alinhado, os botões vão ter que estar tudo certinho, tudo com a nomenclatura certa, senão o cara bate o olho, ele não vê esse profissionalismo. Você tá lá com o motor f***, vai falar: "Pô, velho, beleza, mas parece só uma solução caseira".

**Marcelo:** Aí você manda na no Excel para mim, aí fodeu, né?

**Marco:** Aí você fala: "Pô, beleza, mas lá no Drake o negócio é pré-histórico". É beleza, velho. Mas os caras começaram na época pré-histórica, eles só não se atualizaram. Se a gente quer ganhar notoriedade, a gente tem que ter o diferencial.

### 17:05:32
**Marco:** Qual que é o diferencial? É a plataforma. Não é porque é bonitinho, porque o cara tem que olhar, velho, e agregar valor. Isso aqui é o que faz valer dinheiro. Você pode falar que o motor é f***, mas se o visual for tosco, o cara não vai valorizar, velho. Agora se o cara, o motor é f*** e o visual é f*** e tudo é profissional e tudo é coerente e tudo é bonitinho, você começa a ser caro. Você é caro porque o cara fala: "Velho, isso aqui não custa barato".

**Marcelo:** Os caras vão vir para cima de nós, priminho. Nós vamos receber, nós vamos pegar umas milhas aqui só nessa brincadeira, velho. Posso do jeito que tá, a gente, eu tenho certeza que a gente falava: "Vamos vender essa p****". A gente vende essa p****, velho.

### 17:06:20
**Marco:** Vamos fazer barulho com calma. Aí você começa a inserir nos eventos, a gente vai mostrando o negócio, o negócio é chegar de mansinho e a galera ir falando: "Eita, p***, que que é isso aqui?". É, velho, olha aí, testa aí, veja aí. Ah, mas p***, mas você cobre isso, você cobre aquilo... mas p***, mas você tem tudo isso aqui dentro? É, então. É como quem não quer nada e deixar um negócio f***. É o que eu falei, a estrutura que a gente cria, velho. Imagina o próximo projeto do zero, como é que a gente já não vai ter de estrutura em cima? É o que eu tô falando, igual eu tô fazendo pro ADR lá do Stock. Pô, várias ideias veio pro Certify aí, pô. Beleza. No aí já tem o negócio. P***. Aí você conhece um cara de logística que tem logística de galpão, de estoque, você já vai pensar: "Pô, temos um produto na gaveta ali pronto". Se quiser plugar pro cara e cobrar 20 pau no mês, já tá pronto. É só sentar com o cara, fazer uma reunião, entende o universo dele, a gente contrata um molequinho sagaz para fazer o todo o briefing, toda a pesquisa, tudo que tem que fazer o trabalho pesado e a gente começa a ir plugando as coisas. Então, p***, é nisso que eu tô mais interessado.

### 17:08:03
**Marco:** É tipo, cara, se agora dá para fazer isso, imagina daqui um ano o que que vai dar para fazer e como que a gente vai estar fazendo.

**Marcelo:** É, e eu acho que as coisas... eu acho que os caras vão fechar o cerco das... talvez não tão rápido, mas as coisas vão, como o Claude tá fazendo, velho. O cara tá metendo preço em cima agora, né?

**Marco:** E outra coisa, primo, a gente pensa que, ah, IA tal, não sei o quê, vai... qualquer um que paga sete contos de IA por mês, que é o que eu tô gastando, né?

**Marcelo:** É, e tempo, velho. Quem tem 10 horas do dia para ficar olhando e fazendo, construindo o negócio, velho.

### 17:09:00
**Marco:** Não. E tipo assim, realmente se você for pegar de crédito aqui o que tá gastando de crédito nesse projeto, já deve ter dado uns R$ 5.000. Mas isso é o de menos. Só que você, se você for pensar, não é qualquer um que mete as caras de tipo: "Pô, vou assinar o plano de 200 do Claude, de 200 do GPT, todas as ferramentas complementares e o SPF e não sei das quantas e até o Cursor". Essa semana eu tava vendo para colocar aqui. E assim, não é nego que tem o sangue... o sangue...

**Marcelo:** É aquela coisa, né, velho? Era igual nós no negócio de cripto. Ah, velho, p***, ficava estudando, estudando, mas tem que ter o dinheiro para entrar, velho. Não adianta. Ah, legal. Entendi. Projeto f***, se entrar nesse... no dinheiro. Não tinha dinheiro para pôr. Aprendi como que fazer, como é que vai, não tinha dinheiro para pôr. Aí agora ela tá mais democrática, né? Porque o cara consegue fazer de graça.

### 17:09:58
**Marco:** Sim. Mas primo, é de graça até certo ponto. Por exemplo, você, ah, vamos brincar aí e tal, você já botou o plano do Claude de 100, mas você não tá trabalhando um 1/5 de volume de código do que eu tô. Se você começar, você vai começar a ver: "C*****, tá caro". Beleza. Mas, mano, até o cara entender que ele realmente precisa investir essa quantidade para ele se inteirar... não tô falando de retorno não, mano. Eu investi, não foi pensando: "Ah, pô, porque eu vou fazer os projetos". Eu investi pensando assim: "Cara, para eu dar o catchup com o que eu tô vendo, que tá rolando no que eu tô acompanhando, o mínimo que eu preciso é ter liberdade total com Codex, com Claude para rodar sem pensar em crédito". Isso é o mínimo. Então assim, já só aí já é três contas, aí você começa a pôr o resto, né? Aí já vai inflando. Então assim, eu tô vendo que tem essa barreira de entrada, cara. Muita gente entende igual meu brother DJ, pô, me ligou esse fim de semana: "C*****, mano, agora tô te entendendo, p***. O brother me mostrou aqui, o Claude ficou duas horas comigo, eu já fiz isso, isso aqui, já criei um negócio pra minha empresa".

### 17:11:59
**Marco:** Velho, o cara tá tipo assim, primeira vez que o cara conheceu o Claude e eu tô falando... eu tô p*** mano, que f***, que irado e tal. Só que o cara fala aí, p***, mano, aí, pô, já pagou 20 por mês, aí o bagulho no meio do negócio travou porque não podia, p***. Aí eu falei: "Cara, bagulho...". E o moleque tem grana, sacou? Então assim, tipo assim, nego não... cara, até o próprio Bone, você vai ver, tipo, nego que realmente assina a parada e usa, heavy user, são poucos para mim. E quando a galera virar user, vai ficar tão caro que o user vai ser 5.000, 15.000.

**Marcelo:** Já foi. Então é isso aí. Por isso que nós estamos sendo cobaia dos caras para testar toda hora modelo novo. Mas beleza, mas nós estamos também aprendendo, né, velho?

### 17:12:51
**Marco:** Exatamente. Tem sendo remunerado para fazer o rolê, entendeu? E e outra e olhando tipo, beleza, velho, hoje nós estamos rodando aqui com Claude, mas a hora que virar a chave aqui, o motorzão tá preparado para pegar um GPT, para pegar um Kin, para pegar qualquer p***, porque nós não vamos...

**Marco:** E aí o modelo e a gente que tá todo dia ali, por exemplo, vários dias a gente tava: "Velho, tá uma m**** o Claude, tá uma m****, o bicho não tá pensando, tá travando". De repente muda o modelo pro novo e a parada fica sinistra. Só que você tá trampando todo dia, normal. É só mais um guia e aí o negócio vai para outro dia, meu.

### 17:13:39
**Marcelo:** É, e eu acho que os caras fazem isso, o cara faz isso exatamente para valorizar o próximo modelo. Dá uma travada geral.

**Marco:** Sim, ele vai degradando ali. Quando chega perto de lançar o último modelo, ele vai degradando para você ter uma sensação f*** quando lança o negócio. Só que o que eu tô falando é, eu tô trabalhando todo dia, independente do modelo, modelo bom, modelo ruim. P***, teve momentos do Certify aqui que tava f***, mano, que eu tava trabalhando aí, a IA tava burra para c*****, não fazia nada, eu mandava fazer uma coisa, ela fazia outra e você tem que trampar do mesmo jeito, velho.

### 17:14:39
**Marco:** E você tem que ir fazendo. Só que você tá no meio do dia a dia e aí sai um GPT-6 e aí sai um OPO-5 e aí daqui a pouco qual vai ser as possibilidades? Porque você tá todo dia, entendeu? Então esse é o ponto, mano. Se você tá todo dia, velho, você vai acompanhando a mudança. Esse é que é o que eu entendi, velho, que é o f***. Não é que o bagulho mudou, você perdeu o N8N. Não, velho. Tudo que você saber de N8N, a arquitetura tá aqui. Agora você não tem uma coisa, outra que vai ficar em aberto.

### 17:15:37
**Marco:** Então assim, só que o ponto é que tem gente que é saudosista. O cara se apega na ferramenta, não no processo. Esse aqui é o ponto. Tem... é igual o cara do vinil que p*** mudou para CD, o cara não, velho, porque pô, CD não presta, o negócio é vinil e tal, cara. Saudosismo puro.

**Marcelo:** Foi engolido.

**Marco:** Então se você não... pô, então pô, eu tocava vinil, virou CD. Agora eu vou ser monstro do CD com tudo que eu já aprendi do vinil. P***, agora é mais fácil. Não tem que carregar o bagulho pesado, não estraga no sol, não sei das quantas. Não, velho. O cara ficar naquela p****** lá de "não, velho, o bom é o vinil". Entendeu? Por o cara não quer se dispor a soltar o que ele sabia para aprender o bagulho novo de sair da zona.

### 17:16:23
**Marco:** O cara fala: "Velho, aqui eu domino, enquanto tiver funcionando isso aqui, enquanto ainda ligar, eu tô on". É.

**Marcelo:** O cara ainda tá no conforto. É isso aí.

**Marco:** É, então assim, o que vai mudar é isso, velho. É quem tá aberto para pular para frente. Se hoje chegar um bagulho e falar: "Cara, não é mais Claude, não é mais Codex, agora é o Capivara, vamos embora pro Capivara, mano. P******** do c* do Codex, pau no c* do Claude", entendeu?

### 17:17:22
**Marco:** Não, eu já mexi bastante no meu show, já botei várias regrinhas que só funciona pro GPT, que pro OPS não precisava, já dei uma mexida boa. Agora depois da atualização do 5.5, aí mudou, mudou, mudou legal, porque eles trabalharam muito na última atualização do OpenCloud. Você tem que atualizar o seu OpenCloud pro último e botar ele para rodar no 5.5. Aí você vai sentir o Hermes. O Hermes também tá pica, velho. O Hermes com 5.5 tá animal.

### 17:18:32
**Marco:** Aí eu tô pensando em deixar o OpenCloud para assistente porque ele tem mais coisa, ele tá muito mais maior, tem muito mais estrutura do que o Hermes. O meu Hermes tá bem minimalista assim, ele só tem o que precisa, poucas skills, poucos crons, então ele tá tipo, é, ele tá muito selecionadinho e o OpenCloud tá assim, a p*** toda. Então eu acho que eu vou deixar o meu OpenCloud para ser um assistentezão bala. E o Hermes para ser um CEO, entendeu? Para ser um cara mais coordenador.

**Marcelo:** Passar o que tiver aprovado para ele.

**Marco:** Um cara mais coordenador, um cara mais poucas palavras. Eu tô criando um negocinho aqui que eu não tive tempo de mexer. Eu mexi na semana do meu sogro lá, mas um negocinho para ser um painel de junção de tudo. Ele vai controlar o Hermes, vai controlar o OpenCloud, vai controlar a sessão do Claude e vai controlar a sessão do Codex. E aí eu quero botar eles para se falar.

### 17:19:33
**Marcelo:** É, mas você vai dar o acesso e tal, eles vão, alguém dos caras vão se falar e puxar as informações que precisa.

**Marco:** É, eu não sei como, velho, como é que é, se é sem link, qual que é a tecnologia usada para você conectar essas diferentes plataformas em tempo real, porque o que eu quero é tipo, por exemplo, cara, eu tô... eu tenho cinco sprints para fazer do Certify, uma para cada coisa. Então, uma eu vou mexer na aba de revisão, outra eu vou mexer no centro de comando, outro vou mexer no Supabase. Beleza? Eu planejo isso. E aí eu quero que, tipo, por exemplo, o que é de design, eu quero que toque no Claude. O que é de código, eu até quero que toque no Codex. O que é de supervisão, eu quero que vá pro Hermes e o que é de pesquisa barra meio de campo, OpenCloud. E eu quero que todos eles se conversem durante a sessão.

### 17:20:45
**Marco:** Então o cara do front, eu preciso que o cara do backend me entregue isso aqui. O cara fala: "Ó, daqui a 2 minutos, porque eu preciso do cara do supervisor validar tal coisa". E aí sim você vai começar a chegar num ponto mais autônomo, que eu não vou precisar ficar na frente da tela igual eu fico toda hora. Aí o meu ponto vai ser planejar e entregar e conseguir.

**Marcelo:** Planeja e a execução se acompanha onde tiver.

**Marco:** Então aqui, ó, te mostrar só para você ver a cara do bagulho. Tá ficando, mano, embaçado aqui, ó. Um Chrome aqui, ó. Tá vendo aí? Então aqui você tem aqui, ó, né, o home, as connections, aqui você tem o Hermes, aqui você tem o OpenCloud, as sessions, os arquivos. Isso aqui é tudo Hermes, tá vendo?

### 17:21:58
**Marco:** Aqui é o Hermes é azulzinho. O OpenCloud quando eu clico fica vermelho. Tá vendo? O Claude quando eu clicar vai ficar laranja. O GPT vai ficar preto, entendeu? Então vai ter tudo aqui, vai ter tudo rodando aqui. Então aqui, ó, por exemplo, aqui eu tô no OpenCloud. Aí aqui eu tenho aqui, ó, é porque eu tô no Dev server, ele não tá na versão atualizada, mas já tá funcionando já o do OpenCloud também. Então vou ter aqui conexões, Chrome, os EG, skills e tal. Aqui eu tenho terminal, ó. Se eu abrir aqui, ó, o RS, eu tenho terminal. Não tá funcionando nessa versão, mas já tá funcionando na outra. Já tá escrevendo. O transporte caiu, ó. Tem que reconectar o host para funcionar. E aí aqui vai ter Claude, Codex, OpenCloud e Hermes.

### 17:23:04
**Marco:** E aí eu vou criar um outro ambiente. Aqui é só para configurar, né? Coisa tipo skill, arquivos, Chrome, beleza? Sessions, tal. Aí eu vou ter um outro ambiente que é de action, aonde você vai abrir e esses caras, eu tô pensando em fazer um negócio tipo um grupo de WhatsApp, aonde cada agente vai ser uma pessoa no grupo aqui dentro, uma interface, tipo um grupo de WhatsApp. E aí dentro do grupo, dentro do grupo de WhatsApp, mano, vai rolar tudo. Se você clicar na setinha, vai abrir o trabalho do Hermes. Se você clicar na setinha, vai abrir o trabalho do Codex. Cada sessão que eu abri do Claude, vira uma pessoa dentro do grupo. Então, abri uma aba do Claude, ele entrou um cara no grupo, abriu outra aba, entrou outro cara, terminou o trabalho, fechou a aba, ele sai do grupo, entendeu?

### 17:23:58
**Marco:** Para saber quem tá trampando, tá ali, quem não tá. Então você abre o grupo ali, todo mundo conversa e todo mundo trampa junto. É isso que eu quero criar. Só que é lógico, entre a ideia e o produto final vai dois meses aí no mínimo. E tem que ter tempo para fazer isso. Então eu não tô olhando para isso para não bagunçar minha cabeça, né? Mas é animal, animal. P***, velho. Esse é o cockpit, né?

**Marcelo:** Vou voar que eu tô... já deu a hora de buscar bebê na escola, velho. Olha que p*** que...

**Marco:** Eu tenho que me preparar para a próxima aqui, primi. Mas então, amanhã no horário do meio-dia aí a gente segue o barco, beleza?

**Marcelo:** Dá um alô. Valeu, primo.

**Marco:** Estamos junto.
