# CONTINUAR: traspaso entre sesiones y máquinas

Punto de entrada para retomar el trabajo **desde cualquier computadora**. La memoria de Claude Code y el historial de la conversación son locales de cada máquina y **no** viajan con git. Este archivo concentra lo que hace falta para seguir: dónde está el estado, qué reglas pidió el usuario, qué herramientas instalar y qué falta hacer.

**Uso:** en la otra máquina, clonar el repo, abrir Claude Code en la raíz y escribir **"continuá"**. Claude lee este archivo (lo indica `CLAUDE.md`) y el archivo de estado del frente que corresponda.

- **Última actualización:** 2026-10-26
- **Al cerrar cada sesión:** actualizar la sección 4 ("Dónde quedamos") y el archivo de estado del frente trabajado, y luego commit + push. Si no se pushea, la otra máquina no ve el trabajo.

---

## 1. Frentes de trabajo y su archivo de estado

| Frente | Carpeta | Archivo de estado (leer primero) | Reglas |
|---|---|---|---|
| Cátedra "Diseño según Plataformas de Juego" (UNJu, U4–U7) | `diseno-plataformas/` | `diseno-plataformas/status-unidad.md` | Sección 2 de este archivo |
| Laboratorio de adaptación / porteo (Asteroides y 2D Platformer → Android y Xbox; laboratorio UX de *Unravel*) | `diseno-plataformas/laboratorio-adaptacion/` | `DECISIONS.md` y `PORTEO-ASTEROIDES.md` de esa carpeta | Sección 2 de este archivo |
| Proyecto SDD "Arena" (Asteroid Survival) | `docs/` | `docs/SDD-STATUS.md` | `CLAUDE.md` §2–§10 y skill `sdd-workflow` |
| Proyectos Unity | `proyectos-unity/` | El registro del frente que los usa | Sección 3 |

Los IDs de decisión no se mezclan: `D4-xx` (cátedra, en `status-unidad.md`), `DEC-LAB-###` (laboratorio), `DEC-###` (SDD Arena).

---

## 2. Reglas de trabajo del usuario (antes guardadas solo en la memoria local de Claude)

**Pedagogía (cátedra)**
1. **Nunca empezar por la herramienta.** Cada clase abre con un problema real; la herramienta llega como consecuencia.
2. **Enseñar los límites:** cada tema incluye "qué NO resuelve esto" y los errores conceptuales frecuentes con su corrección.
3. **Continuidad estricta:** mismo caso guía (en U4–U7 es **Asteroides**), mismo formato de archivos por unidad. Antes de diseñar algo nuevo, leer la unidad anterior completa.
4. **No inventar recursos:** toda URL se verifica con fetch real; lo que no se pudo verificar se declara como tal.
5. **Reparto de cada clase: 40 % teoría / 60 % práctica.** La apertura, la teoría y las demos del docente cuentan como teoría. Mostrar el reparto en minutos.
6. **Contenido nuevo:** se integra de forma gradual y explicativa en las clases que **faltan dar**; no se rehacen las que ya se dieron.
7. **Una unidad por vez:** se termina una antes de pasar a la siguiente; todo se guarda en el repo y se controla en `status-unidad.md`.

**Diapositivas**
8. Viñetas breves en la slide (3–6 palabras, máximo 4–5 por slide); el desarrollo completo va en las **notas del docente**.
9. Cada slide empieza sus notas con un **glosario** de una línea por término técnico.
10. **No nombrar clases futuras** ("Clase 3") ni en la slide ni en las notas: usar "más adelante en la unidad".
11. Sin recuadros de imagen vacíos: la sugerencia va en las notas, o se reemplaza por un diagrama nativo con datos verificados.
12. **Versiones nuevas sin pisar las anteriores:** `-v2`, `-v3`… La fuente única es `unidad-NN/04-diapositivas.md` y el generador `unidad-NN/scripts/build_decks.py`.
13. Las slides definitivas se escriben **solo** después de que el usuario apruebe la auditoría y la arquitectura de la unidad.

**Rigor y decisiones**
14. Claude analiza, propone y verifica; **las decisiones las toma el usuario** y se registran con ID. No se resuelven por inferencia.
15. Estados permitidos: `VERIFICADO` / `PROPUESTO` / `UNKNOWN` / `BLOCKED`. Nunca decir "funciona" o "pasa" sin evidencia: XML del Test Runner, log de Unity en batchmode o salida de comando.
16. Las fuentes comerciales o blogs sirven para conceptos; los datos se verifican con fuentes oficiales.

**Git**
17. Commit, push, tag y cambios de rama **solo** cuando el usuario lo pide. Hoy se trabaja en `main`, por pedido del usuario.
18. Antes de commitear, revisar `git status`: hay archivos que **no** se suben sin preguntar (sección 5).

**Builds (pedido del 2026-10-19)**
19. Cada vez que se generan builds de un proyecto Unity porteado, se generan **las dos**: APK de Android **y** instalador de PC (Setup.exe con Inno Setup 6). En el Platformer v2: `Tools\generar_builds.ps1`, con Unity cerrado.
20. Los proyectos Unity se abren y compilan desde una **ruta corta**. En la máquina con el repo en `Documents\2026\...` hay un junction: `C:\Developer\unity\Platformer-v2` → `proyectos-unity\2D-Platformer-Unity-v2`. Abrirlo en Unity Hub desde esa ruta. Desde la ruta larga, la importación falla (ENV-01).
21. Responder siempre en español.

---

## 3. Herramientas que debe tener la otra máquina

| Herramienta | Versión / detalle | Para qué |
|---|---|---|
| Git + acceso a `https://github.com/gameoverplay26-stack/segunplataforma.git` | — | Sincronizar |
| **Ruta del clon recomendada:** `C:\Developer\unity\2026\clases-en-vivo` | — | Los documentos de auditoría citan rutas absolutas con esa base |
| Unity Hub + **Unity 6000.3.11f1** | Módulos: **Android Build Support** (OpenJDK, SDK, NDK) y Windows Build Support | Abrir los proyectos, correr tests y builds. **No cambiar de versión de Unity** |
| Inno Setup 6 (`winget install JRSoftware.InnoSetup`, por usuario) | — | Instalador de PC de los proyectos porteados |
| Python 3 (probado con 3.12) + `pip install python-pptx==1.0.2 matplotlib` | — | Generar los `.pptx` y los gráficos de la U5 |
| Visual Studio 2022 + carga de trabajo UWP + herramientas C++ de UWP + Windows SDK 10.0.19041 o posterior | Instalados el 2026-10-26 en la máquina de la cátedra. **En otra PC:** `powershell -ExecutionPolicy Bypass -File proyectos-unity\Tools-Xbox\verificar_requisitos_xbox.ps1` (tabla OK/FALTA; `-Instalar` agrega lo de Visual Studio). Guía: sección "0 bis" de `GUIA-XBOX-DOCENTE.md` | Paquetes UWP para la demo en Xbox (`Tools-Xbox/generar_builds_xbox.ps1`) |
| Rutas largas de Windows (`LongPathsEnabled = 1`) | Activadas en la máquina de la cátedra: hay rutas de 280 caracteres dentro de `Library`. Sin esto aparece ENV-01 aunque el repo esté en una ruta corta | Abrir y compilar los proyectos Unity |
| Microsoft PowerPoint (opcional) | — | Exportar slides a PNG para revisarlas (COM desde PowerShell) |
| Claude Code | — | Los agents y skills del repo (`.claude/agents`, `.claude/skills`) y `.claude/settings.json` viajan con git; `.claude/settings.local.json` es personal y no viaja |

**Primera apertura de un proyecto Unity en la máquina nueva:** `Library/` no se versiona, así que la primera importación tarda. Input System 1.19.0 viene incluido en el editor 6000.3.11f1 y no requiere descarga aparte.

**Comandos frecuentes** (con Unity **cerrado** para ese proyecto):

```bash
# Tests de Asteroides (Play Mode) con evidencia
"C:/Program Files/Unity/Hub/Editor/6000.3.11f1/Editor/Unity.exe" -batchmode -nographics \
  -projectPath "C:/Developer/unity/2026/clases-en-vivo/proyectos-unity/Asteroides/asteroide-final" \
  -runTests -testPlatform PlayMode \
  -testResults "<ruta>/resultado.xml" -logFile "<ruta>/resultado.log"

# Setup reproducible de los controles en pantalla (idempotente)
... -executeMethod PorteoSetup.Apply -quit -logFile "<ruta>/setup.log"

# Decks de la Unidad 4 (desde diseno-plataformas/unidad-04/)
python scripts/build_decks.py                        # archivo único (3 clases + anexo)
python scripts/build_decks.py --por-clase            # además, un .pptx por sección
```

---

## 4. Dónde quedamos (2026-10-26)

**Cátedra, Unidad 4 (Móvil)**
- La **Clase 1 se dio hasta la slide 15** (A4.1). Quedan **dos encuentros de 90 min** (decisión del 2026-10-13).
- **Versión final** en `unidad-04/`: un solo archivo, `Unidad-4-2026-completa.pptx` (63 slides): Clase 1 = 1–15 (dada), Clase 2 = 16–31, Clase 3 = 32–54, anexo de consulta "Android en Unity 6" = 55–63. Reparto 40/60. Guion en `unidad-04/03-clase-guion-docente.md`. Versiones v1–v4 en `unidad-04/versiones-anteriores/`.
- **2026-10-25 (informe del usuario):** las builds se probaron en celulares reales (sin evidencia archivada en el repo). **TP 3 en pausa** (defensa por video y D4-05 incluidas). Pendiente: D4-06 (programa: tabla UT/TP y bibliografía), que decide la titular.

- **Continuación (2026-10-19):** el deck completo ya se dio. Se agregó la **Clase 4 "Del caso real al código"** (slides 55–67): publicidad (UX y seguridad), FTC vs. Epic como falla de input, antes/después de código real PC → Android, orientación, A4.9 e ítem 9 del TP 3. Archivo vigente: `unidad-04/Unidad-4-2026-completa-v3.pptx` (87 slides, generado entero por el script; el anexo de mercado ya está en la fuente).

**Laboratorio de adaptación / porteo**
- **Asteroides:** porteo de entrada **implementado** (Input System 1.19.0, `ShipInputAdapter`, `Ship.SetIntent`, joystick y botón en pantalla, 3 tests). Tests: 10–11 de 14 en verde; las 3 hipótesis del pool fallan siempre por un defecto real, y hay 1 test inestable causado por el mismo defecto. Ver `laboratorio-adaptacion/PORTEO-ASTEROIDES.md`.
- **UNKNOWN:** comportamiento en el Device Simulator y en un teléfono real (no se ejecutó de forma interactiva).
- **Siguiente paso técnico propuesto:** probar en el Device Simulator y en un teléfono.
- **2D Platformer v2 (2026-10-19):** copia en `proyectos-unity/2D-Platformer-Unity-v2/` porteada a móvil (Input System, botones ◀ ▶ SALTAR en pantalla, orientación horizontal, safe area). Edit Mode 6/6, Play Mode 8/10 y **APK generado**. Las 2 fallas son un defecto del original: salto infinito (R-PLT-09). **Después (mismo día): salto corregido (DEC-LAB-015), sonido (moneda, salto, muerte), 3 vidas con Game Over (DEC-LAB-016) y nivel 2 con más huecos y enemigos; tests 15/15 + 17/17.** Falta probarlo jugando (sonido, nivel 2 completo). El original no se tocó. Commit `49ea3e4`. Ver `laboratorio-adaptacion/PORTEO-PLATFORMER.md`.
- **Rutas largas:** en la máquina con el repo en `Documents\2026\Videojuegos\…`  Unity falla al importar (límite de 260 caracteres). Usar `subst P: "<repo>\proyectos-unity"` o clonar en la ruta corta (ENV-01).
- Pendientes: DEC-LAB-004, 005, 007, 008, 013, 014; laboratorio de *Unravel* **en pausa por pedido del usuario** (DEC-LAB-009 a 012).
- DEC-LAB-002: el usuario decidió modificar Asteroides pese a la licencia de Kodeco (solo para pruebas y clase). **No volver a plantearlo como bloqueo.**

- **Match 3 UI Testing v2 (2026-10-24):** copia migrada a 6000.3.11f1 del tutorial de Kodeco (original 2019.4.21f1 intacto en `proyectos-unity/unity-ui-testing-tutorial-main/`). Junction `C:\Developer\unity\Match3-v2`. 5 tests Play Mode nuevos en verde, APK (IL2CPP ARM64) e instalador `Match3-UI-Testing-Setup.exe` generados con `Tools\generar_builds.ps1`. Falta probarlo en un teléfono. Commit `7943840`. Ver `proyectos-unity/Match3-UI-Testing-v2/README.md`.

**Cátedra, Unidad 5 (Consolas)**
- 2026-10-24: `unidad-05/01-desarrollo-tema-consolas.md` (PROPUESTO): consolas actuales, historia, ranking, histograma, ciclo de vida, regiones, precios 2026 y decisiones de diseño. Gráficos: `python scripts/graficos_consolas.py` (requiere `matplotlib`). Slides de la Clase 1 + anexo: `unidad-05/Unidad-5-2026-completa.pptx` (24 slides), fuente `04-diapositivas.md`, generar con `python scripts/graficos_consolas.py --slides` y `python scripts/build_decks.py` (`--version N` para no pisar). Falta: el resto de la unidad (certificación, mandos, multijugador, optimización).
- **2026-10-26: unidad completa en slides.** Arquitectura aprobada (`unidad-05/03-arquitectura-unidad.md`). Archivo único `unidad-05/Unidad-5-2026-completa-v2.pptx` (74 slides, 6 bloques, unos 150 min de exposición sin contar prácticos, más el anexo A de datos y el anexo B de Developer Mode). Generar con `python scripts/build_decks.py --version 2`. El Bloque 1 (ex Clase 1) todavía no se dio. TP 4 y rúbrica: PROPUESTOS, los define la titular.
- **Demo en Xbox (DEC-LAB-008 resuelta):** Xbox Series X de la docente en **Developer Mode** + paquetes UWP instalados por Device Portal (sin tienda ni nube). Cuatro paquetes: Asteroides y Platformer **originales** (sin cambios de gameplay) y **de consola** (copias `proyectos-unity/Asteroides-Xbox/` y `2D-Platformer-Xbox/` con la capa `Assets/Scripts/Console/`). Script `proyectos-unity/Tools-Xbox/generar_builds_xbox.ps1`. Guías: `laboratorio-adaptacion/GUIA-XBOX-DOCENTE.md` (docente) y `unidad-05/06-guia-alumnos-de-pc-a-xbox.md` (alumnos). Registro y evidencia: `laboratorio-adaptacion/PORTEO-XBOX.md`. **Los 4 `.msix` se generaron el 2026-10-26** (en `Builds/Xbox-Paquete/` de cada proyecto; no se versionan). Tests de la capa en verde, sin regresiones. **Pendiente:** activar el Dev Mode en la consola y hacer la prueba (tabla del paso 8 de la guía).

**Repo (2026-10-25):** `.gitignore` ampliado (estado de IDE, `CodeCoverage/Report-history/`, `/entregas/`, `/evidencias/`) y esos archivos sacados del índice. En Asteroides se versionó el Build Profile de Android y el paquete `com.unity.device-simulator.devices` 1.0.1. En el Platformer **original** se descartó la reimportación de TextMesh Pro que hizo Unity 6 al abrirlo: debe quedar en la línea base `e766f8c` (abrir solo la v2).

**SDD Arena (2026-10-26):** GDD (fase 6) y **Technical Specification (fase 7) cerradas** (tags `etapa-02-gdd-complete` y `etapa-03-technical-specification-complete`). Spec técnica en `docs/03-technical-specification/`: TECH-001…TECH-023; Windows, Android y WebGL; 16:9 en PC y 9:16 en Android con franjas; Input System solo teclado + táctil; URP + uGUI; balance aprobado; 7 sonidos y gráficos de Kenney (CC0, se importan en Implementation). **Siguiente:** Architecture Specification (READY, no iniciada; arranca con orden explícita del usuario). El usuario autorizó commitear al terminar cada tarea corta de la fase.

---

## 5. Lo que NO viaja con git (y qué hacer)

| Qué | Por qué | Qué hacer |
|---|---|---|
| `entregas/` (una subcarpeta por TP) | Entregas de estudiantes: datos de terceros. Ignorada por `.gitignore` | Copiar a mano |
| `evidencias/` | Fotos personales (no son de la cátedra). Ignorada por `.gitignore` | Copiar a mano si hace falta |
| `proyectos-unity/*.zip` (incluido el ZIP original del Platformer, versión 2022.3.13f1) | `.gitignore` excluye `*.zip` | La línea base migrada ya está en git (commit `e766f8c`) |
| `Match-3-Game/`, Boss Room, `_archivos/` | Ignorados por `.gitignore` | Copiar a mano si hacen falta |
| `Library/`, `Logs/`, `Temp/`, `UserSettings/` de cada proyecto Unity | Se regeneran | Nada |
| Memoria local de Claude (`~/.claude/projects/.../memory/`) | Local de la máquina | Su contenido relevante está en la sección 2 |
