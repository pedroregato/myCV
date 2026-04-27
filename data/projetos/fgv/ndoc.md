# Career Card — NDOC: Visao Computacional para Fotografias Institucionais
# Projeto FGV | Status: Ativo
# Repositorio: https://github.com/pedroregato/FGV-FACES (publico)
# Atualizado: 2026-04-26

---

## Identificacao

- **Projeto:** FGV-FACES - Automacao de Identificacao e Legenda de Fotografias (NDOC/FGV)
- **Periodo:** Fevereiro/2025 - atual
- **Status:** Em andamento
- **Minha funcao:** Desenvolvedor principal / Arquiteto de solucao

---

## Problema resolvido

O NDOC (Nucleo de Documentacao da FGV) mantinha um acervo de fotografias institucionais
sem legenda estruturada e sem rastreabilidade de quem aparece em cada imagem. Publicar
fotos no SE-SUITE exigia marcar rostos manualmente e criar arquivos de legenda a mao,
processo lento e inconsistente. O volume de eventos fotografados tornava a operacao
inviavel sem automacao.

---

## Solucao implementada

Pipeline de visao computacional com interface desktop (tkinter) e integracao com o
SE-SUITE, dividido em quatro fases:

1. **Deteccao automatica de rostos** - RetinaFace (deep learning) processa um lote de
   fotos e detecta todas as faces, ordenando-as de cima para baixo e da esquerda para
   a direita. Processamento paralelo com ThreadPoolExecutor (4 workers)

2. **Geracao de artefatos** - Para cada foto sao gerados automaticamente:
   - `*_LEG.jpg` - imagem anotada com retangulos verdes e numeros sobre cada rosto
   - `*.json` - metadados (dimensoes, DPI, tamanho, coordenadas de cada face)
   - `*_LEG.json` / `*_LEG.txt` - template de legenda para preenchimento manual
     ("Da esquerda para a direita: [1] ___, [2] ___")

3. **Saidas interativas** - Modulos adicionais geram:
   - SVG interativo com botoes de download da imagem original/anotada e copia de texto
   - PDF interativo (PyMuPDF) com camadas OCG alternando imagem com/sem anotacoes,
     campos de texto editaveis e botoes de exportacao (requer Adobe Acrobat)

4. **Integracao SE-SUITE** - Conjunto validado (foto original + `_LEG.jpg` + `_LEG.txt`)
   e arrastado para o SE-SUITE, estabelecendo a associacao entre fotografia e legenda

---

## Stack principal

- **Python 3** - logica principal e GUI (tkinter)
- **RetinaFace** - deteccao de rostos (modelo deep learning)
- **OpenCV** - anotacao de imagens (retangulos, labels)
- **PyMuPDF (fitz)** - geracao de PDFs interativos com camadas OCG e JavaScript
- **minidom / SVG** - geracao de SVGs interativos
- **ThreadPoolExecutor** - processamento paralelo de lotes de imagens
- **SE-SUITE (SoftExpert)** - destino final dos artefatos gerados

---

## Impacto mensuravel

- Eliminacao do processo manual de marcacao de rostos e criacao de legendas
- Processamento paralelo de lotes de imagens com medicao de throughput (segundos/MB)
- (Preencher: volume de fotos processadas? Numero de eventos cobertos?)
- (Preencher: reducao estimada de tempo por evento fotografico?)

---

## Decisoes tecnicas importantes

1. **RetinaFace vs MTCNN** - o projeto implementa ambos (`withRetinaFace.py` e
   `withMTCNN.py`); RetinaFace foi escolhido como padrao pela maior precisao em
   fotos de eventos com grupos de pessoas

2. **PDF interativo com camadas OCG** - alternativa ao SVG para usuarios que precisam
   de documento imprimivel; usa JavaScript embarcado no PDF para alternar entre
   versao com e sem anotacoes (restricao: requer Adobe Acrobat para funcionalidade completa)

3. **Legenda como template manual** - decisao intencional de nao usar reconhecimento
   facial (identificacao de quem e quem) para evitar dependencia de base de dados
   biometricos; o sistema numera os rostos e o usuario completa os nomes

---

## Uso do Claude Code

(Preencher: quais partes foram desenvolvidas com Claude Code?
Ex: arquitetura do pipeline, geracao do SVG interativo, modulo livePDF, etc.)

---

## Bullet CV (rascunho)

Desenvolveu sistema de visao computacional (FGV-FACES) para automacao de legenda de
fotografias institucionais no NDOC/FGV: deteccao de rostos com RetinaFace, geracao
automatica de imagens anotadas e templates de legenda, e exportacao em PDF/SVG
interativos para integracao com o SE-SUITE.

---

## Proximos passos

- (Preencher: reconhecimento facial para identificacao automatica de pessoas recorrentes?)
- (Preencher: integracao direta com a API do SE-SUITE para upload automatizado?)
- (Preencher: suporte a video/frames de eventos?)

---

## Notas para sincronizacao

- Repositorio publico no GitHub - pode ser referenciado no CV
- "NDOC" e nome interno da FGV - descrever como "Nucleo de Documentacao" no CV/LinkedIn
- Visao computacional + integracao ECM e combinacao tecnica diferenciada - vale detalhar
- Mencionar RetinaFace (modelo state-of-the-art) agrega credibilidade tecnica

---
<!-- Ultima atualizacao: 2026-04-26 -->
