# TRACEABILITY — Asteroid Survival

Matriz única de trazabilidad del proyecto SDD. La convención está en `.claude/skills/sdd-workflow/traceability.md`: una fila por REQ y columnas que se completan a medida que avanzan las fases.

- Creada el 2026-09-28, junto con los primeros `REQ-###` del GDD (`docs/02-gdd/GDD.md`). Ver INC-08 en `docs/SDD-STATUS.md`.
- **DEC:** decisiones de origen, que viven en `docs/SDD-STATUS.md`. **M#:** MUST HAVE del Concept Definition.
- **TECH / SPEC / ARCH / TEST-UNIT / TEST-INT / VAL:** vacías (`—`) hasta sus fases (Technical Specification, Architecture Specification, Test Strategy, Verification). Una celda vacía en una fase que ya debería haberla completado es un hallazgo para `spec-reviewer`.
- **Candidato:** nivel de verificación previsto en el GDD (`UNIT` / `INT` / `MANUAL` / `DOC` / `N/A`).

| REQ | Resumen | DEC | M# | Candidato | TECH | SPEC | ARCH | TEST-UNIT | TEST-INT | VAL | Estado |
|-----|---------|-----|----|-----------|------|------|------|-----------|----------|-----|--------|
| REQ-001 | Pantalla previa + acción explícita de inicio | DEC-015 | — | INT + MANUAL | — | — | — | — | — | — | GDD aprobado |
| REQ-002 | Cuenta regresiva de 3 s antes de la partida, sin gameplay | DEC-015, DEC-033, DEC-040, DEC-041 | — | UNIT + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-003 | Estado inicial: vida 5, score 0, tiempo 0, orientación hacia arriba | DEC-032, DEC-035 | — | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-004 | Duración objetivo 3 min; aceptación [3, 5] min | DEC-008, DEC-016, DEC-034 | M10 | UNIT + DOC | — | — | — | — | — | — | GDD aprobado |
| REQ-005 | Final por supervivencia → Completado | DEC-011 | M10 | UNIT + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-006 | Vida 0 → Game Over, sin respawn | DEC-009 | M11 | UNIT + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-007 | Empate → Game Over | DEC-017 | M11 | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-008 | Sin gameplay después del final | — (CD §4) | M11 | UNIT + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-009 | Resultado + score final comunicados; sin categorías | DEC-011, DEC-029 | M12 | INT + MANUAL | — | — | — | — | — | — | GDD aprobado |
| REQ-010 | El score no condiciona el resultado | DEC-011 | — | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-011 | Movimiento libre 2D según la intención | DEC-014 | M1, M2, M3 | UNIT + MANUAL | — | — | — | — | — | — | GDD aprobado |
| REQ-012 | Borde bloqueante para la nave | DEC-012 | M2 | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-013 | Orientación = última dirección intentada | DEC-010, DEC-019 | — | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-014 | Contacto → vida −1 | DEC-020, DEC-035 | M7 | UNIT + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-015 | Un asteroide daña una sola vez; sigue su trayectoria | DEC-021, DEC-002 | M7 | UNIT + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-016 | Disparo continuo con cadencia | DEC-022 | M4 | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-017 | Dirección del proyectil = orientación | DEC-010 | M4 | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-018 | Disparo disponible desde el inicio (hacia arriba) | DEC-018, DEC-032 | M4 | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-019 | Proyectil consumido al primer impacto | DEC-023 | M5 | UNIT + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-020 | Proyectil eliminado al salir del área | DEC-012 | M5 | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-021 | Aparición por el borde superior, cayendo en vertical; un solo tipo | DEC-024, DEC-042, DEC-045, DEC-003 | M6 | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-022 | Caída vertical recta a velocidad constante | DEC-025, DEC-045 | M6 | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-023 | Un impacto destruye; sin fragmentación | DEC-026, DEC-003 | M7, M8 | UNIT + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-024 | Aparición ≠ salida; eliminación al salir | DEC-024, DEC-042, DEC-012 | M6 | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-025 | Los asteroides no interactúan entre sí | DEC-030 | — | INT | — | — | — | — | — | — | GDD aprobado |
| REQ-026 | +10 por asteroide destruido, una sola vez | DEC-027, DEC-028, DEC-035 | M9 | UNIT + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-027 | Salida y contacto no puntúan | DEC-027 | M9 | UNIT + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-028 | HUD de score (SHOULD) | DEC-031 | — | MANUAL + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-029 | HUD de tiempo (SHOULD) | DEC-031 | — | MANUAL | — | — | — | — | — | — | GDD aprobado |
| REQ-030 | HUD de vida (SHOULD) | DEC-031 | — | MANUAL + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-031 | Reinicio directo a la cuenta regresiva (SHOULD) | DEC-031, DEC-040 | — | INT + MANUAL | — | — | — | — | — | — | GDD aprobado |
| REQ-032 | Dificultad progresiva (COULD) | DEC-031 | — | N/A (COULD no planificado) | — | — | — | — | — | — | GDD aprobado |
| REQ-033 | Feedback audiovisual (COULD) | DEC-031 | — | N/A (COULD no planificado) | — | — | — | — | — | — | GDD aprobado |
| REQ-034 | Mismo gameplay PC/Mobile; intenciones comunes | DEC-005 (DEFERRED), DEC-010, DEC-022 | M1 | INT + MANUAL | — | — | — | — | — | — | GDD aprobado |
| REQ-035 | Exclusiones del MVP (OUT OF SCOPE) | DEC-002, 003, 006, 009, 010, 011, 012, 013, 029, 043 | — | DOC (N/A: ausencia de funcionalidad) | — | — | — | — | — | — | GDD aprobado |
| REQ-036 | La vida se limita a 0 (incluidos contactos simultáneos) | DEC-036, DEC-020, DEC-021 | M11 | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-037 | Proyectil recto a velocidad constante | DEC-037, DEC-010 | M5 | UNIT | — | — | — | — | — | — | GDD aprobado |
| REQ-038 | Los proyectiles no afectan a la nave | DEC-038 | M7 | UNIT + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-039 | Al terminar, asteroides y proyectiles desaparecen | DEC-039, DEC-027 | M11, M12 | UNIT + INT | — | — | — | — | — | — | GDD aprobado |
| REQ-040 | Un solo asteroide a la vez | DEC-044, DEC-042 | M6 | UNIT + INT | — | — | — | — | — | — | GDD aprobado |
