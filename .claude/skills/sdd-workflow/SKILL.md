---
name: sdd-workflow
description: Flujo Spec-Driven Development del proyecto académico Arena (docs/00-discovery … docs/08-verification, Arena-SDD/). Úsalo antes de producir o modificar cualquier artefacto SDD, al cambiar de fase, al preguntar "en qué fase estamos" o "qué sigue", y para asignar IDs de trazabilidad. Impide saltos de fase no autorizados. No aplica a material de cátedra (docs/unidadNN/) ni a otros proyectos Unity del repo.
---

# SDD workflow — proyecto Arena

## Paso 0: siempre

1. Lee `docs/SDD-STATUS.md`. Es la fuente de verdad de:
   - `Current Phase`
   - `Next Authorized Phase`
   - decisiones pendientes
   - inconsistencias registradas
2. Si la tarea no toca rutas del alcance SDD (`CLAUDE.md` §2), esta skill no aplica.

## Secuencia canónica

```text
Discovery → Concept Definition → Game Design Specification (GDD) → Technical Specification
→ Architecture Specification → Test Strategy → Implementation → Verification
→ Integration Testing → Platform Adaptation → Regression Testing
```

Estos son los nombres de Discovery. **No** usar "Technical Design" ni "Validation" como nombres de fase. Para cada fase, las entradas, los entregables, la carpeta, el criterio de salida y los permisos están en [phases.md](phases.md).

## Reglas de transición (impiden saltos de fase)

1. Solo se producen artefactos de `Current Phase`, o de `Next Authorized Phase` si el usuario ordenó iniciarla explícitamente.
2. Si una tarea exige contenido de una fase posterior:
   - **detente**;
   - di qué fase falta y qué aprobación se necesita;
   - no lo produzcas "como borrador adelantado".
3. Una fase se cierra solo cuando el usuario aprueba su checkpoint. Esa aprobación se registra en `SDD-STATUS.md` (sección Historial), con fecha.
4. Al terminar el trabajo de una fase, emite un checkpoint con este formato:

   ```text
   <FASE> — CHECKPOINT
   Artefactos: <rutas>
   IDs creados: <lista>
   Decisiones pendientes: <lista>
   Inconsistencias nuevas: <lista>
   Estado: PASS | FAIL | BLOCKED | UNKNOWN — <motivo>
   Próximo paso sugerido (requiere aprobación): <fase>
   ```

   Después, espera la aprobación del usuario.
5. Revisar un documento aprobado de una fase anterior requiere autorización explícita. El cambio se registra en el Historial.

## Decisiones

- Las decisiones de producto y diseño son del usuario. Claude presenta opciones con consecuencias y **no elige**.
- Las decisiones heredadas de Discovery (#1–#7) tienen IDs `DEC-001`…`DEC-007`, asignados el 2026-09-25. Su estado vigente está en `docs/SDD-STATUS.md`. DEC-007 (estrategia Git): **RESOLVED — trunk-based + tag por etapa**.
- Una decisión se marca RESOLVED solo con aprobación explícita, registrada con fecha.

## Discovery = CLOSED CHECKPOINT

`docs/00-discovery/PROJECT-DISCOVERY.md` no se modifica (además, `.claude/settings.json` lo bloquea con `deny`). Las inconsistencias que se encuentren se agregan a la tabla de inconsistencias de `SDD-STATUS.md` (`INC-##`).

## Trazabilidad

La convención de IDs, la cadena REQ → … → VAL y el formato de `docs/TRACEABILITY.md` están en [traceability.md](traceability.md). `TRACEABILITY.md` se crea recién cuando Concept Definition genera los primeros requisitos trazables.
