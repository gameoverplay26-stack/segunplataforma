# -*- coding: utf-8 -*-
"""
Genera los 4 decks de la Unidad 4 (Unidad-4-Clase-N-2026.pptx) a partir de
diseno-plataformas/unidad-04/04-diapositivas.md, que es la unica fuente de contenido.

Uso (desde diseno-plataformas/unidad-04/):  python scripts/build_decks.py
Requiere: pip install python-pptx

Formato del .md: ver el encabezado de 04-diapositivas.md.
Paleta y estilo heredados de diseno-plataformas/unidad-03/scripts/generar_diapositivas.py.
"""
import argparse
import os
import re
import sys

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.enum.dml import MSO_LINE_DASH_STYLE
from pptx.util import Inches, Pt

HERE = os.path.dirname(os.path.abspath(__file__))
UNIT_DIR = os.path.dirname(HERE)
SOURCE = os.path.join(UNIT_DIR, "04-diapositivas.md")

# --- Paleta (U3) ------------------------------------------------------------
NAVY = RGBColor(0x1F, 0x2A, 0x44)
TEAL = RGBColor(0x0D, 0x94, 0x88)
GREEN = RGBColor(0x16, 0xA3, 0x4A)
AMBER = RGBColor(0xD9, 0x77, 0x06)
RED = RGBColor(0xDC, 0x26, 0x26)
SLATE = RGBColor(0x1F, 0x29, 0x37)
MUTED = RGBColor(0x6B, 0x72, 0x80)
LIGHT_BG = RGBColor(0xF3, 0xF4, 0xF6)
ROW_ALT = RGBColor(0xE6, 0xF4, 0xF2)
CONTEXT = RGBColor(0x47, 0x55, 0x69)   # barras de contexto (validado con dataviz vs. TEAL)
GRID = RGBColor(0xE5, 0xE7, 0xEB)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
FONT = "Calibri"

SLIDE_W, SLIDE_H = Inches(13.333), Inches(7.5)
MARGIN = Inches(0.55)
HEADER_H = Inches(1.05)
BODY_TOP = Inches(1.35)
FOOTER_Y = Inches(7.08)
SOURCE_Y = Inches(6.70)
CALLOUT_H = Inches(0.5)
IMG_W = Inches(4.3)

KEYS = ("tipo", "kicker", "pregunta", "actividad", "imagen", "diagrama", "cronologia", "hitos", "video", "fuente")
CALLOUTS = (  # clave, etiqueta, color
    ("pregunta", "PREGUNTA", AMBER),
    ("actividad", "ACTIVIDAD", GREEN),
    ("video", "VIDEO", RED),
)


# --- Parser -----------------------------------------------------------------
def parse(path):
    decks, deck, slide, in_notes = [], None, None, False
    with open(path, encoding="utf-8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if line.startswith("# DECK "):
                parts = [p.strip() for p in line[len("# DECK "):].split("|")]
                deck = {"num": int(parts[0]), "title": parts[1], "subtitle": parts[2], "slides": []}
                decks.append(deck)
                slide, in_notes = None, False
                continue
            if deck is None:
                continue  # encabezado del documento
            m = re.match(r"^## (\d+) \| (.+)$", line)
            if m:
                slide = {"num": int(m.group(1)), "title": m.group(2).strip(), "bullets": [],
                         "table": [], "notes": []}
                deck["slides"].append(slide)
                in_notes = False
                continue
            if slide is None:
                continue
            if in_notes:
                if line.strip():
                    slide["notes"].append(line.strip())
                continue
            if line.strip() == "notas:":
                in_notes = True
                continue
            km = re.match(r"^(%s): (.*)$" % "|".join(KEYS), line)
            if km:
                slide[km.group(1)] = km.group(2).strip()
            elif line.startswith("- "):
                slide["bullets"].append(line[2:].strip())
            elif line.startswith("|"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                    slide["table"].append(cells)
    return decks


# --- Helpers de dibujo ------------------------------------------------------
def rect(slide, x, y, w, h, color, shape=MSO_SHAPE.RECTANGLE):
    s = slide.shapes.add_shape(shape, x, y, w, h)
    s.fill.solid()
    s.fill.fore_color.rgb = color
    s.line.fill.background()
    s.shadow.inherit = False
    return s


def textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    return tf


def run(paragraph, text, size, color=SLATE, bold=False, italic=False):
    r = paragraph.add_run()
    r.text = text
    r.font.size = Pt(size)
    r.font.color.rgb = color
    r.font.bold = bold
    r.font.italic = italic
    r.font.name = FONT
    return r


def header(slide, s, total):
    rect(slide, 0, 0, SLIDE_W, HEADER_H, NAVY)
    rect(slide, 0, HEADER_H, SLIDE_W, Pt(3), TEAL)
    circ = rect(slide, Inches(0.3), Inches(0.24), Inches(0.58), Inches(0.58), TEAL, MSO_SHAPE.OVAL)
    tf = circ.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run(p, str(s["num"]), 16, WHITE, bold=True)
    tf = textbox(slide, Inches(1.1), Inches(0.12), SLIDE_W - Inches(1.6), Inches(0.85), MSO_ANCHOR.MIDDLE)
    if s.get("kicker"):
        run(tf.paragraphs[0], s["kicker"].upper(), 11, RGBColor(0x99, 0xF6, 0xE4), bold=True)
        p = tf.add_paragraph()
    else:
        p = tf.paragraphs[0]
    run(p, s["title"], 26, WHITE, bold=True)


def footer(slide, deck, s, total):
    tf = textbox(slide, MARGIN, FOOTER_Y, SLIDE_W - 2 * MARGIN, Inches(0.3), MSO_ANCHOR.MIDDLE)
    p = tf.paragraphs[0]
    run(p, "Diseño según Plataformas de Juego · Unidad IV · Clase %d · %s" % (deck["num"], deck["title"]), 10, MUTED)
    tf2 = textbox(slide, SLIDE_W - MARGIN - Inches(1), FOOTER_Y, Inches(1), Inches(0.3), MSO_ANCHOR.MIDDLE)
    p2 = tf2.paragraphs[0]
    p2.alignment = PP_ALIGN.RIGHT
    run(p2, "%d/%d" % (s["num"], total), 10, MUTED)


def bullets(slide, items, x, y, w, h):
    n = len(items)
    longest = max((len(b) for b in items), default=0)
    size = 22 if n <= 4 and longest < 70 else 20 if n <= 5 else 18
    if h < Inches(2.2):
        size = min(size, 16)
    tf = textbox(slide, x, y, w, h)
    for i, b in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(8)
        run(p, "■  ", size - 6, TEAL, bold=True)
        run(p, b, size)


def table(slide, rows, x, y, w, h):
    nrows, ncols = len(rows), max(len(r) for r in rows)
    longest = max(len(c) for r in rows for c in r)
    size = 16 if nrows <= 4 and longest < 60 else 14 if nrows <= 6 else 12
    row_h = min(Inches(0.62), int(h / nrows))
    shape = slide.shapes.add_table(nrows, ncols, x, y, w, row_h * nrows)
    tbl = shape.table
    for ci in range(ncols):  # columnas proporcionales al texto mas largo
        lens = [len(r[ci]) if ci < len(r) else 0 for r in rows]
        tbl.columns[ci].width = int(w * (max(lens) + 6) / sum(max(len(r[c]) if c < len(r) else 0 for r in rows) + 6 for c in range(ncols)))
    for ri, r in enumerate(rows):
        for ci in range(ncols):
            cell = tbl.cell(ri, ci)
            cell.margin_left = cell.margin_right = Inches(0.08)
            cell.margin_top = cell.margin_bottom = Inches(0.04)
            cell.fill.solid()
            cell.fill.fore_color.rgb = TEAL if ri == 0 else (ROW_ALT if ri % 2 == 0 else WHITE)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            p = cell.text_frame.paragraphs[0]
            cell.text_frame.word_wrap = True
            text = r[ci] if ci < len(r) else ""
            run(p, text, size, WHITE if ri == 0 else SLATE, bold=(ri == 0))


def image_placeholder(slide, text, x, y, w, h):
    box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    box.fill.solid()
    box.fill.fore_color.rgb = LIGHT_BG
    box.line.color.rgb = MUTED
    box.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    box.shadow.inherit = False
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = Inches(0.2)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run(p, "[IMAGEN SUGERIDA]", 13, MUTED, bold=True)
    p2 = tf.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    run(p2, text, 13, MUTED, italic=True)


def layer_diagram(slide, spec, x, y, w, h):
    """Diagrama de capas apiladas con flechas.
    Sintaxis en el .md:  diagrama: Capa: chip, chip | Capa: chip, chip | ... [|| nota al pie]
    """
    spec, _, footnote = spec.partition("||")
    layers = []
    for part in spec.split("|"):
        name, _, chips = part.partition(":")
        layers.append((name.strip(), [c.strip() for c in chips.split(",") if c.strip()]))
    colors = [TEAL, AMBER, NAVY, GREEN, RED]
    foot_h = Inches(0.45) if footnote.strip() else 0
    n = len(layers)
    arrow_h = Inches(0.42)
    box_h = int((h - foot_h - arrow_h * (n - 1)) / n)
    cy = y
    for i, (name, chips) in enumerate(layers):
        color = colors[i % len(colors)]
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, cy, w, box_h)
        box.adjustments[0] = 0.12
        box.fill.solid()
        box.fill.fore_color.rgb = LIGHT_BG
        box.line.color.rgb = color
        box.line.width = Pt(2)
        box.shadow.inherit = False
        tf = textbox(slide, x + Inches(0.2), cy + Inches(0.1), w - Inches(0.4), Inches(0.4))
        run(tf.paragraphs[0], name.upper(), 15, color, bold=True)
        if chips:  # chips en una fila
            gap = Inches(0.15)
            cw = int((w - Inches(0.4) - gap * (len(chips) - 1)) / len(chips))
            ch = min(Inches(0.55), box_h - Inches(0.65))
            for j, c in enumerate(chips):
                chip = rect(slide, x + Inches(0.2) + j * (cw + gap), cy + box_h - ch - Inches(0.15), cw, ch,
                            color, MSO_SHAPE.ROUNDED_RECTANGLE)
                ctf = chip.text_frame
                ctf.word_wrap = True
                ctf.vertical_anchor = MSO_ANCHOR.MIDDLE
                ctf.margin_left = ctf.margin_right = Inches(0.05)
                cp = ctf.paragraphs[0]
                cp.alignment = PP_ALIGN.CENTER
                run(cp, c, 14, WHITE, bold=True)
        cy += box_h
        if i < n - 1:
            arr = rect(slide, x + w / 2 - Inches(0.25), cy + Inches(0.04), Inches(0.5), arrow_h - Inches(0.08),
                       MUTED, MSO_SHAPE.DOWN_ARROW)
            cy += arrow_h
    if footnote.strip():
        tf = textbox(slide, x, cy + Inches(0.1), w, foot_h - Inches(0.1), MSO_ANCHOR.MIDDLE)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run(p, footnote.strip(), 13, RED, italic=True)


def timeline_chart(slide, spec, x, y, w, h, end_year=2026):
    """Cronologia de barras: cada barra va del anio del hito hasta end_year.
    Sintaxis:  cronologia: Etiqueta: 1972 | *Destacada: 2008 | ... [|| nota]
    Un '*' inicial destaca la barra (TEAL + rotulo en negrita); el resto va en gris de contexto.
    """
    spec, _, footnote = spec.partition("||")
    rows = []
    for part in spec.split("|"):
        label, _, year = part.rpartition(":")
        hi = label.strip().startswith("*")
        rows.append((label.strip().lstrip("*").strip(), int(year), hi))
    start = (min(r[1] for r in rows) // 10) * 10
    label_w = Inches(2.35)
    axis_h = Inches(0.35)
    foot_h = Inches(0.4) if footnote.strip() else 0
    plot_x, plot_w = x + label_w, w - label_w - Inches(0.1)
    plot_h = h - axis_h - foot_h
    def xpos(year):
        return plot_x + int(plot_w * (year - start) / (end_year - start))
    # grilla y eje (recesivos)
    for yr in range(start, end_year + 1, 10):
        gx = xpos(yr)
        rect(slide, gx, y, Pt(1), plot_h, GRID)
        tf = textbox(slide, gx - Inches(0.4), y + plot_h + Inches(0.05), Inches(0.8), Inches(0.3))
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run(p, str(yr), 11, MUTED)
    row_h = plot_h / len(rows)
    bar_h = int(row_h - Pt(6))  # separacion entre barras
    for i, (label, year, hi) in enumerate(rows):
        ry = y + int(i * row_h) + Pt(3)
        tf = textbox(slide, x, ry, label_w - Inches(0.15), bar_h, MSO_ANCHOR.MIDDLE)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.RIGHT
        run(p, label, 14, SLATE, bold=hi)
        bx = xpos(year)
        bar = rect(slide, bx, ry, xpos(end_year) - bx, bar_h, TEAL if hi else CONTEXT, MSO_SHAPE.ROUNDED_RECTANGLE)
        bar.adjustments[0] = 0.15
        if xpos(end_year) - bx >= Inches(0.75):  # el anio entra dentro de la barra
            btf = bar.text_frame
            btf.word_wrap = False
            btf.margin_left = Inches(0.08)
            btf.vertical_anchor = MSO_ANCHOR.MIDDLE
            bp = btf.paragraphs[0]
            bp.alignment = PP_ALIGN.LEFT
            run(bp, str(year), 13, WHITE, bold=True)
        else:  # barra angosta: el anio va afuera, a la izquierda, en color de texto
            ytf = textbox(slide, bx - Inches(0.75), ry, Inches(0.68), bar_h, MSO_ANCHOR.MIDDLE)
            yp = ytf.paragraphs[0]
            yp.alignment = PP_ALIGN.RIGHT
            run(yp, str(year), 13, SLATE, bold=True)
    if footnote.strip():
        tf = textbox(slide, x, y + plot_h + axis_h + Inches(0.05), w, foot_h - Inches(0.05), MSO_ANCHOR.MIDDLE)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.RIGHT
        run(p, footnote.strip(), 11, MUTED, italic=True)


def milestones_chart(slide, spec, x, y, w, h):
    """Linea de tiempo de hitos en orden cronologico, con rotulos alternados arriba/abajo.
    Sintaxis:  hitos: 1972 · Nombre · aporte | 1978 · Nombre · aporte | ...
    Los hitos van equiespaciados (escala ordinal): cada tarjeta muestra su anio y una
    leyenda aclara que la separacion no es proporcional al tiempo. Asi no hay cruces
    cuando varios hitos caen en anios cercanos o en el mismo anio.
    """
    items = []
    for part in spec.split("|"):
        f = [t.strip() for t in part.split("·")]
        items.append((int(f[0]), f[1], f[2] if len(f) > 2 else ""))
    n = len(items)
    caption_h = Inches(0.3)
    lab_w = min(Inches(2.2), int(2 * w / (n + 1)) - Inches(0.15))
    lab_h, stem = Inches(0.85), Inches(0.35)
    ax_x0, ax_x1 = x + lab_w / 2, x + w - lab_w / 2
    axis_y = y + int((h - caption_h) / 2)
    step = (ax_x1 - ax_x0) / (n - 1) if n > 1 else 0
    rect(slide, int(ax_x0 - Inches(0.2)), axis_y - Pt(1.5), int(ax_x1 - ax_x0 + Inches(0.4)), Pt(3), MUTED)
    for i, (yr, name, contrib) in enumerate(items):
        cx = int(ax_x0 + i * step)
        up = i % 2 == 0
        ly = axis_y - stem - lab_h if up else axis_y + stem
        rect(slide, cx - Pt(0.75), axis_y - stem if up else axis_y, Pt(1.5), stem, MUTED)
        rect(slide, cx - Inches(0.1), axis_y - Inches(0.1), Inches(0.2), Inches(0.2), NAVY, MSO_SHAPE.OVAL)
        box = rect(slide, int(cx - lab_w / 2), ly, lab_w, lab_h, LIGHT_BG, MSO_SHAPE.ROUNDED_RECTANGLE)
        box.adjustments[0] = 0.1
        tf = box.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = tf.margin_right = Inches(0.06)
        tf.margin_top = tf.margin_bottom = Inches(0.02)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run(p, str(yr) + "  ", 12, TEAL, bold=True)
        run(p, name, 12, SLATE, bold=True)
        if contrib:
            p2 = tf.add_paragraph()
            p2.alignment = PP_ALIGN.CENTER
            run(p2, contrib, 11, MUTED)
    tf = textbox(slide, x, y + h - caption_h, w, caption_h, MSO_ANCHOR.MIDDLE)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    run(p, "Orden cronológico: la separación entre hitos no es proporcional al tiempo", 11, MUTED, italic=True)

def callout(slide, label, text, color, y):
    rect(slide, MARGIN, y, Inches(0.12), CALLOUT_H, color)
    bg = rect(slide, MARGIN + Inches(0.12), y, SLIDE_W - 2 * MARGIN - Inches(0.12), CALLOUT_H, LIGHT_BG)
    tf = bg.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = Inches(0.15)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    run(p, label + "  ", 13, color, bold=True)
    run(p, text, 14 if len(text) < 120 else 12)


# --- Layouts ----------------------------------------------------------------
def build_cover(prs, deck, s, total):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = NAVY
    rect(slide, 0, Inches(5.2), SLIDE_W, Pt(4), TEAL)
    has_img = bool(s.get("imagen"))
    w = SLIDE_W - 2 * MARGIN - (IMG_W + Inches(0.3) if has_img else 0)
    tf = textbox(slide, MARGIN, Inches(1.4), w, Inches(3.6), MSO_ANCHOR.BOTTOM)
    run(tf.paragraphs[0], s.get("kicker", "").upper(), 14, RGBColor(0x99, 0xF6, 0xE4), bold=True)
    p = tf.add_paragraph()
    run(p, s["title"], 40, WHITE, bold=True)
    for b in s["bullets"]:
        p = tf.add_paragraph()
        p.space_before = Pt(6)
        run(p, b, 20, RGBColor(0xCB, 0xD5, 0xE1))
    if has_img:
        image_placeholder(slide, s["imagen"], SLIDE_W - MARGIN - IMG_W, Inches(1.3), IMG_W, Inches(3.6))
    tf = textbox(slide, MARGIN, Inches(6.6), SLIDE_W - 2 * MARGIN, Inches(0.4))
    run(tf.paragraphs[0], "%s · %d/%d" % (deck["subtitle"], s["num"], total), 12, RGBColor(0xCB, 0xD5, 0xE1))
    return slide


def build_content(prs, deck, s, total):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = WHITE
    header(slide, s, total)
    footer(slide, deck, s, total)

    # pie: fuente + callouts apilados desde abajo
    bottom = SOURCE_Y
    if s.get("fuente"):
        tf = textbox(slide, MARGIN, SOURCE_Y, SLIDE_W - 2 * MARGIN, Inches(0.32), MSO_ANCHOR.MIDDLE)
        run(tf.paragraphs[0], "Fuente: ", 10, MUTED, bold=True)
        run(tf.paragraphs[0], s["fuente"], 10, MUTED)
    for key, label, color in reversed(CALLOUTS):
        if s.get(key):
            bottom -= CALLOUT_H + Inches(0.1)
            callout(slide, label, s[key], color, bottom)
    body_h = bottom - BODY_TOP - Inches(0.15)

    has_chart = bool(s.get("cronologia"))
    has_diag = bool(s.get("diagrama"))
    has_img = bool(s.get("imagen")) and not (has_diag or has_chart)
    panel_w = Inches(7.4) if has_chart else Inches(5.6) if has_diag else IMG_W
    body_w = SLIDE_W - 2 * MARGIN - (panel_w + Inches(0.3) if (has_img or has_diag or has_chart) else 0)
    if s.get("hitos"):  # ocupa todo el ancho del cuerpo
        milestones_chart(slide, s["hitos"], MARGIN, BODY_TOP, SLIDE_W - 2 * MARGIN, body_h)
        return slide
    if has_chart:
        timeline_chart(slide, s["cronologia"], SLIDE_W - MARGIN - panel_w, BODY_TOP, panel_w, body_h)
    elif has_diag:
        layer_diagram(slide, s["diagrama"], SLIDE_W - MARGIN - panel_w, BODY_TOP, panel_w, body_h)
    elif has_img:
        image_placeholder(slide, s["imagen"], SLIDE_W - MARGIN - IMG_W, BODY_TOP, IMG_W, body_h)

    y = BODY_TOP
    if s["bullets"] and s["table"]:
        bh = Inches(0.55) * len(s["bullets"]) + Inches(0.1)
        bullets(slide, s["bullets"], MARGIN, y, body_w, bh)
        y += bh
        table(slide, s["table"], MARGIN, y, body_w, body_h - bh)
    elif s["table"]:
        table(slide, s["table"], MARGIN, y, body_w, body_h)
    elif s["bullets"]:
        bullets(slide, s["bullets"], MARGIN, y, body_w, body_h)
    return slide


def add_notes(slide, notes):
    if notes:
        slide.notes_slide.notes_text_frame.text = "\n".join(notes)


def build(decks, only=None, version=None, out_dir=UNIT_DIR):
    out = []
    for deck in decks:
        if only and deck["num"] not in only:
            continue
        prs = Presentation()
        prs.slide_width, prs.slide_height = SLIDE_W, SLIDE_H
        total = len(deck["slides"])
        for s in deck["slides"]:
            maker = build_cover if s.get("tipo") == "portada" else build_content
            add_notes(maker(prs, deck, s, total), s["notes"])
        suffix = "-v%d" % version if version and version > 1 else ""
        path = os.path.join(out_dir, "Unidad-4-Clase-%d-2026%s.pptx" % (deck["num"], suffix))
        prs.save(path)
        out.append((path, total))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Genera los decks de la Unidad 4.")
    ap.add_argument("--decks", type=int, nargs="+", help="numeros de deck a generar (por defecto, todos)")
    ap.add_argument("--version", type=int, help="agrega el sufijo -vN al nombre del archivo (N > 1)")
    ap.add_argument("--out-dir", default=UNIT_DIR, help="carpeta de salida (por defecto, la de la unidad)")
    args = ap.parse_args()
    decks = parse(SOURCE)
    if len(decks) != 4:
        sys.exit("Se esperaban 4 decks y se encontraron %d" % len(decks))
    for path, total in build(decks, args.decks, args.version, args.out_dir):
        print("OK  %-40s %2d slides" % (os.path.basename(path), total))
