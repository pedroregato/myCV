# Career Card — CIDA: Classificacao Inteligente de Documentos Academicos
# Projeto FGV | Status: Ativo
# Repositorios: https://github.com/pedroregato/CIDA (API/producao)
#               https://github.com/pedroregato/ACAD-CLASSIFIER (treinamento/HPC)
# Atualizado: 2026-04-27

---

## Identificacao

- **Projeto:** CIDA - Classificacao Inteligente de Documentos Academicos
- **Periodo:** (preencher data de inicio)
- **Status:** Em producao (API Flask/Docker) + evolucao ativa (ACAD-CLASSIFIER no HPC FGV)
- **Minha funcao:** Desenvolvedor principal / Arquiteto de solucao
- **Infraestrutura:** Servidor HPC FGV (`hpcdc3fpr0001.acad.fgv.br`) com GPU (CUDA 11.8)

---

## Problema resolvido

A FGV processa um volume significativo de documentos academicos (teses, dissertacoes,
artigos, relatorios) que precisavam ser classificados por categoria para fins de
organizacao, indexacao e gestao de acervo. A classificacao manual era lenta, inconsistente
e nao escalavel.

---

## Solucao implementada

Ecossistema de dois repositorios com papeis distintos:

**ACAD-CLASSIFIER** (treinamento, experimentacao, HPC):
1. **Aquisicao de dados via SGC** - integracao SOAP com `sgc.fgv.br` que baixa PDFs
   diretamente do sistema de gestao documental da FGV com metadados estruturados

2. **Pipeline de ML** - Naive Bayes + TF-IDF com GridSearchCV (cv=3, otimizando
   max_features [500-1500] e alpha [0.01-10.0]). Suporte a processamento paralelo
   por CPU. Treinado com GPU (PyTorch + CUDA 11.8) no servidor HPC da FGV

3. **Processamento avancado de PDFs** (`pdfinsight`) - multiplos extratores
   (PyMuPDF, pdfplumber, Tika), deteccao de escrita a mao, extracao de PDFs
   criptografados, inspecao de camadas internas e correcao de texto via LLM

4. **Exploracao multimodal** - avaliacao do Llama 3.2 Vision (11B) via Ollama
   para extracao de metadados de imagens de documentos; LlamaIndex para indexacao
   e retrieval de diretorios de documentos

5. **Analise de modelo** - relatorios com accuracy, precision, recall, F1 por classe,
   matriz de confusao, distribuicao de lingua e heatmap de performance (JSON + PNG)

**CIDA** (producao/API):
6. **API REST** (Flask + JWT) - endpoint `/classify` que recebe PDF e retorna
   classe prevista + scores de probabilidade. Deploy em servidor Linux via Gunicorn + Docker

**13 categorias de classificacao** com codigos internos FGV (ex: 01.134.332/01,
01.144.44/02, 01.125.44/06...) — corpus de 1.750 documentos no conjunto de teste

---

## Stack principal

- **Python 3** - logica principal
- **scikit-learn** - pipeline ML (TfidfVectorizer + MultinomialNB + GridSearchCV)
- **PyTorch + CUDA 11.8** - treinamento acelerado por GPU no HPC FGV
- **spaCy** (`pt_core_news_lg` + `en_core_web_md`) - NLP, lemmatizacao, tokenizacao
- **PyMuPDF / pdfplumber / Tesseract / EasyOCR / Apache Tika** - extracao multi-engine
- **Llama 3.2 Vision (11B) via Ollama** - exploracao multimodal para metadados
- **LlamaIndex** - indexacao e retrieval de documentos
- **Flask + Flask-JWT-Extended + Gunicorn + Docker** - API REST em producao
- **SOAP (sgc.fgv.br)** - aquisicao automatica de documentos do SGC FGV
- **joblib** - serializacao do modelo treinado

---

## Impacto mensuravel

- **96,82% de acuracia** no conjunto de teste (1.750 documentos, 13 categorias)
- **Macro F1-Score: 0.9665** | Weighted F1-Score: 0.9681
- Melhor classe: 99,67% F1 (01.134.332/04, 150 docs) | Pior: 90,85% F1 (01.134.332/02)
- Eliminacao da classificacao manual de documentos academicos da FGV
- API em producao com autenticacao JWT para consumo pelos sistemas internos
- (Preencher: volume de documentos classificados em producao? Frequencia de uso?)

---

## Decisoes tecnicas importantes

1. **Naive Bayes + TF-IDF como baseline solido** - escolhido pela eficiencia com corpus
   moderado (96,82% de acuracia, superando a necessidade de modelos mais pesados);
   GridSearchCV otimiza max_features, alpha e n-grams com cv=3

2. **Pipeline multi-engine de extracao de texto** - hierarquia de extratores (PyMuPDF ->
   pdfplumber -> Tika -> Tesseract/EasyOCR) para cobrir todos os tipos de PDF:
   nativos, baseados em imagem, escaneados, criptografados e com escrita a mao

3. **Categorias inferidas da estrutura de pastas** - labels derivados dos subdiretorios
   do corpus, tornando o modelo extensivel sem alterar codigo

4. **Integracao SOAP com SGC** - aquisicao automatica de documentos de treinamento
   diretamente do sistema de gestao documental da FGV, eliminando coleta manual

5. **Exploracao multimodal com Llama 3.2 Vision** - avaliacao do modelo 11B para
   extracao de metadados de documentos via visao, como alternativa ao pipeline OCR
   para casos de baixa qualidade de digitalizacao

6. **Dois repositorios, papeis distintos** - ACAD-CLASSIFIER para experimentacao
   pesada (HPC + GPU + Jupyter), CIDA para producao (API + Docker) — separa
   ciclo de pesquisa do ciclo de servico

---

## Uso do Claude Code

(Preencher: quais partes foram desenvolvidas com Claude Code?
Ex: arquitetura da API, pipeline de pre-processamento, geracao de relatorio de analise?)

---

## Bullet CV (rascunho)

Desenvolveu ecossistema CIDA/FGV de classificacao inteligente de documentos academicos:
pipeline ML (TF-IDF + Naive Bayes) com 96,82% de acuracia em 13 categorias e 1.750
documentos de teste, extracao multi-engine de PDFs (PyMuPDF · Tesseract · EasyOCR),
integracao SOAP com SGC FGV para aquisicao automatica de corpus, exploracao de Llama 3.2
Vision para processamento multimodal, e API REST Flask/JWT em producao no HPC FGV.

---

## Proximos passos

- Avaliacao formal do Llama 3.2 Vision como substituto/complemento ao pipeline OCR
- (Preencher: expansao para novas categorias de documentos?)
- (Preencher: integracao entre ACAD-CLASSIFIER e CIDA API para deploy automatico de novos modelos?)
- (Preencher: volume de documentos classificados em producao?)

---

## Notas para sincronizacao

- Ambos os repositorios sao publicos no GitHub - podem ser referenciados no CV
- Codigos de categoria (01.134.332/01 etc.) sao internos da FGV - nao detalhar publicamente
- "CIDA" e acronimo interno - usar "classificacao inteligente de documentos academicos" no CV/LinkedIn
- Mencionar HPC FGV e GPU (CUDA) adiciona credibilidade tecnica ao perfil

---
<!-- Ultima atualizacao: 2026-04-27 -->
