# Claude Code — Padrões e Aprendizados Cross-Project
# Base de conhecimento compartilhada entre todos os projetos.
# Atualizado à medida que novos padrões são descobertos.
# Atualizado: 2026-04-26

---

## Por que este arquivo existe

Copiar CLAUDE.md entre projetos gera duplicatas desatualizadas.
Este arquivo captura o que realmente tem valor compartilhar:
padrões que funcionam, armadilhas conhecidas e estratégias de prompt.

---

## Padrões de Arquitetura

### Separação dados / código
Dados de conteúdo (textos, configurações, perfis) em arquivos YAML ou MD separados do código.
O código lê os dados — nunca os contém hardcodados.
**Resultado:** atualizar conteúdo sem tocar em código. Testado em myCV.

### Entry points em scripts/
Manter a lógica de negócio em `src/` e os pontos de entrada do usuário em `scripts/`.
Facilita uso via CLI e evita que o usuário precise entender a estrutura interna.

### Snapshot antes de editar
Antes de qualquer mudança em arquivos de dados importantes, criar um snapshot versionado.
Em myCV: `python scripts/snapshot.py -m "descrição da mudança"`.
Padrão replicável em outros projetos com dados críticos.

---

## Padrões de Trabalho com Claude Code

### Dar contexto antes de pedir código
Antes de pedir implementação, descrever: o que o projeto faz, qual problema resolve,
qual a arquitetura existente. O CLAUDE.md faz isso automaticamente na abertura da sessão.

### Manter CLAUDE.md atualizado
O CLAUDE.md é o "briefing" que o Claude Code lê ao iniciar uma sessão.
Deve refletir o estado real do projeto — não o estado planejado.
Atualizar sempre que a arquitetura ou as regras mudam.

### Pedir análise antes de implementação
Para tarefas complexas: pedir análise e proposta primeiro, confirmar, depois implementar.
Evita retrabalho em decisões de arquitetura.

### Operações paralelas vs sequenciais
Claude Code executa chamadas de ferramentas em paralelo quando são independentes.
Declarar dependências explicitamente: "faça X, depois Y usando o resultado de X".

---

## Armadilhas Conhecidas

### fpdf2 — Charset latin-1
O gerador de PDF (fpdf2 sem fonte TTF) usa encoding latin-1.
Caracteres proibidos nos arquivos YAML que alimentam o PDF:
- `—` (em dash U+2014) → usar ` -`
- `→` (seta U+2192) → usar `->`
- Aspas tipográficas `"` `"` → usar `"`

Validar antes de gerar: `python -c "t=open('arquivo.yaml',encoding='utf-8').read(); print([c for c in t if ord(c)>255] or 'ok')"`

### Não copiar arquivos de referência — linkar
Copiar CLAUDE.md ou outros arquivos de referência entre projetos cria duplicatas.
Preferir: um arquivo de índice com o caminho para o original.

### .gitignore para dados sensíveis
Pastas com documentos pessoais (CPF, RG, documentos gov.br) devem estar no .gitignore
**antes** de qualquer commit. Em myCV: `data/gov_br/` está protegida.

---

## Prompts Eficazes (Claude API)

### Para bullets de CV orientados a resultado
"Reescreva como bullet de CV: verbo de ação + contexto + resultado quantificado.
Máximo 2 linhas. Sem jargão desnecessário."

### Para revisão de seção
"Analise esta seção. Retorne: (1) pontos fortes, (2) até 3 sugestões, (3) versão revisada."

### Para post LinkedIn tipo case
"Estrutura: gancho forte (1 frase) + contexto do problema + solução + resultado quantificado
+ aprendizado ou convite à discussão. 150-250 palavras. Tom profissional, não corporativo."

---

## Skills Úteis (Claude Code)

| Skill | Quando usar |
|---|---|
| `/commit` | Criar commits com mensagem bem estruturada |
| `update-config` | Configurar permissões, hooks, variáveis de ambiente |
| `simplify` | Revisar código gerado em busca de over-engineering |

---

## Registro de Aprendizados por Projeto

| Data | Projeto | Aprendizado |
|---|---|---|
| 2026-04-26 | myCV | fpdf2 rejeita chars acima de U+00FF — substituir em dash e setas |
| 2026-04-26 | myCV | Separar dados YAML do layout PDF elimina retrabalho em atualizações de conteúdo |
| 2026-04-26 | myCV | CLAUDE.md como briefing automático elimina necessidade de recontextualizar o Claude a cada sessão |
