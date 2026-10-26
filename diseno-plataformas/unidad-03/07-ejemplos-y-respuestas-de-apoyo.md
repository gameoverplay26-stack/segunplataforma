# Unidad 3 — Ejemplos y respuestas de apoyo

Referencia rápida para el día de la clase. Cubre, bloque por bloque (misma numeración que [`03-clase-guion-docente.md`](./03-clase-guion-docente.md)), tanto las **preguntas al alumno** (con ejemplos de respuesta esperable) como el **material de apoyo que las diapositivas mencionan pero no desarrollan** — por ejemplo, la Slide 11 pide "clasificar 4 casos sueltos del backlog" sin decir cuáles: acá están, con la clasificación resuelta.

**Cómo usarlo en clase:** no son respuestas para leer en voz alta antes de preguntar — son para tenerlas a mano si la clase queda en silencio, para reconocer una respuesta que va por el camino equivocado, o para tener un segundo ejemplo si el primero no cierra.

---

## Apertura (antes del Bloque 1) — Slides 2 y 3

**Pregunta (Slide 2):** ¿alguna vez modificaron algo en un proyecto propio y rompieron, sin querer, otra parte que ya andaba?

- "Cambié la velocidad de movimiento del jugador para que se sienta mejor, y el salto empezó a fallar porque el cálculo de gravedad dependía de esa velocidad."
- "Agregué un nuevo tipo de enemigo y, sin darme cuenta, el sistema de puntaje empezó a sumar el doble por cada kill."
- "Refactoricé una clase `Player` para ordenarla y me olvidé de que el sistema de guardado leía un campo público que dejé de exponer — el juego cargaba partidas vacías."
- Si nadie tiene un ejemplo propio: "¿vieron a alguien más que le pasara — un compañero de equipo, un video de un dev arreglando un bug en vivo?"

**Pregunta (Slide 3):** ¿esto suena a un bug nuevo, o a algo que dejó de funcionar?

- **Respuesta ingenua a corregir:** "Es un bug nuevo, nunca habíamos visto que el golpe hiciera el doble de daño." → No es "nuevo" en el sentido de nunca-antes-posible: algo que *ya funcionaba* (`TakeDamage` aplicando el daño una vez) dejó de funcionar al tocar `CombatSystem`. La pista está en el propio relato de Marisol: "no siempre" pasa — el comportamiento base seguía andando, pero el cambio introdujo el problema.
- **Respuesta esperada:** "Suena a que algo que ya funcionaba se rompió con el cambio del golpe crítico — una regresión."
- **Contraste útil:** si el jefe nunca hubiera tenido animación de derrota (CRYPT-108, Unidad 2), eso NO sería regresión — nunca funcionó. Achicar la vida al doble sí lo es.

**Ejemplo adicional de regresión** (por si hace falta un segundo caso, más allá de CombatSystem): "Se optimiza el pathfinding del arquero para que persiga más rápido, y ahora el enemigo se queda trabado contra la puerta de la sala 2 — algo que antes (con el pathfinding viejo, más lento) nunca pasaba."

---

## Bloque 1 (0–10 min) — El problema: una regresión real

**Pregunta:** si esto se descubre recién en el playtest, ¿cuántos días de trabajo puede llevar encontrar cuál cambio lo causó?

- "Si el playtest es cada 2-3 días, y el bug pasó desapercibido en el primero, puede tardar una semana entera en descubrirse."
- "Y una vez descubierto, hay que revisar todos los commits entre la build 0.3 y la 0.4 para encontrar cuál tocó `CombatSystem` — horas de `git bisect` manual, o de memoria de quién tocó qué."
- **Gancho de cierre del bloque:** "Con un test como el que vamos a escribir hoy, esto se detecta en segundos, apenas alguien corre el Test Runner después de cambiar el código."

---

## Bloque 2 (10–25 min) — ¿Qué es una prueba unitaria?

**Pregunta:** ¿en qué se parece esto a los campos de un test case de Unidad 2 (precondición, pasos, resultado esperado)?

- "Arrange es la precondición: cómo dejamos el escenario antes de actuar."
- "Act son los pasos de ejecución: lo que se hace."
- "Assert es el resultado esperado vs. el resultado real — si no coinciden, el test queda 'Fallido', igual que en la tabla de Unidad 2."
- **Frase de cierre sugerida:** "No es una herramienta nueva reemplazando el concepto — es el mismo test case, ahora ejecutado por una máquina en vez de por Marisol con una planilla."

**Ejemplo AAA adicional** (por si se quiere un segundo caso, corto, además de `PlayerHealth`):
```
ARRANGE: Inventory con capacidad 1, vacío
ACT:     AddItem("Potion"), después AddItem("Sword")
ASSERT:  la segunda llamada devuelve false (no entra, ya no hay espacio)
```

---

## Bloque 3 (25–40 min) — Unit testing vs. game testing

**Pregunta:** el caso TC-A01 de Unidad 2 (ataque cuerpo a cuerpo conecta con el enemigo) — ¿lo probarían con unit test, integration test, o requiere a una persona jugando?

- "Si solo se verifica que el hitbox y el daño se calculan bien con las posiciones dadas → integration test en Play Mode, similar a `CombatSystemTests`."
- "Si además hay que evaluar si la animación de impacto 'se ve bien' o si el timing del golpe se siente justo → eso necesita QA manual / playtest, no un `Assert`."
- **Respuesta a corregir si aparece:** "Se prueba jugando, nada más" → parcialmente cierto (la sensación sí), pero si el hit conecta y aplica el daño correcto SÍ es automatizable.

### Ejercicio rápido en vivo (Slide 11) — los 4 casos y su clasificación

La slide pide "clasificar 4 casos sueltos del backlog de Cryptbound" sin especificar cuáles — se reutilizan 4 tickets ya conocidos de Unidad 2 (mismo backlog, nueva mirada: no severidad/prioridad, sino *tipo de testing*):

| Ticket | Descripción | Clasificación esperada | Por qué |
|---|---|---|---|
| CRYPT-103 | Crashea al abrir inventario con el arma cargada | Integration test (Play Mode) | Involucra la interacción entre "carga de arma" y "apertura de inventario" — dos sistemas a la vez, no una unidad aislada. |
| CRYPT-105 | El arquero dispara a través de paredes | Unit/Integration test (Play Mode) | Lógica de detección/línea de visión, determinista y aislable — mismo perfil que `EnemyArcherTests`. |
| CRYPT-108 | El jefe no reproduce su animación de derrota | Functional test (parcial) / QA manual | Se puede automatizar "¿se llamó al método que dispara la animación?", pero verificar que "se ve bien" requiere ojo humano. |
| CRYPT-111 | Caída de FPS en la sala del jefe | QA manual / testing de rendimiento | No es unit test — ya se desarrolla el porqué en el Bloque 4. |

---

## Bloque 4 (40–55 min) — Testing en videojuegos: candidatos y límites

**Pregunta:** ¿por qué CRYPT-111 (caída de FPS en la sala del jefe) no se resuelve con un unit test?

- "Porque medir FPS depende de la escena real corriendo, con todos los assets cargados, iluminación y física simultánea — no es un comportamiento aislado que quepa en un Arrange/Act/Assert."
- "Un unit test corre en milisegundos con un `GameObject` vacío o una clase C# pura; no reproduce la carga real de la sala del jefe."
- "Se necesita testing de rendimiento (profiler) y/o QA manual jugando esa sala específica."

**Más ejemplos de "buenos candidatos" (Slide 12), por si piden otro además de Inventory/PlayerExperience:**
- Cooldown de habilidades especiales (¿ya pasó el tiempo mínimo entre usos?).
- Cálculo de resistencias elementales (daño de fuego reducido si el enemigo es "resistente a fuego").
- Tabla de probabilidad de drop de un cofre (determinista si se fija la semilla del random en el test).

**Más ejemplos de "casos complejos" (Slide 13), además de la animación del jefe:**
- Latencia y sincronización en multijugador online.
- Mezcla dinámica de audio (música que sube de intensidad según el combate).
- Sistemas de partículas (¿la explosión "se ve" suficientemente impactante?).

---

## Bloque 5 (55–70 min) — Unity Test Framework

**Pregunta:** ¿por qué el código de test vive en una carpeta separada (`Tests`) con su propio ensamblado, en vez de mezclarse con `Assets/Scripts`?

- "Para que el código de test no se compile dentro del build final del juego — el jugador no necesita los tests instalados."
- "Porque el asmdef de `Tests` ya trae las referencias a NUnit/TestRunner; si estuviera todo junto, cada script del juego arrastraría esas dependencias sin necesitarlas."
- "Separar deja más claro qué es 'código de producción' (`GameAssembly`) y qué es 'código para verificar ese código' (`Tests`)."

---

## Bloque 6 (70–85 min) — Edit Mode vs. Play Mode

**Pregunta:** `Inventory.AddItem` no toca ninguna escena ni `GameObject` — ¿Edit Mode o Play Mode? ¿Y un test que verifica que el HUD se actualiza cuando cambia el inventario?

- "`Inventory.AddItem` → Edit Mode, porque es una clase C# pura sin dependencia de la escena."
- "El test del HUD → Play Mode, porque el HUD es un `GameObject`/`Canvas` real que necesita estar instanciado en una escena para verificar que se actualiza."
- **Matiz para agregar:** verificar que el HUD "se ve bien" sigue sin ser un unit test — como mucho se automatiza que el número interno cambió, no que se lee bien en pantalla.

**Más ejemplos de clasificación Edit/Play Mode, por si hace falta reforzar el criterio:**
- `ScoreManager.AddPoints(int amount)` (clase C# pura) → **Edit Mode**.
- Instanciar un efecto de partículas cuando un enemigo muere (`Instantiate(deathEffect, ...)` dentro de un `MonoBehaviour`) → **Play Mode**, porque depende de la escena y del ciclo de vida de GameObjects.

---

## Bloque 7 (85–100 min) — Primer test en vivo (demo PASS/FAIL)

**Pregunta:** ¿qué hubiera pasado si este bug (vida negativa) llegaba al playtest de Unidad 2 en vez de detectarse acá?

- "Probablemente alguien reportaría algo raro tipo 'el jugador quedó con vida negativa y el juego no lo mató' — confuso de diagnosticar sin saber que viene de un `TakeDamage` sin clamp."
- "Se generaría un ticket nuevo en Jira, alguien tendría que reproducirlo y aislar la causa — todo eso en minutos con el test, en vez de en una sesión de QA completa."

---

## Bloque 8 (100–110 min) — TDD: Red-Green-Refactor

**Pregunta:** ¿por qué escribir el test antes obliga a pensar primero en el comportamiento esperado en vez de en la implementación?

- "Porque para escribir `Assert.AreEqual(30, xp.CurrentExperience)` primero tengo que decidir cómo se va a llamar la propiedad y qué valor debería tener — estoy diseñando la interfaz pública antes de pensar cómo programarla por dentro."
- "Si empezara por el código, es más fácil terminar con una clase que 'anda' pero que nadie verificó que hace lo que el feature pedía."

**Ejemplo adicional para "buenas prácticas" (Slide 31) — contraste de nombres de test:**
- ❌ Mal: `Test1()` que verifica daño, curación y muerte los tres a la vez — si falla, no queda claro cuál de los tres se rompió.
- ✅ Bien: `TakeDamage_ReducesHealthByAmount()`, `Heal_DoesNotExceedMaxHealth()`, `TakeDamage_SetsIsDead_WhenHealthReachesZero()` — cada uno prueba una sola cosa, el nombre ya dice qué se rompió si falla.

**Ejemplo adicional para "cuándo sí / cuándo no usar TDD" (Slide 34):**
- **Buen candidato adicional:** validar una tabla de probabilidad de drop de loot con semilla fija — determinista, reglas claras.
- **Menos conveniente, adicional:** ajustar interactivamente los colores/curvas de un shader de agua — se decide "a ojo", no hay un `Assert` que capture "se ve bien".

---

## Bloque 9 (110–115 min) — Conexión con Unidad 2 + errores conceptuales

**Pregunta:** ¿todos los bugs de Unidad 2 se podrían haber protegido con un test así? ¿Cuáles no, y por qué?

- "CRYPT-105 (arquero dispara a través de paredes) **sí** — es lógica de detección, similar a `EnemyArcherTests`."
- "CRYPT-102 (contador de pociones no se actualiza visualmente) **no del todo** — la lógica del inventario sí, pero 'se actualiza visualmente' es más un integration/UI test."
- "CRYPT-110 (typo en el tutorial) y CRYPT-106 (texto cortado en 4:3) **no** — son contenido/UI, no comportamiento de código."
- "CRYPT-111 (FPS) **no** — ya se vio en el Bloque 4, es rendimiento."

**Ejemplo adicional para "manual vs. automatizado" (Slide 35):**
- **Se presta bien a manual/playtest:** el balance de daño de un arma nueva — ¿se siente justa o rota? Solo lo responde gente jugando.
- **Se presta bien a automatizado:** que el cálculo de crítico nunca aplique más del 200% del daño base, sin importar cuántas veces se ejecute.

---

## Bloque 10 (115–120 min) — Cierre y lanzamiento del TP N° 2

**Pregunta:** ¿qué sistema de un juego que estén programando ustedes mismos se beneficiaría hoy de un test como los que vimos?

- "Un sistema de puntaje o combos, porque tiene reglas claras (+10 por enemigo, x2 si es combo)."
- "Un inventario o crafteo, porque hay condiciones de cantidad/capacidad fáciles de romper sin darse cuenta."
- "Cualquier cálculo de stats (daño, defensa, resistencias) que dependa de fórmulas — determinista, igual que `PlayerHealth` o `PlayerExperience`."
