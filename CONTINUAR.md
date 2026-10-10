# CONTINUAR: traspaso entre sesiones y máquinas

Punto de entrada para retomar el trabajo **desde cualquier computadora**. La memoria de Claude Code y el historial de la conversación son locales de cada máquina y **no** viajan con git. Este archivo concentra lo que hace falta para seguir: dónde está el estado, qué reglas pidió el usuario, qué herramientas instalar y qué falta hacer.

**Uso:** en la otra máquina, clonar el repo, abrir Claude Code en la raíz y escribir **"continuá"**. Claude lee este archivo (lo indica `CLAUDE.md`) y el archivo de estado del frente que corresponda.

- **Última actualización:** 2026-10-10
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

---

## 3. Herramientas que debe tener la otra máquina

| Herramienta | Versión / detalle | Para qué |
|---|---|---|
| Git + acceso a `https://github.com/gameoverplay26-stack/segunplataforma.git` | — | Sincronizar |
| **Ruta del clon recomendada:** `C:\Developer\unity\2026\clases-en-vivo` | — | Los documentos de auditoría citan rutas absolutas con esa base |
| Unity Hub + **Unity 6000.3.11f1** | Módulos: **Android Build Support** (OpenJDK, SDK, NDK) y Windows Build Support | Abrir los proyectos, correr tests y builds. **No cambiar de versión de Unity** |
| Python 3 (probado con 3.12) + `pip install python-pptx==1.0.2` | — | Generar los `.pptx` |
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
python scripts/build_decks.py --version 3            # los 4 decks
python scripts/build_decks.py --decks 2 --version 3  # uno solo
```

---

## 4. Dónde quedamos (2026-10-10)

**Cátedra, Unidad 4 (Móvil)**
- La **Clase 1 se dio hasta la slide 15** (A4.1). Faltan las slides 16–21 y las Clases 2, 3 y 4.
- Decks **v3** generados (`unidad-04/Unidad-4-Clase-N-2026-v3.pptx`), con el porteo real de Asteroides integrado y el reparto 40/60. Detalle en `unidad-04/03-clase-guion-docente.md`.
- **Pendiente de decisión:** cómo entran las slides 16–21 de la Clase 1 (60 min) en el próximo encuentro (ver el guion).
- Otros pendientes en `status-unidad.md`: imágenes reales, implementar el defecto de pausa (A4.4), probar en un teléfono, D4-05 y D4-06.

**Laboratorio de adaptación / porteo**
- **Asteroides:** porteo de entrada **implementado** (Input System 1.19.0, `ShipInputAdapter`, `Ship.SetIntent`, joystick y botón en pantalla, 3 tests). Tests: 10–11 de 14 en verde; las 3 hipótesis del pool fallan siempre por un defecto real, y hay 1 test inestable causado por el mismo defecto. Ver `laboratorio-adaptacion/PORTEO-ASTEROIDES.md`.
- **UNKNOWN:** comportamiento en el Device Simulator y en un teléfono real (no se ejecutó de forma interactiva).
- **Siguiente paso técnico propuesto:** probar en el Device Simulator y en un teléfono; luego el **2D Platformer** con el mismo patrón (Input System autorizado por DEC-LAB-006; ver `MOBILE-ADAPTATION.md` MOB-PLT-01…08).
- Pendientes: DEC-LAB-004, 005, 007, 008, 013, 014; laboratorio de *Unravel* **en pausa por pedido del usuario** (DEC-LAB-009 a 012).
- DEC-LAB-002: el usuario decidió modificar Asteroides pese a la licencia de Kodeco (solo para pruebas y clase). **No volver a plantearlo como bloqueo.**

**SDD Arena:** ver `docs/SDD-STATUS.md` (no se trabajó en esta sesión).

---

## 5. Lo que NO viaja con git (y qué hacer)

| Qué | Por qué | Qué hacer |
|---|---|---|
| `diseno-plataformas/trabajo-practico/` | Entregas de estudiantes (PDF) y un instalador `.exe`; no se suben sin decisión explícita del usuario | Copiar a mano o preguntar al usuario |
| `proyectos-unity/*.zip` (incluido el ZIP original del Platformer, versión 2022.3.13f1) | `.gitignore` excluye `*.zip` | La línea base migrada ya está en git (commit `e766f8c`) |
| `Match-3-Game/`, Boss Room, `_archivos/` | Ignorados por `.gitignore` | Copiar a mano si hacen falta |
| `Library/`, `Logs/`, `Temp/`, `UserSettings/` de cada proyecto Unity | Se regeneran | Nada |
| Memoria local de Claude (`~/.claude/projects/.../memory/`) | Local de la máquina | Su contenido relevante está en la sección 2 |
| `proyectos-unity/Asteroides/asteroide-final/ProjectSettings/Packages/com.unity.testtools.codecoverage/Settings.json` | Aparece modificado solo por fin de línea | No commitear |
