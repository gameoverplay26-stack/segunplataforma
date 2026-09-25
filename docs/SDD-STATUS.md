# SDD-STATUS — Proyecto académico "Arena" (Diseño según Plataforma)

Registro operacional del proceso SDD. Es la **fuente de verdad** del estado de fase. Toda transición de fase requiere aprobación explícita del usuario, registrada en el historial de este archivo.

## Estado actual

```text
Current Phase:            Discovery
Discovery Status:         PASS / CLOSED
Next Authorized Phase:    Concept Definition
Infrastructure Bootstrap: COMPLETE (Checkpoint: PASS · Commit: `chore(sdd): bootstrap SDD infrastructure` · rama sdd/infra-bootstrap, local)
Phase Gate Hook:          DEFERRED
Selected Concept:         NONE (pendiente — Discovery #1)
Unity project (Arena-SDD/): NOT CREATED
```

## Checkpoints

| Fase | Artefacto | Estado | Nota |
|---|---|---|---|
| Discovery | `docs/00-discovery/PROJECT-DISCOVERY.md` | PASS / CLOSED — solo lectura | Sin versionar en git a la fecha de este registro (ver "Pendientes operativos"). SHA-256 de referencia (2026-09-24): `8c2617301405ac9d35b16f5690cd708448b1d657daca0151d214f314c7e46274` |
| Infrastructure Bootstrap | `CLAUDE.md`, `.claude/settings.json`, `.claude/agents/`, `.claude/skills/`, este archivo | COMPLETE — PASS, commiteado | Rama `sdd/infra-bootstrap` (creada desde `main`), commit local `chore(sdd): bootstrap SDD infrastructure`. Reglas `deny` y `ask` verificadas empíricamente (ver Historial 2026-09-25). |
| Concept Definition | `docs/01-concept/` | NOT STARTED | Próxima fase autorizada; no se inicia sin instrucción explícita. |

## Decisiones pendientes heredadas de Discovery

Se listan tal como figuran en `PROJECT-DISCOVERY.md` § "Decisiones pendientes". Los IDs `DEC-###` se asignan formalmente en **Concept Definition**. La única excepción es DEC-007, ya referida con ese ID en la autorización del bootstrap. **Ninguna está resuelta.**

| Discovery # | Decisión | ID | Fase donde se resuelve | Estado |
|---|---|---|---|---|
| 1 | Selección del concepto final (Arena / Alt.1–4 / combinación acotada) | se asigna en Concept Definition | Concept Definition | PENDING |
| 2 | Combate melee / ranged / ambos | se asigna en Concept Definition | GDD | PENDING |
| 3 | Cantidad de tipos de enemigo del vertical slice | se asigna en Concept Definition | GDD | PENDING |
| 4 | Combate MUST HAVE u opcional (Alt.3) | se asigna en Concept Definition | GDD | PENDING |
| 5 | Estrategia de input (interfaz propia vs. Input System con Action Maps) | se asigna en Concept Definition | Technical / Architecture Specification | PENDING |
| 6 | Alcance de power-ups / progresión en el MVP | se asigna en Concept Definition | GDD | PENDING |
| 7 | Estrategia Git: trunk-based + tag por etapa vs. ramas por etapa | **DEC-007** | a definir por el usuario | PENDING — recomendación, no regla |

## Inconsistencias documentales registradas

No se corrigen en `PROJECT-DISCOVERY.md` (checkpoint cerrado). Se resuelven en la fase indicada.

| ID | Inconsistencia | Resolución vigente |
|---|---|---|
| INC-01 | La tabla "Estrategia SDD" de Discovery marca la fila Discovery como "Completo, pendiente de revisión del usuario"; el bloque final dice `STATUS: DISCOVERY COMPLETE`. | El usuario declaró Discovery **PASS / CLOSED** (autorización del bootstrap). |
| INC-02 | Discovery propone las carpetas `docs/03-technical-design/` y `docs/08-validation/`; la nomenclatura canónica de fases es "Technical Specification" y "Verification". | Carpetas autorizadas: `docs/03-technical-specification/` y `docs/08-verification/`. `08-verification/` aloja la evidencia de Verification, Integration Testing y Regression Testing (mismo rol que Discovery asignaba a `08-validation/`). |
| INC-03 | "Próximos pasos" y `NEXT AUTHORIZED STEP` de Discovery agrupan "Concept selection + GDD specification"; la tabla SDD las separa en dos fases. | Próxima fase autorizada: **Concept Definition** únicamente. El GDD requiere su propia autorización. |
| INC-04 | El brief del bootstrap usaba "Technical Design" y "Validation" como nombres de fase. | Se usa la nomenclatura de Discovery ("Technical Specification", "Verification"), por decisión del usuario. |

## Phase Gate Hook — DEFERRED

- **Qué sería:** un hook `PreToolUse` que bloquee ediciones de C#, escenas, prefabs, `Packages/` y `ProjectSettings/` en `Arena-SDD/` mientras `Current Phase` sea anterior a Implementation.
- **Por qué se difiere:** `Arena-SDD/` no existe y sus rutas protegidas no pueden definirse con precisión.
- **Cuándo se evalúa:** antes de comenzar Implementation.
- **Mientras tanto:** la protección depende de `CLAUDE.md` (instrucción) y de `.claude/settings.json` (Discovery `deny`, git `ask`/`deny`).

## Pendientes operativos (no son decisiones de producto)

- `docs/00-discovery/PROJECT-DISCOVERY.md` y la infraestructura del bootstrap quedan versionados en el commit `chore(sdd): bootstrap SDD infrastructure` (rama `sdd/infra-bootstrap`, sin push).
- `.claude/settings.local.json` es configuración personal preexistente: queda **fuera** del control de versiones por decisión del usuario.
- Archivos untracked **PREEXISTENTES / AJENOS AL BOOTSTRAP** (no se commitean, no se modifican, no se ignoran): `Asteroides.zip`, `Asteroides/`, `Introduction-To-Unity-Unit-Testing.zip`, `Introduction-To-Unity-Unit-Testing/`, `Match-3-Game/`, `com.unity.multiplayer.samples.coop/`, `Unidad 3 -2024.pptx`.
- `~/.claude/settings.json` (configuración global del usuario) permite `git push *`, `git reset *` y `git checkout *`. Queda mitigado para este repo por las reglas `ask`/`deny` del proyecto. La configuración global **no** se modifica desde aquí.

## Historial

| Fecha | Evento | Autorizado por |
|---|---|---|
| 2026-09-18 | Discovery completado; checkpoint `PROJECT-DISCOVERY.md`. | Usuario |
| 2026-09-24 | Infrastructure Design Checkpoint: PASS (diseño). | Usuario |
| 2026-09-24 | Autorización de creación de infraestructura; rama `sdd/infra-bootstrap` creada desde `main` (opción A). | Usuario |
| 2026-09-25 | Checkpoint de infraestructura: **PASS**. Regla `ask` verificada con sesiones `claude -p` (`--permission-mode default`): `git clean -n` y `git push --dry-run` quedan en `permission_denials` (el segundo pese a `allow` global), mientras que el control con `allow` global se ejecuta. | Usuario (orden de cierre del paso 1) |
| 2026-09-25 | Commit local de Discovery + infraestructura SDD (`chore(sdd): bootstrap SDD infrastructure`). Infrastructure Bootstrap: COMPLETE. Próximo paso autorizado: decisiones pendientes de Discovery. | Usuario |
