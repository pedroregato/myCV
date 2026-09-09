# Estudo — Fundamentos de Databricks/PySpark
# Objetivo: preparar entrevista técnica para vaga de IA em Contact Center (Data & Analytics)
# Gap identificado: Spark/Databricks é o único requisito obrigatório sem evidência em nenhum
# projeto seu (ver aderência estimada ~75-78% discutida em conversa de 2026-07-13)
# Atualizado: 2026-07-13

---

## Como usar este documento

Você não vai virar especialista em Spark em poucos dias, e não precisa. O objetivo é:
1. Ter o **modelo mental** certo (por que Spark existe, o que ele resolve que Pandas não resolve)
2. Saber **traduzir** o que você já faz em Pandas/SQL/scikit-learn para o vocabulário Spark/Databricks
3. Não travar nas perguntas de entrevista mais prováveis
4. Ter uma resposta honesta e forte para "você já usou Databricks?" que vire força, não fraqueza

A cada seção técnica há uma coluna "Como conectar com sua experiência" — use isso ativamente
na entrevista. Seu argumento não é "eu sei Spark", é "eu já resolvi o problema que Spark
resolve, com outra ferramenta, e sei exatamente por que Spark seria a escolha certa aqui".

---

## 1. Por que Spark existe (o que perguntam sem perguntar diretamente)

Pandas roda em **uma máquina, na memória**. Seus projetos (SJUR, CIDA, P2D) processam
volumes que cabem numa máquina — milhares de e-mails, milhares de documentos, dezenas de
reuniões. Um Contact Center gera **milhões de interações/dia** — não cabe na memória de uma
máquina, e processar sequencialmente seria lento demais.

Spark resolve isso distribuindo o processamento por várias máquinas (**cluster**) em paralelo.
Databricks é a plataforma gerenciada que roda Spark sem você precisar administrar a infraestrutura
(parecido com o que Streamlit Cloud faz para suas apps — gerencia a infra, você foca no código).

**Como conectar com sua experiência:** você já pensa em escala pelo pipeline multi-engine do CIDA
(hierarquia de extratores para cobrir volume e variedade de PDFs) e pelo pipeline multi-agente do
P2D (paralelismo via ThreadPoolExecutor). Spark é o mesmo princípio — paralelismo — aplicado a
dados tabulares em escala de cluster em vez de threads numa máquina.

---

## 2. Arquitetura em 5 minutos

- **Driver**: o processo que roda seu código e monta o plano de execução. É onde seu notebook
  "vive".
- **Executors**: as máquinas do cluster que realmente processam os dados, em paralelo.
- **Cluster**: o conjunto de máquinas (driver + executors) que o Databricks provisiona pra você.
  Existem dois tipos principais:
  - **All-purpose cluster**: para desenvolvimento interativo em notebook (você "liga e mexe")
  - **Job cluster**: sobe automaticamente para rodar um job agendado e desce ao terminar
    (mais barato, usado em produção)
- **Lazy evaluation**: transformações (`filter`, `select`, `groupBy`) não executam na hora —
  Spark monta um plano (DAG) e só executa quando você chama uma **action** (`count()`, `show()`,
  `write()`, `collect()`). Isso permite ao Spark otimizar o plano inteiro antes de rodar.

**Pergunta clássica de entrevista:** "Qual a diferença entre transformação e ação no Spark?"
Resposta: transformação é preguiçosa (lazy), retorna outro DataFrame, não dispara execução;
ação dispara a execução real e retorna um resultado (ou grava dados).

**Como conectar:** o `LangGraph Adaptive Retry` do P2D e o `KnowledgeHub` como fonte única de
verdade também são formas de você já pensar em "planejar antes de executar" e "estado
centralizado" — não é o mesmo conceito, mas mostra que você já opera com abstrações de
orquestração, não só código imperativo linha a linha.

---

## 3. PySpark DataFrame API — tradução direta do que você já sabe

Você já pensa em DataFrames (Pandas). A API do PySpark é deliberadamente parecida. Principais
diferenças práticas:

| O que você quer fazer | Pandas (o que você já sabe) | PySpark |
|---|---|---|
| Ler dados | `pd.read_csv("f.csv")` | `spark.read.csv("f.csv", header=True, inferSchema=True)` |
| Ler tabela Delta/SQL | — | `spark.read.table("catalog.schema.tabela")` ou `spark.sql("SELECT * FROM tabela")` |
| Selecionar colunas | `df[["a","b"]]` | `df.select("a", "b")` |
| Filtrar linhas | `df[df.a > 10]` | `df.filter(df.a > 10)` ou `df.filter("a > 10")` |
| Nova coluna | `df["c"] = df.a + df.b` | `df.withColumn("c", df.a + df.b)` |
| Agrupar e agregar | `df.groupby("a").mean()` | `df.groupBy("a").mean()` ou `.agg({"b": "mean"})` |
| Ordenar | `df.sort_values("a")` | `df.orderBy("a")` |
| Ver os dados | `df.head()` | `df.show()` |
| Contar linhas | `len(df)` | `df.count()` |
| Para Pandas | — | `df.toPandas()` (⚠️ traz tudo pra memória do driver — cuidado com volume) |
| SQL direto | — | `df.createOrReplaceTempView("t")` + `spark.sql("SELECT ...")` |

**Ponto de atenção real (não decore, entenda):** em Pandas, tudo roda na memória local e o
resultado é imediato. Em Spark, `df.filter(...)` não faz nada até você chamar `.show()` ou
`.write()`. Se numa entrevista perguntarem "por que meu `print` não mostra nada depois de um
`.filter()`", a resposta é lazy evaluation.

---

## 4. Spark SQL — sua maior vantagem de transferência

Você já domina SQL avançado. No Databricks, você pode escrever SQL puro em vez de PySpark:

```sql
%sql
SELECT agente_id, AVG(tmo_segundos) AS tmo_medio
FROM interacoes
WHERE data >= '2026-07-01'
GROUP BY agente_id
ORDER BY tmo_medio DESC
```

Isso é literalmente o mesmo SQL que você já escreve — a única diferença é que roda distribuído
por trás. **Esse é provavelmente o seu ponto de entrada mais forte para a entrevista**: você não
precisa aprender um paradigma novo para fazer análises, só precisa saber que Spark SQL existe
e que interopera livremente com DataFrames PySpark (pode alternar entre os dois no mesmo notebook).

---

## 5. Partições, shuffle e performance (tópico clássico de entrevista sênior)

- **Partição**: Spark divide os dados em pedaços (partições) distribuídos entre executors.
  Mais partições = mais paralelismo, até certo ponto.
- **Shuffle**: quando uma operação precisa reorganizar dados entre partições (ex: `groupBy`,
  `join`, `orderBy`), Spark move dados pela rede entre executors — é a operação mais cara.
  Minimizar shuffle é a maior alavanca de performance.
- **`repartition()` vs `coalesce()`**: `repartition` reembaralha os dados para mudar o número
  de partições (caro, mas equilibra carga); `coalesce` só reduz partições sem shuffle completo
  (mais barato, usado antes de escrever poucos arquivos de saída).
- **Broadcast join**: quando uma tabela é pequena (cabe na memória de cada executor), Spark
  pode "distribuir uma cópia" dela para todos os executors em vez de fazer shuffle nas duas
  tabelas grandes — acelera muito joins tabela-grande × tabela-pequena (ex: interações ×
  cadastro de agentes).

**Pergunta clássica:** "Como você otimizaria um join lento no Spark?" Resposta-base: verificar
se uma das tabelas é pequena o suficiente para broadcast join, verificar skew de dados
(partições desbalanceadas), e revisar se há shuffle desnecessário antes do join.

**Como conectar:** seu trabalho no SJUR com reclassificação de risco em milhares de processos e
no CIDA com corpus de 1.750 documentos já exige que você pense em "o que é caro de recalcular"
(por isso o GridSearchCV com cv=3 em vez de cv=10, por exemplo) — é o mesmo tipo de raciocínio
de custo computacional, só que a unidade de otimização muda de "tempo de CPU" para "shuffle de
rede entre máquinas".

---

## 6. Databricks — o que é específico da plataforma (não é só "Spark hospedado")

### Delta Lake
Formato de tabela sobre Parquet que adiciona:
- **ACID transactions** — múltiplos jobs podem escrever na mesma tabela sem corromper dados
- **Time travel** — `SELECT * FROM tabela VERSION AS OF 5` ou `TIMESTAMP AS OF '2026-07-01'`,
  permite auditar/reverter dados (relevante para o "manutenção de modelos perenes" que a vaga
  menciona)
- **`MERGE INTO`** — upsert nativo (insere se não existe, atualiza se existe), essencial para
  pipelines incrementais de dados de contact center chegando continuamente
- **Schema evolution/enforcement** — controla o que acontece quando o schema dos dados muda

**Como conectar:** seus `migrate()` idempotentes documentados nos padrões de projeto (SE-SUITE
Utils, P2D) são exatamente o mesmo princípio de idempotência que o `MERGE INTO` do Delta
resolve nativamente — você já pensa assim, só não tinha o nome "Delta Lake" pra isso.

### MLflow — provavelmente o mais relevante para você
Ferramenta nativa do Databricks para ciclo de vida de ML:
- **Tracking**: registra parâmetros, métricas e artefatos de cada treino (equivalente aos
  relatórios de accuracy/F1/matriz de confusão que você já gera no CIDA, mas versionado
  automaticamente em vez de PNG/JSON manual)
- **Model Registry**: versiona modelos e controla estágios (Staging → Production → Archived)
- **Model Serving**: expõe um modelo registrado como endpoint REST gerenciado — o equivalente
  Databricks-nativo da sua API Flask/JWT do CIDA ou do FastAPI do P2D

**Como conectar — este é o seu argumento mais forte:** você já opera todo o ciclo "treinar →
avaliar com métricas → servir via API → monitorar" manualmente (CIDA: scikit-learn/PyTorch →
relatório de métricas → Flask/JWT/Docker; P2D: telemetria de taxa de erro e qualidade de saída
por versão de prompt). MLflow **automatiza exatamente esse fluxo que você já faz à mão**. Isso é
uma resposta de entrevista muito mais forte que "nunca usei MLflow" — é "eu já implemento o
ciclo que o MLflow formaliza, e sei exatamente o que ele resolveria para mim: versionamento
automático em vez de manual, e um endpoint gerenciado em vez de eu manter o Docker/Gunicorn".

### Databricks Workflows (Jobs)
Orquestração de pipelines — agendar notebooks/scripts, definir dependências entre tarefas,
retries automáticos, alertas de falha.

**Como conectar:** isso é BPM aplicado a pipelines de dados. Você já projetou 90+ processos em
BizAgi e o `Orchestrator._PLAN` do P2D — a lógica de "etapas com dependência, retry, e falha
tratada" é a mesma, só muda a ferramenta.

### Databricks Repos + Unity Catalog (mencionar, não aprofundar)
- **Repos**: integração Git nativa dentro do Databricks (a vaga menciona "documentado e
  versionado (Git)" — Databricks Repos é literalmente isso)
- **Unity Catalog**: governança centralizada de dados (permissões, linhagem, catálogo) —
  conecta com sua experiência de governança de dados/IA (LGPD no P2D, ISO 9000)

---

## 7. Exercício prático — tente resolver antes da entrevista

Cenário adaptado ao domínio da vaga (Contact Center):

```python
# Tabela: interacoes (agente_id, data, tmo_segundos, csat, transferida)
# Objetivo: TMO médio e CSAT médio por agente, só interações não transferidas,
# ordenado do pior para o melhor TMO

from pyspark.sql import functions as F

resultado = (
    spark.table("interacoes")
    .filter(F.col("transferida") == False)
    .groupBy("agente_id")
    .agg(
        F.avg("tmo_segundos").alias("tmo_medio"),
        F.avg("csat").alias("csat_medio"),
        F.count("*").alias("total_interacoes")
    )
    .orderBy(F.desc("tmo_medio"))
)
resultado.show()
```

Se você consegue ler esse código e explicar cada linha (mesmo sem ter escrito do zero), você já
está em posição defensável para a entrevista técnica. O padrão `filter → groupBy → agg →
orderBy` é idêntico ao que você já faz em Pandas ou SQL puro.

---

## 8. Como responder "você tem experiência com Databricks?" honestamente e bem

Não minta e não se desculpe. Estrutura sugerida:

> "Não tenho experiência hands-on em Databricks especificamente, mas tenho experiência sólida
> em todo o ciclo que o Databricks formaliza — construí e operei sozinho pipelines de ML em
> produção com scikit-learn e PyTorch (GPU/CUDA), com API de serving, monitoramento e
> versionamento manual do que o MLflow automatiza. Estudei os fundamentos de PySpark e Delta
> Lake e entendo onde a transição precisa de atenção: pensar em termos de paralelismo
> distribuído e shuffle em vez de processamento local, e usar Spark SQL como ponte, já que
> domino SQL avançado. Espero produtividade real em poucas semanas, não meses."

Isso é honesto, específico, e transforma o gap num plano de ação concreto — exatamente o tipo
de resposta que sustenta sua marca de "assumo o que não sei e entrego mesmo assim".

---

## Referências para aprofundar (se sobrar tempo)

- Databricks Academy — "Data Engineering with Databricks" (curso oficial gratuito, cobre Delta
  Lake e Workflows)
- PySpark DataFrame API oficial — documentação Apache Spark (pyspark.sql.functions é o módulo
  mais usado no dia a dia)
- MLflow Quickstart (mlflow.org) — 30 minutos, cobre tracking + registry
