"""Prompt templates for CV assistant features."""

SYSTEM_CV_EXPERT = """\
You are an expert career consultant and professional CV writer specializing in Data Science, \
AI/ML, and Analytics roles. You write in a clear, results-oriented style, quantifying impact \
whenever possible. You know Pedro Gentil's professional profile: Senior Statistician and \
Analytical Solutions Architect at FGV, with a T-shaped profile combining deep quantitative \
modeling expertise with broad coverage of business processes, automation, and AI/ML.\
"""

IMPROVE_BULLET_PT = """\
Abaixo está uma descrição de uma conquista ou atividade profissional de Pedro Gentil.
Reescreva como um bullet point de currículo em Português: conciso, orientado a resultado,
com verbo de ação no início, e — se possível — com métrica de impacto.
Retorne APENAS o texto do bullet, sem aspas ou formatação extra.

Descrição:
{description}

Contexto (seção do currículo):
{context}
"""

IMPROVE_BULLET_EN = """\
Below is a description of a professional achievement or activity by Pedro Gentil.
Rewrite it as a resume bullet point in English: concise, results-oriented,
starting with an action verb, and — if possible — including an impact metric.
Return ONLY the bullet text, without quotes or extra formatting.

Description:
{description}

Context (CV section):
{context}
"""

TRANSLATE_TO_EN = """\
Translate the following Portuguese CV text to professional English.
Preserve the tone, structure, and technical terminology.
Return ONLY the translated text, maintaining the same format (bullet lists, line breaks, etc.).

Text:
{text}
"""

TRANSLATE_TO_PT = """\
Traduza o seguinte texto de currículo em inglês para português profissional.
Preserve o tom, a estrutura e a terminologia técnica.
Retorne APENAS o texto traduzido, mantendo o mesmo formato (listas, quebras de linha, etc.).

Text:
{text}
"""

REVIEW_SECTION_PT = """\
Você está revisando a seção "{section}" do currículo de Pedro Gentil em Português.
Analise o conteúdo abaixo e forneça:
1. Pontos fortes
2. Sugestões de melhoria (máximo 3)
3. Versão revisada (se houver mudanças relevantes)

Conteúdo:
{content}
"""

REVIEW_SECTION_EN = """\
You are reviewing the "{section}" section of Pedro Gentil's CV in English.
Analyze the content below and provide:
1. Strengths
2. Improvement suggestions (max 3)
3. Revised version (if relevant changes exist)

Content:
{content}
"""

LINKEDIN_POST_PT = """\
Crie um post profissional para o LinkedIn em Português sobre o seguinte tema/conquista:

{achievement}

Tipo de post: {post_type}
Tipos disponíveis:
- case: case de resultado com contexto, solução e impacto quantificado
- tecnico: explicação técnica acessível com aprendizado ou insight
- reflexao: reflexão profissional ou de carreira, tom mais pessoal

Diretrizes:
- Tom: profissional mas autêntico, sem jargão excessivo
- Estrutura: gancho forte na primeira linha, desenvolvimento, chamada à ação ou pergunta final
- Tamanho: entre 150 e 300 palavras
- NÃO use emojis em excesso (máximo 2-3 se necessário)
- Inclua hashtags relevantes no final (5-7)

Retorne apenas o texto do post, pronto para publicar.
"""

LINKEDIN_POST_EN = """\
Create a professional LinkedIn post in English about the following topic/achievement:

{achievement}

Post type: {post_type}
Available types:
- case: result case with context, solution, and quantified impact
- technical: accessible technical explanation with a key learning or insight
- reflection: professional or career reflection, more personal tone

Guidelines:
- Tone: professional but authentic, avoid excessive jargon
- Structure: strong hook in the first line, development, call to action or closing question
- Length: between 150 and 300 words
- NO excessive emojis (max 2-3 if necessary)
- Include relevant hashtags at the end (5-7)

Return only the post text, ready to publish.
"""

SUGGEST_YAML_UPDATE_PT = """\
Pedro Gentil quer adicionar uma nova entrada ao seu currículo.

Seção alvo: {section}
Descrição do que aconteceu: {description}

Com base no perfil profissional dele (Estatístico Sênior / Arquiteto de Soluções Analíticas na FGV, \
foco em IA/ML, NLP, governança de dados e automação), gere o trecho YAML para inserir nessa seção.

Siga exatamente o formato YAML já usado no arquivo de perfil.
Retorne APENAS o bloco YAML, sem explicações adicionais.

Exemplo do formato da seção '{section}':
{example}
"""
