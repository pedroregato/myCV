# Career Card — NDOC: Visao Computacional para Fotografias Institucionais

**Projeto:** FGV-FACES | **Status:** Ativo | **Atualizado:** 2026-08-08
**Repositorio:** https://github.com/pedroregato/FGV-FACES (publico)

> Revisado com leitura direta do codigo-fonte via Claude Code em 2026-08-08.

---

## Identificacao

| Campo | Valor |
|-------|-------|
| Projeto | FGV-FACES — Automacao de Identificacao e Legenda de Fotografias (NDOC/FGV) |
| Periodo | Fevereiro/2025 - atual |
| Status | Em andamento |
| Funcao | Desenvolvedor principal / Arquiteto de solucao |

---

## Problema resolvido

O NDOC (Nucleo de Documentacao da FGV) mantinha um acervo de fotografias institucionais
sem legenda estruturada e sem rastreabilidade de quem aparece em cada imagem. Publicar
fotos no SE-SUITE exigia marcar rostos manualmente e criar arquivos de legenda a mao —
processo lento, inconsistente e inviavel dado o volume de eventos fotografados.

---

## Solucao implementada

Pipeline de visao computacional entregue como **API REST (FastAPI)**, com duas etapas principais.

### Etapa 1 — Deteccao de rostos

`POST /api/faces/detect-faces-base64`

- Recebe imagem em Base64; corrige rotacao EXIF automaticamente
- **RetinaFace** (deep learning) detecta todos os rostos com:
  - Threshold de confianca configuravel (padrao 0.55)
  - Deteccao multi-escala: upscaling automatico para imagens pequenas (lado menor < 800px)
  - Filtros pos-deteccao: aspect ratio, altura minima em pixels, validacao geometrica de
    landmarks (olhos, nariz, boca)
  - NMS (Non-Maximum Suppression) para fundir deteccoes duplicadas entre escalas
  - Processamento paralelo com `ThreadPoolExecutor`
- Retorna JSON de metadados com coordenadas de cada face + imagem anotada em Base64

### Etapa 2 — Geracao de SVG interativo

`POST /api/svg/gerar-svg-legenda-v2`

- Recebe imagem + JSON de metadados + JSON de legendas preenchidas pelo usuario
- Gera SVG interativo autocontido (~18 modulos em `src/face_tools/svg_*.py`):
  - Faces numeradas sobrepostas a imagem original
  - Painel flutuante de Legenda (lista de nomes por numero de rosto)
  - Painel flutuante de Info (titulo, local, data da foto)
  - Zoom, pan e botao Fit
  - Tooltips ao hover sobre cada face
  - Busca de nomes no painel de legendas
  - Tema claro/escuro com toggle
- SVG e autocontido: JavaScript embutido, sem dependencias externas
- Retorna SVG codificado em Base64 para armazenamento no SE-SUITE

### Integracao com SE-SUITE (ECM)

- `hub_integracao/legendador_client.py` consome a API REST do sistema .NET (SE-SUITE)
- Notificacao de conclusao sempre por **ID do arquivo** (nao por nome) para evitar colisoes
- Ambientes separados: dev / homolog / producao

### Interface desktop (legada)

`src/face_tools/FgvFaceApp.py` (tkinter) ainda existe como ferramenta auxiliar;
a entrega principal da solucao e via API REST.

---

## Stack (confirmada no codigo-fonte)

| Tecnologia | Uso |
|-----------|-----|
| FastAPI + Uvicorn | API REST com Swagger automatico; Gunicorn + SSL em producao |
| RetinaFace | Deteccao de rostos (deep learning) |
| TensorFlow 2.19 + Keras 3.9 | Backend do RetinaFace |
| OpenCV + NumPy + Pillow | Processamento de imagem, correcao EXIF, anotacoes |
| SVG + JavaScript embutido | Saida visual interativa autocontida |
| JWT (HS256) + bcrypt | Autenticacao OAuth2, tokens de 24h |
| SQLite + SQLAlchemy | Banco de autenticacao e banco de processamento |
| Docker + Docker Compose | Containerizacao com volume externo para acervo |
| Bamboo (FGV TIC) | CI/CD acionado por push no Bitbucket corporativo |
| tkinter | Interface desktop auxiliar (legada) |

### Itens documentados mas nao implementados em producao

| Item | Situacao |
|------|----------|
| PDF interativo (PyMuPDF) | Existe apenas `docs/livePDF.md` (exploratorio); nenhum `.py` no repositorio. **Nao mencionar no CV.** |
| withMTCNN | Mencionado em versoes antigas do card; arquivo nao existe no repositorio atual. **Nao mencionar no CV.** |

---

## Decisoes tecnicas importantes

1. **RetinaFace como detector unico** — avaliado contra alternativas; escolhido pela
   precisao superior em fotos de grupos com faces pequenas e parcialmente oclusas,
   comuns em eventos institucionais

2. **SVG autocontido com JavaScript embutido** — escolhido sobre HTML/React porque o
   SE-SUITE armazena o resultado como arquivo unico; renderiza direto no browser e em
   visualizadores de documentos sem infraestrutura adicional

3. **Legendagem como template manual** — decisao intencional de nao usar reconhecimento
   facial (identificacao de quem e quem) para evitar dependencia de base de dados
   biometricos; o sistema numera os rostos e o usuario completa os nomes

4. **Modelo carregado no startup** — RetinaFace ocupa ~200MB em memoria; carregado uma
   unica vez no evento `startup` do FastAPI para eliminar latencia na primeira requisicao
   e evitar OOM por multiplos carregamentos concorrentes

5. **SQLite em vez de PostgreSQL** — volume de dados baixo; elimina servidor de banco
   externo e simplifica deploy Docker e operacao pelo time de TI da FGV

---

## Impacto mensuravel

- Eliminacao do processo manual de marcacao de rostos e criacao de legendas
- Processamento paralelo de lotes com medicao de throughput
- _(Preencher: volume de fotos processadas? Numero de eventos cobertos?)_
- _(Preencher: reducao estimada de tempo por evento fotografico?)_

---

## Uso do Claude Code

- Arquitetura e implementacao dos ~18 modulos SVG (`src/face_tools/svg_*.py`)
- Estrategia de deteccao multi-escala com NMS em `withRetinaFace.py`
- Calibragem dos filtros pos-deteccao (aspect ratio, landmarks, thresholds)
- Estruturacao da camada de API REST (routers, services, schemas Pydantic)
- Documentacao tecnica do projeto (`docs/`, `api/docs/`, `carreira/`)
- _(Preencher: outras areas especificas?)_

---

## Bullet CV

> "NDOC [Visao Computacional]: RetinaFace para deteccao e legendagem automatica de multiplos
> rostos em acervo fotografico institucional — geracao de metadados estruturados (JSON) com
> coordenadas de cada face e visualizacao interativa (SVG com zoom, pan e tooltips) entregue
> via API REST (FastAPI)."

---

## Proximos passos

- _(Preencher: reconhecimento facial para identificacao automatica de pessoas recorrentes?)_
- _(Preencher: integracao direta com upload automatizado ao SE-SUITE?)_
- _(Preencher: suporte a video/frames de eventos?)_

---

## Notas para sincronizacao

- Repositorio publico no GitHub — pode ser referenciado no CV
- "NDOC" e nome interno — descrever como "Nucleo de Documentacao da FGV" no CV/LinkedIn
- Combinacao de visao computacional + integracao ECM e diferenciada — vale detalhar
- RetinaFace e modelo state-of-the-art para deteccao facial — agrega credibilidade tecnica
- **Nao mencionar:** PDF interativo (nao implementado) e MTCNN (removido do projeto)
