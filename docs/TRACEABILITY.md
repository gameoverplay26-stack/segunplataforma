# TRACEABILITY — Asteroid Survival

Matriz única de trazabilidad del proyecto SDD. La convención está en `.claude/skills/sdd-workflow/traceability.md`: una fila por REQ y columnas que se completan a medida que avanzan las fases.

- Creada el 2026-09-28, junto con los primeros `REQ-###` del GDD (`docs/02-gdd/GDD.md`). Ver INC-08 en `docs/SDD-STATUS.md`.
- **DEC:** decisiones de origen, que viven en `docs/SDD-STATUS.md`. **M#:** MUST HAVE del Concept Definition.
- **TECH / SPEC / ARCH / TEST-UNIT / TEST-INT / VAL:** vacías (`—`) hasta sus fases (Technical Specification, Architecture Specification, Test Strategy, Verification). Una celda vacía en una fase que ya debería haberla completado es un hallazgo para `spec-reviewer`.
- **Candidato:** nivel de verificación previsto en el GDD (`UNIT` / `INT` / `MANUAL` / `DOC` / `N/A`).

| REQ | Resumen | DEC | M# | Candidato | TECH | SPEC | ARCH | TEST-UNIT | TEST-INT | VAL | Estado |
|-----|---------|-----|----|-----------|------|------|------|-----------|----------|-----|--------|
| REQ-001 | Pantalla previa + acción explícita de inicio | DEC-015 | — | INT + MANUAL | — | — | — | — | — | — | GDD draft |
| REQ-002 | Cuenta regresiva de 3 s antes de la partida, sin gameplay | DEC-015, DEC-033, DEC-040, DEC-041 | — | UNIT + INT | — | — | — | — | — | — | GDD draft |
| REQ-003 | Estado inicial: vida 5, score 0, tiempo 0, orientación hacia arriba | DEC-032, DEC-035 | — | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-004 | Duración objetivo 3 min; aceptación [3, 5] min | DEC-008, DEC-016, DEC-034 | M10 | UNIT + DOC | — | — | — | — | — | — | GDD draft |
| REQ-005 | Final por supervivencia → Completado | DEC-011 | M10 | UNIT + INT | — | — | — | — | — | — | GDD draft |
| REQ-006 | Vida 0 → Game Over, sin respawn | DEC-009 | M11 | UNIT + INT | — | — | — | — | — | — | GDD draft |
| REQ-007 | Empate → Game Over | DEC-017 | M11 | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-008 | Sin gameplay después del final | — (CD §4) | M11 | UNIT + INT | — | — | — | — | — | — | GDD draft |
| REQ-009 | Resultado + score final comunicados; sin categorías | DEC-011, DEC-029 | M12 | INT + MANUAL | — | — | — | — | — | — | GDD draft |
| REQ-010 | El score no condiciona el resultado | DEC-011 | — | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-011 | Movimiento libre 2D según la intención | DEC-014 | M1, M2, M3 | UNIT + MANUAL | — | — | — | — | — | — | GDD draft |
| REQ-012 | Borde bloqueante para la nave | DEC-012 | M2 | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-013 | Orientación = última dirección intentada | DEC-010, DEC-019 | — | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-014 | Contacto → vida −1 | DEC-020, DEC-035 | M7 | UNIT + INT | — | — | — | — | — | — | GDD draft |
| REQ-015 | Un asteroide daña una sola vez; sigue su trayectoria | DEC-021, DEC-002 | M7 | UNIT + INT | — | — | — | — | — | — | GDD draft |
| REQ-016 | Disparo continuo con cadencia | DEC-022 | M4 | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-017 | Dirección del proyectil = orientación | DEC-010 | M4 | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-018 | Disparo disponible desde el inicio (hacia arriba) | DEC-018, DEC-032 | M4 | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-019 | Proyectil consumido al primer impacto | DEC-023 | M5 | UNIT + INT | — | — | — | — | — | — | GDD draft |
| REQ-020 | Proyectil eliminado al salir del área | DEC-012 | M5 | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-021 | Aparición fuera del área, entrando; un solo tipo | DEC-024, DEC-003 | M6 | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-022 | Trayectoria recta a velocidad constante | DEC-025 | M6 | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-023 | Un impacto destruye; sin fragmentación | DEC-026, DEC-003 | M7, M8 | UNIT + INT | — | — | — | — | — | — | GDD draft |
| REQ-024 | Aparición ≠ salida; eliminación al salir | DEC-024, DEC-012 | M6 | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-025 | Los asteroides no interactúan entre sí | DEC-030 | — | INT | — | — | — | — | — | — | GDD draft |
| REQ-026 | +10 por asteroide destruido, una sola vez | DEC-027, DEC-028, DEC-035 | M9 | UNIT + INT | — | — | — | — | — | — | GDD draft |
| REQ-027 | Salida y contacto no puntúan | DEC-027 | M9 | UNIT + INT | — | — | — | — | — | — | GDD draft |
| REQ-028 | HUD de score (SHOULD) | DEC-031 | — | MANUAL + INT | — | — | — | — | — | — | GDD draft |
| REQ-029 | HUD de tiempo (SHOULD) | DEC-031 | — | MANUAL | — | — | — | — | — | — | GDD draft |
| REQ-030 | HUD de vida (SHOULD) | DEC-031 | — | MANUAL + INT | — | — | — | — | — | — | GDD draft |
| REQ-031 | Reinicio directo a la cuenta regresiva (SHOULD) | DEC-031, DEC-040 | — | INT + MANUAL | — | — | — | — | — | — | GDD draft |
| REQ-032 | Dificultad progresiva (COULD) | DEC-031 | — | N/A (COULD no planificado) | — | — | — | — | — | — | GDD draft |
| REQ-033 | Feedback audiovisual (COULD) | DEC-031 | — | N/A (COULD no planificado) | — | — | — | — | — | — | GDD draft |
| REQ-034 | Mismo gameplay PC/Mobile; intenciones comunes | DEC-005 (DEFERRED), DEC-010, DEC-022 | M1 | INT + MANUAL | — | — | — | — | — | — | GDD draft |
| REQ-035 | Exclusiones del MVP (OUT OF SCOPE) | DEC-002, 003, 006, 009, 010, 011, 012, 013, 029 | — | DOC (N/A: ausencia de funcionalidad) | — | — | — | — | — | — | GDD draft |
| REQ-036 | La vida se limita a 0 (incluidos contactos simultáneos) | DEC-036, DEC-020, DEC-021 | M11 | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-037 | Proyectil recto a velocidad constante | DEC-037, DEC-010 | M5 | UNIT | — | — | — | — | — | — | GDD draft |
| REQ-038 | Los proyectiles no afectan a la nave | DEC-038 | M7 | UNIT + INT | — | — | — | — | — | — | GDD draft |
| REQ-039 | Al terminar, asteroides y proyectiles desaparecen | DEC-039, DEC-027 | M11, M12 | UNIT + INT | — | — | — | — | — | — | GDD draft |
