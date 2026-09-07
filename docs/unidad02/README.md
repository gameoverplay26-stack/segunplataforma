# Unidad 2 — Gestión del Testing

**Materia:** Diseño según Plataformas de Juego
**Carrera:** Tecnicatura Universitaria en Diseño Integral de Videojuegos (Plan 2020)
**Docente:** Ing. Elsa Daniela Ramírez
**Ciclo lectivo:** 2026
**Unidad:** 2 — Gestión del testing
**Resultados de aprendizaje vinculados:** RA01, RA03.
**Competencias específicas vinculadas:** CE05, CE06, CE07, CE11, CE12.

Caso guía usado en toda la unidad: **Cryptbound**, un dungeon-crawler de acción producido por un equipo estudiantil de 7 personas.

> **Versión visual/interactiva de todo este material:** [Cryptbound QA](https://claude.ai/code/artifact/02367bb4-89fd-4cbc-ad59-829749d6874a) (artifact HTML publicado — mismo contenido que estos archivos, con tablas, badges de severidad/prioridad y navegación por secciones).

---

## ⚠️ Contradicción detectada entre el encargo y el programa oficial

El pedido original de esta unidad describía una clase de **gestión ágil de producción** completa (Scrum: Product Backlog con Epics/Stories, Sprint Planning, Story Points, Velocity, Burndown). Al analizar el programa real de la cátedra (`Unidad 1/Diseño segun plataformas de juego Plan 2020...pdf`), la **Unidad II se llama "Gestión del testing"** y cubre otra cosa: clasificación de bugs (categoría/severidad/dificultad), tickets/issues, herramientas de tracking (JIRA/TestRail/QAComplete/Confluence), planes de prueba, diseño de casos de prueba, regression/retesting/smoke testing, y solo una **mención breve** del Manifiesto Ágil — sin backlog de producto, sin sprints de features, sin story points ni velocity.

**Decisión adoptada con el docente (modelo híbrido):**
- El **cuerpo evaluable** (archivos `01` a `06` de esta carpeta) es fiel al programa oficial: gestión de bugs y testing.
- El **plan Scrum/Agile completo** originalmente pedido se conserva íntegro como módulo de extensión **no evaluable** en [`06-anexo-scrum-agile.md`](./06-anexo-scrum-agile.md).

---

## Índice de archivos

| Archivo | Contenido |
|---|---|
| [`01-analisis-programa-y-objetivos.md`](./01-analisis-programa-y-objetivos.md) | Análisis del programa (Secc. A), objetivos pedagógicos (Secc. B), conceptos teóricos (Secc. C), relación con Agile sin Scrum completo (Secc. D–E) |
| [`02-caso-cryptbound.md`](./02-caso-cryptbound.md) | Proyecto, equipo, backlog de bugs, plan de pruebas, casos de prueba por género, mapeo a Jira/TestRail/QAComplete/Confluence, errores conceptuales |
| [`03-clase-guion-docente.md`](./03-clase-guion-docente.md) | Estructura de la clase, guía de tiempos y guion bloque por bloque (estilo igual al de `Unidad 1`) |
| [`04-diapositivas.md`](./04-diapositivas.md) | Presentación slide por slide (36 diapositivas) |
| [`05-actividad-practica-y-evaluacion.md`](./05-actividad-practica-y-evaluacion.md) | Actividad práctica en equipos + rúbrica de evaluación |
| [`06-anexo-scrum-agile.md`](./06-anexo-scrum-agile.md) | Módulo de extensión no evaluable: el plan Scrum/Agile completo del encargo original |
| [`07-investigacion-recursos.md`](./07-investigacion-recursos.md) | Recursos investigados y verificados: documentación oficial de Atlassian, videos en español, material sobre videojuegos, comparación y bibliografía |

---

## Relación con otras unidades

```
Unidad I  — Fundamentos y técnicas de testing
             (partición de equivalencia, valores frontera, exploratory testing)
    ↓ aporta el vocabulario técnico que aquí se organiza en tickets
Unidad II — Gestión del testing  ← esta unidad
    ↓ los casos de prueba diseñados aquí se automatizan en la unidad siguiente
Unidad III — Pruebas unitarias con Unity (Unity Test Runner, TDD)
    ↓ el mismo criterio de severidad/prioridad se reutiliza al testear en cada plataforma
Unidades IV–VII — Diseño según plataforma (móvil, consola, PC, emergentes)
```

**Nota sobre datos del programa:** no se especifica un docente auxiliar (JTP) para la materia y 2024 fue su primer dictado, por lo que no hay series históricas de aprobación/desaprobación disponibles para contrastar esta propuesta.
