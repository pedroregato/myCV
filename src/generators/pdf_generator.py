import os
from fpdf import FPDF


class CV(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

    def draw_sidebar(self, sidebar_width, page_height, photo_path, data):
        # Light gray background
        self.set_fill_color(245, 245, 245)
        self.rect(0, 0, sidebar_width, page_height, 'F')

        # Teal decorative shape in top-left corner
        self.set_fill_color(26, 188, 156)
        try:
            with self.local_context(fill_opacity=1):
                with self.path(paint_rule='f') as path:
                    path.move_to(0, 0)
                    path.line_to(sidebar_width * 0.8, 0)
                    path.curve_to(0, 240, sidebar_width * 0.8, 100, 0, 180)
                    path.line_to(0, 0)
                    path.close()
        except AttributeError:
            pass

        # Photo
        if os.path.exists(photo_path):
            photo_y = 40
            photo_size = 50
            photo_x = (sidebar_width - photo_size) / 2
            self.image(photo_path, x=photo_x, y=photo_y, w=photo_size)
            self.set_draw_color(255, 255, 255)
            self.set_line_width(3)
            self.rect(photo_x, photo_y, photo_size, photo_size)

        self.set_text_color(50, 60, 70)
        current_y = 110
        margin_left = 10
        content_width = sidebar_width - 20

        # Skills
        self.set_font('Arial', 'B', 11)
        self.set_xy(margin_left, current_y)
        title = data['competencias_titulo'].upper()
        if self.get_string_width(title) > content_width:
            self.multi_cell(content_width, 6, title)
        else:
            self.cell(content_width, 6, title, 0, 1, 'L')

        line_y = self.get_y() + 1
        self.set_draw_color(41, 128, 185)
        self.set_line_width(0.5)
        self.line(margin_left, line_y, margin_left + 30, line_y)
        current_y = line_y + 8

        for grupo in data['competencias']:
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

        # Education
        current_y += 5
        self.set_xy(margin_left, current_y)
        self.set_font('Arial', 'B', 11)
        self.set_text_color(50, 60, 70)
        self.cell(content_width, 6, data['educacao_titulo'].upper(), 0, 1, 'L')

        line_y = self.get_y() + 1
        self.set_draw_color(41, 128, 185)
        self.line(margin_left, line_y, margin_left + 30, line_y)
        current_y = line_y + 6

        for item in data['educacao']:
            self.set_xy(margin_left, current_y)
            self.set_font('Arial', '', 8)
            self.set_text_color(80, 80, 80)
            self.multi_cell(content_width, 4, item)
            current_y = self.get_y() + 4

        # Languages
        current_y += 2
        self.set_xy(margin_left, current_y)
        self.set_font('Arial', 'B', 11)
        self.set_text_color(50, 60, 70)
        self.cell(content_width, 6, data['idiomas_titulo'].upper(), 0, 1, 'L')

        line_y = self.get_y() + 1
        self.set_draw_color(41, 128, 185)
        self.line(margin_left, line_y, margin_left + 30, line_y)
        current_y = line_y + 6

        self.set_font('Arial', '', 9)
        self.set_text_color(80, 80, 80)
        for item in data['idiomas']:
            self.set_xy(margin_left, current_y)
            self.multi_cell(content_width, 5, f"- {item}")
            current_y = self.get_y()

        # Publications
        current_y += 6
        self.set_xy(margin_left, current_y)
        self.set_font('Arial', 'B', 11)
        self.set_text_color(50, 60, 70)
        self.cell(content_width, 6, data['publicacoes_titulo'].upper(), 0, 1, 'L')

        line_y = self.get_y() + 1
        self.set_draw_color(41, 128, 185)
        self.line(margin_left, line_y, margin_left + 30, line_y)
        current_y = line_y + 6

        self.set_font('Arial', '', 8)
        self.set_text_color(80, 80, 80)
        for item in data['publicacoes']:
            self.set_xy(margin_left, current_y)
            self.multi_cell(content_width, 4, f"- {item}")
            current_y = self.get_y() + 2


def create_cv(filename, data, photo_path="assets/FotoLinkedin.png"):
    pdf = CV()
    pdf.add_page()

    sidebar_width = 70
    main_x = sidebar_width + 10
    main_w = 210 - sidebar_width - 20
    page_height = 297

    def add_sidebar():
        pdf.set_auto_page_break(False)
        pdf.draw_sidebar(sidebar_width, page_height, photo_path, data)
        pdf.set_auto_page_break(True, margin=15)

    add_sidebar()

    # --- MAIN CONTENT ---
    pdf.set_left_margin(main_x)
    pdf.set_y(20)
    pdf.set_x(main_x)

    # Name
    pdf.set_font('Arial', 'B', 22)
    pdf.set_text_color(44, 62, 80)
    pdf.multi_cell(main_w, 8, data['nome'])

    # Professional title
    pdf.ln(2)
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(main_w, 5, data['titulo'])

    # Divider
    pdf.ln(2)
    pdf.set_draw_color(41, 128, 185)
    pdf.set_line_width(0.5)
    pdf.line(main_x, pdf.get_y(), main_x + main_w, pdf.get_y())

    # Contact
    pdf.ln(3)
    pdf.set_font('Arial', '', 9)
    pdf.set_text_color(127, 140, 141)
    pdf.cell(main_w, 5, data['contato'], 0, 1, 'L', link=data['linkedin_url'])

    # Impact highlights box (dynamic height)
    pdf.ln(5)
    pdf.set_font('Arial', '', 9)
    line_height = 5
    total_text_height = 8  # title height

    for item in data['destaques']:
        try:
            lines = pdf.multi_cell(main_w - 10, line_height, f"- {item}", dry_run=True, output="LINES")
        except TypeError:
            lines = pdf.multi_cell(main_w - 10, line_height, f"- {item}", split_only=True)
        total_text_height += len(lines) * line_height + 2

    box_height = total_text_height + 5
    start_y = pdf.get_y()

    pdf.set_fill_color(232, 248, 245)
    pdf.set_draw_color(26, 188, 156)
    pdf.set_line_width(1)
    pdf.rect(main_x, start_y, main_w, box_height, 'F')

    pdf.set_line_width(2)
    pdf.line(main_x, start_y, main_x, start_y + box_height)

    pdf.set_xy(main_x + 5, start_y + 3)
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(22, 160, 133)
    pdf.cell(main_w - 10, 6, data['destaques_titulo'], 0, 1)

    pdf.set_font('Arial', '', 9)
    pdf.set_text_color(44, 62, 80)
    for item in data['destaques']:
        pdf.set_x(main_x + 5)
        pdf.multi_cell(main_w - 10, 5, f"- {item}")
        pdf.ln(2)

    pdf.set_y(start_y + box_height + 5)

    # Professional summary
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(main_w, 6, data['resumo_titulo'].upper(), 0, 1)

    pdf.set_draw_color(41, 128, 185)
    pdf.set_line_width(0.5)
    pdf.line(main_x, pdf.get_y(), main_x + main_w, pdf.get_y())
    pdf.ln(3)

    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(main_w, 5, data['resumo_texto'].strip())
    pdf.ln(5)

    # Work experience
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(main_w, 6, data['experiencia_titulo'].upper(), 0, 1)

    pdf.set_draw_color(41, 128, 185)
    pdf.set_line_width(0.5)
    pdf.line(main_x, pdf.get_y(), main_x + main_w, pdf.get_y())
    pdf.ln(3)

    for exp in data['experiencia']:
        if pdf.get_y() > 250:
            pdf.add_page()
            add_sidebar()
            pdf.set_xy(main_x, 20)

        pdf.set_font('Arial', 'B', 11)
        pdf.set_text_color(44, 62, 80)
        pdf.cell(main_w * 0.7, 6, exp['empresa'].upper(), 0, 0)

        pdf.set_font('Arial', 'I', 10)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(main_w * 0.3, 6, exp['periodo'], 0, 1, 'R')

        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(main_w, 5, exp['cargo'], 0, 1)

        pdf.ln(1)
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(60, 60, 60)
        for detalhe in exp['detalhes']:
            pdf.set_x(main_x)
            pdf.multi_cell(main_w, 5, f"- {detalhe}")
        pdf.ln(4)

    # Testimonials
    if pdf.get_y() > 240:
        pdf.add_page()
        add_sidebar()
        pdf.set_xy(main_x, 20)

    pdf.ln(2)
    pdf.set_font('Arial', 'B', 12)
    pdf.set_text_color(44, 62, 80)
    pdf.cell(main_w, 6, data['depoimentos_titulo'].upper(), 0, 1)

    pdf.set_draw_color(41, 128, 185)
    pdf.set_line_width(0.5)
    pdf.line(main_x, pdf.get_y(), main_x + main_w, pdf.get_y())
    pdf.ln(3)

    for dep in data['depoimentos']:
        if pdf.get_y() > 260:
            pdf.add_page()
            add_sidebar()
            pdf.set_xy(main_x, 20)

        pdf.set_font('Arial', 'I', 9)
        pdf.set_text_color(80, 80, 80)
        pdf.multi_cell(main_w, 5, dep['texto'])

        pdf.ln(1)
        pdf.set_font('Arial', 'B', 9)
        pdf.set_text_color(41, 128, 185)
        pdf.set_x(main_x)
        pdf.cell(main_w, 5, f"- {dep['autor']}", 0, 1, link=dep['link'])
        pdf.ln(3)

    pdf.output(filename)
