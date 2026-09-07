# Unidad 3 — Clase: Pruebas Unitarias con Unity (guion docente)

**Materia:** Diseño según Plataformas de Juego
**Carrera:** Tecnicatura Universitaria en Diseño Integral de Videojuegos (Plan 2020)
**Docente:** Ing. Elsa Daniela Ramírez
**Ciclo lectivo:** 2026
**Unidad:** 3 — Pruebas Unitarias con Unity
**Duración:** 120 minutos
**Resultados de aprendizaje / competencias vinculados:** RA01, RA03 · CE02, CE05, CE06, CE07, CE12 (ver justificación en [`01-analisis-programa-y-objetivos.md`](./01-analisis-programa-y-objetivos.md), Sección F).

Metodología AMMIL / flipped-classroom del programa: se asume que los estudiantes ya vieron la píldora de video y el apunte de esta semana antes de la clase. Esta clase abre el tramo de la Semana 6, que el cronograma dedica íntegramente a Unidad III, y alimenta el **Trabajo Práctico N° 2**.

---

## Sección O — Estructura completa de la clase

```
1. El problema: CombatSystem cambia y Player.TakeDamage() deja de funcionar bien
        ↓
2. ¿Qué es una prueba unitaria? Arrange / Act / Assert
        ↓
3. Unit test ≠ game testing: tabla comparativa completa
        ↓
4. Testing en videojuegos: buenos candidatos vs. casos complejos + beneficios y límites
        ↓
5. Unity Test Framework (Test Runner): qué es, cómo crear y ejecutar un test
        ↓
6. Edit Mode vs. Play Mode
        ↓
7. Primer test en vivo: PASS → FAIL provocado → corrección → PASS
        ↓
8. TDD: Red-Green-Refactor sobre PlayerExperience
        ↓
9. Casos progresivos de Cryptbound + pruebas manuales vs. automatizadas
        ↓
10. Conexión con Unidad 2 (Jira, regresión) + errores conceptuales frecuentes
        ↓
11. Lanzamiento de la actividad práctica (TP N°2)
        ↓
12. Cierre y preguntas
```

---

## Guía de tiempos (120 min)

| # | Min | Bloque | Objetivo del bloque |
|---|-----|--------|----------------------|
| 1 | 0–10 | El problema: una regresión real | Instalar la necesidad antes de nombrar la herramienta |
| 2 | 10–25 | ¿Qué es una prueba unitaria? | Definir con rigor, patrón AAA |
| 3 | 25–40 | Unit testing vs. game testing | Evitar la confusión conceptual central de la unidad |
| 4 | 40–55 | Testing en videojuegos: candidatos y límites | Instalar que no todo se automatiza, sin desalentar la práctica |
| 5 | 55–70 | Unity Test Framework | Presentar la herramienta como consecuencia, no como punto de partida |
| 6 | 70–85 | Edit Mode vs. Play Mode | Concepto central de la unidad — tabla y criterio de decisión |
| 7 | 85–100 | TDD: Red-Green-Refactor | Ciclo completo, no solo la definición |
| 8 | 100–110 | Casos progresivos + manual vs. automatizado | Consolidar con ejemplos y estrategia combinada |
| 9 | 110–115 | Conexión con Unidad 2 + errores conceptuales | Cerrar el círculo con Jira/regresión, corregir mitos |
| 10 | 115–120 | Lanzamiento de TP N°2 y cierre | Dejar la actividad instalada y conectar con Unidad 4 |

**Total: 120 minutos.**

---

## Desarrollo por bloque

### Bloque 1 (0–10 min) — El problema: una regresión real

**Objetivo:** que la clase sienta el problema antes de escuchar la palabra "test".

**Contenido:** Cryptbound pasó de build 0.3 a build 0.4. Iñaki agregó golpes críticos a `CombatSystem`. Nadie tocó `PlayerHealth`. Tres días después, en el playtest, Marisol reporta: *"a veces el mismo golpe le saca el doble de vida al enemigo, no siempre, es rarísimo"*.

**Qué decir:** "La build 0.3 funcionaba. La 0.4 tiene un bug que nadie metió a propósito en `TakeDamage`. ¿Cómo puede romperse algo que nadie tocó?" Mostrar el diagrama de regresión (ver [`02-caso-practico-testing-videojuego.md`](./02-caso-practico-testing-videojuego.md), Sección F) y nombrar el concepto: **regresión**.

**Ejemplo:** CRYPT-201 (Sección I del caso práctico).

**Pregunta:** "Si esto se descubre recién en el playtest, ¿cuántos días de trabajo puede llevar encontrar *cuál* cambio lo causó?"

**Demostración:** ninguna todavía — es apertura conceptual.

**Error conceptual a evitar:** que quede la idea de que este bug es "un error de programación de Iñaki" y no un problema de *proceso*. El énfasis debe estar en "¿cómo lo hubiéramos sabido en segundos, no en tres días?", no en señalar a la persona.

**Duración:** 10 min.

---

### Bloque 2 (10–25 min) — ¿Qué es una prueba unitaria?

**Objetivo:** definición rigurosa y patrón AAA, con el mínimo vocabulario técnico necesario.

**Contenido:** "Una prueba unitaria verifica automáticamente un comportamiento específico de una unidad de código bajo determinadas condiciones." Arrange / Act / Assert.

**Qué decir:** repasar en 30 segundos (no reexplicar) que Unidad 1 ya distinguió el nivel *unitario* de integración/sistema/aceptación, y que Unidad 2 ya diseñó test cases con campos formales — hoy esos mismos test cases se escriben como código que se ejecuta solo.

**Ejemplo:**
```
ARRANGE: Player con 100 HP
ACT:     Player recibe 25 de daño
ASSERT:  HP == 75
```
seguido de inmediato por su equivalente en C#/NUnit (ver caso práctico, Sección C).

**Pregunta:** "¿En qué se parece esto a los campos de un test case de Unidad 2 (precondición, pasos, resultado esperado)?" — objetivo: que la clase misma note que Arrange=precondición, Act=pasos, Assert=resultado esperado vs. real.

**Demostración:** mostrar lado a lado la tabla TC-001 de Unidad 2 y el test de `PlayerHealth` — mismos campos, distinto soporte (papel vs. código).

**Error conceptual a evitar:** "un test unitario prueba muchas cosas a la vez" — reforzar que un buen test verifica **un** comportamiento.

**Duración:** 15 min.

---

### Bloque 3 (25–40 min) — Unit testing vs. game testing (no confundir)

**Objetivo:** instalar la distinción que el programa exige explícitamente.

**Contenido:** tabla comparativa Unit Test / Integration Test / Functional Test / Playtest / QA manual / Automated Test (ver [`04-diapositivas.md`](./04-diapositivas.md) para la tabla completa con columnas Tipo / Qué prueba / Automatizable / Ejemplo).

**Qué decir:** "Un unit test **nunca** juega el nivel completo. Si alguien me dice 'hice un test unitario que juega la mazmorra entera', ya no es un test unitario — es, en el mejor de los casos, un test de sistema."

**Ejemplo:** `EnemyArcher_EntersAlertState_AtExactDetectionRange` (unit/integration acotado, Play Mode) vs. "un tester recorre las 3 salas buscando bugs" (playtest/QA manual, no automatizable con NUnit).

**Pregunta:** "El caso TC-A01 de Unidad 2 (ataque cuerpo a cuerpo conecta con el enemigo) — ¿lo probarían con unit test, integration test o requiere a una persona jugando?"

**Demostración:** clasificar en vivo, entre todos, 4 casos sueltos del backlog de Cryptbound.

**Error conceptual a evitar:** "unit test = probar el videojuego completo" — es el primer ítem de la Sección de errores conceptuales; conviene nombrarlo explícitamente acá, no solo al final.

**Duración:** 15 min.

---

### Bloque 4 (40–55 min) — Testing en videojuegos: candidatos y límites

**Objetivo:** que la clase sepa distinguir, con criterio propio, qué merece un unit test.

**Contenido:** dos columnas — "muy buenos candidatos" (cálculo de daño, puntuación, inventario, cooldown, estados) vs. "más complejos" (físicas, animación, iluminación, rendering, sensación del gameplay). Beneficios (detección temprana, prevención de regresiones, feedback rápido, refactoring seguro, documentación ejecutable) y límites (Sección 11 del programa: bugs visuales, UX, balance, rendimiento no capturado, integración, assets).

**Qué decir:** frase ancla del programa: *"Automatizar pruebas no significa eliminar las pruebas manuales."* Y la fórmula de cierre: `UNIT TESTS + INTEGRATION TESTS + AUTOMATED TESTS + MANUAL QA + PLAYTEST = ESTRATEGIA DE CALIDAD`.

**Ejemplo:** contrastar `PlayerHealth.TakeDamage` (excelente candidato) con "¿el cooldown del ataque se *siente* bien" (queja real de Unidad 2, descartada ahí como opinión de diseño, no bug) — no se puede automatizar con `Assert`.

**Pregunta:** "¿Por qué CRYPT-111 (caída de FPS en la sala del jefe, Unidad 2) no se resuelve con un unit test?"

**Demostración:** ninguna de código — es la sección más conceptual del bloque.

**Error conceptual a evitar:** "los unit tests eliminan los bugs" → corregir a "reducen el riesgo de determinados defectos y permiten detectar regresiones de forma temprana." Y el inverso: "si todos los tests pasan, el juego no tiene bugs" — falso, ver Sección 11.

**Duración:** 15 min.

---

### Bloque 5 (55–70 min) — Unity Test Framework

**Objetivo:** presentar la herramienta recién ahora, como consecuencia de todo lo anterior.

**Contenido:** qué es Unity Test Framework (integración de NUnit dentro de Unity), cómo se crea la carpeta de tests y el *assembly definition* (`Window ▸ General ▸ Test Runner` → *Create Test Assembly Folder*, o `Assets ▸ Create ▸ Testing ▸ Test Assembly Folder`), cómo se crea un script de test, cómo se ejecuta (*Run All* / *Run Selected*) y cómo se lee Pass ✅ / Fail ❌.

**Qué decir:** dato técnico preciso a marcar: el asmdef generado ya referencia `nunit.framework.dll`, `UnityEngine.TestRunner` y `UnityEditor.TestRunner` — por eso el código de test puede usar `using NUnit.Framework;` sin configurar nada más. Mencionar brevemente que en Unity 6 el Test Framework va empaquetado con el Editor (no se administra por separado en el Package Manager como en versiones LTS anteriores) — ver [`06-investigacion-recursos.md`](./06-investigacion-recursos.md) para el detalle verificado por versión.

**Ejemplo:** recorrido de las diapositivas [RECICLADO 2024] (ver [`04-diapositivas.md`](./04-diapositivas.md)) adaptadas a Cryptbound en vez de Crashteroids.

**Pregunta:** "¿Por qué el código de test vive en una carpeta separada (`Tests`) con su propio ensamblado, en vez de mezclarse con `Assets/Scripts`?"

**Demostración:** crear en vivo la carpeta `Tests`, el asmdef, y el primer script vacío — sin escribir el test todavía (eso es el Bloque 7).

**Error conceptual a evitar:** dar un tour exhaustivo de cada botón de la interfaz como si fuera un tutorial de clics — el foco es el flujo (crear carpeta → crear test → ejecutar → leer resultado), no memorizar la UI.

**Duración:** 15 min.

---

### Bloque 6 (70–85 min) — Edit Mode vs. Play Mode

**Objetivo:** concepto central de la unidad — que la clase pueda decidir correctamente cuál usar.

**Contenido:** tabla completa (ver diapositivas) — Edit Mode no soporta corrutinas y corre sin instanciar la escena de juego (rápido, ideal para lógica pura); Play Mode corre como corrutina real vía `[UnityTest]` con `IEnumerator`, permite `yield return null` para avanzar frames, y es necesario para cualquier cosa que dependa de `MonoBehaviour`, `GameObject` o tiempo de ejecución real.

**Qué decir:** "La pregunta que decide el modo no es '¿qué prefiero?' — es '¿mi código depende de la escena de Unity corriendo?'. Si la respuesta es no (como `PlayerHealth` o `Inventory`), Edit Mode. Si es sí (como `CombatSystem` o `EnemyArcher`), Play Mode."

**Ejemplo:** `PlayerHealthTests` (Edit Mode) vs. `EnemyArcherTests` (Play Mode) — mismo proyecto, decisión distinta, y por qué.

**Pregunta:** "`Inventory.AddItem` no toca ninguna escena ni GameObject — ¿Edit Mode o Play Mode? ¿Y un test que verifica que el HUD se actualiza cuando cambia el inventario?"

**Demostración:** mostrar el código de `EnemyArcherTests` y señalar el `[UnityTest]` + `IEnumerator` + `yield return null` como las tres marcas que delatan un test de Play Mode.

**Error conceptual a evitar:** "Play Mode siempre es mejor que Edit Mode" — Edit Mode es más rápido y debería preferirse siempre que el código lo permita; Play Mode es necesario, no superior.

**Duración:** 15 min.

---

### Bloque 7 (85–100 min) — Primer test en vivo: PASS, FAIL provocado, corrección

**Objetivo:** la demostración pedagógica central de toda la unidad (ver programa, punto 14).

**Contenido:** recorrido completo de la Sección C del caso práctico: escribir `PlayerHealthTests.TakeDamage_ReducesHealthByAmount`, ejecutar (PASS), romper `TakeDamage` a propósito quitando el `Mathf.Max`, agregar `TakeDamage_NeverGoesBelowZero`, ejecutar (FAIL, leer el mensaje `Expected: 0, But was: -50`), corregir, ejecutar de nuevo (PASS).

**Qué decir:** al llegar al FAIL: "Esto que están viendo en rojo no es que algo se rompió en la clase — es la prueba haciendo exactamente su trabajo: avisar antes de que este bug llegara a un playtest."

**Ejemplo:** el propio código en vivo.

**Pregunta:** "¿Qué hubiera pasado si este bug (vida negativa) llegaba al playtest de Unidad 2 en vez de detectarse acá?"

**Demostración:** en vivo, en el editor — es el corazón del bloque, no debe recortarse aunque falte tiempo en otro lado.

**Error conceptual a evitar:** que el fallo provocado se viva como un error del docente ("se rompió la demo") en vez de como el resultado esperado del ejercicio — anticiparlo explícitamente antes de ejecutar: "ahora voy a romper el código a propósito".

**Duración:** 15 min.

---

### Bloque 8 (100–110 min) — TDD: Red-Green-Refactor

**Objetivo:** que la clase viva el ciclo completo, no solo la definición.

**Contenido:** `PlayerExperience` construido con TDD (ver caso práctico, Sección H) — RED (test que no compila/falla) → GREEN (implementación mínima) → REFACTOR → se repite con el umbral de nivel.

**Qué decir:** frase ancla: "TDD no es simplemente 'hacer tests'. Es una estrategia de desarrollo donde las pruebas guían la implementación — el test se escribe *antes* de que el código exista, no después." Mencionar cuándo conviene (lógica de dominio, reglas, cálculos deterministas — inventario, combate, XP) y cuándo no (prototipado visual rápido, shaders, animación, exploración de gameplay): "usar TDD donde aporte valor, no convertirlo en dogma."

**Ejemplo:** el ciclo completo de `PlayerExperience` (dos vueltas: ganar XP, subir de nivel).

**Pregunta:** "¿Por qué escribir el test antes obliga a pensar primero en el *comportamiento* esperado en vez de en la implementación?"

**Demostración:** en vivo, siguiendo el código de la Sección H — mostrar el fallo de compilación (RED real, no solo un `Assert` fallido) como parte válida del ciclo.

**Error conceptual a evitar:** "TDD significa escribir tests después del código" — es exactamente lo opuesto; y "más tests siempre significa mejor calidad" — TDD no es una carrera por cantidad de tests, cada test responde a un requisito concreto del ciclo.

**Duración:** 10 min.

---

### Bloque 9 (110–115 min) — Conexión con Unidad 2 + errores conceptuales

**Objetivo:** cerrar el círculo con la gestión de bugs ya aprendida y despejar los mitos más comunes antes de la actividad.

**Contenido:** el flujo `USER STORY → IMPLEMENTACIÓN → UNIT TEST → CODE REVIEW → INTEGRATION → PLAYTEST → BUG → JIRA → FIX → REGRESSION TEST`, con CRYPT-201 como hilo conductor (bug detectado → ticket → fix → test de regresión → protegido). Repaso relámpago de 3-4 errores conceptuales de la Sección de errores (ver [`03-clase-guion-docente.md`](#errores-conceptuales-frecuentes-repaso-r%C3%A1pido) más abajo), priorizando los que la clase mostró confundir en bloques anteriores.

**Qué decir:** "Jira no cambia en esta unidad — lo que cambia es que ahora parte de lo que antes hacía Marisol a mano (retestear después de un fix) lo puede hacer, para este tipo de bugs, un test que corre solo."

**Ejemplo:** CRYPT-201 completo, de punta a punta.

**Pregunta:** "¿Todos los bugs de Unidad 2 se podrían haber protegido con un test así? ¿Cuáles no, y por qué?" (respuesta esperada: CRYPT-102/UI, CRYPT-106/UI, CRYPT-110/typo, CRYPT-111/rendimiento — no son buenos candidatos).

**Demostración:** ninguna de código — cierre conceptual.

**Error conceptual a evitar:** no convertir esto en una clase nueva de Jira — es solo el puente, 5 minutos.

**Duración:** 5 min.

---

### Bloque 10 (115–120 min) — Lanzamiento de TP N° 2 y cierre

**Objetivo:** dejar la actividad instalada y conectar con lo que sigue.

**Contenido:** presentar la consigna del TP N° 2 (ver [`05-actividad-practica-y-evaluacion.md`](./05-actividad-practica-y-evaluacion.md)) — los equipos reciben `PlayerHealth` sin tests y deben escribir la suite completa, encontrar y corregir un fallo real, y agregar un test de regresión. Mencionar en 1 minuto que esto puede escalar a integración continua (Git → CI → build → tests automáticos → resultado) sin desarrollarlo — queda fuera del alcance de esta unidad.

**Qué decir:** frase de cierre (las tres ideas centrales del programa, dichas explícitamente):
> "No hacemos pruebas unitarias porque Unity tenga un Test Runner. Las hacemos porque necesitamos aumentar la confianza en el comportamiento del código y detectar regresiones rápido. Las pruebas automatizadas complementan, no reemplazan, el QA manual y el playtesting. Y TDD no significa 'hacer más tests' — significa usarlos como parte del proceso de diseño."

**Pregunta de cierre:** "¿Qué sistema de un juego que estén programando ustedes mismos se beneficiaría hoy de un test como los que vimos?"

**Demostración:** ninguna.

**Error conceptual a evitar:** dejar la sensación de que la clase terminó "aprendiendo Test Runner" en vez de "aprendiendo por qué automatizar y cuándo".

**Duración:** 5 min.

---

## Errores conceptuales frecuentes (repaso rápido)

Ver el desarrollo completo, con la corrección de cada uno, en [`05-actividad-practica-y-evaluacion.md`](./05-actividad-practica-y-evaluacion.md) (Sección de análisis) y en la diapositiva de cierre correspondiente en [`04-diapositivas.md`](./04-diapositivas.md). En clase se repasan 3-4 según lo que haya generado dudas, no las diez de corrido.

## Notas de contenido por bloque (referencias cruzadas)

- **Bloque 1 (regresión):** desarrollo completo en [`02-caso-practico-testing-videojuego.md`](./02-caso-practico-testing-videojuego.md), Sección F.
- **Bloque 2-3 (AAA, unit vs. game testing):** tablas completas en [`04-diapositivas.md`](./04-diapositivas.md).
- **Bloque 5-6 (Test Framework, Edit/Play Mode):** fuentes oficiales verificadas en [`06-investigacion-recursos.md`](./06-investigacion-recursos.md).
- **Bloque 7 (demo PASS/FAIL):** código completo y guion paso a paso en [`02-caso-practico-testing-videojuego.md`](./02-caso-practico-testing-videojuego.md), Sección C.
- **Bloque 8 (TDD):** ciclo completo con las dos vueltas en [`02-caso-practico-testing-videojuego.md`](./02-caso-practico-testing-videojuego.md), Sección H.
- **Diapositivas sugeridas por bloque:** ver [`04-diapositivas.md`](./04-diapositivas.md) (36 slides numeradas, mapeadas a estos mismos bloques, con las heredadas de `docs/Unidad 3 -2024.pptx` marcadas [RECICLADO 2024]).
- **Ejemplos de respuesta para cada pregunta y material de apoyo para los ejercicios en vivo (incluidos los 4 casos del ejercicio de clasificación del Bloque 3):** ver [`07-ejemplos-y-respuestas-de-apoyo.md`](./07-ejemplos-y-respuestas-de-apoyo.md), organizado con la misma numeración de bloques que este guion.
