# Unidad 4 — Arquitectura de las clases (secuencia didáctica)

Fase cubierta: **7**. **Vigente: versión final del 2026-10-13 (ver abajo).** La arquitectura anterior de 4 clases de 120 min está en `versiones-anteriores/v4/03-clase-guion-docente-v4.md`. Define la **estructura** de cada clase: bloques, minutos, qué se hace en vivo y qué hacen los alumnos. El guion palabra por palabra se escribe junto con las slides definitivas.

**Revisión 2026-10-05** (decisiones del usuario, ver `diseno-plataformas/status-unidad.md`):
- **4 clases teórico-prácticas** de 120 min (D4-04). Se elimina la "clase de taller" de la versión anterior: el TP 3 se avanza dentro de cada clase y se defiende al final de la Clase 4.
- **No hay Mac** (D4-02): iOS se trata de forma **conceptual**, sin build ni Xcode.
- **Los alumnos tienen teléfono Android** (D4-03): la práctica en dispositivo real es **obligatoria** y ocupa la Clase 4 entera.

## Requisitos previos (antes de la Clase 1)

| Requisito | Quién | Fuente |
|---|---|---|
| Módulo **Android Build Support** (con OpenJDK y Android SDK & NDK) instalado en Unity 6000.3.11f1 desde Unity Hub, en las máquinas del aula y de los alumnos | Alumnos (tarea de aula virtual) + docente | [Unity Manual 6000.3: Android environment setup](https://docs.unity3d.com/6000.3/Documentation/Manual/android-sdksetup.html) (fetch OK 2026-10-05) |
| Teléfono Android con **Opciones de desarrollador** y **Depuración USB** activadas + cable USB de datos | Alumnos | [Android: Configure on-device developer options](https://developer.android.com/studio/debug/dev-options) (fetch OK 2026-10-05, actualizada 2026-10-01): tocar 7 veces "Número de compilación" y activar la depuración USB en Opciones de desarrollador (en Android 9 o superior: Ajustes > Sistema > Avanzado) |
| Android **7.1 (API 25) o superior**: mínimo soportado por Unity 6.3 | Alumnos (relevamiento) | B-27 |
| Relevamiento de los teléfonos del curso: modelo, versión de Android, RAM, resolución | Docente (formulario en el aula virtual) | Sirve para la matriz de compatibilidad de la Clase 4 |
| Versión **con defecto** del sistema de pausa en `proyectos-unity/Asteroides/asteroide-final/` | Docente | Tarea pendiente en el status |


## Versión final (2026-10-13): Clase 1 dada + dos encuentros de 90 min

Decisión del usuario: la unidad termina en **dos encuentros de 90 minutos** después de la Clase 1, que se dio hasta la slide 15. Todo el contenido que faltaba (slides 16–21 de la Clase 1 y las antiguas Clases 2, 3 y 4) se reorganizó en dos clases teórico-prácticas con reparto **40 / 60** (36 min de teoría y 54 de práctica por encuentro). Las versiones anteriores del guion y de las slides están en `versiones-anteriores/`.

Hilo: **"¿Qué se rompe de un juego cuando lo llevás al bolsillo de alguien?"**

| Clase | Pregunta | Restricción protagonista | Avance del TP 3 |
|---|---|---|---|
| 1 (dada, slides 1–15) | ¿Qué cambia en la máquina? | Energía, calor, memoria, SO, interrupciones | Secciones 1–2 |
| 2 (90 min) | ¿Qué supone el código y qué cambia en las manos? | Supuestos de PC, táctil, safe area, accesibilidad | Sección 3 (control y HUD) |
| 3 (90 min) | ¿Qué pasa en un teléfono de verdad y quién pone las reglas? | Dispositivo real, testing, tienda y monetización | Secciones 4–7 + entrega |

### Clase 2 — "Del supuesto de PC al pulgar" (90 min) · `Unidad-4-Clase-2-2026.pptx` (16 slides)

| Min | Bloque | Slides | Tipo |
|---|---|---|---|
| 0–3 | Apertura: dónde quedamos (A4.1) | 1–2 | Teoría 3 |
| 3–7 | Demo: el simulador y sus límites | 3 | Teoría 4 |
| 7–19 | **A4.2** Supuestos de PC (código original de `Ship.cs`) | 4 | Práctica 12 |
| 19–24 | Puesta en común: el spawn en vertical | 5 | Práctica 5 |
| 24–27 | ¿Cómo se elige una plataforma? | 6 | Teoría 3 |
| 27–41 | UI táctil: mínimos y densidad, safe area, pulgar y orientación, gestos y accesibilidad | 7–10 | Teoría 14 |
| 41–48 | Demos: una acción, tres dispositivos; la intención en código | 11–12 | Teoría 7 |
| 48–78 | **A4.7** Del boceto al control (une A4.3 y A4.7) | 13 | Práctica 30 |
| 78–85 | Playtest de papel con su teléfono | 14 | Práctica 7 |
| 85–88 | Vistazo de la build (captura real) | 15 | Teoría 3 |
| 88–90 | Cierre y tarea (Build Support, USB, primer APK; lectura "Leer con lupa") | 16 | Teoría 2 |

Reparto: teoría 36 min (40 %), práctica 54 min (60 %).

### Clase 3 — "Asteroides en tu bolsillo" (90 min) · `Unidad-4-Clase-3-2026.pptx` (23 slides)

| Min | Bloque | Slides | Tipo |
|---|---|---|---|
| 0–3 | Apertura: ¿qué no sabemos todavía? | 1–2 | Teoría 3 |
| 3–9 | Repaso de la build con capturas reales: así viene, así queda, carteles | 3–5 | Teoría 6 |
| 9–21 | **Build e instalación** en los teléfonos (plan B: APK de la docente) | 6 | Práctica 12 |
| 21–29 | Medición con el Profiler (5 min de partida) y editor vs. teléfono | 7–8 | Práctica 8 |
| 29–32 | **A4.6** oral | 9 | Práctica 3 |
| 32–42 | **QA manual**: interrupciones y controles (QA-01 a QA-07) | 10 | Práctica 10 |
| 42–46 | Matriz de compatibilidad del curso | 11 | Práctica 4 |
| 46–55 | Testing en móvil: escalera, límites, mismo patrón, test de configuración | 12–15 | Teoría 9 |
| 55–65 | **A4.8** El test que cuida la build | 16 | Práctica 10 |
| 65–78 | Monetización como diseño: FTC vs. Epic, modelos y formatos, reglas de tienda, game design y ética | 17–20 | Teoría 13 |
| 78–85 | **A4.5** ¿Cuál publicarían? (voto justificado) | 21 | Práctica 7 |
| 85–86 | TP 3: entrega y defensa | 22 | Teoría 1 |
| 86–90 | Cierre de unidad: transferencia al Platformer, gamepad y puente a U5 | 23 | Teoría 4 |

Reparto: teoría 36 min (40 %), práctica 54 min (60 %).

### Qué pasa fuera de los encuentros

| Qué | Dónde | Estado |
|---|---|---|
| Tarea técnica y primer APK (IL2CPP + ARM64) | Entre la Clase 2 y la 3 | Obligatoria |
| "Leer con lupa" (artículo de Kevuru Games) | Lectura en el aula virtual | — |
| A4.7 sin terminar | Captura en el aula virtual | — |
| A4.4 "La llamada que mata la nave" | Dossier del TP 3 | Antes era actividad de clase |
| Defensa del TP 3 | Video de 3 min + coevaluación en el aula virtual | **PROPUESTO**, lo decide la titular |
| Demo del test de pausa en rojo | Se omite (la versión con defecto no está implementada) | Pendiente en el status |

### Qué se demuestra en vivo y qué hacen los alumnos

| En vivo (docente) | Alumnos |
|---|---|
| Device Simulator y sus límites; Input System y controles en pantalla; vistazo de la build | A4.2 (supuestos), A4.7 (boceto + controles en Unity), playtest de papel |
| Repaso de la build con capturas reales | Build, instalación, medición, A4.6, QA manual, matriz, A4.8, A4.5 |
