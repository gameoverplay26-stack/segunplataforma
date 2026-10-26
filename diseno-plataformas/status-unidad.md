# Status de unidades — Diseño según Plataformas de Juego (U4–U7)

Archivo de control único. **Se actualiza al final de cada sesión de trabajo.**
Última actualización: **2026-10-26**.

## Reglas de trabajo vigentes

1. **Una unidad por vez.** Se termina una unidad completa antes de avanzar a la siguiente. Instrucción del usuario del 2026-10-05.
2. **Todo lo producido queda en el repo**, en `diseno-plataformas/unidad-NN/`, para no perder trabajo si se corta la sesión. El material común de U4–U7 va en `diseno-plataformas/transversal/`. Estructura del repo reorganizada el 2026-10-05: ver el `README.md` de la raíz.
3. **Las slides definitivas se escriben solo después de aprobar** la auditoría, la propuesta pedagógica y la arquitectura de cada unidad.
4. **No se inventan fuentes.** Lo no verificado se marca y no se usa en clase.
5. Unity **6000.3.11f1**; no se reemplaza la versión.

## Encargo original: 10 fases

F1 Auditoría · F2 Investigación · F3 Correcciones · F4 Objetivos · F5 Actividades · F6 Integrador · F7 Arquitectura de clases · F8 Arquitectura de slides · F9 Banco de recursos · F10 Recomendación final.

## Tablero

| Unidad | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 | F10 | Slides definitivas | Estado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **U4 Móvil** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (cap. 1) | ✅ | ✅ | ✅ | ✅ | ✅ versión final: archivo único de 63 slides (3 clases + anexo) | **Clase 1 dada hasta la slide 15; quedan 2 encuentros de 90 min (versión final 2026-10-13); falta la prueba en un teléfono** |
| U5 Consolas | 🟡 en `00` | ✅ preliminar + datos de mercado | ✅ (auditoría A1–A15 aplicada) | ✅ | ✅ A5.1–A5.6 | 🟡 TP 4 PROPUESTO | ✅ `03-arquitectura-unidad.md` (aprobada 2026-10-26) | ✅ | 🟡 | — | ✅ `Unidad-5-2026-completa-v2.pptx` (74 slides: 6 bloques, 150 min de exposición + anexos A y B) | **Unidad completa en slides (2026-10-26).** Bloque 1 sin dar. Pendiente: TP 4 y rúbrica (titular), demo en la Xbox de la docente |
| U6 PC | 🟡 en `00` | ✅ preliminar | — | — | — | — | — | — | 🟡 | — | — | Investigación guardada, sin procesar |
| U7 Emergentes | 🟡 en `00` | 🟡 preliminar* | — | — | — | — | — | — | 🟡 | — | — | Investigación guardada, sin procesar |
| Transversal | 🟡 bibliografía | ✅ académicas | — | — | — | ⏳ diseño completo | — | — | 🟡 | — | — | Pendiente |

✅ hecho · 🟡 parcial · ⏳ pendiente · — no iniciado
\* El agente de U7 se cortó por el límite de sesión mientras verificaba los últimos videos. El archivo tiene las secciones A–H, pero la sección C debe revisarse antes de usarla.

## Inventario de archivos

| Ruta | Contenido | Estado |
|---|---|---|
| `diseno-plataformas/unidad-04/README.md` | Índice, objetivo, relación entre unidades, recomendación F10, decisiones | ✅ |
| `diseno-plataformas/unidad-04/01-analisis-programa-y-objetivos.md` | F1, F3, F4 | ✅ |
| `diseno-plataformas/unidad-04/02-caso-practico-asteroides-movil.md` | Supuestos S1–S13 verificados en el código, defecto deliberado, hipótesis | ✅ |
| `diseno-plataformas/unidad-04/03-clase-guion-docente.md` | F7: arquitectura de 4 clases | ✅ (el "qué decir" de cada slide está en las notas del docente) |
| `diseno-plataformas/unidad-04/04-diapositivas-arquitectura.md` | F8: arquitectura aprobada | ✅ |
| `diseno-plataformas/unidad-04/04-diapositivas.md` + `Unidad-4-Clase-1..4-2026.pptx` + `scripts/build_decks.py` | Slides definitivas | ✅ |
| `diseno-plataformas/unidad-04/05-actividad-practica-y-evaluacion.md` | F5, F6: A4.1–A4.6, TP 3, rúbrica, parcial | ✅ |
| `diseno-plataformas/unidad-04/06-investigacion-recursos.md` | F2, F9: 61 fichas, videos, PDFs, datos, no verificados, tabla de fuentes | ✅ |
| `diseno-plataformas/unidad-05/00-investigacion-preliminar.md` | Auditoría (15 ítems), 52 fichas, 19 videos, certificación pública vs. NDA | Insumo crudo |
| `diseno-plataformas/unidad-05/01-desarrollo-tema-consolas.md` + `datos/` + `scripts/graficos_consolas.py` + `imagenes/` | Desarrollo del tema: categorías de consola, consolas actuales, historia, ranking, histograma, ciclo de vida, regiones, precios 2026, decisiones de diseño, errores frecuentes, uso en clase 40/60 | PROPUESTO |
| `diseno-plataformas/unidad-05/03-arquitectura-unidad.md` | Arquitectura de la unidad completa: 6 bloques (150 min de exposición), actividades A5.1–A5.6, TP 4 (PROPUESTO), anexos | APROBADA 2026-10-26 |
| `diseno-plataformas/unidad-05/04-diapositivas.md` + `Unidad-5-2026-completa-v2.pptx` | Slides de la unidad completa, v2 (74). La v1 (24) no se pisó | ✅ |
| `diseno-plataformas/unidad-05/06-guia-alumnos-de-pc-a-xbox.md` | Guía para alumnos: predecir, jugar sin mouse, comprobar en la demo de la docente en Xbox y leer la capa de consola. Procedimiento de la docente en `laboratorio-adaptacion/GUIA-XBOX-DOCENTE.md` | PROPUESTO |
| `diseno-plataformas/unidad-06/00-investigacion-preliminar.md` | Auditoría (16 ítems), 69 fichas, 14 videos, análisis de virtualización y contenedores | Insumo crudo |
| `diseno-plataformas/unidad-07/00-investigacion-preliminar.md` | Auditoría, 45 fichas, videos, tabla de tendencias | Insumo crudo (revisar sección C) |
| `diseno-plataformas/transversal/auditoria-bibliografia-y-fuentes-academicas.md` | Auditoría de los 10 libros del programa, libros reales, 21 papers, 12 videos | Insumo crudo |

## Novedad 2026-10-19: continuación de la U4

- El deck completo ya se dio. Se agregó la **Clase 4, "Del caso real al código"** (13 slides, 90 min, teoría 36 / práctica 54): publicidad (UX y seguridad), FTC vs. Epic como falla de input, antes/después de código real PC → Android (input y pantalla), orientación en Asteroides y el Platformer, **A4.9** y el **ítem 9 del TP 3** (PROPUESTO para la rúbrica).
- El anexo "Los plataformeros más vendidos" (armado a mano en el .pptx) pasó a la fuente `04-diapositivas.md`; las imágenes están en `unidad-04/imagenes/mercado/`. El generador suma `tarjetas:`, `subtabla:`, `codigo2:` y `movil:`, admite más de 4 secciones y versiona el archivo completo (`--version N`).
- Archivo vigente: `unidad-04/Unidad-4-2026-completa-v3.pptx` (87 slides). La v2 (74) y la versión sin sufijo quedan como estaban.
- Pendiente (titular): probar el APK y el instalador de PC del Platformer v2 antes de la clase; decidir el peso del ítem 9 en la rúbrica.

## Decisiones pendientes del usuario (U4)

| ID | Decisión | Opciones | Recomendación |
|---|---|---|---|
| D4-01 | Aprobar la auditoría y la arquitectura de U4 (`01`, `03`, `04`) | Aprobar / corregir | ✅ **APROBADA por el usuario el 2026-10-05** (versión corregida) |
| D4-02 | ¿Hay Mac disponible para iOS? | — | ✅ **RESUELTA: no hay Mac → iOS conceptual** |
| D4-03 | ¿Los alumnos tienen Android? | — | ✅ **RESUELTA: sí → build, Profiler y QA manual obligatorios (Clase 4 y TP 3)** |
| D4-04 | Cantidad de encuentros | — | ✅ **RESUELTA: 4 clases teórico-prácticas** (sin clase de taller; TP 3 avanzado en cada clase, defensa al final de la Clase 4) |
| D4-05 | Equivalencia de la rúbrica del TP 3 con la nota (7 para promocionar) | — | Que la defina la titular. ⏸ Atada al TP 3, en pausa (2026-10-25) |
| D4-06 | Corregir en el programa la tabla UT/TP corrida y la bibliografía no verificada | Corregir / dejar | Corregir: lo decide la titular. **Dato nuevo (2026-10-05):** el material previo `unidad-03/material-previo/TP Nº 3--.docx` se titula "TP Nº 3 – Pruebas unitarias con Unity". En ciclos anteriores, TP 3 = U3, como dice la tabla del programa; el cronograma 2025 dice TP 3 = U4. La numeración de TPs del ciclo 2026 queda por confirmar con la titular |

## Tareas técnicas pendientes (U4)

- [ ] Mover `com.unity.multiplayer.samples.coop/` (Boss Room) a `proyectos-unity/` cuando VS Code lo libere (cerrar VS Code o su servidor de C#).
- [ ] Volver a agregar en Unity Hub los proyectos desde `proyectos-unity/…`.

- [ ] Implementar en `proyectos-unity/Asteroides/asteroide-final/` la versión **con defecto** de la pausa y la solución (regla + adaptador + 2 tests), en una rama propia, validada en batch mode como en U3. Requisito de A4.4 y de la demo de la Clase 3.
- [x] Input System: se usa la **1.19.0**, la versión incluida en Unity 6000.3.11f1. Página de On-screen Controls 1.19 verificada el 2026-10-10 (https://docs.unity3d.com/Packages/com.unity.inputsystem@1.19/manual/OnScreen.html). La 1.20 queda para U5 si hace falta.
- [x] Probar el porteo de entrada de Asteroides en el Device Simulator y en un teléfono real (joystick, botón, dos dedos, 48 dp) antes de la Clase 4. ✅ **Hecho (informe del usuario, 2026-10-25): builds probadas en celulares reales.** Sin log ni capturas en el repo.
- [x] Build con **IL2CPP + ARM64**, instalarla en un teléfono y medir cuánto tarda la primera build (dato para la tarea de la Clase 2). Volver a correr `AndroidBuildConfigTests` y registrar el verde. ✅ **Hecho (informe del usuario, 2026-10-25): builds probadas en celulares reales.** Sin log ni capturas en el repo. Quedan sin registrar: el tiempo de la primera build y el verde de `AndroidBuildConfigTests`.
- [ ] Decidir (titular): la revisión de A4.7 pasa a tarea en la v4 de la Clase 3; y si se corrige Active Input Handling = Both en el proyecto (cambiar el `StandaloneInputModule` del prefab Game por `InputSystemUIInputModule`).
- [x] Decidir qué hacer con `proyectos-unity/Asteroides/asteroide-final/Assets/Settings/` (Build Profile de Android creado por la docente, sin versionar). ✅ Versionado en el commit `cd33c42` (2026-10-25).
- [x] **Cronograma:** resuelto el 2026-10-13: la unidad termina en dos encuentros de 90 min (versión final de las slides).
- [ ] Decidir (titular): defensa del TP 3 por video + coevaluación en el aula virtual (PROPUESTO); A4.4 pasa al dossier del TP 3. ⏸ **En pausa por decisión del usuario (2026-10-25).**
- [ ] Volver a verificar Zagal, Björk & Lewis 2013 (URL con certificado vencido) antes de citarlo.
- [ ] Definir los fragmentos (min:seg) de los videos C-02 a C-06. Ninguna duración está verificada.
- [x] URLs de Android environment setup (Unity 6000.3) y developer options (Android) verificadas el 2026-10-05 y cargadas en `03`.
- [ ] Armar el formulario de relevamiento de teléfonos del curso (modelo, Android, RAM, resolución) para la matriz de compatibilidad de la Clase 4.
- [x] Probar en un teléfono Android real la build de desarrollo de Asteroides + el Profiler conectado (ensayo del docente antes de la Clase 4), y preparar el APK del plan B. ✅ **Hecho (informe del usuario, 2026-10-25): builds probadas en celulares reales.** Sin log ni capturas en el repo. Profiler conectado: UNKNOWN.
- [x] Slides definitivas + notas del docente escritas (`04-diapositivas.md`) y 4 `.pptx` generados con `scripts/build_decks.py` (revisados visualmente con export a PNG, 2026-10-05).
- [ ] **Titular:** reemplazar los recuadros [IMAGEN SUGERIDA] por imágenes reales (hay 25 recuadros en total).

## Hallazgos transversales que hay que recordar (para U5–U7)

- **Bibliografía obligatoria del programa:** de 10 títulos, 1 se confirmó tal cual (Schell), 1 existe con otros datos (Kaner et al., *Testing Computer Software*, Wiley 1999) y 8 no aparecieron en los catálogos consultados. Hay reemplazos verificados en el archivo transversal.
- **Tabla UT/TP del programa corrida una unidad.** Se siguió el cronograma: TP 3 = U4, TP 4 = U5. U6 y U7 tienen actividades evaluativas en el aula virtual, sin TP.
- **U7 está comprimida en una sola semana** junto con parte de U6. Hay que priorizar contenidos al diseñarla.
- **U5:** los requisitos de Xbox (XR) y sus casos de prueba **son públicos**. Los de Sony (TRC) y Nintendo (Lotcheck) no lo son. El GDK está en GitHub desde 2021.
- **U6:** los AssetBundles no admiten código C# (mods con scripts no vienen "de fábrica"); macOS solo se virtualiza sobre hardware Apple; Dynamic Resolution en Windows requiere DX12.
- **Narrativa propuesta U4 → U7: "¿quién pone el límite?"**
  - U4: el dispositivo.
  - U5: el fabricante.
  - U6: la diversidad del hardware.
  - U7: el límite sale del dispositivo (cuerpo, entorno, red, navegador).

  **Integrador propuesto:** dossier de plataforma del mismo juego, con un capítulo por unidad. El diseño completo está pendiente.

## Próximo paso

1. El usuario da la aprobación final de U4 corregida y resuelve D4-05/D4-06.
2. Con U4 aprobada: slides definitivas de U4 + implementación del defecto de pausa.
3. Recién después: U5, procesando `diseno-plataformas/unidad-05/00-investigacion-preliminar.md` con el mismo formato que U4.

## Bitácora

| Fecha | Qué se hizo |
|---|---|
| 2026-10-04 | Lectura del programa 2025, de la clase del 28/09 y del código de Asteroides. Investigación verificada en paralelo (U4, U5, U6, U7 y bibliografía) |
| 2026-10-05 | Por límite de tokens, el usuario pide cerrar solo U4 y guardar todo. Se persistieron las investigaciones de U5–U7 y la bibliografía; se completaron las 10 fases de U4 a nivel de diseño; se creó este archivo |
| 2026-10-05 | Correcciones de U4 según el usuario: (1) 4 clases teórico-prácticas: la Clase 4 pasa a ser práctica en dispositivo Android (build, Profiler, QA manual de interrupciones, matriz de compatibilidad del curso, defensa del TP 3); (2) iOS conceptual en `01`, `03`, `04`, `05`; (3) build en Android **obligatoria** en el TP 3, con plan B; (4) playtest de papel con el propio teléfono en la Clase 2; (5) **error corregido en `02`**: se retiró la afirmación de que `maxLeft`/`maxRight` estaban "invertidos" (no demostrado) y se aclaró que el spawn usa coordenadas de mundo (verificado), con la cámara centrada como supuesto a confirmar; (6) slides: 46 → 53 |
| 2026-10-05 | El usuario **aprueba** la U4 corregida. Comienza el armado de las slides definitivas |
| 2026-10-05 | Slides definitivas: texto + notas en `04-diapositivas.md` (fuente única); generador data-driven `scripts/build_decks.py`; 4 decks (15/14/13/11). Verificadas por fetch las URLs de configuración de Android. Pendiente: imágenes, defecto de pausa en Asteroides, Input System 1.20, Zagal 2013, fragmentos de video |
| 2026-10-05 | Reorganización del repo (rama `catedra/reorganizacion`): materia en `diseno-plataformas/`, código en `proyectos-unity/`, streaming en `streaming/`, `docs/` solo SDD. Boss Room quedó en la raíz (bloqueado por VS Code), ignorado por git, pendiente de mover |
| 2026-10-05 | `catedra/reorganizacion` integrada a `main` (fast-forward) y subida a GitHub. U4 completa, U5–U7 preliminares y SDD (Concept) publicados en `origin/main` |
| 2026-10-05 | **Clase 1 v2** (`Unidad-4-Clase-1-2026-v2.pptx`, 20 slides): 5 slides nuevas a partir del artículo de Kevuru Games (fuente comercial, leída críticamente; Stadia y Origin verificados con fuentes oficiales). Regla nueva del usuario: **texto resumido en las slides y versión completa en las notas del docente**. El generador ahora acepta `--decks` y `--version`. Guion de la Clase 1 reprogramado |
| 2026-10-05 | Pedido de la titular: diagrama de las tres capas (dispositivo → intención → nave) en la slide 3 de la Clase 1 v2. Se agregó al generador la clave `diagrama:` (formas nativas y editables) y la opción `--out-dir`. El .pptx v2 debe regenerarse con PowerPoint cerrado: `python scripts/build_decks.py --decks 1 --version 2` |
| 2026-10-05 | Pedido de la titular: "histograma" en la slide 6 de la Clase 1 v2. Se implementó como **cronología de barras** (cada barra desde el hito de la época hasta 2026; teléfono destacado). Clave nueva `cronologia:` en el generador; paleta validada con dataviz (contexto #475569 vs. TEAL: CVD ΔE 15,6, normal 18,4, contraste ≥ 3:1). Fechas verificadas: App Store 10/07/2008, Oculus Rift 28/03/2016, GeForce Now 04/02/2020. .pptx v2 regenerado con los diagramas de las slides 3 y 6 |
| 2026-10-05 | Pedido de la titular: los ejemplos de arcade del artículo, "con gráficos". **Slide 7 nueva** de la Clase 1 v2, "Clásicos del arcade": línea de tiempo de 7 hitos (Pong → Mortal Kombat) en orden cronológico; el primer intento a escala proporcional producía cruces y se reemplazó por espaciado uniforme con leyenda. Clave nueva `hitos:` en el generador. Dato de la ESRB (1994, tras las audiencias de 1993) verificado. La Clase 1 v2 pasa a 21 slides y se corrieron la numeración y las referencias cruzadas de las notas y del guion |
| 2026-10-05 | Correcciones de la titular a la Clase 1 v2: (1) se quitaron todas las menciones a "Clase 2/3/4" (texto proyectado y notas), reemplazadas por "más adelante en la unidad"; (2) **glosario** de conceptos cortos al inicio de las notas de 20 slides (tile, GPU, CPU, SoC, overdraw, fps, throttling, etc.), sin cambiar el texto proyectado; (3) se quitaron los 9 recuadros de imagen vacíos; la sugerencia queda en las notas. Donde se podía diagramar sin inventar datos se agregaron gráficos nativos: slide 9 comparación teléfono/PC, slide 10 tiles y overdraw, slides 11 y 13 cadenas causales, slide 17 código real de Ship.cs 61–73 (leído del archivo), slide 18 pantallas a escala (16:9 vs. 9:16 con el rango de spawn). Para la slide 11 no se dibujó una curva de fps porque no hay datos medidos. Colores validados con dataviz |
| 2026-10-05 | **Clases 2, 3 y 4 v2** generadas con las reglas de la titular: viñetas breves; notas completas con glosario (35 slides); ninguna mención a clases futuras (verificado en los .pptx); 15 recuadros de imagen quitados (sugerencias en las notas) y gráficos nativos donde no hace falta inventar datos: densidad de pantalla, safe area (y plantilla de A4.3), orientación a escala con el rango de spawn, gestos, flujo SO → adaptador → regla → estado, y pasos de la build. Renderizador nuevo `safearea` y modificador `-` en `comparacion`. Las v1 se conservan |
| 2026-10-10 | **Decks v3 + porteo real de Asteroides.** La Clase 1 se dio hasta la slide 15. Por pedido del usuario se integra el porteo de forma gradual en las clases que faltan, con reparto 40 % teoría / 60 % práctica. Implementado en `proyectos-unity/Asteroides/asteroide-final`: Input System 1.19.0, Active Input Handling = Both, `ShipInputAdapter` (dispositivo → intención), `Ship.SetIntent`, controles en pantalla (`OnScreenStick`/`OnScreenButton`) y 3 tests nuevos. Tests en batchmode: línea base 7/11; después del porteo, 10–11/14 (3 hipótesis del pool en rojo constante + 1 inestable del mismo defecto; sin regresiones atribuibles). Slides: Clase 1 (slide 17 con el código original leído de git, `codigo: git:REV:…`), Clase 2 (+2 slides de demo, A4.7 nueva, A4.6 movida), Clase 3 (slide "Mismo patrón, dos adaptadores"), Clase 4 (A4.6, QA-06/07, transferencia al 2D Platformer, puente al gamepad). Registro: `laboratorio-adaptacion/PORTEO-ASTEROIDES.md`. Las v1 y v2 se conservan |
| 2026-10-12 | **Decks v4: build de Android con capturas reales.** Pedido del usuario a partir de su primera prueba de build (carteles "Unsupported Input Handling on Android" y "No Android devices connected"; Mono sin ARM64). Generador: claves `captura:`, `ajustes:` y `panel: ancho`; el código se ajusta al ancho. Clase 1 (tarea: comprobar que la PC ve el teléfono), Clase 2 (vistazo de la build, slide 18, y tarea del primer APK), Clase 3 (A4.8: test de Edit Mode de la configuración de Android, slides 15–16), Clase 4 (bloque de build en slides 3–8). En el proyecto: `Assets/Tests/EditMode/AndroidBuildConfigTests.cs` + `EditModeTests.asmdef` y `Assets/Editor/BuildAndroid.cs`. Evidencia: tests de configuración 2/4 (rojo esperado: Mono y sin ARM64); APK generado en batchmode en 42 s (Mono + ARMv7, 20 MB). Hallazgo: los Player Settings editados dentro del Build Profile quedan en `Assets/Settings/Build Profiles/Android™.asset`, no en ProjectSettings. **UNKNOWN:** build con IL2CPP + ARM64, instalación y juego en un teléfono real |
| 2026-10-13 | **Versión final de U4: dos encuentros de 90 min.** Decisión del usuario: después de la Clase 1 (dada hasta la slide 15) quedan dos encuentros de 90 min, con reparto 40/60. Se reorganizó todo el contenido restante: Clase 2 "Del supuesto de PC al pulgar" (slides 16–19 de la Clase 1, UI táctil condensada, Input System, A4.7 que une A4.3 y A4.7, playtest, vistazo de la build) y Clase 3 "Asteroides en tu bolsillo" (build con capturas reales, medición, A4.6, QA, matriz, testing, A4.8, monetización condensada, A4.5, TP 3, cierre). Fuera del encuentro: "Leer con lupa" (lectura), A4.4 (dossier del TP 3), defensa del TP 3 (video, PROPUESTO). Se omite la demo del test de pausa (versión con defecto no implementada). Los decks v1–v4 y las fuentes de la v4 pasan a `unidad-04/versiones-anteriores/`. El generador produce 3 decks sin sufijo |
| 2026-10-13 | **Archivo único + anexo Android.** Por pedido del usuario la unidad queda en un solo archivo, `unidad-04/Unidad-4-2026-completa.pptx` (63 slides): 3 clases + anexo de consulta "Android en Unity 6" (9 slides: Build Support y External Tools, teléfono y USB, Device Simulator, Build Profiles, Player Settings de identidad y de pantalla, build e instalación, diagnóstico). Pasos con capturas reales en las slides 18 (activar el simulador), 30 (Build Profiles y Switch Platform) y 31 (External Tools). Capturas nuevas de la docente en `imagenes/`. Hallazgos: Project Settings sigue en DefaultCompany (los valores nuevos están en el Build Profile); Render outside safe area y Auto Rotation con 4 orientaciones activos; posible Default Icon asignado por error (cuadro negro). Generador: viñetas `1. ` como pasos numerados, sección Anexo y salida única por defecto (`--por-clase` para decks separados). Decks por clase en `versiones-anteriores/final-por-clase/` |
| 2026-10-19 | **Videos en las slides (pedido del usuario).** Slide 48 (caso Epic/FTC): los 3 videos de Facebook que pasó el usuario (La Tercera, El Deber, El Sol de México) y DW Español; se agregó el caso de Países Bajos (ACM, 1.125.000 euros en 2024, confirmado por el tribunal de Róterdam el 14/01/2026, verificado en acm.nl) como viñeta y en notas. Slides de historia 6 y 7: videos de consulta en español (lucasmelor, Aranimations ES, Academia Play). Slide 62 del anexo: ejemplos de build de PC a Android en español (Jadsa Games con Unity 6, LuisCanary). Todos verificados por título, canal y fecha; **contenido no revisado completo (UNKNOWN)**. Facebook puede pedir sesión para reproducir. El generador ahora admite enlaces clicables `[etiqueta](url)` en `video:`. Nota: el pedido decía "página 58", pero los videos tratan la multa a Epic, que es la slide 48; la 58 (Device Simulator) no se tocó. Las slides 6–7 son de la Clase 1, ya dada: solo se agregó el recuadro de video, sin rehacerlas |
| 2026-10-24 | Pedido del usuario: desarrollar el tema de consolas con consolas, histogramas, datos históricos y actuales. `unidad-05/01-desarrollo-tema-consolas.md` con datos verificados (Nintendo IR al 30-jun-2026, SIE Business Data, PlayStation Blog, Xbox Wire, Steam Store) y 6 gráficos generados por script (paleta dataviz). Microsoft no publica unidades de Xbox: queda fuera de los gráficos. No se hicieron slides (regla 13) |
| 2026-10-24 | Pedido del usuario: slides del tema con el formato de la U4. Fuente `unidad-05/04-diapositivas.md`; generador `unidad-05/scripts/build_decks.py` (reutiliza el de la U4; destacado `consola:`, pie "Unidad V"). `Unidad-5-2026-completa.pptx`: Clase 1 "La consola tiene dueño" (20 slides, 90 min, teoría 36 / práctica 54) + anexo de datos (4). Gráficos para slides con `graficos_consolas.py --slides`. Revisadas exportando a PNG con PowerPoint; 24/24 notas empiezan con glosario |
| 2026-10-25 | **Informe del usuario:** las builds de la U4 se probaron en celulares reales; se marcan hechas las tareas de prueba en teléfono (sin evidencia archivada en el repo). El TP 3 queda en pausa, y con él la defensa por video y D4-05. El Build Profile de Android de Asteroides se versionó (`cd33c42`) |
| 2026-10-26 | **Estado de la U5 y demo en Xbox.** Estado relevado: teoría `01` PROPUESTA; slides solo de la Clase 1 (24); 2 actividades en clase; **TP 4 inexistente**; F3–F8 y F10 sin iniciar. Pedido del usuario: mostrar Asteroides y el Platformer en la Xbox Series X de la docente sin tienda ni nube → vía **Developer Mode + UWP** (DEC-LAB-008 resuelta). Versiones original y de consola, guía docente y guía de alumnos (`unidad-05/06-…`). Detalle: `laboratorio-adaptacion/PORTEO-XBOX.md` |
| 2026-10-26 | **U5 completa.** Arquitectura aprobada (`03-arquitectura-unidad.md`): un solo archivo, unos 150 min de exposición sin contar prácticos. `Unidad-5-2026-completa-v2.pptx` (74 slides): Bloque 1 (la Clase 1, sin dar; solo cambia el kicker), 2 certificación (XR públicos frente a NDA, casos 115-02 y 112-08, clasificación), 3 mando y TV (acciones, remapeo, mandos adaptados, XAG 101/112, zona segura), 4 demo en Xbox en Developer Mode (con el código real de la capa de consola), 5 multijugador y rendimiento (BG3 en Series S, Gambetta, Claypool, ciclo de profiling, técnicas de Unity 6.3), 6 cierre y TP 4 (PROPUESTO), anexo A de datos y anexo B de Developer Mode. Revisión visual con export a PNG; 74/74 notas con glosario; sin "Clase N" ni recuadros de imagen. El pie dice "Bloque N" |
