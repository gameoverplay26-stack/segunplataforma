# Unidad 3 — Pruebas Unitarias con Unity

**Materia:** Diseño según Plataformas de Juego
**Carrera:** Tecnicatura Universitaria en Diseño Integral de Videojuegos (Plan 2020)
**Docente:** Ing. Elsa Daniela Ramírez
**Ciclo lectivo:** 2026
**Unidad:** 3 — Pruebas Unitarias con Unity
**Resultados de aprendizaje vinculados:** RA01, RA03 (inferidos, ver justificación en [`01-analisis-programa-y-objetivos.md`](./01-analisis-programa-y-objetivos.md)).
**Competencias específicas vinculadas:** CE02, CE05, CE06, CE07, CE12 (inferidas — ver la misma sección).

Caso guía usado en toda la unidad: **Cryptbound**, el mismo dungeon-crawler de Unidad 2, ahora en su build 0.4. No se cambia de proyecto — se aprovecha que los sistemas de Cryptbound (vida, inventario, combate, enemigos) ya tienen lógica de reglas clara desde Unidad 2, ideal para pruebas unitarias.

---

## Objetivo de la unidad

Que el estudiante entienda las pruebas unitarias como una respuesta de ingeniería a un problema concreto y recurrente del desarrollo iterativo de videojuegos —la aparición de regresiones cuando un cambio en un sistema rompe silenciosamente otro que ya funcionaba—, sepa ejecutarlas en Unity Test Framework (Edit Mode y Play Mode), aplique el ciclo Red-Green-Refactor de TDD sobre un componente simple, y comprenda con precisión qué parte del testing de un videojuego puede automatizarse y cuál requiere, siempre, QA manual y playtesting.

## Contenidos (según programa analítico)

1. Introducción a las pruebas unitarias: por qué realizarlas, rol en la calidad del software.
2. Beneficios de las pruebas en Unity: reducción de errores en mecánicas y físicas, estabilidad del proyecto.
3. Unity Test Runner (Unity Test Framework): creación y ejecución de pruebas, Edit Mode y Play Mode, buenas prácticas.
4. Test-Driven Development (TDD): conceptos básicos, ciclo Red-Green-Refactor aplicado en Unity.
5. Pruebas manuales vs. automatizadas: diferencias, ventajas, limitaciones, casos de uso combinados.

Cita textual completa del programa en [`01-analisis-programa-y-objetivos.md`](./01-analisis-programa-y-objetivos.md), Sección A.

---

## Relación con otras unidades

```
Unidad I   — Fundamentos y técnicas de testing
              (error/defecto/fallo, niveles de testing, partición de equivalencia, valores frontera)
    ↓ aporta el vocabulario y el nivel "unitario" que aquí se ejecuta como código
Unidad II  — Gestión del testing
              (tickets, severidad/prioridad, regression/retest/smoke, casos de prueba, Jira)
    ↓ los casos de prueba diseñados ahí se automatizan (parcialmente) aquí
Unidad III — Pruebas unitarias con Unity  ← esta unidad
    ↓ el criterio "qué merece automatizarse" se reutiliza al testear en cada plataforma
Unidades IV–VII — Diseño según plataforma (móvil, consola, PC, emergentes)
              cada una retoma testing y portabilidad multiplataforma con sus propias herramientas
```

- **Con Unidad I:** reutiliza directamente error/defecto/fallo, niveles de testing y, de forma muy concreta, partición de equivalencia y valores frontera (el test de `EnemyArcher` sobre el rango de detección del arquero es el mismo caso TC-E01 de Unidad 2, ahora escrito como código).
- **Con Unidad II:** el ciclo `bug → ticket → fix → retest/regression` se retoma explícitamente — un test unitario es, en esta unidad, la forma automatizada de proteger ese retest a futuro. Se usa el mismo backlog de Cryptbound, extendido con tickets nuevos de la build 0.4 (CRYPT-201 a 203).
- **Con Unidad IV (inferida, Diseño según Plataforma Móvil):** esa unidad incluye "Testing y Portabilidad Multiplataforma", lo cual sugiere que el criterio de qué automatizar (aquí aprendido) se retomará con herramientas específicas de testing móvil — sin que el programa detalle aún esa conexión de forma explícita.

**Dato relevante del cronograma real de la cátedra:** a diferencia de Unidad 2 (que compartía el TP N°1 con Unidad 1), la Unidad III tiene su **propio Trabajo Práctico (TP N° 2)**, dedicado por completo a esta unidad según el programa analítico. Además, el Parcial de la Semana 9 evalúa el contenido acumulado de las Unidades 1 a 4.

---

## Estructura documental

| Archivo | Contenido |
|---|---|
| [`01-analisis-programa-y-objetivos.md`](./01-analisis-programa-y-objetivos.md) | Cita textual del programa, análisis del cronograma real, material previo detectado (`docs/Unidad 3 -2024.pptx`), objetivos generales/específicos, qué queda fuera, relación RA/CE |
| [`02-caso-practico-testing-videojuego.md`](./02-caso-practico-testing-videojuego.md) | Cryptbound build 0.4: arquitectura testeable, código y tests de `PlayerHealth`/`Inventory`/`CombatSystem`/`EnemyArcher`, el bug de regresión CRYPT-201, TDD completo sobre `PlayerExperience`, backlog de bugs nuevo, límites del caso |
| [`03-clase-guion-docente.md`](./03-clase-guion-docente.md) | Guion de la clase de 120 minutos, bloque por bloque (objetivo/contenido/qué decir/ejemplo/pregunta/demostración/error a evitar/duración) |
| [`04-diapositivas.md`](./04-diapositivas.md) | Presentación de 36 diapositivas, con las heredadas de `docs/Unidad 3 -2024.pptx` marcadas [RECICLADO 2024] |
| [`05-actividad-practica-y-evaluacion.md`](./05-actividad-practica-y-evaluacion.md) | Dos actividades en equipo (suite de tests + ciclo TDD completo), consignas del TP N° 2, evaluación conceptual/práctica/de análisis con rúbrica, y los 10 errores conceptuales frecuentes con su corrección |
| [`06-investigacion-recursos.md`](./06-investigacion-recursos.md) | Recursos verificados: documentación oficial de Unity y Microsoft, TDD (Fowler/Beck), videos en español e inglés, material universitario, casos de industria AAA (Rare, Activision, Sony Santa Monica) |
| [`07-ejemplos-y-respuestas-de-apoyo.md`](./07-ejemplos-y-respuestas-de-apoyo.md) | Referencia rápida para el día de la clase: ejemplos de respuesta para cada pregunta al alumno del guion/diapositivas, más el material de apoyo que las slides mencionan sin desarrollar (ej. los 4 casos del ejercicio de clasificación de la Slide 11, con su respuesta) |
| [`Unidad-3-Diapositivas-2026.pptx`](./Unidad-3-Diapositivas-2026.pptx) | Deck de PowerPoint generado a partir de `04-diapositivas.md` (36 diapositivas, tablas reales, bloques de código, notas del docente incluidas). Ver `scripts/` para regenerarlo. |
| [`scripts/generar_diapositivas.py`](./scripts/generar_diapositivas.py) + [`scripts/build_deck.py`](./scripts/build_deck.py) | Generador del `.pptx` con `python-pptx` (paleta de colores, layouts reutilizables, contenido de las 36 slides). Ejecutar `python scripts/build_deck.py` desde `docs/unidad03/` para regenerar el archivo tras editar `04-diapositivas.md`. Requiere `pip install python-pptx`. |

Los seis archivos `01`-`06` son los mínimos pedidos originalmente — esta unidad no presentó, a diferencia de Unidad 2, una contradicción entre el encargo y el programa oficial que justificara un anexo de extensión no evaluable. `07-ejemplos-y-respuestas-de-apoyo.md` y el `.pptx` (con su generador) se agregaron después, a pedido del usuario, como material derivado y complementario — no duplican contenido nuevo, lo hacen utilizable en el momento de dar la clase.

## Escenas jugables de demostración (`Unidad03-TestingUnity/`)

A diferencia del resto del material, Cryptbound nunca se construyó como proyecto jugable (ver "Decisiones pedagógicas importantes" más abajo) — es un caso narrativo. Como complemento, y solo para uso del docente en la demo en vivo (no forman parte de ninguna actividad evaluable de la Sección R/S/T de `05-actividad-practica-y-evaluacion.md`), el proyecto `Unidad03-TestingUnity/` incluye dos escenas jugables mínimas que envuelven visualmente el código ya explicado en clase, sin modificarlo:

| Escena | Qué muestra | Sistemas que envuelve |
|---|---|---|
| `Assets/_Project/Scenes/PlayModeDemo.unity` | Barra de vida interactiva: botones/teclado (Espacio = dañar, H = curar, R = reset) sobre `PlayerHealth`, con color dinámico y estado "MUERTO" | `PlayerHealth` (Sección C del caso práctico) |
| `Assets/_Project/Scenes/CombatDemo.unity` | Un Player que se mueve (WASD/flechas) y ataca (Espacio, con rango y cooldown) a un Enemy con su propia barra de vida | `CombatSystem` + `PlayerHealth` (Sección F, el bug de regresión CRYPT-201) |

`CombatSystem` expone en el Inspector del Player un toggle `Enable Critical Hit Bug` (apagado por defecto): activarlo reproduce en vivo, sobre la barra de vida del Enemy, la regresión real de CRYPT-201 (el "crítico" duplica el golpe en vez de aumentarlo) — mismo bug que ya narra la Sección F, ahora visible sin necesidad de leer el Test Runner.

`CombatDemo.unity` tiene además dos refuerzos puramente visuales (no afectan la lógica de `CombatSystem`, viven en `PlayerController`/`EnemyTarget`): un anillo alrededor del Player del tamaño de `attackRange` (gris = fuera de rango, verde = adentro y listo para atacar, ámbar = adentro pero en cooldown) y un pequeño "disparo" (esfera) que viaja del Player al Enemy en cada golpe conectado, con un flash + punch de escala al impactar. El Enemy tiene 100 HP (`attackDamage` 20 por defecto → mínimo 5 golpes para derrotarlo, menos si hay crítico) y retrocede un paso en sentido contrario al Player cada vez que recibe un disparo — el jugador tiene que perseguirlo para completarlo.

Ambas escenas se generan/reconstruyen con `Tools ▸ Demo ▸ Build PlayerHealth Demo Scene` y `Tools ▸ Demo ▸ Build Combat Demo Scene` (menús agregados por `Assets/_Project/Editor/DemoSceneBuilder.cs` y `CombatDemoSceneBuilder.cs`) — útil si alguna se rompe y hay que rearmarla sin repetir los pasos a mano. Validadas en batch mode (compilación limpia + `EditMode`/`PlayMode` sin regresiones) antes de cada commit.

**Fase 1 (jugable) completa. Ideas para una fase 2, no implementadas:** que el Enemy también ataque al Player (reutilizando el mismo `CombatSystem`, para que el Player tenga su propio riesgo), y/o un `EnemyArcher` con patrulla/alerta/ataque (Sección G del caso práctico) en vez de un Enemy fijo.

---

## Duración estimada

Una clase de **120 minutos** (igual que Unidad 1 y Unidad 2, consistente con "dos clases por semana de 2 horas cada una" del programa), más el desarrollo del TP N° 2 fuera de horario de clase (2-3 semanas, según el programa).

## Recursos principales

Ver el detalle completo y verificado en [`06-investigacion-recursos.md`](./06-investigacion-recursos.md). Los tres pilares recomendados si el tiempo de preparación es limitado:

1. **Oficial de Unity:** [Edit mode and Play mode tests](https://docs.unity3d.com/6000.4/Documentation/Manual/test-framework/edit-mode-vs-play-mode-tests.html) — la fuente técnica central de la unidad.
2. **En español:** ["Testing automatizado de juegos"](https://www.youtube.com/watch?v=0NNUkmd08Rg) (Nerdearla) y la presentación ["GamwUS: TDD y Videojuegos"](https://es.slideshare.net/slideshow/gamwus-desarrollo-diriguido-por-pruebas-y-videojuegos/27015200) (Universidad de Sevilla).
3. **Industria AAA:** ["Automated Testing of Gameplay Features in Sea of Thieves"](https://www.youtube.com/watch?v=X673tOi8pU8) (GDC/Rare) — para mostrar que esto no es un ejercicio académico aislado.

## Material previo de la cátedra

`docs/Unidad 3 -2024.pptx` (36 diapositivas, ciclo 2024) — basado en el tutorial oficial de Unity Learn "Unit Testing" (proyecto Crashteroids). Sus pasos técnicos de configuración se reciclan; su ejemplo concreto se reemplaza por Cryptbound para no romper la continuidad narrativa con Unidad 2. Detalle completo en [`01-analisis-programa-y-objetivos.md`](./01-analisis-programa-y-objetivos.md), Sección A.

## Instrucciones para usar esta documentación

1. Leer primero `01-analisis-programa-y-objetivos.md` para entender el encuadre y qué queda deliberadamente fuera.
2. Repasar `02-caso-practico-testing-videojuego.md` — es la fuente de todo el código y los ejemplos que se usan en clase y en la actividad.
3. Dar la clase siguiendo `03-clase-guion-docente.md`, apoyado en `Unidad-3-Diapositivas-2026.pptx` (o en `04-diapositivas.md`, su fuente de contenido, si se prefiere rearmar el diseño en otra herramienta).
4. Lanzar la actividad y evaluar con `05-actividad-practica-y-evaluacion.md`.
5. Usar `06-investigacion-recursos.md` para asignar lecturas/videos complementarios y para citar fuentes con autoridad verificada frente a la cátedra.
6. Si se edita `04-diapositivas.md` (contenido nuevo, corrección, más ejemplos), regenerar el `.pptx` corriendo `python scripts/build_deck.py` desde `docs/unidad03/` — mantiene la paleta y el diseño consistentes en vez de editar el archivo binario a mano.

## Decisiones pedagógicas importantes

- **La herramienta se presenta al final, no al principio.** La clase abre con una regresión real en Cryptbound (Bloque 1 del guion), no con "hoy vamos a aprender Test Runner" — Unity Test Framework aparece recién en el Bloque 5, como consecuencia de una necesidad ya instalada.
- **Continuidad de proyecto, no de plataforma:** se descartó deliberadamente reemplazar Cryptbound por el proyecto Crashteroids del material 2024, aun siendo técnicamente más simple, para no perder el hilo narrativo (equipo, roles, backlog) que los estudiantes ya construyeron en Unidad 2.
- **Los límites del unit testing se enseñan con la misma fuerza que sus beneficios.** La Sección J del caso práctico y el Bloque 4 del guion existen específicamente para que ningún estudiante salga de la clase pensando que "más tests = mejor juego" — esto está respaldado por la propia documentación oficial de Unity (`unity.com/how-to`), no es solo una precaución pedagógica del docente.
- **TDD se presenta con matices, no como dogma.** Se cita explícitamente que TDD es poco común en desarrollo de videojuegos (fuente oficial de Unity) y se dedica un bloque completo a "cuándo sí, cuándo no", en vez de presentarlo como la única forma correcta de programar.
- **Jira aparece solo como puente (5 minutos), no como contenido nuevo** — sigue perteneciendo a Unidad 2; acá se usa únicamente para cerrar el círculo bug→ticket→fix→test de regresión.
- **Se conserva y adapta el material 2024**, en vez de descartarlo, siguiendo el mismo criterio de continuidad documental que la Unidad 1 aplicó con sus PDFs reciclados.
