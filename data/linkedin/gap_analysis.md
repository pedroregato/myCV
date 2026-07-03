# Gap Analysis — LinkedIn vs. CV (profile_pt.yaml)
# Gerado em: 2026-04-26
# Fonte LinkedIn: Profile.pdf exportado em Abr/2026

Este documento lista todas as divergências encontradas entre o perfil real do LinkedIn
e os dados atualmente em data/profile_pt.yaml. Serve de guia para decidir o que atualizar no CV.

---

## 1. CORREÇÕES OBRIGATÓRIAS (dados incorretos no CV)

### 1.1 LinkedIn URL
- **CV atual:** `https://www.linkedin.com/in/pedro-regato-0b6b3b13/`
- **LinkedIn real:** `https://www.linkedin.com/in/pedro-gentil-regato-de-oliveira-soares-46916823`
- **Ação:** Atualizar `linkedin_url` em profile_pt.yaml e profile_en.yaml

### 1.2 Números do projeto SJUR (RESOLVIDO em 2026-07-03)
- **CV atual (era):** R$ 27,3 milhões · 4.977 processos · 92% acurácia
- **LinkedIn real (Abr/2026):** R$ 28 milhões · 4.980 processos saneados em 2025 · R$ 103M monitorados · 3.765 novos em 2026 (1º tri)
- **Definição final:** R$28M refere-se a economia de provisionamento contábil anual (CPC 25),
  gerada por reclassificação mais precisa do risco jurídico dos processos monitorados — não
  ao valor total de exposição monitorada (esse é um número distinto, ~R$103M).
- **Ação:** Concluída — bullet em `destaques`, `experiencia[FGV].detalhes`, `linkedin/experience/fgv_pt.md`,
  `linkedin/experience/fgv_en.md`, `linkedin/about_pt.md`, `linkedin/about_en.md`, `projetos/fgv/sjur.md`
  e `projetos/catalog.yaml` atualizados para deixar explícito que o valor é economia de
  provisionamento anual, não exposição monitorada.

---

## 2. LACUNAS NO CV (projetos/informações que existem no LinkedIn mas não no CV)

### 2.1 Projeto Process2Diagram (open source)
- **O que é:** Ferramenta que converte transcrições de reunião em diagramas BPMN 2.0,
  atas estruturadas e requisitos IEEE 830 em uma execução automatizada.
- **Stack:** Python, LangGraph, LLMs
- **Onde incluir:** Novo destaque em `destaques` e/ou novo bullet em `experiencia[FGV].detalhes`
- **Decisão:** [ ] Incluir no CV  [ ] Manter só no LinkedIn

### 2.2 SE-SUITE Utils (ferramenta interna FGV)
- **O que é:** Biblioteca Python desenvolvida para suprir lacunas da plataforma corporativa.
  Wrappers SOAP para 4 módulos (22+ operações), pipeline de migração idempotente
  (PDF, Word, Visio), motor OCR para organogramas, API REST via FastAPI, integração D4Sign.
- **Onde incluir:** Bullet em `experiencia[FGV].detalhes`
- **Decisão:** [ ] Incluir no CV  [ ] Manter só no LinkedIn

### 2.3 Projeto NDOC — Visão Computacional
- **O que é:** RetinaFace para legendagem automática de acervo fotográfico institucional da FGV.
- **Onde incluir:** Bullet em `experiencia[FGV].detalhes`
- **Decisão:** [ ] Incluir no CV  [ ] Manter só no LinkedIn

### 2.4 Projeto D&I — Diversidade & Inclusão
- **O que é:** Desenho estatístico e análise da pesquisa institucional de D&I da FGV.
- **Onde incluir:** Bullet em `experiencia[FGV].detalhes`
- **Decisão:** [ ] Incluir no CV  [ ] Manter só no LinkedIn

### 2.5 Certificações
Nenhuma certificação consta no CV atual. As do LinkedIn:
- ISO 20000
- ITIL FOUNDATION V2
- Feature Engineering
- Intermediate Machine Learning
- IBM Tivoli Security Solution Sales
- **Onde incluir:** Nova seção `certificacoes` no YAML (requer adição ao layout PDF)
- **Decisão:** [ ] Criar seção no CV  [ ] Manter só no LinkedIn

### 2.6 Stack tecnológico ampliado
O LinkedIn menciona tecnologias não listadas nas competências do CV:
- LangGraph, Streamlit, Docker, SOAP, D4Sign, RetinaFace (Visão Computacional)
- **Onde incluir:** `competencias` no YAML
- **Decisão:** [ ] Adicionar ao CV  [ ] Manter só no LinkedIn

---

## 3. DIVERGÊNCIAS EDITORIAIS (decisões de curadoria do CV)

### 3.1 Cargo e período na FGV — QUESTÃO EM ABERTO
- **CV:** "Estatístico Sênior | Arquiteto de Soluções Analíticas" — 2014 - Atual
- **LinkedIn:** "Analista de Dados Sênior & IA Aplicada" — abril de 2019 - Present
- **Situação confirmada (Abr/2026):** Há uma discrepância intencional entre o cargo formal
  registrado na folha de pagamento da FGV e a função real exercida.
  O cargo do contrato/RH é diferente do que Pedro efetivamente faz (liderança técnica em IA/ML/automação).
- **Implicação para o CV:** O CV deve refletir a função real, não o título do contrato.
  O título "Arquiteto de Soluções Analíticas" é uma descrição funcional, não o cargo formal.
- **Implicação para o LinkedIn:** O LinkedIn está usando um cargo mais próximo do contrato formal.
  Avaliar se vale atualizar o LinkedIn para o título funcional real.
- **Período (2014 vs 2019):** A ser esclarecido — Pedro estava na FGV antes de 2019 em
  outro cargo/contrato? Ou o início formal foi em 2019?
- **Decisão pendente:** [ ] Alinhar CV ao LinkedIn  [ ] Manter título funcional no CV  [ ] Atualizar LinkedIn

### 3.2 Experiências anteriores não presentes no CV
O LinkedIn lista uma trajetória muito mais longa (desde 1995). O CV foca nas 3 mais recentes.
Esta é uma decisão editorial válida — o CV de 1 página prioriza relevância sobre completude.
Experiências omitidas do CV (todas registradas em `data/linkedin/experience/historico_anterior_pt.md`):
- Trust Business Consulting EIRELI (2012 - atual, empresa própria)
- Pilates Studio & Terapias Lenir Cordeiro (2013 - atual, Sócio Diretor)
- MGN Informática (2018 - 2022, Analista BP)
- EPE (2015, Consultor)
- RioCard TI (2011-2013, ITIL V3)
- PMESP (2011-2012, ITIL)
- MULTITERMINAIS (2009-2010)
- Centro Ramakrishna Vedanta (2002-2010, Diretor)
- Probank (2006-2008)
- Xerox do Brasil (2005-2007, Oracle ERP) — diferente da consultoria Xerox (2012-2014)
- Golden Cross (2004-2006)
- GE Aviation (2000-2002)
- Zamboni Comercial (1995-2000)
- SAQ (1995-1996)
- **Decisão:** [ ] Manter CV curado (recomendado)  [ ] Adicionar seção "Histórico Resumido"

### 3.3 Resumo profissional
- **CV:** Tom T-shaped, foco em "Modelo → Sistema → Processo"
- **LinkedIn:** Tom mais direto, foco em resultados concretos e open source
- Ambos válidos para canais diferentes. O LinkedIn está mais atualizado e específico.
- **Decisão:** [ ] Atualizar resumo do CV  [ ] Manter versões diferentes por canal

---

## 4. RESUMO DE AÇÕES SUGERIDAS

| Prioridade | Item | Esforço |
|---|---|---|
| ALTA | Corrigir LinkedIn URL nos YAMLs | Mínimo |
| ~~ALTA~~ | ~~Atualizar números SJUR (R$ 28M, 4.980, 3.765)~~ | ~~Mínimo~~ — concluído 2026-07-03 |
| MÉDIA | Adicionar Process2Diagram como destaque | Baixo |
| MÉDIA | Atualizar stack: LangGraph, Streamlit, Docker | Baixo |
| MÉDIA | Decidir cargo/período FGV (2014 vs 2019) | Editorial |
| BAIXA | Adicionar SE-SUITE Utils, NDOC, D&I como bullets | Baixo |
| BAIXA | Criar seção Certificações no CV | Médio (requer layout) |
| BAIXA | Atualizar resumo profissional | Editorial |
