# myCV — Plataforma Pessoal de Gestão de Carreira

Repositório privado de **Pedro Gentil Regato de Oliveira Soares**.

Gera currículos em PDF (PT e EN) a partir de dados estruturados em YAML,
centraliza referências LinkedIn, histórico de projetos e documentos de carreira,
e integra um assistente IA (Claude API) para atualização e revisão de conteúdo.

---

## Gerar os PDFs

```bash
# Instalar dependências
pip install -r requirements.txt

# Gerar ambos os idiomas
python scripts/generate_cv.py --lang all

# Apenas português
python scripts/generate_cv.py --lang pt

# Apenas inglês
python scripts/generate_cv.py --lang en
```

Os arquivos são salvos em `output/`:
- `output/Curriculo_Pedro_Gentil.pdf`
- `output/Resume_Pedro_Gentil.pdf`

---

## Atualizar conteúdo

**Sempre criar um snapshot antes de editar os YAMLs:**

```bash
python scripts/snapshot.py -m "antes de atualizar <o que vai mudar>"
```

Editar o arquivo de dados correspondente ao idioma:
- `data/profile_pt.yaml` — versão em português
- `data/profile_en.yaml` — versão em inglês

Depois regenerar os PDFs com `generate_cv.py`.

**Regra importante:** os arquivos YAML alimentam o gerador PDF via fpdf2 (encoding
latin-1). Não usar `—` (em dash U+2014) nem `→` (seta U+2192). Substituir por ` -`
e `->` respectivamente.

Validar antes de gerar:
```bash
python -c "t=open('data/profile_pt.yaml',encoding='utf-8').read(); print([c for c in t if ord(c)>255] or 'ok')"
```

---

## Assistente IA

Interface CLI que usa o Claude API (claude-sonnet-4-6) para sugerir melhorias:

```bash
# Melhorar um bullet de experiência
python scripts/update_with_ai.py bullet

# Revisar uma seção completa
python scripts/update_with_ai.py review

# Traduzir PT -> EN
python scripts/update_with_ai.py translate

# Rascunhar post para LinkedIn
python scripts/update_with_ai.py post

# Sugerir edição em YAML
python scripts/update_with_ai.py yaml-update
```

Requer `ANTHROPIC_API_KEY` no arquivo `.env` (ver `.env.example`).

---

## Estrutura de pastas

```
myCV/
├── data/
│   ├── profile_pt.yaml          # Fonte da verdade — CV em português
│   ├── profile_en.yaml          # Fonte da verdade — CV em inglês
│   ├── linkedin/                # Seções do perfil LinkedIn
│   │   ├── about_pt.md          # Seção "Sobre" (PT) — atualizada em Abr/2026
│   │   ├── about_en.md          # Seção "About" (EN)
│   │   ├── headline_pt.txt      # Título profissional
│   │   ├── experience/          # Descrições por empresa
│   │   ├── posts/               # Posts publicados (arquivo)
│   │   └── gap_analysis.md      # Análise LinkedIn vs. YAML
│   ├── projetos/                # Catálogo de projetos
│   │   ├── catalog.yaml         # Índice estruturado de todos os projetos
│   │   ├── claude_patterns.md   # Padrões e aprendizados cross-project
│   │   ├── myCV.md              # Career card deste projeto
│   │   ├── process2diagram.md   # Career card Process2Diagram
│   │   ├── learn_mate.md        # Career card Learn Mate
│   │   └── fgv/                 # Career cards dos projetos FGV
│   │       ├── README.md        # Protocolo de sincronização com conta corporativa
│   │       ├── career_card_template.md
│   │       ├── sjur.md          # DataJud Monitor + Classificador SERDON
│   │       ├── ecm_bpm.md       # SE-SUITE Utils
│   │       ├── portal_contratos_do.md  # Portal de Contratos DO/Compras
│   │       ├── cida.md          # Classificação de Documentos Acadêmicos
│   │       ├── ndoc.md          # FGV-FACES / Visão Computacional
│   │       └── di.md            # Pesquisa D&I
│   ├── certificados/            # Índice de certificações (index.yaml)
│   ├── kaggle/                  # Perfil e histórico Kaggle
│   ├── history/                 # Snapshots versionados dos YAMLs
│   │   └── changelog.md
│   └── gov_br/                  # Documentos pessoais (gitignored)
├── src/
│   ├── generators/
│   │   └── pdf_generator.py     # Layout e renderização PDF (fpdf2)
│   └── ai/
│       ├── cv_assistant.py      # Funções Claude API
│       └── prompts.py           # Templates de prompt
├── scripts/
│   ├── generate_cv.py           # Gera os PDFs
│   ├── update_with_ai.py        # CLI do assistente IA
│   └── snapshot.py              # Cria snapshot versionado
├── assets/
│   └── FotoLinkedin.png         # Foto usada no CV
├── docs/
│   └── index.html               # Documentação HTML standalone
├── output/                      # PDFs gerados (gitignored)
├── CLAUDE.md                    # Guia para o Claude Code
└── requirements.txt
```

---

## Projetos catalogados

| Projeto | Career Card | Repositório |
|---|---|---|
| SJUR — DataJud Monitor + SERDON | `data/projetos/fgv/sjur.md` | interno FGV |
| ECM & BPM — SE-SUITE Utils | `data/projetos/fgv/ecm_bpm.md` | interno FGV |
| Portal de Contratos DO/Compras | `data/projetos/fgv/portal_contratos_do.md` | interno FGV |
| CIDA — Classificação Acadêmica | `data/projetos/fgv/cida.md` | github.com/pedroregato/CIDA |
| NDOC — FGV-FACES | `data/projetos/fgv/ndoc.md` | github.com/pedroregato/FGV-FACES |
| Process2Diagram (open source) | `data/projetos/process2diagram.md` | github.com/pedroregato/Process2Diagram |
| Learn Mate | `data/projetos/learn_mate.md` | (preencher) |

---

## Sincronização com projetos FGV (conta corporativa)

Os projetos desenvolvidos na FGV têm seu próprio ambiente Claude Code (conta corporativa).
Para sincronizar com este repositório sem copiar código proprietário:

1. Em cada projeto FGV, manter a seção `## Career Card` no CLAUDE.md corporativo
2. Ao atingir um marco relevante: `python scripts/snapshot.py -m "antes de atualizar <projeto>"`
3. Copiar o Career Card atualizado para `data/projetos/fgv/<projeto>.md`
4. Se impacto significativo: atualizar `data/profile_pt.yaml` e `data/profile_en.yaml`
5. Regenerar os PDFs: `python scripts/generate_cv.py --lang all`

Ver protocolo completo em `data/projetos/fgv/README.md`.

---

## Estado atual (Abril 2026)

- [x] Geração de PDF funcional PT e EN
- [x] Dados separados em YAML (profile_pt / profile_en)
- [x] Integração Claude API (cv_assistant + update_with_ai)
- [x] Snapshots versionados (history/ + changelog)
- [x] Seções LinkedIn salvas como referência
- [x] Catálogo de projetos com career cards (FGV + pessoais)
- [x] Documentação HTML standalone (docs/index.html)
- [ ] Testes do assistente IA (update_with_ai.py)
- [ ] Completar perfil Kaggle (data/kaggle/)
- [ ] Exportar CTPS Digital e salvar em data/gov_br/
- [ ] Preencher learn_mate.md com dados reais
- [ ] Integração LinkedIn API (publicação assistida)
