# Análise de Aderência — Perfis Profissionais DTI/TI com foco em IA
**Elaborado por:** Pedro Gentil Regato de Oliveira Soares
**Destinatário:** [Nome do Gestor] — Gestor de Soluções Corporativas / DTI/FGV
**Data:** Maio de 2026
**Referência:** Documento "Job Descriptions DTI v2 IA" — Modelos de JD, Área DTI/TI

> **Nota (2026-07-12):** este documento tem um **Adendo v2** ao final, com atualização de
> itens de Cloud, Governança de IA e Observabilidade/FinOps com base em verificação direta
> do código-fonte do Process2Diagram (não inferência). O corpo original abaixo foi mantido
> inalterado como registro do que foi enviado em Maio/2026.

---

## Apresentação

Atendendo à solicitação do meu gestor, elaborei esta análise de aderência aos três perfis descritos no documento de referência. O objetivo é oferecer uma avaliação honesta, baseada em evidências concretas do meu histórico na FGV e fora dela, identificando onde atendo plenamente, onde supero e onde há lacunas reais a reconhecer.

A análise segue a estrutura exata de cada JD e é complementada, ao final, por uma proposta de perfil que entendo aproveitar ao máximo a combinação de competências que acumulei ao longo desta trajetória.

---

## 1. ARQUITETO DE SOLUÇÕES

### 1.1 Requisitos Obrigatórios

| Requisito | Situação | Evidência |
|---|---|---|
| Graduação em Ciência da Computação, Sistemas de Informação, Engenharia ou áreas correlatas | ⚠️ Parcialmente atendido | Graduação em **Estatística (UERJ, 1984–1990)** + **MBA FGV (2012–2014)**. A formação não é em TI clássica, mas confere base matemática e de modelagem superior à maioria dos graduados em computação, além de visão de negócio formal. |
| Experiência mínima de 5 anos em desenvolvimento de software e ao menos 2 anos em função de arquitetura | ✅ Amplamente superado | Carreira em TI/Sistemas desde **1993 (mais de 30 anos)**. Atuação em arquitetura de soluções desde os projetos na Xerox Brasil (2006), EPE, Path ITTS e, de forma sistemática, na FGV desde 2019. |
| Sólido conhecimento em arquitetura de microsserviços, APIs REST/GraphQL e integração de sistemas | ✅ Atendido | Projetei e implementei: **FastAPI/Docker** (SE-SUITE Utils, FGV); wrappers **SOAP** para 22+ operações no SE-Suite; **Flask/JWT** em produção no HPC FGV (CIDA); integração via **API CNJ** (monitoramento processual do SJUR). |
| Experiência com plataformas Cloud (AWS, Azure ou GCP) e seus serviços de IA nativos | ⚠️ Gap a desenvolver | Minha experiência é predominantemente **on-premise** (HPC FGV, servidores locais). Tenho noções de Cloud e uso de APIs gerenciadas (Gemini, DeepSeek via APIs externas), mas não tenho experiência formal com AWS Bedrock, Azure OpenAI ou Vertex AI como plataforma de infraestrutura. É o gap técnico mais relevante a declarar. |
| Conhecimento prático no consumo de APIs de LLMs (OpenAI, Anthropic, etc.): autenticação, estrutura de prompts, tokens, custos e limites | ✅ Amplamente superado | Implementei em produção: classificador de citações em Diários Oficiais via **DeepSeek, Gemini e Llama** (11.998 e-mails, 88% de acurácia); **Claude API** integrada via Anthropic SDK no myCV e em ferramentas internas. Gerencio contexto, custo por token, limites de janela e fallback entre modelos. |
| Domínio de padrões de segurança, autenticação (OAuth, JWT) e conformidade com LGPD | ✅ Atendido | **JWT/OAuth** implementados em múltiplos projetos: CIDA (API Flask/JWT em produção no HPC FGV), **NDOC** (API de legendagem inteligente de faces — RetinaFace) e **SE-SUITE Utils** (autenticação nas integrações SOAP/REST com o SE-Suite). Atuação direta com **D4Sign** (assinatura digital com cadeia de custódia) no Portal de Contratos FGV — 1.330 instrumentos contratuais. Conhecimento de LGPD aplicado à gestão de dados do SJUR e do acervo acadêmico. |
| Capacidade de modelar arquiteturas que incorporam componentes de IA de forma segura e auditável | ✅ Superado | O **SJUR** é um ecossistema IA completo com dois subsistemas em produção: monitoramento processual (consulta CNJ, alerta jurídico) e classificador LLM de Diários Oficiais — ambos com lógica de auditoria, log de decisões e rastreabilidade de outputs. O **Process2Diagram** gera artefatos estruturados (BPMN 2.0 + IEEE 830) a partir de reuniões — rastreabilidade total do processo à decisão. |
| Comunicação técnica clara com equipes de desenvolvimento e lideranças de negócio | ✅ Superado | Atuo como elo técnico direto entre a Diretoria Jurídica, Auditoria, Área Acadêmica e a DTI. Produzo documentação técnica, especificações funcionais e apresentações executivas. Depoimentos de gestores (Rodrigo Gaio/Xerox, Joaquim Santos Neto/CIO) corroboram esta capacidade. |

### 1.2 Diferenciais Desejáveis

| Diferencial | Situação | Evidência |
|---|---|---|
| Certificações em Cloud (AWS Solutions Architect, Azure, etc.) | ❌ Não possuo | Gap declarado. Ação possível: AWS Cloud Practitioner como primeiro passo. |
| Experiência com RAG (Retrieval-Augmented Generation) | ✅ Atendido | RAG é parte da arquitetura do SJUR (recuperação de contexto processual antes da classificação LLM) e do Process2Diagram. |
| Conhecimento em LangChain, LlamaIndex ou frameworks de orquestração de IA | ✅ Atendido | Uso **LangGraph** (framework de orquestração de agentes IA da LangChain) no Process2Diagram e no SJUR — o equivalente moderno e mais robusto do LangChain para pipelines com estado. |
| Vivência com projetos de transformação digital com componentes de IA generativa | ✅ Amplamente superado | SJUR, CIDA, NDOC e Process2Diagram são quatro projetos de transformação digital com IA generativa, ML e visão computacional, todos em produção na FGV. |
| Experiência em definição de políticas de uso responsável de IA em ambientes corporativos | ✅ Parcialmente atendido | Defini critérios de qualidade, log de decisões e validação humana nos pipelines IA do SJUR. Formalização explícita de política de IA corporativa ainda não realizada — mas a prática está presente. |

### 1.3 Avaliação Global — Arquiteto de Soluções

> **Aderência estimada: 82%**
>
> Atendo ou supero a grande maioria dos requisitos obrigatórios e dos diferenciais. O gap principal e honesto é a **ausência de experiência formal com Cloud** (AWS/Azure/GCP como infraestrutura). A formação em Estatística, embora diferente do esperado, é um diferencial estratégico — não uma deficiência — especialmente para um papel de arquitetura onde decisões sobre modelos, risco e governança de IA exigem base quantitativa sólida.

---

## 2. ANALISTA DE SISTEMAS / NEGÓCIO

### 2.1 Requisitos Obrigatórios

| Requisito | Situação | Evidência |
|---|---|---|
| Graduação em Sistemas de Informação, Administração, Engenharia ou correlatas | ⚠️ Parcialmente atendido | Mesma situação do perfil anterior: Estatística + MBA FGV. Equivalente em substância. |
| Experiência mínima de 3 anos como analista de sistemas ou de negócios | ✅ Amplamente superado | 30+ anos. Atuação formal como Analista de Sistema desde 1993 (CBO 8320). |
| Uso comprovado de ferramentas de IA generativa em atividades profissionais | ✅ Amplamente superado | Uso diário de Claude, Gemini, DeepSeek e Llama em produção. Integração via SDK (Anthropic Python SDK). Não só uso, mas **construo e opero** os sistemas que outros analistas usarão. |
| Capacidade de construir prompts estruturados para outputs úteis e consistentes | ✅ Amplamente superado | Engenharia de Prompt é parte formal da minha stack. Implemento chain-of-thought, few-shot, role prompting e decomposição de tarefas nos pipelines do SJUR e Process2Diagram. |
| Domínio de levantamento e documentação de requisitos e modelagem de processos (BPMN) | ✅ Amplamente superado | **Process2Diagram** automatiza exatamente isso: de transcrições de reunião para BPMN 2.0 + atas estruturadas + requisitos IEEE 830. Fui eu quem projetou, construiu e opero esta solução. Décadas de BPM na Xerox, Path ITTS, EPE e FGV. |
| Experiência com metodologias ágeis (Scrum, Kanban) e ferramentas de backlog | ✅ Atendido | Scrum/Kanban presentes em todos os projetos recentes na FGV. |
| Habilidade com ferramentas de documentação colaborativa (Confluence, Notion, etc.) | ⚠️ Parcialmente atendido | Uso documentação estruturada em Markdown, YAML e repositórios Git. Experiência limitada com Confluence/Notion especificamente — uso ferramentas equivalentes. |
| Capacidade de redigir documentos técnicos, revisando outputs de IA | ✅ Amplamente superado | Produção regular de especificações, relatórios técnicos e documentação de projetos. O próprio Process2Diagram gera e valida atas e especificações IEEE 830. |

### 2.2 Diferenciais Desejáveis

| Diferencial | Situação | Evidência |
|---|---|---|
| Automação de fluxos com IA (Make, n8n com LLMs, etc.) | ✅ Superado | LangGraph é minha ferramenta de orquestração de fluxos com IA — mais sofisticada que Make/n8n. Process2Diagram é a prova. |
| Técnicas avançadas de prompting (chain-of-thought, few-shot, role prompting) | ✅ Superado | Uso sistemático nos pipelines em produção. Participei do **GenAI Intensive Google/Kaggle** (5 cursos, Abr/2025) com foco específico nessas técnicas. |
| Certificação em gestão ágil (CSPO, PSM, PMI-ACP) | ❌ Não possuo | Gap a declarar. A prática está presente; a certificação formal não. |
| Ferramentas de prototipagem rápida assistida por IA | ✅ Atendido | **Streamlit** para prototipagem rápida de interfaces de dados (monitoramento processual do SJUR). |
| Vivência em projetos de transformação digital com automação inteligente | ✅ Amplamente superado | SJUR, CIDA, ECM & BPM, Process2Diagram — quatro projetos distintos, todos na FGV. |

### 2.3 Avaliação Global — Analista de Sistemas / Negócio

> **Aderência estimada: 91%**
>
> Este é o perfil ao qual tenho maior aderência técnica imediata. Em vários requisitos não apenas atendo, mas **opero na camada acima** — construo os sistemas que outros analistas usariam como ferramenta. Os únicos gaps são a ausência de certificação ágil formal e experiência específica com Confluence/Notion.

---

## 3. DESENVOLVEDOR FULL STACK

### 3.1 Requisitos Obrigatórios

| Requisito | Situação | Evidência |
|---|---|---|
| Graduação em Ciência da Computação, Sistemas de Informação ou correlatas | ⚠️ Parcialmente atendido | Idem aos perfis anteriores. |
| Experiência mínima de 3 anos em desenvolvimento de software | ✅ Amplamente superado | 30+ anos. Backend profissional desde 1993. |
| Uso comprovado de ferramentas de IA no desenvolvimento | ✅ Amplamente superado | Uso **Claude Code** como ferramenta de desenvolvimento no dia a dia. Integro APIs de LLMs em código Python. |
| Backend sólido (Java, Python, Node.js ou .NET) | ✅ Atendido (Python) | **Python** é minha linguagem principal. FastAPI, Flask, Pandas, NumPy, Scikit-learn, LangGraph. Histórico com Java, PL/SQL e Groovy/Grails. |
| Frontend (React, Angular ou Vue.js) | ⚠️ Gap relevante | Minha atuação em frontend é limitada. Uso **Streamlit** para interfaces de dados, mas não tenho experiência formal com React, Angular ou Vue. Este é um gap real para o perfil Full Stack clássico. |
| Experiência no consumo de APIs REST e integração de APIs de terceiros, incluindo IA | ✅ Amplamente superado | Integração com API CNJ, D4Sign, Anthropic SDK, APIs de LLMs. 22+ operações SOAP documentadas no SE-SUITE Utils. |
| Domínio de bancos de dados relacionais e noções de NoSQL | ✅ Atendido | SQL avançado em múltiplos projetos. DB2 (IBM Maximo), Oracle (Xerox/PUC/Petrobras). Noções de NoSQL. |
| OAuth 2.0, JWT | ✅ Atendido | JWT/OAuth implementados em três projetos FGV: **CIDA** (API Flask/JWT em produção), **NDOC** (API de legendagem inteligente de faces) e **SE-SUITE Utils** (autenticação nas integrações SOAP/REST com o SE-Suite). |
| Git e fluxos de pull request e code review | ✅ Atendido | Git em uso sistemático em todos os projetos. |

### 3.2 Diferenciais Desejáveis

| Diferencial | Situação | Evidência |
|---|---|---|
| APIs de LLMs em produção (gestão de contexto, streaming, custos) | ✅ Amplamente superado | SJUR em produção com controle de contexto, seleção dinâmica de modelo e monitoramento de custo. |
| LangChain, LlamaIndex ou similares | ✅ Atendido | LangGraph. |
| RAG aplicado a bases de conhecimento corporativas | ✅ Atendido | Presente na arquitetura do SJUR. |
| Docker e orquestração de containers | ✅ Atendido | Docker em uso no SE-SUITE Utils e nos ambientes de deploy na FGV. |
| Microsserviços e integração de sistemas complexos | ✅ Parcialmente atendido | FastAPI como serviço isolado; não tenho experiência formal com Kubernetes ou orquestração de múltiplos microsserviços. |

### 3.3 Avaliação Global — Desenvolvedor Full Stack

> **Aderência estimada: 72%**
>
> Atendo plenamente o lado **backend, IA e integração** do perfil Full Stack, mas tenho lacuna real em **frontend moderno** (React/Angular/Vue). Este perfil é o que menos representa minha posição natural — não porque me falte capacidade técnica, mas porque minha atuação evoluiu na direção de arquitetura e inteligência aplicada, não de interface e UX.

---

## 4. SÍNTESE COMPARATIVA

| Dimensão | Arquiteto de Soluções | Analista Sist./Negócio | Dev Full Stack |
|---|---|---|---|
| Formação acadêmica | ⚠️ Equivalente | ⚠️ Equivalente | ⚠️ Equivalente |
| Experiência de mercado | ✅✅ Supera amplamente | ✅✅ Supera amplamente | ✅✅ Supera amplamente |
| LLMs / IA Generativa em produção | ✅✅ Supera amplamente | ✅✅ Supera amplamente | ✅✅ Supera amplamente |
| Arquitetura de sistemas e APIs | ✅ Atende | ✅ Atende | ✅ Atende |
| BPMN / Modelagem de Processos | ✅✅ Supera amplamente | ✅✅ Supera amplamente | — |
| Cloud (AWS/Azure/GCP) | ⚠️ Gap | — | — |
| Frontend moderno (React/Angular) | — | — | ⚠️ Gap |
| Certificações formais (Cloud/Ágil) | ❌ Ausente | ❌ Ausente (ágil) | — |
| **Aderência estimada** | **82%** | **91%** | **72%** |

---

## 5. PONTOS DE DESENVOLVIMENTO PRIORITÁRIOS

Com base na análise honesta acima, identifico três frentes de desenvolvimento para maximizar a aderência formal aos perfis:

### 5.1 Cloud — Gap Técnico mais Relevante
A ausência de experiência formal com AWS, Azure ou GCP é o gap mais substancial para o perfil de Arquiteto. Ação recomendada:
- **AWS Cloud Practitioner** (fundamentos, 1–2 meses)
- **AWS Solutions Architect Associate** (6 meses) ou equivalente Azure
- Prática com serviços de IA nativos: AWS Bedrock, Azure OpenAI Service

### 5.2 Certificação Formal em Gestão Ágil
A prática está consolidada; falta o reconhecimento formal.
- **PMI-ACP** ou **PSM I** são os mais alinhados ao perfil sênior

### 5.3 Formalização de Política de IA Corporativa
Tenho prática de governança de IA nos projetos, mas nunca produzi um documento formal de política. Produzir um whitepaper de uso responsável de IA para a FGV seria simultaneamente um entregável de valor e um item de portfólio para o perfil de Arquiteto.

---

## 6. PROPOSTA DE CARGO — APROVEITAMENTO MÁXIMO DO PERFIL

Com base no cruzamento do meu perfil real com os três JDs analisados, proponho a seguinte posição:

---

### ESPECIALISTA EM IA APLICADA — SOLUÇÕES INTELIGENTES PARA ÁREAS CORPORATIVAS

**Posicionamento estratégico:**
Este cargo existe para transformar o potencial da Inteligência Artificial em **resultado concreto para as áreas corporativas da FGV**. Seu centro de gravidade é o negócio: identificar onde a IA pode gerar impacto real, especificar o que precisa ser construído e estar à frente da sua implementação junto às áreas clientes da SOLCORP — com responsabilidade sobre entrega, adoção e resultado mensurável.

A IA aplicada a processos corporativos é uma disciplina própria. Exige fluência técnica em modelos, pipelines e integração de dados, combinada com leitura precisa do negócio, dos processos e das pessoas envolvidas. É essa combinação — rara no mercado — que justifica um perfil dedicado, com foco, metodologia e histórico de entrega comprovados.

**Por que este cargo aproveita ao máximo o que tenho:**

1. **Base estatística + IA aplicada** — Não sou apenas um engenheiro que usa LLMs. Sou um estatístico que entende distribuições, erro, risco e evidência. Isso é raro em perfis de IA corporativa e produz decisões mais sólidas sobre quando confiar num modelo, quando não confiar e como medir seu desempenho em produção.

2. **Visão de processo + automação inteligente** — Process2Diagram é a síntese desta competência: transformar reuniões em BPMN, atas e requisitos automaticamente não é um projeto de TI — é uma reengenharia de processo habilitada por IA. Isso exige simultaneamente domínio de BPM e de orquestração de LLMs.

3. **Histórico de entrega em produção, com métricas de negócio** — SJUR, CIDA, NDOC e Process2Diagram são sistemas em operação real, com resultados verificáveis: R$ 28M em economia de provisionamento contábil anual, >96% de acurácia em classificação documental, 11.998 e-mails classificados com 88% de acurácia. Não são POCs ou pilotos.

4. **Trânsito entre negócio e tecnologia** — Atuo com igual fluência na conversa com a Diretoria Jurídica e na depuração de um pipeline LangGraph. Esse trânsito bidirecional é exatamente o que este cargo exige: traduzir problemas de negócio em soluções técnicas viáveis e comunicar resultados de volta às lideranças em linguagem de impacto.

5. **Capacidade de institucionalizar sem criar dependência** — Minha experiência em ITIL, BPM e ISO 20000 me permite projetar soluções de IA que se tornam serviços sustentáveis — com documentação, rastreabilidade e handover — e não iniciativas pessoais que morrem quando o especialista sai.

**Responsabilidades sugeridas para o cargo:**
- Mapear e priorizar oportunidades de uso de IA nas áreas corporativas da FGV (Jurídico, Contratos, Acadêmico, Auditoria, RH), com análise de viabilidade e retorno esperado
- Especificar os requisitos funcionais das soluções de IA demandadas pelas áreas de negócio, estando à frente da sua implementação junto às áreas clientes da SOLCORP
- Projetar, implementar e operar soluções de IA aplicada (LLMs, RAG, agentes, ML/NLP, visão computacional) com responsabilidade sobre resultado e continuidade operacional
- Medir e reportar os resultados das soluções implementadas: acurácia, economia gerada, processos automatizados, satisfação das áreas
- Atuar como elo qualificado entre as áreas de negócio e a DTI, traduzindo necessidades em requisitos técnicos e resultados em linguagem executiva

**Nível sugerido:** Especialista Sênior / Analista de Sistemas Sênior com foco em IA Aplicada

---

## Consideração Final

Estou ciente da discussão em curso sobre a alocação de responsabilidades de IA na DTI. Do ponto de vista técnico e de histórico entregável, entendo que minha trajetória na FGV demonstra, de forma objetiva e verificável, uma combinação que não é comum: rigor quantitativo, domínio de processos de negócio, execução de IA em produção e capacidade de tradução entre técnica e estratégia.

Estou à disposição para aprofundar qualquer ponto desta análise, apresentar os projetos referenciados em maior detalhe ou contribuir na elaboração da proposta formal do cargo junto à liderança da companhia.

---
*Documento elaborado com apoio de Claude (Anthropic) | Maio de 2026*

---

# ADENDO v2 — Atualização por Verificação de Código (2026-07-12)

**Elaborado por:** Pedro Gentil Regato de Oliveira Soares
**Data:** 12 de julho de 2026
**Origem da evidência:** Claude Code rodando diretamente no repositório do Process2Diagram
(P2D), lendo código-fonte real — não é inferência nem atualização de intenção, é leitura
de implementação existente e testada.
**Objetivo:** Atualizar, com a mesma honestidade do documento original, os pontos da
análise de Maio/2026 que mudaram de situação desde então — sem inflar o que não mudou.

---

## 1. Itens que evoluíram de "gap declarado" ou "parcialmente atendido" para evidência concreta

### 1.1 Cloud / Azure AI Services — evoluiu, mas com nuance importante

**Situação em Maio/2026:** "Gap a desenvolver... não tenho experiência formal com AWS
Bedrock, Azure OpenAI ou Vertex AI como plataforma de infraestrutura."

**Situação em 12/07/2026:**
- **Azure OpenAI Service agora é capacidade real de produto**, não aspiracional: provider
  implementado no P2D (`client_type="azure_openai"` em `modules/config.py`, client dedicado
  `openai.AzureOpenAI`), coberto por 13 testes automatizados. O P2D orquestra hoje **7
  provedores LLM intercambiáveis** (DeepSeek, Anthropic Claude, OpenAI, Azure OpenAI,
  Google Gemini, Groq, xAI Grok).
- **O que continua sendo gap real, sem atalho:** existe infraestrutura como código pronta
  para Google Cloud Run (Docker multi-stage + Cloud Build), mas **nunca foi implantada em
  produção** — o deploy real e ao vivo do P2D continua sendo Streamlit Cloud. Não afirmo
  "experiência em produção com GCP"; afirmo "infraestrutura como código pronta para Cloud
  Run, deploy real via CI/CD em outra plataforma".
- **Leitura honesta:** o gap deixou de ser "nunca toquei nisso" e passou a ser "tenho a
  peça de integração com a plataforma gerenciada (Azure OpenAI) funcionando em produção,
  mas não tenho a peça de infraestrutura de nuvem (compute, rede, IAM) rodando ao vivo".
  São gaps de natureza diferente — o segundo é bem menor que o primeiro.

### 1.2 Governança de IA / Ética / LGPD — de prática informal para camada nomeada e auditável

**Situação em Maio/2026:** "Defini critérios de qualidade, log de decisões e validação
humana... Formalização explícita de política de IA corporativa ainda não realizada — mas
a prática está presente."

**Situação em 12/07/2026:** o P2D tem uma camada de compliance dedicada e nomeada como tal
(`modules/compliance/`: `detector.py`, `audit.py`, `consent.py`), com tabelas próprias em
produção (`compliance_consent`, `compliance_audit`):
- Pseudonimização reversível de dados pessoais em duas camadas — dados estruturados via
  regex e nomes próprios via reconhecimento de entidades (NER)
- Trilha de consentimento e auditoria versionadas em banco, não apenas log informal

**Caveat honesto que mantenho:** o isolamento multi-tenant (por `project_id`/`tenant_id`)
é real na camada de aplicação, mas Row Level Security (RLS) no Postgres está inconsistente
entre tabelas — algumas sem policy, outras com `USING(true)` permissivo, outras com RLS
explicitamente desabilitada. Não afirmo "isolamento completo a nível de banco de dados";
afirmo "isolamento multi-tenant na aplicação, com RLS parcial, item de hardening pendente".

### 1.3 Observabilidade / Monitoramento de Modelo / FinOps para IA — de "sem evidência" para sistema funcionando

**Situação em Maio/2026:** este item nem constava como atendido na análise original —
não havia sido mapeado como competência declarada.

**Situação em 12/07/2026:**
- Telemetria de chamadas LLM com detecção de anomalia de taxa de erro por provedor
- Rastreamento de taxa de saída bem-formada (schema validation) por agente e por versão
  de prompt ao longo do tempo — fecha o ciclo entre chamada de modelo e sinal acionável
- Ferramenta de modelagem de custo (`core/cost_model.py`) comparando 17 modelos em 6
  provedores por cenário de uso, com projeção de custo antes da execução — decisão de
  trade-off custo × qualidade orientada por dado, não por intuição

### 1.4 Copilots corporativos / assistentes inteligentes — de menção genérica para número verificado

O assistente conversacional do P2D tem **151 ferramentas** especializadas de consulta e
escrita sobre o histórico do projeto (contagem real via `get_tool_schemas_openai()`, não
estimativa), com busca semântica via pgvector e embeddings Matryoshka de 512 dimensões, e
um modo de análise autônoma multi-etapa (até 15 rounds) — um copilot corporativo embutido
no produto, não um wrapper genérico de chat.

---

## 2. O que continua honestamente em aberto — sem mudança

- **Certificações formais** (Azure AI Engineer, AWS Solutions Architect, AWS ML Specialty,
  Google Professional ML Engineer) — gap real, sem atalho de código. Continua exigindo
  estudo e prova.
- **Cloud em produção real como infraestrutura** (AWS/Azure/GCP hospedando a aplicação) —
  o que existe é integração com um serviço gerenciado (Azure OpenAI) e IaC pronta para
  Cloud Run, não uma operação viva nessas plataformas.
- **RLS completo / isolamento a nível de banco** — parcial, não vender como resolvido.
- **Data Lake / Data Warehouse** — o banco do P2D é Postgres transacional (OLTP) +
  pgvector, não um DW. Não forçar isso artificialmente para preencher checklist.

---

## 3. Revisão da aderência estimada — Arquiteto de Soluções

**Estimativa em Maio/2026:** 82%

**Estimativa revisada em 12/07/2026: ~86%**

**Racional da revisão:** o gap mais citado na análise original — "ausência de experiência
formal com Cloud (AWS/Azure/GCP) e seus serviços de IA nativos" — deixou de ser um gap
único e homogêneo. A parte "serviços de IA nativos" (Azure OpenAI Service) passou a ser
atendida com evidência de código em produção. A parte "infraestrutura de nuvem" continua
sendo gap real (IaC pronta, nunca implantada). Como o requisito original mistura as duas
coisas, a aderência sobe, mas não para o teto — o gap de infraestrutura viva permanece.
Os itens de governança de IA e observabilidade/FinOps, antes tratados como "prática
presente mas não formalizada", agora têm evidência nomeada e testável, o que também
reforça a nota sem depender de Cloud.

As avaliações de **Analista de Sistemas/Negócio (91%)** e **Desenvolvedor Full Stack
(72%)** não mudam de forma relevante com esta atualização — os gaps que definem essas
notas (Confluence/Notion, certificação ágil, frontend React/Angular/Vue) não foram
tocados pela verificação de código do P2D.

---

*Adendo elaborado com apoio de Claude Code (Anthropic), a partir de leitura direta do
código-fonte do Process2Diagram | 12 de julho de 2026*
