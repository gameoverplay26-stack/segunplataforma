# Unidad 2 — Clase 1: Gestión del Testing (guion docente)

**Materia:** Diseño según Plataformas de Juego
**Carrera:** Tecnicatura Universitaria en Diseño Integral de Videojuegos (Plan 2020)
**Docente:** Ing. Elsa Daniela Ramírez
**Ciclo lectivo:** 2026
**Unidad:** 2 — Gestión del testing
**Duración:** 120 minutos
**Resultados de aprendizaje vinculados:** RA01, RA03.
**Competencias específicas vinculadas:** CE05, CE06, CE07, CE11, CE12.

Metodología AMMIL / flipped-classroom del programa: se asume que los estudiantes ya vieron la píldora de video y el apunte de esta semana antes de la clase.

---

## Sección O — Estructura completa de la clase

```
1. El problema: un playtest genera 12 bugs en 90 minutos y nadie los anota bien
        ↓
2. Repaso rápido: testing y QA (Unidad I)
        ↓
3. Mención breve: Agile y testing continuo
        ↓
4. De la queja al ticket: qué información hace accionable un bug
        ↓
5. Clasificación: categoría, severidad, prioridad, dificultad
        ↓
6. Herramientas: Jira vs. TestRail vs. QAComplete vs. Confluence
        ↓
7. Jira en detalle: issue, workflow, board, dashboards
        ↓
8. Regression / retesting / smoke testing
        ↓
9. Riesgo, plan de pruebas y casos de prueba por género
        ↓
10. Ciclo de vida del videojuego y el testing en cada hito
        ↓
11. [Extensión, opcional] Jira también gestiona producción — Scrum, brevemente
        ↓
12. Errores conceptuales frecuentes
        ↓
13. Actividad práctica en equipos
        ↓
14. Cierre y preguntas
```

---

## Guía de tiempos (120 min)

| # | Min | Bloque | Qué decir / hacer | Evitar |
|---|-----|--------|---------------------|--------|
| 1 | 0–10 | Problema + repaso | Abrir con 3–4 quejas coloquiales del playtest (ver Actividad, Sección R). Preguntar qué se pierde si viven solo en un chat. Enlazar 30 segundos con Unidad I (no reexplicar). | No convertir el repaso en una clase nueva de 20 minutos. |
| 2 | 10–15 | Equipo y proyecto | Presentar Cryptbound y los 7 roles, con Marisol (QA) al centro. | No demorarse en lore del juego — es un vehículo, no el tema. |
| 3 | 15–20 | Agile, la idea mínima | Una sola idea: el testing es continuo, no una fase final. Sin nombrar sprints ni backlog todavía. | No dejarse arrastrar a preguntas sobre Scrum aquí — anotarlas para el bloque de extensión. |
| 4 | 20–30 | Del ticket a la clasificación | Mostrar CRYPT-107 en bruto ("se rompe cuando guardás") y reescribirlo en vivo con la clase como ticket completo. | No dar la respuesta antes de pedirle a la clase que intente completar los pasos. |
| 5 | 30–45 | Severidad, prioridad, dificultad | Usar CRYPT-102, 108 y 111 como los tres ejemplos que rompen la intuición ("si es grave, es urgente"). Ejercicio rápido con CRYPT-104/106/109, votación a mano alzada. | El error clásico: dejar que la clase entienda severidad = prioridad y avanzar sin corregirlo. Confirmar explícitamente antes de seguir. |
| 6 | 45–60 | Herramientas y Jira | Tabla comparativa primero (por qué existen varias herramientas), después Jira en detalle: issue, el dato de que severidad no es nativa, workflow, board. | No dar un tour de botones de la interfaz actual de Jira — la UI cambia, el concepto no. |
| 7 | 60–75 | Regression / retest / smoke + riesgo | Usar el trío de ejemplos de Cryptbound (retest de CRYPT-103, regresión de CRYPT-107, smoke diario). Preguntar por dónde empezarían con 2 días de regresión y 5 sistemas (riesgo). | No dejar que "regression testing" quede como sinónimo vago de "volver a probar todo". |
| 8 | 75–95 | Plan de pruebas y casos de prueba | Mostrar el plan de pruebas completo de Cryptbound v0.3. Recorrer los 3 casos de prueba por género, marcando explícitamente la conexión con partición de equivalencia/valores frontera de Unidad I. | No presentar el plan de pruebas como papeleo burocrático — mostrar qué decisión evita cada campo. |
| 9 | 95–100 | Ciclo de vida + errores conceptuales | Ubicar el testing en los 4 hitos. Repasar 3–4 errores conceptuales, priorizando severidad≠prioridad y Jira≠Scrum. | No leer todas las filas de corrido — elegir las que resonaron con dudas de la clase. |
| 10 | 100–105 | Bloque de extensión (opcional) | Mencionar en 2 minutos que Jira también gestiona producción completa (backlog, sprints) y que eso se retoma en el anexo si la cátedra lo decide ampliar. | No empezar a explicar Story Points aquí — es la trampa más probable de irse de tema. |
| 11 | 105–120 | Actividad práctica | Formar equipos, entregar el informe de playtest crudo, circular resolviendo dudas de clasificación. | No resolver la clasificación por ellos — señalar el criterio, no la respuesta. |

**Total: 120 minutos.**

---

## Notas de contenido por bloque (referencias cruzadas)

- **Bloque 4 (severidad/prioridad):** contenido teórico completo en [`01-analisis-programa-y-objetivos.md`](./01-analisis-programa-y-objetivos.md), Sección C.
- **Bloque 6 (Jira, TestRail, QAComplete, Confluence):** tabla comparativa completa en [`02-caso-cryptbound.md`](./02-caso-cryptbound.md), Sección I.
- **Bloque 8 (plan de pruebas y casos de prueba):** ejemplos completos en [`02-caso-cryptbound.md`](./02-caso-cryptbound.md), Sección H.
- **Bloque 10 (extensión Scrum):** desarrollo completo en [`06-anexo-scrum-agile.md`](./06-anexo-scrum-agile.md).
- **Diapositivas sugeridas por bloque:** ver [`04-diapositivas.md`](./04-diapositivas.md) (36 slides numeradas, mapeadas a estos mismos bloques).
