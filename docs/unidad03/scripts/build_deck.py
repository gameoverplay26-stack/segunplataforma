# -*- coding: utf-8 -*-
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from generar_diapositivas import Presentation, Inches, RENDERERS, TOTAL_SLIDES  # noqa

OUT_PATH = os.path.join(SCRIPT_DIR, "..", "Unidad-3-Diapositivas-2026.pptx")

CODE_1 = [
    "using NUnit.Framework;",
    "",
    "public class PlayerHealthTests",
    "{",
    "    [Test]",
    "    public void TakeDamage_ReducesHealthByAmount()",
    "    {",
    "        // Arrange",
    "        var health = new PlayerHealth(maxHealth: 100);",
    "",
    "        // Act",
    "        health.TakeDamage(25);",
    "",
    "        // Assert",
    "        Assert.AreEqual(75, health.CurrentHealth);",
    "    }",
    "}",
]

CODE_BREAK = [
    "// Antes (build 0.3) — funciona",
    "CurrentHealth = Mathf.Max(0, CurrentHealth - amount);",
    "",
    "// Se quita el clamp a propósito (bug provocado)",
    "CurrentHealth = CurrentHealth - amount;",
    "",
    "// Nuevo test que lo detecta:",
    "[Test]",
    "public void TakeDamage_NeverGoesBelowZero()",
    "{",
    "    var health = new PlayerHealth(100);",
    "    health.TakeDamage(150);",
    "    Assert.AreEqual(0, health.CurrentHealth);",
    "}",
]

CODE_FAIL_FIX = [
    "// Resultado del Test Runner:",
    "❌ FAIL — TakeDamage_NeverGoesBelowZero",
    "   Expected: 0",
    "   But was: -50",
    "",
    "// Corrección: se restaura el clamp",
    "CurrentHealth = Mathf.Max(0, CurrentHealth - amount);",
    "",
    "✅ PASS — todos los tests en verde",
]

SLIDES = [
    dict(num=1, type="title",
         title="Pruebas Unitarias con Unity",
         subtitle="Unidad III · Diseño según Plataformas de Juego",
         footer="Ing. Elsa Daniela Ramírez · Cryptbound, build 0.4",
         notes="Portada. Antes de empezar, recordar el hilo: seguimos con Cryptbound, no cambiamos de proyecto."),

    dict(num=2, type="bullets", title="Objetivos de la clase",
         bullets=[
             "Explicar por qué automatizar pruebas en un videojuego",
             "Diferenciar unit test de integration, functional, playtest y QA manual",
             "Elegir Edit Mode o Play Mode con criterio",
             "Crear y ejecutar un test con Arrange-Act-Assert",
             "Aplicar el ciclo Red-Green-Refactor (TDD)",
             "Reconocer qué NO se resuelve con pruebas unitarias",
         ],
         pregunta="¿Alguna vez rompieron, sin querer, algo que ya andaba?",
         notes="Ver los 10 objetivos específicos completos en 01-analisis-programa-y-objetivos.md, Sección D."),

    dict(num=3, type="bullets", title="El problema: build 0.4, un golpe raro",
         tag="Cryptbound build 0.4 — sistema Combat",
         quote="«A veces el mismo golpe le saca el doble de vida al enemigo... no siempre.»  — Marisol, QA",
         pregunta="¿Esto suena a un bug nuevo, o a algo que dejó de funcionar?",
         notes="Instalar el problema real antes de cualquier definición. No nombrar todavía la palabra 'test'."),

    dict(num=4, type="flow", title="Regresión: cuando algo que andaba deja de andar",
         flow=[
             "Player.TakeDamage() — build 0.3  ✅  funciona",
             "Se modifica CombatSystem (golpe crítico)",
             "Player.TakeDamage() — build 0.4  ❌  ya no funciona",
         ],
         notes="Evitar personalizar el error en 'el programador' — el foco es el proceso, no la culpa. Nombrar el concepto: REGRESIÓN."),

    dict(num=5, type="flow", title="Repaso relámpago: Unidad I → II → III",
         flow=[
             "Unidad I — error, defecto, fallo, causa raíz",
             "Unidad II — test case, severidad, regression testing",
             "Unidad III — ese mismo test case, ejecutado como código",
         ],
         notes="30 segundos, no una clase nueva. Solo anclar vocabulario ya visto."),

    dict(num=6, type="bullets", title="¿Qué es una prueba unitaria?",
         quote="Verifica automáticamente UN comportamiento específico de una unidad de código, bajo condiciones determinadas.",
         bullets=["'Unidad' ≠ el juego completo — por lo general, un único método"],
         notes="Definición formal y comprensible. Distinguir de inmediato unidad vs. juego completo."),

    dict(num=7, type="flow", title="Arrange / Act / Assert",
         flow=["ARRANGE — preparar el escenario", "ACT — ejecutar el comportamiento", "ASSERT — comprobar el resultado"],
         notes="Mismos campos que un test case de Unidad 2 (precondición / pasos / resultado esperado) — decirlo explícitamente."),

    dict(num=8, type="flow", title="AAA aplicado a Cryptbound",
         tag="PlayerHealth",
         flow=["ARRANGE: Player con 100 HP", "ACT: recibe 25 de daño", "ASSERT: HP == 75"],
         notes=""),

    dict(num=9, type="code", title="El mismo ejemplo, en C# con NUnit",
         code=CODE_1,
         notes="Señalar 'using NUnit.Framework;' y el atributo [Test], sin profundizar todavía en Test Runner (eso viene en el bloque 5)."),

    dict(num=10, type="table", title="No confundir: tipos de testing",
         headers=["Tipo", "Qué prueba", "Automatizable", "Ejemplo en Cryptbound"],
         rows=[
             ["Unit Test", "Una unidad aislada de código", "Sí", "PlayerHealth.TakeDamage"],
             ["Integration Test", "Interacción entre componentes", "Sí (más esfuerzo)", "CombatSystem → PlayerHealth (Play Mode)"],
             ["Functional Test", "Una funcionalidad completa", "Parcial", "Animación de derrota del jefe"],
             ["Playtest", "Una persona juega y evalúa", "No", "Sesión de 90 min, backlog de Unidad 2"],
             ["QA manual", "Verificación humana con plan", "No", "Ejecutar TC-A01 / TC-R01 / TC-E01 a mano"],
             ["Automated Test", "Cualquier prueba corrida por una máquina", "Por definición, sí", "Toda la suite de Assets/Tests"],
         ],
         notes_line="Playtest y QA manual NO son inferiores — son insustituibles para lo que un Assert no puede evaluar.",
         notes="Remarcar con fuerza la última línea antes de pasar al ejercicio."),

    dict(num=11, type="bullets", title="Ejercicio rápido en vivo",
         bullets=["Clasificar 4 casos sueltos del backlog de Cryptbound, entre todos",
                  "5 minutos · votación a mano alzada"],
         notes="Practicar la clasificación de la tabla anterior antes de seguir."),

    dict(num=12, type="bullets", title="Buenos candidatos para unit testing",
         tag="Inventory.AddItem · PlayerExperience.GainExperience",
         bullets=["Cálculo de daño", "Puntuación", "Inventario", "Reglas y cooldown",
                  "Conversión de estadísticas", "Validaciones y estados"],
         notes=""),

    dict(num=13, type="bullets", title="Casos más complejos para unit testing",
         tag="Animación de derrota del jefe — CRYPT-108",
         bullets=["Físicas", "Animaciones", "Iluminación", "Rendering",
                  "UX / sensación del gameplay", "Timing visual", "Diversión"],
         notes="Se verifican jugando, no con Assert."),

    dict(num=14, type="bullets", title="Beneficios de las pruebas unitarias",
         bullets=["Detección temprana de errores", "Prevención de regresiones", "Feedback rápido",
                  "Refactoring más seguro", "Documentación ejecutable del comportamiento",
                  "Confianza para modificar código"],
         notes="Frase literal a decir: 'reducen el riesgo de determinados defectos y permiten detectar regresiones temprano' — nunca 'eliminan los bugs'."),

    dict(num=15, type="bullets", title="¿Qué NO solucionan las pruebas unitarias?",
         tag="CRYPT-111 — caída de FPS en la sala del jefe",
         bullets=["Bugs visuales", "Problemas de UX y de diseño", "Gameplay poco divertido",
                  "Problemas de balance", "Rendimiento no capturado por esos tests",
                  "Problemas de integración, assets, iluminación, animación, físicas complejas"],
         notes="Recordar también la queja 'el combate se siente lento' (Unidad 2) — opinión de diseño, no bug."),

    dict(num=16, type="flow", title="Estrategia de calidad", highlight_last=True,
         flow=["Unit Tests", "+ Integration Tests", "+ Automated Tests", "+ Manual QA", "+ Playtest",
               "= ESTRATEGIA DE CALIDAD"],
         notes="Automatizar pruebas no significa eliminar las pruebas manuales."),

    dict(num=17, type="bullets", title="Unity Test Framework: qué es",
         quote="La función de pruebas unitarias que ofrece Unity — por dentro utiliza NUnit.",
         notes="Afirmación textual del material 2024, sigue vigente. Fuente oficial verificada en 06-investigacion-recursos.md."),

    dict(num=18, type="bullets", title="Verificar el paquete",
         quote="Window ▸ Package Manager ▸ Unity Registry ▸ Test Framework",
         bullets=["En Unity 6: paquete 'core', fijo a la versión del Editor — no se administra por separado"],
         notes="Mencionar brevemente la diferencia de empaquetado si la cátedra usa Unity 6."),

    dict(num=19, type="bullets", title="Abrir Test Runner",
         quote="Window ▸ General ▸ Test Runner",
         notes="Mostrar la ventana acoplada junto al Inspector."),

    dict(num=20, type="bullets", title="Crear la carpeta de tests",
         quote="Botón 'Create Test Assembly Folder' → carpeta Tests + Tests.asmdef",
         bullets=["Referencias automáticas: nunit.framework.dll, UnityEngine.TestRunner, UnityEditor.TestRunner"],
         notes="Por eso el test puede usar 'using NUnit.Framework;' sin configurar nada más."),

    dict(num=21, type="bullets", title="Crear GameAssembly y referenciarlo",
         quote="Assets/Scripts ▸ Create ▸ Assembly Definition → nombrarlo GameAssembly",
         bullets=["Agregarlo como referencia del asmdef de Tests — si no, el test no ve las clases del juego"],
         notes="No es un trámite: es el motivo técnico detrás del paso."),

    dict(num=22, type="bullets", title="Qué es un Test Suite",
         tag="PlayerHealthTests · InventoryTests · CombatSystemTests",
         quote="Un archivo de clase con pruebas unitarias = Test Suite. Se organiza por agrupación lógica.",
         notes="Ver estructura de carpetas completa en 02-caso-practico-testing-videojuego.md, Sección B."),

    dict(num=23, type="table", title="Edit Mode vs. Play Mode",
         headers=["Característica", "Edit Mode", "Play Mode"],
         rows=[
             ["Ejecuta escena real", "No", "Sí"],
             ["Requiere runtime / GameObject", "No", "Sí"],
             ["Soporta corrutinas", "No", "Sí, vía [UnityTest] + IEnumerator"],
             ["Velocidad", "Rápido", "Más lento (instancia escena, avanza frames)"],
             ["Uso recomendado", "Lógica pura: cálculos, reglas, inventario, daño, XP", "MonoBehaviour, interacción entre componentes"],
             ["Ejemplo en Cryptbound", "PlayerHealthTests, InventoryTests", "CombatSystemTests, EnemyArcherTests"],
         ],
         notes="Concepto central de la unidad. La pregunta que decide el modo: '¿mi código depende de la escena corriendo?'"),

    dict(num=24, type="bullets", title="Cuándo usar Edit Mode",
         tag="PlayerHealth · Inventory · PlayerExperience",
         bullets=["Clases C# puras, sin heredar de MonoBehaviour"],
         notes="Separar la lógica de reglas del código dependiente del motor es, en sí mismo, una buena práctica."),

    dict(num=25, type="bullets", title="Cuándo usar Play Mode",
         tag="CombatSystem · EnemyArcher",
         bullets=["MonoBehaviour — dependen de posición, Time.time, frames"],
         pregunta="Inventory.AddItem no toca ninguna escena — ¿Edit Mode o Play Mode?",
         notes=""),

    dict(num=26, type="code", title="Primer test: el código",
         code=CODE_1,
         notes="Demostración pedagógica central — no acelerar este tramo."),

    dict(num=27, type="bullets", title="Ejecutar: PASS ✅",
         quote="✅  Test Runner — AsteroidsMoveDown... digo, TakeDamage_ReducesHealthByAmount: PASS",
         notes="Anticipar en voz alta qué se espera ver antes de correr el test."),

    dict(num=28, type="code", title="Provocar el fallo a propósito",
         code=CODE_BREAK,
         notes="Avisar explícitamente: 'ahora voy a romper el código a propósito', antes de ejecutar."),

    dict(num=29, type="code", title="FAIL ❌, corrección, PASS de nuevo",
         code=CODE_FAIL_FIX,
         pregunta="¿Qué hubiera pasado si este bug llegaba al playtest en vez de acá?",
         notes=""),

    dict(num=30, type="bullets", title="Ejemplos progresivos",
         bullets=["Heal_IncreasesHealthByAmount — curación", "Heal_DoesNotExceedMaxHealth — no supera el máximo",
                  "TakeDamage_SetsIsDead_WhenHealthReachesZero — muerte",
                  "AddItem_PotionIsInInventory — inventario", "Cooldown de ataque"],
         notes="Recorrer rápido — detalle completo en 02-caso-practico-testing-videojuego.md, Secciones D y E."),

    dict(num=31, type="bullets", title="Buenas prácticas al escribir tests",
         tag="Random.value en CombatSystem — test frágil",
         bullets=["Un comportamiento por test", "Nombres descriptivos: Método_Escenario_ResultadoEsperado",
                  "Tests deterministas — cuidado con Random sin controlar", "Aislar unidades",
                  "No depender del orden de ejecución", "AAA siempre",
                  "Probar comportamiento, no implementación interna"],
         notes="Un test que a veces pasa y a veces falla sin que el código cambie es un test frágil."),

    dict(num=32, type="flow", title="TDD: el ciclo Red-Green-Refactor",
         flow=["RED — escribir un test que falla", "GREEN — implementar lo mínimo para pasar",
               "REFACTOR — mejorar sin romper los tests", "Repetir"],
         notes="Frase ancla: TDD no es 'hacer tests' — es una estrategia donde las pruebas guían la implementación."),

    dict(num=33, type="flow", title="TDD en Cryptbound: PlayerExperience",
         flow=["RED: GainExperience_IncreasesTotalExperience (no compila)",
               "GREEN: CurrentExperience += amount",
               "RED 2: GainExperience_LevelsUp_WhenThresholdReached",
               "GREEN 2: se agrega Level y el umbral de 100 XP",
               "REFACTOR: ¿y si se ganan 250 XP de una vez?"],
         notes="Mostrar el fallo de COMPILACIÓN de la primera vuelta como RED válido, no solo un Assert fallido."),

    dict(num=34, type="twocol", title="TDD: cuándo sí, cuándo no",
         left_title="Buenos candidatos",
         left_items=["Lógica de dominio", "Reglas", "Cálculos deterministas", "Inventario", "Combate", "Scoring"],
         right_title="Menos conveniente",
         right_items=["Prototipado visual rápido", "Shaders", "Animación", "Diseño de niveles",
                      "Exploración de gameplay"],
         notes="Usar TDD donde aporte valor, no convertirlo en dogma."),

    dict(num=35, type="twocol", title="Pruebas manuales vs. automatizadas",
         left_title="Manual",
         left_items=["+ Exploración y percepción humana", "+ UX y descubrimiento inesperado",
                      "− Lento y repetitivo", "− Costoso a escala"],
         right_title="Automatizada",
         right_items=["+ Velocidad y repetibilidad", "+ Ideal para regresión, ejecución frecuente",
                       "− Costo inicial y mantenimiento", "− No sustituye el juicio humano"],
         notes="Mencionar en una frase que esto puede escalar a CI (Git → build → tests automáticos) sin desarrollarlo."),

    dict(num=36, type="flow", title="Cierre: conexión con Unidad 2 y lanzamiento del TP N° 2",
         flow=["BUG (playtest)", "JIRA (ticket)", "FIX", "UNIT TEST DE REGRESIÓN", "PROTEGIDO"],
         highlight_last=True,
         pregunta="¿Qué sistema de un juego propio se beneficiaría hoy de un test como los que vimos?",
         notes="CRYPT-201 como ejemplo. Repasar 3-4 errores conceptuales. Lanzar la consigna del TP N° 2."),
]


def main():
    assert len(SLIDES) == TOTAL_SLIDES, f"Se esperaban {TOTAL_SLIDES} slides, hay {len(SLIDES)}"
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    for s in SLIDES:
        renderer = RENDERERS[s["type"]]
        renderer(prs, s)

    prs.save(OUT_PATH)
    print(f"OK — {len(prs.slides)} slides guardadas en {OUT_PATH}")


if __name__ == "__main__":
    main()
