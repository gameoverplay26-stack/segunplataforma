# Unidad 2 — Análisis del programa y objetivos pedagógicos

**Materia:** Diseño según Plataformas de Juego · **Docente:** Ing. Elsa Daniela Ramírez · **Ciclo lectivo:** 2026

---

## Sección A — Análisis del programa de la asignatura

### Qué es realmente la materia

"Diseño según Plataformas de Juego" (Tecnicatura Universitaria en Diseño Integral de Videojuegos, Plan 2020, RESOL-2020-1099-APN-ME, Facultad de Ingeniería – UNJu, 3er año, 60 hs totales) combina dos ejes que no deben confundirse:

1. **Testing y QA de videojuegos.**
2. **Diseño según plataforma** (móvil, consola, PC, VR/AR/emergentes).

No es una materia de gestión de proyectos ni de producción ágil.

### Qué dice literalmente la Unidad II

Programa analítico, Unidad II — "Gestión del testing": clasificación de bugs por categoría/severidad/dificultad; tipos de tickets (issues); herramientas de gestión JIRA, TestRail, QAComplete, Confluence; regression testing vs. retesting; smoke testing; riesgo en testing; relación con el Manifiesto Ágil; fundamentos y estructura de un plan de pruebas; ciclo de vida del desarrollo de videojuegos e integración de pruebas por fase; diseño de casos de prueba (identificador, descripción, condiciones previas, pasos, datos de entrada, resultado esperado vs. real, estado, comentarios); ejemplos por género (acción, RPG, estrategia).

### 1. Conocimientos previos esperados (Unidad I)

- Qué es testing y qué es QA, y la diferencia entre error, defecto, fallo y causa raíz (caso del lápiz).
- Tipos de testing (funcional/no funcional, manual/automatizado) y niveles (unitario, integración, sistema, aceptación).
- Técnicas clásicas: partición de equivalencia, análisis de valores frontera, exploratory testing, testing negativo.
- Técnicas basadas en modelos: testing de estados y transiciones, pairwise testing.
- Conceptos de falso positivo / falso negativo.

Sin este piso conceptual, hablar de "severidad de un bug" o "caso de prueba" carece de fundamento — la clase reutiliza explícitamente estos términos (ver casos de prueba en [`02-caso-cryptbound.md`](./02-caso-cryptbound.md), que citan partición de equivalencia y valores frontera aplicados a IA de enemigos).

### 2. Conocimientos que deben quedar adquiridos al cierre

- Clasificar un bug por categoría, severidad y prioridad, entendiendo que son ejes independientes.
- Redactar un ticket accionable (no una queja) con pasos de reproducción y resultado esperado/real.
- Distinguir smoke testing, retesting y regression testing, y saber cuándo usar cada uno.
- Reconocer los componentes mínimos de un plan de pruebas y de un caso de prueba.
- Explicar qué resuelve una herramienta como Jira frente a alternativas (TestRail, QAComplete, Confluence) y por qué "herramienta" no es sinónimo de "proceso".
- Ubicar el testing dentro del ciclo de vida de producción de un videojuego (no es una fase final aislada).

### 3. Conceptos de gestión relevantes para la carrera

No "gestión de proyectos" en abstracto, sino gestión **de la calidad** del producto: triage de bugs, priorización bajo escasez de tiempo del equipo, trazabilidad (issue → fix → retest → cierre), y comunicación entre QA y desarrollo mediada por un sistema, no por mensajes sueltos.

### 4. Qué parte de Jira corresponde realmente a esta unidad

Issue/ticket de tipo *Bug*, sus campos (severidad, prioridad, pasos de reproducción), el *workflow* de estados, el *board* como visualización del flujo de bugs, y filtros/paneles para reportar tendencias de bugs abiertos vs. cerrados.

**No** corresponde: Product Backlog de features, Sprint Planning, Story Points ni Velocity — eso pertenece a la gestión de producción, ausente del programa de esta unidad (ver [`06-anexo-scrum-agile.md`](./06-anexo-scrum-agile.md)).

### 5. Qué queda deliberadamente fuera

- Roles Scrum (Product Owner / Scrum Master) — no están en el programa.
- Estimación con Story Points / Planning Poker — no está en el programa (la "dificultad" de un bug no equivale a estimación de esfuerzo de features).
- Burndown y Velocity de sprint — pertenecen a gestión de producción.
- Detalle de interfaz específico de una versión de Jira (la UI cambia; se prioriza el concepto sobre la pantalla).

---

## Sección B — Objetivos pedagógicos de la Unidad II

Al finalizar esta clase, el estudiante podrá pasar de *"encontré un montón de bugs jugando"* a *"tengo un backlog de bugs clasificado, un plan de pruebas con criterios de aceptación, casos de prueba diseñados y un flujo de trabajo trazable en una herramienta"*.

**Objetivo general:** comprender por qué un equipo de desarrollo de videojuegos necesita gestionar de forma sistemática los defectos que encuentra, y cómo herramientas como Jira materializan esa gestión — sin confundir la herramienta con el proceso de calidad que la antecede.

**Objetivos específicos:**

1. Clasificar bugs por categoría, severidad, prioridad y dificultad de resolución.
2. Redactar tickets reproducibles y priorizables.
3. Diferenciar regression testing, retesting y smoke testing en un contexto de videojuego.
4. Diseñar un plan de pruebas mínimo viable y casos de prueba por género.
5. Comparar Jira, TestRail, QAComplete y Confluence según el problema que cada uno resuelve mejor.

---

## Sección C — Conceptos teóricos

### Severidad vs. prioridad — el eje que organiza todo lo demás

La **severidad** mide el impacto técnico del defecto sobre el sistema; la fija quien testea y no debería cambiar con el tiempo. La **prioridad** mide la urgencia de negocio para resolverlo; la fija quien lidera QA/producción y puede cambiar según contexto, fecha de entrega o riesgo reputacional. Son ejes **independientes**: existen las cuatro combinaciones (alta/alta, alta/baja, baja/alta, baja/baja).

| Severidad | Prioridad | Ejemplo en un videojuego |
|---|---|---|
| Alta | Alta | El juego crashea al abrir el inventario (rompe todo, hay que arreglarlo ya). |
| Baja | Alta | Un logo de sponsor con el color equivocado en pantalla de carga (impacto técnico mínimo, pero contractualmente urgente). |
| Alta | Baja | Un enemigo secundario que casi nunca aparece atraviesa una pared (grave si ocurre, pero casi nadie lo ve). |
| Baja | Baja | Typo en un tooltip que casi nadie lee. |

### Categoría y dificultad

La **categoría** ubica el bug por sistema afectado (gameplay, UI, audio, guardado, rendimiento, contenido/texto). La **dificultad de resolución** es una estimación aparte: cuánto esfuerzo probable insumirá el fix — un bug de severidad baja puede ser difícil de resolver (una condición de carrera esporádica), y uno de severidad alta puede ser trivial (una única línea con un signo invertido).

### Ticket / Issue

Un ticket es la unidad mínima de trabajo trazable: no es "una queja", es un registro con información suficiente para que otra persona, sin haber jugado la partida, pueda reproducir el problema, entender su impacto y saber cuándo darlo por resuelto.

### Regression testing, retesting y smoke testing

| Técnica | Pregunta que responde | Alcance |
|---|---|---|
| **Retesting** | ¿Se solucionó *este* bug puntual? | Solo los pasos que originalmente reproducían el defecto. |
| **Regression testing** | ¿El fix rompió algo que antes funcionaba? | El área funcional relacionada (no todo el juego, sí lo que puede haberse visto afectado). |
| **Smoke testing** | ¿Este build siquiera arranca y sostiene lo esencial? | Un recorrido mínimo y rápido antes de invertir horas de testing profundo. |

### Riesgo en testing

Todo plan de pruebas trabaja bajo tiempo limitado: el riesgo es la probabilidad de que un defecto no detectado llegue a producción, ponderada por su impacto. Priorizar pruebas es, en el fondo, decidir dónde conviene gastar las horas de testing que el equipo realmente tiene.

### Relación con el Manifiesto Ágil (mención breve, tal como la pide el programa)

El Manifiesto Ágil valora *software funcionando* por sobre documentación exhaustiva y *responder al cambio* por sobre seguir un plan rígido. Aplicado al testing, esto se traduce en una idea puntual: **el testing no es una fase final aislada, sino una actividad continua a lo largo de todo el desarrollo** — se prueba build tras build, no solo "al final". Esta clase no desarrolla Scrum como marco de producción; toma del Manifiesto únicamente esa idea de continuidad.

---

## Sección D — Agile aplicado a videojuegos (nota breve, no un marco completo)

El desarrollo de un videojuego cambia constantemente: una mecánica que se ve bien en el diseño puede no "sentirse bien" jugada; un playtest revela que un jefe es injustamente difícil; un asset cambia de estilo a mitad de producción. Por eso el desarrollo de juegos rara vez sigue un plan cerrado de principio a fin — y por eso el testing tampoco puede ser "una etapa al final": cada build nuevo necesita, otra vez, verificación.

Esta idea es todo lo que el programa pide de Agile para esta unidad. El desarrollo completo de Scrum (roles, backlog de producto, sprints) se reserva para el módulo de extensión ([`06-anexo-scrum-agile.md`](./06-anexo-scrum-agile.md)).

---

## Sección E — Por qué esta clase no enseña Scrum completo

El encargo original imaginaba una clase de producción ágil completa (Product Backlog de features, roles PO/SM/Developers, Sprint Planning, Story Points, Velocity). Es un contenido real y valioso — pero pertenece a la gestión de **producción** de un videojuego, no a la gestión de **testing** que define esta Unidad II. Enseñarlo aquí, a fondo, sería exceder el programa oficial y desplazar tiempo de clase de lo que sí se evalúa.

Ese contenido no se descarta: se preserva íntegro en [`06-anexo-scrum-agile.md`](./06-anexo-scrum-agile.md) como módulo de extensión, para que el docente lo use si la cátedra decide ampliar la materia o si otra asignatura de la carrera (producción de videojuegos, si existiera) lo retoma.
