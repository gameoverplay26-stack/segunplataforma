---
name: project-validation
description: Validación manual del estado del proyecto SDD Arena. Revisa especificaciones, estructura documental, integridad del proyecto Unity Arena-SDD/, compilación, tests, evidencias y scope, y emite un reporte VAL con PASS/FAIL/BLOCKED/UNKNOWN por chequeo.
disable-model-invocation: true
argument-hint: "[alcance opcional: docs | unity | tests | scope | all]"
---

# /project-validation — proyecto Arena

Alcance solicitado: `$ARGUMENTS` (vacío = `all`).

Esta validación **solo observa y reporta**:

- no corrige archivos;
- no instala paquetes;
- no abre escenas para modificarlas;
- no hace commit.

Si un chequeo requiere un cambio para pasar, repórtalo como FAIL con la corrección sugerida.

## Reglas de estado

- `PASS`: se verificó con evidencia concreta (salida de comando, archivo, hash, XML).
- `FAIL`: se verificó y no cumple.
- `BLOCKED`: no se puede ejecutar por una precondición externa (p. ej. `Arena-SDD/` no existe todavía, o el Editor tiene el proyecto abierto).
- `UNKNOWN`: no hay evidencia suficiente. **Nunca** convertir UNKNOWN en PASS por inferencia.
- El estado global es el peor estado individual: FAIL > BLOCKED > UNKNOWN > PASS.

## Chequeos

### 1. Estado SDD (`docs`)

- [ ] `docs/SDD-STATUS.md` existe y declara `Current Phase` y `Next Authorized Phase`.
- [ ] No existen artefactos de fases posteriores a la autorizada. Por ejemplo, `docs/02-gdd/` no debe existir si la fase actual es Concept Definition.
- [ ] Nombres de fase canónicos: buscar "Technical Design" y "Validation" usados como nombre de fase fuera de la tabla de inconsistencias.
- [ ] `docs/00-discovery/PROJECT-DISCOVERY.md` intacto. Con `git diff --stat -- docs/00-discovery/` si está versionado; si no lo está, reportar UNKNOWN salvo que exista un hash de referencia registrado.

### 2. Especificaciones y trazabilidad (`docs`)

- [ ] Si existe `docs/TRACEABILITY.md`:
  - cada REQ tiene criterio de aceptación;
  - los IDs referenciados existen;
  - no hay IDs duplicados;
  - cada REQ relevante tiene candidato unit/integration o "N/A" con motivo.
- [ ] Las decisiones pendientes (DEC-###) no aparecen como resueltas sin registro de aprobación en el Historial de `SDD-STATUS.md`.

### 3. Integridad Unity (`unity`), solo `Arena-SDD/`

- [ ] `Arena-SDD/` existe. Si no existe y la fase es anterior a Implementation, el resultado es BLOCKED (esperado), no FAIL.
- [ ] `Arena-SDD/ProjectSettings/ProjectVersion.txt` → `m_EditorVersion: 6000.3.11f1`.
- [ ] `git diff --stat -- Arena-SDD/Packages Arena-SDD/ProjectSettings`: cada cambio corresponde a una autorización registrada.
- [ ] Compilación, con el proyecto cerrado en el Editor:

  ```bash
  "/c/Program Files/Unity/Hub/Editor/6000.3.11f1/Editor/Unity.exe" -batchmode -quit -projectPath Arena-SDD -logFile <scratch>/compile.log
  ```

  Evidencia: código de salida + ausencia de `error CS` en el log.

### 4. Tests (`tests`)

- [ ] Ejecutar Edit Mode y Play Mode según el skill `unity-testing` (sección "Ejecución y evidencia").
- [ ] Reportar passed/failed/skipped desde el XML, no desde el log.
- [ ] Tests con `[Ignore]` → listar con motivo.
- [ ] Tests sin `Property("Trace", ...)` → listar.

### 5. Scope (`scope`)

- [ ] `git status` / `git diff --stat` restringido al alcance SDD.
- [ ] Cada archivo cambiado en `Arena-SDD/` se justifica por un SPEC/ARCH o por un DEV-###.
- [ ] Hay cambios fuera del alcance SDD (material de cátedra, otros proyectos Unity) → listarlos como **fuera de scope de esta validación**. No es un FAIL automático, pero hay que informarlo.
- [ ] No aparecen funcionalidades marcadas OUT OF SCOPE en Discovery (multiplayer real, backend, monetización).

## Reporte

```text
VAL-### — PROJECT VALIDATION — <fecha> — alcance: <...>
Rama: <git branch --show-current>   Fase (SDD-STATUS): <...>

| # | Chequeo | Estado | Evidencia |

Estado global: PASS | FAIL | BLOCKED | UNKNOWN
Correcciones sugeridas (no aplicadas): <lista>
```

Asigna el siguiente `VAL-###` libre. Si `docs/08-verification/` no existe todavía, entrega el reporte en la conversación y **no** crees la carpeta. Si existe y la fase lo permite, ofrece guardarlo ahí.
