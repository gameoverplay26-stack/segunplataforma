# Unidad 3 — Presentación (slide por slide)

36 diapositivas — mismo número que `docs/Unidad 3 -2024.pptx` (material previo del docente) y que la Unidad 2. Las marcadas **[RECICLADO 2024]** reutilizan la estructura técnica de esa presentación (basada en el tutorial oficial de Unity Learn "Unit Testing", proyecto Crashteroids), adaptada al hilo conductor de Cryptbound en vez del proyecto original — ver justificación en [`01-analisis-programa-y-objetivos.md`](./01-analisis-programa-y-objetivos.md), Sección A.

Formato por slide: **Objetivo pedagógico** · **Contenido visible** · **Visual sugerido** · **Notas del docente** · **Ejemplo de videojuego** · **Pregunta al alumno** (los campos que no aplican se omiten). "NO saturar de texto" — este documento es la fuente de contenido para armar la diapositiva real, no el texto literal que va en pantalla.

---

**01 — Portada**
- Contenido visible: Unidad III — Pruebas Unitarias con Unity · Diseño según Plataformas de Juego.
- Visual sugerido: un test en rojo (FAIL) transformándose en verde (PASS), como imagen de portada.

**02 — Objetivos de la clase**
- Objetivo: que el estudiante sepa qué va a poder hacer al final.
- Contenido visible: los 10 objetivos específicos, resumidos en 4-5 líneas (Sección D, `01-analisis-programa-y-objetivos.md`).
- Pregunta al alumno: ¿alguna vez modificaron algo en un proyecto propio y rompieron, sin querer, otra parte que ya andaba?

**03 — El problema: build 0.4, un golpe raro**
- Objetivo: instalar el problema real antes de cualquier definición.
- Contenido visible: el reporte de Marisol — "a veces el mismo golpe le saca el doble de vida al enemigo, no siempre".
- Ejemplo: Cryptbound build 0.4, sistema Combat.
- Pregunta al alumno: ¿esto suena a un bug nuevo o a algo que dejó de funcionar?

**04 — Regresión: cuando algo que andaba deja de andar**
- Objetivo: nombrar el concepto de regresión con precisión.
- Contenido visible: diagrama `Player.TakeDamage() v1 funciona → se modifica CombatSystem → v2 ya no funciona`.
- Visual sugerido: línea de tiempo build 0.3 → 0.4 con un ✅ que se vuelve ❌.
- Notas del docente: evitar personalizar el error en "el programador" — el foco es el proceso, no la culpa.

**05 — Repaso relámpago: Unidad I → II → III**
- Objetivo: anclar vocabulario ya visto sin reexplicar desde cero.
- Contenido visible: línea de tiempo — error/defecto/fallo (U1), test case/severidad/regression testing (U2), automatización de ese mismo test case (U3).
- Notas del docente: 30 segundos, no una clase nueva.

**06 — ¿Qué es una prueba unitaria?**
- Objetivo: definición formal y comprensible.
- Contenido visible: "Una prueba unitaria verifica automáticamente un comportamiento específico de una unidad de código bajo determinadas condiciones."
- Notas del docente: distinguir de inmediato "unidad" ≠ "el juego completo".

**07 — Arrange / Act / Assert**
- Contenido visible: los 3 pasos, con flechas.
- Visual sugerido: diagrama vertical ARRANGE → ACT → ASSERT.
- Notas del docente: mismos campos que un test case de Unidad 2 (precondición/pasos/resultado esperado), dicho explícitamente.

**08 — AAA aplicado a Cryptbound**
- Contenido visible: `ARRANGE: Player con 100 HP · ACT: recibe 25 de daño · ASSERT: HP == 75`.
- Ejemplo: `PlayerHealth`.

**09 — El mismo ejemplo, en C# con NUnit**
- Contenido visible: el bloque de código `PlayerHealthTests.TakeDamage_ReducesHealthByAmount`.
- Notas del docente: señalar `using NUnit.Framework;` y el atributo `[Test]` sin profundizar todavía en Test Runner (eso viene en el bloque 5 del guion).

**10 — No confundir: tipos de testing**
- Objetivo: instalar la distinción central del programa (Sección 8 del encargo).
- Contenido visible: tabla completa.

| Tipo | Qué prueba | Automatizable | Ejemplo en Cryptbound |
|---|---|---|---|
| Unit Test | Una unidad aislada de código | Sí | `PlayerHealth.TakeDamage` |
| Integration Test | Interacción entre componentes | Sí (con más esfuerzo) | `CombatSystem` aplicando daño a `PlayerHealth` vía Play Mode |
| Functional Test | Una funcionalidad completa | Parcial | "Al derrotar al jefe se reproduce su animación de derrota" |
| Playtest | Una persona juega y evalúa | No | Sesión de 90 min que generó el backlog de Unidad 2 |
| QA manual | Verificación humana siguiendo un plan | No | Ejecutar TC-A01/TC-R01/TC-E01 a mano |
| Automated Test | Cualquier prueba ejecutada por una máquina | Por definición, sí | Toda la suite de `Assets/Tests` corriendo en Test Runner |

- Notas del docente: remarcar que Playtest y QA manual **no son inferiores** — son insustituibles para lo que un `Assert` no puede evaluar.

**11 — Ejercicio rápido en vivo**
- Objetivo: practicar la clasificación antes de seguir.
- Contenido visible: 4 casos sueltos del backlog de Cryptbound para clasificar entre todos.
- Notas del docente: 5 minutos, votación a mano alzada.

**12 — Buenos candidatos para unit testing**
- Contenido visible: cálculo de daño, puntuación, inventario, reglas, cooldown, conversión de estadísticas, validaciones, estados, cálculos matemáticos.
- Ejemplo: `Inventory.AddItem`, `PlayerExperience.GainExperience`.

**13 — Casos más complejos para unit testing**
- Contenido visible: físicas, animaciones, iluminación, rendering, UX, sensación del gameplay, timing visual, diversión.
- Ejemplo: la animación de derrota del jefe (CRYPT-108, Unidad 2) — se verifica jugando, no con `Assert`.

**14 — Beneficios de las pruebas unitarias**
- Contenido visible: detección temprana, prevención de regresiones, feedback rápido, refactoring más seguro, mantenibilidad, documentación ejecutable, confianza para modificar código.
- Notas del docente: frase a decir literal — "reducen el riesgo de determinados defectos y permiten detectar regresiones temprano", nunca "eliminan los bugs".

**15 — Qué NO solucionan las pruebas unitarias**
- Contenido visible: bugs visuales, UX, diseño, diversión, balance, rendimiento no capturado, integración, assets, iluminación, animación, físicas complejas.
- Ejemplo: CRYPT-111 (caída de FPS), la queja de "el combate se siente lento" (Unidad 2).

**16 — Estrategia de calidad**
- Contenido visible: `UNIT TESTS + INTEGRATION TESTS + AUTOMATED TESTS + MANUAL QA + PLAYTEST = ESTRATEGIA DE CALIDAD`.
- Visual sugerido: diagrama de capas o de suma, no una lista.

**17 — [RECICLADO 2024] Unity Test Framework: qué es**
- Objetivo: presentar la herramienta recién ahora, como consecuencia.
- Contenido visible: "Unity Test Framework es la función de pruebas unitarias que ofrece Unity, y por dentro utiliza NUnit."
- Notas del docente: la afirmación viene textual del material 2024 y sigue vigente — Unity Test Framework es, oficialmente, una integración de NUnit dentro de Unity (ver [`06-investigacion-recursos.md`](./06-investigacion-recursos.md)).

**18 — [RECICLADO 2024] Verificar el paquete**
- Contenido visible: `Window ▸ Package Manager ▸ Unity Registry ▸ Test Framework`.
- Notas del docente: en Unity 6, el Test Framework es un paquete "core" fijo a la versión del Editor — mencionarlo brevemente si la cátedra usa Unity 6 (ver nota de versiones en `06-investigacion-recursos.md`).

**19 — [RECICLADO 2024] Abrir Test Runner**
- Contenido visible: `Window ▸ General ▸ Test Runner`.
- Visual sugerido: captura de la ventana Test Runner acoplada junto al Inspector.

**20 — [RECICLADO 2024] Crear la carpeta de tests**
- Contenido visible: botón "Create Test Assembly Folder" → carpeta `Tests` con `Tests.asmdef`.
- Notas del docente: el asmdef ya trae referencias a `nunit.framework.dll`, `UnityEngine.TestRunner` y `UnityEditor.TestRunner` — por eso el test puede usar `using NUnit.Framework;` sin configurar nada más.

**21 — [RECICLADO 2024] Crear GameAssembly y referenciarlo**
- Contenido visible: `Assets/Scripts ▸ Create ▸ Assembly Definition` → nombrarlo `GameAssembly` → agregarlo como referencia del asmdef de `Tests`.
- Notas del docente: sin este paso, el código de test no puede "ver" las clases del juego (`PlayerHealth`, `Inventory`, etc.) — es el motivo técnico detrás del paso, no solo un trámite.

**22 — [RECICLADO 2024, adaptado] Qué es un Test Suite**
- Contenido visible: "Un archivo de clase que contiene pruebas unitarias se llama Test Suite. Se organizan por agrupación lógica: `PlayerHealthTests`, `InventoryTests`, `CombatSystemTests`."
- Ejemplo: la estructura de carpetas de Cryptbound (Sección B, `02-caso-practico-testing-videojuego.md`).

**23 — Edit Mode vs. Play Mode**
- Objetivo: concepto central de la unidad.
- Contenido visible: tabla comparativa.

| Característica | Edit Mode | Play Mode |
|---|---|---|
| Ejecuta escena real | No | Sí |
| Requiere runtime / GameObject | No | Sí |
| Soporta corrutinas | No | Sí, vía `[UnityTest]` + `IEnumerator` |
| Velocidad | Rápido | Más lento (instancia escena, avanza frames) |
| Uso recomendado | Lógica pura: cálculos, reglas, inventario, daño, XP | `MonoBehaviour`, interacción entre componentes, tiempo real |
| Ejemplo en Cryptbound | `PlayerHealthTests`, `InventoryTests` | `CombatSystemTests`, `EnemyArcherTests` |

**24 — Cuándo usar Edit Mode**
- Ejemplo: `PlayerHealth`, `Inventory`, `PlayerExperience` — clases C# puras, sin heredar de `MonoBehaviour`.
- Notas del docente: separar la lógica de reglas del código dependiente del motor es, en sí mismo, una buena práctica que hace el código más testeable.

**25 — Cuándo usar Play Mode**
- Ejemplo: `CombatSystem`, `EnemyArcher` — `MonoBehaviour`, dependen de posición, tiempo (`Time.time`) y frames.
- Pregunta al alumno: `Inventory.AddItem` no toca ninguna escena — ¿Edit Mode o Play Mode?

**26 — Primer test: el código**
- Contenido visible: `PlayerHealthTests.TakeDamage_ReducesHealthByAmount` completo.
- Notas del docente: es la demostración pedagógica central — no acelerar este tramo.

**27 — Ejecutar: PASS ✅**
- Visual sugerido: captura del Test Runner con el ícono verde.
- Notas del docente: anticipar en voz alta qué se espera ver antes de correr el test.

**28 — Provocar el fallo a propósito**
- Contenido visible: se quita `Mathf.Max(0, ...)` de `TakeDamage`, se agrega `TakeDamage_NeverGoesBelowZero`.
- Notas del docente: avisar explícitamente "ahora voy a romper el código a propósito" antes de ejecutar.

**29 — FAIL ❌, corrección, PASS de nuevo**
- Contenido visible: mensaje de error `Expected: 0, But was: -50`; luego el fix y el resultado en verde.
- Pregunta al alumno: ¿qué hubiera pasado si este bug llegaba al playtest en vez de detectarse acá?

**30 — Ejemplos progresivos**
- Contenido visible: curación (`Heal_IncreasesHealthByAmount`), no superar el máximo, muerte (`IsDead`), inventario (`AddItem_PotionIsInInventory`), cooldown de ataque.
- Notas del docente: recorrer rápido — el detalle completo está en `02-caso-practico-testing-videojuego.md`, Secciones D y E.

**31 — Buenas prácticas al escribir tests**
- Contenido visible: un comportamiento por test, nombres descriptivos (`Método_Escenario_ResultadoEsperado`), tests deterministas (evitar `Random` sin controlar), aislar unidades, no depender del orden de ejecución, limpiar recursos, AAA siempre, probar comportamiento — no implementación interna.
- Ejemplo: el problema del test con `Random.value` en `CombatSystem` (Sección F, `02-caso-practico-testing-videojuego.md`) — un test que a veces pasa y a veces falla sin que el código haya cambiado es un test frágil.

**32 — TDD: qué es y el ciclo Red-Green-Refactor**
- Contenido visible: `RED → escribir test que falla → GREEN → implementar lo mínimo → REFACTOR → mejorar sin romper tests → repetir`.
- Notas del docente: frase ancla — "TDD no es simplemente 'hacer tests'; es una estrategia de desarrollo donde las pruebas guían la implementación."

**33 — TDD en Cryptbound: PlayerExperience**
- Contenido visible: recorrido de las dos vueltas completas (ganar XP → subir de nivel) — RED, GREEN, REFACTOR de cada una.
- Notas del docente: mostrar el fallo de **compilación** de la primera vuelta como RED válido, no solo un `Assert` fallido.

**34 — TDD: cuándo sí, cuándo no**
- Contenido visible: buenos candidatos (lógica de dominio, reglas, cálculos deterministas, inventario, combate, scoring) vs. menos conveniente (prototipado rápido, shaders, animación, diseño de niveles, exploración de gameplay).
- Notas del docente: "usar TDD donde aporte valor, no convertirlo en dogma."

**35 — Pruebas manuales vs. automatizadas**
- Contenido visible: dos columnas — Manual (ventajas: exploración, percepción humana, UX, descubrimiento inesperado; límites: lento, repetitivo, costoso a escala) / Automatizada (ventajas: velocidad, repetibilidad, regresión, ejecución frecuente; límites: costo inicial, mantenimiento, cobertura limitada, no sustituye juicio humano).
- Notas del docente: mencionar en una frase que esto puede escalar a integración continua (Git → CI → build → tests automáticos) sin desarrollarlo — no es contenido de esta unidad.

**36 — Cierre: conexión con Unidad 2, errores conceptuales y TP N° 2**
- Contenido visible: flujo `BUG → JIRA → FIX → UNIT TEST DE REGRESIÓN → PROTEGIDO`, con CRYPT-201 como ejemplo; repaso de 3-4 errores conceptuales (ver [`05-actividad-practica-y-evaluacion.md`](./05-actividad-practica-y-evaluacion.md)); lanzamiento de la consigna del TP N° 2.
- Pregunta al alumno: ¿qué sistema de un juego propio se beneficiaría hoy de un test como los que vimos?
