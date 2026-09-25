# Fases SDD — detalle y matriz de autorización

La nomenclatura y la secuencia provienen de `docs/00-discovery/PROJECT-DISCOVERY.md` § "Estrategia SDD". Las carpetas siguen la autorización del bootstrap (ver INC-02 en `docs/SDD-STATUS.md`).

## Fases

| # | Fase | Entrada | Entregable / carpeta | Criterio de salida | Agente principal |
|---|---|---|---|---|---|
| 0 | Discovery | Idea | `docs/00-discovery/PROJECT-DISCOVERY.md` | **CERRADA** (PASS) | — |
| 1 | Concept Definition | Discovery + elección del usuario | `docs/01-concept/` | Concepto aprobado por escrito; decisiones #1–#7 registradas como DEC-### | sdd-architect → spec-reviewer |
| 2 | Game Design Specification (GDD) | Concept Definition | `docs/02-gdd/` | GDD mínimo (Concept, Gameplay, Scope MoSCoW) aprobado; REQ-### con criterio de aceptación | sdd-architect → spec-reviewer |
| 3 | Technical Specification | GDD | `docs/03-technical-specification/` | Requisitos técnicos verificables (TECH-###), plataformas y paquetes propuestos | sdd-architect → spec-reviewer |
| 4 | Architecture Specification | Technical Specification | `docs/04-architecture/` | Componentes, interfaces y eventos (ARCH-###) validados contra puntos de test; abstracción de input definida | sdd-architect → spec-reviewer |
| 5 | Test Strategy | Architecture Specification | `docs/05-testing/` | Casos unit/integration por sistema (TEST-UNIT/TEST-INT diseñados, sin código) | test-engineer → spec-reviewer |
| 6 | Implementation | Todas las specs anteriores | `Arena-SDD/` + `docs/07-implementation/` (DEV-###) | Cumple los MUST HAVE del GDD; compila (log) | unity-engineer |
| 7 | Verification | Implementation | `docs/08-verification/` | Suite de unit tests en verde, con XML del runner | test-engineer |
| 8 | Integration Testing | Verification | `docs/08-verification/` | Flujos end-to-end en verde, con XML del runner | test-engineer |
| 9 | Platform Adaptation | Integration Testing | `docs/06-platform/` + `Arena-SDD/` | Mismo gameplay con input Mobile, sin duplicar lógica; suite sigue en verde | unity-engineer (skill unity-platform) |
| 10 | Regression Testing | Platform Adaptation | `docs/08-verification/` | Cada BUG-### aprobado es detectado por ≥1 test existente (antes/después) | test-engineer + unity-engineer |

Notas:

- `docs/06-platform/` puede recibir la **estrategia** de plataforma durante Architecture Specification. La **adaptación** ocurre en la fase 9.
- `/project-validation` (manual) puede ejecutarse en cualquier fase y emite VAL-###.
- Phase gate hook: **DEFERRED** hasta antes de Implementation (ver `SDD-STATUS.md`).

## Matriz de autorización

`✓` = permitido en la fase · `✗` = prohibido · `explícito` = requiere autorización del usuario para ese caso concreto · `aprob.` = requiere aprobación explícita y registro en el Historial.

| Acción | Discovery | Concept | GDD | Tech / Arch | Test Strategy | Implementation | Verification / Integration / Platform / Regression |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Leer / analizar | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Docs de la fase actual | — (cerrada) | ✓ | ✓ | ✓ | ✓ | ✓ (`07-`) | ✓ (`06-`, `08-`) |
| Docs de fases anteriores | ✗ | ✗ (Discovery cerrado) | aprob. | aprob. | aprob. | aprob. | aprob. |
| `docs/00-discovery/` | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |
| Crear `Arena-SDD/` (proyecto Unity) | ✗ | ✗ | ✗ | ✗ | ✗ | explícito | — |
| C# de gameplay | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ (según SPEC) | solo fixes con BUG/DEV |
| C# de tests | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ |
| Escenas / prefabs | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ (según SPEC) | aprob. |
| `ProjectSettings/` / `Packages/` | ✗ | ✗ | ✗ | ✗ | ✗ | explícito | explícito |
| Instalar paquetes | ✗ | ✗ | ✗ | ✗ | ✗ | explícito | explícito |
| Ejecutar tests existentes | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Introducir bugs intencionales | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | solo en Regression, BUG-### aprobado |
| Commit / tag / push / rama | explícito | explícito | explícito | explícito | explícito | explícito | explícito |

La matriz es una **propuesta aprobada para el bootstrap**. Su endurecimiento mecánico (phase gate hook) está diferido.
