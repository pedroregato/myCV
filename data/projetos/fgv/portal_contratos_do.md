# Career Card — Portal de Contratos DO/Compras Corporativas
# Projeto FGV | Status: Em producao
# Repositorio: (interno FGV — SE-SUITE)
# Atualizado: 2026-04-27

---

## Identificacao

- **Projeto:** Portal de Contratos da Diretoria Operacional (DO) - Compras Corporativas
- **Periodo:** (preencher data de inicio) - atual
- **Status:** Em producao / operacao continua
- **Minha funcao:** Arquiteto de solucao / Desenvolvedor principal
- **Plataforma:** SE-SUITE (SoftExpert) — BPM + ECM integrados

---

## Problema resolvido

A DO/Compras Corporativas da FGV gerencia contratos com fornecedores de Facilities,
TI, Servicos Profissionais, Marketing e Telecom para todas as unidades operacionais
(RJ, SP, BH e demais campi). Sem um portal unificado, o ciclo contratual —
nova contratacao, renovacao, aditivo, rescisao — era conduzido por e-mail e planilhas,
sem rastreabilidade, sem versionamento de documentos e sem visibilidade de prazos.

---

## Solucao implementada

Portal BPM/ECM integrado no SE-SUITE, cobrindo o ciclo contratual completo:

**Tipos de solicitacao suportados:**
- Solicitacao de Nova Contratacao de Servico
- Solicitacao de Renovacao de Servico (Aditivo ou OS)
- Cadastro Legado de Instrumento Contratual
- Solicitacao de Rescisao de Contrato

**Tipos de instrumento gerenciados:**
- Contrato, Aditivo, Guarda-chuva, Rescisao, Ordem de Servico

**Categorias de servico:**
- FACILITIES (Manutencao Predial, Servicos Prediais, Obras, Cessao de Espaco,
  Vigilancia Patrimonial, Servicos de Alimentacao, Gestao de Residuos, Aluguel...)
- TI (Consultoria TI, Desenvolvimento TI, OutSourcing TI, Licenciamento, Softwares...)
- Servicos Profissionais, Marketing, Telecom

**Pipeline BPM (etapas identificadas nos dados):**
1. Abertura da solicitacao pelo gestor
2. Analise juridica (JUR)
3. Analise DCI
4. Tomada de Preco / negociacao com fornecedor
5. Validacao pela DO/COMPRAS
6. Credenciamento
7. Assinatura (integracao D4Sign para assinatura eletronica)
8. Recolhimento fisico no NDOC
9. Conclusao — instrumento ativo no ECM com vigencia registrada

**Usuarios do portal:**
- 58 solicitantes de multiplas unidades gestoras (DTI, DO/SOpS, TON, DRH, SOPS-SP/RJ...)
- 13 compradores responsaveis pela conducao dos processos

---

## Stack principal

- **SE-SUITE (SoftExpert)** — BPM (Workflow) + ECM (Gestao de Documentos) integrados
- **SE-SUITE Utils (Python)** — wrappers SOAP desenvolvidos por Pedro para automatizar
  operacoes no SE-SUITE: publicacao de documentos, disparo de workflows, consulta de status
- **D4Sign** — assinatura eletronica integrada ao pipeline BPM
- **NDOC/FGV-FACES** — recolhimento e legendagem de documentos fisicos pos-assinatura
- **SE Analytics / SQL Server** — relatorios de posicao (por solicitante, por comprador,
  totalizacao geral, demandas em processamento/finalizadas)

---

## Impacto mensuravel

- **1.330 instrumentos contratuais** gerenciados no portal (acumulado total)
- **1.038 processos finalizados** com historico completo auditavel
- **~128 processos em andamento** simultaneamente (snapshot abril/2026)
- **881 processos concluidos** = 85% taxa de finalizacao no historico
- **58 solicitantes + 13 compradores** operando o portal em multiplas unidades
- **23 categorias de servico** cobertas (Facilities + TI + Profissionais + Marketing + Telecom)
- **Ciclo medio de ~90 dias corridos** por processo (min: horas para urgentes, max: 2+ anos para legado)
- **5 tipos de instrumento** com workflows distintos num unico portal
- Eliminacao do fluxo por e-mail/planilha para contratacoes corporativas da DO

---

## Decisoes tecnicas importantes

1. **BPM + ECM no mesmo sistema (SE-SUITE)** — o processo de negocio (workflow) e o
   documento contratual vivem na mesma plataforma; a assinatura aciona automaticamente
   o arquivamento no ECM com metadados de vigencia

2. **Integracao D4Sign no pipeline** — assinatura eletronica acionada diretamente pelo
   BPM elimina o passo manual de envio/retorno de documentos para assinatura

3. **Recolhimento fisico via NDOC** — pos-assinatura, documentos fisicos sao recolhidos
   pelo NDOC e vinculados ao processo no ECM; FGV-FACES automatiza a legendagem
   das fotografias de entrega

4. **SE-SUITE Utils como camada de automacao** — em vez de operar o SE-SUITE manualmente
   para acoes em lote (migracao de legado, backfill de metadados), biblioteca Python
   com wrappers SOAP permite scripts idempotentes e auditaveis

5. **Separacao FACILITIES x TI** — categorias com compradores, SLAs e aprovadores
   distintos; o portal unifica o fluxo mas preserva as especificidades por categoria

---

## Uso do Claude Code

- Arquitetura da integracao SE-SUITE Utils para automacao de operacoes BPM/ECM
- Desenvolvimento dos wrappers SOAP (fm_ws, dc_ws, wf_ws, adm_ws)
- Pipeline de migracao do legado contratual (Cadastro Legado de Instrumento Contratual)
- Scripts de backfill de metadados e diagnostico de cobertura
- (Preencher: outros aspectos desenvolvidos com Claude Code no portal especificamente?)

---

## Bullet CV (rascunho)

Arquitetou e implantou o Portal de Contratos BPM/ECM da DO/Compras Corporativas FGV
no SE-SUITE, integrando D4Sign para assinatura eletronica e automatizando o ciclo
completo de 1.330 instrumentos contratuais (Facilities · TI · Servicos Profissionais)
com 58 solicitantes e 13 compradores em multiplas unidades — eliminando o fluxo
manual por e-mail e planilhas.

---

## Proximos passos

- Endpoints DO Compras (`/api/docompras/`) na API SE-SUITE Utils (em andamento)
- Portal Analytics de cobertura contratual (SE Analytics + queries business-queries/)
- (Preencher: automacao de alertas de vencimento de vigencia?)
- (Preencher: integracao com sistema de pagamentos/ERP?)

---

## Notas para sincronizacao

- "DO/Compras Corporativas" e nome interno — usar "Compras Corporativas" ou
  "Corporate Procurement" no CV em ingles
- Nao mencionar nomes de fornecedores especificos ou valores de contratos individuais
- Os numeros (1.330 instrumentos, 58 solicitantes, 13 compradores) sao de relatorios
  internos do SE-SUITE — ok para CV como metrica de escala
- Este projeto e parte do escopo maior do ECM & BPM — pode ser detalhado como
  subprojeto ou destacado separadamente dependendo do contexto

---
<!-- Ultima atualizacao: 2026-04-27 -->
