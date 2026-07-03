# Projetos FGV — Career Cards
# Atualizado: 2026-04-26

## Como funciona

Esta pasta contém os "Career Cards" dos projetos desenvolvidos na FGV com suporte
do Claude Code (conta corporativa).

**O que é um Career Card:**
Não é uma cópia do projeto — é um extrato estruturado com o que é relevante para
a carreira: problema resolvido, decisões técnicas, impacto mensurável, aprendizados.
Sem código proprietário, sem dados sensíveis da FGV.

## Protocolo de sincronização

1. Em cada projeto FGV, manter a seção `## Career Card` no CLAUDE.md corporativo
2. Ao atingir um marco relevante (entrega, novo projeto, resultado mensurável):
   a. Atualizar o Career Card no projeto FGV
   b. Abrir o myCV e rodar: `python scripts/snapshot.py -m "antes de atualizar {projeto}"`
   c. Colar o Career Card atualizado no arquivo correspondente desta pasta
   d. Se o impacto for significativo, atualizar também `data/profile_pt.yaml`
   e. Regenerar os PDFs: `python scripts/generate_cv.py`

## Frequência sugerida

- **Semanal (rápida):** atualizar o Career Card no projeto FGV se houve progresso
- **Mensal:** sincronizar os cards para o myCV
- **Por marco:** atualizar o profile YAML e regenerar o PDF quando houver novo resultado

## Projetos ativos

| Arquivo | Projeto | Status |
|---|---|---|
| `sjur.md` | SJUR — Monitoramento Processual & IA Jurídica | Ativo |
| `ecm_bpm.md` | ECM & BPM / SE-SUITE Utils | Ativo |
| `cida.md` | CIDA — Classificação Acadêmica | (verificar) |
| `ndoc.md` | NDOC — Visão Computacional | (verificar) |
| `di.md` | D&I — Pesquisa Diversidade & Inclusão | (verificar) |
| (novos projetos) | ... | ... |
