# Análise de Aderência — Analista de GenAI & ML (BTG Pactual)
**Elaborado por:** Pedro Gentil Regato de Oliveira Soares
**Data:** Setembro de 2026
**Referência:** `vagas/BTG-Pactual/2026-09.md`

---

## Veredito

Aderência **alta** — a mais forte entre as vagas analisadas até agora. É praticamente a interseção exata do seu perfil: LLMs + ML clássico + agentes + estatística, com produtos reais em produção. Localização (Rio de Janeiro, híbrido) também bate. Os gaps são pontuais (infra de deploy em nuvem e deep learning/fine-tuning) e concentrados nos "diferenciais", não nos requisitos centrais.

## Pontos fortes — aderência real

| Requisito da vaga | Evidência no perfil |
|---|---|
| Graduação em Estatística/áreas correlatas | Graduação em Estatística - UERJ (Dez/1990) |
| Rio de Janeiro, híbrido | Base em Rio de Janeiro - RJ |
| Integração com LLM (Azure OpenAI, Gemini) | Process2Diagram: 7 provedores LLM intercambiáveis incl. Azure OpenAI; SJUR: fallback multi-provedor (DeepSeek, Gemini, Llama) |
| Docker | Explícito nas competências ("Docker · Git + CI/CD") |
| ML clássico (scikit-learn, XGBoost, Pandas, NumPy) | Competência explícita "Machine Learning Clássico (Scikit-learn · XGBoost)" + "Python (Pandas · NumPy...)"; aplicado em produção no CIDA (96% acurácia, Macro F1 0,96, 6.228 documentos) |
| Python back-end/modelagem/pipelines | FastAPI, Streamlit, Flask/JWT em produção (SJUR, CIDA, NDOC, DataJud Monitor) |
| SQL | "SQL Avançado" explícito |
| Criação/gestão/otimização de prompts | "Engenharia de Prompt" explícito; multi-LLM em produção com fallback e limiar de confiança (SJUR) |
| CI/CD | Git + CI/CD (Bamboo) em ambiente de governança formal na FGV |
| Projetos de ML/AI de prototipagem a entrega | Ponta a ponta é o núcleo do seu perfil: SJUR, CIDA, NDOC, Process2Diagram - todos do discovery ao deploy em produção |
| Comunicação técnica/negócio | Depoimentos documentados (PM Xerox, CIO); interlocução multi-área na FGV (Jurídico, Acadêmico, TI) |
| **Diferencial:** RAG, vector database, multi-agente | Muito forte: Process2Diagram tem 13 agentes orquestrados (Orchestrator próprio + LangGraph); "LLMs · RAG" explícito nas competências; Supabase como backend (P2D, DataJud Monitor) |
| **Diferencial:** pipelines híbridos (determinístico + ML + LLM) | Muito forte: AgentValidator no P2D é validação determinística *sem uso de LLM* combinada aos agentes LLM; SJUR combina validação semântica de regras com classificação via LLM |
| **Diferencial:** inferência estatística | Base central da formação - "Testes de Hipóteses & Validação", "Modelagem Probabilística/Preditiva" |

## Gaps reais — não fabricados

1. **Kubernetes/EKS**: Docker está confirmado, mas não há evidência de orquestração de containers em produção (K8s/EKS). Deploy documentado é via API hardening (gunicorn, Flask/JWT) direto em servidor FGV, não K8s.
2. **Deep Learning / fine-tuning** (diferencial): seu histórico é ML clássico e NLP com spaCy; NDOC usa RetinaFace (modelo de visão computacional pré-treinado, consumido via API, não treinado/ajustado por você). Sem evidência de fine-tuning de modelos.
3. **LightGBM**: XGBoost está documentado; LightGBM não.
4. **Big data (Spark, Airflow)** (diferencial): sem evidência, mesmo gap identificado na vaga do Grupo Guanabara.
5. **Mestrado/Doutorado** (diferencial): não possui - graduação + MBA.
6. **Inglês avançado**: CV lista "Inglês (Avançado - leitura)" - avançado em leitura, não confirma fluência oral/escrita, que a vaga pede de forma mais ampla.
7. **Técnicas de prompting nomeadas explicitamente** (few-shot, chain-of-thought, self-consistency, prompt chaining, guardrails): você pratica isso (ex: AgentValidator funciona como guardrail determinístico), mas o CV não usa esse vocabulário específico - vale nomear explicitamente numa versão tailored.
8. **Bedrock (AWS)**: Azure OpenAI e Gemini documentados; Bedrock não.

## Status da candidatura

- **2026-09-02**: candidatura enviada, usando o CV tailored (`output/Curriculo_Pedro_Gentil_BTG.pdf`, gerado a partir de `data/profile_pt_btg.yaml`).
- **2026-09-09**: resposta negativa do BTG - motivo informado: não atende a todos os requisitos. Gaps mais prováveis, dado o que já estava mapeado nesta análise: Kubernetes/EKS, Deep Learning/fine-tuning, big data (Spark/Airflow), Mestrado/Doutorado, ou o nível de inglês (CV declara "avançado - leitura", vaga pede "inglês avançado" mais amplo). Sem retorno detalhado do recrutador sobre qual requisito pesou mais.

## Recomendação

Essa é a vaga com melhor aderência estrutural até agora - vale investir em uma versão tailored do CV. Sugestões de ajuste (sem fabricar nada):
- Nomear explicitamente as técnicas de prompting já praticadas (few-shot, guardrails via AgentValidator) usando o vocabulário da vaga;
- Reforçar o ângulo "pipelines híbridos determinístico + ML + LLM", que é um diferencial raro e você já tem como prova real (AgentValidator, SJUR);
- Ser transparente sobre Kubernetes/EKS e fine-tuning como áreas de aprendizado rápido, não esconder;
- Confirmar nível real de inglês falado antes de declarar "avançado" amplo (hoje o CV é específico: "avançado - leitura").
