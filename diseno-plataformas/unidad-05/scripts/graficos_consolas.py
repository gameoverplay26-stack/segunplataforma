"""Gráficos del tema "Diseño según plataforma de consolas" (Unidad 5).

Lee los CSV de ../datos (cada fila con su fuente en datos/fuentes.md) y escribe PNG en ../imagenes.
Uso (desde diseno-plataformas/unidad-05/):  python scripts/graficos_consolas.py [--slides]
--slides escribe en ../imagenes/slides una versión para las diapositivas: sin título ni pie
(los pone la slide), con letra más grande y sin márgenes sobrantes.
Requiere: matplotlib.
"""
import csv
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

BASE = Path(__file__).resolve().parent.parent
DATOS = BASE / "datos"
SLIDES = "--slides" in sys.argv
SALIDA = BASE / "imagenes" / ("slides" if SLIDES else "")
SALIDA.mkdir(parents=True, exist_ok=True)

# Paleta de referencia validada (skill dataviz): slots 1-3, que pasan todos los pares CVD.
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK_2 = "#52514e"
GRID = "#e4e3df"
COLOR = {"Sony": "#2a78d6", "Nintendo": "#eb6834", "Microsoft": "#1baf7a"}

if SLIDES:
    # Lienzo más chico con la misma letra: al escalarlo a la slide, el texto se ve más grande.
    _subplots = plt.subplots

    def _subplots_slides(*args, figsize=(10, 6), **kwargs):
        return _subplots(*args, figsize=(figsize[0] * 0.72, figsize[1] * 0.72), **kwargs)

    plt.subplots = _subplots_slides

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 12 if SLIDES else 10,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "axes.edgecolor": GRID,
    "axes.labelcolor": INK_2,
    "xtick.color": INK_2,
    "ytick.color": INK_2,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titlesize": 13,
    "axes.titleweight": "bold",
    "axes.titlecolor": INK,
    "axes.titlelocation": "left",
})


def leer(nombre):
    with open(DATOS / nombre, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pie(fig, texto):
    if SLIDES:
        return
    fig.text(0.01, 0.01, texto, fontsize=7.5, color=INK_2, ha="left", va="bottom")


def titulo(fig, texto, subtitulo=None):
    if SLIDES:
        return
    fig.text(0.01, 0.965, texto, fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
    if subtitulo:
        fig.text(0.01, 0.915, subtitulo, fontsize=9, color=INK_2, ha="left", va="top")


def guardar(fig, nombre):
    if SLIDES:
        fig.savefig(SALIDA / nombre, dpi=200, bbox_inches="tight", pad_inches=0.15)
    else:
        fig.savefig(SALIDA / nombre, dpi=160)
    plt.close(fig)
    print("  ", nombre)


def ranking_ventas():
    filas = sorted(leer("ventas-hardware.csv"), key=lambda r: float(r["millones"]))
    fig, ax = plt.subplots(figsize=(10, 7.2))
    fig.subplots_adjust(left=0.24, right=0.93, top=0.86, bottom=0.1)
    for i, r in enumerate(filas):
        v = float(r["millones"])
        vigente = r["en_venta"] == "si"
        ax.barh(i, v, height=0.72, color=COLOR[r["fabricante"]],
                hatch="///" if vigente else None, edgecolor=SURFACE, linewidth=0)
        etiqueta = f"{v:.1f}" + ("  (en venta)" if vigente else "")
        ax.text(v + 1.5, i, etiqueta, va="center", fontsize=8.5, color=INK)
    ax.set_yticks(range(len(filas)), [f"{r['consola']} ({r['lanzamiento'][:4]})" for r in filas])
    ax.set_xlabel("Millones de unidades despachadas (sell-in)")
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.set_xlim(0, 180)
    titulo(fig, "Consolas Sony y Nintendo: unidades vendidas en toda su vida", "Rayado = todavía en venta (cifra que sigue creciendo). Microsoft no publica unidades de Xbox One ni Series X|S.")
    leyenda = [plt.Rectangle((0, 0), 1, 1, color=COLOR[k]) for k in ("Sony", "Nintendo")]
    ax.legend(leyenda, ["Sony", "Nintendo"], loc="lower right", frameon=False)
    pie(fig, "Fuentes: Nintendo IR, Dedicated Video Game Sales Units (30-jun-2026); SIE, Business Data & Sales (cifras \"more than\", fecha de cada dato en datos/ventas-hardware.csv).")
    guardar(fig, "01-ranking-ventas-consolas.png")


def histograma_ventas():
    valores = [float(r["millones"]) for r in leer("ventas-hardware.csv") if r["en_venta"] == "no"]
    fig, ax = plt.subplots(figsize=(9, 5))
    fig.subplots_adjust(left=0.09, right=0.97, top=0.83, bottom=0.17)
    bins = list(range(0, 200, 25))
    n, _, barras = ax.hist(valores, bins=bins, color=INK_2, edgecolor=SURFACE, linewidth=2)
    for b, c in zip(barras, n):
        if c:
            ax.text(b.get_x() + b.get_width() / 2, c + 0.08, f"{int(c)}", ha="center", fontsize=9, color=INK)
    ax.set_xticks(bins)
    ax.set_xlabel("Ventas de vida (millones de unidades), en intervalos de 25 M")
    ax.set_ylabel("Cantidad de consolas")
    ax.yaxis.get_major_locator().set_params(integer=True)
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    titulo(fig, "Histograma: ¿cuántas consolas vendieron cuánto?",
           f"{len(valores)} consolas ya discontinuadas de Sony y Nintendo. La mayoría queda por debajo de 125 M; superar 150 M es excepcional.")
    pie(fig, "Mismos datos que el ranking, sin las consolas en venta. Un histograma cuenta casos por intervalo; no es un gráfico de barras por consola.")
    guardar(fig, "02-histograma-ventas.png")


def ciclo_de_vida():
    filas = leer("ventas-anuales.csv")
    fig, ax = plt.subplots(figsize=(10, 5.4))
    fig.subplots_adjust(left=0.08, right=0.97, top=0.83, bottom=0.17)
    series = [("Nintendo Switch", COLOR["Nintendo"], "o", "-"),
              ("PlayStation 5", COLOR["Sony"], "s", "-"),
              ("Nintendo Switch 2", COLOR["Nintendo"], "D", "--")]
    for nombre, color, marca, estilo in series:
        pts = [(int(r["anio_de_vida"]), float(r["millones"])) for r in filas if r["consola"] == nombre]
        xs, ys = zip(*pts)
        ax.plot(xs, ys, estilo, color=color, linewidth=2, marker=marca, markersize=7,
                markeredgecolor=SURFACE, markeredgewidth=2, label=nombre)
        x_fin, y_fin = pts[-1]
        ax.annotate(nombre, (x_fin, y_fin), xytext=(8, 0 if nombre != "Nintendo Switch 2" else 6),
                    textcoords="offset points", fontsize=9, color=INK, va="center")
    pico = max((float(r["millones"]), int(r["anio_de_vida"])) for r in filas if r["consola"] == "Nintendo Switch")
    ax.annotate(f"Pico: {pico[0]:.1f} M\n(abr-2020 a mar-2021)", (pico[1], pico[0]), xytext=(18, -6),
                textcoords="offset points", fontsize=8.5, color=INK_2)
    ax.set_xticks(range(1, 11), [f"{i}.º" for i in range(1, 11)])
    ax.set_xlim(0.6, 11.2)
    ax.set_xlabel("Ejercicio fiscal desde el lanzamiento (el 1.º es parcial; ejercicios de abril a marzo)")
    ax.set_ylabel("Millones de unidades por ejercicio")
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.legend(frameon=False, loc="upper right")
    titulo(fig, "Ciclo de vida: ventas por ejercicio fiscal", "Una consola sube, llega a un pico y decae. Switch 2: 19,9 M en su primer ejercicio (10 meses); Switch: 2,7 M en el primero (1 mes) y 15,1 M en el segundo.")
    pie(fig, "Fuentes: Nintendo IR (planilla por región, 31-mar-2026); Sony vía 20-F y Game Developer (8-may-2026). PS5 FY2023 = 93,7 M menos los demás ejercicios.")
    guardar(fig, "03-ciclo-de-vida-anual.png")


def regiones_nintendo():
    filas = leer("regiones-nintendo.csv")
    fig, ax = plt.subplots(figsize=(10, 5.2))
    fig.subplots_adjust(left=0.2, right=0.97, top=0.8, bottom=0.12)
    partes = [("japon", "Japón", "#1a1a19"), ("america", "América", COLOR["Nintendo"]),
              ("europa_y_resto", "Europa y resto", "#f4b393")]
    for i, r in enumerate(reversed(filas)):
        total = sum(float(r[k]) for k, _, _ in partes)
        izq = 0
        for k, _, color in partes:
            pct = 100 * float(r[k]) / total
            ax.barh(i, pct, left=izq, height=0.7, color=color, edgecolor=SURFACE, linewidth=2)
            if pct >= 9:
                ax.text(izq + pct / 2, i, f"{pct:.0f} %", ha="center", va="center", fontsize=8.5,
                        color="white" if color != "#f4b393" else INK)
            izq += pct
    ax.set_yticks(range(len(filas)), [r["consola"] for r in reversed(filas)])
    ax.set_xlim(0, 100)
    ax.set_xlabel("% de las unidades de hardware vendidas")
    ax.legend([plt.Rectangle((0, 0), 1, 1, color=c) for _, _, c in partes], [n for _, n, _ in partes],
              ncol=3, frameon=False, loc="lower left", bbox_to_anchor=(0, 1.0))
    titulo(fig, "Dónde se venden las consolas de Nintendo")
    pie(fig, "Fuente: Nintendo IR, Consolidated Sales Transition by Region (al 31-mar-2026; Switch 2 = primer ejercicio). Antes de Switch, Nintendo no separa Europa de \"otros\".")
    guardar(fig, "04-regiones-nintendo.png")


def precios():
    filas = leer("precios-usd.csv")
    fig, ax = plt.subplots(figsize=(9.5, 4.8 if SLIDES else 3.8))
    fig.subplots_adjust(left=0.22, right=0.95, top=0.76, bottom=0.2)
    for i, r in enumerate(filas):
        a, b = float(r["precio_lanzamiento"]), float(r["precio_actual"])
        color = COLOR["Sony"] if "PS5" in r["consola"] else COLOR["Nintendo"]
        ax.plot([a, b], [i, i], color=GRID, linewidth=6, solid_capstyle="round", zorder=1)
        ax.scatter([a], [i], s=70, color=SURFACE, edgecolor=color, linewidth=2, zorder=2)
        ax.scatter([b], [i], s=70, color=color, edgecolor=SURFACE, linewidth=2, zorder=3)
        ax.text(a - 12, i, f"{a:,.0f}", ha="right", va="center", fontsize=9, color=INK_2)
        ax.text(b + 12, i, f"{b:,.0f}  (+{100 * (b - a) / a:.0f} %)", ha="left", va="center", fontsize=9, color=INK)
    ax.set_yticks(range(len(filas)), [r["consola"] for r in filas])
    ax.set_ylim(-0.6, len(filas) - 0.4)
    ax.set_xlim(330, 760)
    ax.set_xlabel("Precio sugerido en EE. UU. (USD)")
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    titulo(fig, "Las consolas ya no bajan de precio: suben", "Círculo vacío = precio de lanzamiento; lleno = precio vigente en oct-2026. Causa declarada: costo de memoria y almacenamiento.")
    pie(fig, "Fuentes: PlayStation Blog (16-sep-2020 y 27-mar-2026); Nintendo, Notice Regarding Price Revisions (8-may-2026).")
    guardar(fig, "05-precios-lanzamiento-vs-2026.png")


def linea_de_tiempo():
    hitos = {
        "Nintendo": [(1983.5, "Famicom/NES"), (1989.3, "Game Boy"), (1990.9, "Super Famicom"), (1996.5, "N64"),
                     (2001.7, "GameCube"), (2004.9, "DS"), (2006.9, "Wii"), (2011.2, "3DS"), (2012.9, "Wii U"),
                     (2017.2, "Switch"), (2025.4, "Switch 2")],
        "Sony": [(1994.9, "PlayStation"), (2000.2, "PS2"), (2004.9, "PSP"), (2006.9, "PS3"), (2011.9, "PS Vita"),
                 (2013.9, "PS4"), (2016.9, "PS4 Pro"), (2020.9, "PS5"), (2024.85, "PS5 Pro")],
        "Microsoft": [(2001.9, "Xbox"), (2002.9, "Xbox Live"), (2005.9, "Xbox 360"), (2013.9, "Xbox One"),
                      (2017.85, "One X"), (2020.9, "Series X|S")],
    }
    fig, ax = plt.subplots(figsize=(12, 4.6))
    fig.subplots_adjust(left=0.1, right=0.98, top=0.8, bottom=0.14)
    filas = ["Microsoft", "Sony", "Nintendo"]
    for y, fab in enumerate(filas):
        ax.axhline(y, color=GRID, linewidth=1, zorder=0)
        for k, (x, nombre) in enumerate(hitos[fab]):
            ax.scatter(x, y, s=60, color=COLOR[fab], edgecolor=SURFACE, linewidth=2, zorder=3)
            dy = 0.22 if k % 2 == 0 else -0.3
            ax.text(x, y + dy, nombre, ha="center", va="center", fontsize=8, color=INK)
    for x0, x1, nombre in [(1983, 1984, "Crisis de 1983 (EE. UU.)"), (2020.2, 2021.2, "Pandemia")]:
        ax.axvspan(x0, x1, color=GRID, alpha=0.6, zorder=0)
        ax.text((x0 + x1) / 2, 2.62, nombre, ha="center", fontsize=8, color=INK_2)
    ax.axvline(2026.8, color=INK_2, linewidth=1, linestyle=":")
    ax.text(2026.8, -0.62, "hoy", ha="center", fontsize=8, color=INK_2)
    ax.set_yticks(range(3), filas)
    ax.set_ylim(-0.75, 2.8)
    ax.set_xlim(1981, 2028)
    ax.set_xticks(range(1985, 2030, 5))
    for s in ("left", "bottom"):
        ax.spines[s].set_visible(False)
    ax.tick_params(length=0)
    titulo(fig, "Cuatro décadas de consolas: lanzamientos de los tres fabricantes")
    pie(fig, "Fechas del primer lanzamiento mundial. Fuentes: Nintendo IR (planilla por región), SIE Expanded company timeline, Microsoft Facts about Microsoft.")
    guardar(fig, "06-linea-de-tiempo.png")


if __name__ == "__main__":
    print("Generando gráficos en", SALIDA)
    ranking_ventas()
    histograma_ventas()
    ciclo_de_vida()
    regiones_nintendo()
    precios()
    linea_de_tiempo()
