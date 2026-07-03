# Career Card — SJUR (Superintendencia Juridica FGV)
# Projeto FGV | Status: Ativo
# Atualizado: 2026-07-03

**Nota de nomenclatura (2026-07-03):** este projeto NAO deve ser confundido com o
"DataJud Monitor", projeto autoral pessoal (plataforma web multi-tribunal com planos/cotas,
ainda nao comercializada) documentado em `data/projetos/datajud_monitor.md`. Ambos consultam
a mesma API publica do DataJud/CNJ, mas sao sistemas distintos: este aqui e o trabalho feito
para a Superintendencia Juridica da FGV (monitoramento processual + classificador SERDON via IA).

---

## Identificacao

- **Projeto:** SJUR (Superintendencia Juridica FGV) - Monitoramento Processual & Classificacao de Diarios Oficiais
- **Periodo:** 2023 - atual
- **Status:** Em andamento
- **Minha funcao:** Desenvolvedor principal / Responsavel tecnico

## Problema resolvido

O Supremo Tribunal Federal (STF) distribui automaticamente processos ao SJUR (Setor
Juridico da FGV) via DataJud (CNJ). Sem monitoramento, processos chegavam sem triagem,
sem alertas e sem visibilidade de volume ou prazo. A equipe juridica operava de forma
reativa, sem dados para planejar a carga de trabalho.

## Solucao implementada

Sistema automatizado de monitoramento do DataJud que:
- Consulta a API do CNJ periodicamente para capturar novos processos
- Classifica e prioriza processos por tipo, prazo e urgencia
- Gera alertas para a equipe juridica
- Produz relatorios de volume e tendencias (dashboard Streamlit)
- Mantem historico para analise de carga por periodo

## Stack principal

Python - Requests (API CNJ/DataJud) - Streamlit - pandas - SQLite/PostgreSQL
(preencher com stack real do projeto)

## Impacto mensuravel

- R$28M em economia de provisionamento contabil anual (CPC 25), via reclassificacao mais precisa
  do risco juridico dos processos monitorados
- 4.980 processos acompanhados em 2025
- 3.765 novos processos no 1T2026
- Reducao do tempo de triagem manual (preencher % ou horas/semana)
- Visibilidade completa do pipeline juridico (antes: zero)

## Decisoes tecnicas importantes

- (Preencher: por que Streamlit vs outra solucao de dashboard?)
- (Preencher: como foi modelado o banco de dados de processos?)
- (Preencher: estrategia de polling vs webhook na API do CNJ)

## Uso do Claude Code

(Preencher: quais partes foram desenvolvidas com Claude Code?
Ex: geracao do cliente API, modelagem do banco, dashboard Streamlit, etc.)

## Bullet CV (rascunho)

Desenvolvi ecossistema juridico-IA para o SJUR/FGV: (1) monitor do DataJud/CNJ
acompanhando +4.900 processos, gerando R$28M em economia de provisionamento contabil
anual via reclassificacao de risco; (2) classificador de citacoes
em Diarios Oficiais via LLM (DeepSeek/GPT/Gemini/Llama), processando 11.998 e-mails
da SERDON com 88% de acuracia — detectando processos desconhecidos antes que prazos
processuais comecem a correr.

## Iniciativas relacionadas

### POC: Classificacao de Recortes SERDON (maio/2025)

Prova de conceito separada, iniciada em maio/2025, para deteccao precoce de citacoes
da FGV em Diarios Oficiais — situacao em que a API do DataJud (CNJ) nao pode ajudar
porque o numero do processo ainda e desconhecido.

**Contexto do problema:**
A SERDON e uma empresa contratada pela FGV que monitora Diarios Oficiais e envia
por e-mail recortes de publicacoes relacionadas a FGV. O problema critico: quando a
FGV e citada como re em um processo novo, a citacao aparece no Diario Oficial antes
que o SJUR saiba da existencia do processo — ou seja, nao ha numero de processo para
consultar no DataJud. Sem monitoramento, a FGV pode perder prazos processuais por
simplesmente nao saber que foi citada.

**Solucao:**
Pipeline multi-classificador que ingere e-mails HTML do Outlook (via OutlookIngestor),
extrai os recortes do Diario Oficial enviados pela SERDON e classifica cada publicacao
em tres categorias:

- **"citacao"** - FGV esta sendo citada como re em processo novo (critico: prazo comeca a correr)
- **"intimacao"** - FGV ja e parte conhecida e esta sendo intimada em processo existente
- **"nao previsto"** - outros tipos de publicacao sem urgencia processual imediata

**Arquitetura:**
- **5 classificadores paralelos** ativados via `.env`: Regex (heuristica, sempre disponivel),
  DeepSeek (`deepseek-chat`), GPT-3.5, Gemini, Llama 2 (local via `llama-cpp-python`)
- **Classificador principal (DeepSeek):** temperature=0.0 (determinístico), max_tokens=300,
  prompt estruturado com 4 exemplos few-shot e regras explicitas para Mandado de Seguranca
- **Fallback heuristico:** keywords como "intime-se" e "fundacao getulio vargas" com
  scores de confianca (0.7-0.9) quando a API falha
- **Extracao de metadados:** numero do processo, prazos com contagem de dias, partes envolvidas
- **Banco SQLite** com tabelas: emails, recortes, partes, metadados
- **Interface Voila** (Jupyter -> web app) com 4 abas: classificacao, busca, regex, avaliacao
- **Dashboard Streamlit** para exploracao e filtragem dos resultados com exportacao CSV

- **Repositorio:** https://github.com/pedroregato/FGV-SJUR-POC-VOILA (publico)
- **Stack:** Python - DeepSeek API - Gemini API - OpenAI API - llama-cpp-python - Voila -
  Streamlit - SQLite - spaCy (`pt_core_news_lg`) - BeautifulSoup4 - Docker
- **Status:** POC funcional com pipeline completo (maio/2025)
- **11.998 e-mails SERDON processados** com **88% de acuracia** na classificacao
- **(Preencher: integracao futura com o monitoramento de processos do SJUR apos identificar o numero do processo?)**

**Por que e complementar ao monitoramento de processos do SJUR:**
O monitoramento de processos do SJUR rastreia processos **conhecidos**. O classificador SERDON detecta
processos **desconhecidos** a partir da citacao no Diario Oficial. Juntos cobrem o
ciclo completo: descoberta de citacao -> identificacao do processo -> monitoramento continuo.

---

## Proximos passos

- Classificacao de recortes SERDON (POC em andamento — FGV-SJUR-POC-VOILA)
- (Preencher: integracao entre o monitoramento de processos do SJUR e o classificador de recortes?)
- (Preencher: machine learning para priorizacao de processos por perfil de risco?)
- (Preencher: expansao do monitoramento para outros setores da FGV?)

## Notas para sincronizacao

- Dados de volume (R$28M em economia de provisionamento anual, 4.980 processos) sao publicos/internos FGV - ok para CV
- Nao mencionar detalhes de processos especificos ou partes envolvidas
- Titulo "SJUR" pode precisar de expansao para quem nao conhece a FGV

---
<!-- Ultima atualizacao: 2026-04-27 -->
