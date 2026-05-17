---
kind: transcricao-clean
project: certify-mvp
confidence: 0.95
title: "Melhorias Funcionais na Plataforma Certify"
meeting_datetime: 2026-05-05T14:22:00
people: ["Marco", "Marcelo"]
gmail_message_id: 19df9c05ef7cfa28
gmail_thread_id: 19df9c05ef7cfa28
notes_doc_id: 1oyZ13oacGblJtlLEUdVaY0sBClMfRJCFnmyS4UGVjws
---

# Transcrição (limpa): Melhorias Funcionais na Plataforma Certify

**Participantes:** Marco, Marcelo

### 00:00:00
**Marco:** Grande.
**Marcelo:** Fala, priminho.
**Marco:** Priminho.
**Marcelo:** Firme? Tá num visual, hein, mano.
**Marco:** Estamos nas alturas aqui, priminho.
**Marcelo:** Tudo certo.
**Marco:** Tudo certo, irmão? E aí?
**Marcelo:** Já dei um giro geral aqui.
**Marco:** Se familiarizou aí?
**Marcelo:** Sim, já entendi a parada. Tem alguns pontinhos que fui mapeando para a gente dar uma olhada. Acho que a gente poderia evitar alguns conflitos usando aquela matriz antiga. O que eu faria primeiro era subir uma matriz nossa e os documentos com tudo zerado, para não puxar rastro nenhum. Ou, se você preferir, dar uma olhada nesses pontos que eu mapeei.
**Marco:** Você está falando em termos de aprovação?
**Marcelo:** Tem algumas coisas de termo de aprovação, mas trouxe pontos de cada aba, coisas simples, às vezes um botão que não está funcionando.
**Marco:** Tá, vamos passando aí.

### 00:02:50
**Marco:** Não sei se ele já fez o deploy das últimas atualizações do motor, mas vamos passar no detalhe, um a um.
**Marcelo:** Tá, deixa eu jogar para cá. Deixa eu ver como fica melhor para mim.
**Marco:** Mano, você usa o Chrome? Já viu o negocinho de mudar as abas?
**Marcelo:** De abrir elas juntas em dupla?
**Marco:** Não, não sei se o seu está atualizado. Quer ver? Põe na tela aí que eu te mostro.
**Marcelo:** Vou dividir a tela.
**Marco:** Abre umas abas aí.

### 00:04:46
**Marcelo:** Vamos abrir o Cloud.
**Marco:** Vai abrindo qualquer coisa. Clica ali do lado do mais, na parte vazia.
**Marcelo:** Nova guia, reabrir guia fechada, adicionar todas as guias aos favoritos, nomear janela, gerenciar tarefas.
**Marco:** Não, você tem que atualizar o Chrome. Tem que estar na última versão.
**Marcelo:** Ah, reiniciar para atualizar. Ele vai reiniciar tudo.
**Marco:** Manda pau.
**Marcelo:** Depois a gente reinicia. Mas o que ele faz?
**Marco:** Aqui, ó. Você vai do ladinho, ele tem esse "show tabs". Aí ele manda para cá as abas.

### 00:07:45
**Marco:** Dá para você fechar elas aqui. Se ligou? Drive, e-mail.
**Marcelo:** É basicamente onde eu coloco elas todas salvas, onde você pôs o workspace LLM.
**Marco:** Mas aqui são as que estão abertas. Em vez de ficar tudo aqui em cima, elas ficam na lateral. Você pode agrupar.
**Marcelo:** Fica mais visível, melhor.
**Marco:** Exatamente.
**Marcelo:** Sabe por que eu comecei a fechar? Porque estava pesando muito.
**Marco:** Mas isso não é para deixar aberto, é para organizar enquanto você está usando.
**Marcelo:** Tá melhor do que tudo aberto lá em cima.

### 00:08:45
**Marco:** Na última versão eles colocaram essa parada. Deixa eu abrir o Certify.
**Marcelo:** Bora lá. Vou dividir a tela com você. Fui anotando as besteirinhas para a gente ir realinhando.
**Marco:** Agora é no detalhe.
**Marcelo:** Quando vou criar uma nova vaga, não está dando para colocar o recrutador.
**Marco:** É porque não tem nenhum criado nessa versão.
**Marcelo:** Imaginei. Acho que ele já deveria puxar de padrão o cara que está logado criando a vaga, ou permitir escolher o responsável.
**Marco:** O criar vaga já está funcionando.
**Marcelo:** Beleza. Vamos limpar tudo que tiver de informação antiga. Não consegui salvar a vaga, mas beleza. Aqui em "Insights" da vaga, ele abre e edita.
**Marco:** Essa tela inclusive tem que mexer, está antiga ainda. Não está no esquema do novo. Estou anotando.
**Marcelo:** E o que é o "Head"?
**Marco:** Não tenho a mínima ideia. Essa aba está desconsiderada.

### 00:11:21
**Marcelo:** Beleza. Aqui na triagem, quando eu mudo o status, ele não altera lá dentro do card.
**Marco:** Não, não está alterando ainda.
**Marcelo:** Eles não estão vinculados. Dentro do candidato não consegui trocar a barra superior do funil. Na triagem também não faz.
**Marco:** Já tinha mudado a nomenclatura dos títulos, mas perdeu esse commit na limpeza que fiz nos últimos dois dias. Vou ter que refazer.
**Marcelo:** Ele está puxando maiúsculo porque deve estar vindo da base antiga. Quando você limpar a base, talvez resolva.
**Marco:** Mesmo assim, a regra de limite de caracteres e padrão de escrita já estava funcionando. Isso voltou uns passos para trás em termos de layout, mas a funcionalidade está OK.

### 00:13:49
**Marcelo:** Quando venho para "Parcial", seria importante ter a observação.
**Marco:** Já tinha. Mandei tirar a validade porque você coloca no próprio documento e a observação já vai dizer se está vencido. Não precisa bater o olho na validade.
**Marcelo:** Entendi.
**Marco:** As ações ficaram com três ícones e o título não vai esticar, liberando espaço. Já estava tudo pronto, só preciso achar no Git essas alterações e recolocar.

### 00:14:59
**Marcelo:** Na revisão, ele não me dá opção de revisar aqui. Deveria ter um "aprovar" ou "rejeitar" para eu já tomar ação.
**Marco:** A revisão foi feita para enviar para a aba de revisão, onde você tem a visualização completa. Mas podemos colocar o botão direto aí, por que não?
**Marcelo:** Quando estou trabalhando, quero resolver o cara ali mesmo.
**Marco:** O ideal é uma parada mais macro. Se o cara está revisando documento, ele vai para a aba de revisão. Lá você vê só o que é do candidato.

### 00:17:12
**Marcelo:** Se eu estou trabalhando com vários candidatos, quero resolver esse cara específico. Cadê o Alfredini? Talvez um filtro por candidato.
**Marco:** Pode ter um filtro, mas de qualquer forma, os documentos ficam em ordem alfabética. Essa aba é para ele nem ter que entrar no detalhe do candidato.
**Marcelo:** Quando pinga um documento, preciso ter um contexto do que é essa NR e a observação dela.
**Marco:** Você vai ter a aba da direita, que é a do contexto.
**Marcelo:** Aqui ela não está puxando a observação exclusiva daquela NR. Por que tenho que aprovar essa NR3?

### 00:19:15
**Marco:** Já tem a observação. "Lista de presença não é aceita como certificado".
**Marcelo:** Mas eu digo, quando estou olhando o certificado NR3, o que aparecer aqui tem que ser sobre esse documento exclusivo.
**Marco:** Entendi. Mas se for assim, ele vai ter que entrar de documento em documento. Dessa forma macro, ele vê todos os problemas de uma vez.
**Marcelo:** Mas eu não consigo olhar para o cara e saber o que preciso fazer com a NR3.
**Marco:** O ponto que está gerando estranheza é a ordem dos documentos. A ordem na fila de revisão tem que ser a mesma do painel.

### 00:21:18
**Marcelo:** Quando estou plugado na NR3, quero resolver ela agora.
**Marco:** A mesma ordem que você tem na esquerda, vai ter na direita. O objetivo é que o cara bata o olho e veja o que é crítico.
**Marcelo:** Se eu aprovo aqui, pum, próximo. E aqui ele tem a visão geral do cara.
**Marco:** A gente vai deixar essa opção de aprovação rápida. Tem atalhos no teclado também, mas não está ligado no backend ainda.
**Marcelo:** É importante saber quem aprovou e por quê. Se a carga horária está diferente da matriz, mas o cliente liberou, eu preciso registrar.
**Marco:** Quem passou já vai estar automaticamente registrado pelo login, e o histórico de movimentação fica na aba do detalhe. O comentário é opcional.

### 00:26:47
**Marcelo:** O botão de exportar para planilha não está aqui.
**Marco:** Saiu nessa versão. Vou anotar para ajeitar.
**Marcelo:** Está dando uma cortada no layout.
**Marco:** Percebi. Tem umas informações desnecessárias na vaga vinculada que vou limpar.
**Marcelo:** E o percentual de aderência? Está 40% da primeira etapa.
**Marco:** Ele está trabalhando em relação à vaga no geral. Se quiser deixar só em relação aos certificados, é só mudar o que manda.

### 00:29:22
**Marcelo:** Na lógica deles, o primeiro passo é o percentual da matriz para enviar para o cliente. Documento pessoal só entra se for contratado.
**Marco:** Entendi. Vamos zerar o catálogo e seguir a base.
**Marcelo:** A nomenclatura precisa seguir a base mais o "interno".
**Marco:** Não está 100% lapidado, mas vamos ajustar.

### 00:33:47
**Marcelo:** Na matriz, quando vou adicionar documento, não tenho a carga horária.
**Marco:** Tenta buscar por "8 horas" na busca.
**Marcelo:** Algumas aparecem, outras não. Seria importante ter uma coluna de hora.
**Marco:** Vamos focar nisso. Vamos começar a mexer agora.

### 00:37:54
**Marco:** Preciso que você faça uma auditoria para ver se todos os documentos da biblioteca aparecem na criação da matriz.
**Marcelo:** O que acha de limpar o catálogo antes? O que importa agora é a base.
**Marco:** Podemos. O catálogo é legado. A base é o que importa.

### 00:40:51
**Marcelo:** O catálogo deveria ficar em segundo plano, a base é o coração.
**Marco:** Concordo. A biblioteca não precisa ficar visível para ninguém, só para o supervisor. O catálogo serve apenas se der algum problema em um documento específico.

### 00:44:27
**Marco:** Imagina ter todos os treinamentos internos de todo mundo organizados. O negócio fica sinistro.
**Marcelo:** O próximo nicho é aviação, ANAC. Outro filé.
**Marco:** Preciso que todo documento da biblioteca apareça na matriz.
**Marcelo:** Ele já aparece, o que falta é a hora.

### 00:47:07
**Marco:** Vamos ajustar a busca para ser semântica e não literal.
**Marcelo:** E na base também.
**Marco:** Estou abrindo o terminal para mexer no motor. O classificador usa as siglas do catálogo, então vou migrar tudo para a biblioteca.

### 01:00:16
**Marco:** Quando abrir a plataforma, quero que abra no Centro de Comando, nunca em Administração. E em Administração, abrir primeiro Usuários.
**Marcelo:** Quando o recruta abre, ele vê só as informações dele?
**Marco:** Sim, quando clica em "Minha Fila".
**Marcelo:** E nas vagas, ele vê todas ou só as dele?
**Marco:** Mantive como no Certify antigo, todo mundo vê tudo.
**Marcelo:** Vamos deixar assim por enquanto.

### 01:02:00
**Marcelo:** Na triagem, ele só deveria ver os dele para não mexer no trampo dos outros.
**Marco:** Isso é fácil, é só filtrar pelo nome. Mas é outra etapa.
**Marcelo:** O candidato deveria ficar vinculado a um recrutador.
**Marco:** Ele já fica, mas como não tem recrutador criado, não tem o que vincular.

### 01:06:53
**Marco:** Estou migrando a base do catálogo para a biblioteca. É uma mudança grande.
**Marcelo:** Você está cobrando os créditos do Codex e dando essa pala?
**Marco:** O Codex foi cirúrgico. Ele achou 12 problemas no meu plano.

### 01:12:13
**Marcelo:** Voltei para o LEL porque o outro estava mudando o host toda hora.
**Marco:** Tem que se inteirar, não dá para só dar "sim".
**Marcelo:** Comecei a fazer um manual de onde parei para não perder tempo.

### 01:22:29
**Marco:** A abinha de login ficou irada. Vou fazer a logo depois.
**Marcelo:** Marquei para sexta-feira, 11 horas.
**Marco:** Vi o invite. Já aparece os documentos para revisar na "Minha Fila".

### 01:27:05
**Marco:** Quando clica na vaga, aparece o recruta. Pensei em abrir um popup com os candidatos.
**Marcelo:** Acho que está bom. É um filtro por empresa.
**Marco:** O recrutador tem que poder botar mais de um responsável.

### 01:33:19
**Marcelo:** R$ 2.500 só de IA.
**Marco:** Está chegando.
**Marcelo:** É mais de R$ 20 aqui, R$ 20 ali.
**Marco:** Estou usando o ClickUp para o time, mas para mim sozinho é burocracia.

### 01:39:52
**Marcelo:** Estou construindo uma plataforminha de lançamento. Quero monitorar o lead e fazer follow-up personalizado.
**Marco:** Acho que é muito mais um agente do que uma plataforma.
**Marcelo:** É simples botar um OpenCloud no WhatsApp.
**Marco:** Quero testar essas paradas.

### 01:51:56
**Marcelo:** Já tomei bloqueio no passado por causa de palavras de emagrecimento.
**Marco:** A galera acha que é festa, que pode tudo.
**Marcelo:** Estou pensando em e-commerce.
**Marco:** Eu também, estou selecionando materiais.

### 01:54:55
**Marco:** Tem a integração do Shopify com Cloud e Hermes. Você faz a loja inteira no prompt.
**Marcelo:** É o dropshipping que você não precisa mais aprender.
**Marco:** Mas tem que ter bala na agulha para anúncio.

### 01:57:12
**Marco:** O que neutraliza o TDAH é resultado.
**Marcelo:** Quando você tem resultado, você não para na metade.
**Marco:** Já está funcionando a busca da matriz. Digito "NR33" e aparece.

### 02:01:18
**Marcelo:** O N8N travou.
**Marco:** O que você faz quando trava?
**Marcelo:** Dou um grito. O cara está na call, já vejo aí.

### 02:24:45
**Marco:** Ficou melhor, mais organizado.
**Marcelo:** Perfeito. Tudo vindo da base.
**Marco:** O nome do documento, deixamos em português ou inglês?
**Marcelo:** Faria tudo em português e depois um botão para virar para inglês.

### 02:33:24
**Marcelo:** Vou dar uma descida rápida, chegou um cara para trocar a bateria do carro.
**Marco:** Vai lá, priminho. Vou ver se mato essa leva aqui.
**Marcelo:** Já dou um toque assim que liberar.
**Marco:** Valeu.
