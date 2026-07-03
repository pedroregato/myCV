# Career Card — DataJud Monitor
# Projeto Autoral (pessoal) | Status: Ativo | Nao comercializado ainda
# Atualizado: 2026-07-03

**Nota de nomenclatura:** este projeto NAO deve ser confundido com o trabalho feito para
o SJUR/FGV (ver `data/projetos/fgv/sjur.md`). Ambos consultam a mesma API publica do
DataJud/CNJ, mas sao sistemas distintos: este e um projeto autoral, individual, do zero
ao deploy em producao, sem vinculo com a FGV.

---

## Identificacao

- **Projeto:** DataJud Monitor
- **Autoria:** Individual, do zero ao deploy em producao
- **Status:** Ativo, em producao - ainda nao comercializado

## O que e

Plataforma web para consulta e monitoramento em lote de processos judiciais, integrada
a API Publica do DataJud (CNJ).

## Funcionalidades

- Consulta automatizada de processos em todos os tribunais brasileiros (STJ, TRFs, TJs,
  TRTs, TREs) a partir de planilhas
- Classificacao automatica de movimentos processuais pela Tabela Processual Unificada (TPU) do CNJ
- Radar de Prescricao: alerta de risco de prescricao intercorrente (art. 485 CPC)
- Exportacao de resultados em Excel, PDF e JSON
- Sistema de planos, cotas, autenticacao e painel administrativo (usuarios, financeiro,
  logs, notificacoes)

## Stack

Python - Streamlit - Supabase (PostgreSQL + Auth) - API DataJud - Streamlit Cloud

## Referencias no CV/LinkedIn

- Portfolio de Projetos Autorais em `profile_pt.yaml` / `profile_en.yaml`
- (Preencher: numero de usuarios, processos consultados, feedback coletado, plano de comercializacao?)
