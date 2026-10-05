# Unidad 4 — Diseño según Plataforma Móvil

**Materia:** Diseño según Plataformas de Juego
**Carrera:** Tecnicatura Universitaria en Diseño Integral de Videojuegos (Plan 2020)
**Docente:** Ing. Elsa Daniela Ramírez
**Ciclo lectivo:** 2026
**Motor:** Unity 6000.3.11f1 (Unity 6.3 LTS)
**Estado:** fase de **diseño** completa y **corregida el 2026-10-05** según las decisiones de la titular: 4 clases teórico-prácticas, iOS conceptual (no hay Mac), práctica obligatoria en el teléfono Android de los alumnos. Slides definitivas **generadas** (4 decks). Pendiente: imágenes (titular) e implementación del defecto de pausa. Control general en [`../status-unidad.md`](../status-unidad.md).

Caso guía: **nave + asteroides** (`proyectos-unity/Asteroides/asteroide-final/`), el mismo juego base de la clase del 28/09/2026. La justificación del cambio respecto de Cryptbound está en [`02`](./02-caso-practico-asteroides-movil.md).

---

## Objetivo de la unidad

Que el estudiante pueda **tomar y justificar decisiones de diseño, UX, monetización y testing al llevar un videojuego a dispositivos móviles**, entendiendo que energía, calor, memoria, pantalla táctil, interrupciones y reglas de tienda son restricciones de diseño y no solo de programación.

## Estructura documental

| Archivo | Fase del encargo | Contenido |
|---|---|---|
| [`01-analisis-programa-y-objetivos.md`](./01-analisis-programa-y-objetivos.md) | 1, 3, 4 | Cita del programa, cronograma, inconsistencias, auditoría de 17 ítems, qué no enseñar tal como está, qué falta, conservar / modificar / ampliar / incorporar, objetivos, conceptos imprescindibles / importantes / complementarios, alcance |
| [`02-caso-practico-asteroides-movil.md`](./02-caso-practico-asteroides-movil.md) | 5 (base) | Inventario de 13 supuestos de PC **verificados en el código real**, decisiones de diseño, defecto deliberado "la llamada que mata la nave", hipótesis de rendimiento, tabla de qué se automatiza y qué exige dispositivo |
| [`03-clase-guion-docente.md`](./03-clase-guion-docente.md) | 7 | Arquitectura de 4 clases teórico-prácticas de 120 min; la Clase 4 se hace en el teléfono Android de los alumnos; requisitos previos y plan B |
| [`04-diapositivas-arquitectura.md`](./04-diapositivas-arquitectura.md) | 8 | Arquitectura de 53 slides en 4 decks (**aprobada** el 2026-10-05) |
| [`04-diapositivas.md`](./04-diapositivas.md) | Slides definitivas | **Fuente única** del texto final + notas del docente de las 53 slides |
| `Unidad-4-Clase-1..4-2026.pptx` | Slides definitivas | 4 decks generados (15 + 14 + 13 + 11 slides), con notas del docente y recuadros [IMAGEN SUGERIDA] |
| [`scripts/build_decks.py`](./scripts/build_decks.py) | — | Generador: después de editar `04-diapositivas.md`, correr `python scripts/build_decks.py` desde `diseno-plataformas/unidad-04/` (requiere `python-pptx`) |
| [`05-actividad-practica-y-evaluacion.md`](./05-actividad-practica-y-evaluacion.md) | 5, 6 | Actividades A4.1–A4.6 con nivel N1–N5, TP N° 3 (capítulo 1 del integrador), rúbrica y preguntas de parcial |
| [`06-investigacion-recursos.md`](./06-investigacion-recursos.md) | 2, 9 | 61 fichas verificadas, 12 videos, 6 PDFs, 41 datos citables, fuera de alcance, no verificados y tabla final de fuentes |

## Relación con otras unidades

```
Unidad III — Pruebas unitarias / integración (Asteroides: TestSuite + INT-AST-13/14/15)
    ↓ el criterio "qué se automatiza" se aplica a riesgos de plataforma
Clase 28/09 — Panorama de plataformas (Asteroides como juego base)
    ↓ se profundiza móvil
Unidad IV — Móvil  ← esta unidad   (el límite lo pone el DISPOSITIVO: energía, calor, SO)
    ↓ capítulo 1 del dossier de plataforma
Unidad V — Consolas                 (el límite lo pone el FABRICANTE: certificación, mando, TV)
Unidad VI — PC                      (el límite es la DIVERSIDAD: escalabilidad, periféricos)
Unidad VII — Emergentes             (el límite sale del dispositivo: cuerpo, entorno, red, navegador)
```

---

## Recomendación docente final (Fase 10, Unidad 4)

1. **Conceptos realmente imprescindibles:**
   - rendimiento sostenido y térmica;
   - ciclo de vida e interrupciones;
   - UI táctil con mínimos (44 pt / 48 dp, safe area, escalado);
   - separar intención de dispositivo;
   - monetización como diseño con reglas y ética;
   - qué prueba cada herramienta y qué no.
2. **Qué eliminaría o reduciría:** reducir hardware a "SoC + TBDR + calor", sin arquitectura de CPU/GPU. Monetización sin SDKs. Granjas de dispositivos y Android vitals solo como mención.
3. **Qué agregaría un docente experto:**
   - interrupciones del SO;
   - rendimiento sostenido;
   - safe area y densidad;
   - modelo premium;
   - ética y regulación (FTC vs. Epic);
   - reglas de tienda que cambian cada año;
   - límites explícitos de cada herramienta.
4. **Actividades de mayor valor pedagógico:**
   - **A4.4**, la del defecto deliberado: une U3 con U4 y enseña la frontera entre automatización y hardware real;
   - **A4.2**, la del inventario de supuestos: lectura de código con mirada de plataforma;
   - **A4.5**, la de monetización: decisión con ética.
5. **Qué se reutiliza de Asteroides:** input acoplado (S1), límites y cámara/spawner (S3–S5), Canvas (S6), falta de pausa (S8), `Instantiate` por disparo (S9) y la suite de tests existente.
6. **Qué demostrar en vivo:** Device Simulator, en horizontal y en vertical, **con sus límites**; Canvas Scaler y safe area; Player Settings de Android; test de pausa en rojo; la primera build en un teléfono con el Profiler conectado (Clase 4).
7. **Qué queda como actividad de los alumnos:** diagnóstico (A4.1, A4.6), inventario (A4.2), diseño de controles (A4.3), tests (A4.4), monetización (A4.5) y dossier (TP 3).
8. **Qué evaluar:** que el alumno **decida y justifique** y que declare **qué no demuestra** cada prueba. No recordar especificaciones.
9. **Cómo conectar con U5–U7:** el dossier de plataforma del mismo juego, más la pregunta "¿quién pone el límite?". Ver el status general.
10. **Estrategia para las slides:** aprobar `03` y `04` → escribir el texto final con notas del docente → generar el `.pptx` con un script (patrón de U3) → la titular agrega las imágenes.

## Decisiones pedagógicas importantes

- **La herramienta aparece después del problema:** Device Simulator, Profiler y Test Runner aparecen siempre como respuesta a un problema ya planteado.
- **Los límites se enseñan con la misma fuerza que los beneficios:** cada herramienta lleva su "qué no prueba".
- **No se inventan datos:** todo lo no verificado está listado en `06` §G y no se usa en clase sin volver a verificarlo.
- **iOS conceptual, Android práctico** (decisiones del 2026-10-05): sin Mac no hay build de iOS. Los teléfonos Android de los alumnos son el laboratorio de la Clase 4 y su parque se usa como matriz de compatibilidad, discutiendo su representatividad.
