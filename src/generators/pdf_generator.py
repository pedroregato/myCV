import os
from fpdf import FPDF

# ── Palette ─────────────────────────────────────────────────────────────────
DARK        = (18,  18,  18)
AMBER       = (220, 150,  40)
WHITE       = (255, 255, 255)
LIGHT_GRAY  = (190, 190, 190)
MID_GRAY    = (120, 120, 120)
SECTION_COL = ( 40,  40,  40)
BODY_COL    = ( 65,  65,  65)
DIVIDER_COL = (195, 195, 195)

# ── Dimensions (A4 mm) ───────────────────────────────────────────────────────
PAGE_W    = 210
PAGE_H    = 297
SIDEBAR_W = 75
MAIN_X    = SIDEBAR_W
MAIN_W    = PAGE_W - SIDEBAR_W
HEADER_H  = 52        # dark band height on main side
S_MARGIN  = 9         # sidebar inner margin
S_CONT_W  = SIDEBAR_W - 2 * S_MARGIN
M_MARGIN  = 10        # main inner margin
M_CONT_W  = MAIN_W - 2 * M_MARGIN

BULLET_INDENT = 3.5   # mm: space reserved for bullet + gap

# Competencia group deferred to the sidebar continuation page (page 1 doesn't have room for it)
DEFERRED_COMPETENCIA_GROUPS = {"DESENVOLVIMENTO & GOVERNANÇA", "DEVELOPMENT & GOVERNANCE"}


# ── Helper ───────────────────────────────────────────────────────────────────
def _rgb(pdf, color, target="text"):
    r, g, b = color
    if target == "text":  pdf.set_text_color(r, g, b)
    elif target == "fill": pdf.set_fill_color(r, g, b)
    elif target == "draw": pdf.set_draw_color(r, g, b)


class CV(FPDF):
    def header(self): pass
    def footer(self): pass

    # ── Filled-square bullet + indented multi_cell ───────────────────────────
    def _bullet(self, x, y, w, line_h, text,
                text_color=BODY_COL, bullet_color=AMBER, sq=1.3):
        """Draw a small filled square then render text with hanging indent."""
        _rgb(self, bullet_color, "fill")
        self.rect(x + 0.2, y + (line_h - sq) * 0.5, sq, sq, "F")
        _rgb(self, text_color, "text")
        self.set_xy(x + BULLET_INDENT, y)
        self.multi_cell(w - BULLET_INDENT, line_h, text)

    # ── Real height a bullet will need, under the current font ──────────────
    def _bullet_height(self, w, line_h, text):
        lines = self.multi_cell(w - BULLET_INDENT, line_h, text,
                                 dry_run=True, output="LINES")
        return len(lines) * line_h

    # ── Sidebar background (every page) ─────────────────────────────────────
    def _draw_sidebar_bg(self):
        _rgb(self, DARK, "fill")
        self.rect(0, 0, SIDEBAR_W, PAGE_H, "F")

    # ── Wave decoration at bottom-left of sidebar ────────────────────────────
    def _draw_wave(self, data=None):
        _rgb(self, AMBER, "fill")
        _rgb(self, AMBER, "draw")
        self.set_line_width(0.1)
        with self.new_path(paint_rule="f") as p:
            p.move_to(0, PAGE_H)
            p.line_to(SIDEBAR_W, PAGE_H)
            p.line_to(SIDEBAR_W, PAGE_H - 22)
            p.curve_to(SIDEBAR_W * 0.55, PAGE_H - 12,
                       SIDEBAR_W * 0.35, PAGE_H - 38,
                       0, PAGE_H - 18)
            p.close()

        if data:
            _rgb(self, WHITE, "text")
            self.set_font("Arial", "B", 7)
            self.set_xy(0, PAGE_H - 14)
            self.cell(SIDEBAR_W, 4, data.get("wave_pro", ""), align="C")
            self.set_font("Arial", "", 7)
            self.set_xy(0, PAGE_H - 8)
            self.cell(SIDEBAR_W, 4, data.get("wave_pessoal", ""), align="C")

    # ── Circular photo (corner-masking technique) ────────────────────────────
    def _draw_circular_photo(self, photo_path, cx, cy, radius):
        if not os.path.exists(photo_path):
            return
        x, y, d = cx - radius, cy - radius, 2 * radius

        # Square-crop, resize to 400px and compress as JPEG to keep PDF small
        try:
            import io
            from PIL import Image
            img = Image.open(photo_path).convert("RGB")
            w, h = img.size
            size = min(w, h)
            img = img.crop(((w - size) // 2, (h - size) // 2,
                            (w + size) // 2, (h + size) // 2))
            img = img.resize((400, 400), Image.LANCZOS)
            buf = io.BytesIO()
            img.save(buf, format="JPEG", quality=85, optimize=True)
            buf.seek(0)
            self.image(buf, x=x, y=y, w=d, h=d)
        except Exception:
            self.image(photo_path, x=x, y=y, w=d, h=d)

        k = 0.5523 * radius
        _rgb(self, DARK, "fill")
        _rgb(self, DARK, "draw")
        self.set_line_width(0.1)

        # top-left
        with self.new_path(paint_rule="f") as p:
            p.move_to(x, y);  p.line_to(cx, y)
            p.curve_to(cx - k, y, x, cy - k, x, cy)
            p.close()
        # top-right
        with self.new_path(paint_rule="f") as p:
            p.move_to(cx, y);  p.line_to(x + d, y);  p.line_to(x + d, cy)
            p.curve_to(x + d, cy - k, cx + k, y, cx, y)
            p.close()
        # bottom-right
        with self.new_path(paint_rule="f") as p:
            p.move_to(x + d, cy);  p.line_to(x + d, y + d);  p.line_to(cx, y + d)
            p.curve_to(cx + k, y + d, x + d, cy + k, x + d, cy)
            p.close()
        # bottom-left
        with self.new_path(paint_rule="f") as p:
            p.move_to(cx, y + d);  p.line_to(x, y + d);  p.line_to(x, cy)
            p.curve_to(x, cy + k, cx - k, y + d, cx, y + d)
            p.close()

        # white circle border
        _rgb(self, WHITE, "draw")
        self.set_line_width(1.5)
        self.ellipse(x, y, d, d, "D")

    # ── Sidebar section title (white + amber underline) ──────────────────────
    def _sidebar_section(self, y, title):
        self.set_xy(S_MARGIN, y)
        self.set_font("Arial", "B", 10)
        _rgb(self, WHITE, "text")
        self.cell(S_CONT_W, 5.5, title, 0, 1)
        ly = self.get_y() + 0.5
        _rgb(self, AMBER, "draw")
        self.set_line_width(0.7)
        self.line(S_MARGIN, ly, S_MARGIN + 22, ly)
        return ly + 4

    # ── Main section title (dark + full-width divider) ────────────────────────
    def _main_section(self, y, title):
        inner_x = MAIN_X + M_MARGIN
        self.set_xy(inner_x, y)
        self.set_font("Arial", "", 11)
        _rgb(self, SECTION_COL, "text")
        self.multi_cell(M_CONT_W, 7, title, 0)
        ly = self.get_y()
        _rgb(self, DIVIDER_COL, "draw")
        self.set_line_width(0.3)
        self.line(inner_x, ly, inner_x + M_CONT_W, ly)
        return ly + 5

    # ── Full sidebar (page 1) ────────────────────────────────────────────────
    def draw_sidebar(self, photo_path, data):
        self._draw_sidebar_bg()

        radius = 27
        cx     = SIDEBAR_W / 2
        cy     = 12 + radius
        self._draw_circular_photo(photo_path, cx, cy, radius)

        y = cy + radius + 7

        # SOBRE MIM
        y = self._sidebar_section(y, data.get("sidebar_sobre", "SOBRE MIM"))
        bio = data.get("resumo_texto", "").strip().split("\n\n")[0].strip()
        self.set_xy(S_MARGIN, y)
        self.set_font("Arial", "", 7.5)
        _rgb(self, LIGHT_GRAY, "text")
        self.multi_cell(S_CONT_W, 4, bio)
        y = self.get_y() + 5

        # CONTATO
        y = self._sidebar_section(y, data.get("sidebar_contato", "CONTATO"))
        parts = [p.strip() for p in data.get("contato", "").split("|")]
        linkedin_url = data.get("linkedin_url", "")

        # Each entry: (text, link_url, font_size)
        kaggle_url  = data.get("kaggle_url", "")

        contact_rows = []
        for p in parts:
            if "@" in p:
                contact_rows.append((p, "", 8))
            elif p.startswith("+") or (p and p[0].isdigit()):
                contact_rows.append((p, "", 8))
            elif "LinkedIn" in p:
                contact_rows.append(("LinkedIn", linkedin_url, 8))
            elif "Kaggle" in p:
                contact_rows.append(("Kaggle", kaggle_url, 8))
            else:
                contact_rows.append((p, "", 8))

        for text, link, fsize in contact_rows:
            self.set_font("Arial", "", fsize)
            self.set_xy(S_MARGIN, y)
            _rgb(self, LIGHT_GRAY, "text")
            self.multi_cell(S_CONT_W, 4.5, text, link=link)
            y = self.get_y() + 0.5
        y += 4

        # PORTFÓLIO AUTORAL (destaque, logo apos CONTATO)
        if data.get("publicacoes_side"):
            y = self._sidebar_section(y, data.get("sidebar_publicacoes_side", "PORTFÓLIO AUTORAL"))
            self.set_font("Arial", "", 7.5)
            for item in data["publicacoes_side"]:
                self._bullet(S_MARGIN, y, S_CONT_W, 3.8, item,
                             text_color=LIGHT_GRAY, bullet_color=AMBER, sq=1.1)
                y = self.get_y()
            y += 4

        # COMPETENCIAS (o grupo em DEFERRED_COMPETENCIA_GROUPS continua na pagina 2)
        y = self._sidebar_section(y, data.get("sidebar_competencias", "COMPETENCIAS"))
        for grupo in data.get("competencias", []):
            if grupo["grupo"] in DEFERRED_COMPETENCIA_GROUPS:
                continue
            self.set_xy(S_MARGIN, y)
            self.set_font("Arial", "B", 7.5)
            _rgb(self, AMBER, "text")
            self.multi_cell(S_CONT_W, 4, grupo["grupo"])
            y = self.get_y() + 1
            self.set_font("Arial", "", 7.5)
            for item in grupo["itens"]:
                self._bullet(S_MARGIN, y, S_CONT_W, 3.8, item,
                             text_color=LIGHT_GRAY, bullet_color=AMBER, sq=1.1)
                y = self.get_y()
            y += 3

        self._draw_wave(data)

    # ── Continuation sidebar (page 2+) ───────────────────────────────────────
    def draw_sidebar_continuation(self, data=None, page=1):
        self._draw_sidebar_bg()

        if data:
            y = 12
            if page == 1:
                # COMPETENCIAS (continuacao) - grupo(s) que nao couberam na pagina 1
                deferred = [g for g in data.get("competencias", [])
                            if g["grupo"] in DEFERRED_COMPETENCIA_GROUPS]
                if deferred:
                    y = self._sidebar_section(y, data.get("sidebar_competencias", "COMPETENCIAS"))
                    for grupo in deferred:
                        self.set_xy(S_MARGIN, y)
                        self.set_font("Arial", "B", 7.5)
                        _rgb(self, AMBER, "text")
                        self.multi_cell(S_CONT_W, 4, grupo["grupo"])
                        y = self.get_y() + 1
                        self.set_font("Arial", "", 7.5)
                        for item in grupo["itens"]:
                            self._bullet(S_MARGIN, y, S_CONT_W, 3.8, item,
                                         text_color=LIGHT_GRAY, bullet_color=AMBER, sq=1.1)
                            y = self.get_y()
                        y += 3
                    y += 1
                # FORMAÇÃO COMPLEMENTAR
                if data.get("formacao_comp"):
                    y = self._sidebar_section(y, data.get("sidebar_formacao_comp", "FORMAÇÃO COMPL."))
                    self.set_font("Arial", "", 7.5)
                    for item in data["formacao_comp"]:
                        if y > PAGE_H - 60:
                            break
                        self._bullet(S_MARGIN, y, S_CONT_W, 3.8, item,
                                     text_color=LIGHT_GRAY, bullet_color=AMBER, sq=1.1)
                        y = self.get_y()
                    y += 4
                # INTERESSES
                if data.get("interesses") and y < PAGE_H - 55:
                    y = self._sidebar_section(y, data.get("sidebar_interesses", "INTERESSES"))
                    self.set_font("Arial", "", 7.5)
                    for item in data["interesses"]:
                        if y > PAGE_H - 38:
                            break
                        self._bullet(S_MARGIN, y, S_CONT_W, 3.8, item,
                                     text_color=LIGHT_GRAY, bullet_color=LIGHT_GRAY, sq=1.1)
                        y = self.get_y()
            else:
                # ATUAÇÃO COMUNITÁRIA
                if data.get("comunidade"):
                    y = self._sidebar_section(y, data.get("sidebar_comunidade", "COMUNIDADE"))
                    self.set_font("Arial", "", 7.5)
                    for item in data["comunidade"]:
                        if y > PAGE_H - 80:
                            break
                        self._bullet(S_MARGIN, y, S_CONT_W, 3.8, item,
                                     text_color=LIGHT_GRAY, bullet_color=AMBER, sq=1.1)
                        y = self.get_y()
                    y += 4
                # IDIOMAS
                if data.get("idiomas") and y < PAGE_H - 40:
                    y = self._sidebar_section(y, data.get("sidebar_idiomas", "IDIOMAS"))
                    self.set_font("Arial", "", 8)
                    for item in data["idiomas"]:
                        if y > PAGE_H - 20:
                            break
                        self._bullet(S_MARGIN, y, S_CONT_W, 4.5, item,
                                     text_color=LIGHT_GRAY, bullet_color=LIGHT_GRAY, sq=1.1)
                        y = self.get_y()

        self._draw_wave(data)

    # ── Dark header band on main side ────────────────────────────────────────
    def draw_main_header(self, data):
        _rgb(self, DARK, "fill")
        self.rect(MAIN_X, 0, MAIN_W, HEADER_H, "F")

        ix = MAIN_X + M_MARGIN
        iw = M_CONT_W

        # Name
        self.set_xy(ix, 10)
        self.set_font("Arial", "B", 19)
        _rgb(self, WHITE, "text")
        self.multi_cell(iw, 8, data["nome"])
        ny = self.get_y() + 1

        # Amber accent line
        _rgb(self, AMBER, "draw")
        self.set_line_width(2)
        self.line(ix, ny, ix + 38, ny)

        # Title
        self.set_xy(ix, ny + 4)
        self.set_font("Arial", "", 8.5)
        _rgb(self, LIGHT_GRAY, "text")
        self.multi_cell(iw, 4.5, data["titulo"])


# ── Public entry point ───────────────────────────────────────────────────────
def create_cv(filename, data, photo_path="data/linkedin/FotoLinkedin.png"):
    pdf = CV()
    pdf.set_auto_page_break(False)
    pdf.add_page()

    # ── Page 1 chrome ────────────────────────────────────────────────────────
    pdf.draw_sidebar(photo_path, data)
    pdf.draw_main_header(data)

    ix  = MAIN_X + M_MARGIN
    iw  = M_CONT_W
    y   = HEADER_H + 6

    continuation_page = [0]

    def check_page(needed=30):
        nonlocal y
        if y + needed > PAGE_H - 8:
            pdf.add_page()
            continuation_page[0] += 1
            pdf.draw_sidebar_continuation(data, page=continuation_page[0])
            y = 12

    # ── DESTAQUES ────────────────────────────────────────────────────────────
    y = pdf._main_section(y, data["destaques_titulo"])
    pdf.set_font("Arial", "", 8.5)
    for item in data["destaques"]:
        check_page(pdf._bullet_height(iw, 4.5, item) + 2)
        pdf._bullet(ix, y, iw, 4.5, item)
        y = pdf.get_y() + 1.5
    y += 4

    # ── PORTFÓLIO DE PROJETOS PESSOAIS ────────────────────────────────────────
    if data.get("publicacoes"):
        check_page(20)
        y = pdf._main_section(y, data["publicacoes_titulo"])
        pdf.set_font("Arial", "", 8.5)
        for item in data["publicacoes"]:
            check_page(pdf._bullet_height(iw, 4.5, item) + 2)
            pdf._bullet(ix, y, iw, 4.5, item)
            y = pdf.get_y() + 1.5
        y += 4

    # ── EXPERIENCIA (continua na pagina atual se houver espaco para o titulo
    #    e o primeiro bloco; senao comeca pagina nova) ─────────────────────────
    check_page(45)
    y = pdf._main_section(y, data["experiencia_titulo"])

    for exp in data["experiencia"]:
        check_page(25)

        # Company + period
        pdf.set_xy(ix, y)
        pdf.set_font("Arial", "B", 10)
        _rgb(pdf, SECTION_COL, "text")
        pdf.cell(iw * 0.65, 5.5, exp["empresa"], 0, 0)
        pdf.set_font("Arial", "", 9)
        _rgb(pdf, MID_GRAY, "text")
        pdf.cell(iw * 0.35, 5.5, exp["periodo"], 0, 1, "R")
        y = pdf.get_y()

        # Cargo
        pdf.set_xy(ix, y)
        pdf.set_font("Arial", "B", 8.5)
        _rgb(pdf, MID_GRAY, "text")
        pdf.multi_cell(iw, 4.5, exp["cargo"])
        y = pdf.get_y() + 1

        # Nota
        if exp.get("nota"):
            check_page(8)
            pdf.set_xy(ix, y)
            pdf.set_font("Arial", "I", 7.5)
            _rgb(pdf, MID_GRAY, "text")
            pdf.multi_cell(iw, 3.8, exp["nota"])
            y = pdf.get_y() + 1

        # Bullets
        pdf.set_font("Arial", "", 8.5)
        for detalhe in exp["detalhes"]:
            check_page(pdf._bullet_height(iw, 4.5, detalhe) + 2)
            pdf._bullet(ix, y, iw, 4.5, detalhe)
            y = pdf.get_y()
        y += 5

    # ── RESULTADOS VERIFICÁVEIS ───────────────────────────────────────────────
    if data.get("resultados"):
        check_page(20)
        y = pdf._main_section(y, data["resultados_titulo"])
        pdf.set_font("Arial", "", 8.5)
        for item in data["resultados"]:
            check_page(pdf._bullet_height(iw, 4.5, item) + 2)
            pdf._bullet(ix, y, iw, 4.5, item)
            y = pdf.get_y() + 1.5
        y += 4

    # ── FORMACAO ─────────────────────────────────────────────────────────────
    check_page(20)
    y = pdf._main_section(y, data["educacao_titulo"])
    for edu in data["educacao"]:
        check_page(12)
        pdf.set_xy(ix, y)
        pdf.set_font("Arial", "", 8.5)
        _rgb(pdf, BODY_COL, "text")
        pdf.multi_cell(iw, 4.5, edu)
        y = pdf.get_y() + 3

    y += 3

    # ── DEPOIMENTOS ──────────────────────────────────────────────────────────
    check_page(20)
    y = pdf._main_section(y, data["depoimentos_titulo"])

    for dep in data["depoimentos"]:
        check_page(18)
        pdf.set_xy(ix, y)
        pdf.set_font("Arial", "I", 8.5)
        _rgb(pdf, BODY_COL, "text")
        pdf.multi_cell(iw, 4.5, dep["texto"])
        y = pdf.get_y() + 1

        check_page(6)
        pdf.set_xy(ix, y)
        pdf.set_font("Arial", "B", 8.5)
        _rgb(pdf, AMBER, "text")
        pdf.cell(iw, 4.5, dep["autor"], 0, 1,
                 link=dep.get("link", ""))
        y = pdf.get_y() + 4

    pdf.output(filename)
