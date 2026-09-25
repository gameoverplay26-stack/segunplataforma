# CLAUDE.md — clases-en-vivo

## 1. Qué contiene este repositorio

Este repositorio **no es un único proyecto**. Contiene contextos independientes:

| Contexto | Ubicación | Reglas que aplican |
|---|---|---|
| Material de cátedra "Diseño según Plataforma" (UNJu) | `docs/unidadNN/`, `Unidad 1/`, archivos `.md`/`.pptx`/`.pdf`/`.docx` de la raíz | Convenciones propias de cada unidad. **No** aplican las reglas SDD. |
| Proyectos Unity de clase / ejemplos | `Asteroides/`, `Match-3-Game/`, `Unidad03-TestingUnity/`, `com.unity.multiplayer.samples.coop/` (Boss Room), `Introduction-To-Unity-Unit-Testing/` | Independientes entre sí. **No** aplican las reglas SDD. |
| **Proyecto académico SDD "Arena"** | ver §2 | **Reglas SDD de este archivo (§3–§10).** |

Si una tarea no toca rutas del §2, ignorar §3–§10 y trabajar según el contexto correspondiente.

## 2. Alcance SDD (único ámbito gobernado por §3–§10)

```text
docs/00-discovery/                  # CLOSED CHECKPOINT — solo lectura
docs/SDD-STATUS.md                  # registro operacional de fase (fuente de verdad del estado)
docs/01-concept/
docs/02-gdd/
docs/03-technical-specification/
docs/04-architecture/
docs/05-testing/
docs/06-platform/
docs/07-implementation/
docs/08-verification/
Arena-SDD/                          # único proyecto Unity gobernado por SDD (aún no existe)
```

Las carpetas que todavía no existen se crean **solo** al entrar en la fase que las produce.

Plataforma técnica: Unity `6000.3.11f1`, C#, PC primero y Mobile después.

## 3. SDD obligatorio

Secuencia canónica (nomenclatura de `docs/00-discovery/PROJECT-DISCOVERY.md`):

```text
Discovery → Concept Definition → Game Design Specification (GDD) → Technical Specification
→ Architecture Specification → Test Strategy → Implementation → Verification
→ Integration Testing → Platform Adaptation → Regression Testing
```

- Antes de producir cualquier artefacto SDD, leer `docs/SDD-STATUS.md`.
- No producir artefactos de una fase posterior a la autorizada ahí.
- Una fase avanza solo con **aprobación explícita del usuario**, registrada en `SDD-STATUS.md`.
- No implementar nada sin especificación aprobada.
- Usar "Technical Specification" y "Verification", nunca "Technical Design" ni "Validation", como nombres de fase.
- Flujo detallado: skill `sdd-workflow`.

## 4. Decisiones

- Claude **analiza, propone y verifica**. Las decisiones de producto y de diseño del juego las toma el usuario.
- Las decisiones pendientes se registran (como `DEC-###` a partir de Concept Definition) y **no se resuelven por inferencia**.
- No hay un concepto de juego seleccionado mientras `SDD-STATUS.md` no lo registre.

## 5. Discovery = CLOSED CHECKPOINT

`docs/00-discovery/PROJECT-DISCOVERY.md` es de **solo lectura**: no se corrige, no se reescribe y no se completan dentro de él las decisiones pendientes. Las inconsistencias que se detecten se registran en `SDD-STATUS.md`. La protección mecánica está en `.claude/settings.json` (`deny`).

## 6. Control de alcance

- No agregar funcionalidades "porque serían útiles".
- Todo cambio en `Arena-SDD/` debe trazarse a una especificación aprobada o a un desvío registrado (`DEV-###` en `docs/07-implementation/`).
- Lo que el Discovery declara OUT OF SCOPE (multiplayer real, backend, monetización, contenido masivo) sigue fuera de alcance.

## 7. Evidencia primero

- No afirmar que algo "funciona", "compila" o "pasa" sin evidencia: XML del test runner, log de compilación de Unity en batchmode o salida de comando.
- Sin evidencia, el estado es `UNKNOWN`.
- Estados permitidos en checkpoints: `PASS`, `FAIL`, `BLOCKED`, `UNKNOWN`.

## 8. Seguridad en Unity (`Arena-SDD/`)

No modificar escenas, prefabs, assets, `ProjectSettings/` ni `Packages/` fuera de la fase que lo autoriza (ver matriz en skill `sdd-workflow`, archivo `phases.md`). **Nunca** instalar ni actualizar paquetes sin autorización explícita del usuario para ese paquete. No editar a mano archivos YAML de escenas o prefabs salvo instrucción explícita.

## 9. Testing y plataforma

- Toda funcionalidad relevante identifica su **candidato a unit test** y su **candidato a integration test**, o "N/A" con motivo.
- Un test sobre una clase aislada es Unit, aunque corra en Play Mode. Detalle en el skill `unity-testing`.
- El gameplay no se duplica por plataforma: el input PC/Mobile se adapta detrás de una abstracción común (skill `unity-platform`).
- La forma concreta de esa abstracción es una decisión pendiente (Discovery #5).

## 10. Git

- **No** hacer commit, tag, push, merge, rebase ni cambios de rama sin pedido explícito del usuario.
- No reescribir historial.
- La estrategia "trunk-based + tag por etapa" es una **recomendación pendiente (DEC-007)**, no una regla.
- `.claude/settings.json` exige confirmación para operaciones git destructivas y deniega `git push --force`.

## Infraestructura Claude de este repo

- Agents (`.claude/agents/`):
  - `spec-reviewer`: revisión, solo lectura.
  - `sdd-architect`: especificaciones.
  - `unity-engineer`: implementación y adaptación de plataforma.
  - `test-engineer`: tests y evidencia.
- Skills (`.claude/skills/`):
  - `sdd-workflow`
  - `unity-testing`
  - `unity-platform`
  - `project-validation` (solo manual: `/project-validation`)
- Hooks: ninguno. El phase-gate hook está **DEFERRED** (ver `docs/SDD-STATUS.md`).
