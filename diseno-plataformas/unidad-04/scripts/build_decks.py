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

KEYS = ("tipo", "kicker", "pregunta", "actividad", "imagen", "diagrama", "cronologia", "hitos", "flujo", "comparacion", "tiles", "codigo", "vista", "safearea", "video", "fuente")
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


def code_block(slide, spec, x, y, w, h):
    """Bloque de codigo leido del archivo real. Sintaxis: codigo: ruta/relativa/a/la/unidad.cs:61-73
    Resalta en ambar las lineas que contienen 'Input.'"""
    path, _, rng = spec.rpartition(":")
    a, b = [int(v) for v in rng.split("-")]
    with open(os.path.join(UNIT_DIR, path), encoding="utf-8") as fh:
        lines = fh.read().splitlines()[a - 1:b]
    indent = min((len(l) - len(l.lstrip()) for l in lines if l.strip()), default=0)
    title_h = Inches(0.35)
    tf = textbox(slide, x, y, w, title_h, MSO_ANCHOR.MIDDLE)
    run(tf.paragraphs[0], os.path.basename(path) + "  ·  líneas %d–%d" % (a, b), 12, MUTED, bold=True)
    box = rect(slide, x, y + title_h + Inches(0.05), w, h - title_h - Inches(0.05), RGBColor(0x0F, 0x17, 0x2A), MSO_SHAPE.ROUNDED_RECTANGLE)
    box.adjustments[0] = 0.04
    tf = box.text_frame
    tf.word_wrap = False
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = Inches(0.25)
    size = 15 if len(lines) <= 14 else 12
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        r = run(p, "%3d  " % (a + i), size, RGBColor(0x64, 0x74, 0x8B))
        r.font.name = "Consolas"
        hot = "Input." in line
        r2 = run(p, line[indent:] if line.strip() else " ", size, AMBER if hot else RGBColor(0xE2, 0xE8, 0xF0), bold=hot)
        r2.font.name = "Consolas"


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

    if s.get("hitos"):  # ocupa todo el ancho del cuerpo
        milestones_chart(slide, s["hitos"], MARGIN, BODY_TOP, SLIDE_W - 2 * MARGIN, body_h)
        return slide
    # paneles graficos a la derecha (clave, ancho, funcion); el primero presente gana
    panels = (("cronologia", Inches(7.4), timeline_chart), ("vista", Inches(7.4), view_diagram),
              ("codigo", Inches(6.6), code_block), ("comparacion", Inches(6.2), compare_diagram),
              ("tiles", Inches(6.4), tiles_diagram), ("flujo", Inches(5.0), flow_diagram),
              ("diagrama", Inches(5.6), layer_diagram), ("safearea", Inches(4.6), safearea_diagram))
    panel = next((pn for pn in panels if s.get(pn[0])), None)
    has_img = bool(s.get("imagen")) and panel is None
    panel_w = panel[1] if panel else IMG_W
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
