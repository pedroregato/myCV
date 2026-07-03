# Career Card — Process2Diagram (P2D)
# Status: Ativo | Visibilidade: Publico (open source)
# Repositorio: https://github.com/pedroregato/Process2Diagram
# Claude Code: Sim
# Atualizado: 2026-07-03 (numeros revisados - ver nota abaixo)

**Nota de atualizacao (2026-07-03):** os numeros deste card estavam desatualizados
(106 testes, 5 providers, 7 artefatos). Valores corrigidos abaixo com base em dados
fornecidos diretamente por Pedro. A secao "Arquitetura" (lista de agentes) ainda reflete
a versao anterior (7 papeis nomeados) - **preencher** os 2 agentes/papeis que faltam
para fechar em 9, e detalhar o assistente conversacional (~125 ferramentas) e a camada
de conformidade LGPD, nenhum dos quais esta descrito na secao de Arquitetura ainda.

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

Python 3.13 - Streamlit - LangGraph - Supabase - spaCy (`pt_core_news_lg`) -
Anthropic Claude (claude-sonnet-4-20250514) - DeepSeek - OpenAI - Groq - Gemini - Grok -
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

Em producao continua no Streamlit Cloud com auto-deploy no push para `main`.
345 testes automatizados passando. Repositorio criado em marco/2026, evolucao ativa.

## Impacto / Metricas

- 12 artefatos formais gerados em execucao unica a partir de uma transcricao: diagramas
  BPMN 2.0 e Mermaid, atas estruturadas, requisitos IEEE 830, vocabulario SBVR, modelo BMM,
  tabelas DMN 1.4 e grafo de conhecimento entre reunioes
- Pipeline de 9 agentes especializados orquestrados (Python - LangGraph - Supabase)
- Assistente conversacional com ~125 ferramentas de consulta/escrita sobre o historico do projeto
- Suporte a 6 provedores LLM (DeepSeek, Claude, OpenAI, Gemini, Groq, Grok)
- Camada de conformidade LGPD nativa
- 345 testes automatizados, em producao continua
- Deploy continuo: Streamlit Cloud com CI/CD automatico no push
- (Preencher: numero de usuarios? transcricoes processadas? feedback coletado?)

## Referencias no CV/LinkedIn

- Portfolio de Projetos Pessoais em `profile_pt.yaml` / `profile_en.yaml`: "Process2Diagram
  (P2D): plataforma de IA multi-agente (9 agentes - LangGraph - Supabase)..."
- Mencionado em `data/linkedin/about_pt.md`
- Fonte dos numeros revisados: `data/projetos/P2D_fonte_2026-07-03.md` (nota original de Pedro)
- Publicar post no LinkedIn sobre o projeto

## Nota sobre exposicao tecnica (autor)

Ao contrario do material comercial (onde detalhes tecnicos ficam ocultos por protecao
competitiva), no CV a especificidade de stack (LangGraph, Supabase, contagem de ferramentas)
e mantida de proposito - e sinal de profundidade tecnica, nao risco de exposicao.
