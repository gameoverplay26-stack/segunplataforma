# -*- coding: utf-8 -*-
"""
Genera los 3 decks de la Unidad 4 (Unidad-4-Clase-N-2026.pptx) a partir de
diseno-plataformas/unidad-04/04-diapositivas.md, que es la unica fuente de contenido.

Uso (desde diseno-plataformas/unidad-04/):  python scripts/build_decks.py
Requiere: pip install python-pptx

Formato del .md: ver el encabezado de 04-diapositivas.md.
Paleta y estilo heredados de diseno-plataformas/unidad-03/scripts/generar_diapositivas.py.
"""
import argparse
import os
import re
import subprocess
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

KEYS = ("tipo", "kicker", "pregunta", "actividad", "imagen", "diagrama", "cronologia", "hitos", "flujo", "comparacion", "tiles", "codigo2", "codigo", "vista", "safearea", "captura", "ajustes", "tarjetas", "panel", "video", "movil", "fuente")
CALLOUTS = (  # clave, etiqueta, color
    ("movil", "PARA MÓVIL", TEAL),
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
            sm = re.match(r"^subtabla: (.*)$", line)
            if sm:  # varias tablas con título, lado a lado
                slide.setdefault("subtablas", []).append({"titulo": sm.group(1).strip(), "rows": []})
            elif km:
                slide[km.group(1)] = km.group(2).strip()
            elif line.startswith("- "):
                slide["bullets"].append(line[2:].strip())
            elif line.startswith("|"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                    (slide["subtablas"][-1]["rows"] if slide.get("subtablas") else slide["table"]).append(cells)
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


def kicker_text(kicker):
    """Kicker visible sin la duración: los minutos quedan en la fuente, las notas y el guion."""
    parts = [p.strip() for p in kicker.split("·")]
    return " · ".join(p for p in parts if not re.match(r"^\d+\s*MIN\b", p, re.IGNORECASE))


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
        run(tf.paragraphs[0], kicker_text(s["kicker"]).upper(), 11, RGBColor(0x99, 0xF6, 0xE4), bold=True)
        p = tf.add_paragraph()
    else:
        p = tf.paragraphs[0]
    run(p, s["title"], 26, WHITE, bold=True)


def footer(slide, deck, s, total):
    tf = textbox(slide, MARGIN, FOOTER_Y, SLIDE_W - 2 * MARGIN, Inches(0.3), MSO_ANCHOR.MIDDLE)
    p = tf.paragraphs[0]
    where = "Anexo" if deck["title"].startswith("Anexo") else "Clase %d" % deck["num"]
    run(p, "Diseño según Plataformas de Juego · Unidad IV · %s · %s" % (where, deck["title"]), 10, MUTED)
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
        m = re.match(r"(\d+)\. (.*)", b)
        if m:  # paso numerado
            run(p, m.group(1) + "  ", size, TEAL, bold=True)
            run(p, m.group(2), size)
        else:
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

def flow_diagram(slide, spec, x, y, w, h):
    """Cadena vertical de pasos con flechas. Sintaxis: flujo: Paso | Paso | Paso [|| nota]"""
    spec, _, footnote = spec.partition("||")
    steps = [t.strip() for t in spec.split("|") if t.strip()]
    n = len(steps)
    foot_h = Inches(0.45) if footnote.strip() else 0
    arrow_h = Inches(0.38)
    box_h = min(Inches(0.75), int((h - foot_h - arrow_h * (n - 1)) / n))
    total = box_h * n + arrow_h * (n - 1)
    cy = y + int((h - foot_h - total) / 2)
    colors = [TEAL, AMBER, RED, NAVY]
    for i, st in enumerate(steps):
        color = colors[min(i, len(colors) - 1)] if n <= 4 else TEAL
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, cy, w, box_h)
        box.adjustments[0] = 0.2
        box.fill.solid()
        box.fill.fore_color.rgb = LIGHT_BG
        box.line.color.rgb = color
        box.line.width = Pt(2)
        box.shadow.inherit = False
        tf = box.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run(p, st, 17, SLATE, bold=True)
        cy += box_h
        if i < n - 1:
            rect(slide, int(x + w / 2 - Inches(0.22)), cy + Inches(0.04), Inches(0.44), arrow_h - Inches(0.08), MUTED, MSO_SHAPE.DOWN_ARROW)
            cy += arrow_h
    if footnote.strip():
        tf = textbox(slide, x, cy + Inches(0.1), w, foot_h - Inches(0.1), MSO_ANCHOR.MIDDLE)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run(p, footnote.strip(), 13, MUTED, italic=True)


def compare_diagram(slide, spec, x, y, w, h):
    """Dos columnas comparadas. Sintaxis:
    comparacion: Titulo: chip, chip // nota | Titulo: chip, chip // nota
    En la columna cuyo titulo empieza con '+' los chips van juntos dentro de un mismo bloque (un chip)."""
    cols = []
    for part in spec.split("|"):
        head, _, note = part.partition("//")
        title, _, chips = head.partition(":")
        together = title.strip().startswith("+")
        small = title.strip().startswith("-")  # '-' = dibujar los chips a la mitad de tamanio
        cols.append((title.strip().lstrip("+-").strip(), [c.strip() for c in chips.split(",") if c.strip()], note.strip(), together, small))
    gap = Inches(0.3)
    cw = int((w - gap * (len(cols) - 1)) / len(cols))
    colors = [TEAL, NAVY]
    for ci, (title, chips, note, together, small) in enumerate(cols):
        cx = x + ci * (cw + gap)
        color = colors[ci % 2]
        tf = textbox(slide, cx, y, cw, Inches(0.45), MSO_ANCHOR.MIDDLE)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run(p, title.upper(), 16, color, bold=True)
        top = y + Inches(0.55)
        note_h = Inches(0.8)
        area_h = h - Inches(0.55) - note_h
        chip_h = Inches(0.55)
        if together:
            frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, top, cw, area_h)
            frame.adjustments[0] = 0.08
            frame.fill.solid()
            frame.fill.fore_color.rgb = LIGHT_BG
            frame.line.color.rgb = color
            frame.line.width = Pt(2.5)
            frame.shadow.inherit = False
            inner_gap = Inches(0.08)
            total = chip_h * len(chips) + inner_gap * (len(chips) - 1)
            cy = top + int((area_h - total) / 2)
        else:
            inner_gap = Inches(0.35)
            total = chip_h * len(chips) + inner_gap * (len(chips) - 1)
            cy = top + int((area_h - total) / 2)
        for c in chips:
            full_w = cw - Inches(0.6)
            bw, bh = (int(full_w * 0.5), int(chip_h * 0.5)) if small else (full_w, chip_h)
            chip = rect(slide, cx + Inches(0.3) + int((full_w - bw) / 2), cy + int((chip_h - bh) / 2), bw, bh, color, MSO_SHAPE.ROUNDED_RECTANGLE)
            ctf = chip.text_frame
            ctf.vertical_anchor = MSO_ANCHOR.MIDDLE
            ctf.margin_left = ctf.margin_right = ctf.margin_top = ctf.margin_bottom = 0
            cp = ctf.paragraphs[0]
            cp.alignment = PP_ALIGN.CENTER
            run(cp, c, 9 if small else 15, WHITE, bold=True)
            cy += chip_h + inner_gap
        if note:
            tf = textbox(slide, cx, top + area_h + Inches(0.1), cw, note_h - Inches(0.1), MSO_ANCHOR.TOP)
            p = tf.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            run(p, note, 14, SLATE)


def tiles_diagram(slide, spec, x, y, w, h):
    """Pantalla dividida en tiles con un tile ampliado (overdraw).
    Sintaxis: tiles: columnas x filas | rotulo del tile | rotulo de la ampliacion"""
    parts = [t.strip() for t in spec.split("|")]
    cols, rows = [int(v) for v in parts[0].lower().split("x")]
    tile_label = parts[1] if len(parts) > 1 else "1 tile"
    zoom_label = parts[2] if len(parts) > 2 else ""
    phone_h = h - Inches(0.2)
    phone_w = int(phone_h * 0.5)
    px, py = x + Inches(0.1), y + Inches(0.1)
    body = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, py, phone_w, phone_h)
    body.adjustments[0] = 0.08
    body.fill.solid()
    body.fill.fore_color.rgb = NAVY
    body.line.fill.background()
    body.shadow.inherit = False
    m = Inches(0.12)
    sx, sy, sw, sh = px + m, py + m * 2, phone_w - 2 * m, phone_h - 4 * m
    tw, th = sw / cols, sh / rows
    hi = (1, 2)  # columna, fila del tile destacado
    for r in range(rows):
        for c in range(cols):
            t = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, int(sx + c * tw), int(sy + r * th), int(tw), int(th))
            t.fill.solid()
            t.fill.fore_color.rgb = TEAL if (c, r) == hi else WHITE
            t.line.color.rgb = GRID
            t.line.width = Pt(1)
            t.shadow.inherit = False
    hx, hy = int(sx + hi[0] * tw + tw), int(sy + hi[1] * th + th / 2)
    # ampliacion del tile: tres capas superpuestas
    zx = px + phone_w + Inches(0.9)
    zs = Inches(1.4)
    zy = y + Inches(0.6)
    rect(slide, hx, hy - Pt(1), zx - hx - Inches(0.1), Pt(2), MUTED)
    shades = [RGBColor(0xCC, 0xFB, 0xF1), RGBColor(0x5E, 0xEA, 0xD4), TEAL]
    for k, shade in enumerate(shades):
        sq = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, zx + k * Inches(0.3), zy + k * Inches(0.3), zs, zs)
        sq.fill.solid()
        sq.fill.fore_color.rgb = shade
        sq.line.color.rgb = WHITE
        sq.line.width = Pt(2)
        sq.shadow.inherit = False
    tf = textbox(slide, zx - Inches(0.2), zy - Inches(0.5), Inches(2.6), Inches(0.4), MSO_ANCHOR.MIDDLE)
    run(tf.paragraphs[0], tile_label, 15, SLATE, bold=True)
    if zoom_label:
        tf = textbox(slide, zx - Inches(0.2), zy + zs + Inches(0.75), x + w - zx + Inches(0.2), Inches(1.2))
        run(tf.paragraphs[0], zoom_label, 15, SLATE)


def load_code(spec):
    """Lee las líneas pedidas (archivo actual o 'git:REV:ruta'). Devuelve
    (ruta, rev, rangos, líneas numeradas con None para '⋯', líneas, sangría común)."""
    rev = None
    if spec.startswith("git:"):
        rev, _, spec = spec[4:].partition(":")
    path, _, rng = spec.rpartition(":")
    # Uno o varios rangos ("61-63,66-68"): entre rangos se dibuja una línea "⋯".
    ranges = [[int(v) for v in r.split("-")] if "-" in r else [int(r), int(r)] for r in rng.split(",")]
    full = os.path.normpath(os.path.join(UNIT_DIR, path))
    if rev:
        root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], cwd=UNIT_DIR, text=True).strip()
        rel = os.path.relpath(full, root).replace(os.sep, "/")
        text = subprocess.check_output(["git", "show", "%s:%s" % (rev, rel)], cwd=root).decode("utf-8-sig")
    else:
        with open(full, encoding="utf-8-sig") as fh:
            text = fh.read()
    all_lines = text.splitlines()
    numbered = []  # (número de línea o None para "⋯", texto)
    for i, (ra, rb) in enumerate(ranges):
        if i:
            numbered.append((None, "⋯"))
        numbered += [(n, all_lines[n - 1]) for n in range(ra, rb + 1)]
    lines = [t for n, t in numbered if n is not None]
    indent = min((len(l) - len(l.lstrip()) for l in lines if l.strip()), default=0)
    return path, rev, ranges, numbered, lines, indent


def code_width_need(spec):
    """Largo (en caracteres) de la línea más larga de un bloque, para repartir el ancho."""
    spec = spec.partition("##")[0].partition("@")[0].strip()
    _, _, _, _, lines, indent = load_code(spec)
    return max((len(l) - indent for l in lines), default=20) + 6


def code_block(slide, spec, x, y, w, h):
    """Bloque de codigo leido del archivo real. Sintaxis: codigo: ruta/relativa/a/la/unidad.cs:61-73
    o, para una version anterior guardada en git: codigo: git:REV:ruta/relativa/a/la/unidad.cs:61-73
    Resalta en ambar las lineas que contienen 'Input.', o el texto indicado al final con '@texto'.
    Lo que sigue a '##' es la explicación en palabras simples: 'línea: qué hace ; línea: qué hace'."""
    rev = None
    spec, _, explain = spec.partition("##")
    items = [i.strip().partition(":") for i in explain.split(";") if i.strip()]
    if items:
        exp_h = Inches(0.5) + Inches(0.3) * len(items)
        explain_box(slide, items, x, y + h - exp_h, w, exp_h)
        h -= exp_h + Inches(0.12)
    spec, _, hot_text = spec.partition("@")
    hot_text = hot_text.strip() or "Input."
    path, rev, ranges, numbered, lines, indent = load_code(spec)
    a, b = ranges[0][0], ranges[-1][1]
    title_h = Inches(0.35)
    tf = textbox(slide, x, y, w, title_h, MSO_ANCHOR.MIDDLE)
    label = os.path.basename(path) + "  ·  líneas %d–%d" % (a, b) + ("  ·  extracto" if len(ranges) > 1 else "")
    if rev:
        label += "  ·  versión original"
    run(tf.paragraphs[0], label, 12, MUTED, bold=True)
    box = rect(slide, x, y + title_h + Inches(0.05), w, h - title_h - Inches(0.05), RGBColor(0x0F, 0x17, 0x2A), MSO_SHAPE.ROUNDED_RECTANGLE)
    box.adjustments[0] = 0.04
    tf = box.text_frame
    tf.word_wrap = False
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = Inches(0.25)
    longest = max((len(l) - indent for l in lines), default=0)
    fit = int((w - Inches(0.45)) / 12700 / (0.56 * (longest + 5)))  # Consolas: ~0,55 em por caracter
    box_pt = (h - title_h - Inches(0.05)) / 12700
    fit_h = int((box_pt - 24) / (1.2 * len(numbered)))  # que todas las líneas entren en el alto
    size = max(9, min(15 if len(numbered) <= 16 else 12, fit, fit_h))
    for i, (num, line) in enumerate(numbered):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        r = run(p, "%3s  " % (num if num is not None else ""), size, RGBColor(0x64, 0x74, 0x8B))
        r.font.name = "Consolas"
        if num is None:
            r2 = run(p, line, size, RGBColor(0x64, 0x74, 0x8B))
            r2.font.name = "Consolas"
            continue
        hot = hot_text in line
        r2 = run(p, line[indent:] if line.strip() else " ", size, AMBER if hot else RGBColor(0xE2, 0xE8, 0xF0), bold=hot)
        r2.font.name = "Consolas"


def explain_box(slide, items, x, y, w, h):
    """Recuadro 'En palabras simples' con una línea por parte del código."""
    box = rect(slide, x, y, w, h, LIGHT_BG, MSO_SHAPE.ROUNDED_RECTANGLE)
    box.adjustments[0] = 0.06
    tf = textbox(slide, x + Inches(0.18), y + Inches(0.1), w - Inches(0.36), h - Inches(0.2))
    run(tf.paragraphs[0], "EN PALABRAS SIMPLES", 11, TEAL, bold=True)
    for ref, _, text in items:
        p = tf.add_paragraph()
        p.space_before = Pt(3)
        if text:
            run(p, "Línea %s  " % ref.strip(), 13, TEAL, bold=True)
            run(p, text.strip(), 13, SLATE)
        else:
            run(p, ref.strip(), 13, SLATE)


def code_columns(slide, spec, x, y, w, h):
    """Dos bloques de código lado a lado: antes / después.
    Sintaxis: codigo2: ETIQUETA IZQ = spec || ETIQUETA DER = spec
    (cada spec como en 'codigo:', con '@texto' opcional para elegir qué líneas se resaltan)."""
    parts = [p.strip() for p in spec.split("||")]
    gap = Inches(0.35)
    avail = w - gap * (len(parts) - 1)
    need = [code_width_need(part.partition("=")[2]) for part in parts]
    shares = [max(0.35, n / sum(need)) for n in need]
    widths = [int(avail * sh / sum(shares)) for sh in shares]
    chip_h = Inches(0.42)
    colors = [AMBER, TEAL]
    cx = x
    for i, part in enumerate(parts):
        label, _, cspec = part.partition("=")
        cw = widths[i]
        chip = rect(slide, cx, y, cw, chip_h, colors[i % 2], MSO_SHAPE.ROUNDED_RECTANGLE)
        tf = chip.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = Inches(0.15)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        run(p, label.strip(), 15, WHITE, bold=True)
        code_block(slide, cspec.strip(), cx, y + chip_h + Inches(0.08), cw, h - chip_h - Inches(0.08))
        cx += cw + gap


def cards_grid(slide, spec, x, y, w, h):
    """Grilla de tarjetas con imagen (ranking).
    Sintaxis: tarjetas: imagen ; puesto ; título ; cifra ; detalle | ...  (rutas relativas a la unidad)"""
    from PIL import Image
    items = [[t.strip() for t in part.split(";")] for part in spec.split("|") if part.strip()]
    cols = 6 if len(items) > 10 else 5
    rows = -(-len(items) // cols)
    cell_w, cell_h = int(w / cols), int(h / rows)
    text_h = Inches(0.95)
    pad = Inches(0.08)
    for i, (img, rank, title, figure, detail) in enumerate(items):
        cx = x + (i % cols) * cell_w
        cy = y + (i // cols) * cell_h
        box_w, box_h = cell_w - 2 * pad, cell_h - text_h - pad
        iw, ih = Image.open(os.path.join(UNIT_DIR, img)).size
        scale = min(box_w / iw, box_h / ih)
        pw, ph = int(iw * scale), int(ih * scale)
        slide.shapes.add_picture(os.path.join(UNIT_DIR, img), cx + pad + int((box_w - pw) / 2), cy + int((box_h - ph) / 2), pw, ph)
        badge = rect(slide, cx + cell_w - pad - Inches(0.36), cy + box_h - Inches(0.36), Inches(0.36), Inches(0.36), TEAL, MSO_SHAPE.OVAL)
        btf = badge.text_frame
        btf.margin_left = btf.margin_right = btf.margin_top = btf.margin_bottom = 0
        btf.vertical_anchor = MSO_ANCHOR.MIDDLE
        bp = btf.paragraphs[0]
        bp.alignment = PP_ALIGN.CENTER
        run(bp, rank, 11, WHITE, bold=True)
        tf = textbox(slide, cx + pad, cy + box_h + Inches(0.04), cell_w - 2 * pad, text_h)
        run(tf.paragraphs[0], title, 12, SLATE, bold=True)
        p = tf.add_paragraph()
        run(p, figure, 12, TEAL, bold=True)
        p = tf.add_paragraph()
        run(p, detail, 10, MUTED)


def subtables(slide, tables, x, y, w, h):
    """Varias tablas con título, lado a lado (líneas 'subtabla: Título' + filas '|')."""
    gap = Inches(0.35)
    tw = int((w - gap * (len(tables) - 1)) / len(tables))
    title_h = Inches(0.4)
    for i, t in enumerate(tables):
        tx = x + i * (tw + gap)
        tf = textbox(slide, tx, y, tw, title_h, MSO_ANCHOR.MIDDLE)
        run(tf.paragraphs[0], t["titulo"], 15, NAVY, bold=True)
        table(slide, t["rows"], tx, y + title_h, tw, h - title_h)


def view_diagram(slide, spec, x, y, w, h):
    """Dos pantallas a escala para una camara ortografica y un rango de spawn.
    Sintaxis: vista: 5 | -8, 8 | 16:9 | 9:16
      (orthographicSize | rango x del spawn | aspectos a comparar)"""
    parts = [t.strip() for t in spec.split("|")]
    size = float(parts[0])
    s0, s1 = [float(v) for v in parts[1].split(",")]
    aspects = []
    for a in parts[2:]:
        n, d = [float(v) for v in a.split(":")]
        aspects.append((a, n / d))
    world_h = 2 * size
    spans = [max(world_h * r, s1 - s0) for _, r in aspects]
    gap_u = 2.0
    legend_h = Inches(0.9)
    scale = min((w - Inches(0.2)) / (sum(spans) + gap_u * (len(spans) - 1)), (h - legend_h - Inches(0.9)) / world_h)
    cx = x + Inches(0.1)
    top = y + Inches(0.75)
    for (label, r), span in zip(aspects, spans):
        center = cx + span * scale / 2
        half_vis = size * r
        sw, sh = int(2 * half_vis * scale), int(world_h * scale)
        scr = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, int(center - sw / 2), top, sw, sh)
        scr.fill.solid()
        scr.fill.fore_color.rgb = LIGHT_BG
        scr.line.color.rgb = NAVY
        scr.line.width = Pt(2.5)
        scr.shadow.inherit = False
        band_y = top - Inches(0.32)
        band_h = Inches(0.18)
        lo, hi = max(s0, -half_vis), min(s1, half_vis)
        def X(u):
            return int(center + u * scale)
        if s0 < -half_vis:
            seg = rect(slide, X(s0), band_y, X(-half_vis) - X(s0), band_h, RED)
            seg.line.color.rgb = WHITE
        rect(slide, X(lo), band_y, X(hi) - X(lo), band_h, TEAL)
        if s1 > half_vis:
            rect(slide, X(half_vis), band_y, X(s1) - X(half_vis), band_h, RED)
        tf = textbox(slide, int(center - Inches(1.6)), top + sh + Inches(0.08), Inches(3.2), Inches(0.6))
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run(p, label, 15, SLATE, bold=True)
        p2 = tf.add_paragraph()
        p2.alignment = PP_ALIGN.CENTER
        run(p2, "se ven ±%s unidades" % ("%.1f" % half_vis).replace(".", ","), 13, MUTED)
        cx += span * scale + gap_u * scale
    ly = y + h - legend_h + Inches(0.2)
    rect(slide, x + Inches(0.1), ly + Inches(0.06), Inches(0.35), Inches(0.18), TEAL)
    tf = textbox(slide, x + Inches(0.55), ly, Inches(3.2), Inches(0.3), MSO_ANCHOR.MIDDLE)
    run(tf.paragraphs[0], "spawn dentro de la pantalla", 13, SLATE)
    rect(slide, x + Inches(3.6), ly + Inches(0.06), Inches(0.35), Inches(0.18), RED)
    tf = textbox(slide, x + Inches(4.05), ly, Inches(3.2), Inches(0.3), MSO_ANCHOR.MIDDLE)
    run(tf.paragraphs[0], "spawn fuera de la pantalla", 13, SLATE)
    tf = textbox(slide, x + Inches(0.1), ly + Inches(0.35), w, Inches(0.3), MSO_ANCHOR.MIDDLE)
    run(tf.paragraphs[0], "Escala real: cámara ortográfica de tamaño %s; spawn en x ∈ [%g, %g]" % (("%g" % size), s0, s1), 11, MUTED, italic=True)

def safearea_diagram(slide, spec, x, y, w, h):
    """Esquema de telefono en vertical: muesca, barra de gestos y zona segura punteada.
    Sintaxis: safearea: rotulo de la zona segura"""
    label = spec.strip()
    ph = h - Inches(0.1)
    pw = int(ph * 0.48)
    px = x + int((w - pw) / 2)
    py = y + Inches(0.05)
    body = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px, py, pw, ph)
    body.adjustments[0] = 0.1
    body.fill.solid()
    body.fill.fore_color.rgb = NAVY
    body.line.fill.background()
    body.shadow.inherit = False
    m = Inches(0.1)
    scr = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px + m, py + m, pw - 2 * m, ph - 2 * m)
    scr.adjustments[0] = 0.08
    scr.fill.solid()
    scr.fill.fore_color.rgb = WHITE
    scr.line.fill.background()
    scr.shadow.inherit = False
    notch_w, notch_h = int(pw * 0.3), Inches(0.28)
    rect(slide, int(px + (pw - notch_w) / 2), py + m, notch_w, notch_h, NAVY, MSO_SHAPE.ROUNDED_RECTANGLE)
    bar_w = int(pw * 0.4)
    rect(slide, int(px + (pw - bar_w) / 2), py + ph - m - Inches(0.2), bar_w, Inches(0.07), MUTED, MSO_SHAPE.ROUNDED_RECTANGLE)
    sx, sy = px + m + Inches(0.12), py + m + notch_h + Inches(0.12)
    sw, sh = pw - 2 * m - Inches(0.24), ph - 2 * m - notch_h - Inches(0.52)
    safe = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, sx, sy, sw, sh)
    safe.fill.solid()
    safe.fill.fore_color.rgb = RGBColor(0xE6, 0xF4, 0xF2)
    safe.line.color.rgb = TEAL
    safe.line.width = Pt(2)
    safe.line.dash_style = MSO_LINE_DASH_STYLE.DASH
    safe.shadow.inherit = False
    tf = safe.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    run(p, label, 14, TEAL, bold=True)
    # rotulos de las zonas reservadas, a los costados
    for text, ty in (("muesca / cámara", py + m), ("barra de gestos", py + ph - m - Inches(0.35))):
        tb = textbox(slide, px + pw + Inches(0.12), ty, Inches(1.6), Inches(0.35), MSO_ANCHOR.MIDDLE)
        run(tb.paragraphs[0], "← " + text, 12, MUTED)

def screenshot(slide, spec, x, y, w, h):
    """Captura real de pantalla. Sintaxis: captura: imagenes/a.png + imagenes/b.png | pie
    Las rutas son relativas a la unidad; varias imagenes separadas por ' + ' se apilan."""
    from PIL import Image
    paths, _, caption = spec.partition("|")
    files = [os.path.join(UNIT_DIR, f.strip()) for f in paths.split("+")]
    cap_h = Inches(0.4) if caption.strip() else 0
    gap = Inches(0.15)
    slot_h = int((h - cap_h - gap * (len(files) - 1)) / len(files))
    cy = y
    for f in files:
        iw, ih = Image.open(f).size
        scale = min(w / iw, slot_h / ih)
        pw, ph = int(iw * scale), int(ih * scale)
        pic = slide.shapes.add_picture(f, x + int((w - pw) / 2), cy + int((slot_h - ph) / 2), pw, ph)
        pic.line.color.rgb = GRID
        pic.line.width = Pt(1)
        cy += slot_h + gap
    if caption.strip():
        tf = textbox(slide, x, y + h - cap_h, w, cap_h, MSO_ANCHOR.MIDDLE)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        run(p, caption.strip(), 12, MUTED, italic=True)


def settings_panel(slide, spec, x, y, w, h):
    """Panel tipo Inspector de Unity. Sintaxis: ajustes: Titulo | Campo: valor | Campo: *valor
    El '*' marca el valor que hay que poner (se resalta)."""
    parts = [p.strip() for p in spec.split("|")]
    title, rows = parts[0], [r.partition(":") for r in parts[1:]]
    head_h = Inches(0.5)
    row_h = min(Inches(0.55), int((h - head_h) / max(len(rows), 1)))
    panel = rect(slide, x, y, w, head_h + row_h * len(rows), RGBColor(0x28, 0x28, 0x28))
    tf = textbox(slide, x + Inches(0.2), y, w - Inches(0.4), head_h, MSO_ANCHOR.MIDDLE)
    run(tf.paragraphs[0], title, 15, WHITE, bold=True)
    label_w = int(w * 0.5)
    for i, (field, _, value) in enumerate(rows):
        ry = y + head_h + row_h * i
        rect(slide, x, ry, w, Pt(1), RGBColor(0x3C, 0x3C, 0x3C))
        tf = textbox(slide, x + Inches(0.2), ry, label_w - Inches(0.2), row_h, MSO_ANCHOR.MIDDLE)
        run(tf.paragraphs[0], field.strip(), 14, RGBColor(0xD4, 0xD4, 0xD4))
        value = value.strip()
        hot = value.startswith("*")
        vx, vw = x + label_w, w - label_w - Inches(0.2)
        box = rect(slide, vx, ry + Inches(0.08), vw, row_h - Inches(0.16),
                   TEAL if hot else RGBColor(0x1E, 0x1E, 0x1E), MSO_SHAPE.ROUNDED_RECTANGLE)
        tf = box.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = Inches(0.12)
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        run(p, value.lstrip("*").strip(), 14, WHITE, bold=hot)


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
    # [etiqueta](url) se dibuja como enlace clicable que muestra solo la etiqueta
    parts = re.split(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", text)
    size = 14 if len("".join(parts[0::3] + parts[1::3])) < 120 else 12
    for i in range(0, len(parts), 3):
        if parts[i]:
            run(p, parts[i], size)
        if i + 2 < len(parts):
            r = run(p, parts[i + 1], size, color, bold=True)
            r.font.underline = True
            r.hyperlink.address = parts[i + 2]


# --- Layouts ----------------------------------------------------------------
def build_cover(prs, deck, s, total):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = NAVY
    rect(slide, 0, Inches(5.2), SLIDE_W, Pt(4), TEAL)
    has_img = bool(s.get("imagen"))
    w = SLIDE_W - 2 * MARGIN - (IMG_W + Inches(0.3) if has_img else 0)
    tf = textbox(slide, MARGIN, Inches(1.4), w, Inches(3.6), MSO_ANCHOR.BOTTOM)
    run(tf.paragraphs[0], kicker_text(s.get("kicker", "")).upper(), 14, RGBColor(0x99, 0xF6, 0xE4), bold=True)
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

    if s.get("hitos"):  # ocupa todo el ancho del cuerpo
        milestones_chart(slide, s["hitos"], MARGIN, BODY_TOP, SLIDE_W - 2 * MARGIN, body_h)
        return slide
    # paneles graficos a la derecha (clave, ancho, funcion); el primero presente gana
    if s.get("subtablas"):  # ocupa todo el ancho del cuerpo
        subtables(slide, s["subtablas"], MARGIN, BODY_TOP, SLIDE_W - 2 * MARGIN, body_h)
        return slide
    panels = (("cronologia", Inches(7.4), timeline_chart), ("vista", Inches(7.4), view_diagram),
              ("codigo2", Inches(12.2), code_columns), ("tarjetas", Inches(12.2), cards_grid),
              ("codigo", Inches(6.6), code_block), ("comparacion", Inches(6.2), compare_diagram),
              ("tiles", Inches(6.4), tiles_diagram), ("flujo", Inches(5.0), flow_diagram),
              ("diagrama", Inches(5.6), layer_diagram), ("safearea", Inches(4.6), safearea_diagram),
              ("captura", Inches(7.6), screenshot), ("ajustes", Inches(6.4), settings_panel))
    panel = next((pn for pn in panels if s.get(pn[0])), None)
    has_img = bool(s.get("imagen")) and panel is None
    panel_w = panel[1] if panel else IMG_W
    if panel and s.get("panel") == "ancho":  # el grafico ocupa todo el ancho; sin viñetas
        panel_w = SLIDE_W - 2 * MARGIN
    body_w = SLIDE_W - 2 * MARGIN - (panel_w + Inches(0.3) if (panel or has_img) else 0)
    if panel:
        panel[2](slide, s[panel[0]], SLIDE_W - MARGIN - panel_w, BODY_TOP, panel_w, body_h)
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


def build_unido(decks, out_dir=UNIT_DIR, version=None):
    """Un solo .pptx con todas las clases, numeracion continua; el pie conserva la clase.
    Con version N > 1 se guarda como Unidad-4-2026-completa-vN.pptx (no pisa la anterior)."""
    prs = Presentation()
    prs.slide_width, prs.slide_height = SLIDE_W, SLIDE_H
    total = sum(len(d["slides"]) for d in decks)
    n = 0
    for deck in decks:
        for s in deck["slides"]:
            n += 1
            s = dict(s, num=n)
            maker = build_cover if s.get("tipo") == "portada" else build_content
            add_notes(maker(prs, deck, s, total), s["notes"])
    suffix = "-v%d" % version if version and version > 1 else ""
    path = os.path.join(out_dir, "Unidad-4-2026-completa%s.pptx" % suffix)
    prs.save(path)
    return path, total


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Genera los decks de la Unidad 4.")
    ap.add_argument("--decks", type=int, nargs="+", help="numeros de deck a generar (por defecto, todos)")
    ap.add_argument("--version", type=int, help="agrega el sufijo -vN al nombre de los archivos, incluido el completo (N > 1)")
    ap.add_argument("--out-dir", default=UNIT_DIR, help="carpeta de salida (por defecto, la de la unidad)")
    ap.add_argument("--por-clase", action="store_true", help="genera ademas un .pptx por seccion")
    args = ap.parse_args()
    decks = parse(SOURCE)
    if len(decks) < 4:
        sys.exit("Se esperaban al menos 4 secciones (clases + anexos) y se encontraron %d" % len(decks))
    if args.por_clase or args.decks:
        for path, total in build(decks, args.decks, args.version, args.out_dir):
            print("OK  %-40s %2d slides" % (os.path.basename(path), total))
    path, total = build_unido(decks, args.out_dir, args.version)
    print("OK  %-40s %2d slides" % (os.path.basename(path), total))
