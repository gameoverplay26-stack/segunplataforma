# SDD-STATUS — Proyecto académico "Arena" (Diseño según Plataforma)

Registro operacional del proceso SDD. Es la **fuente de verdad** del estado de fase. Toda transición de fase requiere aprobación explícita del usuario, registrada en el historial de este archivo.

## Estado actual

```text
Current Phase:            Discovery
Discovery Status:         PASS / CLOSED (REOPENED → CLOSED el 2026-09-25: incorporación de Alt.5)
Next Authorized Phase:    Concept Definition
Infrastructure Bootstrap: COMPLETE (Checkpoint: PASS · Commit: `chore(sdd): bootstrap SDD infrastructure` · rama sdd/infra-bootstrap, local)
Phase Gate Hook:          DEFERRED
Selected Concept:         Alt.5 — Nave + Asteroides (vertical slice provisional: Asteroid Survival) — DEC-001, 2026-09-25
Git Strategy:             RESOLVED — trunk-based + tag por etapa (DEC-007, 2026-09-25). Tag de cierre de Discovery: etapa-00-discovery-complete (local). Rama de Fase 5: sdd/01-concept
Unity project (Arena-SDD/): NOT CREATED
```

## Checkpoints

| Fase | Artefacto | Estado | Nota |
|---|---|---|---|
| Discovery | `docs/00-discovery/PROJECT-DISCOVERY.md` | PASS / CLOSED — solo lectura (REOPENED → CLOSED 2026-09-25) | SHA-256 de referencia vigente (2026-09-25, con Alt.5): `47c6e17a297872741b64a315e23b5c5a630f932546abcf419e1587fcb4f82c7c`, versionado en el commit `docs(sdd): add Alt.5 to Discovery and register DEC-001/DEC-007` (tag `etapa-00-discovery-complete`). Versión anterior (commiteada en `cd2a4a8`): `8c2617301405ac9d35b16f5690cd708448b1d657daca0151d214f314c7e46274`. |
| Infrastructure Bootstrap | `CLAUDE.md`, `.claude/settings.json`, `.claude/agents/`, `.claude/skills/`, este archivo | COMPLETE — PASS, commiteado | Rama `sdd/infra-bootstrap` (creada desde `main`), commit local `chore(sdd): bootstrap SDD infrastructure`. Reglas `deny` y `ask` verificadas empíricamente (ver Historial 2026-09-25). |
| Concept Definition | `docs/01-concept/` | NOT STARTED | Próxima fase autorizada; no se inicia sin instrucción explícita. |

## Decisiones heredadas de Discovery

Fuente: lista formal de `PROJECT-DISCOVERY.md` § "Decisiones pendientes" (7 ítems). IDs `DEC-###` asignados formalmente el 2026-09-25 en el checkpoint de registro de decisiones (fase 4), con la correspondencia `Discovery #N → DEC-00N`. Discovery no se modifica para insertar los IDs.

| Discovery # | ID | Decisión | Fase donde se resuelve | Estado |
|---|---|---|---|---|
| 1 | DEC-001 | Selección del concepto final (Arena / Alt.1–5 / combinación acotada) | Concept Definition | **RESOLVED 2026-09-25 — Alt.5 "Nave + Asteroides" (Asteroid Survival)**. Opción 6 de 7, elegida explícitamente por el usuario. |
| 2 | DEC-002 | Combate melee / ranged / ambos | GDD | PENDING — observación de Discovery: el loop conceptual de Alt.5 usa combate a distancia; no se cierra hasta el GDD. |
| 3 | DEC-003 | Cantidad de tipos de enemigo (asteroides) del vertical slice | GDD | PENDING — se refiere a **tipos**, no a cantidad simultánea. |
| 4 | DEC-004 | Combate MUST HAVE u opcional (Alt.3) | — | **N/A — no aplica al concepto seleccionado.** Discovery la formula para "conceptos donde no es el núcleo (Alt.3)"; en Alt.5 el disparo forma parte del loop base. |
| 5 | DEC-005 | Estrategia de input (interfaz propia vs. Input System con Action Maps) | Technical / Architecture Specification | **DEFERRED** por decisión explícita de Discovery ("no se decide en esta fase"). |
| 6 | DEC-006 | Alcance de power-ups / progresión en el MVP | GDD | PENDING — Discovery (Alt.5) los deja fuera del MVP conceptual; el alcance final se decide en el GDD. |
| 7 | DEC-007 | Estrategia Git: trunk-based + tag por etapa vs. ramas por etapa | Independiente | **RESOLVED 2026-09-25 — trunk-based + tag por etapa** (opción A). Primer tag: `etapa-00-discovery-complete`. El nombre de los tags siguientes se decide al cerrar cada etapa. |

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
- Los cambios del 2026-09-25 (Discovery con Alt.5, este archivo, `CLAUDE.md` §10 y el skill `sdd-workflow`) se versionan en el commit `docs(sdd): add Alt.5 to Discovery and register DEC-001/DEC-007`, integrado a `main` por fast-forward y etiquetado `etapa-00-discovery-complete`. Todo es local, sin push.
- `~/.claude/settings.json` (configuración global del usuario) permite `git push *`, `git reset *` y `git checkout *`. Queda mitigado para este repo por las reglas `ask`/`deny` del proyecto. La configuración global **no** se modifica desde aquí.

## Historial

| Fecha | Evento | Autorizado por |
|---|---|---|
| 2026-09-18 | Discovery completado; checkpoint `PROJECT-DISCOVERY.md`. | Usuario |
| 2026-09-24 | Infrastructure Design Checkpoint: PASS (diseño). | Usuario |
| 2026-09-24 | Autorización de creación de infraestructura; rama `sdd/infra-bootstrap` creada desde `main` (opción A). | Usuario |
| 2026-09-25 | Checkpoint de infraestructura: **PASS**. Regla `ask` verificada con sesiones `claude -p` (`--permission-mode default`): `git clean -n` y `git push --dry-run` quedan en `permission_denials` (el segundo pese a `allow` global), mientras que el control con `allow` global se ejecuta. | Usuario (orden de cierre del paso 1) |
| 2026-09-25 | Commit local de Discovery + infraestructura SDD (`chore(sdd): bootstrap SDD infrastructure`). Infrastructure Bootstrap: COMPLETE. Próximo paso autorizado: decisiones pendientes de Discovery. | Usuario |
| 2026-09-25 | **Discovery REOPENED → CLOSED.** Motivo: incorporación formal de Alt.5 — Nave + Asteroides / *Asteroid Survival*. Cambios: nueva alternativa (sección Alt.5); nueva columna de matriz (estimaciones justificadas; puntuaciones existentes sin cambios); decisión #1 (DEC-001) actualizada con Alt.5; referencias "4 alternativas" y resumen final actualizados. El `deny` sobre `docs/00-discovery/**` se retiró temporalmente y se restauró byte a byte idéntico. Nuevo SHA-256: `47c6e17a…4f82c7c`. No se inició Concept Definition. **Sin commit.** | Usuario (reapertura controlada explícita) |
| 2026-09-25 | **Checkpoint de registro de decisiones (fase 4).** DEC-001 = Alt.5 "Nave + Asteroides" y DEC-007 = A (trunk-based + tag por etapa), ambas elegidas explícitamente por el usuario. Se asignan formalmente DEC-001…DEC-007: DEC-004 = N/A; DEC-005 = DEFERRED; DEC-002, DEC-003 y DEC-006 PENDING para el GDD. Concept Definition autorizada como próxima fase, todavía no iniciada. Sin operaciones git. | Usuario |
| 2026-09-25 | Aplicación de DEC-007: commit `docs(sdd): add Alt.5 to Discovery and register DEC-001/DEC-007` en `sdd/infra-bootstrap`; `main` actualizado por fast-forward; tag local `etapa-00-discovery-complete`; rama `sdd/01-concept` creada desde ese commit. `CLAUDE.md` §10 y el skill `sdd-workflow` actualizados (DEC-007 RESOLVED). Sin push. | Usuario (autorización a+b+c+d) |
