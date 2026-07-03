"""
Compatibilidade reversa — este arquivo foi mantido para não quebrar o fluxo antigo.
O novo entry point é: python scripts/generate_cv.py

Para gerar os PDFs, use preferencialmente:
    python scripts/generate_cv.py
    python scripts/generate_cv.py --lang pt
    python scripts/generate_cv.py --lang en
"""

import os
import sys

if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(__file__))
    from scripts.generate_cv import main
    main()
    sys.exit(0)

# --- LEGACY CODE BELOW (mantido como referência histórica) ---

import os
from fpdf import FPDF
from datetime import datetime

# --- CONFIGURAÇÃO DE DADOS ---

# Dados Pessoais
NOME = "PEDRO GENTIL REGATO DE OLIVEIRA SOARES"
TITULO = "ARQUITETO DE SOLUÇÕES ANALÍTICAS | ESTATÍSTICA APLICADA | ML/NLP & GENAI | PYTHON | DADOS & GOVERNANÇA"
CONTATO = "Rio de Janeiro - RJ | pedro.regato@gmail.com | +55 21 99330-6338 | LinkedIn"
LINKEDIN_URL = "https://www.linkedin.com/in/pedro-regato-0b6b3b13/"

# Resumo Profissional
RESUMO_TITULO = "PERFIL PROFISSIONAL | PROPOSTA DE VALOR"
RESUMO_TEXTO = """Sou profissional com formação em Estatística e perfil T-shaped: profundidade em modelagem quantitativa e raciocínio analítico, com atuação ampla em processos de negócio, automação e tecnologia.

Minha trajetória evoluiu de soluções baseadas em modelagem e simulação (logística/operacional) para iniciativas de Ciência de Dados, Machine Learning, NLP e IA aplicada. Nem todo desafio exigiu estatística formal - mas o rigor de hipótese, evidência, medição e risco sempre orientou minhas decisões técnicas e de negócio.

Meu diferencial está em integrar Modelo -> Sistema -> Processo. Em vez de análises isoladas, desenho soluções operáveis (dados, automação, governança, observabilidade e custo), sustentáveis do ponto de vista institucional."""

# Destaques de Impacto (Caixa Verde)
DESTAQUES_TITULO = "DESTAQUES DE IMPACTO"
DESTAQUES_LISTA = [
    "R$ 27,3 milhões: redução de provisões jurídicas com 4.977 processos saneados e 92% de acurácia em classificações críticas (projeto SJUR).",
    ">97% de acurácia: e >50% de redução de esforço humano na classificação de documentos acadêmicos, com operação governada em escala (projeto CIDA).",
    "~30% de redução: do tempo restante de execução em projeto crítico (consultoria Xerox Brasil), por solução inovadora aplicada em cenário real.",
    "Transformação de Governança: Migração de fluxos 'estáticos' (SharePoint/e-mail) para operação integrada (BPMN/Workflow/ECM + IA) na Auditoria Interna da FGV."
]

# Experiência Profissional
EXPERIENCIA_TITULO = "EXPERIÊNCIA PROFISSIONAL & PROJETOS RELEVANTES"
EXPERIENCIA_LISTA = [
    {
        "empresa": "FUNDAÇÃO GETÚLIO VARGAS (FGV)",
        "periodo": "2014 - Atual",
        "cargo": "Estatístico Sênior | Arquiteto de Soluções Analíticas",
        "detalhes": [
            "Liderança técnica em projetos de IA/ML e automação para áreas corporativas (Jurídico, Auditoria, Acadêmico), atuando desde a concepção (PoC) até a produtização e governança.",
            "Desenvolvimento de pipelines de dados e modelos preditivos/classificatórios (Python, Scikit-learn, NLP) integrados a sistemas de gestão (BPMN/ECM).",
            "Mentoria técnica e disseminação de cultura Data-Driven para equipes de negócio e TI."
        ]
    },
    {
        "empresa": "XEROX BRASIL (Consultoria)",
        "periodo": "2012 - 2014",
        "cargo": "Consultor Sênior de Processos & Estatística",
        "detalhes": [
            "Atuação em projetos críticos de outsourcing de impressão e gestão documental.",
            "Aplicação de modelagem estatística para otimização de SLA e dimensionamento de recursos.",
            "Recuperação de projeto em crise (turnaround) através de redesenho de processos e simulação de cenários."
        ]
    },
    {
        "empresa": "CONSULTORIA INDEPENDENTE",
        "periodo": "2008 - 2012",
        "cargo": "Estatístico & Consultor de Negócios",
        "detalhes": [
            "Projetos de inteligência de mercado, análise de risco e modelagem financeira para clientes de médio porte.",
            "Desenvolvimento de dashboards e ferramentas de apoio à decisão."
        ]
    }
]

# Barra Lateral
COMPETENCIAS_TITULO = "COMPETÊNCIAS-CHAVE"
COMPETENCIAS_GRUPOS = [
    {
        "grupo": "ESTATÍSTICA & MODELAGEM",
        "itens": [
            "Estatística Descritiva/Inferencial",
            "Testes de Hipóteses & Validação",
            "Modelagem Probabilística/Preditiva",
            "Séries Temporais",
            "Análise Discriminante"
        ]
    },
    {
        "grupo": "IA & ENGENHARIA DE DADOS",
        "itens": [
            "Machine Learning (Scikit-learn)",
            "Deep Learning (PyTorch/Keras)",
            "NLP & LLMs (OpenAI, Llama, RAG)",
            "Engenharia de Prompt",
            "ETL/ELT & SQL Avançado"
        ]
    },
    {
        "grupo": "DESENVOLVIMENTO & GOVERNANÇA",
        "itens": [
            "Python (Pandas, NumPy, FastAPI)",
            "R (Tidyverse, Shiny)",
            "BPMN & Automação de Processos",
            "Governança de Dados/IA",
            "Metodologias Ágeis (Scrum/Kanban)"
        ]
    }
]

EDUCACAO_TITULO = "FORMAÇÃO ACADÊMICA"
EDUCACAO_LISTA = [
    "MBA em Gestão Estratégica e Econômica de Negócios\nInstituição: Fundação Getúlio Vargas - FGV, Agosto/2014",
    "Extensão em Análise e Projeto Estruturado de Sistemas\nInstituição: Universidade do Estado do Rio de Janeiro - UERJ, Dez /1990",
    "Graduação em Estatística\nInstituição: Departamento de Matemática e Estatística da Universidade do Estado do Rio de Janeiro - UERJ, Dez /1990"
]

IDIOMAS_TITULO = "IDIOMAS"
IDIOMAS_LISTA = [
    "Português (Nativo)",
    "Inglês (Avançado/Fluente)"
]

PUBLICACOES_TITULO = "PUBLICAÇÕES"
PUBLICACOES_LISTA = [
    "LEARN MATE - Multi Agent AI Tutor (LinkedIn, Dez/2025)",
    "Visão e Missão (LinkedIn, Jul/2018)",
    "Passivos Subjetivos (LinkedIn, Jul/2018)",
    "Estratégia em Ação (LinkedIn, Jun/2018)"
]

DEPOIMENTOS_TITULO = "DEPOIMENTOS"
DEPOIMENTOS_LISTA = [
    {
        "texto": "\"Inovação decisiva em momento crítico: propôs e executou solução com risco técnico controlado, gerando ~30% de economia no tempo restante e permitindo entrega antes do prazo. Profissional brilhante e confiável.\"",
        "autor": "Rodrigo Monteiro Gaio - PMP | IT Project Manager (Xerox Brasil)",
        "link": "https://www.linkedin.com/in/rodrigogaiopmp/"
    },
    {
        "texto": "\"Profissional business-solution driven, altamente comprometido com resultado e rigor técnico. Entrega soluções simples e brilhantes, com visão, ética, confiabilidade e forte capacidade de relacionamento e liderança.\"",
        "autor": "Joaquim Santos Neto - CIO | Transformação Digital",
        "link": "https://www.linkedin.com/in/joaquimsantosneto/"
    },
    {
        "texto": "\"Consultor com vasta experiência em soluções de TI, reconhecido por profissionalismo e responsabilidade. Atuou em projeto pioneiro de Gestão de Serviços de TIC (ITIL v3) na PMESP, desenhando e implementando o modelo de gerenciamento.\"",
        "autor": "Aércio Dornelas - MBA, PMP, CBPP - Cliente",
        "link": "https://www.linkedin.com/in/aerciodornelas/"
    },
    {
        "texto": "\"Profissional atento a detalhes, focado em resultados, paciente e engajado na solução de problemas.\"",
        "autor": "Marcel Dubiella - IBM Maximo Senior Consultant",
        "link": "https://www.linkedin.com/in/marceldf/"
    }
]

# --- TRADUÇÃO PARA INGLÊS ---
EN_DATA = {
    "TITULO": "ANALYTICAL SOLUTIONS ARCHITECT | APPLIED STATISTICS | ML/NLP & GENAI | PYTHON | DATA & GOVERNANCE",
    "CONTATO": "Rio de Janeiro - RJ | pedro.regato@gmail.com | +55 21 99330-6338 | LinkedIn",
    "RESUMO_TITULO": "PROFESSIONAL PROFILE | VALUE PROPOSITION",
    "RESUMO_TEXTO": """I am a professional with a background in Statistics and a T-shaped profile: depth in quantitative modeling and analytical reasoning, with broad application in business processes, automation, and technology.

My trajectory evolved from solutions based on modeling and simulation (logistics/operational) to Data Science, Machine Learning, NLP, and Applied AI initiatives. Not every challenge required formal statistics - but the rigor of hypothesis, evidence, measurement, and risk has always guided my technical and business decisions.

My differentiator lies in integrating Model -> System -> Process. Instead of isolated analyses, I design operable solutions (data, automation, governance, observability, and cost) that are sustainable from an institutional perspective.""",
    "DESTAQUES_TITULO": "IMPACT HIGHLIGHTS",
    "DESTAQUES_LISTA": [
        "R$ 27.3 million: reduction in legal provisions with 4,977 lawsuits cleansed and 92% accuracy in critical classifications (SJUR project).",
        ">97% accuracy: and >50% reduction in human effort in academic document classification, with governed operation at scale (CIDA project).",
        "~30% reduction: in remaining execution time on a critical project (Xerox Brasil consulting), through an innovative solution applied in a real-world scenario.",
        "Governance Transformation: Migration of 'static' flows (SharePoint/email) to integrated operation (BPMN/Workflow/ECM + AI) in FGV Internal Audit."
    ],
    "EXPERIENCIA_TITULO": "PROFESSIONAL EXPERIENCE & RELEVANT PROJECTS",
    "EXPERIENCIA_LISTA": [
        {
            "empresa": "FUNDAÇÃO GETÚLIO VARGAS (FGV)",
            "periodo": "2014 - Present",
            "cargo": "Senior Statistician | Analytical Solutions Architect",
            "detalhes": [
                "Technical leadership in AI/ML and automation projects for corporate areas (Legal, Audit, Academic), acting from conception (PoC) to productization and governance.",
                "Development of data pipelines and predictive/classificatory models (Python, Scikit-learn, NLP) integrated with management systems (BPMN/ECM).",
                "Technical mentorship and dissemination of Data-Driven culture for business and IT teams."
            ]
        },
        {
            "empresa": "XEROX BRASIL (Consulting)",
            "periodo": "2012 - 2014",
            "cargo": "Senior Process & Statistics Consultant",
            "detalhes": [
                "Action in critical print outsourcing and document management projects.",
                "Application of statistical modeling for SLA optimization and resource sizing.",
                "Recovery of a project in crisis (turnaround) through process redesign and scenario simulation."
            ]
        },
        {
            "empresa": "INDEPENDENT CONSULTING",
            "periodo": "2008 - 2012",
            "cargo": "Statistician & Business Consultant",
            "detalhes": [
                "Market intelligence, risk analysis, and financial modeling projects for mid-sized clients.",
                "Development of dashboards and decision support tools."
            ]
        }
    ],
    "COMPETENCIAS_TITULO": "KEY SKILLS",
    "COMPETENCIAS_GRUPOS": [
        {
            "grupo": "STATISTICS & MODELING",
            "itens": [
                "Descriptive/Inferential Statistics",
                "Hypothesis Testing & Validation",
                "Probabilistic/Predictive Modeling",
                "Time Series",
                "Discriminant Analysis"
            ]
        },
        {
            "grupo": "AI & DATA ENGINEERING",
            "itens": [
                "Machine Learning (Scikit-learn)",
                "Deep Learning (PyTorch/Keras)",
                "NLP & LLMs (OpenAI, Llama, RAG)",
                "Prompt Engineering",
                "ETL/ELT & Advanced SQL"
            ]
        },
        {
            "grupo": "DEVELOPMENT & GOVERNANCE",
            "itens": [
                "Python (Pandas, NumPy, FastAPI)",
                "R (Tidyverse, Shiny)",
                "BPMN & Process Automation",
                "Data/AI Governance",
                "Agile Methodologies (Scrum/Kanban)"
            ]
        }
    ],
    "EDUCACAO_TITULO": "ACADEMIC BACKGROUND",
    "EDUCACAO_LISTA": [
        "MBA in Strategic and Economic Business Management\nInstitution: Fundação Getúlio Vargas - FGV, August/2014",
        "Extension in Structured Systems Analysis and Design\nInstitution: Rio de Janeiro State University - UERJ, Dec/1990",
        "B.S. in Statistics\nInstitution: Department of Mathematics and Statistics, Rio de Janeiro State University - UERJ, Dec/1990"
    ],
    "IDIOMAS_TITULO": "LANGUAGES",
    "IDIOMAS_LISTA": [
        "Portuguese (Native)",
        "English (Advanced/Fluent)"
    ],
    "PUBLICACOES_TITULO": "PUBLICATIONS",
    "PUBLICACOES_LISTA": [
        "LEARN MATE - Multi Agent AI Tutor (LinkedIn, Dec/2025)",
        "Vision and Mission (LinkedIn, Jul/2018)",
        "Subjective Liabilities (LinkedIn, Jul/2018)",
        "Strategy in Action (LinkedIn, Jun/2018)"
    ],
    "DEPOIMENTOS_TITULO": "TESTIMONIALS",
    "DEPOIMENTOS_LISTA": [
        {
            "texto": "\"Decisive innovation at a critical moment: proposed and executed a solution with controlled technical risk, generating ~30% savings in remaining time and allowing delivery ahead of schedule. Brilliant and reliable professional.\"",
            "autor": "Rodrigo Monteiro Gaio - PMP | IT Project Manager (Xerox Brasil)",
            "link": "https://www.linkedin.com/in/rodrigogaiopmp/"
        },
        {
            "texto": "\"Business-solution driven professional, highly committed to results and technical rigor. Delivers simple and brilliant solutions, with vision, ethics, reliability, and strong relationship and leadership skills.\"",
            "autor": "Joaquim Santos Neto - CIO | Digital Transformation",
            "link": "https://www.linkedin.com/in/joaquimsantosneto/"
        },
        {
            "texto": "\"Consultant with vast experience in IT solutions, recognized for professionalism and responsibility. Acted in a pioneering ICT Service Management (ITIL v3) project at PMESP, designing and implementing the management model.\"",
            "autor": "Aércio Dornelas - MBA, PMP, CBPP - Client",
            "link": "https://www.linkedin.com/in/aerciodornelas/"
        },
        {
            "texto": "\"Professional attentive to details, focused on results, patient, and engaged in problem-solving.\"",
            "autor": "Marcel Dubiella - IBM Maximo Senior Consultant",
            "link": "https://www.linkedin.com/in/marceldf/"
        }
    ]
}

# --- CLASSE PDF ---

class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

    def draw_sidebar(self, sidebar_width, height, photo_path, competencias_titulo, competencias_grupos, educacao_titulo, educacao_lista, idiomas_titulo, idiomas_lista, publicacoes_titulo, publicacoes_lista):
        # Fundo Cinza Claro da Barra Lateral
        self.set_fill_color(245, 245, 245)
        self.rect(0, 0, sidebar_width, height, 'F')

        # --- CABEÇALHO DA BARRA LATERAL (GEOMETRIA CORRIGIDA - V30) ---
        # Forma verde preenchendo o canto superior esquerdo e descendo em curva diagonal
        self.set_fill_color(26, 188, 156)  # Verde Água (Teal)
        
        # Desenhar a forma curva suave usando path context do fpdf2
        try:
            with self.local_context(fill_opacity=1):
                with self.path(paint_rule='f') as path:
                    path.move_to(0, 0)
                    path.line_to(sidebar_width * 0.8, 0)
                    path.curve_to(0, 240, sidebar_width * 0.8, 100, 0, 180)
                    path.line_to(0, 0)
                    path.close()
        except AttributeError:
            # Fallback para versões antigas do fpdf2 (se necessário)
            pass

        # Foto
        if os.path.exists(photo_path):
            photo_y = 40
            photo_size = 50
            photo_x = (sidebar_width - photo_size) / 2
            
            self.image(photo_path, x=photo_x, y=photo_y, w=photo_size)
            
            # Borda Branca Grossa
            self.set_draw_color(255, 255, 255)
            self.set_line_width(3)
            self.rect(photo_x, photo_y, photo_size, photo_size)

        # Conteúdo da Barra Lateral
        self.set_text_color(50, 60, 70)
        # CORREÇÃO: Ajustar current_y para logo abaixo da foto (aprox y=100) em vez de 260
        current_y = 110

        # Margem interna da barra lateral
        margin_left = 10
        content_width = sidebar_width - 20 # Largura útil para texto

        # Competências
        self.set_font('Arial', 'B', 11) # Fonte reduzida para caber (V32)
        
        # Título com linha inferior
        self.set_xy(margin_left, current_y)
        # Verifica se o título cabe, se não, quebra
        if self.get_string_width(competencias_titulo) > content_width:
             self.multi_cell(content_width, 6, competencias_titulo.upper())
        else:
             self.cell(content_width, 6, competencias_titulo.upper(), 0, 1, 'L')
        
        # Linha decorativa abaixo do título
        line_y = self.get_y() + 1
        self.set_draw_color(41, 128, 185) # Azul
        self.set_line_width(0.5)
        self.line(margin_left, line_y, margin_left + 30, line_y) # Linha curta
        
        current_y = line_y + 8

        for grupo in competencias_grupos:
            self.set_xy(margin_left, current_y)
            self.set_font('Arial', 'B', 9)
            self.set_text_color(44, 62, 80)
            self.multi_cell(content_width, 5, grupo['grupo'].upper())
            current_y = self.get_y() + 2
            
            self.set_font('Arial', '', 9)
            self.set_text_color(80, 80, 80)
            for item in grupo['itens']:
                self.set_xy(margin_left, current_y)
                self.multi_cell(content_width, 5, f"- {item}")
                current_y = self.get_y()
            current_y += 4

        # Formação Acadêmica
        current_y += 5
        self.set_xy(margin_left, current_y)
        self.set_font('Arial', 'B', 11)
        self.set_text_color(50, 60, 70)
        self.cell(content_width, 6, educacao_titulo.upper(), 0, 1, 'L')
        
        line_y = self.get_y() + 1
        self.set_draw_color(41, 128, 185)
        self.line(margin_left, line_y, margin_left + 30, line_y)
        current_y = line_y + 6

        for item in educacao_lista:
            self.set_xy(margin_left, current_y)
            self.set_font('Arial', '', 8) # Fonte um pouco menor para caber detalhes
            self.set_text_color(80, 80, 80)
            self.multi_cell(content_width, 4, item)
            current_y = self.get_y() + 4

        # Idiomas
        current_y += 2
        self.set_xy(margin_left, current_y)
        self.set_font('Arial', 'B', 11)
        self.set_text_color(50, 60, 70)
        self.cell(content_width, 6, idiomas_titulo.upper(), 0, 1, 'L')
        
        line_y = self.get_y() + 1
        self.set_draw_color(41, 128, 185)
        self.line(margin_left, line_y, margin_left + 30, line_y)
        current_y = line_y + 6

        self.set_font('Arial', '', 9)
        self.set_text_color(80, 80, 80)
        for item in idiomas_lista:
            self.set_xy(margin_left, current_y)
            self.multi_cell(content_width, 5, f"- {item}")
            current_y = self.get_y()

        # Publicações
        current_y += 6
        self.set_xy(margin_left, current_y)
        self.set_font('Arial', 'B', 11)
        self.set_text_color(50, 60, 70)
        self.cell(content_width, 6, publicacoes_titulo.upper(), 0, 1, 'L')
        
        line_y = self.get_y() + 1
        self.set_draw_color(41, 128, 185)
        self.line(margin_left, line_y, margin_left + 30, line_y)
        current_y = line_y + 6

        self.set_font('Arial', '', 8)
        self.set_text_color(80, 80, 80)
        for item in publicacoes_lista:
            self.set_xy(margin_left, current_y)
            self.multi_cell(content_width, 4, f"- {item}")
            current_y = self.get_y() + 2

def create_cv(filename, language="pt"):
    pdf = PDF()
    pdf.add_page()
    
    # Configurações de Layout
    sidebar_width = 70
    main_content_x = sidebar_width + 10
    main_content_width = 210 - sidebar_width - 20
    page_height = 297

    # Dados baseados no idioma
    if language == "pt":
        t_titulo = TITULO
        t_contato = CONTATO
        t_resumo_tit = RESUMO_TITULO
        t_resumo_txt = RESUMO_TEXTO
        t_destaques_tit = DESTAQUES_TITULO
        t_destaques_lista = DESTAQUES_LISTA
        t_exp_tit = EXPERIENCIA_TITULO
        t_exp_lista = EXPERIENCIA_LISTA
        t_comp_tit = COMPETENCIAS_TITULO
        t_comp_grupos = COMPETENCIAS_GRUPOS
        t_edu_tit = EDUCACAO_TITULO
        t_edu_lista = EDUCACAO_LISTA
        t_idiomas_tit = IDIOMAS_TITULO
        t_idiomas_lista = IDIOMAS_LISTA
        t_pub_tit = PUBLICACOES_TITULO
        t_pub_lista = PUBLICACOES_LISTA
        t_dep_tit = DEPOIMENTOS_TITULO
        t_dep_lista = DEPOIMENTOS_LISTA
    else:
        t_titulo = EN_DATA["TITULO"]
        t_contato = EN_DATA["CONTATO"]
        t_resumo_tit = EN_DATA["RESUMO_TITULO"]
        t_resumo_txt = EN_DATA["RESUMO_TEXTO"]
        t_destaques_tit = EN_DATA["DESTAQUES_TITULO"]
        t_destaques_lista = EN_DATA["DESTAQUES_LISTA"]
        t_exp_tit = EN_DATA["EXPERIENCIA_TITULO"]
        t_exp_lista = EN_DATA["EXPERIENCIA_LISTA"]
        t_comp_tit = EN_DATA["COMPETENCIAS_TITULO"]
        t_comp_grupos = EN_DATA["COMPETENCIAS_GRUPOS"]
        t_edu_tit = EN_DATA["EDUCACAO_TITULO"]
        t_edu_lista = EN_DATA["EDUCACAO_LISTA"]
        t_idiomas_tit = EN_DATA["IDIOMAS_TITULO"]
        t_idiomas_lista = EN_DATA["IDIOMAS_LISTA"]
        t_pub_tit = EN_DATA["PUBLICACOES_TITULO"]
        t_pub_lista = EN_DATA["PUBLICACOES_LISTA"]
        t_dep_tit = EN_DATA["DEPOIMENTOS_TITULO"]
        t_dep_lista = EN_DATA["DEPOIMENTOS_LISTA"]

    # Desenhar Barra Lateral
    # Desativar quebra de página automática para a barra lateral para evitar que ela empurre o conteúdo
    pdf.set_auto_page_break(False)
    pdf.draw_sidebar(sidebar_width, page_height, "data/linkedin/FotoLinkedin.png", 
                     t_comp_tit, t_comp_grupos, t_edu_tit, t_edu_lista, t_idiomas_tit, t_idiomas_lista, t_pub_tit, t_pub_lista)
    
    # Reativar quebra de página automática para o conteúdo principal
    pdf.set_auto_page_break(True, margin=15)

    # --- CONTEÚDO PRINCIPAL ---
    # Definir a margem esquerda para o conteúdo principal para evitar sobreposição
    pdf.set_left_margin(main_content_x)
    
    # Forçar o cursor para o topo da página atual
    pdf.set_y(20)
    # Não é necessário set_x se a margem esquerda estiver definida, mas mal não faz
    pdf.set_x(main_content_x)

    # Nome
    pdf.set_font('Arial', 'B', 22)
    pdf.set_text_color(44, 62, 80) # Azul Escuro
    pdf.multi_cell(main_content_width, 8, NOME)
    
    # Título Profissional
    pdf.ln(2)
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(main_content_width, 5, t_titulo)

    # Linha Divisória
    pdf.ln(2)
    pdf.set_draw_color(41, 128, 185)
    pdf.set_line_width(0.5)
    pdf.line(main_content_x, pdf.get_y(), main_content_x + main_content_width, pdf.get_y())

    # Contato
    pdf.ln(3)
    pdf.set_font('Arial', '', 9)
    pdf.set_text_color(127, 140, 141)
    
    # Processar links no contato (simples)
    pdf.cell(main_content_width, 5, t_contato, 0, 1, 'L', link=LINKEDIN_URL)

    # Destaques de Impacto (Caixa Verde) - ALTURA DINÂMICA (V31)
    pdf.ln(5)
    
    # Calcular altura necessária para o texto
    pdf.set_font('Arial', '', 9)
    line_height = 5
    total_text_height = 0
    
    # Simular a escrita para medir altura
    temp_y = 0
    # Título
    total_text_height += 8 
    # Itens
    for item in t_destaques_lista:
        # Get number of lines for this item
        # Try-except block to handle different fpdf2 versions
        try:
            # New fpdf2 versions use dry_run=True
            lines = pdf.multi_cell(main_content_width - 10, line_height, f"- {item}", dry_run=True, output="LINES")
        except TypeError:
            # Older fpdf2 versions use split_only=True
            lines = pdf.multi_cell(main_content_width - 10, line_height, f"- {item}", split_only=True)
            
        total_text_height += len(lines) * line_height
        total_text_height += 2 # Espaço entre itens
    
    box_height = total_text_height + 5 # Padding extra
    
    pdf.set_fill_color(232, 248, 245) # Verde muito claro
    pdf.set_draw_color(26, 188, 156) # Borda verde
    pdf.set_line_width(1)
    
    # Desenhar retângulo com borda esquerda grossa
    start_y = pdf.get_y()
    pdf.rect(main_content_x, start_y, main_content_width, box_height, 'F')
    
    # Borda esquerda grossa
    pdf.set_line_width(2)
    pdf.line(main_content_x, start_y, main_content_x, start_y + box_height)
    
    # Conteúdo da Caixa
    pdf.set_xy(main_content_x + 5, start_y + 3)
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(22, 160, 133)
    pdf.cell(main_content_width - 10, 6, t_destaques_tit, 0, 1)
    
    pdf.set_font('Arial', '', 9)
    pdf.set_text_color(44, 62, 80)
    for item in t_destaques_lista:
        pdf.set_x(main_content_x + 5)
        pdf.multi_cell(main_content_width - 10, 5, f"- {item}")
        pdf.ln(2)

    pdf.set_y(start_y + box_height + 5)

    # Resumo Profissional
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(main_content_width, 6, t_resumo_tit.upper(), 0, 1)
    
    pdf.set_draw_color(41, 128, 185)
    pdf.set_line_width(0.5)
    pdf.line(main_content_x, pdf.get_y(), main_content_x + main_content_width, pdf.get_y())
    pdf.ln(3)
    
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(main_content_width, 5, t_resumo_txt)
    pdf.ln(5)

    # Experiência Profissional
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(main_content_width, 6, t_exp_tit.upper(), 0, 1)
    
    pdf.set_draw_color(41, 128, 185)
    pdf.set_line_width(0.5)
    pdf.line(main_content_x, pdf.get_y(), main_content_x + main_content_width, pdf.get_y())
    pdf.ln(3)

    for exp in t_exp_lista:
        # Verificar quebra de página
        if pdf.get_y() > 250:
            pdf.add_page()
            pdf.draw_sidebar(sidebar_width, page_height, "data/linkedin/FotoLinkedin.png", 
                     t_comp_tit, t_comp_grupos, t_edu_tit, t_edu_lista, t_idiomas_tit, t_idiomas_lista, t_pub_tit, t_pub_lista)
            pdf.set_xy(main_content_x, 20)

        pdf.set_font('Arial', 'B', 11)
        pdf.set_text_color(44, 62, 80)
        pdf.cell(main_content_width * 0.7, 6, exp['empresa'].upper(), 0, 0)
        
        pdf.set_font('Arial', 'I', 10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(main_content_width * 0.3, 6, exp['periodo'], 0, 1, 'R')
        
        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(main_content_width, 5, exp['cargo'], 0, 1)
        
        pdf.ln(1)
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(60, 60, 60)
        for detalhe in exp['detalhes']:
            pdf.set_x(main_content_x)
            pdf.multi_cell(main_content_width, 5, f"- {detalhe}")
        pdf.ln(4)

    # Depoimentos (NOVA SEÇÃO - V26)
    # Verificar espaço para título
    if pdf.get_y() > 240:
        pdf.add_page()
        pdf.draw_sidebar(sidebar_width, page_height, "data/linkedin/FotoLinkedin.png", 
                     t_comp_tit, t_comp_grupos, t_edu_tit, t_edu_lista, t_idiomas_tit, t_idiomas_lista, t_pub_tit, t_pub_lista)
        pdf.set_xy(main_content_x, 20)

    pdf.ln(2)
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(main_content_width, 6, t_dep_tit.upper(), 0, 1)
    
    pdf.set_draw_color(41, 128, 185)
    pdf.set_line_width(0.5)
    pdf.line(main_content_x, pdf.get_y(), main_content_x + main_content_width, pdf.get_y())
    pdf.ln(3)

    for dep in t_dep_lista:
        # Verificar quebra de página para cada depoimento
        if pdf.get_y() > 260:
            pdf.add_page()
            pdf.draw_sidebar(sidebar_width, page_height, "data/linkedin/FotoLinkedin.png", 
                     t_comp_tit, t_comp_grupos, t_edu_tit, t_edu_lista, t_idiomas_tit, t_idiomas_lista, t_pub_tit, t_pub_lista)
            pdf.set_xy(main_content_x, 20)

        pdf.set_font('Arial', 'I', 9)
        pdf.set_text_color(80, 80, 80)
        pdf.multi_cell(main_content_width, 5, dep['texto'])
        
        pdf.ln(1)
        pdf.set_font('Arial', 'B', 9)
        pdf.set_text_color(41, 128, 185) # Azul link
        # Autor com link
        pdf.set_x(main_content_x)
        pdf.cell(main_content_width, 5, f"- {dep['autor']}", 0, 1, link=dep['link'])
        pdf.ln(3)

    pdf.output(filename)

if __name__ == "__main__":
    create_cv("Curriculo_Pedro_Gentil.pdf", "pt")
    create_cv("Resume_Pedro_Gentil.pdf", "en")
    print("Currículos gerados com sucesso!")
