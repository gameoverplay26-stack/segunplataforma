# Trazabilidad — convención de IDs

## Cadena

```text
DEC (decisión del usuario)
  ↓
REQ (requisito funcional, GDD) ──► TECH (requisito técnico, Technical Specification)
  ↓
SPEC (especificación de comportamiento verificable)
  ↓
ARCH (componente / interfaz / evento)
  ↓
Implementación en Arena-SDD/ (+ DEV si hay desvío)
  ↓
TEST-UNIT ──► TEST-INT
  ↓
VAL (evidencia: XML del runner, log, captura)
```

`BUG-###` (bugs intencionales de Regression Testing) apunta al REQ o SPEC que viola y al test que debe detectarlo.

## Prefijos

| Prefijo | Qué identifica | Se crea en | Dónde vive |
|---|---|---|---|
| `DEC-###` | Decisión (pendiente o resuelta) | Concept Definition en adelante | `docs/SDD-STATUS.md` → `TRACEABILITY.md` |
| `REQ-###` | Requisito funcional | GDD | `docs/02-gdd/` |
| `TECH-###` | Requisito técnico | Technical Specification | `docs/03-technical-specification/` |
| `SPEC-###` | Comportamiento especificado, con criterio de aceptación | GDD / Technical Specification | carpeta de la fase |
| `ARCH-###` | Componente, interfaz o evento | Architecture Specification | `docs/04-architecture/` |
| `TEST-UNIT-###` | Unit test | Test Strategy (diseño) → Implementation (código) | `docs/05-testing/` + `Arena-SDD/` |
| `TEST-INT-###` | Integration test | Test Strategy → Implementation | `docs/05-testing/` + `Arena-SDD/` |
| `DEV-###` | Desvío respecto de una spec | Implementation en adelante | `docs/07-implementation/` |
| `BUG-###` | Bug intencional aprobado | Regression Testing (hereda de `BUG-CAND-0N` de Discovery) | `docs/08-verification/` |
| `VAL-###` | Evidencia de validación (`/project-validation` o ejecución de suite) | cualquier fase | `docs/08-verification/` |
| `INC-##` | Inconsistencia documental | cualquier fase | `docs/SDD-STATUS.md` |

## Reglas

1. Los IDs son secuenciales por prefijo, con tres dígitos, y **nunca se reutilizan**. Un ID descartado queda como `WITHDRAWN` con motivo.
2. Se crea un ID **solo** cuando existe el artefacto que identifica. No hay IDs de reserva ni se generan en masa.
3. Cada REQ declara su candidato a unit test y su candidato a integration test, o "N/A" con motivo.
4. En el código, los tests se enlazan con atributos NUnit (soportados por Unity Test Framework):

   ```csharp
   [Test, Property("Id", "TEST-UNIT-001"), Property("Trace", "REQ-003")]
   ```

   Así, el XML de resultados del runner queda ligado a requisitos.
5. No se insertan IDs en `docs/00-discovery/` (checkpoint cerrado). La correspondencia `Discovery #N → DEC-###` se registra en `SDD-STATUS.md` / `TRACEABILITY.md`.

## `docs/TRACEABILITY.md` (se crea en Concept Definition, no antes)

Una sola tabla, con una fila por REQ:

```markdown
| REQ | Resumen | DEC | TECH | SPEC | ARCH | TEST-UNIT | TEST-INT | VAL | Estado |
|-----|---------|-----|------|------|------|-----------|----------|-----|--------|
```

Las columnas se completan a medida que avanzan las fases. Una celda vacía en una fase que ya debería haberla completado es un hallazgo para `spec-reviewer`.
