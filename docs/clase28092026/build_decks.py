# -*- coding: utf-8 -*-
"""
Genera las diapositivas de la clase del 28/09/2026 (docs/clase28092026.md):

  - Clase1-Testing-Integracion.pptx
  - Clase2-Plataformas.pptx

Estilo visual reutilizado de docs/unidad03/scripts/generar_diapositivas.py
(misma paleta, cabecera y tipografia) para mantener la continuidad con la Unidad 3.

Los recuadros punteados "IMAGEN" son marcadores para insertar imagenes a mano.
Las referencias a codigo del proyecto nave + asteroides se citan por archivo y
lineas (no se copia el codigo: licencia Kodeco). Numeros de linea tomados de
Asteroides/asteroide-final/CodeCoverage/Report/*.html.

Requiere: pip install python-pptx
"""
import os
import math

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_LINE

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------------
# Paleta (identica a Unidad 3)
# ----------------------------------------------------------------------------
NAVY = RGBColor(0x1F, 0x2A, 0x44)
NAVY_LIGHT = RGBColor(0x33, 0x41, 0x63)
GREEN = RGBColor(0x16, 0xA3, 0x4A)
AMBER = RGBColor(0xD9, 0x77, 0x06)
TEAL = RGBColor(0x0D, 0x94, 0x88)
TEAL_SOFT = RGBColor(0x9C, 0xC9, 0xC5)
SLATE = RGBColor(0x1F, 0x29, 0x37)
MUTED = RGBColor(0x6B, 0x72, 0x80)
LIGHT_BG = RGBColor(0xF3, 0xF4, 0xF6)
ACT_BG = RGBColor(0xEA, 0xF2, 0xF1)
CODE_BG = RGBColor(0xFE, 0xF3, 0xE2)
IMG_BG = RGBColor(0xF8, 0xFA, 0xFC)
IMG_LINE = RGBColor(0x94, 0xA3, 0xB8)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

FONT = "Calibri"

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN_X = Inches(0.55)
HEADER_H = Inches(1.05)
FOOTER_Y = Inches(7.08)

IMG_X = Inches(8.85)
IMG_W = Inches(3.93)
CONTENT_W_IMG = Inches(8.0)


# ----------------------------------------------------------------------------
# Primitivas
# ----------------------------------------------------------------------------
def add_rect(slide, x, y, w, h, color, shape=MSO_SHAPE.RECTANGLE):
    shp = slide.shapes.add_shape(shape, x, y, w, h)
    shp.fill.solid()
    shp.fill.fore_color.rgb = color
    shp.line.fill.background()
    shp.shadow.inherit = False
    return shp


def add_textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(x, y, w, h)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    return tb, tf


def style_run(r, size, color=SLATE, bold=False, italic=False):
    r.font.size = Pt(size)
    r.font.color.rgb = color
    r.font.bold = bold
    r.font.italic = italic
    r.font.name = FONT


def add_text(slide, x, y, w, h, text, size=18, color=SLATE, bold=False, italic=False,
             align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    tb, tf = add_textbox(slide, x, y, w, h, anchor=anchor)
    p = tf.paragraphs[0]
    p.alignment = align
    style_run(p.add_run(), size, color, bold, italic)
    p.runs[0].text = text
    return tb


def add_pill(slide, x, y, text, bg, size=12, width=None):
    w = width or Inches(0.4 + 0.085 * len(text))
    shp = add_rect(slide, x, y, w, Inches(0.34), bg, MSO_SHAPE.ROUNDED_RECTANGLE)
    try:
        shp.adjustments[0] = 0.5
    except Exception:
        pass
    tf = shp.text_frame
    tf.margin_left = tf.margin_right = Inches(0.08)
    tf.margin_top = tf.margin_bottom = Inches(0.01)
    tf.word_wrap = False
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = text
    style_run(r, size, WHITE, bold=True)
    return shp


def lines_for(text, width_in, size_pt):
    """Estimacion grosera de lineas que ocupa un texto."""
    chars_per_line = max(10, int(width_in * 72 / (size_pt * 0.5)))
    return max(1, math.ceil(len(text) / chars_per_line))


def new_slide(prs):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = WHITE
    return slide


def add_header(slide, num, title, kicker=None, badge=None):
    add_rect(slide, 0, 0, SLIDE_W, HEADER_H, NAVY)
    add_rect(slide, 0, HEADER_H, SLIDE_W, Pt(3), TEAL)
    circ = add_rect(slide, Inches(0.3), Inches(0.24), Inches(0.58), Inches(0.58), TEAL, MSO_SHAPE.OVAL)
    ctf = circ.text_frame
    ctf.margin_left = ctf.margin_right = ctf.margin_top = ctf.margin_bottom = 0
    cp = ctf.paragraphs[0]
    cp.alignment = PP_ALIGN.CENTER
    cr = cp.add_run()
    cr.text = str(num)
    style_run(cr, 18, WHITE, bold=True)

    tb, tf = add_textbox(slide, Inches(1.05), Inches(0.12), Inches(9.7), Inches(0.85), anchor=MSO_ANCHOR.MIDDLE)
    if kicker:
        pk = tf.paragraphs[0]
        rk = pk.add_run()
        rk.text = kicker.upper()
        style_run(rk, 11, TEAL_SOFT, bold=True)
        p = tf.add_paragraph()
    else:
        p = tf.paragraphs[0]
    r = p.add_run()
    r.text = title
    style_run(r, 26, WHITE, bold=True)
    if badge:
        add_pill(slide, Inches(10.85), Inches(0.37), badge, AMBER, size=11, width=Inches(2.1))


def add_footer(slide, num, total, footer_text):
    add_text(slide, MARGIN_X, FOOTER_Y, Inches(10), Inches(0.3), footer_text, size=10, color=MUTED, italic=True)
    add_text(slide, Inches(12.1), FOOTER_Y, Inches(0.9), Inches(0.3), f"{num}/{total}", size=10,
             color=MUTED, align=PP_ALIGN.RIGHT)


def add_image_placeholder(slide, x, y, w, h, description):
    box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    box.fill.solid()
    box.fill.fore_color.rgb = IMG_BG
    box.line.color.rgb = IMG_LINE
    box.line.width = Pt(1.5)
    box.line.dash_style = MSO_LINE.DASH
    box.shadow.inherit = False
    tf = box.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = Inches(0.2)
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = "🖼  IMAGEN"
    style_run(r, 14, MUTED, bold=True)
    p2 = tf.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    p2.space_before = Pt(6)
    r2 = p2.add_run()
    r2.text = description
    style_run(r2, 12, MUTED, italic=True)


def add_band(slide, y, text, icon, bg=ACT_BG, color=NAVY, size=15):
    add_rect(slide, MARGIN_X, y, SLIDE_W - 2 * MARGIN_X, Inches(0.72), bg)
    tb, tf = add_textbox(slide, MARGIN_X + Inches(0.2), y, SLIDE_W - 2 * MARGIN_X - Inches(0.4),
                         Inches(0.72), anchor=MSO_ANCHOR.MIDDLE)
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = f"{icon}  {text}"
    style_run(r, size, color, bold=True, italic=True)


def add_coderef(slide, y, text, width):
    add_rect(slide, MARGIN_X, y, width, Inches(0.5), CODE_BG)
    tb, tf = add_textbox(slide, MARGIN_X + Inches(0.15), y, width - Inches(0.3), Inches(0.5),
                         anchor=MSO_ANCHOR.MIDDLE)
    p = tf.paragraphs[0]
    r1 = p.add_run()
    r1.text = "💻 Ver en el código:  "
    style_run(r1, 12, AMBER, bold=True)
    r2 = p.add_run()
    r2.text = text
    style_run(r2, 12, SLATE)


def add_bullets(slide, x, y, w, items, size):
    width_in = w / 914400
    total_h = 0
    heights = []
    for it in items:
        h = lines_for(it, width_in - 0.3, size) * size * 1.25 / 72 + 0.1
        heights.append(h)
        total_h += h
    tb, tf = add_textbox(slide, x, y, w, Inches(total_h))
    for i, it in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.space_after = Pt(6)
        if it.startswith("  "):  # sub-item
            r = p.add_run()
            r.text = f"      –  {it.strip()}"
            style_run(r, size - 2, MUTED)
        else:
            r = p.add_run()
            r.text = "■  "
            style_run(r, size - 4, TEAL, bold=True)
            r2 = p.add_run()
            r2.text = it
            style_run(r2, size, SLATE)
    return Inches(total_h)


def add_flow(slide, x, y, w, steps, box_h=Inches(0.52), arrow_h=Inches(0.28), size=15, highlight_last=False):
    for i, step in enumerate(steps):
        last = i == len(steps) - 1
        color = GREEN if (last and highlight_last) else NAVY_LIGHT
        add_rect(slide, x, y, w, box_h, color)
        add_text(slide, x + Inches(0.2), y, w - Inches(0.4), box_h, step, size=size, color=WHITE, bold=True,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
        y += box_h
        if not last:
            add_text(slide, x, y, w, arrow_h, "↓", size=16, color=TEAL, bold=True,
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            y += arrow_h
    return y


def add_table(slide, x, y, w, headers, rows, widths=None, size=12, title=None):
    if title:
        add_text(slide, x, y, w, Inches(0.35), title, size=14, color=TEAL, bold=True)
        y += Inches(0.38)
    nrows, ncols = len(rows) + 1, len(headers)
    row_h = Inches(0.36)
    gt = slide.shapes.add_table(nrows, ncols, x, y, w, row_h * nrows).table
    if widths:
        tot = sum(widths)
        for i, wd in enumerate(widths):
            gt.columns[i].width = Emu(int(w * wd / tot))
    for c, h in enumerate(headers):
        cell = gt.cell(0, c)
        cell.text = h
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        for p in cell.text_frame.paragraphs:
            for r in p.runs:
                style_run(r, size + 1, WHITE, bold=True)
    for ri, row in enumerate(rows, start=1):
        for c, val in enumerate(row):
            cell = gt.cell(ri, c)
            cell.text = val
            cell.fill.solid()
            cell.fill.fore_color.rgb = LIGHT_BG if ri % 2 == 0 else WHITE
            cell.margin_top = cell.margin_bottom = Inches(0.04)
            for p in cell.text_frame.paragraphs:
                for r in p.runs:
                    style_run(r, size, SLATE, bold=(c == 0))
    # altura estimada real (celdas que envuelven texto)
    est = 0.0
    col_w_in = [(gt.columns[i].width / 914400) for i in range(ncols)]
    for row in [headers] + rows:
        est += max(lines_for(v, col_w_in[i] - 0.2, size) for i, v in enumerate(row)) * size * 1.3 / 72 + 0.1
    return y + Inches(est)


# ----------------------------------------------------------------------------
# Renderers
# ----------------------------------------------------------------------------
def render_title(prs, s, deck):
    slide = new_slide(prs)
    add_rect(slide, 0, 0, SLIDE_W, SLIDE_H, NAVY)
    add_rect(slide, 0, Inches(4.55), SLIDE_W, Pt(3), TEAL)
    add_text(slide, Inches(1), Inches(1.9), Inches(11.3), Inches(0.5), s["kicker"].upper(), size=20,
             color=TEAL_SOFT, bold=True)
    add_text(slide, Inches(1), Inches(2.45), Inches(11.3), Inches(1.4), s["title"], size=42, color=WHITE, bold=True)
    add_text(slide, Inches(1), Inches(3.85), Inches(11.3), Inches(0.6), s["subtitle"], size=20,
             color=RGBColor(0xD1, 0xD5, 0xDB))
    add_text(slide, Inches(1), Inches(4.8), Inches(11.3), Inches(0.5), s["footer"], size=14, color=TEAL_SOFT,
             italic=True)
    if s.get("image"):
        add_image_placeholder(slide, Inches(8.9), Inches(5.3), Inches(3.9), Inches(1.6), s["image"])
    add_footer(slide, s["num"], deck["total"], deck["footer"])
    slide.notes_slide.notes_text_frame.text = s.get("notes", "")


def render_content(prs, s, deck):
    slide = new_slide(prs)
    add_header(slide, s["num"], s["title"], kicker=s.get("kicker"), badge=s.get("badge"))

    has_img = bool(s.get("image"))
    cw = CONTENT_W_IMG if has_img else SLIDE_W - 2 * MARGIN_X
    y = Inches(1.4)

    if s.get("tag"):
        add_pill(slide, MARGIN_X, y, f"Ejemplo: {s['tag']}", TEAL, size=12)
        y += Inches(0.52)
    if s.get("quote"):
        qs = s.get("qsize", 20)
        h = Inches(lines_for(s["quote"], cw / 914400, qs) * qs * 1.3 / 72 + 0.1)
        add_text(slide, MARGIN_X, y, cw, h, s["quote"], size=qs, color=NAVY, bold=True, italic=True)
        y += h + Inches(0.15)
    if s.get("flow"):
        y = add_flow(slide, MARGIN_X, y, cw, s["flow"], size=s.get("fsize", 15),
                     highlight_last=s.get("highlight_last", False)) + Inches(0.15)
    for t in s.get("tables", []):
        y = add_table(slide, MARGIN_X, y, cw, t["headers"], t["rows"], t.get("widths"),
                      size=t.get("size", 12), title=t.get("title")) + Inches(0.2)
    if s.get("bullets"):
        y += add_bullets(slide, MARGIN_X, y, cw, s["bullets"], s.get("bsize", 17 if has_img else 18))
    if s.get("cols"):
        col_w = (cw - Inches(0.35)) / 2
        for i, (ctitle, citems, ccolor) in enumerate(s["cols"]):
            x = MARGIN_X + i * (col_w + Inches(0.35))
            add_rect(slide, x, y, col_w, Inches(0.5), ccolor)
            add_text(slide, x, y, col_w, Inches(0.5), ctitle, size=16, color=WHITE, bold=True,
                     align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            add_bullets(slide, x, y + Inches(0.65), col_w, citems, s.get("bsize", 15))

    bottom_band_y = Inches(6.15)
    if s.get("coderef"):
        cy = Inches(5.5) if s.get("actividad") or s.get("pregunta") or s.get("nota") else Inches(6.3)
        add_coderef(slide, cy, s["coderef"], SLIDE_W - 2 * MARGIN_X)
    if s.get("actividad"):
        add_band(slide, bottom_band_y, s["actividad"], "✍ Actividad:")
    elif s.get("pregunta"):
        add_band(slide, bottom_band_y, s["pregunta"], "❓")
    elif s.get("nota"):
        add_band(slide, bottom_band_y, s["nota"], "ℹ", bg=LIGHT_BG, color=MUTED, size=14)

    if has_img:
        img_bottom = Inches(5.35) if s.get("coderef") else (Inches(5.95) if (s.get("actividad") or s.get("pregunta") or s.get("nota")) else Inches(6.85))
        add_image_placeholder(slide, IMG_X, Inches(1.4), IMG_W, img_bottom - Inches(1.4), s["image"])

    add_footer(slide, s["num"], deck["total"], deck["footer"])
    slide.notes_slide.notes_text_frame.text = s.get("notes", "")


def build(deck, filename):
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    deck["total"] = len(deck["slides"])
    for i, s in enumerate(deck["slides"], start=1):
        s["num"] = i
        (render_title if s.get("type") == "title" else render_content)(prs, s, deck)
    out = os.path.join(OUT_DIR, filename)
    prs.save(out)
    print(f"OK — {len(prs.slides)} diapositivas en {out}")


# ============================================================================
# CLASE 1 — Testing de integración
# ============================================================================
CLASE1 = dict(
    footer="Diseño según Plataformas de Juego · Clase 28/09/2026 · Testing de integración (Unidades I–III)",
    slides=[
        dict(type="title", kicker="Unidades I · II · III",
             title="Testing de integración en videojuegos",
             subtitle="Diseño según Plataformas de Juego · Clase teórico-práctica (120 min)",
             footer="Ing. Elsa Daniela Ramírez · FI – UNJu · 2026",
             notes="Portada. Continuidad directa con la Unidad III (pruebas unitarias) y la Unidad II (tickets)."),

        dict(title="Objetivos de la clase", kicker="Al finalizar podrán",
             bullets=[
                 "Diferenciar los NIVELES de prueba (unitario, integración, sistema, aceptación) y reconocer el TIPO funcional como un eje independiente",
                 "Identificar los sistemas de un juego que deben probarse en conjunto",
                 "Diseñar casos de prueba de integración, incluido un caso de valor frontera",
                 "Ejecutar una prueba de integración en Unity, automatizada o manual documentada",
                 "Registrar un defecto con un ticket completo",
                 "Reconocer qué NO detecta una prueba de integración",
             ],
             notes="Objetivo 1 reformulado respecto del borrador original: 'funcional' no es un nivel sino un tipo de prueba (Unidad I del programa)."),

        dict(title="Agenda (120 min)", kicker="Organización",
             tables=[dict(headers=["Bloque", "Minutos", "Qué hacemos"],
                          widths=[3, 1.2, 7],
                          size=16,
                          rows=[
                              ["1. Problema y recuperación", "10", "Un caso real y lo que ya sabemos de la prueba unitaria"],
                              ["2. Teoría", "20", "Niveles y tipos · integración · Play Mode · diseño de casos"],
                              ["3. Análisis del proyecto", "10", "Clasificar la suite del proyecto nave + asteroides"],
                              ["4. Puente: ticket", "5", "Del fallo al ticket (detalle en Unidad II)"],
                              ["Práctica principal", "45", "Diseñar y ejecutar una prueba de integración"],
                              ["5. Puesta en común", "20", "≈ 3 min por grupo"],
                              ["6. Cierre", "10", "Ticket de salida individual"],
                          ])],
             notes="El borrador original sumaba 135 min. Se recortaron recuperación (−5), teoría (−5), análisis (−10) y Jira (−10); se amplió la puesta en común (+10) para que todos los grupos presenten."),

        # --- Bloque 1 ---
        dict(title="Cada pieza funciona… y el juego no", kicker="El problema",
             tag="Pokémon Rojo / Azul · MissingNo.",
             bullets=[
                 "El sistema de encuentros salvajes funciona",
                 "El sistema que guarda el nombre del jugador funciona",
                 "Juntos: en la costa de Isla Canela, la tabla de encuentros lee datos que dejó el nombre del jugador",
                 "Resultado: aparece un Pokémon que no existe",
                 "Ninguna prueba de una sola pieza lo habría encontrado",
             ],
             image="Captura de MissingNo. en combate (Pokémon Rojo/Azul). Opcional: esquema de dos cajas «Nombre del jugador» → «Tabla de encuentros» con la flecha marcada en rojo.",
             pregunta="¿Qué prueba unitaria habría detectado este fallo?",
             notes="5 min. Mecanismo: tras ver el tutorial del anciano en Ciudad Verde, el nombre del jugador queda en la zona de memoria que luego se usa como datos de encuentro; la costa este de Isla Canela no carga su propia tabla y lee esos restos. Respuesta esperada: ninguna — el defecto está en la interacción. No nombrar todavía 'integración'."),

        dict(title="Lo que ya sabemos: la prueba unitaria", kicker="Recuperación · Unidad III",
             tag="Cryptbound · PlayerHealth.TakeDamage",
             bullets=[
                 "Verifica UN comportamiento de UNA unidad aislada",
                 "Vida 100 → TakeDamage(25) → vida 75",
                 "Rápida, determinista, fácil de diagnosticar",
                 "No verifica cómo esa unidad se conecta con las demás",
             ],
             image="Captura del Test Runner de la Unidad III con los tests de PlayerHealth en verde.",
             pregunta="Si cada componente pasa sus tests… ¿el juego funciona?",
             notes="5 min. No reexplicar la Unidad III: solo anclar vocabulario. La pregunta final abre el concepto de integración."),

        # --- Bloque 2 ---
        dict(title="Niveles y tipos: dos ejes distintos", kicker="Unidad I · marco conceptual",
             tables=[
                 dict(title="NIVELES — ¿qué alcance tiene la prueba?",
                      headers=["Nivel", "Qué verifica", "Ejemplo"], widths=[1.6, 4, 5], size=13,
                      rows=[
                          ["Unitario", "Una unidad de código aislada", "AgregarVida(20) suma 20 y no supera la vida máxima"],
                          ["Integración", "La comunicación entre dos o más componentes", "Recoger una poción y que aparezca en el inventario"],
                          ["Sistema", "El juego completo, en una build similar a la real", "Completar Nivel01 de principio a fin en la build de PC"],
                          ["Aceptación", "Que cumple los criterios acordados con quien lo recibe", "El playtest / publisher aprueba el nivel según lo acordado"],
                      ]),
                 dict(title="TIPOS — ¿qué aspecto mira? (se aplican en cualquier nivel)",
                      headers=["Tipo", "Qué verifica", "Ejemplo"], widths=[1.6, 4, 5], size=13,
                      rows=[
                          ["Funcional", "QUÉ hace el juego", "Comprar, equipar y usar un objeto"],
                          ["No funcional", "CÓMO lo hace: rendimiento, usabilidad…", "La pelea del jefe se mantiene en 60 FPS"],
                      ]),
             ],
             nota="Manual / automatizado no son niveles: son formas de ejecutar una prueba, combinables con cualquier nivel.",
             notes="8 min. Corrección conceptual del borrador: 'Funcional' NO es un nivel entre integración y sistema; es un tipo. 'Comprar, equipar y usar' puede probarse a nivel de integración o de sistema. Se agrega el nivel Aceptación, que está en el programa (Unidad I)."),

        dict(title="Clasificar: ¿qué nivel? ¿qué tipo?", kicker="Práctica rápida",
             tag="Sea of Thieves (Rare) · GDC 2019",
             bullets=[
                 "1. Comprar un arma descuenta el oro correcto y la agrega al inventario",
                 "2. CalcularDaño(crítico) devuelve el doble",
                 "3. La pelea del jefe se mantiene en 60 FPS",
                 "4. El Nivel 1 se completa de principio a fin en la build",
                 "5. El publisher aprueba la demo según lo acordado",
                 "En Sea of Thieves, Rare combina tests unitarios, de integración y pruebas nocturnas de rendimiento",
             ],
             image="Matriz de dos ejes vacía (filas: unitario / integración / sistema / aceptación; columnas: funcional / no funcional) para ubicar los casos. Opcional: la pirámide de tests de la charla de Rare (GDC 2019).",
             actividad="Ubiquen cada caso en la matriz nivel × tipo (votación a mano alzada).",
             notes="Respuestas: 1 integración · funcional | 2 unitario · funcional | 3 sistema · no funcional (rendimiento) | 4 sistema · funcional | 5 aceptación (funcional y no funcional). Referencia: 'Automated Testing of Gameplay Features in Sea of Thieves', Robert Masella, GDC 2019 (verificada en docs/unidad03/06-investigacion-recursos.md)."),

        dict(title="Integración: seguir el flujo entre sistemas", kicker="Teoría",
             tag="Proyecto nave + asteroides (repositorio)",
             flow=[
                 "El láser choca con un asteroide",
                 "Laser detecta la colisión y avisa a Game",
                 "Game suma 1 al puntaje (score)",
                 "Game actualiza el texto del HUD (scoreText)",
             ],
             image="Diagrama de secuencia: Láser → Asteroide → Game → HUD, con cada «costura» (flecha entre sistemas) resaltada en rojo.",
             coderef="Laser.cs 46–55 (llamada a Game en 50) · Game.cs 82–86 (score en 84, HUD en 85)",
             actividad="¿En qué flecha se puede romper este flujo? Marquen cada costura.",
             notes="3 min. Integración = verificar las costuras entre componentes, no cada componente. Cada flecha es una interfaz: un método llamado, un dato que cruza, una condición inicial."),

        dict(title="Contratos invisibles entre sistemas", kicker="Teoría",
             tag="Proyecto nave + asteroides (repositorio)",
             bullets=[
                 "El asteroide reconoce a la nave comparando el NOMBRE del objeto con «ShipModel»",
                 "Ese nombre vive en la escena / prefab, no en el código de la nave",
                 "Si alguien renombra el objeto: no hay Game Over",
                 "Ningún test del asteroide solo lo detecta; sí una prueba que junta Asteroide + Nave + Game",
             ],
             image="Captura de la jerarquía o del Inspector de Unity con el objeto «ShipModel» resaltado.",
             coderef="Asteroid.cs 52–59 (comparación de nombre en 54) · TestSuite.cs 63–71 (test que lo cubre)",
             pregunta="¿Qué otros contratos invisibles hay en sus proyectos? (nombres, tags, layers, orden de escenas)",
             notes="3 min. Es el ejemplo más claro de dependencia implícita: el contrato no está escrito en ninguna interfaz."),

        # --- Bloque 3 ---
        dict(title="Play Mode no es lo mismo que integración", kicker="Unidad III → integración",
             tag="TestSuite.cs del proyecto nave + asteroides",
             bullets=[
                 "Edit Mode / Play Mode = DÓNDE corre el test",
                 "Unitario / integración = QUÉ alcance tiene",
                 "Una clase aislada probada en Play Mode sigue siendo una prueba unitaria",
                 "La suite del proyecto carga el prefab completo Game → casi todos sus tests integran varios sistemas",
                 "El comentario del código dice que solo uno es de integración: ¿es cierto?",
             ],
             image="Captura del Test Runner con los 7 tests de la suite (sin clasificar).",
             coderef="TestSuite.cs 40–45 (carga del prefab en 43) · comentario 82–87 · tests en 53–149",
             actividad="En grupos: clasifiquen los 7 tests de TestSuite.cs y justifiquen (10 min).",
             notes="Respuestas orientativas — AsteroidsMoveDown (53–61) y LaserMovesUp (117–125): el comportamiento es de una sola clase pero depende del Spawner/Ship y del prefab → discutible, buen debate. GameOverOccursOnAsteroidCollision (63–71): integración (Spawner, Asteroid, física, Game). NewGameRestartsGame (73–80): integración (NewGame toca Spawner, Ship y UI aunque el assert mire solo un flag). GameOverStopsSpawningAndDisablesShip (88–115): integración. LaserDestroysAsteroid (127–137) y DestroyedAsteroidRaisesScore (139–149): integración. Conclusión: el comentario de 82–87 es impreciso — la cantidad de asserts no define el nivel."),

        dict(title="Diseñar un caso de integración", kicker="Unidad II → integración",
             tables=[dict(headers=["Campo", "INT-001", "INT-002 (valor frontera)"], widths=[1.7, 4.3, 4.3], size=14,
                          rows=[
                              ["Nombre", "Recibir daño actualiza vida y barra", "Daño letal activa la derrota"],
                              ["Precondiciones", "Vida 100/100 · UNA sola colisión · sin invulnerabilidad", "Igual que INT-001"],
                              ["Datos", "Daño del enemigo: 25", "Daño: 100 (y 99 como contraste)"],
                              ["Pasos", "1. Iniciar escena de prueba  2. Provocar una colisión  3. Leer vida y barra", "Igual que INT-001"],
                              ["Resultado esperado", "Vida = 75 · barra = 75/100 · sin derrota", "100 → vida 0 y derrota · 99 → vida 1 y sin derrota"],
                              ["Resultado obtenido", "(completar al ejecutar)", "(completar al ejecutar)"],
                              ["Estado", "Pasado / Fallido", "Pasado / Fallido"],
                          ])],
             actividad="En parejas: completen INT-002 antes de ver la respuesta.",
             notes="6 min. Correcciones respecto del borrador: (1) 'la barra se actualiza' no es verificable → 'barra = 75/100'; (2) sin 'una sola colisión' el contacto sostenido aplica daño varias veces; (3) el flujo incluía la derrota pero ningún caso la probaba → INT-002 con valores frontera (Unidad I); (4) 'Pasado/Fallido' según el programa."),

        dict(title="Lo que el test no ve", kicker="Límites",
             tag="DestroyedAsteroidRaisesScore",
             bullets=[
                 "El test verifica score… pero no el texto del HUD",
                 "Si se borra la línea que actualiza scoreText, la suite sigue en verde → falso negativo",
                 "Las esperas fijas (0,1 s) dependen de la máquina y de la física: el test puede fallar sin defecto → falso positivo",
                 "Una suite en verde no demuestra que no haya defectos",
             ],
             image="Pantalla dividida: a la izquierda, el Test Runner con DestroyedAsteroidRaisesScore en verde; a la derecha, el juego con el asteroide destruido y el HUD en «Score: 0» (bug provocado).",
             coderef="TestSuite.cs 139–149 (assert en 148) · Game.cs 85 (HUD) · esperas en TestSuite.cs 58, 68, 134, 146",
             actividad="¿Qué assert agregarían para cubrir el HUD?",
             notes="3 min (disparador de la práctica). Terminología de la Unidad I: falso negativo = el test pasa aunque hay defecto; falso positivo = el test falla sin que haya defecto. 'Las pruebas muestran la presencia de defectos, no su ausencia' es uno de los 7 principios."),

        dict(title="¿Automatizar o no?", kicker="Unidad III · manual vs. automatizada",
             tag="Call of Duty (Activision) · GDC",
             cols=[
                 ("Conviene automatizar", [
                     "Flujos que se repiten en cada build",
                     "Resultado verificable por código (valores, estados)",
                     "Riesgo de regresión frecuente",
                     "Ej.: daño → vida · asteroide → puntaje",
                 ], NAVY_LIGHT),
                 ("Conviene manual documentada", [
                     "Lo que se ve o se siente (legibilidad, animación, feedback)",
                     "Flujos largos y costosos de montar",
                     "Primera exploración de un sistema nuevo",
                     "Ej.: menú → cambio de escena con transición",
                 ], TEAL),
             ],
             actividad="Clasifiquen los 5 flujos del análisis: ¿automatizable o manual?",
             notes="Incluido en teoría. Una prueba de integración manual y documentada sigue siendo una prueba de integración. Referencia: 'Automated Testing and Profiling for Call of Duty', GDC (ver docs/unidad03/06-investigacion-recursos.md): aun automatizando a escala mantienen QA manual."),

        # --- Bloque 4 ---
        dict(title="Puente: del fallo al ticket", kicker="Unidad II · 5 min", badge="Ver Unidad II",
             tables=[dict(headers=["Campo", "Ejemplo"], widths=[2, 6], size=14,
                          rows=[
                              ["Título", "La barra de vida no se actualiza tras recibir daño"],
                              ["Pasos", "1. Abrir Nivel01  2. Iniciar  3. Una colisión con el enemigo  4. Observar la barra"],
                              ["Esperado / Actual", "Vida y barra 100 → 75  /  vida interna 75 (Inspector), barra en 100"],
                              ["Severidad / Prioridad", "Media / Alta"],
                              ["Entorno / Build", "Build 0.x · Windows 11 · Unity 6000.x (completar)"],
                              ["Evidencia / Asignado", "Captura o video / (completar)"],
                          ])],
             image="Captura de un ticket real en Jira con estos campos señalados.",
             nota="Severidad ≠ prioridad. No profundizar: el detalle está en la Unidad II.",
             notes="5 min como máximo. Se completan los campos que el borrador pedía pero el ejemplo omitía (entorno, build, asignado)."),

        # --- Práctica ---
        dict(title="Consigna práctica (45 min)", kicker="Actividad principal",
             bullets=[
                 "1. Elegir un flujo con al menos dos sistemas",
                 "2. Dibujar el diagrama: evento → sistema A → sistema B → resultado observable",
                 "3. Escribir un caso de integración + un caso de valor frontera",
                 "4. Ejecutar (automatizado o manual documentado) y registrar el resultado",
                 "5. El proyecto trae un defecto sembrado: si lo encuentran, redacten el ticket",
             ],
             image="Plantilla vacía del diagrama de flujo: cuatro cajas (Evento · Sistema A · Sistema B · Resultado observable) unidas por flechas.",
             nota="Opciones de flujo: recolección + inventario · daño + UI · enemigo + puntaje · fin de nivel + desbloqueo · guardado + carga",
             notes="El defecto sembrado garantiza que todos los grupos ejerciten el ticket aunque sus pruebas pasen (en el borrador, si la prueba pasaba, el objetivo 'registrar errores' quedaba sin evidencia)."),

        dict(title="Entrega y rúbrica", kicker="Evaluación",
             tables=[dict(headers=["Criterio", "%"], widths=[8, 1], size=17,
                          rows=[
                              ["Identificación de los sistemas involucrados", "20"],
                              ["Diseño de los casos (incluye el caso frontera)", "30"],
                              ["Ejecución y registro de resultados", "25"],
                              ["Calidad del ticket", "15"],
                              ["Presentación y reflexión final", "10"],
                          ])],
             nota="Entrega: diagrama del flujo · casos de prueba · evidencia de ejecución · ticket · conclusión breve",
             notes="Rúbrica ajustada: el ticket baja de 20 % a 15 % (Jira es un puente de la Unidad II, no el tema de la clase) y el diseño de casos sube de 25 % a 30 %."),

        # --- Bloques 5 y 6 ---
        dict(title="Puesta en común (20 min)", kicker="≈ 3 min por grupo",
             bullets=[
                 "Flujo elegido y sistemas involucrados",
                 "Caso de prueba y resultado obtenido",
                 "Ticket, si encontraron el defecto",
                 "¿Qué dependencia implicó más riesgo?",
             ],
             pregunta="Los demás grupos: ¿qué costura no se probó?",
             notes="Pedir a los grupos que escuchan una pregunta concreta por presentación."),

        dict(title="Cierre", kicker="Ideas para llevarse",
             bullets=[
                 "La prueba unitaria verifica piezas; la de integración verifica las costuras",
                 "Play Mode no define el nivel de la prueba",
                 "Funcional es un tipo, no un nivel",
                 "Todo caso necesita un resultado esperado verificable",
                 "Una suite en verde no garantiza que no haya defectos",
             ],
             actividad="Ticket de salida: un ejemplo propio de prueba unitaria vs. prueba de integración.",
             notes="10 min. Preguntas extra si sobra tiempo: ¿qué sistema fue más difícil de probar? ¿qué información hizo falta para reproducir el error?"),
    ],
)


# ============================================================================
# CLASE 2 — Introducción a las plataformas
# ============================================================================
CLASE2 = dict(
    footer="Diseño según Plataformas de Juego · Clase 28/09/2026 · Introducción a las plataformas (panorama U-IV a U-VII)",
    slides=[
        dict(type="title", kicker="Panorama · Unidades IV a VII",
             title="Introducción a las plataformas de videojuegos",
             subtitle="Diseño según Plataformas de Juego · Clase teórico-práctica (120 min)",
             footer="Ing. Elsa Daniela Ramírez · FI – UNJu · 2026",
             notes="Portada. Presentar la clase como un MAPA: cada plataforma se desarrolla en su propia unidad (IV móvil, V consolas, VI PC, VII emergentes)."),

        dict(title="Objetivos de la clase", kicker="Al finalizar podrán",
             bullets=[
                 "Reconocer las principales plataformas y sus condiciones de uso",
                 "Comparar sus características técnicas y de interacción",
                 "Explicar cómo la plataforma condiciona controles, interfaz, ritmo y rendimiento",
                 "Proponer la adaptación de un mismo juego a otra plataforma",
                 "Formular pruebas con criterios medibles para una plataforma",
             ],
             notes="Resultados de aprendizaje vinculados: RA01 y RA02 (competencias CGT03 y CGT04)."),

        dict(title="Agenda (120 min)", kicker="Organización",
             tables=[dict(headers=["Bloque", "Minutos", "Qué hacemos"], widths=[3, 1.2, 7], size=16,
                          rows=[
                              ["1. Apertura", "10", "¿Para qué plataforma fue diseñado?"],
                              ["2. Teoría", "25", "Plataforma · PC · consolas · móvil · web · VR/AR · port y crossplay"],
                              ["3. Ficha comparativa", "15", "Su plataforma + una de contraste"],
                              ["Práctica principal", "40", "Adaptar el juego base (nave + asteroides)"],
                              ["4. De la plataforma al testing", "10", "Criterios medibles"],
                              ["5. Presentaciones", "15", "2–3 min por grupo"],
                              ["6. Cierre", "5", "Pregunta integradora con la Clase 1"],
                          ])],
             notes="El borrador original sumaba 140 min. Se recortaron teoría (−5), ficha (−5), práctica (−5) y presentaciones (−5)."),

        dict(title="¿Para qué plataforma fue diseñado?", kicker="Apertura",
             bullets=[
                 "Observen cuatro juegos, sin nombres ni logos",
                 "¿Qué controles se adivinan?",
                 "¿Qué tamaño tienen los textos y los botones?",
                 "¿Cómo está orientada la pantalla?",
                 "¿Cuánta información muestra la interfaz a la vez?",
             ],
             image="Mosaico 2×2 SIN logos ni títulos: A) Monument Valley (móvil, vertical, táctil) · B) Civilization VI (PC, interfaz densa para mouse) · C) Mario Kart 8 Deluxe (Switch) · D) Beat Saber (VR).",
             pregunta="¿En qué se fijaron para decidir? ¿Un mismo juego puede funcionar igual en todas?",
             notes="10 min. Anotar en el pizarrón las pistas que usan: esas pistas son, sin saberlo, los criterios de diseño según plataforma. Respuestas: A móvil, B PC, C Switch (sobremesa y portátil), D VR."),

        dict(title="¿Qué es una plataforma?", kicker="Definición",
             tag="Stardew Valley · PC, Switch y móvil",
             bullets=[
                 "Hardware: procesador, gráficos, memoria, batería",
                 "Sistema operativo y reglas del fabricante",
                 "Dispositivos de entrada",
                 "Contexto de uso: dónde, cuánto tiempo, a qué distancia",
                 "Distribución: tienda, certificación, modelo de negocio",
             ],
             quote="Diseñar según plataforma = decidir controles, interfaz, ritmo y rendimiento a partir de esas condiciones.",
             qsize=17,
             image="La misma escena de Stardew Valley en PC, Switch y móvil, lado a lado (mismo juego, distinto control e interfaz).",
             notes="3 min. Stardew Valley: el mismo juego con otra entrada y otra interfaz, no otro juego."),

        dict(title="PC", kicker="Teoría · Unidad VI",
             tag="Batman: Arkham Knight (2015)",
             bullets=[
                 "Hardware muy variado: de notebooks básicas a equipos de gama alta",
                 "Teclado + mouse, y también gamepad (configuraciones híbridas)",
                 "El jugador espera opciones gráficas, reasignar teclas y varias resoluciones y relaciones de aspecto",
                 "Riesgo: un port que no escala. Arkham Knight fue retirado de la venta en PC en 2015 por su rendimiento",
             ],
             image="Captura de un menú de opciones gráficas de PC con presets (Bajo / Medio / Alto / Ultra) y opciones de resolución.",
             pregunta="¿Qué opciones no pueden faltar en el menú gráfico de un juego de PC?",
             notes="4 min. Ejemplo adicional: Elden Ring salió en PC con la tasa de cuadros limitada a 60 FPS y sin soporte nativo de ultrawide."),

        dict(title="Consolas", kicker="Teoría · Unidad V",
             tag="Baldur's Gate 3 · Xbox Series S",
             bullets=[
                 "Hardware más uniforme que en PC, pero no único: PS5 / PS5 Pro, Xbox Series X / S",
                 "Sobremesa (TV a ~3 m) vs. portátil (Switch, pantalla en la mano)",
                 "Gamepad como entrada principal: todo debe navegarse sin mouse",
                 "Certificación del fabricante antes de publicar (ej.: manejar la desconexión del mando)",
                 "BG3: la pantalla dividida en Series S demoró su lanzamiento en Xbox",
             ],
             image="Esquema: sofá a ~3 m de una TV frente a una Switch en modo portátil en las manos del jugador.",
             pregunta="¿Qué cambia en la interfaz si el jugador está a 3 metros de la pantalla?",
             notes="4 min. [VERIFICAR antes de proyectar el detalle de BG3: Larian atribuyó la demora de la versión de Xbox a la pantalla dividida en Series S; Microsoft terminó flexibilizando el requisito de paridad.] Terminología: 'gamepad' o 'mando' (el programa dice gamepads); 'joystick' es la palanca analógica."),

        dict(title="Dispositivos móviles", kicker="Teoría · Unidad IV",
             tag="Fortnite / CoD Mobile · Vampire Survivors",
             bullets=[
                 "Táctil: sin respuesta física del botón; los dedos tapan la pantalla",
                 "Pantallas muy variadas; muescas y bordes → zonas seguras",
                 "Batería y temperatura: si el equipo se calienta, baja el rendimiento",
                 "Interrupciones: llamadas, notificaciones, cambio de app",
                 "Sesiones que suelen ser más cortas (tendencia, no regla)",
                 "HUD reubicable (Fortnite, CoD Mobile) · Vampire Survivors solo pide moverse",
             ],
             bsize=16,
             image="Captura de un HUD táctil (Fortnite o CoD Mobile) con las zonas de los pulgares superpuestas en semitransparente.",
             pregunta="¿Qué zonas de la pantalla tapan los pulgares?",
             notes="4 min. 'Sesiones cortas' es una tendencia: Genshin Impact tiene sesiones largas en móvil. Vampire Survivors se adapta bien porque el ataque es automático."),

        dict(title="Juegos web", kicker="Teoría · Unidad VII",
             tag="Wordle",
             bullets=[
                 "Se juega desde el navegador, sin instalación",
                 "El tiempo de carga es parte de la experiencia",
                 "Distintos navegadores y dispositivos: teclado, mouse o táctil",
                 "El navegador no reproduce audio hasta que el jugador interactúa",
                 "Memoria y rendimiento más limitados que en una build nativa",
             ],
             image="Un juego corriendo en una pestaña del navegador con la barra de carga y el botón «Click to start».",
             pregunta="¿Por qué tantos juegos web empiezan con «Click to start»?",
             notes="3 min. Respuesta: la política de autoplay de los navegadores bloquea el audio hasta la primera interacción. [VERIFICAR si se menciona: Vampire Survivors nació en HTML5 (Phaser) y luego migró a Unity.]"),

        dict(title="Realidad virtual y aumentada", kicker="Teoría · Unidad VII",
             tag="Half-Life: Alyx · Pokémon GO",
             bullets=[
                 "VR · Visor + controles de movimiento: interacción espacial",
                 "VR · Tasa de cuadros alta y estable: las caídas producen malestar",
                 "VR · La cámara la mueve la cabeza del jugador: el juego no debe moverla por él",
                 "VR · Opciones de confort: teletransporte, desplazamiento continuo, giro por pasos (Alyx)",
                 "AR · Cámara, GPS y sensores: el entorno real es parte del juego (Pokémon GO AR+)",
             ],
             bsize=16,
             image="Captura del menú de opciones de locomoción / confort de Half-Life: Alyx.",
             pregunta="¿Qué mecánica de un juego de PC sería incómoda en VR?",
             notes="4 min. Mencionar en una frase el cloud gaming (Unidad VII): el juego corre en un servidor y la latencia pasa a ser un problema de diseño."),

        dict(title="Port, multiplataforma, crossplay", kicker="Conceptos",
             tables=[dict(headers=["Término", "Qué significa", "Ejemplo"], widths=[2.2, 5, 3.5], size=16,
                          rows=[
                              ["Port", "Llevar un juego existente a otra plataforma", "DOOM (2016) en Switch (Panic Button)"],
                              ["Multiplataforma", "Un mismo juego publicado en varias plataformas", "Stardew Valley"],
                              ["Crossplay", "Jugadores de distintas plataformas en la misma partida", "Fortnite"],
                              ["Progresión cruzada", "El progreso se comparte entre plataformas", "Fortnite (cuenta Epic)"],
                          ])],
             nota="La jugabilidad no se duplica por plataforma: se adaptan la entrada y la interfaz.",
             notes="3 min. DOOM en Switch: el port usa resolución dinámica y 30 FPS para entrar en el hardware."),

        dict(title="Entrada acoplada al gameplay", kicker="Del concepto al código",
             tag="Proyecto nave + asteroides (repositorio)",
             flow=[
                 "Teclado  ·  Táctil  ·  Gamepad",
                 "Intención del jugador: mover · disparar",
                 "Nave: movimiento, disparo, límites",
             ],
             bullets=[
                 "Hoy la nave lee directamente Espacio y flechas",
                 "Para llevarla a móvil habría que modificar la clase de la nave",
                 "Idea: separar QUÉ quiere hacer el jugador de CÓMO lo pide",
             ],
             image="Diagrama en tres capas: dispositivos de entrada arriba → capa de «intención» (mover, disparar) → la nave. Tachar la conexión directa teclado → nave.",
             coderef="Ship.cs 54–75 (lectura de teclas en 61, 66 y 71)",
             pregunta="¿Qué partes de la nave NO deberían cambiar al pasar a móvil?",
             notes="Solo la idea, sin dar implementación. Respuesta: movimiento, disparo, límites y colisiones son jugabilidad común; lo que cambia es de dónde viene la orden."),

        # --- Bloque 3 ---
        dict(title="Ficha comparativa (15 min)", kicker="Actividad",
             tables=[dict(headers=["Aspecto", "PC", "Consola", "Móvil", "Web", "VR"], widths=[2.6, 1.6, 1.6, 1.6, 1.6, 1.6], size=16,
                          rows=[
                              ["Control principal", "", "", "", "", ""],
                              ["Pantalla / distancia", "", "", "", "", ""],
                              ["Sesión típica", "", "", "", "", ""],
                              ["Interfaz", "", "", "", "", ""],
                              ["Rendimiento", "", "", "", "", ""],
                              ["Accesibilidad", "", "", "", "", ""],
                              ["Riesgos de diseño", "", "", "", "", ""],
                          ])],
             actividad="Cada grupo completa SU plataforma + una de contraste.",
             notes="Se agregaron las columnas Web y VR: en el borrador, los grupos que elegían esas plataformas en la práctica no tenían con qué comparar."),

        # --- Práctica ---
        dict(title="Juego base: nave + asteroides", kicker="Práctica principal",
             bullets=[
                 "Control: Espacio para disparar, flechas para moverse",
                 "Límites laterales fijos (±40 unidades), sin mirar la relación de aspecto",
                 "La partida se inicia con un botón pensado para clic",
                 "Partida continua, sin pausa",
             ],
             image="Captura del juego con anotaciones: los límites laterales de la nave, el botón de inicio y las teclas usadas.",
             coderef="Ship.cs 46–47 y 99–115 (límites) · Ship.cs 61–71 (teclas) · Game.cs 54 y 67–80 (inicio)",
             pregunta="¿Qué pasa con los límites en un celular en vertical? ¿Se puede empezar sin mouse en consola?",
             notes="Usar un juego base común hace comparables las presentaciones (en el borrador, cada grupo elegía un género distinto)."),

        dict(title="Consigna: adaptar a una plataforma (40 min)", kicker="Práctica principal",
             bullets=[
                 "1. Control: ¿cómo se mueve y dispara?",
                 "2. Interfaz: botones, textos, zonas seguras",
                 "3. Sesión: duración, pausa, interrupciones",
                 "4. Rendimiento: FPS objetivo y dispositivo de referencia",
                 "5. Pruebas: 5 casos con criterio medible",
                 "  Opcionales: accesibilidad, guardado, distribución",
             ],
             image="Ícono o foto de cada plataforma posible (PC, consola, móvil, web, VR) para que cada grupo elija la suya.",
             nota="Entrega: ficha · propuesta de adaptación · 5 pruebas medibles · 1 ticket de bug posible",
             notes="Se redujo de 10 aspectos a 5 obligatorios y de 8 pruebas a 5: con 40 minutos no alcanza para más con calidad."),

        # --- Bloque 4 ---
        dict(title="De la plataforma al testing: criterios medibles", kicker="Unidad II → plataformas",
             tag="Steam Deck Verified",
             tables=[dict(headers=["Vago (no se puede verificar)", "Medible"], widths=[1, 1.5], size=14,
                          rows=[
                              ["El rendimiento es estable", "≥ 30 FPS durante 10 min en [dispositivo de referencia]"],
                              ["La batería no se consume de más", "≤ N % de batería en 30 min de juego en [dispositivo]"],
                              ["El texto es legible", "Texto ≥ N px a 1080p, según la guía de la plataforma"],
                              ["Se puede pausar en una llamada", "Al pasar a segundo plano, el juego se pausa y conserva el estado"],
                              ["Los menús funcionan con mando", "Todas las pantallas se recorren y confirman solo con el gamepad"],
                          ])],
             image="Insignia «Steam Deck Verified» junto a sus cuatro criterios: entrada, continuidad, pantalla y soporte del sistema.",
             actividad="Reescriban 2 pruebas vagas de su lista como pruebas medibles.",
             notes="10 min. Steam Deck Verified evalúa entrada, continuidad (sin launchers que exijan mouse, etc.), pantalla (legibilidad del texto) y soporte del sistema. Conecta con 'criterios de aceptación' de la Unidad II."),

        # --- Bloques 5 y 6 ---
        dict(title="Presentaciones (15 min)", kicker="2–3 min por grupo",
             bullets=[
                 "Plataforma elegida",
                 "Cambios principales al juego base",
                 "Riesgos de diseño",
                 "Pruebas con criterio medible",
                 "Un bug posible propio de esa plataforma",
             ],
             pregunta="Los demás grupos: ¿qué riesgo no se consideró?",
             notes="Pedir una pregunta concreta por presentación."),

        dict(title="Cierre", kicker="Idea central",
             quote="La plataforma no es solo el lugar donde se ejecuta un juego: condiciona sus controles, su interfaz, su ritmo, su accesibilidad, su rendimiento y las pruebas necesarias.",
             qsize=20,
             image="El diagrama de flujo de la Clase 1 (daño → vida → barra) con íconos de PC, consola y móvil sobre las costuras.",
             pregunta="¿Cómo cambiaría la prueba de integración de la Clase 1 en PC, consola o móvil?",
             notes="5 min. Ejemplo de respuesta: no se prueba igual un menú con mouse que uno táctil o con gamepad; en móvil hay que sumar la interrupción por llamada al flujo de daño → vida → barra."),
    ],
)


if __name__ == "__main__":
    build(CLASE1, "Clase1-Testing-Integracion.pptx")
    build(CLASE2, "Clase2-Plataformas.pptx")
