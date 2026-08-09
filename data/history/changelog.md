# Changelog — Histórico de versões do CV

Formato de snapshot: `v{N}_{YYYY-MM-DD}/`
Cada pasta contém `profile_pt.yaml` e `profile_en.yaml` da data correspondente.

Para criar um novo snapshot:
```bash
python scripts/snapshot.py --message "Descrição do que mudou"
```

---

## v1 — 2026-04-26

**Contexto:** Versão inicial estruturada. Refatoração do CV de monolito Python
para dados separados em YAML + gerador PDF + módulo de IA (Claude API).

**Conteúdo:**
- Perfil completo PT e EN
- 3 experiências: FGV (2014-atual), Xerox Brasil (2012-2014), Consultoria Independente (2008-2012)
- Destaques de impacto: SJUR (R$ 27,3M), CIDA (>97% acurácia), Xerox turnaround (~30%), FGV Auditoria
- Publicações: LEARN MATE (Dez/2025), Visão e Missão, Passivos Subjetivos, Estratégia em Ação (2018)
- 4 depoimentos: Rodrigo Gaio (Xerox), Joaquim Santos Neto (CIO), Aércio Dornelas, Marcel Dubiella

## v2 — 2026-04-26

Teste do sistema de snapshot — estrutura inicial com linkedin/ e history/ criados.

## v3 — 2026-04-26

Snapshot antes de sincronizar com LinkedIn Profile.pdf exportado em Abr/2026

## v4 — 2026-04-26

Snapshot antes de corrigir entrada FGV (período, cargo e projetos) e números SJUR

## v5 — 2026-08-08

Adiciona paragrafo de governanca de TI corporativa (arquitetura, infra, banco de dados, redes, negocio, seguranca, gestao de mudanca formal), CI/CD (Git/Bamboo) nas competencias e menciona Orchestrator proprio do Process2Diagram (alem de LangGraph); sincroniza mesmo conteudo nas referencias do LinkedIn (about e experiencia FGV).

## v6 — 2026-08-08

correção de layout: títulos órfãos, alturas calculadas, proteção de competências
