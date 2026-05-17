---
kind: sumario
project: certify-mvp
confidence: 1.00
title: "Estruturação Técnica do Motor Certify"
meeting_datetime: 2026-04-27T14:43:00
people: ["Marco", "Marcelo"]
gmail_message_id: 19dd0a32fb659105
gmail_thread_id: 19dd0a32fb659105
notes_doc_id: 18LXdp-LgfwGcQdpvhADyueJ6D_1jUVOfkUcOK2t8Qq8
---

# Estruturação Técnica do Motor Certify

**Participantes:** Marco, Marcelo

# 📝 Observações

abr. 27, 2026

## Reunião em 27 de abr. de 2026 às 14:43 GMT-03:00

Registros da reunião [Transcrição](https://docs.google.com/document/d/18LXdp-LgfwGcQdpvhADyueJ6D_1jUVOfkUcOK2t8Qq8/edit?usp=drive_web&tab=t.lv06bnuggcb1) 

### Resumo

Reunião definiu estruturação técnica do novo motor de compliance e estratégia para apresentação do produto aos sócios.

**Ajustes do motor técnico**  
A equipe priorizou a estabilização do motor de validação sobre ajustes estéticos. Decidiu-se testar documentos individualmente para garantir precisão na aderência à matriz.

**Gerenciamento de exigências clientes**  
Clientes deverão fornecer esboços de treinamentos internos para importação correta. Ficou decidido criar uma aba de exigências específicas para evitar inconsistências no sistema.

**Estratégia de negócio produto**  
O foco será apresentar a conformidade normativa detalhada como valor central do negócio. Estabeleceu-se um cronograma de reuniões diárias para profissionalização do produto para testes.

### Próximas etapas

- [ ] \[Off Digital\] Criar V3: Desenvolver a versão 3 (V3) do sistema para testes. Deve ser uma base limpa, sem dados existentes.

- [ ] \[Off Digital\] Remover Empresa: Solicitar remoção da empresa teste denominada Marcelo da base de dados.

- [ ] \[Off Digital\] Investigar Candidatos: Fazer um scan nos 52 candidatos ativos para identificar por que não estão vinculados à empresa ou vaga.

- [ ] \[Off Digital\] Validar Nome: Implementar validação para garantir que o nome do candidato corresponda ao documento na checagem de certificação.

- [ ] \[Off Digital\] Padronizar Nomes: Estabelecer nomenclatura padrão para renomear documentos, matrizes e candidatos no sistema.

- [ ] \[Off Digital\] Estrutura Treinamento: Preparar estrutura nas matrizes para upload de exigências de treinamento específicas do cliente. Garantir o endereçamento correto na aba de certificados.

- [ ] \[Off Digital\] Detalhar Status: Implementar campo na visualização de detalhes para mostrar o porquê do status parcial ou da revisão. A informação deve mudar ao clicar no item.

- [ ] \[Off Digital\] Ligar Botões: Ativar e ligar todos os botões de interface pendentes. Incluir Aprovar para DP, Solicitar Revisão de NR e Rejeitar Candidato.

- [ ] \[Marcelo Costa\] Enviar Lista: Enviar a lista final de pontos levantados, incluindo os arquivos de lista de presença, a logo da MDE e o documento de exemplo com QR Code.

- [ ] \[Marcelo Costa\] Auditar Resultados: Realizar auditoria e cruzamento minucioso entre os resultados do motor de validação e a base de documentos real. Explicar item a item o que confere ou está pendente.

- [ ] \[O grupo\] Agendar Encontros: Agendar encontros diários de acompanhamento ao meio-dia para o desenvolvimento final.

- [ ] \[Off Digital\] Delegar V3: Delegar criação de V3 limpo, sem dados, para abrir o negócio. Vincular documentos da matriz ao V3 para teste real.

- [ ] \[Off Digital\] Realizar Hotfix: Fazer hotfix nos dados para o caso Laudis virar teste padrão (golden test). Corrigir falha na promoção de campos extraídos de metadata e uso de alias.

- [ ] \[Marcelo Costa\] Enviar Manual: Enviar o manual de como usar o OpenCloud com o GPT.

### Detalhes

* **Criação de Versão de Teste V3**: Off Digital planeja criar uma nova versão (V3) do produto para testes em um banco de dados limpo, o que levará cerca de uma hora e pode ser feito mais tarde ou na manhã seguinte ([00:00:00](#00:00:00)). Marcelo Costa sugere que o teste prossiga com a versão atual, que já está populada, por ser mais útil para os objetivos atuais. Off Digital esclarece que a base de dados em si será mantida, mas a nova versão (V3) não apontará nenhum dado de candidato ou matriz ([00:02:48](#00:02:48)).

* **Ajustes Cosméticos e Definição de Cobertura Baixa**: Off Digital observa que os próximos passos são principalmente ajustes cosméticos e de produto, como o que define um status de "cobertura baixa" nos cards ([00:02:48](#00:02:48)). Marcelo Costa concorda que o foco deve ser garantir o funcionamento do "coração" do sistema, adicionando elementos cosméticos e de usabilidade aos poucos ([00:04:00](#00:04:00)).

* **Atualização da Lista de Empresas e Matrizes**: Off Digital confirmou que as empresas foram atualizadas no sistema, totalizando 17, e que as matrizes já foram importadas. Off Digital menciona a necessidade de remover a empresa "Marcelo" (provavelmente uma entrada de teste) e explica que os documentos dos candidatos não foram carregados porque estão sendo limpos para se adequarem aos padrões do sistema e serem validados no motor ([00:05:02](#00:05:02)).

* **Endereçamento de Candidatos sem Empresa**: Off Digital identificou vários candidatos sem vínculo com uma empresa, o que precisa ser verificado no sistema para entender o motivo. Marcelo Costa sugere que isso pode ser devido a uma mudança anterior no banco de dados para criar um campo específico para a empresa ([00:06:35](#00:06:35)). Off Digital planeja rodar uma varredura (scan) para entender por que 52 candidatos ativos não estão vinculados a vagas ou empresas ([00:07:43](#00:07:43)).

* **Funcionalidade de Zoom no Mac (Dica Técnica)**: Off Digital compartilhou com Marcelo Costa uma dica técnica para usar o zoom na tela do Mac segurando a tecla Command e arrastando com dois dedos no trackpad ([00:09:44](#00:09:44)). Marcelo Costa descobriu que a funcionalidade de zoom já estava disponível no Google Meet e que seu Mac permitia o gesto de pinça para zoom sem o uso da tecla Command, o que facilitaria a leitura da tela compartilhada ([00:13:19](#00:13:19)) ([00:15:22](#00:15:22)).

* **Implementação de Checagem de Nomes e Documentos**: Marcelo Costa alertou para a necessidade de garantir que o nome do candidato seja checado em relação ao seu documento durante a validação, evitando que documentos válidos de terceiros sejam aceitos ([00:16:18](#00:16:18)). Off Digital solicitou que Marcelo Costa enviasse essa demanda por escrito no WhatsApp para garantir o acompanhamento ([00:17:41](#00:17:41)).

* **Definição e Classificação de "Modalidade"**: Marcelo Costa buscou esclarecer a nomenclatura de "modalidade", que ele associava a aspectos como "trabalhador de viga" ou "supervisor" em NR (Normas Regulamentadoras) ([00:17:41](#00:17:41)). Off Digital explicou que o sistema classifica como "modalidade" o que o próprio documento explicita, tratando o conceito anterior de Marcelo Costa como "variação" (variação da NR, como 6 horas de salvamento) ([00:18:54](#00:18:54)).

* **Fonte de Dados e Nomenclatura Padrão**: Off Digital esclarece que os dados sobre as normas (como o que pode ou não ser EAD, ou detalhes como "12 meses" em um certificado) são obtidos de fontes verídicas, como a Portaria e o site Gov.br, o que torna a informação indiscutível ([00:23:29](#00:23:29)). Marcelo Costa confirmou que esse esclarecimento "matou na fonte" sua dúvida sobre a origem dos dados ([00:24:24](#00:24:24)). A "modalidade" (informação do documento) virou "variação" no novo sistema ([00:22:34](#00:22:34)) ([00:25:11](#00:25:11)).

* **Criação de Nomenclatura Padrão para Documentos**: Marcelo Costa lembrou da pendência de padronizar a nomenclatura de documentos para facilitar a visualização e a lógica do sistema ([00:25:11](#00:25:11)). Off Digital confirmou que a criação de uma nomenclatura padrão para documentos, matrizes e candidatos é um item de baixa prioridade, pois a definição ideal depende da visão do sistema completo ([00:26:12](#00:26:12)).

* **Necessidade de Gerenciar Treinamentos Internos de Clientes**: Marcelo Costa trouxe a questão dos treinamentos internos e particulares dos clientes, como os da Hélix, que precisam ser controlados, mas não seguem uma norma padrão ([00:34:32](#00:34:32)). Em casos anteriores, esses documentos eram categorizados como "outros" ou "cliente", mas isso gerava erros ao serem confundidos com treinamentos oficiais, como o OPITO, pelo sistema ([00:37:06](#00:37:06)).

* **Solução para Gerenciamento de Exigências Específicas do Cliente**: Off Digital propôs que, para amarrar legalmente os treinamentos internos, o cliente deve enviar à equipe uma base de suas exigências para que uma estrutura específica (como uma "aba de exigências do cliente") seja criada no sistema. Marcelo Costa concordou que isso evitará que o sistema seja responsabilizado por inconsistências e exigirá que cada cliente forneça ativamente o esboço de seus treinamentos internos para importação ([00:39:21](#00:39:21)) ([00:48:18](#00:48:18)).

* **Melhorias na Visualização do Detalhe do Candidato**: Off Digital apresentou as melhorias na visualização dos documentos do candidato, incluindo ícones de "confere" e a organização dos documentos em blocos ([00:49:39](#00:49:39)). Foi notada a necessidade de exibir também o status "pendente" e adicionar um campo que explique o motivo de um documento estar em "parcial" ou em "revisão", idealmente ao lado da listagem de documentos ([00:55:40](#00:55:40)).

* **Funcionalidade de Revisão e Aderência à Matriz**: Off Digital explicou que o botão "revisão" envia o documento para uma fila de revisão humana ([00:55:40](#00:55:40)). O sistema também exibe o percentual de aderência do candidato à matriz (por exemplo, 38%), dividindo as categorias como saúde, operacional e normativo. O botão "aprovar para DP" (Departamento Pessoal) representa a etapa final, quando todos os certificados estão em dia ([00:57:48](#00:57:48)).

* **Validação de Documentos e Processos de Aprovação**: A discussão começou com a confirmação de que os documentos estão sendo validados, com Off Digital observando que um caso com 16 conferências estaria reprovado (em DP) imediatamente, enquanto um caso com 15 conferências e um parcial exigiria uma revisão manual \[i, 39\]. Marcelo Costa destacou que, nesses casos, o procedimento padrão da empresa é solicitar ao funcionário que resolva as pendências, suba os documentos atualizados e, em seguida, passe para DP (Dependência), o que poderá ser automatizado futuramente ([00:58:56](#00:58:56)).

* **Escopo da Declaração e Lista de Presença**: Off Digital confirmou a inclusão da declaração de documentos, e Marcelo Costa sugeriu expandir o escopo para incluir a "lista de presença". Marcelo Costa explicou que, embora a declaração seja um documento temporário (válido por 30 dias) antes do certificado final, a lista de presença (assinada pelos participantes de um curso, como a NR 20\) deve ser considerada como um tipo de documento complementar ao certificado, citando um exemplo anterior com a Shell ([01:00:20](#01:00:20)).

* **Necessidade de Amostras de Lista de Presença**: Off Digital solicitou que Marcelo Costa forneça arquivos de "lista de presença" para que a solução possa processá-los, aprender a tipologia e criar um parâmetro de triagem para essa categoria. Marcelo Costa anotou o ponto, comprometendo-se a enviar os arquivos via WhatsApp, e Off Digital mencionou que estava atualizando a ferramenta com o link dos candidatos com as empresas ([01:01:31](#01:01:31)).

* **Branding e Logo da MDE**: Off Digital mencionou a necessidade de definir o nome do produto, domínio e logo, sugerindo usar a logo da MDE (Mesma Empresa) de forma provisória. Marcelo Costa inicialmente questionou a necessidade, mas concordou que os clientes valorizam a inclusão da logo ([01:01:31](#01:01:31)). Off Digital sugeriu incorporar a logo da MDE ao lado do nome de cada recruta, substituindo as iniciais ou fotos, para que ela apareça em várias partes do sistema ([01:03:08](#01:03:08)).

* **Documentos de Rádio Operador com QR Code**: Marcelo Costa perguntou sobre a documentação de "rádio operador" (TCEA) e mencionou que alguns documentos, como o TCEA, vêm com um QR code cuja leitura é necessária para verificar a validade. Off Digital afirmou que a leitura de QR code é um recurso fácil de adicionar e que novas regras podem ser plugadas ao sistema ([01:04:55](#01:04:55)).

* **Checagem de Assinaturas nos Documentos**: Marcelo Costa introduziu a necessidade de o sistema de Reconhecimento Óptico de Caracteres (OCR) verificar se os documentos possuem assinaturas, um requisito solicitado pela Héliix ([01:04:55](#01:04:55)). Ele detalhou o padrão de assinaturas para diferentes documentos (como quatro assinaturas para NR e duas para OPITO) e mencionou a falta de assinatura do candidato em alguns documentos ([01:08:01](#01:08:01)).

* **Análise de Certificados Marítimos (STCW)**: Marcelo Costa adicionou que o certificado STCW (Standard Training Certification and Watchkeeping) requer a assinatura de um representante marítimo e um selo do DPC, que pode ser implementado em uma segunda fase. Off Digital pediu para anotar todos esses pontos, enquanto Marcelo Costa e Off Digital começaram a revisar a conferência de documentos de um candidato específico no novo motor ([01:09:53](#01:09:53)).

* **Divergências na Classificação de Documentos entre Sistemas**: A equipe analisou as contagens de documentos de um candidato, notando divergências entre o sistema anterior (Certify) e o novo motor, especialmente na classificação de documentos como pendentes, parciais e conferidos ([01:15:47](#01:15:47)). Eles identificaram que um documento (CAC EAEC) estava dando parcial no sistema antigo por falta de carga horária (40 horas exigidas), mas o novo motor estava validando como "confere" ([01:19:48](#01:19:48)).

* **Falso Positivo no Documento CRR/EGPM**: O principal problema identificado foi a validação incorreta de um documento, onde um item pendente (o CRR – Curso de Embarcação Rápida e Resgate) no sistema antigo, era erroneamente classificado no novo sistema ([01:22:30](#01:22:30)). Off Digital descobriu que o problema não estava no motor de aprovação, mas sim na interface do usuário (UI), onde a tela estava tratando uma classificação de "declaração" (um documento de EGPM) como "confere", levando a um falso positivo ([01:33:27](#01:33:27)) ([01:43:19](#01:43:19)).

* **Estratégia para Teste do Motor de Validação**: Marcelo Costa sugeriu que, em vez de usar grandes volumes de dados de importação que dificultam a identificação de erros, o processo de teste deve focar em subir documentos um a um para candidatos específicos, garantindo a validação da matriz. O objetivo é garantir que o sistema não misture regras e atue com precisão, pois o teste com volumes grandes pode levar a bugs e passar despercebido em detalhes ([01:37:13](#01:37:13)) ([01:40:57](#01:40:57)).

* **Melhorias na Interface do Usuário e Próximos Ajustes**: Off Digital confirmou a correção do erro de UI onde "declaração" era exibida como "confere" ([01:43:19](#01:43:19)). O próximo foco de trabalho será em ajustes finais de usabilidade e motor, como consertar a aba de pendentes, ligar a IA de forma funcional e garantir que os botões de ação operem corretamente ([01:50:02](#01:50:02)).

* **Otimização da Base de Dados e Matrizes**: Off Digital identificou que, embora a base de dados com as normas (como 194 documentos NR) estivesse completa, a funcionalidade de linkar essa base com a criação das matrizes não estava 100% pronta ([01:55:22](#01:55:22)). Isso exige um ajuste de rota interna para garantir que a biblioteca de normas alimente corretamente as matrizes ([01:56:23](#01:56:23)).

* **Considerações Finais sobre Prazo e Qualidade**: Marcelo Costa e Off Digital concordaram em focar na qualidade da entrega e evitar prazos rígidos, priorizando a estabilização do motor antes de liberar para os usuários. O objetivo é entregar um produto robusto que não exija que os usuários resolvam problemas básicos, garantindo que o tempo gasto na solução seja mais eficiente do que o trabalho manual ([01:48:47](#01:48:47)) ([01:53:26](#01:53:26)).

* **Acompanhamento Diário e Teste do Produto**: As partes concordaram em estabelecer reuniões diárias, preferencialmente ao meio-dia, para dar um impulso final ao projeto. A intenção é que o produto esteja pronto para testes no dia seguinte, focando em um "V3" sem dados para iniciar o processo de forma limpa e realizar um passo a passo real de criação da matriz ([01:58:26](#01:58:26)).

* **Expectativa de Valor e Ansiedade com o Produto**: Marcelo Costa expressou confiança no valor do novo produto, indicando que ele é superior ao que o cliente está acostumado a usar. Eles observaram que Marcelão, o contato de negócios, tem uma "cabeça de negócio" e reconhecerá a utilidade da solução ([01:59:30](#01:59:30)).

* **Estratégia de Apresentação a Adão (ADW)**: Foi discutida a melhor forma de envolver Adão, um associado que não está a par da extensão do novo produto, no processo. A sugestão foi validar o produto com Marcelo e, após a aprovação, apresentar a solução a Adão para que eles assumam a manutenção e responsabilidades diárias do novo sistema ([02:00:23](#02:00:23)).

* **Comunicação e Papel de Adão no Novo Produto**: Marcelo Costa enfatizou que, como Adão não tem ciência da criação do novo produto, a abordagem consultiva seria a melhor, demonstrando o trabalho de estruturação do processo e mapeamento da norma STCW ([02:01:31](#02:01:31)). Eles expressaram o desejo de que Adão reconheça o valor do trabalho e sinta-se confortável, percebendo que adquiriu uma participação (10%) no negócio devido à falta de capacidade deles em realizar a organização detalhada e a emergência nas regras ([02:05:10](#02:05:10)).

* **Valor da Análise de Processos e Conformidade**: Marcelo Costa destacou que o maior valor do negócio reside na imersão e estruturação dos processos de conformidade, incluindo o mapeamento linha a linha da norma STCW, o que Adão não realizou. Este motor do negócio, que demonstra por que os documentos "batem" ou "não batem" e que foi emergido no processo com auditoria, é o que será enfatizado na apresentação, em vez de apenas a interface (front-end) ([02:02:45](#02:02:45)).

* **Posicionamento e Confiança na Liderança de Marcelo Costa**: Off Digital manifestou confiança na liderança de Marcelo Costa, reforçando que eles são o proprietário da ideia e do cliente, e têm o poder de direcionar o negócio. Off Digital está somando e investindo seu tempo e habilidades no negócio, mas Marcelo Costa é quem ditará a composição e o crescimento, devendo conduzir a conversa para entender o posicionamento de Adão ([02:03:45](#02:03:45)) ([02:07:15](#02:07:15)).

* **Oportunidade para Adão e Visão de Negócios**: Marcelo Costa acredita que, ao verem o produto, Adão reconhecerá a oportunidade de se juntar ao empreendimento, visto que eles não tiveram a mesma visão para o negócio grande que Off Digital demonstrou ([02:08:16](#02:08:16)). O projeto profissionalizou a solução a um novo patamar, e ainda há tempo para Adão se envolver, o que Marcelo Costa está esperando que aconteça ([02:09:19](#02:09:19)).

* **Estratégia de Introdução do Produto a Adão**: Marcelo Costa planeja apresentar o produto diretamente a Adão sem mencionar a validação de Marcelo para evitar que se sintam "atravessados". Após a validação interna do produto, a intenção é realizar uma reunião para apresentar o compliance e a norma por trás do sistema, o que era a expectativa original de Marcelo Costa para o trabalho de Adão ([02:11:11](#02:11:11)).

* **Evolução do Produto: Do MVP ao V1 Profissional**: As partes reconheceram que o que tinham anteriormente era um MVP (Produto Mínimo Viável) em rodagem, e a evolução atual representa o MVP profissional do V1 do produto. O objetivo é, após a validação inicial do V1, profissionalizar a solução em um nível mais alto, olhando para a latência e migrando componentes técnicos para modelos mais robustos, como Superbase com \*Sko\*, para maior segurança e velocidade ([02:11:58](#02:11:58)).

* **Melhorias de Compliance e Estrutura Técnica**: A estrutura de compliance e de negócios está madura, mas a estrutura técnica de produto e código precisa de atenção futura para segurança e questões de \*hackeabilidade\* ([02:13:03](#02:13:03)). O mapeamento detalhado do processo de \*compliance\*, que envolve catalogar normas e entender o motor de aprovação, é o ponto de maior valor da solução, permitindo uma conversa clara com o cliente ([02:14:02](#02:14:02)).

* **Feedback Técnico e Próximos Passos (Golden Test)**: Off Digital relatou um feedback sobre falhas no motor atual, incluindo problemas na promoção de campos extraídos de metadados e uso incorreto de \*alias\* compostos. O próximo passo é realizar um \*hotfix\* nos dados para que o caso \*Laudis\* sirva como um \*golden test\*, utilizando a IA para extrair o padrão e replicá-lo, o que ajudará a consolidar um manual de manutenção no futuro ([02:14:52](#02:14:52)).

* **Importância do Visual Profissional do Produto**: As partes concordaram que, apesar do motor (compliance e certeza) ser o apelo principal, o aspecto visual deve estar alinhado para que o produto seja considerado profissional e agregue valor. Um visual "tosco" pode fazer com que a solução pareça caseira, desvalorizando o motor e afetando a percepção de preço do produto ([02:21:31](#02:21:31)).

* **Visão de Mercado e Barreira de Entrada da IA**: As partes reconheceram que o desenvolvimento atual lhes dá uma vantagem no mercado, onde poucos estão pensando com essa mentalidade ([02:22:32](#02:22:32)) ([02:24:04](#02:24:04)). Eles observaram que o investimento em tempo e dinheiro em ferramentas de IA (como Cloud e GPT) representa uma barreira de entrada, já que a maioria das pessoas não tem essa disponibilidade ou está apenas começando a interagir com as ferramentas ([02:25:03](#02:25:03)) ([02:26:58](#02:26:58)).

* **Tendências e Degradação de Modelos de IA**: Off Digital notou que os grandes modelos de IA (OpenCloud/GPT) estão constantemente sendo atualizados, com a versão 5.5 do GPT sendo ótima, mas com a tendência de degradação da performance em modelos mais antigos. Eles especularam que as empresas podem estar degradando modelos anteriores intencionalmente para valorizar o próximo lançamento ([02:28:51](#02:28:51)).

* **Perigo do Saudosismo Tecnológico**: Foi discutida a diferença entre se apegar a uma ferramenta (como N8N) e se apegar ao processo e à arquitetura, destacando que aqueles que não estão dispostos a abandonar o que dominam (saudosismo) para aprender o novo correm o risco de serem engolidos ([02:29:39](#02:29:39)). Eles enfatizaram a importância de se manter aberto a novas tecnologias (como \*Capivara\*, se surgir) ([02:31:23](#02:31:23)).

* **Configuração e Relação entre Modelos de IA (Hermes e OpenCloud)**: Off Digital descreveu como tem configurado e gerenciado seus assistentes de IA, usando o OpenCloud para assistente principal (com mais estrutura) e o Hermes para ser um CEO ou coordenador, mais minimalista e estratégico ([02:32:22](#02:32:22)). A ideia é que o OpenCloud faça o trabalho inicial e o Hermes valide e suba o que for aprovado ([02:33:32](#02:33:32)).

* **Criação de um Painel de Junção Autônomo (Cockpit)**: Off Digital está planejando desenvolver um painel de junção ("cockpit") que controlará o Hermes, OpenCloud, Cloud e Codex, permitindo que eles se comuniquem para realizar as tarefas de maneira autônoma ([02:33:32](#02:33:32)). O objetivo é reduzir a necessidade de intervenção direta, onde o papel principal será planejar e conferir a execução ([02:34:33](#02:34:33)).

* **Interface Futura de Gestão de IA**: O conceito futuro para o painel de junção é uma interface de "ação" semelhante a um grupo de WhatsApp, onde cada agente de IA (ou sessão do Cloud/Codex) será uma "pessoa" no grupo, permitindo a comunicação e a coordenação de tarefas de design, código e supervisão ([02:36:58](#02:36:58)). Embora o desenvolvimento leve tempo (cerca de dois meses), o objetivo é atingir um ponto mais autônomo na execução dos projetos ([02:38:04](#02:38:04)).

*Revise as anotações do Gemini para checar se estão corretas. [Confira dicas e saiba como o Gemini faz anotações](https://support.google.com/meet/answer/14754931)*

*Como está a qualidade de **destas observações?** [Responda a uma breve pesquisa](https://google.qualtrics.com/jfe/form/SV_9vK3UZEaIQKKE7A?confid=FpTTf5_UrofO7ZZCgADnDxIQOAIIigIgABgFCA&detailid=standard&screenshot=false) para nos dar seu feedback, incluindo o quanto as observações foram úteis para o que você precisa.*

# 📖 Transcrição

27 de abr. de 2026

## Reunião em 27 de abr. de 2026 às 14:43 GMT-03:00 \- Transcrição

### 00:00:00 {#00:00:00}

   
**Off Digital:** Ah. E daí,  
**Marcelo Costa:** Fala para mim.  
**Off Digital:** primo?  
**Marcelo Costa:** Bora nessa.  
**Off Digital:** Bora que bora. Deixa eu ver aqui que que que o bicho já rodou aqui. Importar, excluir, duplicar. Agora tá funcionando. Lá lá pá, depois eu paro para fazer aqui. Só te jogar para cima aqui. Yeah. Primo, vou vamos volotar de volta aqui mesmo. Eh, eu vou fazer depois então uma versão do zero pra gente testar.  
**Apresentação de Off Digital:** Er  
**Off Digital:** Pode ser até mais tarde quando eu terminar a reunião com o brother umas 8:30 ou amanhã cedo também porque demora um tempo, velho. Porque, tipo, tá vendo que aqui tá V2? Ah, não aparece aí, né?  
**Marcelo Costa:** Não.  
**Off Digital:** Mas a URL tá v.cercerfy.cllaudia.com.br. br. Aí o aquele o V1, aquele douradinho lá do jeito que tava antes, tá a um RL salva ainda, normal, porque eu não apaguei ele, porque, né? Eh, e aí eu vou criar um V3 para fazer esse teste sem nada na base, entendeu? Só que não não base não.  
**Marcelo Costa:** vai criar um su base novo também.  
   
 

### 00:02:48 {#00:02:48}

   
**Off Digital:** Eu só vou falar aqui no no V3 ele não precisa apontar os o nenhum dado de candidato, de matriz, de nada. Eu quero ele mantém a base lá.  
**Marcelo Costa:** pra gente criado importar inserido zero os os  
**Off Digital:** A base continua impacta, só que eu não quero que isso espele no produto,  
**Marcelo Costa:** Sim.  
**Off Digital:** entendeu?  
**Marcelo Costa:** Na frente.  
**Off Digital:** É. Aí, só que aí tem que apontar domínio,  
**Marcelo Costa:** Uhum.  
**Off Digital:** tem que ir lá no Gold configurar não sei das quantas lá no Versel, é as coisas tem que fazer manual, entendeu?  
**Marcelo Costa:** Tá.  
**Off Digital:** Então, porque senão fazia agora mesmo, mas vai demorar, demora uma horinha para fazer o rolê,  
**Marcelo Costa:** É,  
**Off Digital:** mais ou menos.  
**Marcelo Costa:** mas tá bom. Vamos usar do jeito que tá aí no vamos no populado aí que ainda até melhor para nós  
**Off Digital:** É, então aí então eu acho que aqui com que tem aqui,  
**Marcelo Costa:** aí.  
**Off Digital:** primo, agora é mais coisa cosmética de produto mesmo. Eh, por exemplo, essas coisas aqui de cobertura baixa, eh, tem que decidir exatamente qual que é, tipo, o que que vai definir aqui, entendeu? Se se a gente deixa se a gente deixa a cobertura baixa tá  
**Marcelo Costa:** Deu uma cortada aí, primo.  
   
 

### 00:04:00 {#00:04:00}

   
**Off Digital:** ouvindo? Oi, oi,  
**Marcelo Costa:** Oi.  
**Off Digital:** oi.  
**Marcelo Costa:** Voltou aí. Deu uma cortada.  
**Off Digital:** Internet tá,  
**Marcelo Costa:** Será que é a sua ou a minha?  
**Off Digital:** cara, essa minha tá com sinal cheio aqui.  
**Marcelo Costa:** É,  
**Off Digital:** Hum. Mas se cortar de novo,  
**Marcelo Costa:** a minha também tá dando uma cortada até na câmera aí.  
**Off Digital:** você fala aí a gente vê.  
**Marcelo Costa:** Deu, tá dando uma cortada, não sei se é o Agora voltou.  
**Off Digital:** Alô,  
**Marcelo Costa:** Voltou.  
**Off Digital:** alô.  
**Marcelo Costa:** Beleza, agora tá bom.  
**Off Digital:** alizou. Será?  
**Marcelo Costa:** Acho que sim.  
**Off Digital:** Beleza. Eh, então aqui, por exemplo, hoje a utilidade que eu arrumei para esses cards é esse lance do cobertura baixa, né? Mas isso aqui a gente pode mudar, pode ser alguma outra coisa. Mas assim, é o que eu falei, eu acho que pro inicial já tá  
**Marcelo Costa:** É, eu acho que até menos o o importante é a gente tá com o coração funcionando,  
**Off Digital:** muito  
**Marcelo Costa:** porque senão até dá deixa muita coisa, sabe? Aí vai a gente vai adicionando aos  
**Off Digital:** Exato. Exato.  
**Marcelo Costa:** poucos.  
**Off Digital:** Mas agora eu acho que é muito cosmético, tipo assim, cara, as vagas já estão aqui, ó.  
   
 

### 00:05:02 {#00:05:02}

   
**Off Digital:** Então, um, ó, já atualizou as a as empresas. Então, 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17\. Só esse Marcelo aqui que que foi aquela que a gente criou teste.  
**Marcelo Costa:** Acho que se bobear fui eu.  
**Off Digital:** Tá.  
**Marcelo Costa:** M.  
**Off Digital:** Deixa eu até pedir para ele aqui tirar a empresa Marcelo.  
**Marcelo Costa:** E aí você tá trazendo os dados de lá,  
**Off Digital:** Agora eu já trouxe, tá? As matrizes já estão aqui. Só não tem os documentos.  
**Marcelo Costa:** tá?  
**Off Digital:** eh dos candidatos,  
**Marcelo Costa:** Dos candidatos.  
**Off Digital:** porque a gente tá fazendo a a a limpeza para ele entrar no padrão que o sistema já exige, entendeu? E nós vamos validar no motor também.  
**Marcelo Costa:** Ah.  
**Off Digital:** Aí eu tô com a com a aba aberta aqui. Depois eu vou depois eu vou ver certinho aqui o que que ele o que que ele me dá e como é que a gente vai organizar isso e depois eu te explico como é que ficou organizado, como é que a gente mastigou isso, entendeu? Ainda não tá definido. Ele deu as ideias de tipo,  
**Marcelo Costa:** Tá.  
**Off Digital:** ó, podemos fazer assim, assim, assado, mas ah, tem que seguir aí coisa cosmética, tipo,  
   
 

### 00:06:35 {#00:06:35}

   
**Marcelo Costa:** Tá.  
**Off Digital:** botar o loguinho da empresa aqui, enfim. e essas coisas, sabe?  
**Marcelo Costa:** É.  
**Off Digital:** Mas cosmético,  
**Marcelo Costa:** E também não não depende a É isso  
**Off Digital:** né? Cosmético, por exemplo, eh tem vários candidatos que tão sem  
**Marcelo Costa:** aí.  
**Off Digital:** empresa, tá vendo? Então,  
**Marcelo Costa:** Tá.  
**Off Digital:** tem que ver, tem que ver isso no sistema, quem que é esse candidato, por que ele tá sem empresa, né?  
**Marcelo Costa:** É, talvez ele não, mas todos estão sem empresa ali, parece.  
**Off Digital:** Não tem a maioria, tá? Mas tem vários que que tão,  
**Marcelo Costa:** Não,  
**Off Digital:** ó, com empresa, ó, Hélix aqui, por exemplo, Posidônia, Shell. Então, tem que ver esses candidatos sem empresa,  
**Marcelo Costa:** eu ten que onde da onde ele tá puxando esse  
**Off Digital:** cara.  
**Marcelo Costa:** dado.  
**Off Digital:** Ele tá puxando do Supas da da primeira primeira leva que eu fiz lá.  
**Marcelo Costa:** É, então talvez eh é que aí tinha lá o supabase, ele tá com desde o início,  
**Off Digital:** Primeira,  
**Marcelo Costa:** talvez tenha isso. Teve uma época, eu pedi para mudar mesmo, ter um campo só paraa empresa e nós mudamos porque tava dando pau. Então pode ser nesse momento que que não tinha ainda,  
   
 

### 00:07:43 {#00:07:43}

   
**Off Digital:** sim. Então,  
**Marcelo Costa:** ele não tinha um campo específico paraa empresa,  
**Off Digital:** a a gente tá meio que nessa parte agora,  
**Marcelo Costa:** entendeu?  
**Off Digital:** na parte de tipo, tá, tem um monte de dado, tá puxando tudo, tá mandando tudo pro lugar certo, mas tem dado que não tá endereçado, né? Aí nós podemos, ó, por exemplo, vamos ver isso aqui agora.  
**Marcelo Costa:** Ah,  
**Off Digital:** Deixa eu aqui tá aparecendo minha tela aí para você.  
**Marcelo Costa:** tá lá.  
**Off Digital:** vai ficar muito ruim de ler, né? Mas eu vou pegar aqui, por exemplo, eu vou tirar um print, eu colo aqui e aí vou falar na aba triagem temos vários de dados. Ver se tá aberto o meu meu botão de voz aqui. Estão listados no Camba. que estão listados lá na nossa view de Camban,  
**Marcelo Costa:** O primo, um segundo.  
**Off Digital:** eh,  
**Marcelo Costa:** Deixa eu só ver um cara que chegou aqui.  
**Off Digital:** não estão interessados para nenhuma empresa e para nenhuma vaga. Eu quero que você faça um scan em todos os candidatos.  
**Marcelo Costa:** Não.  
**Off Digital:** São 52 candidatos ativos. Eu quero que você faça um escan nesses 52 candidatos e entenda porque eles não tão vinculados à vaga e porque eles não tão vinculados à empresa.  
   
 

### 00:09:44 {#00:09:44}

   
**Marcelo Costa:** Primo, um segundo que eu vou ver só uma parada aqui.  
**Off Digital:** Tranquilo.  
**Marcelo Costa:** Bora  
**Off Digital:** Eh, priminho, tem um negócio aí para melhorar sua visualização. Se você segurar o commody no Mac e e a e jogar a barra de rolagem, passar o passar o o segura o command, põe põe dois dedos na tua trackpad. e arrasta para cima.  
**Marcelo Costa:** Mas com o com o coiso para quê? que você tá falando para eu aumentar a minha  
**Off Digital:** Aham. Segura o comand,  
**Marcelo Costa:** tela?  
**Off Digital:** põe seus dois dedos, eh, os dois dedos principal em cima do trackpad e arrasta para cima os dois ao mesmo tempo.  
**Marcelo Costa:** É na segunda tela não rola. Vamos ver  
**Off Digital:** Não, não tem que ser na Não, na segunda tela rola também.  
**Marcelo Costa:** aqui.  
**Off Digital:** Ó, tá vendo aí na minha tela o zoom que vai dando?  
**Marcelo Costa:** Aham.  
**Off Digital:** É exatamente isso.  
**Marcelo Costa:** Mas isso você tá dando zoom dentro do do da sua tela do Zoom  
**Off Digital:** Pode, pode ser onde você quiser,  
**Marcelo Costa:** do Meet.  
**Off Digital:** velho. Po, em qualquer lugar da tela que  
**Marcelo Costa:** Deixa eu até ver uma parada aqui que eu tô vendo um mais um maisinho dentro do Zoom.  
**Off Digital:** você  
**Marcelo Costa:** Ah, aqui eu tenho maisinho dentro do Zoom, velho.  
   
 

### 00:13:19 {#00:13:19}

   
**Off Digital:** Como assim?  
**Marcelo Costa:** Acabei de ver aqui na tela do Zoom. Não tem a tela do Zoom onde você tá dividindo?  
**Off Digital:** No Google.  
**Marcelo Costa:** Do Google. É do Meeting, desculpa. Tem um maisinho. Acabei de ver. Tem um maisinho. Eu consigo aproximar e ir mexendo como se fosse a tela mesmo. Ele ele mexe exatamente aí. É o que ele faz.  
**Off Digital:** p\*\*\*\*, irado. Ótimo.  
**Marcelo Costa:** É.  
**Off Digital:** Mas faz isso para você aprender quando você precisar de dar zoom em qualquer coisa no Mac. Por exemplo, você tá lendo um um site que ele tá muito distante, você segura o comand, o comand que tem do lado da barra de espaço, comand esquerdo, o comand  
**Marcelo Costa:** Sei.  
**Off Digital:** esquerdo,  
**Marcelo Costa:** Comando esquerdo e vai com os dois dedos para cima, né?  
**Off Digital:** né?  
**Marcelo Costa:** É que eu é que eu na verdade eu tô ó o que eu uso aqui, ó.  
**Off Digital:** Sim, mas o teu, mas o teu, é, o teu computador é um laptop, não é?  
**Marcelo Costa:** É,  
**Off Digital:** Clica aí no teclado do Mac mesmo. Segura o command lá no teclado do Mac e arrasta os dois dedos no  
**Marcelo Costa:** eu segurei.  
**Off Digital:** track pad.  
   
 

### 00:14:20

   
**Marcelo Costa:** Então, tô tentando.  
**Off Digital:** Não,  
**Marcelo Costa:** Ele não tá dando esse aqui.  
**Off Digital:** você tem que continuar segurando. Você fica segurando e arrasta.  
**Marcelo Costa:** Sim, eu tô fazendo.  
**Off Digital:** Ele não dá zoom.  
**Marcelo Costa:** Ele não tá dando zoom. Água. Ele dá zoom assim de abrir, não para cima. Quando eu abro, ele abre tipo um, ele funciona quando eu deixa eu ver se eu preciso do comand. Ah, não preciso nem do comand, velho. Só de eu abrir assim, ele abre igual o celular. O seu não faz não.  
**Off Digital:** Não, velho.  
**Marcelo Costa:** Ó,  
**Off Digital:** O meu,  
**Marcelo Costa:** tô na tela.  
**Off Digital:** o meu é no comand. O, ó, tá vendo a setinha como é que ficou aí? O meu dá zoom tanto para fora quanto para dentro.  
**Marcelo Costa:** Aham.  
**Off Digital:** No, eu seguro o comand e vou arrastando com os dois dedos. Esses dois dedos aqui,  
**Marcelo Costa:** Certo. Pera, agora para o seu aí.  
**Off Digital:** ó.  
**Marcelo Costa:** Deixa eu ver um negócio. É, cara, eu não sei se é porque tá no dentro do Zoom. Deixa eu ver em outra tela aqui. Qualquer tela você faz  
**Off Digital:** Qualquer dela, velho.  
   
 

### 00:15:22 {#00:15:22}

   
**Marcelo Costa:** isso.  
**Off Digital:** Tira do full screen. Tem não pode estar no full screen  
**Marcelo Costa:** Não, não tá no full, por exemplo. Tô numa guia do do  
**Off Digital:** do finder,  
**Marcelo Costa:** coiso.  
**Off Digital:** qualquer parada. Mas não pode estar em full screen. Ele tem que tá tipo o meu que tem várias telas, um do lado da outra assim.  
**Marcelo Costa:** Sim. Então, ó, agora o meu funciona, mas não correndo os dedos assim. Ele funciona dando zoom mesmo de de celular, sabe?  
**Off Digital:** E ele abre.  
**Marcelo Costa:** Ele abre, mas ele nem preciso tá no comand. Tu tenta só no só fazendo abrindo.  
**Off Digital:** Não, o meu não, o meu não vai.  
**Marcelo Costa:** Ah, então deve ser alguma configuração, né,  
**Off Digital:** Ah,  
**Marcelo Costa:** velho?  
**Off Digital:** mas em pé funciona,  
**Marcelo Costa:** Funciona até melhor que o meu é sem o comy,  
**Off Digital:** né?  
**Marcelo Costa:** velho. Já vi aqui que ele vai sem o comy, mas ficou bom, porque aí você não depende de pedir pro outro aumentar o  
**Off Digital:** a pessoa, vocês conseguem se virar no zoom,  
**Marcelo Costa:** negócio.  
**Off Digital:** entendeu? por exemplo, dá zoom aí. Vê se você consegue dar zoom para ler o que tá escrito aqui,  
**Marcelo Costa:** Consigo.  
   
 

### 00:16:18 {#00:16:18}

   
**Off Digital:** por exemplo.  
**Marcelo Costa:** Agora sim. Agora dou o zoom e eu não preciso ficar dependendo de você.  
**Off Digital:** Exatamente.  
**Marcelo Costa:** Oh.  
**Off Digital:** Isso aqui eu eu fiz uma lista de coisa que eu queria fazer ontem. Isso aqui tava na lista. Quero aplicar esses dois propostes. Beleza. Corrigir matriz. Vamos ver. implementado e funcionando. Remover a empresa Marcelo. Ai, cadê quantidados  
**Marcelo Costa:** Primo, você sabe uma i\*\*\*\*\*\*\*  
**Off Digital:** aqui?  
**Marcelo Costa:** que assim com certeza tá previsto aí, mas eu lembrei aqui que é foi um negócio que eu barrei, que eu que eu tive que mexer lá, que era o seguinte, ele ele fazia toda a validação, beleza? Ele só não validava o nome do cara, porque o nome do candidato, concorda que eu tô, eu crio o candidato, eu posso pôr seu nome inteiro, posso pôr seu nome pela metade e aí depois o documento ele tem que tem  
**Off Digital:** Ага.  
**Marcelo Costa:** que ter esse cheque. Senão eu pego lá, eu tô criando Marcelo, mas subiu um documento do Marco e ele vai falar: "Ó, o documento tá OK, validado, tal". É um cheque simples,  
**Off Digital:** Ага.  
**Marcelo Costa:** mas que eu tive que falar lá do outro lado.  
   
 

### 00:17:41 {#00:17:41}

   
**Marcelo Costa:** Eu não sei aí se ele já tá previsto,  
**Off Digital:** Entendi, entendi.  
**Marcelo Costa:** mas eu lembrei para ver se as  
**Off Digital:** É isso, a gente vai conseguir ver fácil no teste. p\*\*\*\*, eh, pra gente não perder porque é muita coisa,  
**Marcelo Costa:** eh  
**Off Digital:** cara. Você mandando, vai mandando no Whats isso que você me falou. digita aí uma linha, fala, cara, eh, garantir,  
**Marcelo Costa:** ele  
**Off Digital:** garantir que o nome eh do candidato esteja atrelado com o documento de na validação.  
**Marcelo Costa:** eu já eu já botei esse eu já tá na minha listinha aqui. Vou te mandar de vou aproveitar. Tem um outro que quer já falar ou quer  
**Off Digital:** Vamos,  
**Marcelo Costa:** ir,  
**Off Digital:** me manda tudo no Whats, a gente já vai fazendo agora, eu acho. Já vai, já vamos mexendo.  
**Marcelo Costa:** tá? Um outro ponto é modalidade. Eu vi que você tem uma nomenclatura modalidade. Ele entende modalidade, por exemplo, numa NR, como ele não separa lá em camadas, né, que você falou. Deixa eu, deixa eu achar aqui o texto que você me mandou, ó.  
**Off Digital:** Tem aqui, Aqui, ó, tem aqui a classifica aqui, ó. Deixa eu compartilhar com você  
**Marcelo Costa:** Ó, modalidade é o curso ou exigência específico dentro da NR.  
   
 

### 00:18:54 {#00:18:54}

   
**Off Digital:** aqui.  
**Marcelo Costa:** Então a modalidade ele tem lá se ele é um trabalhador, se ele é um trabalhador de viga, se ele é um supervisor, se ele é um resgate. Isso para ele é pro sistema modalidade,  
**Off Digital:** Ah, não, não,  
**Marcelo Costa:** certo?  
**Off Digital:** não necessariamente. É só quando o documento explicita  
**Marcelo Costa:** É, então ele dividiu em camadas,  
**Off Digital:** isso.  
**Marcelo Costa:** né? Então eu tenho lá, por exemplo, modalidade, é isso. Eu tenho o parâmetro da modalidade. Então aqui  
**Off Digital:** É, ó, por exemplo, só para você entender aqui,  
**Marcelo Costa:** entra,  
**Off Digital:** ó, modalidade, por exemplo, dá o zoom você aí mesmo.  
**Marcelo Costa:** tá? Pode deixar.  
**Off Digital:** Aqui modalidade. Você vê que ele tá aqui, ó. Documento 55 horas, CAP eventual, CAP inicial,  
**Marcelo Costa:** Uhum.  
**Off Digital:** EAD semipresencial, CIPA, Gen, 12 meses, Beas, 20 hor 40 meses. Ele puxa a modalidade do próprio documento, conforme o documento explicita que aquilo é a modalidade do documento, entendeu?  
**Marcelo Costa:** Certo. Certo. Então ele tá buscando documento, né?  
**Off Digital:** o  
**Marcelo Costa:** Aí, só que aí quando eu vou quando eu vou colocar a matriz,  
   
 

### 00:20:15

   
**Off Digital:** documento.  
**Marcelo Costa:** aí você vai definir se você quer qual modalidade você quer, certo?  
**Off Digital:** Não, porque você é que você tá enxergando modalidade,  
**Marcelo Costa:** é que essa como como o cara faz a  
**Off Digital:** por exemplo,  
**Marcelo Costa:** modalidade, essa que é a diferença.  
**Off Digital:** não é?  
**Marcelo Costa:** Como o cara faz  
**Off Digital:** É, não. Modalidade para você seria, por exemplo,  
**Marcelo Costa:** dele?  
**Off Digital:** NR3 e a modalidade seria 6 horas eh de de de salvamento. 6 horas seria na sua cabeça seria a modalidade. E aqui não não é essa lógica que ele que ele tá aplicando. Ele tá lendo dentro do documento o que que o documento eh mostra como dentro do documento o que é modalidade, entendeu? Aqui o que você vê hoje como modalidade no nosso sistema,  
**Marcelo Costa:** Tá.  
**Off Digital:** ele é variação. Então ele é só uma variação da NR. Ele não é uma  
**Marcelo Costa:** Beleza?  
**Off Digital:** modalidade  
**Marcelo Costa:** Então ele tá definido, então ele isso tá definido dentro, ele tá trazendo o dado real do documento, certo?  
**Apresentação de Off Digital:** Er  
**Off Digital:** para do documento,  
**Marcelo Costa:** Que ele encontra lá como modalidade.  
**Off Digital:** porque ele encontra e classifica como modalidade depois de ler o documento.  
**Marcelo Costa:** Beleza? Aí tem uma segunda  
   
 

### 00:21:25

   
**Off Digital:** Tanto é que tem documento aqui que é uma NR que você vê aqui,  
**Marcelo Costa:** modalidade.  
**Off Digital:** ó, que a modalidade ficou documento, porque não tem nada que explicita como modalidade. E é uma NR. E aqui é outra NR. Mas já tem aqui, ó, hiperb, porque ela explicita,  
**Marcelo Costa:** Tá.  
**Off Digital:** entendeu?  
**Marcelo Costa:** E essa e essa eh vamos dizer essa modalidade que você tá mostrando aí, ela não tem muito assim, não é um negócio de relevância que o cara bate o olho, tá? porque é um negócio bem diferente.  
**Off Digital:** No,  
**Marcelo Costa:** Não,  
**Off Digital:** no,  
**Marcelo Costa:** não, ele não precisa desse dessa informação. A modalidade que eu tinha lá no Certify é outro,  
**Off Digital:** no.  
**Marcelo Costa:** eu tô é outro é outro outra modalidade que eu quis dizer que é o quê? É como o cara fez aquele certificado. Então existem, por exemplo, as empresas de certificado que ela tem curso EAD.  
**Off Digital:** Aha.  
**Marcelo Costa:** Então o cara fez modalidade AAD, foi  
**Off Digital:** Não, isso continua. Ó, por exemplo, tá vendo aqui,  
**Marcelo Costa:** totalmente  
**Off Digital:** ó? Você tem EAD semipresencial, só que a própria NR já fala NR01 é AD semipresencial.  
**Marcelo Costa:** então é porque então isso e essa regra ela já existe.  
   
 

### 00:22:34 {#00:22:34}

   
**Marcelo Costa:** O que pode ser EAD, o que que não pode ser AD.  
**Off Digital:** Exatamente.  
**Marcelo Costa:** Então, então antes eu tinha isso separado porque só que isso me travava porque assim,  
**Off Digital:** Exatamente.  
**Marcelo Costa:** a empresa não quer saber, ela quer se o cara tem NR10, se foi presencial, semipresencial. Eu quando eu construí,  
**Off Digital:** Aham.  
**Marcelo Costa:** eu achei que tinha essa exigência, mas não tem. Então, porque a norma diz,  
**Off Digital:** Sim.  
**Marcelo Costa:** a norma fala pode ser AD ou não pode ou às vezes é sem metade um,  
**Off Digital:** Não, o que mudou pra gente aqui é que a modalidade passou a ser só uma informação e o que era modalidade para  
**Marcelo Costa:** metade outro.  
**Off Digital:** você virou variação, ou seja, variação de NR,  
**Marcelo Costa:** Tá.  
**Off Digital:** variação de óbitto, variação de SCW, não é mais modalidade,  
**Marcelo Costa:** E você acha que ela Bom,  
**Off Digital:** entendeu?  
**Marcelo Costa:** podemos deixar completo, não muda nada. Ter ou não ter não muda, né? Então vamos manter  
**Off Digital:** Não. E às vezes é até E às vezes são até informações pertinentes,  
**Marcelo Costa:** aí.  
**Off Digital:** entendeu? Tipo, por exemplo,  
**Marcelo Costa:** Sim.  
**Off Digital:** aqui tá dizendo que é 12 meses.  
   
 

### 00:23:29 {#00:23:29}

   
**Off Digital:** Então é legal você bater o olho e saber que aqui tá dizendo que é 12 meses, porque não tem essa informação. Aqui fala que é 8 horas, né? Aqui fala que é grau de risco um,  
**Marcelo Costa:** Sim,  
**Off Digital:** mas aqui trouxe um detalhe a mais que é 12 meses,  
**Marcelo Costa:** 12 meses deve ser o quê? Será, né?  
**Off Digital:** talvez 12 meses.  
**Marcelo Costa:** Essa NR5 CIP eu nunca vi. Eu não sei se o cara é um treinamento.  
**Off Digital:** De repente 12 meses é o tempo que demora para tirar ela  
**Marcelo Costa:** Pode ser. Agora esses dados não é não é trazido de lá já.  
**Off Digital:** de lá da onde?  
**Marcelo Costa:** Essas informações são Ah, não. Aí é a nossa base.  
**Off Digital:** Aqui a nossa base tá trazendo do tá trazendo da norma  
**Marcelo Costa:** Ah, p\*\*\*\*, eu tô achando sem documentos. Beleza, beleza. Não,  
**Off Digital:** verídica,  
**Marcelo Costa:** p\*\*\*, acabou. Agora entendi, primo. Beleza.  
**Off Digital:** entendeu?  
**Marcelo Costa:** Ele já tá trazendo o que a norma diz sobre isso aqui.  
**Off Digital:** Irmão, não tem não.  
**Marcelo Costa:** Ele é semipresencial.  
**Off Digital:** Isso isso aqui é indiscutível, não tem o que você falar,  
   
 

### 00:24:24 {#00:24:24}

   
**Marcelo Costa:** Não,  
**Off Digital:** entendeu? É tipo assim, cara,  
**Marcelo Costa:** agora não,  
**Off Digital:** da onde você tá consultando isso, cara? Clica aí para você ver da onde eu tô consultando.  
**Marcelo Costa:** não, acabou.  
**Off Digital:** Da portaria ou tá aqui?  
**Marcelo Costa:** É isso aí. Isso vem da regra,  
**Off Digital:** Aqui na portaria. Entendeu? Tá aqui que é o link oficial.  
**Marcelo Costa:** tá?  
**Off Digital:** Você não você não confia aqui no meu PDF, beleza? Então clica aqui, ó.  
**Marcelo Costa:** Vem no gov, que é onde é a  
**Off Digital:** Link oficial aqui, ó. Pronto.  
**Marcelo Costa:** base.  
**Off Digital:** Tá aqui, ó. Fonte, beleza? Golv. BR trabalho/conselhos tá  
**Marcelo Costa:** Perfeito.  
**Apresentação de Off Digital:** Er  
**Marcelo Costa:** Ótimo.  
**Off Digital:** aqui.  
**Marcelo Costa:** É que esse, p\*\*\*\*, agora matou na na fonte. Pronto. Que essa era a dúvida, eh,  
**Off Digital:** É porque,  
**Marcelo Costa:** da onde tava vindo esse dado, como é que a  
**Off Digital:** priminho, depois da nossa última reunião que você falou da fonte, da fonte na verdade e tal,  
**Marcelo Costa:** genteava  
**Off Digital:** eu falei: "Cara, esse é o único jeito, porque nós vamos ficar entrando em detalhe, porque você vai falar: "Velho, p\*\*\*, isso aqui da forma que eu faço, eu vou falar: "Cara, mas isso aqui da forma que a gente tá fazendo".  
   
 

### 00:25:11 {#00:25:11}

   
**Off Digital:** Então, a a a forma é essa.  
**Marcelo Costa:** que é a base, velho?  
**Off Digital:** É aqui,  
**Marcelo Costa:** Da onde vem?  
**Off Digital:** aqui é o embasamento, acabou, entendeu?  
**Marcelo Costa:** Ótimo,  
**Off Digital:** É isso. Então,  
**Marcelo Costa:** ó.  
**Off Digital:** beleza. Então, só para você entender, o que era modalidade virou  
**Marcelo Costa:** Tá, deixa eu botar aqui para você umas coisa para não esquecer que é o nome para modalidade.  
**Off Digital:** variação.  
**Marcelo Costa:** OK. Vamos falar de um outro ponto aqui que eu lembrei também, ó. Modalidade. Nós entendemos renomear os documentos. Você quer que eu te mando ou isso aqui? Você já sabe? Já sabe, né?  
**Off Digital:** Que que é renomear os documentos  
**Marcelo Costa:** Renomear os documentos que você falou que ia ver depois.  
**Off Digital:** mesmo?  
**Marcelo Costa:** Isso aí é bom botar aí para ficar na para você lembrar,  
**Off Digital:** Ah,  
**Marcelo Costa:** né?  
**Off Digital:** nomenclatura.  
**Marcelo Costa:** É para ele pegar depois os documentos e renomear conforme ele lê, né?  
**Off Digital:** Sim, sim. Eh, eh,  
**Marcelo Costa:** Eu vou  
**Off Digital:** eh, criar criar nomenclatura padrão de renome de de documentos,  
**Marcelo Costa:** pôr  
**Off Digital:** matrizes, candidatos, tudo tem que tá no padrão.  
   
 

### 00:26:12 {#00:26:12}

   
**Off Digital:** Isso eu quis deixar por último, velho, porque ele tem que porque é legal ver o sistema inteiro para ele entender como como a gente cria essa nomenclatura,  
**Marcelo Costa:** e como ele vai padronizar para ficar mais fácil visualização e numa lógica,  
**Off Digital:** entendeu,  
**Marcelo Costa:** porque senão você cria um negócio  
**Off Digital:** igual eu tô criando do brother aqui, ó. o o projeto do brother que eu te falei que tá ficando irado. Eh, deixa eu ver se tem como te mostrar aqui. Vou compartilhar o codex com você. Pera aí. Onde que é o browser mesmo? Aqui, primo, redesenhei tudas, ó lá. Tá vendo as tela azulzinha aí de novo.  
**Marcelo Costa:** Aham.  
**Off Digital:** Aí desenhei todas.  
**Marcelo Costa:** você fez no design,  
**Off Digital:** Que isso?  
**Marcelo Costa:** ele tá pica, né, velho?  
**Off Digital:** Tá f\*\*\*,  
**Marcelo Costa:** Bom,  
**Off Digital:** mano.  
**Marcelo Costa:** mas consome, né, velho?  
**Off Digital:** Não, consome para c\*\*\*\*\*\*.  
**Marcelo Costa:** E não dá nem  
**Off Digital:** Isso não, isso é que eu já dei para ele tudo pronto,  
**Marcelo Costa:** chance.  
**Off Digital:** né? Tipo, ele só melhorou as telas porque já tava tudo feito. Eh, tudo as abas, tudo a lógica,  
**Marcelo Costa:** É, não, não dá para não dá para dar essa missão para ele,  
   
 

### 00:28:22

   
**Off Digital:** todos saí na fonte,  
**Marcelo Costa:** né?  
**Off Digital:** eh, se ele não ia tirar do zero, entendeu? Tipo em cima. Agora deixa eu ver aqui. Subi server. Não, bicho. Rapidão. É aqui, ó. Quanto ele sobe, deixou mudanças principais implementado e funcionando. Boa. Eu mudei esses botões aqui, tá vendo que eles estão preto? Eu botei para ficar transparente agora ao para ficar mais da hora.  
**Marcelo Costa:** А  
**Off Digital:** Eh, val browser ainda não fechado. Fiz o deploy. Deploy ver. Subiu. Vou subir. Perfeito. Serve subiu. Ó o painelzinho que eu fiz aqui do brother aqui.  
**Marcelo Costa:** Esse é o quê?  
**Off Digital:** Esse é o do brother do estoque dos eventos que eu te falei.  
**Marcelo Costa:** Ah\!  
**Off Digital:** É a é a gestão do estoque dele. Ele tem eh ele tem 600 e poucos itens.  
**Marcelo Costa:** daquele que tem os Qode lá  
**Off Digital:** Aí aqui já calcula qual que é o patrimônio,  
**Marcelo Costa:** parado.  
**Off Digital:** com os eventos dele aqui, ó. Tá vendo? próximos eventos. aqui o os RFID, que é as tagzinhas que ele vai ligar no nos equipamentos, tipo aqui ele vai ligar aquelas tagzinhas de metal em cada equipamento e aí quando quando ele tira  
   
 

### 00:30:49

   
**Marcelo Costa:** Tá ligado?  
**Off Digital:** do estoque já dá baixa automático, sem ele fazer nada, só pelo movimento. O RF já capita que saiu do estoque depois que sai de tantos metros de distância e ele já dá baixa. Muito louco o bagulho. Aí aqui, ó, no catálogo dele, se liga. Eu criei aqui, eh, ele tem aqui os itens disponíveis, os itens em campo, os itens em manutenção, o que que tá crítico na condição, se já tá f\*\*\*\*\*, se tá novo, se tá tá zoado, eh, o que tá regular, o que tá ótimo. E aqui, ó, criou um código de nomenclaturas, tá vendo? Eh, M, ó, MMDU 004\.  
**Marcelo Costa:** Aham.  
**Off Digital:** Então, quer dizer que é um equipamento de iluminação, ó. Tá vendo? Todos de iluminação fica ILU.  
**Marcelo Costa:** Tá.  
**Off Digital:** Então, 001 MD e Lu 003\.  
**Marcelo Costa:** Bate o olho já sabe o que é, né?  
**Off Digital:** Aqui eu botei só a iluminação. Aqui eu ponho áudio. Aí ele fica mmd audi 001 002 e todos os equipamentos. Então você tá criando um código de catálogo interno, ó. Estrutura eh EST praticável,  
   
 

### 00:31:57

   
**Marcelo Costa:** E até depois que o cara,  
**Off Digital:** eh estrutura geral.  
**Marcelo Costa:** pô, o cara vai montar o pedido lá do que eu quero, o cara vai já ticando lá no site dele.  
**Off Digital:** Exato.  
**Marcelo Costa:** Daqui a pouco  
**Off Digital:** Pô, o que que tá na rua, cara? Tá o o aud 004005 007,  
**Marcelo Costa:** já  
**Off Digital:** entendeu? Mandei para aquele evento e tal. Então é mesmo esquema que eu quero fazer de catálogo com a gente. Então, p\*\*\*\*, NR001, tal, tal, tal. Então, tipo, tudo tem um catálogo, entendeu?  
**Marcelo Costa:** é que é o que as empresas hoje, por exemplo, você for lá na na Maesco, na Reli que são certificadores, elas têm o código dela para cada um dos itens.  
**Off Digital:** Exato. Código interno. Código interno do nosso compliance.  
**Marcelo Costa:** Eh,  
**Off Digital:** Então aqui dentro do nosso motor,  
**Marcelo Costa:** sim.  
**Off Digital:** aqui dentro do nosso software, a gente tem um catálogo nosso interno.  
**Marcelo Costa:** Que ele tem um depara na rilá. O nosso 001 é o 203 dele,  
**Off Digital:** Exatamente.  
**Marcelo Costa:** né? Para cá. Então a gente sabe,  
**Off Digital:** Então,  
**Marcelo Costa:** ah, para uma e para outra é esse.  
   
 

### 00:32:50

   
**Marcelo Costa:** A  
**Off Digital:** então não importa a organização do cara aqui para dentro de casa.  
**Marcelo Costa:** gente  
**Off Digital:** O nosso 001 é isso, o 002 é isso. E a gente vai se referenciar em cima disso aí.  
**Marcelo Costa:** vê que os os padrãozinhos,  
**Off Digital:** Pô,  
**Marcelo Costa:** né, são é mais ou menos próximo assim à forma de desenvolver, de pensar,  
**Off Digital:** é exatamente. E aí, p\*\*\*\*, velho,  
**Marcelo Costa:** né?  
**Off Digital:** olha aí. Você clica aqui, ó, já aparece o Qcode pro cara, mano. O bagulho tá ficando animal, tá ligado? Tipo,  
**Marcelo Costa:** É da hora, né, velho?  
**Off Digital:** tem tem folha grande. É, não, você aí você vai pegando a manha, tá ligado?  
**Marcelo Costa:** Hello.  
**Off Digital:** Aí aqui, ó, você passa o darkzinho também, tá treta com os negócios tipo de evento, as luzinhas, sabe? Parece aquelas luz de evento aqui, ó. Roxo,  
**Marcelo Costa:** É de ficou da hora,  
**Off Digital:** azul. Então,  
**Marcelo Costa:** né?  
**Off Digital:** simplesinho assim, nada demais, mas tipo o bagulho filé,  
**Marcelo Costa:** Não, mas velho,  
**Off Digital:** entendeu?  
**Marcelo Costa:** vai trazer uma inteligência pro cara do negócio  
   
 

### 00:33:37

   
**Off Digital:** É, o bagulho é filé, entendeu?  
**Marcelo Costa:** dele,  
**Off Digital:** Filé simples, mas fácil de de usar, fácil de mastigar. Sim.  
**Marcelo Costa:** não. E o cara vai depois olhar e entender, p\*\*\*\*,  
**Off Digital:** Tipo,  
**Marcelo Costa:** velho, tô perdendo dinheiro porque tá ficando um negócio na rua. Há quanto tempo fica na rua essa p\*\*\*\* aqui, velho. O cara vai,  
**Off Digital:** não, mano. O cara tem,  
**Marcelo Costa:** não busca.  
**Off Digital:** velho, 1 milhão. É porque tem coisa que não entrou. O cara tem 1 milhão de se o cara tá que que tá rolando, entendeu? Eu falei: "Velho, pelo amor de Deus, velho." E o cara faz uns eventos grande, mano. Tava fazendo um negócio agora lá pro Shark Tank. Eh, enfim.  
**Marcelo Costa:** João Angelique, depois você mostrar isso para ele, ele vai querer certeza.  
**Off Digital:** Não. E é é o que eu tô falando, eu faço direitinho porque tudo depois vira produto. Isso aqui eu já posso depois pegar e falar:  
**Marcelo Costa:** Sim,  
**Off Digital:** "Velho, eu tenho um produto de controle de de estoque.  
**Marcelo Costa:** de  
**Off Digital:** Não é só o do não é só o do cara,  
   
 

### 00:34:32 {#00:34:32}

   
**Marcelo Costa:** qualquer  
**Off Digital:** entendeu? Então eu faço bem, eu faço bem feitinho porque eu já penso nisso, velho. Depois vai virar um produto.  
**Marcelo Costa:** já vira outra,  
**Off Digital:** É lógico.  
**Marcelo Costa:** né?  
**Off Digital:** Aí os caras só vai ter o login dele lá no no produto e boa. Entendeu? Tem um que ele eles pagam que chama rang. É igual o Hackman. Tem o tem o rangm que é o para que é o sistema que os cara usa que eu também peguei de  
**Marcelo Costa:** Sei.  
**Off Digital:** referência. É mesmo esquema,  
**Marcelo Costa:** Eh,  
**Off Digital:** entendeu?  
**Marcelo Costa:** o cara pega o green e aí vai acabar. Esses caras tão assim mais ou menos, né?  
**Off Digital:** Aí, priminho, ficou muito mais chique,  
**Marcelo Costa:** Mas,  
**Off Digital:** sabia? Vou jogar de volta pro pro nosso  
**Marcelo Costa:** ó, voltando aqui,  
**Off Digital:** aqui.  
**Marcelo Costa:** tem uma parada que a gente, pra gente pensar que hoje o eh o outro trata, mas meio grosseiramente, vamos dizer assim, que é o seguinte. Existem alguns treinamentos da RIX, por exemplo, que é um treinamento interno deles,  
**Off Digital:** Mhm.  
**Marcelo Costa:** tá? E ela exige tal que o que o que a MDE controle esses treinamentos também, só que isso é muito particular, entendeu?  
   
 

### 00:35:47

   
**Off Digital:** Tá.  
**Marcelo Costa:** Porque não tem uma regra, né? Cada cliente, por exemplo, a Hélix tem os treinamentos internos deles. Só que aí o que que eu que eu construí é o seguinte,  
**Off Digital:** Uhum.  
**Marcelo Costa:** eu botava lá como outros, tá? ou cliente,  
**Off Digital:** Uhum.  
**Marcelo Costa:** o quando eu cadastrava um negócio pro cliente e eu coloco um de até mostrar, vou abrir um para você ver  
**Off Digital:** Abre  
**Marcelo Costa:** aqui.  
**Off Digital:** aí.  
**Marcelo Costa:** Tá vendo aí, ó? Então tenho aqui cliente treinamento de fogo de linha de fogo. Aí quando eu venho no,  
**Off Digital:** Tá.  
**Marcelo Costa:** você tá vendo o pop-up aí? Então ó, é da Hélix.  
**Off Digital:** Tô  
**Marcelo Costa:** Ela mesmo treina o cara internamente lá. E às vezes até antes do cara entrar ele tem que passar por esses, mas esses aqui são internos da Hélix, tá?  
**Off Digital:** tá.  
**Marcelo Costa:** Então ela criou, você vê que tem uma tabela aqui que é esse Q7.000 aqui. É tipo a tabela de treinamentos deles internos.  
**Off Digital:** Угу.  
**Marcelo Costa:** Então, ó, treinamento linha de fogo, tá? Tem um certificadinho e tal, só que isso aqui é interno dela. Ela tem, ó, até quem tá lá, MDE 500 e tanto, que é o número, acho que talvez do candidato, não sei.  
   
 

### 00:37:06 {#00:37:06}

   
**Marcelo Costa:** Só que isso aqui é um pouco solto. E ó, tá vendo, ó? Eles até fizeram EAD, ó. Foi através de um EAD do Drake, ó. Nem sabia que o Drake tinha um EAD, ó. Então, tem um treinamento dentro do Drake lá de EAD.  
**Off Digital:** Tá.  
**Marcelo Costa:** que o cara deve botar as aulinhas, o cara entra lá, faz as aulinhas, OK? Deve gerar esse certificado aqui. Então, o que que acontece? Só que isso aqui não é um padrão, certo? A Hélix tem um, a Petrobras tem outro, o outro tem outro nomenclatura diferente e outro,  
**Off Digital:** Ah.  
**Marcelo Costa:** então não é norma, não é nada, mas é interno do cliente, eles controlam também. Aqui, como eu botei em outros lá, na maioria das vezes, como eu botei exatamente o nome no negócio, ó,  
**Off Digital:** Угу.  
**Marcelo Costa:** treinamento de linha de fogo, pense segurança, pense processo, treinamento, teste de gás. Aqui às vezes dá pau porque eu tenho um, o cliente tem um interno deles, mas o opito também tem um treinamento de gás. Então, normalmente ele até lê o Opito. Vamos ver o que deu aqui, ó. Aí, ó.  
   
 

### 00:38:16

   
**Off Digital:** Угу.  
**Marcelo Costa:** Ele pegou um opito e jogou  
**Off Digital:** Uhum.  
**Marcelo Costa:** lá que tá errado,  
**Off Digital:** E linkou com isso que você criou. Ele linkou com o  
**Marcelo Costa:** entendeu?  
**Off Digital:** pit.  
**Marcelo Costa:** Porque o esse é interno do cliente, não deveria ser o Pit. Ele deu um confere aqui, ó. Entendeu?  
**Off Digital:** Sim.  
**Marcelo Costa:** Então eu não sei isso como não. Eu não sei como que a gente pode eh tratar,  
**Off Digital:** Ah,  
**Marcelo Costa:** porque é muito solto isso, né?  
**Off Digital:** como é que chega, como é que chega para você? Quem que tá fazendo? É o Marcelo? É você que tá subindo?  
**Marcelo Costa:** O quê?  
**Off Digital:** E esses treinamentos por fora, como é que chega? Chega o certificado,  
**Marcelo Costa:** Eu não tô,  
**Off Digital:** chega na matriz.  
**Marcelo Costa:** eu não tô subindo. A matriz já vem exigindo para ele e o candidato vai  
**Off Digital:** Aham.  
**Marcelo Costa:** fazendo. Só que eh eh vamos lá. O candidato antes dele ser contratado, ó, cara, beleza, nós vamos, a Hélix falou, vou contratar o cara, tá? Vou contratar o Marco. Agora o Marco precisa fazer esses treinamentos aqui que é interno nosso, mas ele vai lá no Drake lá, pelo que eu vi, é no Drake, vai lá e vai fazer o candidato, manda para ele, caminho normal,  
   
 

### 00:39:21 {#00:39:21}

   
**Off Digital:** Tá,  
**Marcelo Costa:** manda para ele, ele valida e aí manda pro cliente, ó, terminou, tá OK com os treinamentos, inclusive os seus,  
**Off Digital:** tá. Isso então é,  
**Marcelo Costa:** entendeu?  
**Off Digital:** isso então é depois de certificados, antes de documento pessoal.  
**Marcelo Costa:** É, ele tá dentro dos certificados. É mais uma leva de certificado, só que em vez de ser um STCW, em vez de ser um opito, é o é do cliente, exigência do  
**Off Digital:** Tá? O que a gente pode faz,  
**Marcelo Costa:** cliente.  
**Off Digital:** qual que seria a forma disso ficar amarrado da forma legal? A gente vai ter que criar de cliente para cliente uma aba de exigências do cliente,  
**Marcelo Costa:** Ele tem que mandar um pra gente,  
**Off Digital:** uma modalidade de ele tem que mandar pra gente a  
**Marcelo Costa:** pra gente entender o que é.  
**Off Digital:** a a base. Então, toda vez que tiver um cliente novo, exigências do cliente, ele vai ter que solicitar essa parte, entendeu? Eu acho que é a  
**Marcelo Costa:** É isso aí, porque senão de novo a gente abre brecha pro cara botar o que quer e falar que é o sistema que tá dando pau. Fala: "Não é, velho, tem que ser. O compliance é esse.  
**Off Digital:** forma  
**Marcelo Costa:** Você me manda, então o cliente manda pra gente um um esboço.  
   
 

### 00:40:30

   
**Marcelo Costa:** Qual que é? Me manda quatro aí do esses quatro. Me manda os quatro. Eu vou ver aqui, vou botar internamente falar para relix. ela tem esses treinamentos ou até se ela tiver uma base maior, fala: "Rélix, a gente trabalha com vocês aí, qual é os treinamentos que vocês têm? Me manda base, me manda toda a informação pra gente imputar aqui.  
**Off Digital:** Se Deixa eu ver aqui.  
**Marcelo Costa:** Sì.  
**Off Digital:** Vamos voltar aqui no Vamos voltar no codex aqui.  
**Marcelo Costa:** О.  
**Off Digital:** Ah. Relix. O qu?  
**Marcelo Costa:** Helix, não sei se solution.  
**Off Digital:** Solutions.  
**Marcelo Costa:** Deixa eu ver.  
**Off Digital:** Acho  
**Marcelo Costa:** Helix Energy  
**Off Digital:** que  
**Marcelo Costa:** Solution.  
**Off Digital:** vamos ver se ele consegue achar, porque se a gente conseguir achar direto aqui, esquece, aí a gente já vai ter o treinamento interno dos caras sem precisar deles. Aí  
**Marcelo Costa:** É, e esse é o primeiro cara que nós vamos vender a solução, viu, primo? Eles têm 3.000 funcionários,  
**Off Digital:** fodeu.  
**Marcelo Costa:** velho, no mundo. Brasil é uma ponta, ó. Mas os caras tão em Houston, tão em Luziana, tão olha barém só nos nos picos de ol gás, velho. Aqui é é dinheiro, primo, com força, velho.  
   
 

### 00:42:52

   
**Off Digital:** É mineração de dinheiro,  
**Marcelo Costa:** Ó, Singapura.  
**Off Digital:** né?  
**Marcelo Costa:** Os caras tão em Singapura, tão em Ué, pret, sei lá onde que é essa p\*\*\*\* aqui, velho.  
**Off Digital:** É, não, prim, nós temos que ser competitivo global, velho. Tava brincando  
**Marcelo Costa:** Não é essa, essa solução aqui é embaçada, velho. Vou te falar, nós estamos criando um bagulho cabuloso,  
**Off Digital:** de  
**Marcelo Costa:** velho. Eu acho que você não vai ter esses treinamentos. Agora, o que eu queria ver como eu abri aquele treinamento aqui, ele tinha onde foi feito, né?  
**Off Digital:** ver, viu, primo, que eu não acho impossível de ter não, cara. Porque se o cara tem que contratar o treinamento, tem que ter algum lugar que lista quais são os  
**Marcelo Costa:** Então, quem faz é o Drake. Ó,  
**Off Digital:** treinamentos.  
**Marcelo Costa:** tô vendo aqui o Drake. Ó, Drake. Ah, ó, não tinha visto essa plataforma no Drake. Um Drake para chamar de seu. O My Drake é uma nova maneira de da força de trabalho acessar  
**Off Digital:** Ja.  
**Marcelo Costa:** informações e receber notificações em tempo real. Ah, ó os cara fazendo aqui. Isso aqui tem que ficar esperto. Esse é um dos caras que eu pretendo, que eu acho que um dia vão querer comprar nós, mas eles estão andando aqui também.  
   
 

### 00:44:19

   
**Off Digital:** Ó, primeiro,  
**Marcelo Costa:** Vai,  
**Off Digital:** que que tem aqui?  
**Marcelo Costa:** te mandei no chat aí, depois você dá uma olhada.  
**Off Digital:** Vê se alguém bate aí com com os que você já deu  
**Marcelo Costa:** Pera aí,  
**Off Digital:** entrada.  
**Marcelo Costa:** deixa eu abrir aqui. Ó, esse que eu já vi, orientação, familiarização de embarcação, eh, ó, segurança operacional Nossa, de corrupção, treinamento. Eh, não, não tem esses que eu te falei que eu acho que eles são mais  
**Off Digital:** Quais são esses que você falou?  
**Marcelo Costa:** hã,  
**Off Digital:** Quais são os que você  
**Marcelo Costa:** veja que esse aqui tão mais offshore,  
**Off Digital:** falou?  
**Marcelo Costa:** ó. orientação e familiarização. Tá vendo na área tem offshore.  
**Off Digital:** Aham.  
**Marcelo Costa:** Esse tem mais do offshore, que é onde mais tem  
**Off Digital:** Fala, fala uns exemplos de alguns aí.  
**Marcelo Costa:** eh como é que ele veio para aqui? Assistir e garantir treinamento. Treinamento de linha de fogo. Pense na segurança do processo. Treinamento. Teste de gás. autorizado. Assistir esse videozinho do Drake, que que eles estão fazendo para eu ver. Cara, cri criar um inbox entre o funcionário e o e o e a empresa.  
   
 

### 00:48:18 {#00:48:18}

   
**Marcelo Costa:** Então aqui deve ter um negócio de treinamento também que o cara pode treinar aqui dentro,  
**Off Digital:** M.  
**Marcelo Costa:** mas ele tem um inboxinho o cara, ah, pedir suas férias, compromisso quando eu tenho que embarcar ou não e tal, mais um controle do usuário ali, mas tá longe dessa,  
**Off Digital:** Cara, não, isso aí é fácil. Eu tô vendo aqui só para tipo assim, vai que, né? Vai que já tem. Mas isso aí é fácil. a gente recebe eh o modelo e a  
**Marcelo Costa:** não, o cliente manda, o cliente manda Manda, qual é o modelo? Se eu preciso que ele faça, me fala qual é, velho. Vou entender.  
**Off Digital:** gente  
**Marcelo Costa:** O cliente tem isso, entendeu? Acabou. É só a gente pensar como é que a gente sobe isso, deixar um espaço pra gente subir o do cliente, certo? Vamos pegar essa base e sobe lá. Mas cada cliente, um cliente, a gente pega e faz. Quando tiver esse caso, a gente mexe na mão e acerta.  
**Off Digital:** a gente deixa a estrutura pronta assim toda área lá nas matrizes de subir treinamento específico do cliente e quando ele subir já endereça o cliente certo e já abre  
**Marcelo Costa:** Угу.  
**Off Digital:** ali dentro na aba de certificados, entendeu?  
   
 

### 00:49:39 {#00:49:39}

   
**Marcelo Costa:** Опа.  
**Off Digital:** Beleza? Então, o que que eu tô fazendo aqui? que eu tô endereçando aqueles candidatos que estão sem empresas e sem vagas direcionadas aqui. Já tô fazendo endereçamento. Вот.  
**Marcelo Costa:** Tá, eu vou tô procurando uma outra parada. Agora tem uns documento novo. Tô tentando procurar aqui. É, deixa eu ver se eu acho.  
**Off Digital:** อ  
**Marcelo Costa:** M.  
**Off Digital:** Aí, priminha, aqui no no detalhe do candidato, ó, você não tinha pegado um exemplo ainda que tem confere, tá vendo? confere. Fica aqui, ó. Aí fica um bloco com vários. Por exemplo, se tivesse oito, ia ter oito. Ia ter quatro em cima e quatro embaixo.  
**Marcelo Costa:** Ah, ficou bem melhor de  
**Off Digital:** É, velho. Fica confere.  
**Marcelo Costa:** visualizar.  
**Off Digital:** Aí você clicou aqui, ó, tudo clicável. OK. Clicou, já um. Lá aparece o documento aí, por exemplo,  
**Marcelo Costa:** Top.  
**Off Digital:** aqui só tá aparecendo parcial e confere, mas eu vou falar para ele que tem que aparecer eh o pendente também tem que aparecer tudo, porque aqui ele tá aparecendo só parcial,  
**Marcelo Costa:** o o que você tem.  
   
 

### 00:55:40 {#00:55:40}

   
**Off Digital:** parcial e confere  
**Marcelo Costa:** E aí ele tem as revisão aí, né? Aí quer ver depois volta aí. Aí o revisão você clicar nele vai para onde?  
**Off Digital:** revisão. Ele vai para essa aba aqui de revisão, ó. Aqui tem quatro parciais e seis confere, tá vendo?  
**Marcelo Costa:** Aham.  
**Off Digital:** Beleza.  
**Marcelo Costa:** Aí esse,  
**Off Digital:** Só não tá aparecendo os pendentes, tem que aparecer. Quais que são os pendentes?  
**Marcelo Costa:** tá? E aí a aba revisão,  
**Off Digital:** Certo?  
**Marcelo Costa:** você vai lá ver ele aí ele traz o detalhe do que  
**Off Digital:** Você clica em revisão, aí ele vai te vai mandar ele paraa fila de revisão  
**Marcelo Costa:** é,  
**Off Digital:** aqui,  
**Marcelo Costa:** tá?  
**Off Digital:** entendeu?  
**Marcelo Costa:** Ele não fala por que tá em revisão  
**Off Digital:** Pera aí, deixa eu voltar aqui. Onde é que nós estava mesmo? No detalhe, né?  
**Marcelo Costa:** dentro de um de um de um candidato aí. É isso aí,  
**Off Digital:** aqui, velho,  
**Marcelo Costa:** ó.  
**Off Digital:** é para enviar ele paraa revisão. Por que que ele vai paraa revisão? Porque ele tá parcial.  
**Marcelo Costa:** Certo. Mas por que ele tá parcial?  
**Off Digital:** Aí lá na aba de revisão vai aparecer, entendeu?  
   
 

### 00:56:54

   
**Off Digital:** Po, pode aparecer aqui também, provavelmente vai aparecer aqui nas sugestões da IA,  
**Marcelo Costa:** Eh,  
**Off Digital:** entendeu?  
**Marcelo Costa:** seria bom ele aparecer aí, porque pensa o seguinte, o cara tá eh o cara fica a maioria do tempo trabalhando no próprio candidato aqui. Tô subindo os documentos dele, quero entender esse cara. Tô aqui falando com o Marco. Ó, Marco, seus documentos, deixa eu ver aqui, ó. Esse CBSP seu tá com validade,  
**Off Digital:** อือ  
**Marcelo Costa:** não sei o quê. Ó, esse ele tá mostrando aí que é validade. Não, não é questão de validade, mas botar observação aí do porquê, entendeu? Seria bom ter esse campo aí para você bater o  
**Off Digital:** É, tem que ser aqui do lado,  
**Marcelo Costa:** olho.  
**Off Digital:** velho. Aqui do lado é o porquê, entendeu? Então,  
**Marcelo Costa:** É,  
**Off Digital:** quando eu clico aqui,  
**Marcelo Costa:** pode.  
**Off Digital:** muda aqui do lado. Quando eu clico aqui, muda aqui do lado.  
**Marcelo Costa:** É boa.  
**Off Digital:** Tem que ter o o o tipo o porquê,  
**Marcelo Costa:** É,  
**Off Digital:** né?  
**Marcelo Costa:** ficaria bom.  
**Off Digital:** Beleza. Aí você tem isso aqui tá bem funcional também, ó. Você tem quanto por cento o cara tá de aderência com a matriz.  
   
 

### 00:57:48 {#00:57:48}

   
**Off Digital:** Então, nesse caso, ele tá com 38%, porque ele tem quatro parcial e seis pendente. O que que tá pendente?  
**Marcelo Costa:** Uhum.  
**Off Digital:** Ó, saúde tá 100%, operacional tá 100%, normativo tá. É porque provavelmente isso aqui não tá correto, né?  
**Marcelo Costa:** Sim,  
**Off Digital:** Não táando, não tá,  
**Marcelo Costa:** ele não tá puxado mais.  
**Off Digital:** não tá informando. Mas tipo, você vai ter aqui, pô. Então o cara tá tá ruim no marítimo aqui. Beleza. Então é isso.  
**Marcelo Costa:** Então vou mandar a trava do nome.  
**Off Digital:** Aprovar para DP. Isso aqui também solicitar revisão de NR, rejeitar candidato. Isso aqui tudo tem que ligar esses botão. Então aprovar para DP, velho, é o final de tudo,  
**Marcelo Costa:** Tá.  
**Off Digital:** né? Tipo, tá, tá, todos os certificados estão de pé. Provar para DP,  
**Marcelo Costa:** Ele pode ter uma é até uma trava. Não, só a prova se tiver OK, né? Mas é é melhor não travar nesse  
**Off Digital:** não é? Porque aqui essa aprovação é quando você tem parcial revisão  
**Marcelo Costa:** momento.  
**Off Digital:** humana. Vamos dizer que o cara tivesse com tem,  
   
 

### 00:58:56 {#00:58:56}

   
**Marcelo Costa:** Tudo batendo.  
**Apresentação de Off Digital:** Er  
**Marcelo Costa:** Ele já ia ter  
**Off Digital:** é, o cara tem aqui, ó, 6 \+ 6,  
**Marcelo Costa:** passado.  
**Off Digital:** 12 \+ 4, 16\. 16 conferem ele, ele não ia tá aprovar para DP, ele já ia tá em DP. Agora o caso, o cara tem um 15 confere e um parcial,  
**Marcelo Costa:** Sim.  
**Off Digital:** vai ter que vir alguém aqui e ver e falar: "Não, velho, beleza, pode aprovar,  
**Marcelo Costa:** É. E o que acontece normalmente nesses casos é que eles vão lá e  
**Off Digital:** entendeu?"  
**Marcelo Costa:** manda o cara fazer.  
**Apresentação de Off Digital:** Er  
**Marcelo Costa:** Então ele vai lá na empresa,  
**Off Digital:** Aham.  
**Marcelo Costa:** marca, faz toda, faz toda essa,  
**Off Digital:** Aham.  
**Marcelo Costa:** esse negócio, marca pro cara fazer. Quando ficar pronto, sobe aqui e passa o cara para DP. Então, não é agora,  
**Off Digital:** É isso.  
**Marcelo Costa:** mas num próximo momento a gente vai poder até plugar essa essa quem faz,  
**Off Digital:** Sim. O já na solução,  
**Marcelo Costa:** quem não  
**Off Digital:** né? já na solução. Exatamente.  
**Marcelo Costa:** faz.  
**Off Digital:** Isso.  
**Marcelo Costa:** Ô primo, declaração você tem, você botou aquele, ele já sai falando que é uma declaração, né, da separação dos documentos e a declaração.  
   
 

### 01:00:20 {#01:00:20}

   
**Off Digital:** declaração já. Uhum.  
**Marcelo Costa:** Eu o que poderia aumentar aí nesse escopo da declaração é  
**Off Digital:** Uhum.  
**Marcelo Costa:** declaração lista de presença. Porque às vezes vem um negócio que é assim, ó, a declaração, ele fala assim, ó, o cara tem a NR20 aqui, é uma declaração, quer dizer,  
**Off Digital:** Угуm.  
**Marcelo Costa:** ele fez, mas ainda não recebeu o certificado. Essa declaração vale por 30 dias. Então, eh, ele, ele fala sobre certificado. Já a lista de presença, às vezes você tem um curso, ah, ó, vai ter um curso de NR 20 aqui, vai fazer todo mundo. Aí fez 10 funcionários lá, aí o cara assina a lista de presença.  
**Off Digital:** Угу.  
**Marcelo Costa:** E os documentos que vem junto, ó, minha lista de presença que eu tava no curso mais o certificado. Então, isso às vezes vem que era um que você tá abrindo ali, às vezes ele tem, tinha um da Shell que você abriu, que aquilo é uma lista de presença. Quando você lê o cabeçário lá, ela fala: "Ó, beleza, é ele r, o Marco participou". Ou seja, tem uma assinatura, ó, o cara fez. É lógico, eu acredito que do jeito que ele tá, ele já vai barrar, mas só para entender que tem essas duas coisas: declaração e lista de presença  
   
 

### 01:01:31 {#01:01:31}

   
**Off Digital:** Aí o Cara,  
**Marcelo Costa:** também.  
**Off Digital:** você tem que me mandar alguns arquivos de lista de presença, se você tiver. Aí eu peço aí eu jogo para ele mastigar, entender e criar um parâmetro de triagem para pra lista. Aí ele vai entender o que que é.  
**Marcelo Costa:** Tô anotando aqui. Daqui a pouco eu vou te mandando tudo no zap esses pontos que nós estamos falando. Já tô anotando na  
**Off Digital:** aqui. Beleza,  
**Marcelo Costa:** conversa.  
**Off Digital:** eu já tô resolvendo o link aqui dos candidatos com as empresas. Eh, deixa eu ver o que que mais que ele atualizou aqui. Aí agora tem que ver direitinho, botar o nome do produto, ver o domínio, eh, botar uma logo, nem que seja provisória, pegar logo lá do MDE e você me mandar para eu botar aqui também, ou você ver se se não quer botar, se quer botar, como é que faz? De repente pode ter a logo dele, em vez de ser aqui na barrinha do produto, ser aqui na administração, eh, em nome  
**Marcelo Costa:** Não, não v, eu acho que não tem que pôr, não. É,  
**Off Digital:** de  
**Marcelo Costa:** é o, a solução. É, velho, os caras tão usando a solução nossa ali.  
   
 

### 01:03:08 {#01:03:08}

   
**Marcelo Costa:** Talvez se ele queira mostrar para alguém,  
**Off Digital:** Então,  
**Marcelo Costa:** pode. O cliente parece que valoriza, né, velho? O cara meter a login dele lá. Pode pôr,  
**Off Digital:** não,  
**Marcelo Costa:** né?  
**Off Digital:** a A gente põe a logo dele aqui, ó, no nome de cada recruta, põe MDE.  
**Marcelo Costa:** Угуm.  
**Off Digital:** Em vez de pôr a foto do recruta, põe a logo do MDE, entendeu? Aí vai ficar vários MDE aparecendo no sistema inteiro, entendeu?  
**Marcelo Costa:** M.  
**Off Digital:** Por exemplo, tá vendo aqui, ó? Fica aqui teste certify, recruta certify. Vai ser aqui o nome da dos recrutas, tipo, cadê? Mariana Costa, Rafael Neves, Camila Duarte, vai tá tudo aqui. E aí, em vez de ficar as iniciais dele, vai ficar loginho da MDE.  
**Marcelo Costa:** Boa. Eu tenho logo aqui  
**Off Digital:** Então você vai ver, você vai ver vários MDE operando dentro do sistema,  
**Marcelo Costa:** já.  
**Off Digital:** mas não vai, não precisa ter uma logo no, no lado MDE, entendeu?  
**Marcelo Costa:** M. O que que a gente tem mais? Tem, eu pedi pra menina aqui, tem um documento específico, acho que a gente não precisa nem se prender nele, não, mas é um de rádio operador que eu não sei se Deixa eu achar aqui.  
   
 

### 01:04:55 {#01:04:55}

   
**Marcelo Costa:** LPNL em algum momento você cruzou com ele?  
**Off Digital:** Ô primo, você tem um login do Drake? Não  
**Marcelo Costa:** Tenho.  
**Off Digital:** tem?  
**Marcelo Costa:** Ô primo, lá na sua regra, em algum momento você falou ali da do TCEA, que são os documentos de rádio operador.  
**Off Digital:** Ah.  
**Marcelo Costa:** Em algum momento você já puxou essa essa regra aí, já tá naquelas naquelas classificações sua. Um dos documentos desses cara aqui, ele ele vem com o Qode. Então vem o documento do cara, mas você precisa ler o QR code para mostrar a validade, entendeu?  
**Off Digital:** Угуm.  
**Marcelo Costa:** É um documento exclusivo que não precisa ter isso aí nesse momento, mas em algum momento a gente vai tava olhando ele, né? vai passar por ele. Rádio operador tem bastante, então talvez é alguma solução que leia aí o cara tem que ler o QRC e entrar para validade. É uma parada mais Vou achar um documento, eu vou pegar uma um exemplo, tá?  
**Off Digital:** Não, o fato de ler que record é muito tranquilo, é só a gente plugar mais Tá? A gente vai adicionando regra, né,  
**Apresentação de Off Digital:** Er  
**Off Digital:** priminho? Vai adicionando regra.  
**Marcelo Costa:** LNA Ja. Aí nessa nessa relação de conferência, um ponto que às vezes os caras precisam Na verdade, já pediram para eles, a própria Hélix pediu para eles olharem isso, é que os documentos eles vêm assinado, tem assinatura de do órgão lá e tal, de quem fez o o certificado e tal.  
   
 

### 01:08:01 {#01:08:01}

   
**Marcelo Costa:** E às vezes tem um outro documento que vem sem assinatura, sem carinho. Aéliix mandou outro dia eles olharem e uma das checagens era se os documentos têm assinatura. Então era era bom a gente pensar nisso também para ele fazer essa checagem na leitura do do OCR. Deixa eu dar uma olhada aqui no em algum documento pra gente dar uma Sempre eu tenho algumas assinaturas, ó. Tem assinatura, tem uns que não tá assinado pelo candidato, entendeu?  
**Off Digital:** Угу.  
**Marcelo Costa:** Candidato recebeu e não assinou o documento. Então você vê, normalmente tem quatro assinaturas, ó. Tem um do diretor administrativo, outro do engenheiro de segurança do trabalho, técnico de segurança e o aluno.  
**Off Digital:** Угу.  
**Marcelo Costa:** Isso nas RS aí, vamos ver. Sem NR. Deixa eu ver. Eu acho que o padrão são quatro assinaturas na NR. É isso, ó. assinatura do aluno, tem o engenheiro de segurança do trabalho, tem o instrutor e a  
**Apresentação de Off Digital:** Er  
**Marcelo Costa:** administradora do curso. Nr4 assinaturas. Vamos ver o STCW. O pito, opito, duas assinaturas. Você tem, ó, gerente operacional e engenheiro de segurança, responsável técnico. Duas assinaturas no OPITO,  
   
 

### 01:09:53 {#01:09:53}

   
**Apresentação de Off Digital:** Er  
**Marcelo Costa:** CBSP. O STCW, além das assinaturas, ele tem uma assinatura do representante marítimo e tem também um um selo do de DPC, que são aqueles eh são tropicalizados, né? pode ser num segundo momento, mas só lembrando que esse é um ponto que a  
**Off Digital:** Anota para mim, anota tudo.  
**Marcelo Costa:** Ч. Técnico segurança do trabalho e engenheiro segurança do trabalho. Ч.  
**Apresentação de Off Digital:** Er  
**Off Digital:** Aí, priminho já tá pegando tudo aqui, ó, no camban.  
**Apresentação de Off Digital:** Er  
**Off Digital:** Tá vendo? Pegando as empresas,  
**Marcelo Costa:** Угуm.  
**Off Digital:** os documentos aqui, ó. Laudc tem 16 documentos. Calma aí que não carregou ainda aqui. Alo.  
**Marcelo Costa:** Sete confere dois parcial. Agora ele já tá usando o motor aí para conferir ou ele tá Então ele já  
**Off Digital:** Tá,  
**Marcelo Costa:** tá diferente do outro.  
**Off Digital:** tá.  
**Marcelo Costa:** Ele tá pegando o mesmo cara, mas tá usando o motor para conferir.  
**Off Digital:** Exatamente.  
**Marcelo Costa:** Top. Então  
**Off Digital:** O que a gente tem que o que a gente tem que entender é se ele tá se tá batendo o número de  
**Marcelo Costa:** da  
**Off Digital:** documentos, por exemplo.  
**Marcelo Costa:** tá, vamos pegar,  
   
 

### 01:15:47 {#01:15:47}

   
**Off Digital:** Vamos ver se eu tô com eles abertos,  
**Marcelo Costa:** vamos pegar uns casos aí. Deixa eu  
**Off Digital:** tô com outro aberto aqui. Vamos ver lá o desci.  
**Marcelo Costa:** só  
**Off Digital:** Só que aqui no teu eu não consigo ver o número de documentos ações. Onde é que clica? aqui  
**Marcelo Costa:** qualquer um ou olhinho ou o outro tá na mesma.  
**Off Digital:** documentos cinco  
**Marcelo Costa:** A quantidade tá lá em cima.  
**Off Digital:** confere três parcial um pendente. Então aqui ele tem oito,  
**Marcelo Costa:** Nove no total.  
**Off Digital:** nove documentos. Aqui só tem sete,  
**Marcelo Costa:** Deixa eu dar uma analisada  
**Apresentação de Off Digital:** Er  
**Off Digital:** não, aqui tem nove. Sete confere dois parcial.  
**Marcelo Costa:** nele.  
**Off Digital:** E aqui a gente tem cinco confere, três parcial e um pendente.  
**Marcelo Costa:** Só que ele tem muito mais documento que ele não tá somando tudo que tem do cara aí, que é os documentos que não exigível, que estão lá embaixo, né?  
**Off Digital:** Sim, tá, tá botando só os da matriz. Agora pendente, ele tem um STCW pendente e aqui tá acusando 1 2 3 4 5\. Confirma. do parcial. Certificado de proficiência, certificado de competência.  
   
 

### 01:17:56

   
**Off Digital:** É que é muito diferente os nomes do jeito que tá mostrando no teu sistema. Ele ele abre o documento.  
**Marcelo Costa:** Abre aí.  
**Off Digital:** Certificado de proeficiência parcial. Se eu agora não tô entendendo esse pendente curso de embacação rápida de  
**Marcelo Costa:** Pendente.  
**Off Digital:** resgate.  
**Marcelo Costa:** Pendente é que ele nem subiu, não existe, não veio o documento  
**Off Digital:** Não, mas aqui ele tá não tem nenhum que que tem nove  
**Marcelo Costa:** ainda.  
**Off Digital:** documentos.  
**Marcelo Costa:** Vamos dizer aqui. Ele não leu nenhum daqueles que bateu aí, então aí ele nem conferiu nada.  
**Off Digital:** Não, eu tô querendo entender o pendente para onde o que ele não tinha subido, como que ele classificou, entendeu?  
**Marcelo Costa:** Então o pendente é que não apareceu, não mandou nada. Então como ele como ele tinha  
**Off Digital:** Curso de embarcação rápida.  
**Marcelo Costa:** que  
**Off Digital:** Curso de embarcação rápida de resgate. Agora  
**Marcelo Costa:** ele não mandou esse documento. Esse documento não existe, por isso que tá pendente, ele precisa mandar a matriz. Essa parte de cima, ele tá dizendo, ó, esse aqui tá pendente, a matriz exige, não chegou nada aqui que validou com isso. Então ele não viu o documento ainda, não vai ter esse documento.  
**Off Digital:** Então é os coque esse aqui e esse aqui.  
   
 

### 01:19:48 {#01:19:48}

   
**Off Digital:** Ele ele deu esses dois aqui pendente, ele bateu parcial. Quer dizer, esse,  
**Marcelo Costa:** Os dois parcial ele bateu.  
**Off Digital:** esse, e, esse ele bateu parcial,  
**Marcelo Costa:** E mas e no seu?  
**Off Digital:** só que esse parcial ele deu confere.  
**Marcelo Costa:** Aonde você tá dizendo? Pera aí.  
**Off Digital:** Tô dizendo no novo.  
**Marcelo Costa:** O seu conferiu.  
**Off Digital:** Conferiu.  
**Marcelo Costa:** E qual que é o documento? Deixa eu ver aí.  
**Off Digital:** É esse aqui.  
**Marcelo Costa:** Deixa eu vol, deixa eu abrir também esse cara aqui, só para eu conseguir ver melhor como que chama esse cara aí.  
**Off Digital:** É o Laudci.  
**Marcelo Costa:** Lá desc. Beleza, Laudestir tem um parcial que é o CAC EAEC, né?  
**Off Digital:** Uhum.  
**Marcelo Costa:** Ele tá dando parcial. Carga horária não informada no documento ou não atend.  
**Off Digital:** Ou sei, né? C A aqui ele deu.  
**Marcelo Costa:** É,  
**Off Digital:** Aqui ele deu confere.  
**Apresentação de Off Digital:** Er  
**Marcelo Costa:** tem aí no seu.  
**Off Digital:** Deu  
**Marcelo Costa:** Então vamos ver se que que acontece aqui se ele tem a carga horária aqui,  
**Off Digital:** confere.  
**Marcelo Costa:** porque no meu ele não validou porque disse que não tinha 40 horas.  
**Off Digital:** Não é por causa da da do vencimento que ele não tem a data de  
   
 

### 01:21:26

   
**Marcelo Costa:** Não veja que ele tá falando aí no no canto,  
**Off Digital:** vencimento.  
**Marcelo Costa:** ó. É por isso que eu falei que ele dá observação para você aí para entender, ó. Então, ó, carga horária não informada no documento,  
**Off Digital:** Aham.  
**Marcelo Costa:** ou seja, não encontrou 40 horas.  
**Off Digital:** Aham.  
**Marcelo Costa:** e ele pede 40 horas na matrícula.  
**Off Digital:** Não atende ou não atende a  
**Marcelo Costa:** Eh, então assim,  
**Off Digital:** exigência.  
**Marcelo Costa:** ele falou: "Ó, o documento é exato e tal, mas você tá pedindo 40 horas e não tem nada no documento falando que é 40 horas. E realmente,  
**Off Digital:** Uhum.  
**Marcelo Costa:** realmente não tem. Só que aí tem um ponto importante. Esse documento ele não existe, não existe 20 horas, um CAC 20 horas, entendeu? A norma, a norma é a ela é o o CAC,  
**Off Digital:** Aha.  
**Marcelo Costa:** pode ser que demore, tenha os 40 horas para fazer, mas eu acho que isso tá na norma, como já tá na tua regra. Então assim, aqui ele barrou falando, ó, você falou 40 horas,  
**Apresentação de Off Digital:** Er  
**Marcelo Costa:** eu não encontrei,  
**Off Digital:** Aqui ele já validou e falou:  
   
 

### 01:22:30 {#01:22:30}

   
**Marcelo Costa:** mas a regra vai lá no não existe K com menos.  
**Off Digital:** "Não precisa.  
**Marcelo Costa:** Você tem o certificado, quer dizer que fez as 40\. Então eu acredito que tá mais nesse caminho do  
**Off Digital:** Sim. O que eu quero entender é que tem um pendente que é o  
**Marcelo Costa:** que  
**Off Digital:** CRR, custo de embarcação rápida e resgate.  
**Marcelo Costa:** Então esse documento ele ainda não mandou.  
**Off Digital:** E sim, mas aqui ele tá dando como confere e tá aqui um  
**Marcelo Costa:** Ah, ele tá dando um confere aí,  
**Off Digital:** documento.  
**Marcelo Costa:** então. Então, pode ser que no meu ele leu, mas não  
**Off Digital:** Ó lá, ó lá. Eu vou abrir abrir o PDF  
**Marcelo Costa:** identificou.  
**Off Digital:** aqui.  
**Marcelo Costa:** E vamos ver o que ele é.  
**Off Digital:** C R C habilitação profissional para gerenciamento dos recursos de praça de máquinas profissional skills indign room centro de instruçãoante gradã aranha. Onde que aparece a sigla dele aqui?  
**Marcelo Costa:** No, às vezes, na maioria das vezes, não vem. A sigla é muito é  
**Off Digital:** Tá. Então,  
**Marcelo Costa:** muito  
**Off Digital:** abre aí no teu e e vê aí o que que é exatamente curso de embarcação rápida e resgate 24  
**Marcelo Costa:** Não, tá certo. Esse esse é quase certeza que esse é o documento,  
   
 

### 01:23:48

   
**Off Digital:** horas.  
**Marcelo Costa:** tá? Deixa eu ver o código dele aqui. Eh, ó, ele tá dando regras, não especificada anteriormente. Deixa eu ver o código do STCW. STCW 1978\. Amende aqui. Eh, esse é um ser mesmo, eu acredito, viu? É, esse cara é um ser que você tá vendo aí. Agora o meu pode ser que, ó, tá aqui, ó. Vamos lá. lá no certify,  
**Off Digital:** Ага.  
**Marcelo Costa:** ele deu um confere no documento,  
**Off Digital:** Ага.  
**Marcelo Costa:** tá? Mas ele não identificou que esse documento é um ser. Você for lá embaixo,  
**Off Digital:** Uhum.  
**Marcelo Costa:** ele tem um confere lá embaixo no de baixo para cima.  
**Off Digital:** Tá aqui,  
**Marcelo Costa:** 1 2 3 4 5 aí tá esse documento. Vamos conferir se é esse. Aí vamos ver se é esse.  
**Off Digital:** né?  
**Marcelo Costa:** É o mesmo documento, né? Não,  
**Off Digital:** Aonde priminho?  
**Marcelo Costa:** não, não.  
**Off Digital:** histórico.  
**Marcelo Costa:** Vai lá no mesmo, no na aba. Pode descendo. Vai para baixo aí. Pode ir, pode ir aí nos documentos aí,  
**Off Digital:** Aham.  
   
 

### 01:25:26

   
**Marcelo Costa:** ó. Ó, vê se confere que tem aí, ó.  
**Off Digital:** Esse esse é um  
**Marcelo Costa:** Isso. Eh, eu achei que pode ser esse que ele deu um confere,  
**Off Digital:** aquaviário.  
**Marcelo Costa:** mas não é porque é outro código esse. Esse não é o certo que a gente tá falando. Eu não sei porque que ele deu. Confere aí  
**Off Digital:** Ele não fala que não subiu o documento,  
**Marcelo Costa:** embaixo.  
**Off Digital:** ele fala que não, ainda não comparado. Tá vendo aqui, ó?  
**Marcelo Costa:** É, então, mas o mas o ainda não comparado é que assim, ele não recebeu nenhum documento que batesse para ele comparar, entendeu?  
**Off Digital:** Uhum. O documento tá aqui.  
**Marcelo Costa:** Só que talvez esse  
**Off Digital:** Não tá. Não é esse documento o certo  
**Marcelo Costa:** é, esse é, só que eu não sei da onde ele tirou. Às vezes os tava lá no banco de dados, os caras subiram de novo e ele não identificou aqui.  
**Off Digital:** Bom, então a gente sabe que tá funcionando, né?  
**Marcelo Costa:** Tá melhor do que o outro.  
**Off Digital:** E bem,  
**Marcelo Costa:** Não,  
**Off Digital:** e bem,  
**Marcelo Costa:** ó, agora eu acho que deixa eu  
**Off Digital:** porque p\*\*\*\*, se ele se ele trouxe,  
**Marcelo Costa:** ver  
   
 

### 01:26:21

   
**Off Digital:** já trouxe pro confere dois dois, um parcial e um pendente, ele trouxe pro confere.  
**Marcelo Costa:** 07511\. Não é esse aqui. Deixa eu dar um ir dando mais uma olhada aqui.  
**Off Digital:** Você  
**Marcelo Costa:** Pera aí.  
**Off Digital:** quer que abra o documento aqui de novo?  
**Marcelo Costa:** Não, esse que você tá aberto é o seu, né? Deixa ele aberto aí.  
**Off Digital:** É.  
**Marcelo Costa:** O código dele lá em cima, né? Opá, é um 07 51\. Não, não. Pode ser esse, ó. Não é nenhum desses aí. Vamos ver aqui esse negócio tá 05 905\.  
**Off Digital:** Quer que eu pergunte na Ia aqui?  
**Marcelo Costa:** É, o meu aqui tá com vários erros, velho. Tá subindo,  
**Off Digital:** Você  
**Marcelo Costa:** tá dando uns confere, tá subindo o mesmo documento, ó.  
**Off Digital:** quer que eu confirmo aqui se isso é um cerco  
**Marcelo Costa:** No César  
**Off Digital:** aí?  
**Marcelo Costa:** confirma, mas eu é, é, com certeza é agora você vê o meu, o nosso aqui, o certifi tá dando maior vacilo em tudo aqui, velho. Tá lendo uns bagulhos, nada a ver. É sé, né?  
**Off Digital:** É, é um STCWCR.  
   
 

### 01:28:29

   
**Marcelo Costa:** Eu  
**Off Digital:** Joguei na Ia Vamos ver.  
**Marcelo Costa:** achei ele aqui. Achei ele aqui, ó. Esse documento que você tá falando aí, que você tá mostrando aí, aqui ele bateu com EGPM. Deixa eu ver se é isso. É. Ele bateu com um epm habilitação profissional para gerenciamento eh de recurso. Pá, 07 511\. Beleza, achei esse documento aqui, só que ele bateu aqui como um gerenciamento dos recursos para máquina, não sei o quê, um STCW que não É, que ele não tem código, né?  
**Off Digital:** Да.  
**Marcelo Costa:** Ó, regra não especificada no STCW.  
**Apresentação de Off Digital:** Er  
**Marcelo Costa:** Agora Tá. Eu tô na dúvida. Tô na dúvida, primo, porque tem um documento aqui que é muito parecido, um STCW que não tem código.  
**Off Digital:** Aham.  
**Marcelo Costa:** Eu vou dar uma busca se ele é um cerco ou não. Deixa eu ver quem que é esse cara. Chefe,  
**Off Digital:** Eu mandei aqui também.  
**Marcelo Costa:** subchefe oceânica.  
**Off Digital:** Eu acho que não é não, primo.  
**Apresentação de Off Digital:** Er  
**Off Digital:** tá falando aqui que pelo certificado ele diz que é habilitação profissional para gerenciamento dos recursos de praça de  
   
 

### 01:31:49

   
**Marcelo Costa:** Então,  
**Off Digital:** máquinas.  
**Marcelo Costa:** tem um documento que é o é conhecido como egm. Eu acho que é esse, ó. Certificado emitido. Só que aqui é outra parada. Vamos ver. Verificado emitindo tem professor internacional sobre  
**Apresentação de Off Digital:** Er  
**Marcelo Costa:** padrões. É, eu acho que esse não é o CES.  
**Off Digital:** Eu tô achando que ele não é também. Eu tô pedindo para ele,  
**Marcelo Costa:** Ele é um,  
**Apresentação de Off Digital:** Er  
**Marcelo Costa:** ele já bateu com outros aqui. O  
**Off Digital:** eu vou pedir para ele analisar o candidato como um  
**Marcelo Costa:** CS  
**Off Digital:** todo.  
**Marcelo Costa:** é não é o CES, tá? Porque o César é o seguinte, o César é curso especial de embarcação e sobrevivência e salvamento.  
**Off Digital:** Não,  
**Marcelo Costa:** E ele tem um código de  
**Off Digital:** mas mas é o e e é e c rr,  
**Marcelo Costa:** CW  
**Off Digital:** né? O c  
**Marcelo Costa:** C e não, você tá falando Cés ou C?  
**Off Digital:** tô falando ser o CRR  
**Marcelo Costa:** C E RR,  
**Off Digital:** é o é o documento que tava faltando pendente é o CRR, o CES tá confere.  
**Marcelo Costa:** curso especial de embarcação e resgate rápido.  
**Off Digital:** Isso,  
**Marcelo Costa:** É esse que você tá falando.  
   
 

### 01:33:27 {#01:33:27}

   
**Off Digital:** isso, isso.  
**Marcelo Costa:** Ele tem uma tabela específica no STCW, só que nesse nessa certificadora aí não está aparecendo a tabela, por isso que talvez ele tá ele não tá, mas ele não deveria jogar como CES, porque esse aí não é um não é um SER, nenhum CES. Eu tenho aqui o S e o CES, que são é outra coisa. E eles têm tabela. Esse aí não tá, não tem tabela. Ele deveria ter. É, mas ele é esse documento em específico não tem tabela, mas eles no nosso aqui tá dando  
**Off Digital:** Ó, ó o que que ele deu aqui para mim no Tô falando já com a gente aqui. M. Ó, ele tá falando aqui,  
**Marcelo Costa:** F.  
**Off Digital:** confirmado que esse candidato existe, tem o PDF eh PGM Engine Room Resource Manager processada.  
**Marcelo Costa:** M.  
**Off Digital:** Agora vou olhar a comparação que colocou isso como cer, porque isso é falso, positivo, claro. No banco a comparação desse candidato não tem nenhum confere para o item certo. O HPGM aparece como declaração ou não exigindo, não como aprovado. Então o erro provavelmente está na camada de exibição do detalhe do candidato agrupando o documento sem usar o altaração. Vou conferir esse caminho agora. Achei a causa. Não é o motor aprovado.  
   
 

### 01:35:25

   
**Off Digital:** Certo. O banco gravou declaração, mas a tá colocando declaração dentro de confere. Isso tá errado para uso real. Vou ajustar para só.  
**Marcelo Costa:** Eh É, mas não tem mas não tem nada a ver com declaração.  
**Off Digital:** Pois é.  
**Marcelo Costa:** Fala, não tem nada a ver com  
**Off Digital:** Vamos ver isso aqui.  
**Marcelo Costa:** declaração.  
**Off Digital:** Claração vai para revisão parcial, porque na verdade esse documento é porque não tinha o documento, não é isso?  
**Marcelo Costa:** Aqui para mim ele tá pendente porque o cara não tinha mandado, não mandou.  
**Off Digital:** Exato.  
**Marcelo Costa:** Não existe esse documento na base. Ele aí do seu lado,  
**Off Digital:** Exato.  
**Marcelo Costa:** ele pegou um documento e validou um documento que não  
**Off Digital:** Na verdade,  
**Marcelo Costa:** é.  
**Off Digital:** ele não validou. Ele, ó lá, como ele falou aqui, ele não tem confere, não tem confere para o item certo.  
**Marcelo Costa:** Mas o front que tá mostrando é isso?  
**Off Digital:** O front tá mostrando como declaração, só que também não é declaração. Então vamos entender o que que  
**Marcelo Costa:** Esse HPGM, na verdade, para mim, a  
**Off Digital:** será que ele não mandou esse documento HPGM? Ele deu como não enviado.  
**Marcelo Costa:** para mim é egpm. Esse documento que você lê aí na minha matriz aqui do do Certify, ele tá dizendo que é ele bate com EGPM, ele bate certo aqui com que eu botei de nomenclatura que não é HPGM, é eg, mas é que às vezes os caras usam em inglês e troca um pouco a sigla, né?  
   
 

### 01:37:13 {#01:37:13}

   
**Off Digital:** Uhum. Então, mas então foi que o cara subiu esse documento no lugar de ser. É  
**Marcelo Costa:** Não, não. Aqui, na verdade, esse documento, o seu, aí pegou e jogou no lugar do  
**Off Digital:** isso.  
**Marcelo Costa:** CS. Aqui ele leu certo no lugar que é o documento certo mesmo, que é esse GPM. Eu acho, primo, que o caminho pra gente testar o motor, que era a forma que eu mais testava aqui, era pega um candidato, sobe um a um e vê o que ele lê. Aí a gente vai, p\*\*\*\*, beleza, validou, ó, aqui deu erro assim, ó, isso aqui, ah, não, verdade, isso aqui é tal. Aí, porque aí a gente consegue,  
**Off Digital:** Sim.  
**Marcelo Costa:** porque quando você pega um bloco muito grande, a gente fica perdido no que que tem que arrumar. E aí você começa a ver um monte de, ah, arruma isso, arruma aquilo, arruma. Então é melhor pegar, ó, vamos pegar as normas, vamos subir todas as normas aqui. Vamos ver o que vai  
**Off Digital:** Não, isso aí a gente tem que fazer,  
**Marcelo Costa:** acontecer.  
**Off Digital:** vai ser o vai ser a validação final, final. Mas cara, já foi um positivo muito bom, porque de todos os documentos ele errou um basicamente,  
   
 

### 01:38:27

   
**Marcelo Costa:** É.  
**Off Digital:** né, no automático, só na importação, sem sem upload, porque assim, o motor ele foi feito eh enrijecido na matriz. Esses documentos a gente importou sem passar pela matriz.  
**Marcelo Costa:** Então, mas ele tá batendo contra  
**Off Digital:** tá batendo contra eh direto nas na base de  
**Marcelo Costa:** quem?  
**Off Digital:** norma.  
**Marcelo Costa:** Mas aí como é que ele tá dando? Porque vamos pensar, ele tá subindo numa vaga. A vaga tá pedindo o EGPM, beleza?  
**Off Digital:** Uhum.  
**Marcelo Costa:** Ele e tá pedindo também o SER, ele pegou o documento e botou esse como SER.  
**Off Digital:** Mhm. Mhm.  
**Marcelo Costa:** Então ele tá, ele tá conferindo, batendo contra a matriz, senão ele botava não exigido  
**Off Digital:** Sim,  
**Marcelo Costa:** aí.  
**Off Digital:** mas é que a eh eu acho que que tá acontecendo, como a matriz não foi criada dentro das regras, entendeu?  
**Marcelo Costa:** É, mas então se não tem matriz no E Ele  
**Off Digital:** Não tem a matriz,  
**Marcelo Costa:** não é,  
**Off Digital:** mas é uma matriz importada, não é uma matriz criada.  
**Marcelo Costa:** então aí você não tá pegando na raiz, né? Porque você para você montar a matriz aí dentro,  
**Off Digital:** Entendeu?  
**Marcelo Costa:** você vai pegar a matriz só dos documentos validados, velho.  
   
 

### 01:39:53

   
**Marcelo Costa:** Se não é um documento validado, eu tenho que entender o que que esse é.  
**Off Digital:** Exatamente. Que o problema tá na hora de criar a matriz. Eu  
**Marcelo Costa:** É, mas esse mas esse erro dele aqui, esse erro dele aí, ele validou um documento errado,  
**Off Digital:** acho.  
**Marcelo Costa:** vamos dizer assim. Não, não tá batendo com a matriz, não tem nada a ver de amarra com a matriz. Ele pegou um documento e falou: "Ó, isso aqui confere no CS". Não, não, não pode conferir isso no CES. Então, no, independente da matriz, eu acho que ele não tá batendo aí. Agora talvez é o fluxo mesmo de p\*\*\*\* botei a matriz fazer. Eu acho talvez tenha que seguir esse caminho, né? Que ele tá puxando, velho,  
**Off Digital:** Não,  
**Marcelo Costa:** 1000  
**Off Digital:** eu eu eu tô supondo isso que que tipo ele pode ter gerado essa confusão porque ele não passou dentro de  
**Marcelo Costa:** documentos.  
**Off Digital:** uma matriz criada e validada, mas a gente ainda não entendeu aqui porque é o erro, porque assim aqui o feedback é esse, né? Achei a causa, não é que o motor tá aprovando o c, o banco gravou declaração, mas a UI tá colocando declaração dentro de confere.  
   
 

### 01:40:57 {#01:40:57}

   
**Off Digital:** Então, que também é outro erro, né?  
**Marcelo Costa:** É,  
**Off Digital:** Também é outro erro. É,  
**Marcelo Costa:** não deveria.  
**Off Digital:** exatamente. Mas basicamente o que ele tá falando aqui é que ele não deu confere pro cé e vamos entender no frigir dos  
**Marcelo Costa:** Você pediu,  
**Off Digital:** ovos aqui o que que exatamente que aconteceu.  
**Marcelo Costa:** ele tá rodando.  
**Off Digital:** Hã,  
**Marcelo Costa:** Ele tá rodando. Você pediu para  
**Off Digital:** tá rodando, tá rodando, tá rodando.  
**Marcelo Costa:** mais  
**Off Digital:** Aí por isso que eu não mandei nada, porque eh tem que esperar ele parar para que ele não lê o Se eu mandar agora no meio, ele não vai ler, entendeu?  
**Marcelo Costa:** em cima.  
**Off Digital:** Eu teria que parar o que ele tá fazendo para ele ler.  
**Marcelo Costa:** Não, deixa ele olhar aí.  
**Off Digital:** Então, mas é isso, primo. A gente só vai conseguir ver mesmo fazendo o teste real.  
**Marcelo Costa:** Eh,  
**Off Digital:** Só que a  
**Marcelo Costa:** cara, o teste real e não com 1000 documentos,  
**Off Digital:** diferença  
**Marcelo Costa:** tá ligado? Porque 1000, velho, a chance dele errar com pegar 1000 e e do jeito que ele fez rápido, eh,  
**Off Digital:** Aham.  
**Marcelo Costa:** cara, ele tem que tem que ir no caminho, sobe 10 documentos, vai ver ele como ele se porta com 10\. Aqui ele se porta totalmente diferente quando eu subo 10 documentos, quando eu subo 50\. Aí a gente criou um sistema de fila que ele entrava,  
   
 

### 01:42:02

   
**Off Digital:** Ага.  
**Marcelo Costa:** ó, entra na fila, lê um, acaba de ler, entra o outro, lê outro, acaba de ler. Então, a cada candidato aqui demorava tipo às vezes 5, 10 minutos por candidato. Então, quando ele pega um lote gigante, velho, algum detalhinho passa, entendeu?  
**Off Digital:** Sim.  
**Marcelo Costa:** Ele pegou aí de porrada, né?  
**Off Digital:** É, teoricamente não era para dar bug porque ele tem muitos workers funcionando e o trabalho ele já é dividido, entendeu? Ele já é dividido em vários workers. Então, provavelmente assim dentro da lógica de que foi construído o sistema, não é para ele ter divergência em volume, mas como a gente tá fazendo um negócio envolvendo todas as normas, toda a base, muito mais informação, eh, pode acontecer muito de cara misturar regra, de esse esse refinito.  
**Marcelo Costa:** E cara,  
**Off Digital:** Então a gente é  
**Marcelo Costa:** e aí é os guardi que o cara tem que ir colocando, entendeu?  
**Off Digital:** exatamente,  
**Marcelo Costa:** Não adianta. É isso que é é coisinha que a gente tem quear.  
**Off Digital:** você só vai ver na prática. Não, não é, não tem como. Agora o bom,  
**Marcelo Costa:** É,  
**Off Digital:** velho, é que quando deu pau, nós vamos abrir um terminal e vamos resolver.  
   
 

### 01:43:19 {#01:43:19}

   
**Off Digital:** Nós não vamos ter que abrir lá o emaranhado, né,  
**Marcelo Costa:** é.  
**Off Digital:** velho?  
**Marcelo Costa:** Não, pelo amor de Deus,  
**Off Digital:** Entendeu?  
**Marcelo Costa:** pelo menos a gente pode fazer o bagulho, né?  
**Off Digital:** Plugga o negócio e fala:  
**Marcelo Costa:** E outra aqui nessa,  
**Off Digital:** "Ó, velho, deu pau aqui, que que é?" Entendeu?  
**Marcelo Costa:** só nesse cara aí tem erro para c\*\*\*\*\*\* de outras coisas aqui que ele leu errado. meu  
**Off Digital:** terminar que eu tava que eu tava  
**Marcelo Costa:** aqui.  
**Off Digital:** c\*\*\*\*\*\*. Tinha um terminar aqui. Hum. Vamos lá. O cara já abriu uma aba aqui para mim do nada. Eh, vamos lá. Confimos para Biss. Lá desses não tem nenhum confere no motor. Para S. O documento hpgm. PDF está salvo como declaração code documento classificado como declaração temporária não comparado com a matriz. O candidato inteiro tá assim no banco. Declaração 9, não exigido 128 parcial 1, pendente 6 confere zero. A causa era o i, não motor. A tela estava tratando a declaração como se fosse confere. Então jogava o item e confere. Corrigir para confere em só aceito.  
   
 

### 01:44:55

   
**Off Digital:** Confere declaração para revisão parcial ação do item virar revisão. Não abrir como aprovado. Também adicionei o teste de recreção para impedir se voltar. Tá beleza. Deixa eu dar um refresh aqui para ver como é que ele vai ficar agora, tá? Então agora ele tá dando um confere e oito parciais. Deixa eu entender porquê. Agora eu já sei como que eu vou fazer. Eu vou fazer o seguinte, eu vou tirar um  
**Marcelo Costa:** print da tela e manda para ele,  
**Off Digital:** print.  
**Marcelo Costa:** né?  
**Off Digital:** Olha só, eh, nesse print que eu te enviei e a validação do motor do Certify MVP, que é a versão antiga. Ele classificou os documentos dessa forma. Você tem aí no status o que confere o que tá parcial e pendente é quando o documento não foi enviado. Então, teoricamente a gente não teria esse documento na base e ele tá entrando como parcial agora e entrou como confere na última. Então eu preciso que você faça aí uma auditoria e um cruzamento minucioso entre esse resultado e o que a gente tem na base de fato. Me explique aí eh item a item, o que a gente tem, o que a gente não tem, o que confere, o que não confere, o que tá pendente e por quê.  
   
 

### 01:46:54

   
**Off Digital:** Sì. aqui. Calma aí. Cadê aquele negócio do treinamento aqui, ó? Ele falou aqui, ó, para mim, só para você saber, aquele outro negócio lá que a gente tava vendo, ó. Marca, achei os links e a leitura ficou assim. Existe link público para alguns conteúdos, mas o catálogo Elix My Drake é fechado pro login. Não encontrei uma página pública, tal, tal, tal. o treinamento procurar assistir e garantir quase certamente é o assiste e achure tem treinamento público da SAP Together e e Learnha de Fogo confirmado como tema campanha da da Elix line of Fire também aportar o público com os materiais pense na segurança do processo bate com process saf programa material do Welless Safety ligado a Shell Indústria. Não achei vínculo público com Helix. Teste de gás autorizado. Bate com autoriz gás teste o padrão Opito 9240 aparece certificação externa não curso elix público e aí eu ma é o portal app tal tal tal tal tal tal tal tal tal. Então já dá para entender que, cara,  
**Marcelo Costa:** É, mas não é um padrão.  
**Off Digital:** ah,  
**Marcelo Costa:** Cada um cria e bota lá e tal. Não, talvez tenha um padrãozinho, mas não é. A gente vai ter que construir um a um aí nesse caso, né?  
   
 

### 01:48:47 {#01:48:47}

   
**Off Digital:** É, velho, pedir pro cliente o documento, a gente imputar um por um, fazer uma análise e e imputar no  
**Marcelo Costa:** Вот  
**Off Digital:** sistema. Beleza? Vamos ver aqui então. Motor 2.0. Vamos só entender aqui como é que tá essa. Bom, é isso aí, priminho. Você você já já viu aí onde o onde a gente tá eh agora é realmente a gente fazer na prática entender os probleminhas e ajustando, né? que eu acho que não passa de um dia pra gente fazer isso. Aí eu não sei se você quer, se você quer manter com Marcelo,  
**Marcelo Costa:** É,  
**Off Digital:** você quer jogar um dia paraa frente, você quer garantir  
**Marcelo Costa:** eu eu prefiro que a gente mate do que mostrar e depois isso aqui vai ficar Tá,  
**Off Digital:** isso.  
**Marcelo Costa:** vai ficar, cara, segura aí, já tá tá rodando com outro até agora e velho.  
**Off Digital:** Exato.  
**Marcelo Costa:** Entendeu? Porque senão eu fazer duas reunião para fazer uma,  
**Off Digital:** Exato. É.  
**Marcelo Costa:** entendeu?  
**Off Digital:** E tipo assim, não tem porquê. O negócio já tá filé. Agora é mais essas essa essas afinadas aí de motor mesmo que vai ter que  
**Marcelo Costa:** É,  
**Off Digital:** afinar,  
**Marcelo Costa:** não tô com não tô com pressa disso.  
   
 

### 01:50:02 {#01:50:02}

   
**Off Digital:** entendeu?  
**Marcelo Costa:** Agora veja aí, priminho, se você quiser eh a hora que for, você quiser me a gente monta uma matriz, você também me libera para eu subir um candidato e ir testando aqui, porque beleza, mexendo e apertando os botão,  
**Off Digital:** É diferente.  
**Marcelo Costa:** o cara vai vendo também onde onde ô isso aqui podia,  
**Off Digital:** Lógico,  
**Marcelo Costa:** esse botão tá para cá,  
**Off Digital:** lógico,  
**Marcelo Costa:** tá para lá e tal.  
**Off Digital:** lógico,  
**Marcelo Costa:** Mas vê a hora que tiver conectado tudo aí,  
**Off Digital:** lógico.  
**Marcelo Costa:** você fala: "Tá, agora  
**Off Digital:** É, falta pouco para mim.  
**Marcelo Costa:** dá.  
**Off Digital:** Tem, eu acho que um, só falta é um 10% aí que tá de botão que ainda tá desligado, de coisinha. É, é muito essa aba aqui agora, ó. que tem que trabalhar lógico.  
**Marcelo Costa:** Eu  
**Off Digital:** O que que é? Ops. Eh, é mais essa parte aqui. Cadê? Você tá vendo o code aí?  
**Marcelo Costa:** tô vendo outra parada, acho.  
**Off Digital:** Essa parte aqui é a parte que mais tem que trabalhar, essa essa aba como um todo para mostrar os os pendentes que não tá mostrando. Esse negócio da IA tem que ligar para ele ficar e é de verdade. Essas coisas aqui tem que funcionar, esses botões tem que funcionar.  
   
 

### 01:51:18

   
**Off Digital:** Eh, aí tem que testar o documentos pessoais, a aba de formulário. Então, essa parte aqui tem que tirar um dia só para trabalhar essa parte. O resto, velho, eu já tá tudo filé. O Camban tá funcionando, já tá lincando com  
**Marcelo Costa:** É, beleza.  
**Off Digital:** empresas.  
**Marcelo Costa:** A parte de user experience aí tá bala. Agora a gente ir testando o motorzinho aí para ver o bichinho e botando esses guard raio aí para ele para ele entender, né?  
**Off Digital:** Exato.  
**Marcelo Costa:** Ó, vou te mandar os pontos que eu levantei aqui,  
**Off Digital:** Ja.  
**Marcelo Costa:** só para não esquecer, que é o nome, aquela trava do nome, renome do documento, mostrar o motivo parcial do candidato, dentro do candidato, checagem de assinatura. Eu vou terminar de escrever aqui o que que precisa e eu te enviar uma lista, uma declaração, logo da MDE e aquele outro que tem Qode. Eu te mando aí,  
**Off Digital:** Como é que você faz hoje com QR code lá?  
**Marcelo Costa:** hã,  
**Off Digital:** Como é que tá fazendo hoje com QR code?  
**Marcelo Costa:** eu leio ele e dou um valido nele, sem validade, sem nada. E os caras se vira para para olhar lá depois esse documento exclusivo é um documento. Então, velho, nem me preocupo com isso aqui agora também.  
   
 

### 01:52:36

   
**Marcelo Costa:** Vamos manter assim, vamos deixar tem muita coisinha que nós vamos nós vamos ter que ajustar no motorzinho, bá bá. Depois a gente deixa para um segundo momento,  
**Off Digital:** Exatamente.  
**Marcelo Costa:** velho.  
**Off Digital:** Outra coisa, até para ter coisa para mexer depois, porque não dá para entregar o produto para falar, tá  
**Marcelo Costa:** É, nunca nunca é 100%, né?  
**Off Digital:** 100%,  
**Marcelo Costa:** é que tipo, esse é como se fosse assim, né? Esse é uma é uma segunda versão de um que tava funcionando. Então o cara sempre tá esperando que esse vai vir funcionando mais do que o outro,  
**Off Digital:** exatamente.  
**Marcelo Costa:** né? Só que agora,  
**Off Digital:** Mas, mas é um,  
**Marcelo Costa:** só queou totalmente o conceito,  
**Off Digital:** mas é um salto,  
**Marcelo Costa:** né, velho? né? Outro produto,  
**Off Digital:** é um salto quântico,  
**Marcelo Costa:** não é mais o mesma  
**Off Digital:** né, velho? E outra coisa, o cara não entende o que tava rolando por trás.  
**Marcelo Costa:** coisa.  
**Off Digital:** Não adianta você falar para ele, p\*\*\*\*, velho, porque agora eu não tenho um emaranhado de coisa aqui e falar pro  
**Marcelo Costa:** Ah, mas eles, o Marcelo em si sabe, né? O resto dos caras é que não. Mas eu acho que a gente tem que testar o máximo.  
   
 

### 01:53:26 {#01:53:26}

   
**Off Digital:** car.  
**Marcelo Costa:** Tem documento suficiente pra gente testar e deixar ele filezinho. Eu quero só botar pr os caras usar. Nem falar, cara, vai demorar mais 10 dias, beleza, 10 dias. Mas eu, a gente entrega pros caras rodando. Eu quero que eles testem a o que eu falar assim, put, isso aqui vai ser acaso. Agora o que eu sei onde que pode dar pau, a gente tem um monte de documento. Vou testar,  
**Off Digital:** É  
**Marcelo Costa:** testar, testar até falar assim, cara,  
**Off Digital:** lógico.  
**Marcelo Costa:** para mim tá 100%, o que sair fora aqui é coisa que eu não vi. E aí deixar isso pros caras,  
**Off Digital:** Sim.  
**Marcelo Costa:** não deixar o grosso pros caras limpar,  
**Off Digital:** Não, até porque, velho,  
**Marcelo Costa:** porque senão  
**Off Digital:** a gente não quer entregar um negócio f\*\*\* para ficar escutando. Ah, pô, isso aqui, aquilo ali.  
**Marcelo Costa:** é é o e  
**Off Digital:** Pelo contrário, a gente quer entregar um negócio pros caras falar: "Meu, meu Deus do céu, velho, tá doido".  
**Marcelo Costa:** o Marcelo me falou outro dia aqui que ele falou: "p\*\*\*\*, dei uma comida de raba nos caras aqui porque eles não estavam usando". Ou seja, porque o nosso também tem tá dando uns pauzinhos, não sei o quê.  
   
 

### 01:54:25

   
**Marcelo Costa:** O cara tem, ah, uns negócios menorzinho,  
**Off Digital:** Aham.  
**Marcelo Costa:** melhor eu fazer na mão. Então, aí já começa a ficar ruim, né,  
**Off Digital:** Aham.  
**Marcelo Costa:** o cara olhar, falar: "Ó, tá fazendo na mão, p\*\*\*\*, tá pagando a solução e fazendo na mão". Então, mas é isso aí.  
**Off Digital:** Sim.  
**Marcelo Costa:** Vamos, vamos pro pau para mim. Tá, ficou tá maravilhoso, velho. O negócio tá  
**Off Digital:** Beleza. Vamos, vamos entender agora. Eu também, velho, tava curioso para chegar do Zé,  
**Marcelo Costa:** f\*\*\*.  
**Off Digital:** falar: "Velho, vamos criar o candidato, vamos criar a vaga, vamos criar a empresa, entendeu? Vamos subir a matriz, vamos subir os documentos, vamos arrastar o cara, vamos ver se tudo mexe, entendeu? Agora aí que começa, né? Aí que começa.  
**Marcelo Costa:** É, começa os detalhinhos,  
**Off Digital:** E aí você vai sentindo,  
**Marcelo Costa:** velho.  
**Off Digital:** vai falando: "p\*\*\*, isso aqui também, isso aqui não, isso aqui não era para tá aqui, né? Isso aqui é melhor,  
**Marcelo Costa:** É.  
**Off Digital:** pô, tá faltando um botão aqui, entendeu?  
**Marcelo Costa:** Eh, mas eu acho que pensando no mais simples, mais fácil da gente detectar onde tá os gapzinhos, é, em vez de importar tudo essa doideira que veio 200 documentos e aí você não sabe da onde que p\*\*\*  
   
 

### 01:55:22 {#01:55:22}

   
**Off Digital:** Aham.  
**Marcelo Costa:** isso aqui e a gente ficar puxando da onde o cara puxou,  
**Off Digital:** Aham.  
**Marcelo Costa:** é uma matriz sobe um cara,  
**Off Digital:** Aham.  
**Marcelo Costa:** opa,  
**Off Digital:** Uhum.  
**Marcelo Costa:** NR deu isso aqui, opito deu isso aqui.  
**Off Digital:** Uhum.  
**Marcelo Costa:** Aí fica mais fácil da gente identificar onde tá  
**Off Digital:** Deixa eu garantir aqui hoje aqui se se já tá 100% a criação da  
**Marcelo Costa:** Ah.  
**Off Digital:** matriz. Deixa eu criar aqui nome da empresa. É, na verdade isso aqui eu já sei que tá 100% sim. Nome da empresa, adicionar documento. É, tá 100% sim. Só que o que eu acho é que ele não tá puxando da base aqui ainda. Tá vendo que tem poucas NRs? Ó, ele não tá puxando da nossa base,  
**Marcelo Costa:** Não tá puxando, né? Não tem tudo aí  
**Off Digital:** não. Então é isso, cara. É essas coisas,  
**Marcelo Costa:** não.  
**Off Digital:** entendeu? Tipo, ele já tá aqui, ele já tá aqui no no na base, mas ele não tá na matriz.  
**Marcelo Costa:** Mas cadê a base toda aí, NR?  
**Off Digital:** A base toda tá aqui,  
**Marcelo Costa:** Vamos lá.  
**Off Digital:** ó.  
   
 

### 01:56:23 {#01:56:23}

   
**Off Digital:** MR 194 documentos,  
**Marcelo Costa:** Vai.  
**Off Digital:** ó.  
**Marcelo Costa:** Ah, tá no próximo.  
**Apresentação de Off Digital:** Oké,  
**Marcelo Costa:** Então ele não tá ele não tá liberando essas para você puxar pra matriz. Então não tá  
**Off Digital:** Exato. Ele não tá linkando, não é nem liberando, ele não tá linkando.  
**Marcelo Costa:** trelando.  
**Off Digital:** Isso é tudo coisa de rota interna no super base. É só falar, velho, a base, a biblioteca, a base tem que alimentar as matrizes. Ele vai falar na hora vou fazer o pum, feito. Entendeu?  
**Marcelo Costa:** É.  
**Off Digital:** Então é coisa que,  
**Marcelo Costa:** E esse é  
**Off Digital:** tipo assim, é muita coisa, né, velho? Você tá criando a base, aí você pensa:  
**Marcelo Costa:** o  
**Off Digital:** "Cara, agora eu preciso dessa base dentro do software, que foi o que eu fiz. Só que eu não pensei, tá, agora tem que ligar essa base na matriz, entendeu? É, é um porqu a menos. Aí quando você vai lá na hora de criar a matriz,  
**Marcelo Costa:** É,  
**Off Digital:** você fala: "p\*\*\*, não tá lincando com a base".  
**Marcelo Costa:** não tá puxando  
**Off Digital:** É, mas é isso aí, priminho. Esse esse é o trampo mesmo artesanal aqui o negócio,  
   
 

### 01:57:14

   
**Marcelo Costa:** é boa.  
**Off Digital:** ó. Você viu? Ficou agora os botão ficou transparente. Você viu aqui, ó?  
**Marcelo Costa:** Ah,  
**Off Digital:** Lembra que tava pretinho?  
**Marcelo Costa:** entendi. O transparente ele só faz o Deixa eu jogar ele no Mac  
**Off Digital:** É, ele ficou muito mais clean, ó.  
**Marcelo Costa:** aqui. É,  
**Apresentação de Off Digital:** Er  
**Off Digital:** Entendeu,  
**Marcelo Costa:** saiu de cara de IA, né? De negocinho produtinho feito com IA,  
**Off Digital:** né? Clean para c\*\*\*\*\*\*.  
**Marcelo Costa:** né?  
**Off Digital:** Clean para c\*\*\*\*\*\*. Bem bem Mac, né?  
**Marcelo Costa:** É  
**Off Digital:** E é legal que ele ele tá de um jeito que ele vai transpor legal no Windows,  
**Marcelo Costa:** top.  
**Off Digital:** porque eu acho que os caras vão trampar bastante no Windows lá, né?  
**Marcelo Costa:** 90  
**Off Digital:** É, então eu tô pensando nisso.  
**Marcelo Costa:** 99%.  
**Off Digital:** Tô Por isso também que eu quis dar um acabamento diferente para para não ficar um negócio muito Mac, porque no Mac é uma delícia, né? Agora aí quando você vai pro inolzão, então,  
**Marcelo Costa:** Tem que ver como é.  
**Off Digital:** então beleza, velho. Então ganha mais um ganha mais um tempinho aí. Vamos fazendo isso, cara. Não adianta a gente botar esse deadline porque é coisa que a gente vai mexendo e vai e vai sentindo, né?  
   
 

### 01:58:26 {#01:58:26}

   
**Marcelo Costa:** É boa. Bom, veja aí o que você precisar de mim,  
**Off Digital:** Beleza. Amanhã, amanhã,  
**Marcelo Costa:** priminho. que a hora que você falar,  
**Off Digital:** amanhã a gente segue aí,  
**Marcelo Costa:** ó, dá para testar, vamos ver se a gente faz esse  
**Off Digital:** velho.  
**Marcelo Costa:** caminho.  
**Off Digital:** Amanhã a gente segue. Eu acho que a gente agora tem que ter esse encontro diário aí com esse  
**Marcelo Costa:** Cortou aqui, primo.  
**Off Digital:** gás.  
**Marcelo Costa:** Cortou. Deu uma cortada, deu uma cortada aqui. Se falar amanhã a gente  
**Off Digital:** Deixa eu parar o compartilhamento para ver se melhora aqui.  
**Marcelo Costa:** segue.  
**Off Digital:** Eu acho que agora a gente tem que ter um encontro todo dia pra gente dar um gás aí nessa reta final. Então amanhã a gente já deixa um horário aí,  
**Marcelo Costa:** Sim,  
**Off Digital:** esse mesmo horário do meio-dia eu acho que é bom.  
**Marcelo Costa:** tá, eu tenho só essa questão, né? 1:30 eu levo ao bebê. Então eu dou  
**Off Digital:** Não, não tem problema. A gente para até a hora de eu paro para almoço também.  
**Marcelo Costa:** essa,  
**Off Digital:** Então vamos deixar esse horário e vamos aí todo dia. Se amanhã já não tiver, eu acho que amanhã já tá pronto pro teste, velho.  
   
 

### 01:59:30 {#01:59:30}

   
**Off Digital:** Eu já vou fazer isso aqui, já vou delegar para ele fazer um V3 sem dado nenhum pra gente abrir o negócio  
**Marcelo Costa:** é,  
**Off Digital:** clean.  
**Marcelo Costa:** mete um Z3 sem dado nenhum pra gente já falar, ó, e vincula esses documentos da matriz e vamos fazer um passo real mesmo, ó. Vamos criar a matriz. Pá, pá,  
**Off Digital:** Exato,  
**Marcelo Costa:** pá, pá. E aí a gente vai ver os onde vai tá aí.  
**Off Digital:** exatamente,  
**Marcelo Costa:** Show de bola.  
**Off Digital:** exatamente. E aí a gente já fica aqui na call mesmo resolvendo,  
**Marcelo Costa:** Sobre mim. Tá bom,  
**Off Digital:** entendeu?  
**Marcelo Costa:** fechado.  
**Off Digital:** Bele,  
**Marcelo Costa:** Eu vou mandar para  
**Off Digital:** mas falta pouco, prima. p\*\*\*\*,  
**Marcelo Costa:** você.  
**Off Digital:** eu tô louco para botar isso pros caras funcionar também, velho, de falar, p\*\*\*\*, velho, agora é  
**Marcelo Costa:** Não, ó, eu nem eu é daquele jeito.  
**Off Digital:** só  
**Marcelo Costa:** Eu nem tô eu nem tô ansioso, tá ligado? Tá, eu sei que vai, eu sei que o bagulho vai ser velho, o que os caras tão acostumado aqui, eh, o cara vai olhar e outra,  
**Off Digital:** sim.  
**Marcelo Costa:** e até o Marcelão é o cara tem cabeça de negócio, né, velho?  
   
 

### 02:00:23 {#02:00:23}

   
**Marcelo Costa:** O cara vai olhar, vai falar, c\*\*\*\*\*\*. Aí eu tô até pensando uma coisa que nós não falamos, é, nós vamos mostrar pro Marcelo e e não falamos com a Dávio, né? Porque eu não vejo ainda assim,  
**Off Digital:** Sì.  
**Marcelo Costa:** eu não vejo como é bom, o ADW conhece da de sufabez e o c\*\*\*\*\*\*. Acho que eu não sei em que momento a gente bota ele nessa nessa parada, né? O cara às vezes não sentir que, sei lá, acho que não tem nem não tem problema. Se ele sentir, ele sente o que ele quiser também. Mas o aqui em que momento eu boto o cara, né? Que momento  
**Off Digital:** Cara, eu acho que validou com Marcelo decidiu que vai botar para rolar,  
**Marcelo Costa:** seria?  
**Off Digital:** aí ele já tem que aí pode fazer uma reunião com ele, falar: "Ó, velho, a gente pegou o aval do Marcelo porque não adianta ficar passando item a item com você". chegar lá, o Marcelo não aprova que é isso, que é aquilo diferente, a gente tem que mexer de novo. Então, aprovamos com o Marcelo e agora estamos sentando para te passar o produto aqui. Os caras já vão entrar em uso e como é que a gente pode contar com você no dia a dia paraa manutenção?  
   
 

### 02:01:31 {#02:01:31}

   
**Off Digital:** Então, ah, p\*\*\*\*, velho, tem uma um negócio aqui que tá endereçando pra vaga que era para tá mandando para candidato. Ah, p\*\*\*\*, tem uma matriz aqui que tem que criar não sei o quê. Tudo velho. Tudo ele que vai ficar com a bola. É o único, é o único sentido que faz de,  
**Marcelo Costa:** Eh,  
**Off Digital:** de, de, de, de, de de daqui paraa frente, né? Ou o que que você  
**Marcelo Costa:** é, é, eu acho que só pensar no tipo ele,  
**Off Digital:** acha?  
**Marcelo Costa:** eu ele não tem ideia que nós estamos fazendo tudo isso, né? Porque inicialmente eu falei pro cara,  
**Off Digital:** Aham.  
**Marcelo Costa:** ó, não passei para um brother aqui que que trampa com processo, caramba, e tá mexendo aqui, p\*\*\*\*, criando umas estruturas legal aqui. Aí fala, não, montamos um. Então, às vezes o cara não tá esperando que, p\*\*\*\*, o cara fizeram um produto novo, não falaram nada, agora chega aqui, quanto eu quero só para fazer a manutenção, né? Então assim, a minha conversa com ele sempre foi, ó,  
**Off Digital:** Ага.  
**Marcelo Costa:** você é meu sócio aqui nessa parada aqui, estamos junto aqui e tal, né? Eh, então eu tô, talvez a gente faça uma, vamos dizer assim, eh, pensando meio que assim, consultiv, ô, vem aí, ó, o que nós fizemos, velho.  
   
 

### 02:02:45 {#02:02:45}

   
**Marcelo Costa:** Nós mexemos nisso aqui, estruturamos assim marca de processo, pegamos o STCW. Hoje é a nossa conversa inicial, mapeamos linha a linha do processo, que que é qual? Porque isso ele não fez e e era o que eu espero. Tipo, você manja daí,  
**Off Digital:** Ага.  
**Marcelo Costa:** ah, você vai atrás da regra, tal, não sei o quê. p\*\*\*\*, isso que você fez para mim é onde tá o maior eh valor do negócio que ele não parou para fazer. Então, isso que eu quero demonstrar para ele,  
**Off Digital:** Sì.  
**Marcelo Costa:** porque o front, beleza, o front até o cara na Iá, o cara vai, se vira, manda fazer, não sei o quê. Beleza, agora esse motor depende do que você fez, que foi emergir na parada. Cara, o cara emergiu no processo para entender por que bate, por que não bate, fez uma auditoria, não sei o quê. Então isso vale muito mais para mim para mostrar para ele, para falar assim, ó, o peso que o cara chegou e e falar, p\*\*\*\*, beleza. Aí o front, p\*\*\*\*, já veio o front junto aqui, mas tá aqui, isso aqui foi o peso. Olha o que nós fizemos,  
**Off Digital:** Não. E e p\*\*\*\*,  
   
 

### 02:03:45 {#02:03:45}

   
**Marcelo Costa:** eu tenho certeza.  
**Off Digital:** e e o ponto principal que que começou a conversa não é nem o fronte e não é nem o peso do trabalho completo de de entrar no negócio, é tirar vocês do NM. Aí o cara já tinha ter,  
**Marcelo Costa:** É,  
**Off Digital:** o cara já tinha que ter tido a proatividade assim, pelo amor de Deus, mano. Não tô querendo eh eh botar um dedo pro cara que eu nem conheço,  
**Marcelo Costa:** não.  
**Off Digital:** muito pelo contrário, porque eu já entendi que ele é ponta firme e e primo,  
**Marcelo Costa:** Sim.  
**Off Digital:** nesse negócio aqui, eu nem quero dar muito pitaco no sentido de como é que vai ser o modelo de negócio, porque um é um negócio que você criou,  
**Marcelo Costa:** Да.  
**Off Digital:** eu tô eu tô entrando somando, eu tô botando antes, então eu tô entrando tipo investindo, eu tô investindo meu tempo e e minhas habilidades no negócio que eu sei que eu confio para onde você pode levar a gente dentro desse negócio. E quem vai ditar nesse negócio até então dentro desse produto específico, como é que funciona? É você. E eu confio exatamente em como você vai direcionar, seja de composição, seja de crescimento do negócio, eu confio 100%.  
**Marcelo Costa:** Sì.  
**Off Digital:** Então não eu não quero ficar impondo nem dando opinião, eh, vamos dizer, opinião com peso em nada, mas assim, a minha forma de pensar é, p\*\*\*\*, nós já estamos há um ano aonde você consegue fazer as paradas com cloud muito bem feito e tal.  
   
 

### 02:05:10 {#02:05:10}

   
**Off Digital:** Eh, e seria legal ter tido uma preocupação do lado dele de falar, p\*\*\*\*, vamos fazer um sprint aqui para tirar a gente desse motor barulhento de p\*\*\*\* de fiar para cá, fiarada para lá. E aí eu entendo o cara ser pai de família e tá correndo atrás das contas e tá atolado lá no trampo dele e saber que dá um trampo é uma pica. Não é um negócio assim que você faz também, tipo, ah, sento ali e e estralo os dedos, mas tem que  
**Marcelo Costa:** É, mas mas o seguinte, primo, além disso, além disso,  
**Off Digital:** fazer.  
**Marcelo Costa:** eh, e onde que é o onde eu acho que eu assim, tô trilhando aqui, abrindo com você, como é o caminho que eu tô pensando com o cara para também deixar o cara confortável e e e ele ele reconhecer que falar: "p\*\*\*, velho, virei 10% do negócio, entendeu? Eu quero que ele tenha essa percepção,  
**Off Digital:** Sim.  
**Marcelo Costa:** mas não eu falando: "Ó, você tem 10 porque o cara fez isso? Eu quero mostrar para ele, porque eu sei que ele não tem a capacidade de de  
**Off Digital:** Aham.  
**Marcelo Costa:** organização e de chegar no detalhe do detalhe, porque ele é um cara de N8N, velho. Até hoje você pode falar.  
   
 

### 02:06:19

   
**Marcelo Costa:** Outro dia eu tava, quando eu eu tava trocando ideia com ele, eu tava falando de Open Cloud, ele ah, velho, isso aí você faz no N8N,  
**Off Digital:** Aham.  
**Marcelo Costa:** não sei o quê.  
**Off Digital:** Tem o saudosismo ali, né?  
**Marcelo Costa:** Então você falar, ó,  
**Off Digital:** Entendi.  
**Marcelo Costa:** saímos do N8N para ele, ele vai falar, p\*\*\*\*, velho, saiu do que eu domino a minha vida inteira.  
**Off Digital:** Aham. Entendi, entendi.  
**Marcelo Costa:** Então,  
**Off Digital:** É, não tinha  
**Marcelo Costa:** eu prefiro ir pro lado e falar assim pro cara, velho, olha aqui as normas, sabe onde tava dando pau? Porque a gente não categorizou ou a a reunião quando você me mostrou ali,  
**Off Digital:** pensado  
**Marcelo Costa:** cara, olha isso aqui, fiz a categorização, agora a gente entende. Quando você mostrar isso, o cara vai falar, cara, ele não tinha nem a capacidade de se falar, tira 100% do seu tempo e vai olhar ele. Não, eu, eu acho que ele não faria isso porque entra muito em modelo de negócio, entendeu? Então, a gente mostrando isso para ele, eu vou conseguir deixar explícito que ele virou 10% do negócio e que eu tô deixando  
**Off Digital:** Total. Não. E essa é uma reunião e e essa é uma reunião que eu acho que você tem que fazer com a você.  
   
 

### 02:07:15 {#02:07:15}

   
**Marcelo Costa:** ele  
**Off Digital:** Você vai ter o acesso de supervisor, você dá um acesso para ele e você troca esse essa ideia com ele, apresenta o produto, troca a ideia com o cara aberto, deixa ele falar o que ele quiser, chega numa conclusão com ele e aí depois dessa conclusão você faz uma reunião para apresentar a gente. Fala aí,  
**Marcelo Costa:** É lógico.  
**Off Digital:** ó, com a data.  
**Marcelo Costa:** No no no último ponto, primo, assim, eu sou o dono da parada, eu sou o dono do cliente, eu sou o dono da da ideia, tal. O cara foi um cara que eu trouxe e então. Então assim, eu tenho o poder de falar: "Va a chave aqui". Pu tô mandando minha nota, Marcelo, agora minha nota vem daqui. Mas é lógico, não é? Eh, não é isso que eu quero e eu quero que ele chegue nessa conclusão, entendeu?  
**Off Digital:** Sim,  
**Marcelo Costa:** Então vou trilhando o cara e porque é real não  
**Off Digital:** sim. E você precisa entender o posicionamento dele também, como é que o cara vai se posicionar,  
**Marcelo Costa:** tô.  
**Off Digital:** que que o cara vai se propor. Porque é o que eu tô falando, tudo questão de de de posicionamento. Se o cara chega e fala: "p\*\*\*\*, que animal, velho, pô, agora o negócio foi para outro nível, vamos fazer,  
   
 

### 02:08:16 {#02:08:16}

   
**Marcelo Costa:** Eu eu acho que quando ele vê isso,  
**Off Digital:** vamos acontecer, p\*\*\*\*".  
**Marcelo Costa:** quando ele vê isso, com certeza vai ser pela pelo que eu vi dele,  
**Off Digital:** Lógico.  
**Marcelo Costa:** ele ele vai sentir isso porque assim, eu ele não teve a cabeça que você teve de olhar pro negócio e falar: "c\*\*\*\*\*\*, isso aqui é um business grande, tem óleo e gás envolvido, cara.  
**Off Digital:** Sim.  
**Marcelo Costa:** Você me conhece há mais tempo, você sabe que eu fuço numas numas gavetas grande e tal. Então f cara aqui o cara tem uma gaveta. Ele não teve isso porque senão ele parava para olhar, velho.  
**Off Digital:** Ah.  
**Marcelo Costa:** Entendeu? Então ele não teve isso. Então para ele a gente tem mais uma solução aí velho.  
**Off Digital:** É um jovem, né?  
**Marcelo Costa:** Tem mais outras pequenininha com os parceiros e tal.  
**Off Digital:** Uhum.  
**Marcelo Costa:** p\*\*\*\*, você diferente de você que olhou e falou: "Cara, vou gastar meu tempo, vou botar meu tempo, meu dinheiro aqui, vou parar para fazer isso". Então tá claro isso, né, velho? Então não tem eh eu tenho poder de  
**Off Digital:** Beleza, não é tarde. Se o se o cara entender até que tarde e e falar, p\*\*\*\*,  
**Marcelo Costa:** conduzir,  
**Off Digital:** beleza, entendi só agora o que eu já deveria ter entendido.  
   
 

### 02:09:19 {#02:09:19}

   
**Off Digital:** É o que eu falei, velho, quanto mais a gente potencializa o negócio, melhor. Tem um cara que vai assumir várias broncas e vai entrar de cabeça na parada, velho. A gente se divide para multiplicar e  
**Marcelo Costa:** e ainda, primo, nós fizemos, nós demos um reformulada na parada que profissionalizou de um  
**Off Digital:** você  
**Marcelo Costa:** nível e e ainda dá tempo dele olhar, falar: "Cara, vou largar umas coisas e vou montar com esses caras". Porque tem,  
**Off Digital:** é o que eu tô falando.  
**Marcelo Costa:** entendeu? É isso que eu tô esperando,  
**Off Digital:** Sim,  
**Marcelo Costa:** que eu acredito que ele vai olhar e vai falar:  
**Off Digital:** sim.  
**Marcelo Costa:** "p\*\*\*\*, velho, eu achei que não ia para esse lado. Os caras fizeram um bagulho f\*\*\* que assim, ele nunca lhe deu ele ele, pelo que eu entendo assim, ele sempre deu aulinha, tal, desenvolvendo uma soluçãozinha, mas nunca nunca sentou numa empresa para ver qual que precisa ter um soque, qual que é a pressão de uma empresa grande.  
**Off Digital:** Aham.  
**Marcelo Costa:** E agora nós estamos trazendo um negócio para outro nível, velho. Então eu,  
**Off Digital:** Sim.  
**Marcelo Costa:** se eu fosse ele, eu ia parar falar: "Velho, ainda dá tempo de eu  
**Off Digital:** E foi a visão que eu tive quando você começou a me falar e me mostrar o negócio.  
   
 

### 02:10:13

   
**Marcelo Costa:** encostar  
**Off Digital:** Eu falei: "Não, velho, esse negócio tem muito mais potencial para est do jeito que ele tá, velho. Eu vou tentar botar minha mão aqui para para elevar o negócio,  
**Marcelo Costa:** eh,  
**Off Digital:** pra gente poder dar mais um passo, paraí dar mais outro passo e assim ir,  
**Marcelo Costa:** é, e assim, eu acho,  
**Off Digital:** né?  
**Marcelo Costa:** primo, que ele é um cara que esses pauzinho que vai dando, ele tem uma, ele ele conhece tempos mexendo, ele vai saber, cara, isso é LLM. Não, cara,  
**Off Digital:** Aham.  
**Marcelo Costa:** isso é super base. Cara,  
**Off Digital:** Aham.  
**Marcelo Costa:** em vez da gente ficar batendo cabeça, testando, mon falando,  
**Off Digital:** Sim,  
**Marcelo Costa:** ele já tem. Então,  
**Off Digital:** cara.  
**Marcelo Costa:** é um cara que soma,  
**Off Digital:** Total,  
**Marcelo Costa:** eu tenho certeza, cara.  
**Off Digital:** total. E e tipo assim, com certeza eu ainda vou, quando eu conhecer ele,  
**Marcelo Costa:** Então,  
**Off Digital:** eu ainda vou ter mais visão do que mais ele pode somar, fora o que você já sabe. Então assim, é só questão de você entender a postura,  
**Marcelo Costa:** eu vou conduzir, eu vou conduzir isso  
**Off Digital:** você conduzir,  
**Marcelo Costa:** da  
**Off Digital:** entender a postura do cara para você entender como ele entra na composição e quem vai tomar essa decisão é você.  
   
 

### 02:11:11 {#02:11:11}

   
**Off Digital:** Então tá tudo certo,  
**Marcelo Costa:** Sim,  
**Off Digital:** tá ligado?  
**Marcelo Costa:** sim,  
**Off Digital:** Agora eu acho que esse é o  
**Marcelo Costa:** mas eu acho que vale a gente depois eu vou preparar a hora que tiver redondinho.  
**Off Digital:** caminho.  
**Marcelo Costa:** Acho que nem preciso falar que a gente validou com o Marcelo e tal para ele não sentir que a gente talvez atravessou alguma coisa assim,  
**Off Digital:** É, faz um, troca uma ideia com o cara, faz um call com ele, mostra, mostra tudo,  
**Marcelo Costa:** mas a hora que tiver bom.  
**Off Digital:** é, mostra tudo, manda para ele mexer, entendeu? Às vezes ele mesmo acha algumas coisas que a gente ainda não achou,  
**Marcelo Costa:** Eh, é,  
**Off Digital:** então  
**Marcelo Costa:** mas eu acho que eu prefiro, eu vou trocar essa ideia e aí eu prefiro trazer que você venha para abrir a reunião que nós fizemos hoje cedo, velho,  
**Off Digital:** fala.  
**Marcelo Costa:** mostrando o compliance da parada, o que que tem por trás. Peguei toda a norma, tá aqui a norma, ó. A norma é isso aqui por causa disso. Ele lê as NRs, do que você me mandou no zap lá, ele é NNR por causa disso. Isso aí é um negócio que o cara não parou para fazer e, cara, era a minha expectativa que tinha que fazer.  
   
 

### 02:11:58 {#02:11:58}

   
**Marcelo Costa:** Então, eh, e pronto, beleza. Mas estamos, estamos definido. Isso aí tá tá simples de fazer. Era só tá alinhadinho aí.  
**Off Digital:** É, não, isso aí é problema bom, velho. Problema bom. É que importa, velho, o negócio tá evoluindo, entendeu? A gente,  
**Marcelo Costa:** É,  
**Off Digital:** você ainda nem começou a bater nas portas que que vai dar para bater, né? Isso é um V1, porque o que você tinha, primo, era um MVP, né? Agora a gente não MVP  
**Marcelo Costa:** que foi foi rodar, mas assim  
**Off Digital:** rodando. Então agora a gente tá saindo do a gente agora a gente tá indo para um MVP profissional do V1 do produto.  
**Marcelo Costa:** Isso  
**Off Digital:** Quando a gente validar depois de um mês,  
**Marcelo Costa:** aí.  
**Off Digital:** ele vai ser um V1 rodando. E aí a gente ainda vai ter um um gap aí de alguns meses pra gente profissionalizar ele realmente no nível alto, que aí é ver rodando, melhor a latência, de repente migrar um super base para um negócio mais pro, de repente, entendeu? Porque tem tipo esse modelo de super base com sko para você botar um site de PMA.  
**Marcelo Costa:** Sim,  
**Off Digital:** Quando você quer botar um negócio com a segurança mais forte para ficar mais rápido num servidor mais  
   
 

### 02:13:03 {#02:13:03}

   
**Marcelo Costa:** sim.  
**Off Digital:** f\*\*\*, aí vai entrando várias outras coisas. Então a gente vai olhar pra estrutura, depois vai falar: "Cara,  
**Marcelo Costa:** Sim.  
**Off Digital:** beleza, o negócio tá funcionando, tá bom, tá promissor, tá bonito, tá atendendo o que a gente precisa. Agora vamos começar a bater em outras portas, aí vai entrar, p\*\*\*\*. Vamos mudar de  
**Marcelo Costa:** Mas nós fizemos muito baseado na estrutura de ANVP rápido,  
**Off Digital:** novo.  
**Marcelo Costa:** saindo da solução e pau. Beleza, agora, p\*\*\*\*, a hora que,  
**Off Digital:** Sim,  
**Marcelo Costa:** né? Vai,  
**Off Digital:** sim.  
**Marcelo Costa:** mas já pensando em uma auditoria, já olhando como é que eu, p\*\*\*\*,  
**Off Digital:** Não,  
**Marcelo Costa:** catalogando os processos,  
**Off Digital:** parte de parte de parte de comprar esse parte de negócio já tá maduro,  
**Marcelo Costa:** né, velho? É.  
**Off Digital:** né? É mais é mais é mais o que eu dig quando eu falo estrutura, eu falo de estrutura técnica de de produto, código de cara depois plugar um dev para falar, cara,  
**Marcelo Costa:** Sim.  
**Off Digital:** que que tem de segurança? O que que pode vazar? Como é que o cara pode me hackear? Entendeu? Esse tipo de coisa que não vale a pena a gente olhar agora, mas,  
   
 

### 02:14:02 {#02:14:02}

   
**Marcelo Costa:** É.  
**Off Digital:** né?  
**Marcelo Costa:** E e outra e o mapeamento de todo o processo que você tem aí. O que que faz? O que? Em que momento? do desenhinho. Aquela sua primeira reunião hoje foi aquilo, velho. Ali para mim é onde tá o valor da parada, velho. Aqui não é o valor da parada,  
**Off Digital:** É que sem sem aquilo você não tem como conversar com o cara, porque o cara não é técnico nem você. E aí como é que você vai explicar que funcinho de porco você vai falar?  
**Marcelo Costa:** velho.  
**Off Digital:** p\*\*\*, mas mano, eu joguei na Ia aqui que ele montou uma básica e tal. Não, mano, tá aqui, ó, tudo que eu tenho coberto, o que não cobre, por quê, o que aprova no automático, por quê, como é que meu motor pensa? Como é que ele que a gente integra as duas coisas? Beleza, legal. O cara vai falar: "p\*\*\*\*, é isso mesmo. Validou que na prática também funciona assim, cara,  
**Marcelo Costa:** Tá boa, né?  
**Off Digital:** conversa, entendeu? Agora prendeu aqui, ó. Ele me deu aqui, eh, enquanto a gente conversava, ele me deu,  
**Marcelo Costa:** Cou  
   
 

### 02:14:52 {#02:14:52}

   
**Off Digital:** ó, tô até na hora também, mas só para te passar essa esse feedback, ó. Confirmei. O problema aqui não é só o ser. Esse caso do Laudis põe uma falha maior. A base atual tem vários PDFs reais, mas a parte da extração ficou gravada, certo? no metadata e errado barra vazia nos campos que o motor usa para decidir. Também confirmei uma coisa importante, no superabas atual, o lado si não tem nenhum item confere. O print antigo mostra cinco conferes. Então vamos lá, passando item a item. Circock, CBSN, EGPM, CAS, CPPM, CES, CER, CPSO. Resumo direto, o print antigo está mais pró resultado operacional, correto? A base atual não tem C. A base atual não encontrou CES, apesar do print antigo de Z confere. O motor atual está falhando em três pontos. Não promoveu campos extraídos do metadata para os campos estruturados.  
**Marcelo Costa:** Да.  
**Off Digital:** Não usou de forma correta os alias compostos da matriz, tipo eh, C, Esi e Esciaia. E deixou a declaração também contaminar outros da outros itens da matriz quando deveria. ter sido isolado e não substituto de documento. Próximo passo correto é fazer no hotfix dos dados para esse caso virar nosso golden test.  
   
 

### 02:16:31

   
**Off Digital:** Lud precisa fechar como confere, confere confere parcial, parcial CS pendente ou  
**Marcelo Costa:** Ela  
**Off Digital:** reimportar.  
**Marcelo Costa:** pode meter bronca, priminha. É isso mesmo.  
**Off Digital:** Mas o bom da gente tá plugado com a IA é isso, porque além dele rodar esse golden test, ele vai extrair o padrão e a gente vai replicar em tudo. Esse quero o  
**Marcelo Costa:** Isso aí. É. E aí é testando, velho, porque agora isso,  
**Off Digital:** ponto.  
**Marcelo Costa:** você vai conectar o seu diferente de um de um de construir em qualquer num love da vida, que ele quando você pede para ele trocar um botão, ele troca a conexão, ele tira de uma tomada e põe na outra. O seu tá em locais diferentes,  
**Off Digital:** Aham.  
**Marcelo Costa:** então você tem que pedir para tirar a tomada daqui e você ir botar lá. E aí, velho, às vezes não botou essa tomada, né? Então é é isso que ele  
**Off Digital:** Sim. Mas o bom, o bom é que depois que o produto tiver redondo, a gente consegue consolidar e criar um manual de  
**Marcelo Costa:** He.  
**Off Digital:** manutenção. Ou seja, cara, toda vez que eu te imputar isso, você precisa conferir isso, isso, isso, isso, isso, isso, isso, isso.  
   
 

### 02:17:50

   
**Off Digital:** A regra é isso, a regra é aquilo, entendeu? Aí você consolida. Agora ele não tá consolidado porque, cara, toda hora mudando de layout, toda hora mudando o nome de botão, toda hora tirando um botão daqui, botando aqui. Então, não adianta você consolidar.  
**Marcelo Costa:** É isso aí, velho. É, é a forma de construindo,  
**Off Digital:** Entendeu?  
**Marcelo Costa:** né, velho?  
**Off Digital:** Não. E deve deve é isso, né, velho?  
**Marcelo Costa:** Tem  
**Off Digital:** Você imagina o cara lá no terminal fazendo no código lá, velho. Você acha que o cara sobe um negócio já igual no loambadinho, bonitinho?  
**Marcelo Costa:** não, não,  
**Off Digital:** É,  
**Marcelo Costa:** velho.  
**Off Digital:** velho.  
**Marcelo Costa:** É, p\*\*\*\*,  
**Off Digital:** O cara é,  
**Marcelo Costa:** hoje em dia,  
**Off Digital:** entendeu?  
**Marcelo Costa:** hoje em dia o bagulho tá muito mais fácil para fazer,  
**Off Digital:** É isso.  
**Marcelo Costa:** né?  
**Off Digital:** É isso. Então, mas mas beleza, priminho. Vamos,  
**Marcelo Costa:** Imagina que isso aqui,  
**Off Digital:** vamos aí.  
**Marcelo Costa:** eh, você tem você tem os cara, o dev, o dev de back, velho. Então, além de ter que mandar pro outro, você manda para outro cara.  
   
 

### 02:18:37

   
**Marcelo Costa:** E aí virava uma briga do cara do front falando: "Velho, o cara mandou os dados errado, velho. Os dado não sei o quê, velho. Aí é, p\*\*\*\*,  
**Off Digital:** E aí dentro do back você tem cinco,  
**Marcelo Costa:** p\*\*\*\*\*\*.  
**Off Digital:** seis caras e dentro do front cinco, seis cara, entendeu? Então você tem lá o dev, você tem o cara que só roda QA, que é os testes, você tem o cara que escreve, você tem o cara que só mexe com com credencial, com hospedagem,  
**Marcelo Costa:** né?  
**Off Digital:** com  
**Marcelo Costa:** E é complexo. E é por isso que os caras tão ficando louco,  
**Off Digital:** servidores.  
**Marcelo Costa:** que ele fala: "Velho, a gente não, os caras nunca imaginaram que o bagulho tão complexo do que eles sabiam fazer ia ficar tão fácil, né, velho?" E uns carinhas, uns dev, tem uns devzinho que eu vi outro dia, o cara, velho, o bagulho tá muito louco,  
**Off Digital:** Exatamente.  
**Marcelo Costa:** realmente. Antes eu achava que eu não ia perder meu emprego, agora eu já perdi. Por sorte eu tô olhando isso aqui como uma oportunidade e tô aprendendo. Mas assim, o que eu sabia fazer, esquece, velho. Acabou.  
   
 

### 02:19:28

   
**Marcelo Costa:** Então é doideira, né?  
**Off Digital:** Que  
**Marcelo Costa:** Nós pegamos os cara,  
**Off Digital:** louco.  
**Marcelo Costa:** raspamos os cara no meio do caminho, né, primo?  
**Off Digital:** Porque hoje, mano, você só precisa ter tempo, porque assim, você vai resolver, mas se você não for pro caminho certo, você vai dar volta. Então, esse é que é o lance. Então, assim,  
**Marcelo Costa:** É,  
**Off Digital:** quanto volta você vai dar, é o que vai diferenciar quem tem velocidade e quem não tem. Por exemplo, eu eu passei por três frontes para chegar no que a gente tem hoje.  
**Marcelo Costa:** mas com certeza no seu próximo desenvolvimento você não vai fazer isso.  
**Off Digital:** Exatamente. Então, assim, por quê? Porque eu achei que o motor era tão importante que eu ia fazer o motor inteiro primeiro e depois eu ia fazer o front, que o fronte não era tão importante. Tava, tava errado meu pensamento? Não, mas eu fui muito muito curto aqui em olhar pro pra parada isso, porque primeiro eu tive que ter desenhado a experiência para fazer um aire frame de como ia ser o uso do do do produto para criar o motor pensado no uso.  
**Marcelo Costa:** Cara, não, eu não sei porque eu acho que o motor era o mais importante do que precisa validar depois. Era,  
**Off Digital:** É, mas assim,  
   
 

### 02:20:43

   
**Marcelo Costa:** é que é meio,  
**Off Digital:** mas o,  
**Marcelo Costa:** p\*\*\*\*, meio junto, né?  
**Off Digital:** mas o motor ele é determinístico. Como é que você vai plugar o motor a experiência? Primeiro você tem que saber a  
**Marcelo Costa:** É, mas pensando,  
**Off Digital:** experiência.  
**Marcelo Costa:** p\*\*\*\*, para mim o importante você falar assim, ó, eu vou eu vou jogar os certificados aqui, ele vai empendendo o motor, vai me devolver uma planilha,  
**Off Digital:** Aham.  
**Marcelo Costa:** já resolve a vida dos caras lá.  
**Off Digital:** Sim, sim, sim,  
**Marcelo Costa:** E nunca ninguém resolveu isso.  
**Off Digital:** sim.  
**Marcelo Costa:** Jogar numa planilha com confere, não confere, tudo na mesma ordem, desnomeado,  
**Off Digital:** Aham.  
**Marcelo Costa:** porque que p\*\*\*\* só na linha já é p\*\*\*\*.  
**Off Digital:** Aham.  
**Marcelo Costa:** Aí é o motor só trabalhando, falando, cara, vê a regra, vê se bate. Isso aí para mim é coraçãozão.  
**Off Digital:** Uhum.  
**Marcelo Costa:** Aí depois o resto vai vindo perfumaria,  
**Off Digital:** Sim.  
**Marcelo Costa:** um monte de coisa que aí vai facilitando mesmo a vida do cara, né? Bateu o  
**Off Digital:** É, mas aí a a gente a gente entra no ponto, velho, do profissional. Então o profissional ele tem que atender tudo.  
   
 

### 02:21:31 {#02:21:31}

   
**Marcelo Costa:** olho.  
**Off Digital:** Por mais que o seu o seu apelo ele seja o motor, fala: "Beleza, velho, o esse negócio é o motor, é o compli, é a certeza, beleza? OK. Só que para ele ser profissional, o visual vai ter que tá alinhado,  
**Marcelo Costa:** Sim.  
**Off Digital:** os botões vão ter que vai ter que tá tudo certinho, tudo com a nomenclatura certa, senão o cara bate o olho, ele não vê esse profissionalismo, entendeu? Você tá lá com o motor for,  
**Marcelo Costa:** É,  
**Off Digital:** vai falar: "Pô, velho, beleza, mas, pô, mas parece só uma solução caseira". Tá,  
**Marcelo Costa:** aí você manda na no Excel para mim,  
**Off Digital:** mas você fala,  
**Marcelo Costa:** aí fodeu,  
**Off Digital:** entendeu? Aí você fala: "Pô, beleza,  
**Marcelo Costa:** né?  
**Off Digital:** mas lá no break o negócio é pré-histórico, tal. É beleza, velho. Mas os caras começaram na época pré-histórica, eles só não se atualizaram. Eles não se atualizaram, mas eles começaram. Na época que eles começaram, provavelmente o bagulho deles era hightech. Se a gente quer ganhar notoriedade,  
**Marcelo Costa:** Com certeza tem que  
**Off Digital:** a gente tem que ter o diferencial.  
   
 

### 02:22:32 {#02:22:32}

   
**Off Digital:** Qual que é o diferencial?  
**Marcelo Costa:** vir compliance visual,  
**Off Digital:** Qual que é o diferencial? É a plataforma. Se você olhar a plataforma Exato.  
**Marcelo Costa:** né?  
**Off Digital:** Não é porque é bonitinho, porque não é porque o cara tem que olhar, velho, e agregar valor. Isso aqui é o que faz valer dinheiro. Você pode falar que o motor é f\*\*\*, mas se o visual for tosco, o cara não vai valorizar, velho.  
**Marcelo Costa:** Ja.  
**Off Digital:** Entendeu? O cara vai falar, p\*\*\*\*, mas e tal. Agora se o cara, o motor é f\*\*\* e a o visual é f\*\*\* e tudo é profissional e tudo é coerente e tudo é bonitinho, tudo segue uma lógica,  
**Marcelo Costa:** É,  
**Off Digital:** você começa a ser caro.  
**Marcelo Costa:** não,  
**Off Digital:** Você é caro porque o cara fala:  
**Marcelo Costa:** os cara,  
**Off Digital:** "Velho, isso aqui não custa barato,  
**Marcelo Costa:** os caras vão vir para cima de nós,  
**Off Digital:** o cara  
**Marcelo Costa:** priminho. Nós vamos receber,  
**Off Digital:** olha,  
**Marcelo Costa:** nós vamos pegar umas milhas aqui só nessa brincadeira, velho. Posso do jeito que tá, a gente,  
**Off Digital:** vamos,  
**Marcelo Costa:** eu tenho certeza que a gente falava, vamos vender essa p\*\*\*\*, a gente vende essa p\*\*\*\*, velho.  
   
 

### 02:23:20

   
**Off Digital:** né? Vamos fazer barulho com calma.  
**Marcelo Costa:** Nós vamos pegar um negócio  
**Off Digital:** Aí você começa a inserir nos eventos, a gente vai mostrando o negócio,  
**Marcelo Costa:** maior.  
**Off Digital:** o negócio é chegar de mansinho e a galera ir falando: "Eita, p\*\*\*\*, que que é isso aqui?" É, velho, olha aí, testa aí, veja aí, entendeu? Ah, mas p\*\*\*\*, mas o c\*\*\*\*\*\*, mas você cobre isso, você cobre aquilo, mas p\*\*\*\*, mas você tem tudo isso aqui dentro, mas é, então,  
**Marcelo Costa:** Usa aí,  
**Off Digital:** né? É, usa aí 15 dias aí depois,  
**Marcelo Costa:** testa aí.  
**Off Digital:** p\*\*\*\*, mano, botei lá, os cara tão tal, é, então, mas você sabia que se você precisar eu posso plugar também mais isso, isso e isso para você no custom.  
**Marcelo Costa:** É  
**Off Digital:** p\*\*\*\*, tá. É, então uma hora você vai pegar um cara que o cara vai falar:  
**Marcelo Costa:** isso.  
**Off Digital:** "Velho, não dá, mano. Eu, ó, isso aqui eu Como é quanto é que faz para te comprar?" Porque eu né,  
**Marcelo Costa:** Fala,  
**Off Digital:** eu preciso de você,  
**Marcelo Costa:** velho, para fazer isso aí não tem.  
**Off Digital:** velho. Ah,  
**Marcelo Costa:** E outra,  
   
 

### 02:24:04 {#02:24:04}

   
**Off Digital:** velho,  
**Marcelo Costa:** nesse mercado não tem ninguém pensando ainda com essa cabeça aí,  
**Off Digital:** é,  
**Marcelo Costa:** velho.  
**Off Digital:** é como quem não quer nada e deixar um negócio f\*\*\*. É o que eu falei, a estrutura que a gente cria, velho. Imagina o próximo projeto do zero,  
**Marcelo Costa:** เอ  
**Off Digital:** como é que que a gente já não vai ter de de de estrutura em cima? É o que eu tô falando, igual eu tô fazendo pro pro ADR lá do Stock. Pô, várias ideias veio pro CFY aí, pô. Beleza. No aí já tem o negócio,  
**Marcelo Costa:** começa a ficar voltada para isso.  
**Off Digital:** p\*\*\*\*. Aí você conhece um cara de logística que tem logística de de de galpão, de estoque, você já vai pensar, pô, temos um produto na gaveta ali pronto. Se quiser plugar pro cara e cobrar 20 pau no mês, já tá já tá pronto. É só sentar com o cara, fazer uma reunião, entende o universo dele, a gente contrata um, daqui a pouco contrata um molequinho sagaz para fazer o todo o briefing, toda a pesquisa, todo tudo que tem que fazer o trabalho pesado e a gente começa a ir plugando as coisas. Então, p\*\*\*\*, é nisso que eu tô mais interessado.  
   
 

### 02:25:03 {#02:25:03}

   
**Off Digital:** É tipo, cara, se agora dá para fazer isso, imagina daqui um ano o que que vai dar para fazer e como que a gente vai tá  
**Marcelo Costa:** É, e eu acho que as coisas,  
**Off Digital:** fazendo.  
**Marcelo Costa:** eu acho que os caras vão fechar o cerco das, talvez não tão rápido, mas as coisas vão, como como o Cláudi tá fazendo, velho. O cara tá metendo preço em cima agora,  
**Off Digital:** É.  
**Marcelo Costa:** né?  
**Off Digital:** E outra coisa, primo, a gente pensa que, ah, i tal, não sei o quê, vai, né? Qualquer um que paga sete conos de A por mês, que é o que eu tô gastando, né?  
**Marcelo Costa:** Eh,  
**Off Digital:** Entendeu? Então assim, eu tô investindo tempo e dinheiro,  
**Marcelo Costa:** é e tempo,  
**Off Digital:** realmente eu tô investindo,  
**Marcelo Costa:** velho.  
**Off Digital:** pô.  
**Marcelo Costa:** Quem tem 10 horas do dia para ficar olhando e fazendo,  
**Off Digital:** Não.  
**Marcelo Costa:** construindo o negócio,  
**Off Digital:** E e e tipo assim, realmente se você for pegar de crédito aqui o que o que tá gastando de crédito  
**Marcelo Costa:** velho.  
**Off Digital:** nesse projeto, já deu aí já deve ter dado uns R000. Mas isso é o de menos. Isso é o de menos. Só que você, se você for pensar, não é qualquer um que mete as caras de tipo, pô, vou assinar o plano de 200 da Cláudio, de 200 do GPT,  
   
 

### 02:26:00

   
**Marcelo Costa:** Não,  
**Off Digital:** o mano, todas as ferramentas complementares e o SPF e não sei das quantas e e até o cursor essa  
**Marcelo Costa:** velho.  
**Off Digital:** semana eu tava vendo para para colocar aqui.  
**Marcelo Costa:** É,  
**Off Digital:** E assim, não é nego que tem um sangue,  
**Marcelo Costa:** é aquela coisa,  
**Off Digital:** o sangue  
**Marcelo Costa:** né, velho? Era igual nós no negócio de cripto.  
**Off Digital:** não.  
**Marcelo Costa:** Ah, velho, p\*\*\*, ficava estudando, estudando, mas tem que ter o dinheiro para entrar, velho, né? Não adianta. Ah, legal. Entendi. Projeto f\*\*\*  
**Off Digital:** Aí pagou lá o custo do persigo,  
**Marcelo Costa:** se entrar nesse évei  
**Off Digital:** pagou não sei o quê, pagou não sei das contas, aí tudo é custo,  
**Marcelo Costa:** no dinheiro. Não tinha dinheiro para pôr.  
**Off Digital:** velho.  
**Marcelo Costa:** Aprendi como que fazer, como é que vai, não tinha dinheiro para pôr. Aí agora ela tá mais democrática, né? Porque o cara consegue fazer de graça.  
**Off Digital:** Sim.  
**Marcelo Costa:** Mas vai, para mim vai acabar isso porque as empresas não estão se pagando, né, velho?  
**Off Digital:** Não, mas primo, é de graça até certo ponto.  
**Marcelo Costa:** Entendeu?  
**Off Digital:** Por exemplo, você, ah, vamos brincar aí e tal, você já botou o plano do Cloud de 100, mas você não tá trabalhando um 1/5 de volume de código do que eu tô.  
   
 

### 02:26:58 {#02:26:58}

   
**Off Digital:** Se você começar, você vai começar a ver, c\*\*\*\*\*\*, tá caro, beleza. Mas, mano, até o cara, até o cara entender que ele realmente precisa investir essa quantidade para ele se se interar. Não tô falando de retorno não, mano.  
**Marcelo Costa:** É  
**Off Digital:** Eu eu investi, não foi pensando, ah, pô, porque eu vou fazer os projetos. Eu investi pensando assim, cara, para eu dar o catchup com o que eu tô vendo, que tá rolando no que eu tô acompanhando, o mínimo que eu preciso é ter liberdade total com Codex, com cloud para rodar sem pensar em crédito.  
**Marcelo Costa:** para botar a mão e apertar os botão,  
**Off Digital:** Isso é o isso, isso é a base, velho.  
**Marcelo Costa:** velho.  
**Off Digital:** Isso é o mínimo. Então assim, já é só aí já é três contas, aí você começa a pôr o resto, né? Aí já vai inflando. Então assim, eu tô vendo que tem essa barreira de entrada,  
**Marcelo Costa:** Ja.  
**Off Digital:** cara. Muita gente entende igual meu brother DJ, pô, me ligou esse fim de semana, c\*\*\*\*\*\*, mano, agora tô te entendendo, p\*\*\*\*. O brother me mostrou aqui, o Cloud ficou duas horas comigo, eu já fiz isso, isso aqui, já criei um negócio pra minha empresa.  
   
 

### 02:27:59

   
**Off Digital:** Velho, o cara tá tipo assim, primeira vez que o cara, velho conheceu o Cloud e eu tô falando,  
**Marcelo Costa:** Acabou de acabou de botar o pintinho,  
**Off Digital:** eu tô p\*\*\*\*  
**Marcelo Costa:** né? Fala  
**Off Digital:** mano, que f\*\*\*, que irado e tal.  
**Marcelo Costa:** velho.  
**Off Digital:** Só que o cara fala aí, p\*\*\*\*, mano, aí, pô, já pagou 20 por mês, aí o bagulho no meio do negócio travou porque não podia, p\*\*\*\*. Aí eu falei, cara, bagulho e o moleque tem grana, sacou?  
**Marcelo Costa:** E só dá para pular pro 100,  
**Off Digital:** Então assim,  
**Marcelo Costa:** né,  
**Off Digital:** é, então assim,  
**Marcelo Costa:** velho?  
**Off Digital:** tipo assim, nego não, cara, até o próprio Bone, você vai ver, tipo, nego que realmente assina a parada e usa have user são poucos para mim.  
**Marcelo Costa:** É,  
**Off Digital:** E quando a galera virar user, vai ficar tão caro que o user vai ser $.000,  
**Marcelo Costa:** já foi.  
**Off Digital:** $.000,  
**Marcelo Costa:** Então é isso aí.  
**Off Digital:** 15.000,  
**Marcelo Costa:** É isso aí. Por isso que nós estamos sendo cobaia dos caras para testar toda hora modelo novo.  
**Off Digital:** entendeu?  
**Marcelo Costa:** Mas beleza, mas nós estamos também aprendendo, né, velho?  
   
 

### 02:28:51 {#02:28:51}

   
**Marcelo Costa:** Entendeu?  
**Off Digital:** Exatamente. Tem ser sendo remunerado para fazer o rolê,  
**Marcelo Costa:** E e outra e e olhando tipo,  
**Off Digital:** entendeu?  
**Marcelo Costa:** beleza, velho, hoje nós estamos rodando aqui com cloud, mas a hora que virar a chave aqui, o motorzão tá preparado para pegar um GPT, para pegar um kin, para pegar qualquer p\*\*\*\*,  
**Off Digital:** Sim,  
**Marcelo Costa:** porque nós não vamos, né?  
**Off Digital:** sim.  
**Marcelo Costa:** Então é estrutura,  
**Off Digital:** E aí o modelo e a gente que tá todo dia ali,  
**Marcelo Costa:** né?  
**Off Digital:** por exemplo, vários dias a gente tava, velho, tá uma m\*\*\*\* o cláudio, tá uma m\*\*\*\*, o bicho não tá pensando, tá travando. De repente muda o modelo pro novo e o parada fica sinistra. Só que você tá trampando todo dia, normal.  
**Marcelo Costa:** É,  
**Off Digital:** É só mais um guia e aí o negócio vai para outro dia,  
**Marcelo Costa:** é, mas e eu acho que os caras fazem isso,  
**Off Digital:** meu.  
**Marcelo Costa:** o cara faz isso exatamente para para valorizar o próximo modelo.  
**Off Digital:** Sim,  
**Marcelo Costa:** Dá uma travada  
**Off Digital:** ele ele degrada, ele vai degradando ali.  
**Marcelo Costa:** geral.  
**Off Digital:** Quando chega perto de lançar o último modelo, ele vai degradando para você ter um uma sensação f\*\*\* quando lança o negócio.  
   
 

### 02:29:39 {#02:29:39}

   
**Off Digital:** Só que o que eu tô falando é,  
**Marcelo Costa:** É.  
**Off Digital:** eu tô trabalhando todo dia, independente do modelo, modelo bom, modelo ruim. p\*\*\*\*, teve teve momentos do certifi aqui que tava f\*\*\*, mano, que eu tava trabalhando aí, ela tava burra para c\*\*\*\*\*\*, não fazia nada, eu mandava fazer uma coisa, eu fazia outra e você tem que trampar do mesmo jeito, velho.  
**Marcelo Costa:** É, e tem que achar a solução e ir indo,  
**Off Digital:** Entendeu? E você tem que ir fazendo.  
**Marcelo Costa:** né?  
**Off Digital:** Então assim, só que você tá no meio do dia a dia e aí sai um GPT6 e aí sai um OPO 5 e aí daqui a pouco qual vai ser as possibilidades? Porque você tá todo dia,  
**Marcelo Costa:** É, você sabe diferença de  
**Off Digital:** entendeu? Então esse é o ponto, mano. Se você tá todo dia, velho, você vai acompanhando a a mud.  
**Marcelo Costa:** um  
**Off Digital:** Esse é que é o que eu que eu entendi, velho, que é o f\*\*\*. Não é que o bagulho mudou, você perdeu o N8N. Não, velho. Tudo que você saber de N8N, a arquitetura tá aqui.  
**Marcelo Costa:** e quem não quem não participou às vezes não vai conseguir conectar tantas pontas.  
**Off Digital:** Agora você não tem uma coisa, outra que vai ficar em aberto.  
   
 

### 02:30:37

   
**Off Digital:** Então assim, só que o ponto é que tem gente que é saudosista. O cara se apega na na ferramenta, não no processo. Esse aqui é o ponto. Tem é que igual o cara do vinil que p\*\*\*\*  
**Marcelo Costa:** É  
**Off Digital:** mudou para CD, o cara não, velho, porque pô, CD não presta, o negócio é vinil e tal, cara. Saludosismo puro,  
**Marcelo Costa:** foi engolido.  
**Off Digital:** saudosismo.  
**Marcelo Costa:** Ela  
**Off Digital:** Então se você não, pô, então pô, eu tocava vinil, virou CD. Agora eu vou ser monstro do CD com tudo que eu já aprendi do vinil.  
**Marcelo Costa:** vai.  
**Off Digital:** p\*\*\*\*, agora é mais fácil. Não tem que carregar o bagulho pesado, não estraga no sol, não sei das quantas, não sei das quantas. Não, velho. O cara ficar naquela p\*\*\*\*\*\* lá de não, velho. O bom é o vinil, entendeu?  
**Marcelo Costa:** É,  
**Off Digital:** Por o cara não quer se dispor a soltar o que ele sabia para aprender o bagulho  
**Marcelo Costa:** é,  
**Off Digital:** novo de sair da zona.  
**Marcelo Costa:** o cara não tá a fim de de de mudar, né, velho? Que p\*\*\*\*, para mim é,  
**Off Digital:** De sair da zona. O cara fala: "Vel,  
   
 

### 02:31:23 {#02:31:23}

   
**Marcelo Costa:** né?  
**Off Digital:** aqui eu domino, enquanto tiver funcionando isso aqui, enquanto ainda ligar,  
**Marcelo Costa:** É,  
**Off Digital:** eu tô on." É.  
**Marcelo Costa:** o cara ainda tá no conforto. É isso  
**Off Digital:** É, então assim, o que vai mudar é isso, velho.  
**Marcelo Costa:** aí.  
**Off Digital:** É quem é quem tá aberto para para pular pra frente. Se hoje chegar um bagulho e falar: "Cara, não é mais Cláudio, não é mais Codex, agora é o Capivara, vamos embora pro Capivara, mano. p\*\*\*\*\*\*\*\* do c\* do Codex,  
**Marcelo Costa:** Isso aí.  
**Off Digital:** pau do c\* do Cláudio, entendeu?  
**Marcelo Costa:** Eu peguei depois aqui também um um aquele moleque que eu mandei lá que fez os cursinhos do OpenCloud, não sei o quê,  
**Off Digital:** Nãoi.  
**Marcelo Costa:** ele fez um manualzinho até bom, velho. Tipo assim, p\*\*\*\*, como fazer o seu OpenCloud voltar como era com o GPT. E aí ele deu vários passos de fazer uma uma auditoria nele, não sei o quê, tal, tal, fazer umas bases lá para voltar. Ele diz ele que assim, beleza, não voltou o o com opos que era muito pica, mas ele tá a 80%, velho.  
**Off Digital:** Priminho, o GPT com 5.5 tá voando.  
   
 

### 02:32:22 {#02:32:22}

   
**Marcelo Costa:** Então,  
**Off Digital:** O o o open cloud tá ótimo. Voltou de novo. É,  
**Marcelo Costa:** é,  
**Off Digital:** tem que tem algumas mexid assim, a personalidade dele ainda não é tão pá, mas em termos de execução, p\*\*\*\*,  
**Marcelo Costa:** é, mas foi justamente no sou que ele falou para mexer e tal.  
**Off Digital:** tá voando.  
**Marcelo Costa:** Vou te mandar depois o Ele fez um manualzinho, depois você dá uma  
**Off Digital:** Sim, sim. Não, eu já mexi bastante no meu show,  
**Marcelo Costa:** olhada.  
**Off Digital:** já já botei várias regrinhas que só funciona pro GPT, que pro OPS não precisava, já dei uma mexida boa. Agora depois da atualização do 5.5, aí mudou, mudou, mudou legal,  
**Marcelo Costa:** Eh,  
**Off Digital:** porque eles eles trabalharam muito na última atualização do OpenCloud.  
**Marcelo Costa:** vou  
**Off Digital:** Você tem que atualizar o seu open cloud pro último e botar ele para rodar no 5.5. Aí você vai sentir o Her,  
**Marcelo Costa:** eu vouar  
**Off Digital:** o Ernest também tá pica, velho. O Hermes o Ernis com 5.5 tá animal.  
**Marcelo Costa:** também.  
**Off Digital:** Aí eu tô pensando em deixar o OpenCloud para assistente porque ele tem mais coisa, ele tá muito mais maior, tem muito mais estrutura do que o Hermes. O meu Hermes tá bem, meu Herm tá bem minimalista assim, ele só tem o que precisa, poucas skills, poucos crons,  
   
 

### 02:33:32 {#02:33:32}

   
**Marcelo Costa:** mais  
**Off Digital:** então ele tá tipo, é, ele tá muito selecionadinho e o open cloud tá assim,  
**Marcelo Costa:** estratégico.  
**Off Digital:** a p\*\*\*\* toda. Então eu acho que eu vou deixar o meu open cloud para ser um assistentezão bala. E o Hermes para ser um CEO, entendeu? para ser um cara mais coordenador.  
**Marcelo Costa:** passar o o que tiver aprovado para ele.  
**Off Digital:** Um cara mais coordenador, um cara mais poucas palavras.  
**Marcelo Costa:** Se for validado, sobe, né, velho? Deixa o pencal batendo cabeça e o validou bota no  
**Off Digital:** Eh, exato, exato. Então, deixar ele, eu hermes,  
**Marcelo Costa:** outro.  
**Off Digital:** para ser um cara mais poucas ideias. Eu tô criando um negocinho aqui que eu não tive tempo de mexer. Eu mexi na semana do meu sogro lá, mas um negocinho para ser um painel de junção de tudo. Ele vai controlar o Herms, vai controlar o OpenCloud, vai controlar a sessão do cloud e vai controlar a sessão do Codex. E aí eu quero botar eles para se falar. Eu ainda não sei como eu vou fazer para eles para se falar, mas eu já tenho o eu já tenho  
**Marcelo Costa:** É, mas você vai dar o acesso e tal, eles vão,  
   
 

### 02:34:33 {#02:34:33}

   
**Off Digital:** o  
**Marcelo Costa:** alguém, algum dos dos caras vão se falar e puxar. as informação que precisa,  
**Off Digital:** É, eu não sei como, velho, como é que é,  
**Marcelo Costa:** né?  
**Off Digital:** se é sin link, qual que é o a tecnologia usada para você conectar essas diferentes plataformas em tempo real, porque o que eu quero é tipo, por exemplo, eh, É, cara, eu tô eu tenho cinco sprint para fazer do certify, uma para cada coisa. Então, uma eu vou mexer na aba de revisão, outra eu vou mexer no centro de comando, outro vou mexer no superbase. Beleza? Eu planejo isso. E aí eu quero que, tipo, por exemplo, o que é de design, eu quero que toque no cloud. O que é de código, eu até quero que toque no Codex. O que é de supervisão, eu quero que vá pro Hermes e o que é de pesquisa barra eh meio meio de campo open cloud. E eu quero que todos eles se conversem durante a sessão.  
**Marcelo Costa:** Entendi. Ver, ó,  
**Off Digital:** Então o cara doar no front,  
**Marcelo Costa:** tô precisando disso aqui. Se eu fiz isso,  
**Off Digital:** eu preciso que o cara do backend me entregue isso aqui.  
**Marcelo Costa:** tal.  
**Off Digital:** O cara fala: "Ó, daqui a 2 minutos, porque eu preciso do cara do supervisor validar tal coisa." E aí sim você vai começar a chegar num  
   
 

### 02:35:45

   
**Off Digital:** ponto mais autônomo, que eu não vou precisar ficar na frente da tela igual eu fico toda hora. Aí o meu meu ponto vai ser planejar e entregar e  
**Marcelo Costa:** planeja e a execução se acompanha onde  
**Off Digital:** conseguir. Planeja entrega e confere.  
**Marcelo Costa:** tiver.  
**Off Digital:** Então aqui, ó, te mostrar só para você ver a cara do bagulho. Tá ficando, mano, embaçado aqui, ó. um Chrome aqui,  
**Marcelo Costa:** Hum.  
**Off Digital:** ó.  
**Marcelo Costa:** Угуm.  
**Off Digital:** Tá vendo aí? Então aqui você tem aqui, ó, né, o home, eh, as connections, aqui você tem o Hermes, aqui você tem o open cloud, eh, as sessions, os arquivos. Isso aqui é tudo ermes, tá vendo?  
**Marcelo Costa:** Isso é dentro do Hermes,  
**Off Digital:** dentro do Hermes.  
**Marcelo Costa:** essa organização,  
**Off Digital:** É isso tudo. Isso aqui tudo eu construí tudo esse software, você tá vendo eu que fiz. Mas aqui, ó, as skills,  
**Marcelo Costa:** tá?  
**Off Digital:** por exemplo, tá aqui as skills, ó. Tá vendo? Ó, skill aqui e tal.  
**Marcelo Costa:** Uhum.  
**Off Digital:** E você pode vir editar. Se eu editar aqui, ele ele edita no Hers. Beleza. Aqui eu tô conectado no Hers.  
   
 

### 02:36:58 {#02:36:58}

   
**Off Digital:** Aqui eu tô no OpenCloud, entendeu?  
**Marcelo Costa:** Tá,  
**Off Digital:** Aqui, ó.  
**Marcelo Costa:** você já separou um tipo um centro de comando dos dois,  
**Off Digital:** Aqui é o Hermes é azulzinho.  
**Marcelo Costa:** né? Ele só não  
**Off Digital:** O o open cloud quando eu clico fica vermelho. Tá vendo?  
**Marcelo Costa:** Tá. Uhum.  
**Off Digital:** O cloud quando eu clicar vai ficar laranja. O GPT vai ficar preto,  
**Marcelo Costa:** Tá,  
**Off Digital:** entendeu?  
**Marcelo Costa:** tá.  
**Off Digital:** Então vai ter tudo aqui,  
**Marcelo Costa:** Centralzinho.  
**Off Digital:** vai ter tudo rodando aqui. Então aqui, ó, por exemplo, aqui eu tô no Open Cloud.  
**Marcelo Costa:** M.  
**Off Digital:** Aí aqui eu tenho aqui, ó, é porque eu tô no Dev server, ele não tá na na versão atualizada, mas já tá funcionando já o do OpenCloud também. Então vou ter aqui conexões, Chrome, os os EG, skills e tal. Aqui eu tenho terminal, ó. Se eu abrir aqui, ó, o RS, eu tenho terminal. Não tá funcionando nessa versão, mas já tá funcionando na na outra. Já tá escrevendo. O transporte caiu,  
**Marcelo Costa:** Top.  
**Off Digital:** ó. Tem que reconectar o host para funcionar. E aí aqui vai ter cloud, eh, Codex, Open Cloud e Hermes.  
   
 

### 02:38:04 {#02:38:04}

   
**Off Digital:** E aí eu vou criar um outro ambiente. Aqui é só para configurar, né? Coisa tipo skill, arquivos, Chrome, beleza? Sessions, tal. Aí eu vou ter um outro ambiente que é de action, aonde você vai abrir e esses cara, eu tô pensando em fazer um negócio tipo um grupo de WhatsApp, aonde cada gente vai ser uma pessoa no grupo aqui dentro, uma interface, tipo um grupo de WhatsApp. E aí dentro do grupo,  
**Marcelo Costa:** falar  
**Off Digital:** dentro do grupo de WhatsApp, mano, vai rolar tudo. Vai, vai. Se você clicar na setinha, vai abrir o trabalho do Hermes. Se você clicar na setinha, vai abrir o trabalho do Codex. Cada sessão que eu abri do cloud, vira uma pessoa dentro do grupo. Então, abri uma aba do cloud, ele entrou um cara no grupo, abriu outra aba, entrou outro cara, terminou o trabalho, encher aba,  
**Marcelo Costa:** Entendi,  
**Off Digital:** ele sai do grupo, entendeu?  
**Marcelo Costa:** entendi. Para saber quem tá trampando tá ali,  
**Off Digital:** quem tá trampando naquele momento,  
**Marcelo Costa:** quem não tá.  
**Off Digital:** naquele projeto. Então você abre o grupo ali, todo mundo conversa e todo mundo trampa junto. É isso que eu quero criar. Só que é lógico, entre a ideia e o produto final vai dois meses aí no mínimo,  
**Marcelo Costa:** Top.  
**Off Digital:** né?  
**Marcelo Costa:** É,  
**Off Digital:** E ainda e tem que ter tempo para fazer isso.  
**Marcelo Costa:** p\*\*\*\*.  
**Off Digital:** Então eu não tô olhando para isso para não bagunçar minha cabeça, né?  
**Marcelo Costa:** É,  
**Off Digital:** Mas é  
**Marcelo Costa:** mas animal, animal. p\*\*\*\*, velho. Esse é o cockpit, né?  
**Off Digital:** Vamos aí.  
**Marcelo Costa:** Vou vou voar que eu tô Já deu a hora de buscar bebê na escola,  
**Off Digital:** Eu tenho que eu tenho que me preparar  
**Marcelo Costa:** velho. Olha que p\*\*\*  
**Off Digital:** pra próxima aqui,  
**Marcelo Costa:** que  
**Off Digital:** primi. Mas então, amanhã no horário do meio-dia aí a gente a gente segue o bar,  
**Marcelo Costa:** vai. Tá bom.  
**Off Digital:** beleza?  
**Marcelo Costa:** Dá um alô. Valeu, primo.  
**Off Digital:** Tamamos junto.  
**Marcelo Costa:** Tamo junto.  
   
 

### A transcrição foi encerrada após 02:39:40

*Esta transcrição editável foi gerada por computador e pode conter erros. As pessoas também podem alterar o texto depois que ele for criado.*
