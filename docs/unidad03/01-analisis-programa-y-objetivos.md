# Unidad 3 — Análisis del programa y objetivos pedagógicos

**Materia:** Diseño según Plataformas de Juego · **Docente:** Ing. Elsa Daniela Ramírez · **Ciclo lectivo:** 2026

---

## Sección A — Análisis del programa de la asignatura

### Cita textual del programa analítico (Anexo, "Diseño según plataformas de juego", Plan 2020)

> **UNIDAD N° 3: Pruebas Unitarias con Unity**
>
> Introducción a las pruebas unitarias: ¿Por qué realizar pruebas unitarias? Rol de las pruebas en la calidad del software.
>
> Beneficios de las pruebas en Unity: Reducción de errores en mecánicas y físicas. Aseguramiento de la estabilidad en proyectos de videojuegos.
>
> Pruebas unitarias en Unity con Unity Test Runner: Creación y ejecución de pruebas unitarias. Tipos de tests soportados: Edit Mode y Play Mode. Buenas prácticas de uso.
>
> Test-Driven Development (TDD): Conceptos básicos. Ciclo Red – Green – Refactor aplicado en Unity. Ejemplos de implementación en componentes de juegos.
>
> Pruebas manuales vs. automatizadas: Definiciones y diferencias. Ventajas y limitaciones en entornos de videojuegos. Casos de uso combinados.

Verificado contra el PDF fuente (`Unidad 1/Diseño segun plataformas de juego Plan 2020 - Año 2024 - - Elsa Daniela Ramirez .pdf`, Anexo del Programa Analítico) — coincide palabra por palabra con el encargo recibido.

### Dónde encaja esta unidad en el cronograma real de la cátedra

El cronograma semanal del programa (Punto 3.1) ubica el contenido de Unidad III a caballo entre la **Semana 5** (cierre de Unidad II: ciclo de vida y casos de prueba) y la **Semana 6** (Unidad III completa), con una actividad de aula virtual llamada *"Defensa del diseño de mecánicas de juegos"* en el mismo tramo — no forma parte del contenido evaluable de esta unidad, es una instancia paralela sobre diseño de mecánicas, no sobre testing.

Dato importante para el docente: el programa indica explícitamente **`Trabajo Práctico N° 2 — "Toda la Unidad 03"`**. A diferencia de Unidad II (que alimentaba el TP N°1 junto con Unidad I), **la Unidad III tiene su propio trabajo práctico dedicado**. Además, el **Parcial de la Semana 9** evalúa el contenido acumulado de las Unidades 1 a 4, por lo que Unity Test Runner y TDD son materia de examen, no solo de práctica en clase.

### Material docente previo detectado

Existe en el repositorio `docs/Unidad 3 -2024.pptx` — una presentación de 36 diapositivas del ciclo 2024, construida sobre el tutorial oficial de Unity Learn *"Unit Testing"* (proyecto de ejemplo **Crashteroids**, un clon de Asteroids). Cubre: instalación del paquete Unity Test Framework, creación de la carpeta `Tests` y de los *Assembly Definition* (`Tests.asmdef` / `GameAssembly.asmdef`), y la escritura de 5 tests (`AsteroidsMoveDown`, `GameOverOccursOnAsteroidCollision`, `LaserDestroysAsteroid`, `LaserMovesUp`, `NewGameRestartsGame`), más una introducción al paquete Code Coverage. Cita como fuente la documentación oficial `docs.unity3d.com/Packages/com.unity.test-framework@1.1/manual/index.html` (versión de paquete desactualizada respecto a 2026 — ver [`06-investigacion-recursos.md`](./06-investigacion-recursos.md) para la versión vigente).

**Decisión adoptada — modelo de continuidad, igual que Unidad 1 con sus PDFs reciclados:** los pasos técnicos de configuración de ese material (instalar el paquete, crear la carpeta de tests, crear y vincular los *assembly definitions*, la pestaña PlayMode/EditMode del Test Runner) son correctos y se **reciclan** — Unity no cambió ese flujo de forma sustancial entre 2024 y 2026. Lo que cambia es el **ejemplo concreto**: en lugar de Crashteroids (un proyecto ajeno al hilo conductor de la cátedra), todos los tests de esta unidad se escriben sobre **Cryptbound**, el mismo dungeon-crawler usado en Unidad 2, para no romper la continuidad narrativa que el estudiante ya construyó. Las diapositivas marcadas **[RECICLADO 2024]** en [`04-diapositivas.md`](./04-diapositivas.md) señalan qué pasos provienen de ese material.

### Qué es realmente esta unidad (y qué no)

Es la primera vez en la materia que el testing deja de ser un proceso humano (jugar, reportar, clasificar — Unidades 1 y 2) para convertirse parcialmente en **código que se ejecuta solo**. No es una clase de "botones de Unity": el programa pide explícitamente entender *por qué* automatizar, no solo *cómo* clickear Test Runner. Tampoco es una clase de TDD dogmático ni de arquitectura de software — TDD se presenta como una herramienta más, con límites claros (Sección 20 de este documento y del guion docente).

### 1. Conocimientos previos esperados (Unidades I y II)

- Error, defecto, fallo, causa raíz (Unidad I) — un test unitario automatiza la detección de un *fallo*, no elimina los *errores* humanos que lo originan.
- Tipos de testing (funcional/no funcional, manual/automatizado) y niveles (unitario, integración, sistema, aceptación) — la Unidad III profundiza específicamente el nivel **unitario** y la modalidad **automatizada**, ya nombrados pero no ejecutados en Unidad I.
- Test case y test suite, con su estructura de campos (Unidad II) — un test automatizado en C# es, conceptualmente, el mismo test case de Unidad II, pero expresado como código en vez de como fila de tabla.
- Regression testing, retesting, smoke testing y el ciclo bug → ticket → fix → retest (Unidad II) — esta unidad responde a la pregunta que Unidad II deja abierta: *¿puede una máquina hacer parte de ese retesting/regression automáticamente?*
- Partición de equivalencia y valores frontera (Unidad I), ya aplicados al backlog de Cryptbound en Unidad 2 (ej. TC-E01, rango de detección del arquero) — se reutilizan como criterio para diseñar *qué* casos merecen un test unitario.

### 2. Conocimientos que deben quedar adquiridos al cierre

- Explicar por qué un equipo de videojuegos necesita pruebas automatizadas además de QA manual y playtesting.
- Diferenciar Edit Mode y Play Mode, y decidir correctamente cuál usar según el tipo de código a probar.
- Crear, ejecutar e interpretar un test en Unity Test Framework usando el patrón Arrange-Act-Assert.
- Explicar el ciclo Red-Green-Refactor y ejecutarlo sobre un componente simple de gameplay.
- Distinguir qué defectos son buenos candidatos para unit testing y cuáles requieren QA manual o playtesting.
- Conectar un bug real (ticket de Unidad II) con un test de regresión que lo protege a futuro.

### 3. Relación con la industria (por qué importa más allá de la nota)

En un equipo real de videojuegos, el testing automatizado no reemplaza al playtesting ni al QA manual — reduce el tiempo que ambos dedican a re-verificar lo que ya funcionaba. Esta unidad enseña a decidir *dónde* conviene esa automatización (lógica de reglas, cálculos, estados) y dónde no (sensación de control, iluminación, balance), evitando tanto el extremo de "no testear nada" como el de "intentar automatizar la diversión".

### 4. Qué queda deliberadamente fuera

- **CI/CD e integración continua** (Sección 43 del encargo): se menciona en una sola diapositiva como *hacia dónde puede escalar* esto, sin desarrollarla — no está en el programa de esta unidad y pertenece a un contenido de infraestructura de proyecto, no de testing en sí.
- **Mocking frameworks avanzados** (NSubstitute, Moq) y **dependency injection**: útiles en proyectos grandes, pero agregarían una capa de abstracción que el programa no pide y que oscurecería el objetivo central (entender qué es y para qué sirve un test unitario).
- **Unity Test Framework para paquetes/assets de terceros** y **testing de rendimiento con el Performance Testing Package**: exceden el alcance de "pruebas unitarias" y pertenecen más a testing de sistema/rendimiento.
- **Cobertura de código (Code Coverage)** como métrica formal: el material 2024 la menciona: se conserva como mención breve de cierre ("existe, para quien quiera profundizar") pero no se evalúa — el programa no la pide y "más cobertura = mejor calidad" es, de hecho, uno de los errores conceptuales que esta unidad corrige (Sección 41).
- **Roles Scrum, backlog de producción, sprints**: igual que en Unidad 2, no corresponde a esta unidad. Si aparece la palabra "Jira" es únicamente como puente con Unidad II (Sección 24 del encargo), no como contenido nuevo.
- **Detalle de versión exacta de la interfaz de Unity**: se documenta la versión de referencia usada (ver [`06-investigacion-recursos.md`](./06-investigacion-recursos.md)) pero se prioriza el concepto — la ventana Test Runner cambia de aspecto entre versiones de Unity con más frecuencia que su lógica interna.

---

## Sección B — Interpretación pedagógica

El programa pide, en ese orden: (1) el *por qué* de las pruebas unitarias, (2) sus beneficios específicos en Unity, (3) la herramienta (Unity Test Runner) con sus dos modos, (4) TDD, (5) el contraste manual/automatizado. Ese orden **no es arbitrario** y se respeta en el guion docente: nombrar la herramienta antes de justificar la necesidad produce el efecto que el encargo pedagógico busca evitar explícitamente — una clase que empieza en "hoy vamos a aprender a usar el Test Runner" en lugar de partir de un problema real de ingeniería.

La secuencia pedagógica adoptada es:

```
Cryptbound sigue creciendo (build 0.3 → 0.4)
        ↓
Cada sprint se tocan más sistemas (Player, Combat, Inventory, Enemy)
        ↓
Un cambio en Combat rompe algo en Player que ya funcionaba
        ↓
Nadie lo nota hasta el siguiente playtest — 3 días después
        ↓
REGRESIÓN
        ↓
¿Cómo lo detectamos en segundos, no en el próximo playtest?
        ↓
PRUEBAS AUTOMATIZADAS → PRUEBAS UNITARIAS
        ↓
UNITY TEST FRAMEWORK (Test Runner)
        ↓
EDIT MODE / PLAY MODE
        ↓
TDD: escribir el test antes de que el bug exista
```

---

## Sección C — Objetivos generales

Que el estudiante comprenda que las pruebas unitarias son una respuesta de ingeniería a un problema concreto del desarrollo iterativo de videojuegos —la aparición de regresiones—, sepa ejecutarlas con Unity Test Framework en sus dos modalidades, y entienda su lugar dentro de una estrategia de calidad más amplia que no reemplaza el QA manual ni el playtesting.

## Sección D — Objetivos específicos

Al finalizar la clase, el estudiante debería poder:

1. Explicar por qué se utilizan pruebas unitarias en el desarrollo de videojuegos, con al menos un ejemplo propio de regresión.
2. Diferenciar una prueba unitaria de un test de integración, un test funcional, un playtest y QA manual.
3. Explicar Edit Mode y Play Mode, y elegir correctamente cuál usar dado un fragmento de código.
4. Crear una prueba básica en Unity Test Framework siguiendo el patrón Arrange-Act-Assert.
5. Utilizar assertions de NUnit para verificar un resultado esperado.
6. Explicar el ciclo Red-Green-Refactor y en qué se diferencia de "escribir tests después de programar".
7. Aplicar Red-Green-Refactor sobre un componente simple (sistema de experiencia del jugador).
8. Identificar qué problemas de un videojuego son buenos candidatos para unit testing y cuáles no.
9. Explicar por qué las pruebas automatizadas no sustituyen las pruebas manuales ni el playtesting.
10. Conectar un bug corregido con un test de regresión que impide que vuelva a aparecer.

## Sección E — Conceptos que quedan fuera

(Ver el detalle y la justificación completa en la Sección A.4 de este documento — CI/CD, mocking/DI avanzado, Code Coverage como métrica evaluable, Scrum/producción, y detalle exhaustivo de UI de una versión puntual de Unity.)

---

## Sección F — Relación con otras unidades

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

**Resultados de aprendizaje y competencias vinculadas (inferidas del programa, con el mismo criterio de razonamiento explícito que Unidad 2 aplicó — el programa no desagrega RA/CE por unidad más allá de la tabla genérica de la Sección 1.5):** RA01, RA03. CE02 (implementar y documentar algoritmos de mecánicas de juego — los tests verifican exactamente esos algoritmos), CE05 (diseñar y ejecutar casos de prueba — aquí se ejecutan como código), CE06 (identificar y documentar defectos — vía tests de regresión), CE07 (documentación técnica de testing — un test bien nombrado es documentación ejecutable), CE12 (coordinar diseño, implementación y testing — TDD integra las tres actividades en un mismo ciclo).

**Nota sobre datos del programa:** al igual que en Unidad 2, no existe una tabla oficial que desagregue RA/CE por unidad temática con más detalle que la tabla genérica de la Sección 1.5 del programa analítico — esta asignación es una interpretación razonada del docente/preparador, no una cita literal.
