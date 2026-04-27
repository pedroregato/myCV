# Career Card — SE-SUITE Utils (FGV)

> Este bloco e sincronizado periodicamente com o repositorio myCV pessoal.
> Nao contem codigo proprietario nem dados sensiveis da FGV.
> Atualizar a cada marco relevante (entrega, resultado mensuravel, novo projeto).

---

### Identificacao

- **Projeto:** SE-SUITE Utils — Automacao de Gestao Documental FGV
- **Periodo:** 10/2024 - atual
- **Status:** Em andamento
- **Minha funcao:** Desenvolvedor principal / Arquiteto de solucao

---

### Problema resolvido

A FGV mantinha centenas de documentos de auditoria (Instrucoes de Trabalho, Catalogos de Processos, Organogramas) dispersos em pastas de rede sem rastreabilidade. A migracao para o sistema corporativo SE-SUITE era feita manualmente — operacao suscetivel a duplicatas, inconsistencias e alto custo operacional. Operacoes recorrentes como gerar documentos padronizados e atualizar metadados consumiam horas de trabalho humano por ciclo.

---

### Solucao implementada

Suite Python de automacao que integra com o SE-SUITE via SOAP/REST e expoe uma API FastAPI para consumo interno. O sistema cobre tres frentes:

1. **Migracao do acervo legado** — scripts idempotentes que percorrem a arvore de pastas de rede (`\\fgvfsbi\AUDITORIA-LEGADO-DOCS`), extraem dados de PDFs e Word, e publicam documentos no SE-SUITE com pipeline de revisoes controlado por BPM.

2. **Geracao automatica de documentos** — endpoints REST que geram `.docx` de IT (Instrucao de Trabalho) e CP (Catalogo de Processos) a partir dos dados cadastrados no SE-SUITE, publicam a revisao e retornam envelope JSON para integracao com formularios responsivos.

3. **Analytics e diagnostico** — queries SQL para o SE Analytics (cobertura documental por escola, indices de maturidade) e scripts de diagnostico operacional (backfill de campos, verificacao de hierarquia).

---

### Stack principal

- **Python 3.11** — logica de negocio, integracao SOAP, processamento de documentos
- **FastAPI + Uvicorn/Gunicorn** — API REST com autenticacao JWT / API Key / Basic Auth
- **pdfplumber + PyMuPDF** — extracao de texto e tabelas de PDFs do acervo legado
- **python-docx** — geracao de documentos Word a partir de templates
- **Streamlit** — dashboard operacional de migracao
- **Docker** — deploy em servidor corporativo com SSL TLS 1.2
- **SE-SUITE SOAP** (fm_ws, dc_ws, wf_ws, adm_ws) — integracao com todos os modulos do sistema
- **SQL Server / SE Analytics** — queries de cobertura e validacao pos-migracao
- **Claude Code** — parceiro de desenvolvimento ao longo de todo o projeto

---

### Impacto mensuravel

- **~200+ documentos** de auditoria migrados do acervo legado para o SE-SUITE com rastreabilidade completa (hash SHA-256 como chave de idempotencia)
- **28 escolas/unidades** da FGV com estrutura organizacional, processos e subprocessos cadastrados de forma automatizada
- **Eliminacao de trabalho manual** na geracao de ITs e CPs — operacao que levava horas passou a ser acionada via formulario em segundos
- **Pipeline de revisoes BPM** implementado end-to-end: criacao, upload, emissao — sem intervencao humana
- **Backfill de metadados** (`entranait`) em 90 subprocessos em execucao unica com matching seq/titulo/fuzzy sobre PDFs do legado

---

### Decisoes tecnicas importantes

1. **Sem mocks para o SE-SUITE** — decisao arquitetural intencional. Todos os testes batem na instancia real. Evita falsa seguranca: a API SOAP do SE-SUITE tem comportamentos indocumentados (retorno de campos em UPPERCASE, namespaces XML que quebram `find()`, sequencia de pipeline rigida) que so aparecem com a integracao real.

2. **Idempotencia por hash SHA-256 do caminho de origem** — permite reexecutar qualquer script de migracao sem gerar duplicatas. Decisao que viabilizou iteracao rapida: migrar, corrigir, migrar novamente sem limpeza manual do SE-SUITE.

3. **Arquitetura em camadas (API / Use Cases / Business / Core)** — separacao que permitiu reutilizar a logica de geracao de documentos tanto nos scripts de migracao em batch quanto nos endpoints REST, sem duplicacao de codigo.

---

### Uso do Claude Code

Claude Code foi utilizado como parceiro de desenvolvimento em sessao continua ao longo de todo o projeto:

- **Arquitetura e design** — definicao das camadas, convencoes de nomenclatura, estrutura de dominios
- **Geracao de codigo** — implementacao de wrappers SOAP, endpoints FastAPI, scripts de migracao, pipeline de revisoes
- **Debugging de integracao** — diagnostico de comportamentos indocumentados do SE-SUITE (namespace XML, retorno UPPERCASE, sequencia de pipeline)
- **Documentacao viva** — manutencao dos arquivos CLAUDE.md com contexto acumulado entre sessoes
- **Resolucao de incidentes** — diagnostico de 500 silenciosos, correcao de git em share SMB, fix de idempotencia de backfill

O projeto e evidencia pratica de fluencia em desenvolvimento assistido por IA em contexto corporativo real, com restricoes de seguranca, sistemas legados e integracao SOAP complexa.

---

### Bullet CV (rascunho)

Desenvolveu suite Python de automacao de gestao documental para a FGV, integrando com o sistema corporativo SE-SUITE via SOAP/REST e eliminando operacoes manuais recorrentes para 28 unidades academicas; implementou pipeline de migracao idempotente de 200+ documentos e API FastAPI com deploy Docker em ambiente corporativo.

---

### Proximos passos

- Backfill `entranait` para todas as escolas (`--all`) apos validacao por amostra
- Endpoints do dominio DO Compras (`/api/docompras/`) e SRA (`/api/sra/`)
- Portal Analytics de cobertura documental (SE Analytics + queries business-queries/)
- Formulario responsivo AUD-CLAUDE-001 para acionar geracao de IT/CP diretamente do SE-SUITE

---

### Notas para sincronizacao

- Nao mencionar nomes de servidores internos (10.61.36.x), credenciais ou dados de clientes
- "SE-SUITE" e o nome comercial do sistema — pode ser referenciado publicamente
- "FGV" pode ser mencionada como cliente/empregador
- O repositorio GitHub e publico: `github.com/pedroregato/seSuiteUtils`
- Periodo de inicio estimado — confirmar data exata antes de publicar no myCV

---
<!-- Ultima atualizacao: 2026-04-26 -->
