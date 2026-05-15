# Workflows

## Fluxo 1: importar transcrito do e-mail

1. Buscar mensagens candidatas por query configurada.
2. Identificar provedores conhecidos de reunião.
3. Baixar ou extrair transcrito.
4. Salvar original em área local ignorada pelo Git.
5. Gerar receipt com origem, hash e metadados.

Saída esperada: transcrito bruto preservado e item pronto para normalização.

## Fluxo 2: processar transcrito

1. Remover ruído técnico sem apagar conteúdo semântico.
2. Separar participantes, timestamps e tópicos.
3. Extrair decisões, ações, perguntas abertas e riscos.
4. Marcar trechos com baixa confiança.
5. Persistir JSON estruturado.

Saída esperada: objeto processado com evidências rastreáveis.

## Fluxo 3: enviar para vault

1. Escolher vault e pasta alvo por projeto, pessoa ou cliente.
2. Gerar nota Markdown com frontmatter.
3. Criar links internos previstos.
4. Rodar dry-run mostrando caminho e diff.
5. Escrever só com autorização explícita.

Saída esperada: nota pronta para vault, com caminho determinístico.

## Fluxo 4: operar GitHub

1. Detectar repositórios mencionados.
2. Mapear tarefas para issue drafts.
3. Mapear decisões para comentários ou updates de docs.
4. Rodar dry-run com payloads.
5. Criar issue, comentário ou PR só com autorização explícita.

Saída esperada: ações GitHub propostas com contexto e evidência.

## Fluxo 5: revisão diária

1. Listar reuniões processadas.
2. Mostrar pendências sem destino.
3. Mostrar ações GitHub ainda não aplicadas.
4. Mostrar notas de vault pendentes.
5. Fechar receipts concluídos.
