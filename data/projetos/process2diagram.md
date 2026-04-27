# Career Card — Process2Diagram
# Status: Ativo | Visibilidade: Publico (open source)
# Repositorio: https://github.com/pedroregato/Process2Diagram
# Claude Code: Sim
# Atualizado: 2026-04-27

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
como fonte unica de verdade entre agentes):

- **Quality Inspector** - classifica a transcricao de A a E com criterios ponderados
- **Preprocessor** - remove ruidos de ASR, pausas, fillers (sem LLM, Python puro)
- **NLP Chunker** - spaCy NER para reconhecimento de entidades e atores
- **BPMN Architect** - extracao via LLM + auto-repair determinístico em 4 passagens
- **Minutes & Requirements** - executam em paralelo via ThreadPoolExecutor
- **SBVR & BMM Agents** - extracao semantica opcional
- **Executive Synthesizer** - gera relatorio HTML com sidebar e comentarios

**Mecanismos de qualidade:**
- LangGraph Adaptive Retry: re-executa o agente BPMN ate atingir threshold de qualidade (max 5 tentativas)
- Tournament mode: gera 1, 3 ou 5 candidatos BPMN e seleciona o melhor por scoring ponderado
- ROI-TR Dashboard: metrica de qualidade de reuniao (0-10) com 11 tipos classificados e matrizes de peso dinamicas

## Tecnologias

Python 3.13 - Streamlit - LangGraph - spaCy (`pt_core_news_lg`) -
Anthropic Claude (claude-sonnet-4-20250514) - DeepSeek - OpenAI - Groq - Gemini -
ThreadPoolExecutor - python-docx - PyMuPDF - BPMN 2.0 XML

## Uso do Claude Code

Desenvolvido integralmente com Claude Code como parceiro de desenvolvimento:
- Arquitetura do pipeline multi-agente e padrao KnowledgeHub
- Implementacao dos agentes especializados e do BaseAgent com retry e token tracking
- Algoritmos de layout BPMN (eliminacao de lane-crossing, alinhamento de branches paralelos)
- Sistema de auto-repair determinístico (4 passagens sem LLM)
- Suite de testes (106 testes unitarios, zero chamadas LLM)
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

4. **Multi-provider LLM** - suporte a 5 providers permite ao usuario escolher entre
   custo (DeepSeek), velocidade (Groq), qualidade (Claude) ou tier gratuito (Gemini)

## Status atual

**v4.14** - Em producao no Streamlit Cloud com auto-deploy no push para `main`.
106 testes unitarios passando (~0.5s de execucao, zero chamadas LLM).
Repositorio criado em marco/2026, evolucao ativa.

## Impacto / Metricas

- 7 tipos de artefato gerados em execucao unica a partir de uma transcricao
- 106 testes unitarios sem mock de LLM (cobertura de auto-repair, validacao estrutural,
  scoring 4-dimensional, geracao Mermaid)
- Deploy continuo: Streamlit Cloud com CI/CD automatico no push
- (Preencher: numero de usuarios? transcricoes processadas? feedback coletado?)

## Referencias no CV/LinkedIn

- Destaque em `profile_pt.yaml`: "Process2Diagram (open source): reunioes -> BPMN 2.0..."
- Mencionado em `data/linkedin/about_pt.md`
- Publicar post no LinkedIn sobre o projeto
