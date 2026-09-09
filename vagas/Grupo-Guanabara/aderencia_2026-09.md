# Análise de Aderência — Engenheira(o) de Dados Sênior, Martech (Grupo Guanabara)
**Elaborado por:** Pedro Gentil Regato de Oliveira Soares
**Data:** Setembro de 2026
**Referência:** `vagas/Grupo-Guanabara/2026-09.md`

---

## Veredito

Aderência **moderada-baixa**. Diferente das vagas Foursys e Grupo SBF (onde o perfil de "IA Product Builder ponta a ponta" encaixa quase diretamente), esta é uma vaga de **Engenharia de Dados especializada em stack moderno de Martech**, com ferramentas nomeadas (dbt, Airflow/Prefect, BigQuery/Snowflake) que não aparecem no histórico documentado. Os fundamentos (SQL, Python, ETL, integração via API, rigor de qualidade) são reais e fortes; o gap está nas ferramentas específicas e no domínio de negócio (Martech/CRM).

## Pontos fortes — aderência real

| Requisito da vaga | Evidência no perfil |
|---|---|
| SQL avançado e modelagem de dados | "SQL Avançado" explícito nas competências; modelagem aplicada em SJUR, CIDA e DataJud Monitor (schemas Supabase) |
| Python para pipelines, transformações e automações | Python (Pandas · NumPy · FastAPI · Streamlit) usado de ponta a ponta em SJUR, CIDA, NDOC e Process2Diagram |
| ETL/ELT | Explícito nas competências; SJUR e CIDA envolvem extração multi-fonte (API DataJud/CNJ, e-mails SERDON, OCR multi-engine) e transformação para consumo downstream |
| Integração via APIs e feeds de dados, múltiplas fontes | Forte: API DataJud/CNJ (19.560 processos investigados), integração SOAP com o SGC da FGV, wrappers SE-SUITE (22+ operações), 7 provedores LLM intercambiáveis no Process2Diagram — evidência real de lidar com heterogeneidade de fontes |
| Conforto com desenvolvimento assistido por IA (Claude Code) | Match direto — é o próprio fluxo de trabalho atual de Pedro (CV e projetos), reforçado por "Introduction to Model Context Protocol - Anthropic" (Mai/2026) |
| Qualidade e confiabilidade de dados | CIDA: 96% de acurácia (Macro F1 0,96) com pipeline validado; SJUR: revisão humana abaixo do limiar de confiança; Process2Diagram: AgentValidator determinístico (sem uso de LLM) para validação de qualidade |
| Mentalidade de produto aplicada a dados | DataJud Monitor tem sistema de planos/cotas — pensado como produto, não apenas entrega técnica |
| Base estatística para métricas como RFM/LTV | Graduação em Estatística + "Modelagem Probabilística/Preditiva" — fundamenta conceitualmente essas métricas, mesmo sem aplicação documentada em Martech |

## Gaps reais — não fabricados

1. **dbt**: ferramenta central da vaga para transformação/modelagem; sem uso documentado no perfil.
2. **Orquestração de pipelines (Airflow, Prefect)**: o perfil tem orquestração de *agentes de IA* (LangGraph/Orchestrator próprio no Process2Diagram), que é um domínio distinto de orquestração de *pipelines de dados agendados*. Não há evidência de DAGs de dados.
3. **Data warehouses modernos em nuvem (BigQuery, Snowflake, Athena)**: experiência documentada é em Oracle/PL-SQL, DB2 e Supabase (Postgres) — sem cloud DW colunar.
4. **Pipelines de streaming**: todo o histórico é batch ou request-response (chamadas de API, OCR em lote, e-mails processados em lote); sem experiência em streaming (Kafka, Pub/Sub ou similar).
5. **Domínio de Martech/CRM/mídia paga**: nenhuma experiência com CDP, CRM ou plataformas de mídia paga (Meta Ads, Google Ads); o domínio de atuação é jurídico/acadêmico/institucional, não marketing.
6. **Unificação de identidade de cliente** (diferencial): sem experiência documentada em resolução de identidade entre fontes.

## Recomendação

Não recomendo montar uma versão de CV tailored "forçando" esses gaps — eles são estruturais (ferramentas e domínio de negócio), não apenas de enquadramento textual como nos casos anteriores. Se Pedro tiver interesse real nesta vaga, as opções honestas são:

- Concorrer citando a transferibilidade de ETL/API/qualidade de dados e a fluência com Claude Code, sendo direto sobre a lacuna em dbt/Airflow/cloud DW e disposição de aprender rapidamente;
- Ou tratar como sinal de que a vaga está fora do eixo atual (IA aplicada/automação/BPM) e não vale o esforço de adaptação.
