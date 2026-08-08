# Career Card — Process2Diagram (P2D)
# Status: Ativo | Visibilidade: Publico (open source)
# Repositorio: https://github.com/pedroregato/Process2Diagram
# Claude Code: Sim
# Atualizado: 2026-07-12 (verificacao por leitura direta do codigo-fonte - ver nota abaixo)

**Nota de atualizacao (2026-07-12):** numeros e capacidades verificados por Claude Code
rodando diretamente no repositorio do P2D (leitura de codigo, nao inferencia), a partir de
um gap analysis contra checklist de vaga de IA. Substituem os valores de 2026-07-03
(9 agentes, ~125 ferramentas, 6 providers, 345 testes). Detalhe por item: ver secoes
"Governanca & Compliance", "Observabilidade & FinOps" e "Cloud & API" abaixo, todas novas
nesta revisao. A lista nominal dos 13 agentes ainda precisa ser preenchida (a versao
anterior nomeava 7 papeis); os 6 adicionais nao foram detalhados nesta verificacao.

---

## O que e

Sistema multi-agente que converte transcricoes de reuniao em artefatos de negocio
estruturados, em uma unica execucao automatizada. Publicado como projeto open source
no GitHub. Deploy continuo no Streamlit Cloud.

Aceita entrada em texto, `.txt`, `.docx` ou `.pdf` e gera simultaneamente:
- Diagramas BPMN 2.0 (XML com viewer interativo)
- Fluxogramas Mermaid (SVG com pan/zoom)
- Ata de reuniao (`.md` / `.docx` / `.pdf`)
- Requisitos classificados por IEEE 830
- Vocabulario SBVR (regras de negocio, padrao OMG)
- Modelo BMM (visao, missao, objetivos, estrategias)
- Relatorio executivo HTML interativo (filtros, comentarios persistentes)

## Problema que resolve

Documentacao pos-reuniao e trabalho manual, repetitivo e frequentemente negligenciado.
Process2Diagram automatiza esse fluxo completo a partir da transcricao bruta, eliminando
horas de trabalho por reuniao e produzindo artefatos padronizados prontos para uso.

## Arquitetura

Pipeline multi-agente orquestrado via `KnowledgeHub` (dataclass em `st.session_state`
como fonte unica de verdade entre agentes). Contagem verificada em 2026-07-12 via
`Orchestrator._PLAN` (passos com LLM): **13 agentes especializados**. Os 7 papeis abaixo
foram nomeados na revisao de 2026-07-03; os 6 agentes adicionais que fecham em 13
**ainda precisam ser detalhados aqui**:

- **Quality Inspector** - classifica a transcricao de A a E com criterios ponderados
- **Preprocessor** - remove ruidos de ASR, pausas, fillers (sem LLM, Python puro)
- **NLP Chunker** - spaCy NER para reconhecimento de entidades e atores
- **BPMN Architect** - extracao via LLM + auto-repair determinístico em 4 passagens
- **Minutes & Requirements** - executam em paralelo via ThreadPoolExecutor
- **SBVR & BMM Agents** - extracao semantica opcional
- **Executive Synthesizer** - gera relatorio HTML com sidebar e comentarios
- (Preencher: 6 agentes adicionais - candidatos prováveis incluem DMN e o pipeline de compliance/PII)

**Mecanismos de qualidade:**
- LangGraph Adaptive Retry: re-executa o agente BPMN ate atingir threshold de qualidade (max 5 tentativas)
- Tournament mode: gera 1, 3 ou 5 candidatos BPMN e seleciona o melhor por scoring ponderado
- ROI-TR Dashboard: metrica de qualidade de reuniao (0-10) com 11 tipos classificados e matrizes de peso dinamicas

## Governanca & Compliance (LGPD)

Camada de compliance dedicada, `modules/compliance/` (`detector.py`, `audit.py`,
`consent.py`), com tabelas proprias em producao (`compliance_consent`, `compliance_audit`):
- Pseudonimizacao reversivel de PII em duas camadas - dados estruturados via regex e
  nomes proprios via NER
- Trilha de consentimento e auditoria versionadas em banco

**Isolamento multi-tenant - honestamente:** o isolamento por `project_id`/`tenant_id` e
real na camada de aplicacao, mas RLS (Row Level Security) no Postgres esta inconsistente
entre tabelas (mistura de tabelas sem policy, `USING(true)` permissivo, e RLS
explicitamente desabilitada em algumas). **Nao vender como "RLS completo" ou "isolamento a
nivel de banco"** - o correto e "isolamento multi-tenant na aplicacao, com RLS parcial".

## Observabilidade & FinOps

- Telemetria de chamadas LLM com deteccao de anomalia de taxa de erro por provedor
- Rastreamento de taxa de saida bem-formada (schema validation) por agente/versao de
  prompt ao longo do tempo - fecha o ciclo entre chamada de modelo e sinal acionavel
- Ferramenta de modelagem de custo (`core/cost_model.py`, `pages/CostBenefitScenarios.py`)
  comparando 17 modelos em 6 provedores por cenario de uso, com projecao de custo
  antes da execucao

## RAG / Copilot corporativo

Assistente conversacional com **151 ferramentas** (contagem real via
`get_tool_schemas_openai()`, nao estimativa) de consulta/escrita sobre o historico do
projeto, com busca semantica via pgvector e embeddings Matryoshka 512-dim. Dois modos:
tool-use direto e analise autonoma multi-etapa (ate 15 rounds).

## Cloud & API

- Containerizacao multi-stage (Docker) e infraestrutura como codigo para Google Cloud
  Run (Cloud Build CI/CD) - **preparada, nunca implantada em producao**. O deploy real
  e ao vivo continua sendo Streamlit Cloud, com CI/CD automatico no push para `main`.
  **Nao afirmar "experiencia em producao com GCP"** - afirmar "IaC pronta para Cloud Run".
- API comercial propria (FastAPI, autenticacao por chave + rate limiting)

## Tecnologias

Python 3.13 - Streamlit - LangGraph - Supabase (Postgres + pgvector) - spaCy (`pt_core_news_lg`) -
Anthropic Claude (claude-sonnet-4-20250514) - DeepSeek - OpenAI - Azure OpenAI Service -
Groq - Gemini - Grok - FastAPI - Docker - Google Cloud Run (IaC) -
ThreadPoolExecutor - python-docx - PyMuPDF - BPMN 2.0 XML

## Uso do Claude Code

Desenvolvido integralmente com Claude Code como parceiro de desenvolvimento:
- Arquitetura do pipeline multi-agente e padrao KnowledgeHub
- Implementacao dos agentes especializados e do BaseAgent com retry e token tracking
- Algoritmos de layout BPMN (eliminacao de lane-crossing, alinhamento de branches paralelos)
- Sistema de auto-repair determinístico (4 passagens sem LLM)
- Suite de testes (874 testes automatizados, mocks para chamadas LLM)
- Documentacao (README, CLAUDE.md)

## Decisoes importantes

1. **KnowledgeHub como estado central** - cada agente le apenas os campos necessarios
   e escreve somente na sua secao designada; versionamento em toda mutacao. Evita
   acoplamento direto entre agentes e permite paralelismo seguro

2. **ThreadPoolExecutor em vez de asyncio** - Streamlit usa modelo sincrono incompativel
   com asyncio nativo; solucao com workers gerenciados explicitamente

3. **Auto-repair determinístico (sem LLM)** - correcao de BPMN invalido em 4 passagens
   (arestas soltas, nos isolados, labels XOR, bypass de gateways) sem custo adicional
   de tokens e com comportamento previsivel e testavel

4. **Multi-provider LLM** - suporte a 7 providers (incl. Azure OpenAI Service, adicionado
   em 2026-07-12 - `client_type="azure_openai"` em `modules/config.py`, client dedicado
   `openai.AzureOpenAI`, 13 testes mockados) permite ao usuario escolher entre custo
   (DeepSeek), velocidade (Groq), qualidade (Claude) ou tier gratuito (Gemini)

## Status atual

Em producao continua no Streamlit Cloud com auto-deploy no push para `main`.
874 testes automatizados passando. Repositorio criado em marco/2026, evolucao ativa.

## Impacto / Metricas

- 12 artefatos formais gerados em execucao unica a partir de uma transcricao: diagramas
  BPMN 2.0 e Mermaid, atas estruturadas, requisitos IEEE 830, vocabulario SBVR, modelo BMM,
  tabelas DMN 1.4 e grafo de conhecimento entre reunioes
- Pipeline de 13 agentes especializados (Orchestrator proprio em Python, LangGraph restrito
  a retry adaptativo de qualidade, validacao deterministica via AgentValidator sem LLM, Supabase)
- Assistente conversacional com 151 ferramentas de consulta/escrita sobre o historico do projeto
- Suporte a 7 provedores LLM (DeepSeek, Claude, OpenAI, Azure OpenAI, Gemini, Groq, Grok)
- Camada de conformidade LGPD nativa (pseudonimizacao PII, consentimento e auditoria versionados)
- Telemetria de custo/erro por provedor (FinOps) com deteccao de anomalia
- 874 testes automatizados, em producao continua
- Deploy continuo: Streamlit Cloud com CI/CD automatico no push
- IaC pronta para Google Cloud Run (Docker multi-stage + Cloud Build) - nao implantada em producao
- (Preencher: numero de usuarios? transcricoes processadas? feedback coletado?)

## Referencias no CV/LinkedIn

- Portfolio de Projetos Autorais em `profile_pt.yaml` / `profile_en.yaml`: "Process2Diagram
  (P2D): plataforma de IA multi-agente (13 agentes - Orchestrator proprio em Python -
  LangGraph restrito a retry adaptativo de qualidade - Supabase) ... com validacao
  deterministica de qualidade (AgentValidator, sem uso de LLM) ..."
- Mencionado em `data/linkedin/about_pt.md`
- Fonte dos numeros revisados: `data/projetos/P2D_fonte_2026-07-03.md` (nota original de Pedro,
  parcialmente superada pela verificacao de codigo de 2026-07-12 acima)
- Publicar post no LinkedIn sobre o projeto

## Nota sobre exposicao tecnica (autor)

Ao contrario do material comercial (onde detalhes tecnicos ficam ocultos por protecao
competitiva), no CV a especificidade de stack (LangGraph, Supabase, contagem de ferramentas)
e mantida de proposito - e sinal de profundidade tecnica, nao risco de exposicao.
