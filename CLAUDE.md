# CLAUDE.md — myCV Project Guide

## Visão Geral

Este projeto gera o currículo profissional de **Pedro Gentil** em PDF (PT/EN) usando Python + fpdf2.
A evolução planejada é transformá-lo em uma plataforma pessoal de gestão de carreira, integrando:

- Geração de PDF (PT e EN) a partir de dados estruturados
- Atualização assistida por IA (Claude API) para sugerir melhorias e manter conteúdo atualizado
- Integração com LinkedIn (publicações, resumo de projetos)
- Catálogo de projetos com histórico e métricas

---

## Estrutura de Pastas Proposta

```
myCV/
├── CLAUDE.md                        # Este arquivo
├── README.md                        # Instruções para o usuário
├── requirements.txt                 # Dependências Python
├── .gitignore
├── .env                             # Secrets (não versionado) — ver .env.example
├── .env.example                     # Template de variáveis de ambiente
│
├── data/                            # Fonte da verdade — todos os dados
│   ├── profile_pt.yaml              # Perfil completo em Português
│   ├── profile_en.yaml              # Perfil completo em Inglês
│   │
│   ├── linkedin/                    # Seções do perfil LinkedIn (referência)
│   │   ├── headline_pt.txt          # Título profissional (PT)
│   │   ├── headline_en.txt          # Título profissional (EN)
│   │   ├── about_pt.md              # Seção "Sobre" (PT)
│   │   ├── about_en.md              # Seção "Sobre" (EN)
│   │   ├── experience/              # Descrições por empresa
│   │   │   ├── fgv_pt.md
│   │   │   ├── fgv_en.md
│   │   │   ├── xerox_pt.md
│   │   │   └── consultoria_independente_pt.md
│   │   └── posts/                   # Posts publicados (arquivo)
│   │       ├── 2025-12_learn-mate-multi-agent-tutor.md
│   │       └── 2018-07_visao-e-missao.md
│   │
│   └── history/                     # Snapshots versionados do CV
│       ├── changelog.md             # O que mudou em cada versão
│       ├── v1_2026-04-26/           # profile_pt.yaml + profile_en.yaml
│       └── v2_2026-04-26/           # ...
│
├── src/                             # Código-fonte modularizado
│   ├── generators/
│   │   └── pdf_generator.py         # Layout e renderização PDF
│   ├── integrations/
│   │   └── linkedin.py              # Integração LinkedIn API (futuro)
│   └── ai/
│       ├── cv_assistant.py          # Funções Claude API para o CV
│       └── prompts.py               # Templates de prompt
│
├── assets/
│   └── FotoLinkedin.png             # Foto usada no CV
│
├── output/                          # PDFs gerados (gitignored)
│   ├── Curriculo_Pedro_Gentil.pdf
│   └── Resume_Pedro_Gentil.pdf
│
└── scripts/
    ├── generate_cv.py               # Gera os PDFs a partir dos YAMLs
    ├── update_with_ai.py            # CLI interativo com Claude
    └── snapshot.py                  # Cria snapshot versionado do CV
```

---

## Arquitetura e Fluxo de Trabalho

### Separação de dados e layout

O arquivo `gerar_curriculo.py` atual mistura **dados** (textos, listas) com **layout** (FPDF).
A refatoração proposta separa:

- `data/profile_pt.yaml` / `data/profile_en.yaml` — apenas o conteúdo do CV
- `src/generators/pdf_generator.py` — apenas o layout e renderização PDF
- `scripts/generate_cv.py` — entry point que carrega os dados e chama o gerador

Isso permite atualizar o CV sem tocar no código de layout.

### Integração com Claude (Anthropic API)

Uso planejado do modelo `claude-sonnet-4-6` via `anthropic` SDK:

1. **Revisão e melhoria de texto** (`src/ai/cv_assistant.py`):
   - Dado um novo projeto ou conquista, Claude sugere como redigir o bullet point
   - Traduz automaticamente PT -> EN mantendo tom profissional
   - Avalia se o texto está alinhado ao perfil T-shaped e proposta de valor

2. **Geração de posts para LinkedIn** (`scripts/post_to_linkedin.py`):
   - A partir de `data/projects.yaml`, Claude gera um rascunho de post
   - Formatos: artigo técnico, case de resultado, reflexão profissional

3. **Atualização guiada** (`scripts/update_with_ai.py`):
   - Interface CLI onde Pedro descreve o que aconteceu (novo projeto, certificação, etc.)
   - Claude extrai as informações relevantes e propõe edições nos arquivos YAML
   - Pedro revisa e confirma antes de regenerar o PDF

### Integração com LinkedIn API

Usar `linkedin-api` (não-oficial) ou `requests` para:
- Buscar posts e engajamento existentes
- Publicar rascunhos gerados por Claude (requer aprovação manual)
- Sincronizar headline e about section com o CV

---

## Regras de Desenvolvimento

- **Dados ficam em `data/`**: nunca hardcodar texto de CV no código Python
- **Output em `output/`**: PDFs gerados não entram no git (adicionar ao `.gitignore`)
- **Segredos via `.env`**: `ANTHROPIC_API_KEY`, `LINKEDIN_ACCESS_TOKEN` nunca no código
- **Idioma do código**: inglês (variáveis, funções, comentários técnicos)
- **Idioma dos dados**: PT e EN separados em arquivos distintos

---

## Dependências Principais

```
fpdf2>=2.7.0          # Geração de PDF
anthropic>=0.30.0     # Claude API
python-dotenv>=1.0    # Variáveis de ambiente
pyyaml>=6.0           # Leitura dos arquivos de dados
requests>=2.31        # Chamadas HTTP (LinkedIn)
```

---

## Estado Atual (Abril 2026)

- [x] Geração de PDF funcional em PT e EN (`scripts/generate_cv.py`)
- [x] Layout com barra lateral, foto, destaques de impacto, depoimentos
- [x] Refatoração: dados separados em `data/profile_pt.yaml` e `data/profile_en.yaml`
- [x] Integração Claude API (`src/ai/cv_assistant.py` + `scripts/update_with_ai.py`)
- [x] Seções LinkedIn salvas como referência (`data/linkedin/`)
- [x] Sistema de histórico com snapshots versionados (`data/history/` + `scripts/snapshot.py`)
- [x] Documentos pessoais organizados em `data/gov_br/` (gitignored)
- [x] Catálogo de projetos em `data/projetos/` (catalog.yaml + MD por projeto + claude_patterns.md)
- [ ] Testes do assistente IA (`scripts/update_with_ai.py`)
- [ ] Completar dados Kaggle (`data/kaggle/`)
- [ ] CTPS Digital — baixar extrato e salvar em `data/gov_br/`
- [ ] Integração LinkedIn API (publicação assistida)
