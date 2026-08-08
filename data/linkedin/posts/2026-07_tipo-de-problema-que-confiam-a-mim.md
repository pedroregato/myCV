# Post LinkedIn — Este é o tipo de problema que confiam a mim
# Data: Julho/2026
# Tipo: reflexao/case
# Idioma: PT
# URL: (adicionar link quando publicado)
# Engajamento: (preencher após publicação)

---

## Este é o tipo de problema que confiam a mim e é assim que eu resolvo

**O problema que me entregam**

Não me chamam para "rodar um modelo" ou "montar um dashboard". Me chamam - ou eu mesmo identifico - quando o problema tem três características ao mesmo tempo:

1. Envolve risco real (jurídico, financeiro, operacional, reputacional) e ninguém tem certeza de onde ele está escondido.
2. Não existe uma solução pronta de mercado - ou existe, mas não fecha com a governança e os sistemas legados da instituição.
3. Não há squad dedicado para construir. Existe orçamento (ou só convicção pessoal) para *um* profissional que assuma do discovery ao deploy.

Dois exemplos concretos - um encomendado, outro que eu mesmo enxerguei antes de qualquer um pedir.

**Por que confiam a mim esse tipo de problema**

Porque minha base não é só engenharia - é Estatística (UERJ). Hipótese, evidência, medição e risco vêm antes da ferramenta. Isso muda a forma como ataco o problema: não pergunto "qual modelo usar", pergunto "o que precisa ser verdadeiro para essa decisão ser confiável, e como eu meço isso continuamente depois que o sistema estiver no ar".

E porque entrego sozinho. Não documento o problema para uma equipe construir depois - eu concebo, prototipo, coloco em produção e opero. Prefiro codar com IA para resolver o problema real a escrever um relatório sobre ele.

---

### Caso 1 - SJUR/FGV: o problema que me encomendaram

A Superintendência Jurídica da FGV precisava saber, entre milhares de processos, quais representavam risco de perda relevante - e precisava saber *antes* de o processo virar réu formal, não depois. A alternativa era continuar provisionando contabilmente por estimativa, sem reclassificação de risco caso a caso.

Construí um ecossistema jurídico-IA: monitoramento via API pública do CNJ/DataJud + classificador de citações em Diários Oficiais via LLM, com trilha de auditoria em cada classificação.

**Resultado:** R$ 28 milhões em economia de provisionamento contábil anual, 4.980 processos saneados em 2025, 11.998 e-mails classificados com 88% de acurácia.

### Caso 2 - Process2Diagram: o problema que ninguém tinha nomeado

Este eu não recebi de ninguém. Eu vi o padrão se repetir em toda organização por onde passei: a reunião é o ativo mais caro da empresa e o menos documentado.

Os números que sustentam isso não são intuição - 71% das decisões estratégicas nascem em reuniões corporativas, uma hora de reunião executiva custa em média R$ 8,2 mil no Brasil, e 67% do conhecimento gerado nunca é formalizado (Gartner). Uma organização com 50 executivos reunidos 2h/dia gasta R$ 3,5 milhões/ano em reuniões - documentando menos de 33% do que decide. O retrabalho por conhecimento não documentado consome de 20% a 40% do esforço total de um projeto (PMI, 2024).

Ninguém me encomendou resolver isso. Mas é exatamente o tipo de risco silencioso que eu já sabia reconhecer - só que dessa vez o cliente era qualquer organização, e o produto eu tive que definir sozinho, do zero.

**O que construí:** uma plataforma de IA multi-agente que transforma a transcrição de uma reunião em 12 artefatos formais em menos de 5 minutos - diagrama BPMN 2.0, requisitos IEEE 830 com IDs rastreáveis, ata estruturada, vocabulário SBVR, Modelo de Motivação do Negócio (BMM), tabelas de decisão DMN, mapa de argumentação IBIS (o *porquê* de cada decisão, não só o *quê*), relatório executivo HTML e grafo de conhecimento acumulado entre reuniões. Pipeline com 13 agentes especializados, orquestrados por um Orchestrator próprio (LangGraph restrito a retry adaptativo de qualidade), suporte a 7 provedores de LLM sem lock-in de fornecedor (DeepSeek, Anthropic Claude, OpenAI, Azure OpenAI, Google Gemini, Groq, xAI Grok), e um assistente RAG com 151 ferramentas que responde perguntas cruzando todas as reuniões de um projeto.

A parte que mais me orgulha não é gerar diagrama bonito - é a governança embutida: cada decisão é rastreável da fala do participante até a regra de negócio (fala -> ata -> requisito -> etapa do BPMN -> tabela DMN), exportável em JSON-LD para sistemas de GRC, com camada própria de conformidade LGPD (pseudonimização reversível de dados pessoais, trilha de consentimento e auditoria versionadas em banco) e telemetria de custo/erro por provedor. E o sistema detecta contradições sozinho: num piloto simulado, uma reunião definiu prazo de integração em 90 dias e outra aprovou cronograma de 120 dias - o P2D sinalizou o conflito antes da reunião seguinte, antes de virar problema em produção.

**Resultado medido:** -90% no tempo de formalização de processos, -35% de retrabalho por falta de documentação, +80% de velocidade de onboarding de novos membros. Projeto autoral, 874 testes automatizados, em produção contínua.

---

**O padrão se repete**

O mesmo método aparece no CIDA (96% de acurácia, Macro F1: 0,96, na classificação de acervo acadêmico, em produção no HPC da FGV) e no DataJud Monitor (plataforma própria de monitoramento processual multi-tribunal). Problema encomendado ou problema que eu mesmo enxerguei - a disciplina é a mesma: medir antes de desenhar, integrar Modelo -> Sistema -> Processo, construir governança embutida, entregar e operar sozinho.

É por isso que este é o tipo de problema que confiam a mim - e às vezes nem precisam confiar, porque eu já vi o risco antes de alguém nomeá-lo. De um jeito ou de outro, é assim que eu resolvo: **construo sistemas onde método e execução não se separam.**

#IA #GenAI #EstatisticaAplicada #GovernancaDeIA #AutomacaoDeProcessos #MultiAgent #CarreiraDeDados
