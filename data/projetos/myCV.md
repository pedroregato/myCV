# Projeto: myCV
# Status: Ativo | Visibilidade: Privado
# Caminho: D:/PythonProjects/myCV
# Claude Code: Sim
# Atualizado: 2026-04-26

---

## O que é

Plataforma pessoal de gestão de carreira construída com Claude Code.
Gera CVs em PDF (PT/EN) a partir de dados YAML, integra assistente IA (Claude API)
para atualização de conteúdo, e centraliza referências LinkedIn, certificados e histórico.

## Problema que resolve

Antes: CV era um script Python monolítico com dados hardcodados, sem histórico, sem IA.
Depois: dados separados em YAML, geração automatizada, assistente IA para revisão e posts,
snapshots versionados, documentos pessoais organizados.

## Arquitetura

- `data/` — fonte da verdade (YAML, LinkedIn, certificados, projetos, gov_br)
- `src/generators/` — gerador PDF (fpdf2)
- `src/ai/` — assistente Claude API (cv_assistant.py + prompts.py)
- `scripts/` — entry points (generate_cv.py, update_with_ai.py, snapshot.py)
- `docs/index.html` — documentação HTML standalone
- `data/history/` — snapshots versionados dos YAMLs

## Tecnologias

Python · fpdf2 · PyYAML · Anthropic SDK (claude-sonnet-4-6) · python-dotenv

## Decisões importantes

- **Dados em YAML, nunca no código:** permite atualização sem tocar em Python
- **Charset latin-1 no fpdf2:** evitar `—` (em dash) e `→` nos YAMLs — usar ` -` e `->`
- **Snapshot antes de editar:** sempre criar snapshot antes de mudanças nos YAMLs
- **Título funcional vs cargo formal:** CV usa título funcional real, não o cargo do contrato CLT
- **FGV apresentada como bloco unificado 2019-atual:** inclui período MGN com nota discreta

## Uso do Claude Code

- Refatoração inicial do script monolítico para arquitetura data/src/scripts
- Criação do módulo de IA (cv_assistant.py, prompts.py, update_with_ai.py)
- Análise do LinkedIn Profile.pdf e gap_analysis
- Análise da CTPS e organização de documentos pessoais
- Construção da documentação HTML (docs/index.html)
- Catálogo de projetos (esta pasta)

## Padrões Claude Code que funcionaram bem

Ver `data/projetos/claude_patterns.md`

## Próximos passos

- [ ] Testar o assistente IA (scripts/update_with_ai.py)
- [ ] Completar dados do Kaggle (data/kaggle/)
- [ ] Preencher catalog.yaml com dados dos outros projetos
- [ ] Extrair CTPS Digital e salvar em data/gov_br/
- [ ] Implementar data/projects.yaml como input para o gerador PDF (seção certificações)
