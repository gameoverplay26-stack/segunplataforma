# Unidad 4 — Arquitectura de las diapositivas (APROBADA 2026-10-05)

Fase cubierta: **8**. Por pedido explícito, esto **no** es el texto definitivo de las slides. Define cantidad, objetivo, bloques y secuencia. El contenido final y el `.pptx` (generador al estilo de `diseno-plataformas/unidad-03/scripts/`) se hacen **después de la aprobación**.

Marcas: **[RECICLADO 28/09]** = idea o imagen ya usada en `diseno-plataformas/clases/2026-09-28-integracion-y-plataformas/Clase2-Plataformas.pptx`. **[IMAGEN SUGERIDA: …]** = imagen que agrega la titular más adelante. No se generan imágenes.

## Resumen

| Ítem | Definición |
|---|---|
| Cantidad estimada | **53 diapositivas** en 4 decks: Clase 1 ≈ 15, Clase 2 ≈ 14, Clase 3 ≈ 13, Clase 4 ≈ 11 (revisión del 2026-10-05: 4 clases teórico-prácticas, Clase 4 en dispositivo Android real, iOS conceptual) |
| Objetivo | Que cada slide ayude a **tomar una decisión** de plataforma, no a memorizar una especificación |
| Bloques temáticos | 1. La máquina (energía, calor, memoria, SO) · 2. Manos y pantalla (táctil, safe area, accesibilidad) · 3. Negocio (monetización con reglas y ética) · 4. Prueba (qué prueba cada herramienta) · 5. Integración (TP 3) |
| Actividades | A4.1–A4.6 y TP 3 (ver [`05`](./05-actividad-practica-y-evaluacion.md)) |
| Ejemplos | Asteroides (S1–S13), Call of Duty: Mobile (HUD editable), Alto's Adventure (premium, un dedo), Vampire Survivors (monetización no intrusiva), Pokémon GO (ahorro de batería), FTC vs. Epic |
| Videos | WWDC19-422 (térmica), Zach Gage GDC 2012 (táctil), Dark Patterns GDC 2017, Unity Input System Mobile controls |
| Fuentes | Fichas B-01…B-61 de [`06`](./06-investigacion-recursos.md) |

---

## Deck Clase 1 — "Un teléfono no es una PC chica"

| N.º | Título | Objetivo pedagógico | Idea central | Contenido | Ejemplo | Actividad | Fuente | Imagen | Video |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Portada U4 | Ubicar | Unidad IV, Móvil | Título, materia, fecha | — | — | — | [IMAGEN SUGERIDA: teléfono en vertical con Asteroides corriendo] | — |
| 2 | El bug que no es un bug | Instalar el problema | Un juego que "anda" en PC falla de 3 formas en un teléfono | Relato: traba a los 10 min, calor, llamada | Asteroides | Pregunta: ¿cuántos problemas hay? | — | [IMAGEN SUGERIDA: tres íconos (termómetro, batería, llamada entrante) sobre la captura del juego] | — |
| 3 | Lo que ya vimos [RECICLADO 28/09] | Continuidad | Repaso de la slide 8 y de intención vs. dispositivo | 5 viñetas del 28/09 | — | — | Clase 28/09 | [IMAGEN SUGERIDA: miniatura de la slide 8 del 28/09] | — |
| 4 | Objetivos de la unidad | Orientar | Decidir y justificar | 5 objetivos (de `01` §F.2) | — | — | `01` | — | — |
| 5 | Adentro del teléfono | Comprender el SoC | CPU, GPU y memoria comparten chip, energía y calor | SoC, núcleos heterogéneos, memoria compartida | — | — | B-08, Arm §2.3 | [IMAGEN SUGERIDA: diagrama de bloques SoC vs. PC (CPU, GPU dedicada y RAM separadas)] | — |
| 6 | Por qué el overdraw cuesta más | Comprender TBDR (solo la idea) | Dibujar dos veces el mismo píxel gasta ancho de banda = batería | Tiles; transparencias; partículas | Explosión de Asteroides | — | B-14, Arm §2.3 | [IMAGEN SUGERIDA: pantalla dividida en tiles, con capas de partículas superpuestas en un tile] | — |
| 7 | Pico vs. sostenido | Concepto imprescindible | Lo que importa es el fps del minuto 10, no el del minuto 1 | Térmica → throttling → caída de fps; regla del ~65 % del presupuesto de frame | — | Pregunta: ¿cómo medirían "estable"? | e-book Unity p. 19; B-08 | [IMAGEN SUGERIDA: gráfico de fps vs. tiempo que cae a los 8 min, superpuesto a una curva de temperatura] | WWDC19-422 (19:40–31:00), de tarea |
| 8 | 30 fps no es un error | Decisión de diseño | Unity usa 30 fps por defecto en móvil para ahorrar batería | `targetFrameRate`, frame pacing, refresco | S12 | — | B-01, B-59 | [IMAGEN SUGERIDA: captura de la doc de targetFrameRate con la frase resaltada] | — |
| 9 | El sistema operativo manda | Ciclo de vida | El juego puede morir en background | Interrupciones; LMK / jetsam; `onTrimMemory` no previene (corrección) | — | — | B-11, B-13, B-38 | [IMAGEN SUGERIDA: diagrama de estados de la app (activa → background → terminada) con la llamada como disparador] | — |
| 10 | Qué hace Unity con eso | Conectar con el motor | `OnApplicationPause` / `OnApplicationFocus` | Callbacks; el teclado dispara Focus en Android | S8 | — | B-37 | — | — |
| 11 | Actividad A4.1 | Aplicar | Síntoma → restricción → prueba | 6 reportes de bug | — | **A4.1** (15 min) | `05` | — | — |
| 12 | Demo: el simulador y sus límites | Herramienta como consecuencia | Simula layout; **no** simula rendimiento, memoria ni render | Device Simulator en vivo | Asteroides en vertical | Demo en vivo | B-04 | [IMAGEN SUGERIDA: Device Simulator con Asteroides en vertical y los asteroides fuera de pantalla] | — |
| 13 | Actividad A4.2 | Analizar | ¿Qué supuestos de PC trae el juego? | Fragmentos de código | `Ship.cs`, `Spawner.cs` | **A4.2** (25 min) | `02` | [IMAGEN SUGERIDA: fragmento de Ship.cs 61–73 resaltado] | — |
| 14 | Lo que encontramos | Puesta en común | La cámara y el spawner, juntos, rompen el juego en vertical | S4 + S5 revelado | Asteroides | — | `02` §1 | [IMAGEN SUGERIDA: dos capturas lado a lado, 16:9 vs. 9:16, con el rango de spawn marcado] | — |
| 15 | Qué no resuelve esto + TP 3 | Límites + consigna | El simulador no mide calor ni batería | Límites; lanzamiento del TP 3 | — | Consigna del TP 3 | `05` | — | — |

## Deck Clase 2 — "Diseñar para el pulgar"

| N.º | Título | Objetivo | Idea central | Contenido | Ejemplo | Actividad | Fuente | Imagen | Video |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ¿Cuánto mide un dedo? | Problema | El HUD de PC no entra en la mano | Captura del HUD con notch | S6, S7 | Pregunta | — | [IMAGEN SUGERIDA: HUD de Asteroides en un teléfono con notch, score tapado] | — |
| 2 | 44 pt y 48 dp | Norma verificable | Hay mínimos oficiales | Apple 44×44 pt (28 mín.); Android 48×48 dp | — | — | B-15, B-16, B-21 | [IMAGEN SUGERIDA: un pulgar sobre una grilla de botones de 44 pt vs. 30 px] | — |
| 3 | pt, dp, px | Comprender la densidad | El mismo botón mide distinto en píxeles según la pantalla | Densidad; Canvas Scaler | S6 | — | B-32 | [IMAGEN SUGERIDA: el mismo botón en dos teléfonos de distinta densidad] | — |
| 4 | Safe area y cutouts | Concepto imprescindible | No todo el rectángulo es usable | `Screen.safeArea`; Android 15 edge-to-edge | — | — | B-02, B-23 | [IMAGEN SUGERIDA: teléfono con notch y la safe area sombreada] | — |
| 5 | Dónde llega el pulgar [RECICLADO 28/09] | Ergonomía | Los pulgares tapan la acción | Hoober 2013 (**con advertencia de antigüedad**) | CoD Mobile (HUD editable) | Pregunta: ¿qué zona tapa el pulgar en Asteroides? | B-56, dato E-38 | [IMAGEN SUGERIDA: HUD táctil con las zonas de pulgar superpuestas en semitransparente] | — |
| 6 | Orientación | Decisión | Vertical u horizontal cambia el juego (S4/S5) | AutoRotation; Android 16 y la excepción de juegos | Asteroides | — | B-24, B-25, B-34 | [IMAGEN SUGERIDA: el mismo nivel en vertical y en horizontal] | — |
| 7 | Gestos | Patrones | Un gesto custom nunca es la única vía | Tap, swipe, drag, hold, pinch; no pisar gestos del sistema | — | — | B-18 | [IMAGEN SUGERIDA: íconos de los 5 gestos estándar] | — |
| 8 | Sin botón físico | Táctil | Falta el feedback del botón | Joystick virtual vs. toque directo; háptica opcional | Alto's Adventure (un dedo) | — | B-20, B-22, dato E-39 | — | Zach Gage, GDC 2012 (C-04), fragmento a determinar |
| 9 | Accesibilidad móvil | Imprescindible | Accesible = más jugadores, no un extra | Controles grandes, remapeo, háptica desactivable, alternativas a gestos | — | — | B-58, B-16 | — | — |
| 10 | Primera sesión | Onboarding | Jugar apenas se instala | Enseñar jugando; descarga inicial corta | — | — | B-19, B-45 | — | — |
| 11 | Demo: escalar la UI | Herramienta como consecuencia | Constant Pixel Size → Scale With Screen Size | En vivo en el simulador | S6 | Demo en vivo | B-32 | — | Unity, "Input System Mobile controls" (C-01), opcional |
| 12 | Actividad A4.3 | Diseñar | Dos esquemas, una decisión | Plantilla de boceto + tabla | Asteroides | **A4.3** (25 min) | `05` | [IMAGEN SUGERIDA: plantilla de pantalla de teléfono vacía con la safe area marcada] | — |
| 13 | Playtest de papel con tu teléfono | Probar con personas | El HUD se prueba con la mano real, no en el editor | HUD a escala sobre la silueta del propio teléfono: alcance y oclusión | El teléfono de cada alumno | Prueba de 15 min | HIG Designing for games (B-19) | [IMAGEN SUGERIDA: una mano sosteniendo un teléfono con un HUD de papel superpuesto] | — |
| 14 | A4.6 + qué no resuelve un buen layout | Analizar + límites | La comodidad se prueba con personas | Caso "los primeros 5 min"; playtesting | — | **A4.6** | `05` | — | — |

## Deck Clase 3 — "El negocio y la prueba"

| N.º | Título | Objetivo | Idea central | Contenido | Ejemplo | Actividad | Fuente | Imagen | Video |
|---|---|---|---|---|---|---|---|---|---|
| 1 | USD 520 millones por un botón | Problema | La UI de compra tiene consecuencias legales | Caso FTC vs. Epic 2022 | Fortnite | Pregunta: ¿monetizar es diseñar? | B-54 | [IMAGEN SUGERIDA: titular del comunicado de la FTC] | — |
| 2 | Cuatro modelos | Comparar | Premium / freemium / ads / híbrido | Tabla: quién paga, cuándo, qué cambia en el diseño | Alto's Adventure (premium) | — | dato E-39 | [IMAGEN SUGERIDA: tabla visual de 4 columnas con íconos] | — |
| 3 | Tres formatos de anuncio | Distinguir | Rewarded ≠ interstitial ≠ banner | Opt-in; transiciones naturales; espacio de pantalla | — | — | B-49 | [IMAGEN SUGERIDA: tres mockups de pantalla, uno por formato] | — |
| 4 | Lo que AdMob prohíbe | Reglas externas | El momento del anuncio tiene reglas | Al abrir o salir; después de cada acción; uno tras otro | — | Pregunta rápida | B-49 | — | — |
| 5 | La tienda manda | Reglas externas | IAP obligatorio para contenido digital; probabilidades visibles | Apple 3.1.1; Google Play Billing | — | — | B-46, B-47 | — | — |
| 6 | Monetización = game design | Analizar | La monetización toca la dificultad, el ritmo y la progresión | "Continuar" con rewarded cambia el Game Over | Vampire Survivors ("nunca interrumpir") | — | dato E-41 | — | — |
| 7 | El lado oscuro | Ética | Dark patterns y loot boxes | Zagal et al. (pendiente de URL); Zendle & Cairns (**correlacional**); Petrovskaya & Zendle; Bélgica | — | — | B-51, B-52, B-55 | — | "Dark Patterns" GDC 2017 (C-06), fragmento a determinar |
| 8 | Actividad A4.5 | Evaluar | P1, P2, P3: ¿cuál publicarías? | Consigna y criterios | Asteroides | **A4.5** (25 min) | `05` | — | — |
| 9 | ¿Qué prueba cada herramienta? | Taxonomía | 6 niveles, cada uno con un límite | Simulador → emulador → dispositivo + profiler → Player tests → granjas → vitals | — | — | B-04, B-30, B-31, B-39–B-42, B-12 | [IMAGEN SUGERIDA: escalera de 6 peldaños con "qué prueba" / "qué no prueba" en cada uno] | — |
| 10 | La plataforma se mueve | Distribución | Target API 36, AAB; iOS requiere macOS (en la cátedra, iOS es **conceptual**) | Reglas que cambian cada año; por qué no compilamos para iOS | — | — | B-26, B-28, B-29 | — | — |
| 11 | Demo: el test de pausa en rojo | Herramienta como consecuencia | El test detecta el defecto… en el editor | Test Runner (Edit/Play Mode); la pestaña Player se usa en la Clase 4 | S8 | Demo en vivo | B-30 | — | — |
| 12 | Actividad A4.4 | Aplicar (U3 → U4) | La llamada que mata la nave | Comportamiento esperado; regla / adaptador | S8 | **A4.4** (inicio) | `02` §3 | [IMAGEN SUGERIDA: diagrama regla (C# puro) ← adaptador (MonoBehaviour) ← SO] | — |
| 13 | Qué se automatiza y qué no | Cierre | Tabla riesgo → prueba → ¿dispositivo? | `02` §5 | — | — | `02` | — | — |

## Deck Clase 4 — "Asteroides en tu bolsillo" (práctica en dispositivo Android)

| N.º | Título | Objetivo | Idea central | Contenido | Ejemplo | Actividad | Fuente | Imagen | Video |
|---|---|---|---|---|---|---|---|---|---|
| 1 | ¿Qué no sabemos todavía? | Problema | Todo lo anterior fue en el editor | Recuperar la columna "qué no demuestra" de A4.4 | S8 | Pregunta | `02` §5 | [IMAGEN SUGERIDA: editor de Unity vs. teléfono, con un signo de pregunta entre ambos] | — |
| 2 | De la PC al teléfono | Procedimiento | Development Build + depuración USB + Autoconnect Profiler | Pasos de la build (checklist) | — | Build en vivo | B-28, B-31 | [IMAGEN SUGERIDA: Build Profiles de Android con Development Build marcado] | — |
| 3 | Plan B | Gestión de riesgo | Si la build falla, APK del docente | Qué se pierde (Profiler) y qué no (QA manual) | — | — | — | — | — |
| 4 | Medir, no opinar | Rendimiento | Frame time y GC en el dispositivo | H1 (GC por disparo), H2 (10 min) | S9 | Medición (20 min) | B-31, e-book p. 11 | [IMAGEN SUGERIDA: Profiler conectado a un teléfono, con el pico de GC marcado] | — |
| 5 | Editor vs. teléfono | Comparar | El número del editor no predice el del teléfono | Tabla editor / teléfono que completan los grupos | — | — | B-04 | — | — |
| 6 | Interrumpir a propósito | QA manual | Llamada, home, bloqueo, teclado, cierre forzado | Formato de caso de prueba (U2): esperado vs. real | S8 | QA manual (20 min) | B-37, B-38 | [IMAGEN SUGERIDA: notificación de llamada entrante sobre el juego en pausa] | — |
| 7 | Lo que el test automático no vio | Límites | Comparar A4.4 (editor) con el QA manual | ¿Coinciden? ¿Qué apareció solo en el teléfono? | — | Discusión | — | — | — |
| 8 | Matriz de compatibilidad del curso | Compatibilidad | ¿Alcanzan nuestros teléfonos para decir "anda en Android"? | Modelo, versión, RAM, resolución, fps, ¿spawn visible en vertical? | Parque de teléfonos del curso | Puesta en común | B-12, e-book p. 20 | [IMAGEN SUGERIDA: tabla con los teléfonos del curso, con celdas verdes y rojas] | — |
| 9 | Defensa del TP 3 | Comunicar | Una decisión + la evidencia del dispositivo, en 3 min | Plantilla PDR | — | Defensa | `05` | — | — |
| 10 | Coevaluación | Evaluar pares | Rúbrica simplificada (3 criterios) | Decisión justificada / evidencia / límites declarados | — | Coevaluación | `05` | — | — |
| 11 | Puente a U5 | Narrativa | En móvil el límite lo pone el dispositivo; en consola, el fabricante | Pregunta transversal | — | — | — | [IMAGEN SUGERIDA: teléfono → gamepad frente a una TV] | — |

---

## Estrategia para convertir esto en slides definitivas

1. Aprobar o corregir esta arquitectura y la de `03`.
2. Escribir `04-diapositivas.md` definitivo: texto final + notas del docente por slide, con el mismo formato que `diseno-plataformas/unidad-03/04-diapositivas.md`.
3. Generar el `.pptx` con un script en `diseno-plataformas/unidad-04/scripts/` (reutilizando el patrón de `diseno-plataformas/unidad-03/scripts/build_deck.py`).
4. La titular agrega las imágenes en los lugares marcados.
