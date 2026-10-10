# Auditoría de adaptación multiplataforma y laboratorio UX de *Unravel*: índice documental

- **Fecha de la auditoría:** 2026-10-10
- **Fase:** 0, Descubrimiento y diagnóstico (solo lectura). Este paquete también incluye las **propuestas** de las fases 1 (móvil) y 2 (Xbox) y el diseño del laboratorio, sin implementar nada.
- **Estado de autorización:** DEC-LAB-001, 002, 003 y 006 están resueltas (ver `DECISIONS.md`). Las demás siguen pendientes.

## Proyectos auditados (rutas exactas)

| ID | Proyecto | Ruta absoluta |
|---|---|---|
| P1 | Asteroides | `C:\Developer\unity\2026\clases-en-vivo\proyectos-unity\Asteroides\asteroide-final` |
| P2 | 2D Platformer | `C:\Developer\unity\2026\clases-en-vivo\proyectos-unity\2D-Platformer-Unity-main` |

## Ubicación de este paquete

`C:\Developer\unity\2026\clases-en-vivo\diseno-plataformas\laboratorio-adaptacion\`, según lo resuelto en **DEC-LAB-001** el 2026-10-10. No se ubica en `docs/` porque esa carpeta pertenece al proyecto SDD "Arena", que tiene sus propias reglas de fase (ver `CLAUDE.md` del repositorio, §1–§2).

## Documentos

| Documento | Contenido | Tipo |
|---|---|---|
| `PROJECT-DISCOVERY.md` | Inventario técnico y de jugabilidad de P1 y P2, más la comparación | VERIFICADO + UNKNOWN |
| `MOBILE-ADAPTATION.md` | Propuesta de adaptación a Android, por juego | PROPUESTO |
| `XBOX-ADAPTATION.md` | Viabilidad y requisitos para Xbox | PROPUESTO / UNKNOWN / BLOCKED |
| `UNRAVEL-LAB-GUIDE.md` | Guía docente del laboratorio (planificación, grupos, protocolo) | PROPUESTO |
| `UNRAVEL-QUESTIONNAIRE.md` | Cuestionario del jugador, listo para imprimir | PROPUESTO |
| `UNRAVEL-OBSERVATION-SHEET.md` | Ficha de observación por grupo | PROPUESTO |
| `UNRAVEL-ASSESSMENT-RUBRIC.md` | Rúbrica de evaluación | PROPUESTO |
| `DECISIONS.md` | Decisiones pendientes (`DEC-LAB-###`) | Pendiente de aprobación |
| `EVIDENCE-LOG.md` | Evidencias (`EV-###`) y fuentes externas (`SRC-###`) | VERIFICADO |

## Convención de estados

`VERIFICADO`: respaldado por evidencia observable (archivo, configuración, log o fuente citada). · `PROPUESTO`: recomendación no implementada. · `UNKNOWN`: no se pudo determinar. · `BLOCKED`: no puede avanzar por una dependencia o decisión.

Los IDs usan el prefijo `DEC-LAB-` para no colisionar con los `DEC-###` del proyecto SDD "Arena".
