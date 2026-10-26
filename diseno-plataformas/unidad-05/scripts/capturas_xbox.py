# -*- coding: utf-8 -*-
"""
Imagenes del Anexo B (Xbox en Developer Mode, paso a paso) de la Unidad 5.

Escribe PNG en ../imagenes/xbox/, que 04-diapositivas.md usa con "captura:".
Hay dos clases de imagen, y cada una lo dice en una franja al pie:
- PC (pc-*.png): salen de datos reales. La consola de PowerShell reproduce lineas del log de la
  ultima corrida de generar_builds_xbox.ps1, y el arbol de carpetas recorre el paquete generado.
- Consola y Device Portal (xb-*.png): RECREACIONES ESQUEMATICAS. Sin una consola en Developer Mode
  no hay capturas reales; se dibujan los elementos que nombra GUIA-XBOX-DOCENTE.md, sin logos.
  Las etiquetas exactas pueden variar con la version del sistema de la consola.

Capturas reales: si existe imagenes/xbox/reales/<nombre>.png, se copia esa en lugar de dibujar
la recreacion (por ejemplo, una captura de Device Portal -> Media capture).

Uso (desde diseno-plataformas/unidad-05/):  python scripts/capturas_xbox.py
Despues: python scripts/build_decks.py --version 3
Requiere: Pillow.
"""
import os
import re
import shutil
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).resolve().parent.parent
REPO = BASE.parent.parent
SALIDA = BASE / "imagenes" / "xbox"
REALES = SALIDA / "reales"
LOG = REPO / "proyectos-unity" / "Tools-Xbox" / "ultima-corrida.log"
PAQUETES = REPO / "proyectos-unity" / "Asteroides" / "asteroide-final" / "Builds" / "Xbox-Paquete"

W, H = 1280, 720
BAND = 44  # franja inferior con el rotulo

# Paleta del deck (unidad-04/scripts/build_decks.py)
NAVY = "#1F2A44"
TEAL = "#0D9488"
AMBER = "#D97706"
SLATE = "#1F2937"
MUTED = "#6B7280"
LIGHT = "#F3F4F6"
GRID = "#E5E7EB"
WHITE = "#FFFFFF"
# Consola (tema oscuro generico, no la marca)
TV_BG = "#16181D"
TV_PANEL = "#23262E"
TV_TILE = "#2F333D"
TV_TEXT = "#E5E7EB"
TV_MUTED = "#9CA3AF"

FONTS = Path(os.environ.get("WINDIR", r"C:\Windows")) / "Fonts"
IP = "192.168.0.50"  # IP de ejemplo; la real la muestra Dev Home


def font(size, bold=False, mono=False):
    names = (["consolab.ttf"] if bold else ["consola.ttf"]) if mono else \
        (["segoeuib.ttf", "calibrib.ttf"] if bold else ["segoeui.ttf", "calibri.ttf"])
    for n in names:
        if (FONTS / n).exists():
            return ImageFont.truetype(str(FONTS / n), size)
    return ImageFont.load_default(size)


# --- Primitivas ---------------------------------------------------------------
def lienzo(bg):
    img = Image.new("RGB", (W, H), bg)
    return img, ImageDraw.Draw(img)


def texto(d, xy, s, size=26, color=SLATE, bold=False, mono=False, anchor="la"):
    d.text(xy, s, font=font(size, bold, mono), fill=color, anchor=anchor)


def boton(d, box, s, bg=TEAL, fg=WHITE, size=26, borde=None):
    d.rounded_rectangle(box, radius=10, fill=bg, outline=borde, width=3 if borde else 0)
    cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
    texto(d, (cx, cy), s, size, fg, bold=True, anchor="mm")


def resaltar(d, box, n):
    """Recuadro ambar con un numero que coincide con el paso de la slide."""
    x0, y0, x1, y1 = box
    d.rounded_rectangle((x0 - 8, y0 - 8, x1 + 8, y1 + 8), radius=14, outline=AMBER, width=5)
    r = 22
    cx, cy = x0 - 8, y0 - 8
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=AMBER)
    texto(d, (cx, cy), str(n), 26, WHITE, bold=True, anchor="mm")


def casilla(d, x, y, marcada, s, color=TV_TEXT, size=26):
    d.rectangle((x, y, x + 30, y + 30), outline=color, width=3, fill=TEAL if marcada else None)
    if marcada:
        d.line((x + 6, y + 16, x + 13, y + 23, x + 25, y + 7), fill=WHITE, width=4)
    texto(d, (x + 46, y + 15), s, size, color, anchor="lm")


def rotulo(d, s, real=False):
    d.rectangle((0, H - BAND, W, H), fill=TEAL if real else AMBER)
    texto(d, (24, H - BAND / 2), s, 22, WHITE, bold=True, anchor="lm")


def recreacion(d, que):
    rotulo(d, "RECREACIÓN ESQUEMÁTICA · %s · no es una captura real" % que)


def navegador(url, titulo_pestana, inseguro=False):
    """Ventana de navegador generica: pestaña, barra de direccion y pagina blanca."""
    img, d = lienzo("#DADCE0")
    d.rounded_rectangle((16, 10, 420, 60), radius=10, fill=WHITE)
    texto(d, (36, 35), titulo_pestana, 22, SLATE, anchor="lm")
    d.rectangle((0, 56, W, 116), fill=WHITE)
    d.rounded_rectangle((90, 66, W - 40, 106), radius=20, fill=LIGHT)
    for i, c in enumerate(("‹", "›")):
        texto(d, (28 + i * 30, 86), c, 36, MUTED, anchor="mm")
    if inseguro:
        texto(d, (110, 86), "No es seguro", 22, "#B91C1C", bold=True, anchor="lm")
        texto(d, (262, 86), url, 22, SLATE, anchor="lm")
    else:
        texto(d, (110, 86), url, 22, SLATE, anchor="lm")
    d.rectangle((0, 116, W, H - BAND), fill=WHITE)
    d.line((0, 116, W, 116), fill=GRID, width=2)
    return img, d


def portal(seccion):
    """Device Portal: barra lateral con las secciones y area de contenido."""
    img, d = navegador("https://%s:11443/" % IP, "Xbox Device Portal", inseguro=True)
    d.rectangle((0, 117, 270, H - BAND), fill=NAVY)
    texto(d, (24, 150), "Device Portal", 28, WHITE, bold=True, anchor="lm")
    items = ("Home", "Media capture", "Performance", "Settings", "Network", "Processes")
    for i, it in enumerate(items):
        y = 200 + i * 56
        if it == seccion:
            d.rectangle((0, y - 24, 270, y + 24), fill=TEAL)
        texto(d, (32, y), it, 24, WHITE, bold=it == seccion, anchor="lm")
    return img, d


def tv(titulo):
    """Pantalla de la consola (Dev Home y apps del sistema), con la IP arriba a la izquierda."""
    img, d = lienzo(TV_BG)
    texto(d, (40, 40), titulo, 34, TV_TEXT, bold=True)
    return img, d


def guardar(img, nombre):
    img.save(SALIDA / nombre, optimize=True)


# --- Consola y Device Portal (recreaciones) ---------------------------------
def xb01_registro():
    img, d = navegador("storedeveloper.microsoft.com", "Cuenta de desarrollador")
    texto(d, (80, 170), "Abrí una cuenta de desarrollador", 40, SLATE, bold=True)
    texto(d, (80, 230), "Para publicar en la tienda o, como acá, para activar una consola.", 26, MUTED)
    boton(d, (80, 300, 470, 370), "Get started for free")
    resaltar(d, (80, 300, 470, 370), 1)
    d.rounded_rectangle((80, 420, 600, 600), radius=14, outline=TEAL, width=4, fill="#E6F4F2")
    texto(d, (110, 455), "Individual developer", 30, SLATE, bold=True)
    texto(d, (110, 500), "Persona, sin costo de registro", 24, MUTED)
    texto(d, (110, 540), "Verificación: documento + selfie", 24, MUTED)
    resaltar(d, (80, 420, 600, 600), 2)
    d.rounded_rectangle((660, 420, 1180, 600), radius=14, outline=GRID, width=3)
    texto(d, (690, 455), "Company", 30, MUTED, bold=True)
    texto(d, (690, 500), "Empresa: no hace falta", 24, MUTED)
    recreacion(d, "registro web")
    guardar(img, "xb-01-registro.png")


def xb02_codigo():
    img, d = tv("Xbox Dev Mode")
    texto(d, (40, 110), "App gratuita de la tienda de la consola", 26, TV_MUTED)
    d.rounded_rectangle((140, 190, 1140, 560), radius=18, fill=TV_PANEL)
    texto(d, (640, 250), "Código de activación", 32, TV_TEXT, anchor="mm")
    texto(d, (640, 345), "A B C D 1 2 3", 84, WHITE, bold=True, mono=True, anchor="mm")
    resaltar(d, (330, 300, 950, 395), 1)
    texto(d, (640, 450), "Ingresalo en partner.microsoft.com/xboxconfig/devices", 26, TV_MUTED, anchor="mm")
    texto(d, (640, 510), "(código de ejemplo: el real lo genera la consola)", 22, TV_MUTED, anchor="mm")
    recreacion(d, "pantalla de la consola")
    guardar(img, "xb-02-codigo.png")


def xb03_activar():
    img, d = navegador("partner.microsoft.com/xboxconfig/devices", "Partner Center")
    texto(d, (80, 170), "Xbox devices", 40, SLATE, bold=True)
    texto(d, (80, 230), "Activar una consola con el código que muestra Xbox Dev Mode", 26, MUTED)
    texto(d, (80, 300), "Código de activación", 24, SLATE, bold=True)
    d.rounded_rectangle((80, 335, 620, 395), radius=8, outline=MUTED, width=2)
    texto(d, (100, 365), "ABCD123", 30, SLATE, mono=True, anchor="lm")
    resaltar(d, (80, 335, 620, 395), 1)
    boton(d, (80, 450, 440, 515), "Agree and activate")
    resaltar(d, (80, 450, 440, 515), 2)
    d.rounded_rectangle((700, 300, 1200, 520), radius=14, fill=LIGHT)
    texto(d, (730, 335), "Consolas activadas", 26, SLATE, bold=True)
    texto(d, (730, 385), "Cada cuenta tiene un número", 24, MUTED)
    texto(d, (730, 420), "limitado de activaciones.", 24, MUTED)
    texto(d, (730, 470), "Desde acá también se desactivan.", 24, MUTED)
    recreacion(d, "Partner Center")
    guardar(img, "xb-03-activar.png")


def xb04_switch():
    img, d = tv("Xbox Dev Mode")
    d.rounded_rectangle((140, 150, 1140, 600), radius=18, fill=TV_PANEL)
    texto(d, (640, 220), "Activación completa", 36, TV_TEXT, bold=True, anchor="mm")
    texto(d, (640, 290), "La consola va a reiniciar en Developer Mode.", 28, TV_MUTED, anchor="mm")
    texto(d, (640, 335), "El reinicio tarda más de lo normal.", 28, TV_MUTED, anchor="mm")
    boton(d, (420, 420, 860, 500), "Switch and restart", borde=WHITE)
    resaltar(d, (420, 420, 860, 500), 1)
    recreacion(d, "pantalla de la consola")
    guardar(img, "xb-04-switch.png")


def dev_home_base():
    """Dev Home muestra la IP arriba a la izquierda (GUIA-XBOX-DOCENTE.md, paso 3.2)."""
    img, d = lienzo(TV_BG)
    texto(d, (40, 40), "IP: %s" % IP, 30, WHITE, bold=True)
    texto(d, (W - 40, 40), "Dev Home", 34, TV_TEXT, bold=True, anchor="ra")
    tabs = ("Home", "Settings", "Quick Actions")
    for i, t in enumerate(tabs):
        texto(d, (40 + i * 200, 110), t, 26, TEAL if i == 0 else TV_MUTED, bold=i == 0)
    return img, d


def xb05_dev_home():
    img, d = dev_home_base()
    resaltar(d, (36, 36, 330, 78), 2)
    d.rounded_rectangle((40, 170, 620, 430), radius=14, fill=TV_TILE)
    texto(d, (70, 200), "Usuario", 28, TV_TEXT, bold=True)
    d.ellipse((70, 260, 150, 340), fill=TEAL)
    texto(d, (110, 300), "D", 40, WHITE, bold=True, anchor="mm")
    texto(d, (175, 285), "docente@outlook.com", 26, TV_TEXT)
    texto(d, (175, 325), "Sesión iniciada", 24, "#86EFAC")
    resaltar(d, (70, 255, 590, 350), 1)
    d.rounded_rectangle((660, 170, 1240, 430), radius=14, fill=TV_TILE)
    texto(d, (690, 200), "Remote Access", 28, TV_TEXT, bold=True)
    texto(d, (690, 260), "Device Portal: apagado", 24, TV_MUTED)
    boton(d, (690, 330, 1100, 395), "Remote Access Settings", bg=TV_PANEL, borde=TV_MUTED, size=24)
    texto(d, (40, 480), "Sin usuario con sesión iniciada, instalar falla con 0x87e10008.", 26, TV_MUTED)
    texto(d, (40, 525), "La IP de arriba es la que se usa desde la PC.", 26, TV_MUTED)
    recreacion(d, "Dev Home en la consola")
    guardar(img, "xb-05-dev-home.png")


def xb06_remote_access():
    img, d = tv("Remote Access Settings")
    d.rounded_rectangle((40, 110, 1240, 640), radius=18, fill=TV_PANEL)
    casilla(d, 90, 160, True, "Enable Xbox Device Portal", size=30)
    resaltar(d, (84, 152, 520, 198), 1)
    texto(d, (90, 250), "Authentication", 28, TV_TEXT, bold=True)
    boton(d, (90, 300, 560, 365), "Set username and password", bg=TV_TILE, borde=TV_MUTED, size=24)
    resaltar(d, (90, 300, 560, 365), 2)
    texto(d, (620, 333), "Un usuario y una clave solo para esto", 24, TV_MUTED, anchor="lm")
    texto(d, (90, 450), "Device Portal:", 28, TV_TEXT, bold=True)
    texto(d, (90, 500), "https://%s:11443" % IP, 40, WHITE, bold=True, mono=True)
    resaltar(d, (90, 495, 700, 545), 3)
    texto(d, (740, 520), "anotar esta URL", 24, TV_MUTED, anchor="lm")
    recreacion(d, "Dev Home en la consola")
    guardar(img, "xb-06-remote-access.png")


def xb07_certificado():
    img, d = navegador("https://%s:11443" % IP, "Error de privacidad", inseguro=True)
    resaltar(d, (100, 70, 600, 102), 1)
    d.polygon(((150, 185), (100, 270), (200, 270)), fill="#B91C1C")
    texto(d, (150, 245), "!", 44, WHITE, bold=True, anchor="mm")
    texto(d, (230, 195), "La conexión no es privada", 40, SLATE, bold=True)
    texto(d, (230, 255), "La consola usa un certificado propio: es esperable.", 26, MUTED)
    boton(d, (230, 330, 470, 390), "Avanzado", bg=WHITE, fg=SLATE, borde=MUTED, size=24)
    resaltar(d, (230, 330, 470, 390), 2)
    d.rounded_rectangle((230, 430, 1180, 560), radius=10, fill=LIGHT)
    texto(d, (260, 465), "Este servidor no pudo demostrar que es %s." % IP, 24, MUTED)
    texto(d, (260, 515), "Continuar a %s (no seguro)" % IP, 26, "#1D4ED8", bold=True)
    resaltar(d, (255, 512, 720, 556), 3)
    recreacion(d, "aviso del navegador")
    guardar(img, "xb-07-certificado.png")


def xb08_preferencias():
    img, d = portal("Settings")
    texto(d, (310, 150), "Settings", 36, SLATE, bold=True)
    texto(d, (310, 220), "Preference Settings", 28, SLATE, bold=True)
    d.rounded_rectangle((310, 260, 1240, 470), radius=12, fill=LIGHT)
    casilla(d, 340, 290, True, "Treat UWP apps as games by default", SLATE, 28)
    resaltar(d, (334, 282, 860, 328), 1)
    texto(d, (340, 370), "Sin tildar: el paquete corre como app, con 1 GB de memoria.", 24, MUTED)
    texto(d, (340, 410), "Tildado: corre como juego, con 5 GB y la GPU completa.", 24, MUTED)
    texto(d, (310, 520), "Se hace una sola vez, antes de instalar.", 26, SLATE)
    recreacion(d, "Device Portal")
    guardar(img, "xb-08-preferencias.png")


def lista_juegos(d, y, filas, menu=False):
    d.rounded_rectangle((310, y, 1240, y + 60 + 56 * len(filas)), radius=12, outline=GRID, width=2)
    for i, c in enumerate(("Nombre", "Estado")):
        texto(d, (340 + i * 560, y + 30), c, 22, MUTED, bold=True, anchor="lm")
    for i, (nombre, estado) in enumerate(filas):
        ry = y + 60 + 56 * i
        d.line((310, ry, 1240, ry), fill=GRID, width=2)
        texto(d, (340, ry + 28), nombre, 24, SLATE, anchor="lm")
        texto(d, (900, ry + 28), estado, 24, MUTED, anchor="lm")
        texto(d, (1180, ry + 28), "Actions", 22, TEAL, bold=True, anchor="rm")


def xb10_add():
    img, d = portal("Home")
    texto(d, (310, 150), "My games & apps", 36, SLATE, bold=True)
    boton(d, (1060, 135, 1240, 190), "Add", size=26)
    resaltar(d, (1060, 135, 1240, 190), 1)
    lista_juegos(d, 230, [("Xbox Dev Mode", "Sistema")])
    texto(d, (310, 420), "Add abre el asistente para instalar un paquete desde la PC.", 26, MUTED)
    recreacion(d, "Device Portal")
    guardar(img, "xb-10-add.png")


def asistente(paso, titulo):
    img, d = portal("Home")
    d.rectangle((270, 117, W, H - BAND), fill="#6B7280")
    d.rounded_rectangle((330, 150, 1220, 640), radius=16, fill=WHITE)
    texto(d, (370, 190), "Instalar un paquete · paso %d de 3" % paso, 22, MUTED)
    texto(d, (370, 230), titulo, 32, SLATE, bold=True)
    return img, d


def xb11_msix():
    img, d = asistente(1, "Elegir el paquete")
    boton(d, (370, 300, 600, 360), "Choose file", bg=WHITE, fg=SLATE, borde=MUTED, size=24)
    resaltar(d, (370, 300, 600, 360), 1)
    texto(d, (630, 330), "Asteroides (original)_1.0.0.0_x64_Master.msix", 22, SLATE, anchor="lm")
    texto(d, (370, 420), "Es el .msix de la carpeta Builds/Xbox-Paquete/<Nombre>_…_Test/.", 24, MUTED)
    texto(d, (370, 460), "No elegir los .appx de Dependencies: eso va en el paso 2.", 24, MUTED)
    boton(d, (1000, 560, 1180, 615), "Next", size=24)
    resaltar(d, (1000, 560, 1180, 615), 2)
    recreacion(d, "Device Portal")
    guardar(img, "xb-11-msix.png")


def xb12_dependencias():
    img, d = asistente(2, "Dependencias y certificado")
    texto(d, (370, 300), "Dependencia (obligatoria la primera vez):", 24, SLATE, bold=True)
    boton(d, (370, 340, 600, 395), "Choose file", bg=WHITE, fg=SLATE, borde=MUTED, size=24)
    texto(d, (630, 367), "Dependencies/x64/Microsoft.VCLibs.x64.14.00.appx", 22, SLATE, anchor="lm")
    resaltar(d, (370, 340, 1180, 395), 1)
    texto(d, (370, 440), "Certificado (solo si lo pide):", 24, SLATE, bold=True)
    boton(d, (370, 480, 600, 535), "Choose file", bg=WHITE, fg=SLATE, borde=MUTED, size=24)
    texto(d, (630, 507), "Asteroides (original)_1.0.0.0_x64_Master.cer", 22, MUTED, anchor="lm")
    boton(d, (1000, 560, 1180, 615), "Start", size=24)
    resaltar(d, (1000, 560, 1180, 615), 2)
    recreacion(d, "Device Portal")
    guardar(img, "xb-12-dependencias.png")


def xb13_instalado():
    img, d = portal("Home")
    texto(d, (310, 150), "My games & apps", 36, SLATE, bold=True)
    d.rounded_rectangle((310, 200, 1240, 250), radius=8, fill="#DCFCE7")
    texto(d, (330, 225), "Paquete instalado", 24, "#166534", bold=True, anchor="lm")
    lista_juegos(d, 280, [("Asteroides (original)", "Juego"), ("Xbox Dev Mode", "Sistema")])
    d.rounded_rectangle((980, 368, 1240, 560), radius=10, fill=WHITE, outline=MUTED, width=2)
    for i, a in enumerate(("Launch", "Remove", "View details")):
        texto(d, (1005, 400 + i * 56), a, 24, SLATE, bold=i < 2, anchor="lm")
    resaltar(d, (990, 380, 1230, 420), 1)
    resaltar(d, (990, 436, 1230, 476), 2)
    texto(d, (310, 600), "Remove: con el juego cerrado, para reinstalar una versión nueva.", 22, MUTED)
    recreacion(d, "Device Portal")
    guardar(img, "xb-13-instalado.png")


def xb14_jugar():
    img, d = dev_home_base()
    texto(d, (40, 175), "Games & apps", 28, TV_TEXT, bold=True)
    juegos = ("Asteroides (original)", "Asteroides (consola)", "Platformer (original)", "Platformer (consola)")
    for i, j in enumerate(juegos):
        x = 40 + i * 305
        d.rounded_rectangle((x, 225, x + 285, 425), radius=12, fill=TEAL if i == 0 else TV_TILE,
                            outline=WHITE if i == 0 else None, width=4)
        nombre, _, version = j.partition(" (")
        texto(d, (x + 20, 345), nombre, 26, WHITE, bold=True)
        texto(d, (x + 20, 385), "(" + version, 22, TV_TEXT)
    resaltar(d, (40, 225, 325, 425), 1)
    d.ellipse((40, 478, 80, 518), fill="#16A34A")
    texto(d, (60, 498), "A", 26, WHITE, bold=True, anchor="mm")
    texto(d, (96, 498), "Abrir con el control: probar todo sin mouse ni teclado.", 28, TV_TEXT, anchor="lm")
    texto(d, (40, 530), "≡ Menu: en la versión de consola pausa la partida.", 26, TV_MUTED)
    recreacion(d, "Dev Home en la consola")
    guardar(img, "xb-14-jugar.png")


def xb15_evidencia():
    img, d = portal("Media capture")
    resaltar(d, (30, 236, 262, 276), 1)
    texto(d, (310, 150), "Media capture", 36, SLATE, bold=True)
    boton(d, (310, 210, 600, 270), "Capture Screenshot", size=24)
    resaltar(d, (310, 210, 600, 270), 2)
    d.rectangle((310, 300, 760, 553), fill=TV_BG)
    texto(d, (535, 426), "captura de la TV", 24, TV_MUTED, anchor="mm")
    texto(d, (800, 300), "Performance (en vivo)", 26, SLATE, bold=True)
    for k, (nombre, pts) in enumerate((("CPU", (40, 55, 48, 60, 52, 58)), ("Frame rate", (60, 59, 60, 41, 60, 60)))):
        y0 = 345 + k * 105
        texto(d, (800, y0), nombre, 22, MUTED)
        d.rectangle((800, y0 + 30, 1220, y0 + 90), outline=GRID, width=2)
        xs = [800 + i * 84 for i in range(len(pts))]
        d.line([(x, y0 + 90 - p) for x, p in zip(xs, pts)], fill=TEAL, width=4)
    resaltar(d, (30, 292, 262, 332), 3)
    texto(d, (310, 590), "Guardar las capturas con fecha para PORTEO-XBOX.md §7.", 22, MUTED)
    recreacion(d, "Device Portal")
    guardar(img, "xb-15-evidencia.png")


def xb16_salir():
    img, d = dev_home_base()
    d.rectangle((0, 100, W, 150), fill=TV_BG)
    for i, t in enumerate(("Home", "Settings", "Quick Actions")):
        texto(d, (40 + i * 200, 110), t, 26, TEAL if i == 2 else TV_MUTED, bold=i == 2)
    resaltar(d, (440, 106, 600, 145), 1)
    acciones = ("Leave developer mode", "Restart", "Show Visual Studio pin", "Launch Device Portal settings")
    for i, a in enumerate(acciones):
        y = 190 + i * 90
        d.rounded_rectangle((40, y, 640, y + 70), radius=10, fill=TEAL if i == 0 else TV_TILE)
        texto(d, (70, y + 35), a, 26, WHITE, bold=i == 0, anchor="lm")
    resaltar(d, (40, 190, 640, 260), 2)
    d.rounded_rectangle((700, 190, 1240, 520), radius=14, fill=TV_PANEL)
    texto(d, (730, 225), "Al salir", 28, TV_TEXT, bold=True)
    for i, s in enumerate(("La consola reinicia en modo normal.", "Los juegos comprados vuelven a correr.",
                           "Para volver: Xbox Dev Mode →", "Switch and restart (sin reactivar).")):
        texto(d, (730, 285 + i * 50), s, 24, TV_MUTED)
    recreacion(d, "Dev Home en la consola")
    guardar(img, "xb-16-salir.png")


# --- PC (datos reales) --------------------------------------------------------
def pc01_powershell():
    """Consola de PowerShell con las lineas del log de la ultima corrida del script."""
    if not LOG.exists():
        print("AVISO  no está %s: se conserva pc-01 anterior" % LOG)
        return
    lineas = LOG.read_text(encoding="utf-8", errors="replace").splitlines()
    utiles = [l.rstrip() for l in lineas
              if l.startswith("== ") or l.lstrip().startswith("Unity: ") or re.search(r" -> .*\.msix$", l)]
    # Solo los proyectos que llegaron al .msix: un bloque cortado no se muestra como si hubiera terminado.
    bloques, actual = [], []
    for l in utiles:
        if l.startswith("== ") and actual:
            bloques.append(actual)
            actual = []
        actual.append(l)
    bloques.append(actual)
    utiles = [l for b in bloques if b[-1].endswith(".msix") for l in b]
    img, d = lienzo("#012456")
    d.rectangle((0, 0, W, 44), fill="#E5E7EB")
    texto(d, (20, 22), "Windows PowerShell", 22, SLATE, anchor="lm")
    y = 66

    def linea(s, color="#EEEDF0", bold=False):
        nonlocal y
        texto(d, (24, y), s if len(s) <= 92 else s[:89] + "…", 21, color, bold, mono=True)
        y += 31

    linea(r"PS> powershell -ExecutionPolicy Bypass -File \ ", "#FDE68A", True)
    linea(r"      proyectos-unity\Tools-Xbox\generar_builds_xbox.ps1", "#FDE68A", True)
    y += 8
    for l in utiles:
        if l.startswith("== "):
            y += 8
            linea(l, "#FFFFFF", True)
        elif "Unity:" in l:
            linea(l.strip(), "#86EFAC")
            linea("   msbuild: compila IL2CPP en Master x64 …  (varios minutos)", "#9CA3AF")
        else:
            nombre, _, ruta = l.strip().partition(" -> ")
            carpeta, _, archivo = ruta.split("\\Builds\\", 1)[-1].rpartition("\\")
            linea("   " + nombre + " ->", "#EEEDF0")
            linea("     …\\Builds\\" + carpeta + "\\", "#93C5FD")
            linea("        " + archivo, "#93C5FD", True)
    rotulo(d, "PC · líneas reales de ultima-corrida.log (proyectos terminados); salida de msbuild omitida", real=True)
    guardar(img, "pc-01-powershell.png")


def pc02_carpeta():
    """Arbol del paquete generado, con los archivos que se suben resaltados."""
    dirs = sorted(PAQUETES.glob("*_Test")) if PAQUETES.exists() else []
    if not dirs:
        print("AVISO  no hay paquete en %s: se conserva pc-02 anterior" % PAQUETES)
        return
    raiz = dirs[0]
    img, d = lienzo(WHITE)
    d.rectangle((0, 0, W, 60), fill=LIGHT)
    texto(d, (24, 30), "Builds › Xbox-Paquete › " + raiz.name, 24, SLATE, bold=True, anchor="lm")
    filas = []
    for f in sorted(raiz.iterdir(), key=lambda p: (p.is_dir(), p.name.lower())):
        if f.is_file():
            filas.append((0, f.name, f.stat().st_size, f.suffix.lower() == ".msix", f.suffix.lower() == ".cer"))
    dep = raiz / "Dependencies"
    if dep.exists():
        filas.append((0, "Dependencies/", None, False, False))
        otras = [a.name + "/" for a in sorted(dep.iterdir()) if a.name != "x64"]
        if otras:  # la Xbox es x64: las demas arquitecturas van en una sola linea
            filas.append((1, ", ".join(otras) + "  (otras arquitecturas: no subir)", None, False, False))
        for f in sorted((dep / "x64").glob("*")):
            filas.append((1, "x64/" + f.name, f.stat().st_size, True, False))
    y = 90
    for nivel, nombre, tam, sube, opcional in filas:
        x = 40 + nivel * 48
        color = SLATE if (sube or opcional or nombre == "Dependencies/") else "#9CA3AF"
        icono = "■ " if nombre == "Dependencies/" else "   "
        if sube:
            d.rounded_rectangle((x - 10, y - 6, W - 40, y + 38), radius=8, fill="#E6F4F2", outline=TEAL, width=3)
        texto(d, (x, y), icono + nombre, 24, color, bold=sube)
        if tam is not None:
            texto(d, (W - 340, y), "%.1f MB" % (tam / 2**20) if tam > 2**20 else "%d KB" % max(1, tam // 1024),
                  22, color, anchor="ra")
            etiqueta = "SUBIR" if sube else "si lo pide" if opcional else "no subir"
            texto(d, (W - 60, y), etiqueta, 22, TEAL if sube else AMBER if opcional else "#9CA3AF",
                  bold=sube or opcional, anchor="ra")
        y += 52
    rotulo(d, "PC · contenido real de la carpeta del paquete generado el 2026-10-26 (Asteroides original)", real=True)
    guardar(img, "pc-02-carpeta.png")


GENERADORES = (xb01_registro, xb02_codigo, xb03_activar, xb04_switch, xb05_dev_home, xb06_remote_access,
               xb07_certificado, xb08_preferencias, pc01_powershell, pc02_carpeta, xb10_add, xb11_msix,
               xb12_dependencias, xb13_instalado, xb14_jugar, xb15_evidencia, xb16_salir)


if __name__ == "__main__":
    SALIDA.mkdir(parents=True, exist_ok=True)
    for g in GENERADORES:
        g()
    # Las capturas reales, si las hay, reemplazan a las recreaciones del mismo nombre.
    for real in sorted(REALES.glob("*.png")) if REALES.exists() else []:
        shutil.copyfile(real, SALIDA / real.name)
        print("REAL   %s" % real.name)
    print("OK  %d imágenes en %s" % (len(list(SALIDA.glob("*.png"))), SALIDA.relative_to(BASE)))
    sys.exit(0)
