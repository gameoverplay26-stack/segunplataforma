# Anexo — Módulo de extensión: Jira para producción completa (Scrum)

> **No evaluable. No forma parte del programa oficial de esta unidad.** Se conserva porque el encargo original lo pedía en detalle, y porque es un contenido genuinamente valioso si la cátedra decide ampliarlo o si otra instancia de la carrera lo retoma.

El encargo original pedía un desarrollo completo con el mismo estudio de caso (Cryptbound), llevado ahora al plano de producción en lugar de QA: un Product Backlog con Epics (Player, Combate, Enemigos, Nivel, UI, Audio, Sistema de Guardado), historias de usuario ("Como jugador quiero moverme para explorar el nivel"), tareas, priorización por valor/riesgo/esfuerzo/MVP, estimación con Story Points (Fibonacci, sin ser horas), un Sprint 1 "Player Prototype" con capacidad de 20 SP frente a una lista de 30 SP disponibles (obligando a decidir qué queda afuera), Sprint Goal, y los roles Product Owner / Scrum Master / Developers mapeados sobre el mismo equipo de 7 personas.

## Esqueleto de esa clase alternativa (referencia, sin desarrollar a fondo)

```
Problema de producción: hay más funcionalidades que tiempo de equipo
        ↓
Agile → Scrum: roles, artefactos, eventos
        ↓
Product Backlog de Cryptbound: Epics → Stories → Tasks
        (distinto del backlog de bugs de la Unidad II)
        ↓
Priorización por valor/riesgo/esfuerzo, MVP
        ↓
Story Points (Fibonacci) — explícitamente no son horas
        ↓
Sprint 1 "Player Prototype": capacidad 20 SP, backlog disponible 30 SP
        → qué entra y qué no
        ↓
Jira como tablero de producción: Backlog view, Sprint board, Burndown, Velocity
```

### Ejemplo de Product Backlog (Epics → Stories → Tasks → Bugs)

- **Epic: Player** → Story: "Como jugador quiero mover a mi personaje para poder explorar el nivel" → Tasks: implementar movimiento, configurar input, crear animaciones, implementar colisiones.
- **Epic: Combate** → Story: "Como jugador quiero atacar cuerpo a cuerpo para derrotar enemigos."
- **Epic: Enemigos** → Story: "Como jugador quiero que el arquero reaccione a mi presencia para que el combate sea táctico."
- **Epic: UI** → Story: "Como jugador quiero ver mi vida e inventario en pantalla para tomar decisiones informadas."
- **Epic: Sistema de Guardado** → Story: "Como jugador quiero guardar mi progreso para continuar otro día."

### Ejemplo de estimación con Story Points

| Ítem | Story Points |
|---|---|
| Movimiento del jugador | 3 |
| Salto | 3 |
| Cámara | 3 |
| Animaciones | 5 |
| Colisiones | 3 |
| Sistema de combate | 8 |
| IA del enemigo arquero | 8 |

**Story Points NO son horas** — miden complejidad/esfuerzo/incertidumbre relativa, no tiempo de reloj.

### Ejemplo de Sprint 1 — "Player Prototype"

**Objetivo del sprint:** crear un personaje jugable capaz de desplazarse dentro del primer nivel.

Backlog disponible: Movimiento (5 SP), Salto (3 SP), Cámara (3 SP), Animaciones (5 SP), Colisiones (3 SP), Combate (8 SP), IA enemigo (8 SP) — total 35 SP.

Capacidad del equipo: ~20 SP.

**Ejercicio para los estudiantes (si se dicta este módulo):** decidir qué entra en el sprint sin superar los 20 SP, priorizando lo que sostiene el Sprint Goal. La intención pedagógica: el Sprint no consiste en meter todo lo posible; consiste en alcanzar un objetivo con una capacidad limitada.

---

## Referencia estructural: qué cubre un curso pago especializado en esto

Se revisó públicamente la página del curso pago *Mastering Jira for Game Producers* (GameDevStation, `gamedevstation.com/course/mastering-jira-for-game-producers/`) solo para identificar qué temas suelen agruparse bajo "Jira para producción" en la industria, sin acceder a contenido protegido:

| Módulo (según página pública) | Qué cubre |
|---|---|
| 2. Preparación para usar Jira | Caso de uso, jerarquía básica, anatomía de un issue, tableros, filtros. |
| 3. Estructura apropiada de Jira | Tipos de trabajo, workflows, componentes/etiquetas, versiones. |
| 4. Funcionalidades clave | Product Backlog, dependencias, dashboards, **planificación de sprints**. |
| 5. Expansión | Confluence como complemento, wiki de equipo. |

Confirma, desde la industria, la misma distinción que organiza todo este documento: gestionar **bugs** (Unidad II) y gestionar **producción** (este Anexo) son configuraciones distintas de la misma herramienta. El curso es de pago — no se referencia como fuente de contenido, solo como evidencia de que la distinción es real y reconocida profesionalmente.
