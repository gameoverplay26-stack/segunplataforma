# -*- coding: utf-8 -*-
"""
Genera Testing-Integracion-II.pptx: clase posterior a "Testing de integración"
(diseno-plataformas/clases/2026-09-28-integracion-y-plataformas/). Hilo conductor: proyecto nave + asteroides (proyectos-unity/Asteroides/).

Reutiliza las primitivas y el estilo de diseno-plataformas/clases/2026-09-28-integracion-y-plataformas/build_decks.py.
El código del proyecto (licencia Kodeco) se cita por archivo y líneas; los
fragmentos de código que aparecen en las diapositivas son propios (tests nuevos
propuestos), no copias del proyecto.

Números de línea tomados de proyectos-unity/Asteroides/asteroide-final/CodeCoverage/Report/*.html.

Requiere: pip install python-pptx
"""
import os
import sys

sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "2026-09-28-integracion-y-plataformas"))
import build_decks as base  # noqa: E402
from notas import NOTAS  # noqa: E402
from build_decks import (  # noqa: E402
    Presentation, Inches, Pt, RGBColor, PP_ALIGN, MSO_ANCHOR,
    new_slide, add_header, add_footer, add_rect, add_textbox, style_run,
    add_band, add_coderef, add_bullets, add_image_placeholder,
    render_title, render_content, NAVY, NAVY_LIGHT, TEAL, AMBER, GREEN,
    MUTED, SLATE, SLIDE_W, SLIDE_H, MARGIN_X,
)

CODE_BG = RGBColor(0x0F, 0x17, 0x2A)
CODE_TEXT = RGBColor(0xE2, 0xE8, 0xF0)
CODE_COMMENT = RGBColor(0x94, 0xA3, 0xB8)
RED = RGBColor(0xDC, 0x26, 0x26)


def render_code(prs, s, deck):
    """Diapositiva con bloque de código (fragmentos PROPIOS, no del proyecto)."""
    slide = new_slide(prs)
    add_header(slide, s["num"], s["title"], kicker=s.get("kicker"), badge=s.get("badge"))
    y = Inches(1.4)
    if s.get("intro"):
        y += add_bullets(slide, MARGIN_X, y, SLIDE_W - 2 * MARGIN_X, s["intro"], 16) + Inches(0.05)
    has_side = bool(s.get("side"))
    code_w = Inches(7.9) if has_side else SLIDE_W - 2 * MARGIN_X
    bottom = Inches(6.0) if (s.get("nota") or s.get("pregunta") or s.get("actividad")) else Inches(6.85)
    if s.get("coderef"):
        bottom -= Inches(0.62)
    add_rect(slide, MARGIN_X, y, code_w, bottom - y, CODE_BG)
    tb, tf = add_textbox(slide, MARGIN_X + Inches(0.25), y + Inches(0.15), code_w - Inches(0.5), bottom - y - Inches(0.3))
    size = s.get("csize", 12.5)
    for i, line in enumerate(s["code"]):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        r = p.add_run()
        r.text = line if line else " "
        stripped = line.strip()
        if stripped.startswith("//"):
            color = CODE_COMMENT
        elif stripped.startswith("✗") or "Expected" in line or "But was" in line or "Unhandled" in line:
            color = RGBColor(0xFC, 0xA5, 0xA5)
        else:
            color = CODE_TEXT
        style_run(r, size, color)
        r.font.name = "Consolas"
    if has_side:
        sx = MARGIN_X + code_w + Inches(0.3)
        sw = SLIDE_W - MARGIN_X - sx
        add_rect(slide, sx, y, sw, Inches(0.45), TEAL)
        tbh, tfh = add_textbox(slide, sx + Inches(0.1), y, sw - Inches(0.2), Inches(0.45), anchor=MSO_ANCHOR.MIDDLE)
        rh = tfh.paragraphs[0].add_run()
        rh.text = s.get("side_title", "Qué cambia")
        style_run(rh, 14, RGBColor(0xFF, 0xFF, 0xFF), bold=True)
        add_bullets(slide, sx, y + Inches(0.6), sw, s["side"], s.get("side_size", 14))
    if s.get("coderef"):
        add_coderef(slide, bottom + Inches(0.1), s["coderef"], SLIDE_W - 2 * MARGIN_X)
    if s.get("actividad"):
        add_band(slide, Inches(6.15), s["actividad"], "✍ Actividad:")
    elif s.get("pregunta"):
        add_band(slide, Inches(6.15), s["pregunta"], "❓")
    elif s.get("nota"):
        add_band(slide, Inches(6.15), s["nota"], "ℹ", bg=RGBColor(0xF3, 0xF4, 0xF6), color=MUTED, size=14)
    add_footer(slide, s["num"], deck["total"], deck["footer"])
    slide.notes_slide.notes_text_frame.text = s.get("notes", "")


def build(deck, filename):
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    deck["total"] = len(deck["slides"])
    renderers = {"title": render_title, "code": render_code}
    for i, s in enumerate(deck["slides"], start=1):
        s["num"] = i
        assert s["title"] in NOTAS, f"Falta la nota de la diapositiva: {s['title']}"
        s["notes"] = NOTAS[s["title"]]
        renderers.get(s.get("type"), render_content)(prs, s, deck)
    out = os.path.join(HERE, filename)
    prs.save(out)
    print(f"OK - {len(prs.slides)} diapositivas en {out}")


# ============================================================================
# Contenido
# ============================================================================
DECK = dict(
    footer="Diseño según Plataformas de Juego · Testing de integración II · Hilo conductor: nave + asteroides",
    slides=[
        dict(type="title", kicker="Continuación de «Testing de integración»",
             title="Testing de integración II",
             subtitle="De 7 tests a una estrategia · Diseño según Plataformas de Juego · 120 min",
             footer="Ing. Elsa Daniela Ramírez · FI – UNJu · 2026"),

        # ---------------------------------------------------------------- diagnóstico
        dict(title="Dónde quedamos: la suite actual", kicker="Diagnóstico · clase anterior",
             tables=[dict(headers=["#", "Test (TestSuite.cs)", "Flujo que cubre", "Tipo de caso"],
                          widths=[0.5, 4.2, 4.3, 1.8], size=13,
                          rows=[
                              ["01", "AsteroidsMoveDown", "El asteroide se desplaza", "Positivo"],
                              ["02", "GameOverOccursOnAsteroidCollision", "Asteroide + nave → Game Over", "Positivo"],
                              ["03", "NewGameRestartsGame", "Reinicio (Game Over simulado a mano)", "Positivo"],
                              ["04", "GameOverStopsSpawningAndDisablesShip", "Game Over detiene spawner y nave", "Positivo"],
                              ["05", "LaserMovesUp", "El láser se desplaza", "Positivo"],
                              ["06", "LaserDestroysAsteroid", "Láser + asteroide → destrucción", "Positivo"],
                              ["07", "DestroyedAsteroidRaisesScore", "Láser + asteroide → puntaje", "Positivo"],
                          ])],
             coderef="TestSuite.cs 53–149",
             nota="Todos son casos positivos. Sin negativos, sin bordes, sin HUD, sin limpieza entre tests."),

        dict(title="Objetivos de la clase", kicker="Al finalizar podrán",
             bullets=[
                 "Diseñar casos de integración positivos, negativos y de borde para un flujo de juego",
                 "Preparar fixtures y datos de prueba que aíslen cada test",
                 "Reconocer las causas de un test frágil (flaky) y corregirlas",
                 "Elegir qué dependencias usar reales y cuáles reemplazar por dobles de prueba",
                 "Interpretar un reporte de cobertura sin sobreestimarlo",
                 "Organizar una mini-suite de integración priorizada",
             ],
             image="Diagrama de evolución: «7 tests positivos» → «suite con positivos, negativos, bordes y regresión» (dos columnas con flecha)."),

        dict(title="Agenda (120 min)", kicker="Organización",
             tables=[dict(headers=["Bloque", "Min", "Teoría", "Demo", "Práctica", "Resolución"],
                          widths=[4.6, 0.8, 1, 1, 1.1, 1.3], size=13,
                          rows=[
                              ["Apertura y diagnóstico", "8", "5", "3", "–", "–"],
                              ["1. Positivos, negativos y borde", "12", "8", "4", "–", "–"],
                              ["   Actividad 1 · diseñar casos", "17", "–", "–", "12", "5"],
                              ["   Actividad 2 · casos borde", "15", "–", "–", "10", "5"],
                              ["2. Fixtures, aislamiento y tests frágiles", "13", "8", "5", "–", "–"],
                              ["   Actividad 3 · analizar un test fallido", "15", "–", "–", "10", "5"],
                              ["3. Dependencias y dobles de prueba", "8", "6", "2", "–", "–"],
                              ["4. Cobertura y regresión", "8", "5", "3", "–", "–"],
                              ["   Actividad 4 · mini-suite", "19", "–", "–", "14", "5"],
                              ["Cierre", "5", "5", "–", "–", "–"],
                              ["Total", "120", "37", "17", "46", "20"],
                          ])]),

        dict(title="La suite pasa… ¿y el juego?", kicker="Apertura",
             bullets=[
                 "¿Qué pasa si reinicio la partida con asteroides todavía en pantalla?",
                 "¿Y si dos láseres golpean el mismo asteroide en el mismo instante?",
                 "¿Qué pasa si un asteroide choca con otro asteroide?",
                 "El reporte de cobertura dice 73,6 %, y Game.cs tiene 100 %. ¿Qué tan protegidos estamos?",
             ],
             image="Captura del Test Runner con los 7 tests en verde junto al resumen del reporte de cobertura regenerado (73,6 % de líneas).",
             pregunta="¿Cuál de estas preguntas responde hoy la suite? (Respuesta: ninguna)"),

        # ---------------------------------------------------------------- bloque 1
        dict(title="Positivos, negativos y borde", kicker="Bloque 1 · teoría",
             tag="una puerta con cerradura",
             tables=[dict(headers=["Tipo de caso", "Qué pregunta", "Puerta", "Nave + asteroides"],
                          widths=[1.6, 3, 2.6, 3.6], size=13,
                          rows=[
                              ["Positivo", "¿Hace lo que debe con una entrada válida?", "La llave correcta abre", "El láser destruye el asteroide y suma 1"],
                              ["Negativo", "¿Ignora o rechaza lo que no corresponde?", "Otra llave no abre", "Un asteroide que choca con otro NO da Game Over"],
                              ["Borde", "¿Qué pasa justo en el límite?", "La llave a medio girar", "Un asteroide en y = −5,0 exacto: ¿se destruye?"],
                          ])],
             bullets=[
                 "Negativo ≠ test que falla: el test pasa si el sistema ignora correctamente la entrada",
                 "En integración, el borde no es solo un número: también tiempo, cantidad, repetición y orden",
             ],
             bsize=16),

        dict(title="Cinco dimensiones del borde en integración", kicker="Bloque 1 · teoría",
             tables=[dict(headers=["Dimensión", "Pregunta", "En el juego"],
                          widths=[1.8, 3.6, 5.4], size=13,
                          rows=[
                              ["Valor / posición", "¿Justo en el límite?", "Asteroide en y = −4,99 / −5,00 / −5,01"],
                              ["Tiempo", "¿Justo antes o después de un intervalo?", "Disparo a 0,39 s y a 0,41 s del anterior (cooldown 0,4 s)"],
                              ["Cantidad / simultaneidad", "¿0, 1 o 2 eventos a la vez?", "Dos láseres contra el mismo asteroide en el mismo paso de física"],
                              ["Repetición", "¿Qué pasa si se llama dos veces?", "NewGame() dos veces seguidas"],
                              ["Orden", "¿Y si los eventos llegan al revés?", "Un punto que se suma en el mismo frame del Game Over"],
                          ])],
             coderef="Asteroid.cs 43–50 (límite −5) · Ship.cs 82–90 (cooldown 0,4 s) · Laser.cs 46–55 · Game.cs 67–80",
             nota="Algunos bordes no tienen un resultado esperado obvio: lo decide el diseño, no quien prueba."),

        dict(title="Formato de un caso de integración", kicker="Bloque 1 · caso modelo",
             tables=[dict(headers=["Campo", "INT-AST-11 · Choque entre asteroides (negativo)"], widths=[2.2, 8.6], size=13,
                          rows=[
                              ["Objetivo", "Un choque entre dos asteroides no provoca Game Over"],
                              ["Componentes", "Asteroid ×2 · física · Game"],
                              ["Entrada", "Dos asteroides superpuestos, lejos de la nave"],
                              ["Precondiciones", "Prefab Game instanciado · 1 frame (Start ejecutado) · isGameOver = false"],
                              ["Pasos", "1. SpawnAsteroid() ×2  2. Ubicar ambos en (6, 3)  3. Esperar 2 FixedUpdate"],
                              ["Resultado esperado", "isGameOver = false · ambos asteroides siguen existiendo · score sin cambios"],
                              ["Bug que detecta", "Alguien relaja la condición de Asteroid.cs 54 y cualquier choque termina la partida"],
                              ["¿Por qué integración?", "Verifica el contrato por nombre entre Asteroid y Game a través de la física real"],
                          ])]),

        dict(title="Actividad 1 · Diseñar casos nuevos (12 min)", kicker="Práctica · en grupos",
             bullets=[
                 "Flujo A: láser destruye asteroide → puntaje",
                 "Flujo B: asteroide choca la nave → Game Over",
                 "Flujo C: Game Over → nueva partida",
                 "Para cada flujo: un caso POSITIVO nuevo y un caso NEGATIVO",
                 "Usar la ficha de 8 campos · no repetir los tests 01–07",
             ],
             image="La ficha de 8 campos vacía (Objetivo · Componentes · Entrada · Precondiciones · Pasos · Resultado esperado · Bug que detecta · ¿Por qué integración?).",
             actividad="Entreguen 6 fichas (2 por flujo). Pista: ¿qué NO debería pasar en cada flujo?"),

        dict(title="Actividad 1 · Resolución", kicker="Resolución docente",
             tables=[dict(headers=["Flujo", "Caso", "Resultado esperado", "Bug que detecta"],
                          widths=[0.8, 3.4, 3.6, 3.4], size=12,
                          rows=[
                              ["A +", "INT-AST-09 · El HUD muestra el puntaje", "2 impactos → score = 2 y texto «Score: 2»", "Se borra la actualización del texto (Game.cs 85)"],
                              ["A −", "INT-AST-10 · Láser contra objeto ajeno", "score = 0 · el objeto sigue intacto · sin excepción", "Se quita el filtro GetComponent<Asteroid>() (Laser.cs 48)"],
                              ["B +", "(ya cubierto por 02 y 04)", "—", "—"],
                              ["B −", "INT-AST-11 · Choque entre asteroides", "isGameOver = false", "Cualquier choque dispara Game Over"],
                              ["C +", "INT-AST-08 · Reinicio tras Game Over real", "Nave viva en (0,0,0) · score 0 · spawner activo", "RepairShip o BeginSpawning omitidos"],
                              ["C −", "NewGame con partida en curso", "Estado inicial, sin doble spawner", "Ver INT-AST-15 (repetición)"],
                          ])],
             nota="HUD: scoreText es privado, pero está dentro del prefab Game (UICanvas/ScoreText): el test puede encontrarlo con GetComponentsInChildren<Text>()."),

        dict(title="Actividad 2 · Casos borde (10 min)", kicker="Práctica · análisis sin código",
             quote="Una fila por dimensión, con valores concretos y resultado esperado. Marquen con ⚠ las filas cuyo resultado no pueden decidir ustedes.",
             qsize=17,
             tables=[dict(headers=["Dimensión", "Valores a probar", "Resultado esperado", "⚠"],
                          widths=[2, 3.6, 4, 0.6], size=13,
                          rows=[["Valor", "", "", ""], ["Tiempo", "", "", ""], ["Simultaneidad", "", "", ""],
                                ["Repetición", "", "", ""], ["Orden", "", "", ""]])],
             actividad="¿Quién decide el resultado esperado de una fila marcada con ⚠?"),

        dict(title="Actividad 2 · Resolución", kicker="Resolución docente",
             tables=[dict(headers=["Dimensión", "Valores", "Resultado esperado", "⚠"],
                          widths=[1.7, 3.6, 4.6, 0.5], size=12,
                          rows=[
                              ["Valor", "Asteroide en y = −4,99 · −5,00 · −5,01", "Vivo · vivo · destruido (condición estricta «< −5») → INT-AST-12", ""],
                              ["Tiempo", "Disparo a 0,39 s y 0,41 s del anterior", "No dispara · dispara → INT-AST-16 (hoy no se puede automatizar)", ""],
                              ["Simultaneidad", "2 láseres → 1 asteroide, mismo paso", "score +1 y sin excepción → INT-AST-13 (EJECUTADO: suma 2 y lanza excepción)", ""],
                              ["Simultaneidad", "1 láser → 2 asteroides superpuestos", "¿+1 o +2? Decisión de diseño", "⚠"],
                              ["Repetición", "NewGame() dos veces seguidas", "Misma tasa de aparición → INT-AST-15 (EJECUTADO: 8 asteroides vs. 5)", ""],
                              ["Orden", "Punto sumado en el frame del Game Over", "¿Cuenta o no? Decisión de diseño", "⚠"],
                          ])]),

        # ---------------------------------------------------------------- bloque 2
        dict(title="Fixtures y datos de prueba", kicker="Bloque 2 · teoría",
             tag="un laboratorio",
             bullets=[
                 "Fixture: el estado conocido del que parte cada test (SetUp) y la limpieza al terminar (TearDown)",
                 "Como un laboratorio: mesada limpia antes del experimento, limpieza al terminar",
                 "En la suite actual, TearDown destruye solo el prefab Game",
                 "Asteroides y láseres se crean como objetos raíz: sobreviven al test y «ensucian» el siguiente",
                 "Game.instance es estático: puede apuntar a un Game ya destruido hasta que corra el siguiente Start()",
                 "Spawner usa Random sin semilla: cada corrida genera posiciones distintas",
             ],
             bsize=15,
             image="Esquema de dos tests consecutivos: los asteroides del Test A siguen en escena cuando empieza el Test B (flecha roja entre ambos).",
             coderef="TestSuite.cs 40–51 · Spawner.cs 73–99 (Instantiate sin padre) y 103 (Random) · Game.cs 46 y 50 (instancia estática)"),

        dict(type="code", title="Fixture mejorada (PROPUESTA)", kicker="Bloque 2 · demo",
             code=[
                 "[UnitySetUp]",
                 "public IEnumerator SetUp()",
                 "{",
                 "    Random.InitState(12345);        // datos reproducibles",
                 "    var prefab = Resources.Load<GameObject>(\"Prefabs/Game\");",
                 "    game = Object.Instantiate(prefab).GetComponent<Game>();",
                 "    yield return null;              // corre Start(): instance listo",
                 "}",
                 "",
                 "[UnityTearDown]",
                 "public IEnumerator TearDown()",
                 "{",
                 "    Object.Destroy(game.gameObject);",
                 "    var none = FindObjectsSortMode.None;",
                 "    foreach (var a in Object.FindObjectsByType<Asteroid>(none))",
                 "        Object.Destroy(a.gameObject);   // lo que el test dejó",
                 "    foreach (var l in Object.FindObjectsByType<Laser>(none))",
                 "        Object.Destroy(l.gameObject);",
                 "    yield return null;              // Destroy termina al final del frame",
                 "}",
             ],
             csize=11.5,
             side_title="Qué cambia",
             side=["Semilla fija: datos reproducibles",
                   "Un frame de espera: Start() ya corrió",
                   "Limpieza total, no solo del prefab",
                   "Otro frame: el próximo test empieza limpio"],
             nota="Código propio de la cátedra. La limpieza (UnityTearDown) ya corre en IntegrationHypothesesTests.cs; la semilla no se probó."),

        dict(title="Tests frágiles (flaky)", kicker="Bloque 2 · teoría",
             tag="Martin Fowler · «Eradicating Non-Determinism in Tests»",
             tables=[dict(headers=["Causa", "En la suite actual", "Remedio"], widths=[2, 5.2, 3.6], size=12,
                          rows=[
                              ["Tiempo fijo", "WaitForSeconds(0,1) depende de la máquina y de la física", "Esperar por condición, con tiempo máximo"],
                              ["Estado compartido", "Asteroides de tests anteriores siguen en escena", "TearDown que limpia todo"],
                              ["Orden", "04 cuenta TODOS los asteroides de la escena", "Contar solo lo que creó el test"],
                              ["Azar", "Posición X aleatoria del spawner", "Random.InitState(semilla)"],
                              ["Física", "Las colisiones ocurren en FixedUpdate", "yield return new WaitForFixedUpdate()"],
                          ])],
             nota="Flaky: pasa o falla sin que cambie el código. Destruye la confianza en toda la suite."),

        dict(type="code", title="Esperar por condición, no por tiempo fijo (PROPUESTA)", kicker="Bloque 2 · demo",
             code=[
                 "// Antes: espera fija (TestSuite.cs 134)",
                 "yield return new WaitForSeconds(0.1f);",
                 "",
                 "// Después: espera hasta que se cumpla la condición o se agote el tiempo",
                 "float timeout = 2f;",
                 "while (asteroid != null && timeout > 0f)",
                 "{",
                 "    timeout -= Time.deltaTime;",
                 "    yield return null;",
                 "}",
                 "Assert.IsTrue(asteroid == null,",
                 "    \"El asteroide debería destruirse al recibir el láser\");",
             ],
             side_title="Por qué",
             side=["Pasa apenas se cumple: más rápido",
                   "Tolera máquinas lentas",
                   "El timeout evita esperas infinitas",
                   "«asteroid == null» usa la comparación de Unity para objetos destruidos"],
             nota="Código propio (PROPUESTA). El mensaje del Assert explica QUÉ se esperaba: ayuda a diagnosticar."),

        dict(type="code", title="Actividad 3 · Un test que falla (10 min)", kicker="Práctica · análisis",
             code=[
                 "[UnityTest]  // INT-AST-14 · IntegrationHypothesesTests.cs",
                 "public IEnumerator NewGame_RemovesLeftoverAsteroids()",
                 "{",
                 "    yield return null;                     // Start() asigna Game.instance",
                 "    game.NewGame();",
                 "    GameObject leftover = game.GetSpawner().SpawnAsteroid();",
                 "    leftover.transform.position = new Vector3(6f, 3f, leftover.transform.position.z);",
                 "    Game.GameOver();",
                 "    yield return null;",
                 "",
                 "    game.NewGame();                        // el jugador reinicia",
                 "    yield return null;",
                 "",
                 "    Assert.IsTrue(leftover == null, \"NewGame debería eliminar los asteroides previos\");",
                 "}",
                 "",
                 "✗ FAIL (batchmode 28/09/2026) — NewGame debería eliminar los asteroides previos",
                 "  Expected: True   But was: False",
             ],
             csize=11.5,
             actividad="1) ¿Falla el juego o el test?  2) Causa en el código  3) Impacto para el jugador  4) Ticket  5) ¿Y después del arreglo?"),

        dict(title="Actividad 3 · Resolución", kicker="Resolución docente",
             flow=[
                 "SpawnAsteroid() crea con Instantiate y nunca pasa por el pool",
                 "NewGame() → ClearAsteroids() → asteroids.Dispose()",
                 "Dispose() vacía el pool… que no contiene los asteroides en pantalla",
                 "El asteroide viejo sobrevive y puede chocar la nave recién reparada",
             ],
             fsize=14,
             bullets=[
                 "Falla el juego si el diseño exige limpiar; confirmarlo antes de levantar el ticket",
                 "Ticket: «Reiniciar no elimina asteroides previos: posible Game Over inmediato» · Severidad Media · Prioridad Alta",
                 "Arreglo: usar el pool de forma consistente (Get/Release) o destruir los Asteroid en ClearAsteroids",
                 "Después del arreglo, el test se queda en la suite como test de regresión",
             ],
             bsize=14,
             coderef="Spawner.cs 73–99 (Instantiate) y 115–117 (Dispose) · Game.cs 78 (ClearAsteroids) · Spawner.cs 52–53 (creación del pool)"),

        # ---------------------------------------------------------------- bloque 3
        dict(title="Dependencias y dobles de prueba", kicker="Bloque 3 · teoría",
             tag="Martin Fowler · «TestDouble» (taxonomía de Gerard Meszaros)",
             tables=[dict(headers=["Doble", "Qué hace", "Ejemplo simple", "En el juego"],
                          widths=[1.2, 3, 3, 3.6], size=12,
                          rows=[
                              ["Dummy", "Solo ocupa un lugar", "Un DNI de muestra para llenar un formulario", "Cubo con collider en INT-AST-10"],
                              ["Stub", "Devuelve respuestas fijas", "Un reloj que siempre dice 7:00", "Entrada que siempre dice «Espacio presionado» (PROPUESTA)"],
                              ["Spy", "Registra llamadas para revisarlas después", "Un contador de timbres", "Contar llamadas a AsteroidDestroyed (PROPUESTA)"],
                              ["Mock", "Espera llamadas concretas y falla si no llegan", "«El timbre debe sonar una vez»", "GameOver llama a StopSpawning exactamente una vez (PROPUESTA)"],
                              ["Fake", "Implementación simple que funciona", "Una agenda en papel en vez de la app", "Récord guardado en memoria en vez de un archivo (PROPUESTA)"],
                          ])],
             nota="En integración, lo que está en la costura bajo prueba va REAL; se reemplaza lo no determinista o lo que queda fuera de alcance."),

        dict(title="Caso: la regla del cooldown vive junto al teclado", kicker="Bloque 3 · aplicación",
             tag="INT-AST-16 (PROPUESTA)",
             bullets=[
                 "Regla de juego: como máximo un láser cada 0,4 s aunque se mantenga Espacio",
                 "El chequeo de canShoot está en Update(), junto a Input.GetKey(Space)",
                 "ShootLaser() no respeta la regla: dos llamadas seguidas crean dos láseres",
                 "Sin simular el teclado, la regla no se puede probar",
                 "Opción A: Input System + InputTestFixture (requiere un paquete no confirmado en el proyecto)",
                 "Opción B: separar la lectura de entrada detrás de una interfaz y usar un stub (refactor)",
             ],
             bsize=15,
             image="Diagrama: hoy «Teclado → Ship.Update (regla + movimiento)»; propuesta «Teclado / Stub → Entrada → Ship (regla)», con el stub resaltado.",
             coderef="Ship.cs 61–64 (regla + tecla) · Ship.cs 77–80 (ShootLaser sin chequeo) · Ship.cs 82–90 (cooldown)",
             pregunta="Esperado con Espacio mantenido 1 s: ¿cuántos láseres? (Respuesta: 3, en t = 0; 0,4; 0,8)"),

        # ---------------------------------------------------------------- bloque 4
        dict(title="Cobertura: qué mide y qué no", kicker="Bloque 4 · caso real del proyecto",
             tag="Reporte regenerado: 7 tests, carpeta limpia, 28/09/2026",
             bullets=[
                 "Reporte viejo del repo: 65,5 %, mezclando 3 corridas (15/09 y 18/09) y el código de los tests",
                 "Regenerado: 73,6 % de líneas y 87 % de métodos de GameAssembly · Game.cs 100 % · Ship.cs 43 %",
                 "Game.cs 100 %… pero la línea del HUD (85) se ejecuta sin que ningún test la compruebe",
                 "Nunca ejecutado: entrada del jugador, movimiento lateral, asteroide que sale de pantalla, spawn automático",
                 "Cobertura de ramas: 0 de 0 → no se midió",
             ],
             bsize=15,
             image="Captura del reporte regenerado: resumen por clase (Game 100 %, Ship 43 %) y la vista línea por línea de Ship.cs con las líneas 61–74 en rojo.",
             coderef="Sin cubrir: Ship.cs 61–74 y 99–115 · Asteroid.cs 48 · Spawner.cs 69 · Laser.cs 42 — Ejecutada sin verificar: Game.cs 85",
             pregunta="Game.cs tiene 100 % de cobertura: ¿está bien probado? ¿Usarían ese número para decidir si el juego está listo?"),

        dict(title="Regresión: del bug al test que lo vigila", kicker="Bloque 4 · teoría",
             flow=[
                 "Se detecta el defecto (Actividad 3: asteroides que sobreviven al reinicio)",
                 "Se escribe el test y se ve en ROJO: prueba que el defecto existe",
                 "Se arregla el código y el test pasa a VERDE",
                 "El test queda en la suite: si el defecto vuelve, se entera la suite antes que el jugador",
             ],
             fsize=14,
             highlight_last=True,
             nota="Retesting = volver a probar ESE arreglo. Regresión = volver a probar TODO lo que ya andaba (Unidad II)."),

        dict(title="Actividad 4 · Diseñar una mini-suite (14 min)", kicker="Práctica · en grupos",
             bullets=[
                 "Tienen los 7 tests actuales + los casos nuevos de la clase",
                 "Máximo 12 tests en la suite de integración",
                 "Categorías: Smoke (cada cambio) · Integración · Borde · Regresión",
                 "Definan la fixture común y una convención de nombres",
                 "Decidan qué tests existentes se quedan, se reescriben, se fusionan o salen",
             ],
             image="Tablero de cuatro columnas (Smoke · Integración · Borde · Regresión) con tarjetas de los tests para ubicar.",
             actividad="Entreguen la suite en una tabla: test · categoría · cuándo corre · decisión (queda / reescribir / fusionar / sale)."),

        dict(title="Actividad 4 · Resolución", kicker="Resolución docente",
             tables=[dict(headers=["Categoría", "Tests", "Cuándo corre"], widths=[1.8, 6.6, 2.4], size=12,
                          rows=[
                              ["Smoke", "02 Game Over por choque · 06 Láser destruye asteroide · 08 Reinicio tras Game Over", "Cada cambio (segundos)"],
                              ["Integración", "04 reescrito (limpieza + conteo propio) · 09 HUD (absorbe 07) · 10 Láser vs. objeto ajeno · 11 Asteroide vs. asteroide", "Cada commit"],
                              ["Borde", "12 Límite y = −5 · 13 Doble impacto · 15 Doble NewGame", "Cada commit"],
                              ["Regresión", "14 Reinicio limpia asteroides (en rojo hasta el arreglo)", "Cada commit"],
                              ["Fuera de esta suite", "01 y 05 → movimiento de un solo componente · 03 → reemplazado por 08 · 16 → pendiente del refactor de entrada", "—"],
                          ])],
             nota="Fixture común: semilla fija + limpieza total · Nombres: Flujo_Condición_Resultado · [Category(\"Smoke\")]"),

        dict(title="Cierre", kicker="Ideas para llevarse",
             bullets=[
                 "Una suite solo de casos positivos deja sin probar lo que el juego NO debe hacer",
                 "El borde en integración también es tiempo, cantidad, repetición y orden",
                 "Sin fixtures que limpien, los tests se contaminan entre sí y se vuelven frágiles",
                 "Un doble de prueba se usa para lo que no está bajo prueba, no para todo",
                 "La cobertura dice qué se ejecutó, no qué se verificó",
             ],
             actividad="Ticket de salida: un caso negativo y un caso borde para un juego propio."),

        # ---------------------------------------------------------------- anexos
        dict(title="Anexo · Catálogo de casos nuevos", kicker="Referencia",
             tables=[dict(headers=["ID", "Caso", "Tipo", "Estado"], widths=[1.4, 5.8, 2, 1.8], size=12,
                          rows=[
                              ["INT-AST-08", "Reinicio completo tras un Game Over real", "Positivo · flujo", "PROPUESTA"],
                              ["INT-AST-09", "El HUD muestra el puntaje", "Positivo · regresión", "PROPUESTA"],
                              ["INT-AST-10", "Láser contra un objeto que no es asteroide", "Negativo", "PROPUESTA"],
                              ["INT-AST-11", "Choque entre asteroides no da Game Over", "Negativo", "PROPUESTA"],
                              ["INT-AST-12", "Asteroide que cruza y = −5", "Borde · valor", "PROPUESTA"],
                              ["INT-AST-13", "Dos láseres contra el mismo asteroide", "Borde · simultaneidad", "EJECUTADO · FAIL"],
                              ["INT-AST-14", "NewGame elimina los asteroides previos", "Regresión", "EJECUTADO · FAIL"],
                              ["INT-AST-15", "NewGame dos veces seguidas", "Borde · repetición", "EJECUTADO · FAIL"],
                              ["INT-AST-16", "Cooldown de disparo con tecla mantenida", "Dependencia de entrada", "PROPUESTA (refactor)"],
                          ])],
             nota="PROPUESTA: todavía no existe en el proyecto. EJECUTADO: en Assets/Tests/IntegrationHypothesesTests.cs (batchmode, 28/09/2026)."),

        dict(title="Anexo · Para una clase futura", kicker="Contenido reservado",
             cols=[
                 ("Técnicas", [
                     "Integración con sistemas externos: guardado del récord, tabla online",
                     "Input System + InputTestFixture para simular teclado y táctil",
                     "Tests parametrizados ([TestCase], [ValueSource]) para bordes",
                     "LogAssert para esperar o prohibir mensajes en el log",
                 ], NAVY_LIGHT),
                 ("Proceso", [
                     "Ejecución en batchmode y CI (tests en cada push)",
                     "Cobertura de ramas y umbrales mínimos",
                     "Tests de rendimiento (Performance Testing)",
                     "Relación con la plataforma: la misma suite en PC y en móvil",
                 ], TEAL),
             ]),
    ],
)


if __name__ == "__main__":
    build(DECK, "Testing-Integracion-II.pptx")
