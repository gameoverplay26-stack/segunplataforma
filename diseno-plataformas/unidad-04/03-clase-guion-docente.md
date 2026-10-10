# Unidad 4 — Arquitectura de las clases (secuencia didáctica)

Fase cubierta: **7**. Define la **estructura** de cada clase: bloques, minutos, qué se hace en vivo y qué hacen los alumnos. El guion palabra por palabra se escribe junto con las slides definitivas.

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


## Hilo de la unidad

Pregunta de la unidad: **"¿Qué se rompe de un juego cuando lo llevás al bolsillo de alguien?"**

| Clase | Pregunta | Restricción protagonista | Avance del TP 3 |
|---|---|---|---|
| 1 | ¿Qué cambia en la máquina? | Energía, calor, memoria, SO, interrupciones | Secciones 1–2 (ficha, supuestos) |
| 2 | ¿Qué cambia en las manos y en la pantalla? | Táctil, safe area, aspect ratio, accesibilidad | Sección 3 (control y HUD) |
| 3 | ¿Qué cambia en el negocio y cómo se prueba? | Reglas de tienda, monetización, testing | Secciones 6–7 (monetización, estrategia de pruebas) |
| 4 | ¿Qué pasa en un teléfono de verdad? | Dispositivo real: build, Profiler, interrupciones, compatibilidad | Secciones 4–5 (interrupciones, rendimiento) + defensa |

Regla de la cátedra: **ninguna clase empieza por la herramienta**, siempre por un problema.

---

## Clase 1 — "Un teléfono no es una PC chica" (120 min) · versión 2

Deck: `Unidad-4-Clase-1-2026-v2.pptx` (21 slides). Agrega, respecto de la v1, el bloque "¿Qué es una plataforma?" (slides 5–8: capas, cronología de épocas, clásicos del arcade y tiendas móviles) y el bloque "Elegir y leer con lupa" (slides 19–20). Por pedido de la titular, la slide 3 tiene el diagrama de tres capas (dispositivo → intención → nave), la slide 6 una cronología de barras y la slide 7 la línea de tiempo de los clásicos del arcade, a partir del artículo de Kevuru Games leído con mirada crítica. Para hacerles lugar se recortaron 5 min de la Teoría 1 y 5 min de A4.2.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0–10 | **Apertura (problema)** | 1–2 | Relato: "Asteroides anda perfecto en la PC del aula; en un teléfono, a los 10 minutos se traba, el teléfono quema y, al atender una llamada, la partida se pierde". ¿Cuántos problemas distintos hay? |
| 10–15 | Puente con el 28/09 + objetivos | 3–4 | Slides 8 (móvil) y 12 (intención vs. dispositivo) del 28/09 |
| 15–25 | **Qué es una plataforma** (nuevo en v2) | 5–8 | Cuatro capas (ejecución, distribución, nube, comunidad) y definición de trabajo de la materia; de los arcades al bolsillo con la cronología de épocas y los clásicos del arcade (4 min en total, contexto); las tiendas móviles cambiaron quién publica, pero con reglas |
| 25–45 | Teoría 1: la máquina | 9–14 | SoC y TBDR; **sostenido vs. pico**; regla del ~65 %; 30 fps por defecto; memoria y cierre de procesos; ciclo de vida; Android vs. iOS (iOS conceptual: Xcode exige macOS) |
| 45–60 | **A4.1** Diagnóstico de síntomas + puesta en común | 15 | Parejas |
| 60–68 | **Demo en vivo 1** | 16 | Player Settings de Android; Device Simulator y **qué no simula** |
| 68–88 | **A4.2** ¿Qué supuestos de PC tiene Asteroides? | 17 | Grupos con el código (20 min) |
| 88–100 | Puesta en común A4.2 | 18 | Revelar S4/S5 en el Device Simulator con un perfil vertical |
| 100–110 | **Elegir y leer con lupa** (nuevo en v2) | 19–20 | Cinco criterios para elegir plataforma (cuatro del artículo + restricciones técnicas) aplicados a Asteroides; lectura crítica del artículo (Stadia cerrado, Origin reemplazada, cifras sin fuente) |
| 110–120 | Cierre | 21 | Límites del simulador. Consigna del TP 3. Tarea: instalar Android Build Support y activar la depuración USB (necesario para la Clase 4) |

## Resto de la Clase 1 (slides 16–21) · versión 3

La Clase 1 se cortó en la slide 15 (A4.1). Las slides 16–21 se dan al empezar el próximo encuentro (60 min), con el deck `Unidad-4-Clase-1-2026-v3.pptx`. El único cambio respecto de la v2: la slide 17 muestra el código **original** de `Ship.cs` (leído del commit `e766f8c`), porque el repositorio ya tiene el porteo de entrada; y las notas de la 18 cierran con el supuesto S1 (teclado) como problema abierto, sin mostrar la herramienta.

| Min | Bloque | Slides | Tipo |
|---|---|---|---|
| 0–8 | Demo: el simulador y sus límites | 16 | Teoría (demo) |
| 8–28 | **A4.2** Supuestos de PC (código original) | 17 | Práctica |
| 28–40 | Puesta en común A4.2 + S1 como problema abierto | 18 | Práctica |
| 40–45 | ¿Cómo se elige una plataforma? | 19 | Teoría |
| 45–50 | Leer con lupa | 20 | Práctica |
| 50–60 | Cierre, TP 3 y tarea técnica | 21 | Teoría |

Reparto: teoría 23 min (38 %), práctica 37 min (62 %).

> **Decisión pendiente (cronograma):** al sumar estos 60 minutos, el encuentro siguiente no alcanza para la Clase 2 completa. Opciones: (a) dar el resto de la Clase 1 + la primera hora de la Clase 2 y correr todo medio encuentro; (b) comprimir la teoría de la Clase 2. La decide la titular.

## Clase 2 — "Diseñar para el pulgar" (120 min) · versión 3

Cambios de la v3: demo ampliada con el porteo real (slides 13–14), actividad nueva **A4.7 "Del boceto al control"** en Unity (slide 16) y A4.6 movida a la práctica con el teléfono.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0–8 | **Apertura (problema)** | 1–2 | HUD de Asteroides en un teléfono con notch: score tapado, botón diminuto. "¿Cuánto mide un dedo?" |
| 8–28 | Teoría 2: UI táctil | 3–7 | 44 pt / 48 dp; pt, dp, px; safe area; Canvas Scaler; zona del pulgar; orientación |
| 28–38 | Teoría 3: gestos, accesibilidad y onboarding | 8–11 | Gestos estándar vs. custom; joystick virtual vs. toque directo; accesibilidad; primera sesión |
| 38–48 | **Demos en vivo 2** | 12–14 | Canvas Scaler y `Screen.safeArea`; "una acción, tres dispositivos": Input System 1.19, `ShipInputAdapter`, controles en pantalla en el Device Simulator |
| 48–68 | **A4.3** Dos esquemas de control | 15 | Grupos: bocetos + tabla comparativa |
| 68–98 | **A4.7** Del boceto al control | 16 | Grupos en Unity: implementan su esquema con Input System, lo prueban en el Device Simulator, miden 48 dp y listan lo que el simulador no prueba |
| 98–110 | Prueba con el pulgar real | 17 | Playtest de papel del HUD implementado, sobre la silueta de su teléfono |
| 110–120 | Cierre | 17 | La comodidad se prueba con personas. Verificar quién tiene la depuración USB funcionando |

Reparto: teoría 48 min (40 %), práctica 72 min (60 %).

## Clase 3 — "El negocio y la prueba" (120 min) · versión 3

Cambio de la v3: slide nueva 12, **"Mismo patrón, dos adaptadores"**, que conecta el porteo de la entrada con A4.4 y usa la evidencia real de los tests (10–11 de 14 en verde; 3 hipótesis en rojo por defectos reales del pool; 1 test inestable).

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0–8 | **Apertura (problema)** | 1–2 | FTC vs. Epic 2022. "¿Monetizar es diseñar?" |
| 8–26 | Teoría 4: monetización como diseño | 3–8 | Modelos, formatos, reglas de tienda, dark patterns |
| 26–48 | **A4.5** Tres propuestas de monetización | 9 | Grupos + debate |
| 48–62 | Teoría 5: testing en móvil + mismo patrón | 10–12 | Escalera de herramientas; la plataforma se mueve; adaptador de entrada y adaptador de pausa |
| 62–70 | **Demo en vivo 3** | 13 | Test de pausa en **rojo** contra la versión con defecto |
| 70–105 | **A4.4** (parte 1) "La llamada que mata la nave" | 14 | Grupos: comportamiento esperado, regla / adaptador, test de Edit Mode (ejemplo: `ShipIntentTests.cs`) |
| 105–115 | Revisión de A4.7 | — | Cada grupo muestra en el Device Simulator lo que le faltó de los controles y lo completa |
| 115–120 | Cierre | — | Lo que el test **no** demuestra se prueba en el teléfono |

Reparto: teoría 48 min (40 %), práctica 72 min (60 %).

## Clase 4 — "Asteroides en tu bolsillo" (120 min, práctica en dispositivo real) · versión 3

Cambios de la v3: la build **ya es jugable** en el teléfono gracias al porteo de entrada (sin él, solo se podía tocar "Start"); A4.6 se hace acá, con el Profiler; QA manual con dos casos de controles (QA-06 dos dedos, QA-07 48 dp y oclusión); transferencia al 2D Platformer y puente al gamepad.

| Min | Bloque | Slides | Qué pasa |
|---|---|---|---|
| 0–8 | **Apertura (problema)** | 1–2 | "¿Qué no sabemos todavía?" |
| 8–28 | **Build en el teléfono** | 3–4 | Development Build + Autoconnect Profiler; plan B con APK |
| 28–46 | **Medición** | 5–6 | Profiler conectado; partida de 10 minutos; editor vs. teléfono |
| 46–54 | **A4.6** "Anda bien los primeros 5 minutos" | 7 | Individual, formativa, contrastada con su medición |
| 54–74 | **QA manual** | 8–9 | QA-01 a QA-05 (interrupciones) + QA-06 y QA-07 (controles) |
| 74–84 | **Matriz de compatibilidad del curso** | 10 | ¿Alcanza para decir "anda en Android"? |
| 84–106 | **Defensa del TP 3** | 11 | 3 min por grupo, coevaluación |
| 106–114 | **Transferencia: el mismo porteo, otro juego** | 12 | 2D Platformer: ¿qué se reutiliza y qué no? |
| 114–120 | Cierre de unidad y puente a U5 | 13 | El límite lo pone el dispositivo; mismo input, otro control (gamepad); en consola, el fabricante |

**Plan B:** si la build falla en la mayoría de las máquinas (SDK, drivers USB), el docente instala su build en los teléfonos por APK, sin Profiler. La medición de rendimiento queda como tarea; el QA manual y A4.6 se mantienen.

---

## Qué se demuestra en vivo y qué hacen los alumnos

| En vivo (docente) | Alumnos |
|---|---|
| Player Settings de Android; Device Simulator y sus límites | Diagnóstico (A4.1, A4.6) e inventario de supuestos (A4.2) |
| Canvas Scaler y safe area; Input System y controles en pantalla (porteo real) | Diseño de controles (A4.3), implementación en Unity (A4.7) y playtest de papel sobre su teléfono |
| Test de pausa en rojo (Test Runner) | Tests de Edit Mode y Play Mode de la pausa (A4.4) |
| Primera build en un teléfono + Profiler conectado | Build propia, medición, QA manual de interrupciones, matriz de compatibilidad (Clase 4) |
| — | Monetización: decisión y defensa (A4.5) |
