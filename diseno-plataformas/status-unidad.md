# Status de unidades — Diseño según Plataformas de Juego (U4–U7)

Archivo de control único. **Se actualiza al final de cada sesión de trabajo.**
Última actualización: **2026-10-05**.

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
| **U4 Móvil** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (cap. 1) | ✅ | ✅ | ✅ | ✅ | ✅ 4 decks (53 slides) | **Slides generadas; faltan imágenes y el defecto de pausa** |
| U5 Consolas | 🟡 en `00` | ✅ preliminar | — | — | — | — | — | — | 🟡 | — | — | Investigación guardada, sin procesar |
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
| `diseno-plataformas/unidad-06/00-investigacion-preliminar.md` | Auditoría (16 ítems), 69 fichas, 14 videos, análisis de virtualización y contenedores | Insumo crudo |
| `diseno-plataformas/unidad-07/00-investigacion-preliminar.md` | Auditoría, 45 fichas, videos, tabla de tendencias | Insumo crudo (revisar sección C) |
| `diseno-plataformas/transversal/auditoria-bibliografia-y-fuentes-academicas.md` | Auditoría de los 10 libros del programa, libros reales, 21 papers, 12 videos | Insumo crudo |

## Decisiones pendientes del usuario (U4)

| ID | Decisión | Opciones | Recomendación |
|---|---|---|---|
| D4-01 | Aprobar la auditoría y la arquitectura de U4 (`01`, `03`, `04`) | Aprobar / corregir | ✅ **APROBADA por el usuario el 2026-10-05** (versión corregida) |
| D4-02 | ¿Hay Mac disponible para iOS? | — | ✅ **RESUELTA: no hay Mac → iOS conceptual** |
| D4-03 | ¿Los alumnos tienen Android? | — | ✅ **RESUELTA: sí → build, Profiler y QA manual obligatorios (Clase 4 y TP 3)** |
| D4-04 | Cantidad de encuentros | — | ✅ **RESUELTA: 4 clases teórico-prácticas** (sin clase de taller; TP 3 avanzado en cada clase, defensa al final de la Clase 4) |
| D4-05 | Equivalencia de la rúbrica del TP 3 con la nota (7 para promocionar) | — | Que la defina la titular |
| D4-06 | Corregir en el programa la tabla UT/TP corrida y la bibliografía no verificada | Corregir / dejar | Corregir: lo decide la titular. **Dato nuevo (2026-10-05):** el material previo `unidad-03/material-previo/TP Nº 3--.docx` se titula "TP Nº 3 – Pruebas unitarias con Unity". En ciclos anteriores, TP 3 = U3, como dice la tabla del programa; el cronograma 2025 dice TP 3 = U4. La numeración de TPs del ciclo 2026 queda por confirmar con la titular |

## Tareas técnicas pendientes (U4)

- [ ] Mover `com.unity.multiplayer.samples.coop/` (Boss Room) a `proyectos-unity/` cuando VS Code lo libere (cerrar VS Code o su servidor de C#).
- [ ] Volver a agregar en Unity Hub los proyectos desde `proyectos-unity/…`.

- [ ] Implementar en `proyectos-unity/Asteroides/asteroide-final/` la versión **con defecto** de la pausa y la solución (regla + adaptador + 2 tests), en una rama propia, validada en batch mode como en U3. Requisito de A4.4 y de la demo de la Clase 3.
- [ ] Ubicar las páginas equivalentes de Input System **1.20** para Touch y On-Screen (las de 1.20 dieron 404; se citó la 1.17). Contradicción detectada: para U5, la página 1.20 de rebinding respondió HTTP 200, pero no se leyó el contenido.
- [ ] Volver a verificar Zagal, Björk & Lewis 2013 (URL con certificado vencido) antes de citarlo.
- [ ] Definir los fragmentos (min:seg) de los videos C-02 a C-06. Ninguna duración está verificada.
- [x] URLs de Android environment setup (Unity 6000.3) y developer options (Android) verificadas el 2026-10-05 y cargadas en `03`.
- [ ] Armar el formulario de relevamiento de teléfonos del curso (modelo, Android, RAM, resolución) para la matriz de compatibilidad de la Clase 4.
- [ ] Probar en un teléfono Android real la build de desarrollo de Asteroides + el Profiler conectado (ensayo del docente antes de la Clase 4), y preparar el APK del plan B.
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
