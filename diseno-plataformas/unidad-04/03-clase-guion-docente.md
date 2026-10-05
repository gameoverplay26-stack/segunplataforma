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

## Clase 1 — "Un teléfono no es una PC chica" (120 min)

| Min | Bloque | Qué pasa |
|---|---|---|
| 0–10 | **Apertura (problema)** | Relato: "Asteroides anda perfecto en la PC del aula; en un teléfono, a los 10 minutos se traba, el teléfono quema y, al atender una llamada, la partida se pierde". ¿Cuántos problemas distintos hay? |
| 10–15 | Puente con el 28/09 | Slides 8 (móvil) y 12 (intención vs. dispositivo) |
| 15–40 | Teoría 1: la máquina | SoC y TBDR (solo la idea y por qué importa el overdraw); **sostenido vs. pico**; térmica y regla del ~65 %; 30 fps por defecto; batería; memoria y cierre de procesos; ciclo de vida e interrupciones; Android vs. iOS (iOS: solo conceptual, con la razón: Xcode exige macOS) |
| 40–55 | **A4.1** Diagnóstico de síntomas | Parejas |
| 55–60 | Puesta en común A4.1 | — |
| 60–70 | **Demo en vivo 1** | Player Settings de Android (Application Category = Game, orientación, versión mínima de API); Device Simulator y **qué no simula** |
| 70–95 | **A4.2** ¿Qué supuestos de PC tiene Asteroides? | Grupos con el código |
| 95–110 | Puesta en común A4.2 | Revelar S4/S5 en el Device Simulator con un perfil vertical |
| 110–120 | Cierre | Límites del simulador. Consigna del TP 3. Tarea: instalar Android Build Support y activar la depuración USB (necesario para la Clase 4) |

## Clase 2 — "Diseñar para el pulgar" (120 min)

| Min | Bloque | Qué pasa |
|---|---|---|
| 0–10 | **Apertura (problema)** | HUD de Asteroides en un teléfono con notch: score tapado, botón diminuto. "¿Cuánto mide un dedo?" |
| 10–35 | Teoría 2: UI táctil | 44 pt / 48 dp; pt, dp, px; safe area y cutouts; Canvas Scaler; oclusión y zona del pulgar (Hoober 2013, con advertencia); orientación y Android 16 en pantallas grandes |
| 35–50 | Teoría 3: gestos e interacción | Gestos estándar vs. custom; joystick virtual vs. toque directo; háptica opcional; accesibilidad; onboarding |
| 50–55 | **Demo en vivo 2** | Constant Pixel Size → Scale With Screen Size en el simulador; `Screen.safeArea` |
| 55–80 | **A4.3** Dos esquemas de control | Grupos: bocetos + tabla comparativa |
| 80–95 | Prueba con el pulgar real | Cada grupo imprime o dibuja su HUD a escala sobre la silueta de **su propio teléfono** y prueba alcance y oclusión con la mano. Es un playtest de papel: barato y con personas |
| 95–110 | **A4.6** "Anda bien los primeros 5 minutos" | Individual, formativa |
| 110–120 | Cierre | "Qué no resuelve un buen layout": la comodidad se prueba con personas. Verificar quién ya tiene la depuración USB funcionando |

## Clase 3 — "El negocio y la prueba" (120 min)

| Min | Bloque | Qué pasa |
|---|---|---|
| 0–10 | **Apertura (problema)** | FTC vs. Epic 2022: una UI de compra terminó en USD 520 millones. "¿Monetizar es diseñar?" |
| 10–35 | Teoría 4: monetización como diseño | Premium / freemium / ads / híbrido; AdMob, Apple 3.1.1, Google Play Billing, probabilidades; dark patterns, loot boxes (correlacional), Bélgica; efecto sobre dificultad, ritmo y progresión |
| 35–60 | **A4.5** Tres propuestas de monetización | Grupos + debate |
| 60–80 | Teoría 5: testing en móvil | Taxonomía de 6 niveles y el límite de cada uno; target API 36 y AAB; iOS: Simulator y Xcode como **concepto** (no disponible en la cátedra) |
| 80–90 | **Demo en vivo 3** | Test Runner, pestaña Player; test de pausa en **rojo** contra la versión con defecto |
| 90–115 | **A4.4** (parte 1) "La llamada que mata la nave" | Grupos: comportamiento esperado, separación regla / adaptador, test de Edit Mode |
| 115–120 | Cierre | Lo que el test **no** demuestra se prueba la próxima clase, en el teléfono |

## Clase 4 — "Asteroides en tu bolsillo" (120 min, práctica en dispositivo real)

| Min | Bloque | Qué pasa |
|---|---|---|
| 0–10 | **Apertura (problema)** | "Todo lo que probamos hasta ahora fue en el editor. ¿Qué no sabemos todavía?" Los grupos recuperan su columna "qué no demuestra" de A4.4 |
| 10–30 | **Build en el teléfono** | Development Build + Autoconnect Profiler → instalar en el teléfono de un integrante (el docente lo hace primero en vivo y los grupos lo repiten). Si un teléfono falla, se usa el de otro integrante |
| 30–50 | **Medición** | Profiler conectado: frame time, GC Alloc por disparo (H1, S9); partida de 10 minutos con registro de fps (H2). Se compara con la misma medición en el editor |
| 50–70 | **QA manual de interrupciones** | Sobre su build: llamada (o alarma), botón home, bloqueo de pantalla, teclado, cierre forzado desde las opciones de desarrollador. Registran resultado esperado vs. real (formato de caso de prueba de la U2) |
| 70–85 | **Matriz de compatibilidad del curso** | Se juntan los datos de todos los grupos (modelo, Android, RAM, resolución, fps medido, ¿se ven los asteroides en vertical?). Discusión: ¿alcanza este parque de teléfonos para decir "anda en Android"? |
| 85–110 | **Defensa del TP 3** | 3 min por grupo: una decisión de plataforma (PDR) y la evidencia del dispositivo. Coevaluación con la rúbrica simplificada |
| 110–120 | Cierre de unidad y puente a U5 | "En móvil el límite lo pone el **dispositivo**; en consola lo pone el **fabricante**". Entrega final del dossier por aula virtual |

**Plan B:** si la build falla en la mayoría de las máquinas (SDK, drivers USB), el docente instala su build en los teléfonos por APK, sin Profiler. La medición de rendimiento queda como tarea y el bloque de QA manual se mantiene igual.

---

## Qué se demuestra en vivo y qué hacen los alumnos

| En vivo (docente) | Alumnos |
|---|---|
| Player Settings de Android; Device Simulator y sus límites | Diagnóstico (A4.1, A4.6) e inventario de supuestos (A4.2) |
| Canvas Scaler y safe area | Diseño de controles + playtest de papel sobre su teléfono (A4.3) |
| Test de pausa en rojo (Test Runner) | Tests de Edit Mode y Play Mode de la pausa (A4.4) |
| Primera build en un teléfono + Profiler conectado | Build propia, medición, QA manual de interrupciones, matriz de compatibilidad (Clase 4) |
| — | Monetización: decisión y defensa (A4.5) |
