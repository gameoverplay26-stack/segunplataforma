# PORTEO-XBOX: registro de la demo en Xbox (Developer Mode, UWP)

- **Fecha:** 2026-10-26 · **Unity:** 6000.3.11f1 · **Rama:** `main` (sin commit).
- **Autorización:** DEC-LAB-008 (demo real en la Xbox Series X de la docente, en Developer Mode, sin tienda ni nube) y DEC-LAB-017 (instalar la carga de trabajo de UWP, las herramientas C++ y el SDK).
- **Guías:** `GUIA-XBOX-DOCENTE.md` (procedimiento completo) y `../unidad-05/06-guia-alumnos-de-pc-a-xbox.md`.
- **Análisis previo:** `XBOX-ADAPTATION.md` (fase 2). Este registro reemplaza su conclusión "BLOCKED". Para una **demo** existe una vía pública: Developer Mode + UWP. Publicar sigue BLOCKED (requiere ID@Xbox y el GDK).

## 1. Vía elegida y por qué

| | Xbox nativo (GDK / GameCore) | **Developer Mode + UWP (elegida)** |
|---|---|---|
| Acceso | ID@Xbox, NDA, plug-in GDK privado, Unity Pro o clave de plataforma | App Xbox Dev Mode + cuenta de Partner Center **gratuita** |
| Instalación | Kit de desarrollo | Paquete `.msix` por red local (Device Portal) |
| Publicación | Sí, con certificación | **No**: Microsoft ya no acepta juegos UWP en la tienda de Xbox |
| Recursos para un juego | Kit completo | 5 GB de RAM, 4 núcleos exclusivos + 2 compartidos, GPU completa, solo x64 |

Fuentes en la sección "Fuentes" de `GUIA-XBOX-DOCENTE.md`. En Unity 6000.3, `PlayerSettings.WSATargetFamily` todavía incluye la familia **Xbox** (verificado en la referencia de scripting).

## 2. Las cuatro versiones

| Paquete | Proyecto | Identidad (`PackageName`) | Cambios respecto del proyecto de clase |
|---|---|---|---|
| Asteroides (original) | `proyectos-unity/Asteroides/asteroide-final` | `Catedra.Asteroides.Original` | Solo `Assets/Editor/BuildXbox.cs` (herramienta de Editor) y los ajustes de UWP que escribe al compilar. **Sin cambios de gameplay ni de UI** |
| Platformer (original) | `proyectos-unity/2D-Platformer-Unity-v2` | `Catedra.Platformer.Original` | Ídem |
| Asteroides (consola) | `proyectos-unity/Asteroides-Xbox` (copia nueva) | `Catedra.Asteroides.Consola` | Capa de consola (§3) |
| Platformer (consola) | `proyectos-unity/2D-Platformer-Xbox` (copia nueva) | `Catedra.Platformer.Consola` | Capa de consola (§3) |

- Cada versión tiene **su propia identidad de paquete**, así que las cuatro conviven en la consola.
- El nombre visible se cambia **solo durante la build** (`BuildXbox` restaura `productName`). El APK y el `.exe` conservan el suyo.
- Las copias se hicieron con `robocopy` desde los proyectos de clase, sin `Library/`, `Builds/`, `Logs/`, `Temp/`, `obj/` ni `UserSettings/`.

## 3. Capa de consola (versiones "consola")

Código en `Assets/Scripts/Console/`. Es **idéntico** en los dos proyectos salvo `ConsoleText.cs`: Asteroides usa `Text` y el Platformer también usa TextMesh Pro. **No edita escenas ni prefabs:** se instala sola con `[RuntimeInitializeOnLoadMethod(AfterSceneLoad)]` y actúa en cada `sceneLoaded`.

| Archivo | Responsabilidad | Prueba de aceptación |
|---|---|---|
| `ConsoleLayer.cs` | Reemplaza `StandaloneInputModule` por `InputSystemUIInputModule` (Asteroides lo traía del Input Manager); mantiene el **foco** en el botón de más arriba si nada está seleccionado; color "Selected" amarillo; oculta los botones que llaman a `Quit`; **pausa** (`Time.timeScale = 0`, `AudioListener.pause`, overlay con mensaje) con Menu (≡) o Esc, al desconectarse un mando físico y al perder el foco; al cargar escena, reanuda | XB-AC-01, 02, 04 |
| `PauseState.cs` | Estado de pausa sin MonoBehaviour. Menu pausa solo durante la partida (sin botones a la vista) y reanuda siempre; la desconexión del control tiene prioridad sobre el mensaje | XB-AC-04 |
| `ConsoleRules.cs` | Reglas puras: método `Quit`, pausa por dispositivo (solo **físico**: `device.native`), escala de `CanvasScaler`, **26 px a 1080p** (XAG 101) | XB-AC-03, 04 |
| `ConsoleText.cs` | Sube a 26 px a 1080p los textos más chicos (`Text` y, en el Platformer, `TMP_Text`) | XB-AC-03 |
| `IConsolePausable.cs` | Los adaptadores de entrada (`ShipInputAdapter`, `PlayerInputAdapter`) se apagan en pausa y limpian la intención | XB-AC-04 |

**Gameplay:** no cambió. `Ship.cs`, `PlayerController.cs` y la lógica de juego son los de las versiones de clase. En los adaptadores solo se agregó `SetConsolePaused`.

**Defecto encontrado y corregido durante la implementación:**
- **Síntoma:** en Asteroides de consola, 5 tests fallaban con `NullReferenceException` en `ShipInputAdapter.SetConsolePaused`.
- **Causa:** `MobileControlsVisibility` apaga el joystick y el botón en pantalla fuera del móvil. Al apagarse, `OnScreenStick`/`OnScreenButton` **quitan su gamepad virtual**, y la capa lo tomaba como "control desconectado" y pausaba durante la carga de la escena.
- **Corrección:** solo cuentan los mandos con `device.native`, más una guarda de nulo en los adaptadores.
- **Relevancia:** el defecto también habría aparecido en la consola.

## 4. Tests (evidencia en `evidencia/`)

| Corrida | Archivo | Resultado | Lectura |
|---|---|---|---|
| Platformer consola, Edit Mode | `xbox-01-platformer-consola-editmode.xml` | **25/25** | 15 previos + 10 de `ConsoleRulesTests` |
| Platformer consola, Play Mode | `xbox-02-platformer-consola-playmode.xml` | **25 passed, 0 failed, 2 skipped** | Los 2 *skipped* son tests del paquete Input System marcados *Ignored*. Incluye 6 de `ConsoleLayerTests`. Corrida antes de la corrección de §3 |
| Platformer consola, ambos modos, tras corregir | `xbox-01b-…-editmode.xml`, `xbox-02b-…-playmode.xml` | **25/25** y **25 passed, 0 failed, 2 skipped** | Sin cambios |
| Asteroides consola, Edit Mode (1.ª) | `xbox-03-asteroides-consola-editmode.xml` | 12/14 | Los 2 rojos son `AndroidBuildConfigTests` (Mono, sin ARM64), **igual que en el original** |
| Asteroides consola, Play Mode (1.ª) | `xbox-04-asteroides-consola-playmode.xml` | 10/19 | 5 de la capa en rojo por el defecto de §3 |
| Asteroides consola, Edit Mode (tras corregir) | `xbox-03b-asteroides-consola-editmode.xml` | 12/14 | Ídem |
| Asteroides consola, Play Mode (tras corregir) | `xbox-04b-asteroides-consola-playmode.xml` | **16/19** | Los 5 de la capa en verde. Rojos: las 3 hipótesis del pool (defecto conocido, `PORTEO-ASTEROIDES.md`) |
| Asteroides **original**, Edit Mode (línea base) | `xbox-00a-asteroides-original-editmode.xml` | 2/4 | Los mismos 2 rojos de configuración de Android |
| Asteroides **original**, Play Mode (línea base) | `xbox-00b-asteroides-original-playmode.xml` | 10/14 | 3 hipótesis + `TestSuite.LaserMovesUp` (inestable, ya registrado) |

**Conclusión:** sin regresiones atribuibles a la capa de consola. Lo que falla en la versión de consola también falla en el original.

## 5. Toolchain y builds

| Paso | Evidencia | Estado |
|---|---|---|
| 1.ª build UWP (Platformer v2), antes de instalar el SDK | `2D-Platformer-Unity-v2/Logs/build-xbox.log`, línea 8955: `Could not find any supported UWP SDK installations. Please install Windows SDK version 10.0.19041.0 (or newer).` | FAIL → BLOCKED por toolchain |
| Instalación de Visual Studio: carga de trabajo UWP | `setup.exe modify … --add Microsoft.VisualStudio.Workload.Universal --includeRecommended` (código 0), pero **sin** Windows SDK en disco | Incompleta |
| Instalación de Visual Studio: SDK y C++ de UWP | `--add Microsoft.VisualStudio.Component.Windows11SDK.26100 Microsoft.VisualStudio.ComponentGroup.UWP.VC Microsoft.VisualStudio.Component.VC.Tools.x86.x64 Microsoft.VisualStudio.ComponentGroup.UWP.Support` (código 0); `C:\Program Files (x86)\Windows Kits\10\Include\10.0.26100.0` presente | PASS |
| 1.ª corrida del script | Se trabó después de la build de Unity: `Start-Process -Wait` (PowerShell 5.1) espera a los descendientes y quedó vivo `vctip.exe`. Corregido con `WaitForExit()` sobre el proceso de Unity. Otros dos arreglos: lista `-Proyectos "a,b"` (con `-File` llega como un solo texto) y archivo guardado en UTF-8 con BOM (acentos en PowerShell 5.1) | Corregido |
| **Paquetes de las 4 versiones** | `Logs/build-xbox.log` (`[BuildXbox] Succeeded`) y `Logs/build-xbox-msbuild.log` de cada proyecto; salida del script en `2D-Platformer-Xbox/Logs/generar_builds_xbox.out.txt` y `Asteroides-Xbox/Logs/generar_builds_xbox.out.txt` | **PASS (build)** |

| Paquete | Archivo (`Builds/Xbox-Paquete/…_Master_Test/`) | Tamaño | Manifiesto |
|---|---|---|---|
| Asteroides (original) | `Asteroides (original)_1.0.0.0_x64_Master.msix` | 27,6 MB | `Catedra.Asteroides.Original`, x64, `Windows.Xbox` + `Windows.Desktop` (MinVersion 10.0.19041.0) |
| Asteroides (consola) | `Asteroides (consola)_1.0.0.0_x64_Master.msix` | 27,6 MB | `Catedra.Asteroides.Consola`, ídem |
| Platformer (original) | `Platformer (original)_1.0.0.0_x64_Master.msix` | 37,8 MB | `Catedra.Platformer.Original`, ídem |
| Platformer (consola) | `Platformer (consola)_1.0.0.0_x64_Master.msix` | 37,8 MB | `Catedra.Platformer.Consola`, ídem |

Cada carpeta trae el `.cer`, `Dependencies/x64/Microsoft.VCLibs.x64.14.00.appx` (dependencia `Microsoft.VCLibs.140.00` del manifiesto) e `Install.ps1`. Tiempos de la build de Unity: 4 min 21 s (Platformer, primera vez) y entre 16 s y 5 min en las siguientes; msbuild compila el C++ de IL2CPP en Master. Advertencia sin efecto: `SuppressSystemOverlays` obsoleto en `App.cpp` (código generado por Unity).

**Lo que esto prueba:** que los cuatro paquetes **se generan** y declaran la familia Xbox. **No** prueba que corran en la consola: eso es UNKNOWN hasta la prueba del §7.

**Hallazgo sobre rutas (ENV-01), medido el 2026-10-26:** en la PC de la cátedra hay rutas de 280 caracteres (`2D-Platformer-Unity-v2\Library\PackageCache\com.unity.collections…`) y de 300 (`asteroide-final\Library\Bee\Android\…`, de la build de Android). Funcionan porque `LongPathsEnabled = 1`. La ruta más larga fuera de `Builds/` mide 226 caracteres desde `proyectos-unity`. Por eso, en una PC sin rutas largas, falla aunque el repo esté en una ruta "corta".

## 6. Archivos nuevos o tocados

| Archivo | Cambio |
|---|---|
| `proyectos-unity/Tools-Xbox/generar_builds_xbox.ps1` | Nuevo: certificado de prueba, Unity batchmode, msbuild Master x64 sideload. Primero corre la verificación de requisitos |
| `proyectos-unity/Tools-Xbox/verificar_requisitos_xbox.ps1` | Nuevo: tabla OK/FALTA de Unity + módulo UWP, Visual Studio 2022 y componentes, MSBuild, Windows SDK, proyectos, rutas largas y certificados; `-Instalar` agrega lo que falte de Visual Studio. Probado en la PC de la cátedra: todo OK (código 0); con una ruta de Unity inexistente, 2 FALTA (código 1) |
| `*/Assets/Editor/BuildXbox.cs` (4 proyectos) | Nuevo: build UWP x64, familias Xbox + Desktop, identidad de paquete y certificado |
| `ProjectSettings.asset` de `asteroide-final` y `2D-Platformer-Unity-v2` | La build UWP escribió solo campos `metro*` (familias Desktop y Xbox, `metroPackageName`, certificado `Certificados/xbox-prueba.pfx`) y la entrada de batching de *Windows Store Apps*. `productName`, Android y Standalone quedaron intactos (verificado con `git diff`). Los demás archivos que figuran modificados en el Platformer v2 solo cambian los finales de línea |
| `Asteroides-Xbox/`, `2D-Platformer-Xbox/` | Copias nuevas + capa de consola + tests (`ConsoleRulesTests` en Edit Mode, `ConsoleLayerTests` en Play Mode) |
| `Asteroides-Xbox/Assets/Tests/*.asmdef` | Referencias a `GameAssembly` y `Unity.InputSystem` para los tests nuevos |
| `.gitignore` (raíz) | `*.pfx` y `**/Certificados/` (clave privada del certificado de prueba) |

## 7. Prueba en la consola

Pendiente. Completar con la tabla del paso 8 de `GUIA-XBOX-DOCENTE.md`: fecha, resultados PASS/FAIL/UNKNOWN y capturas del Device Portal.

## 8. Pendientes

- [x] Generar los 4 paquetes y registrar el resultado en §5.
- [x] Volver a correr el Play Mode del Platformer de consola después de la corrección de §3.
- [ ] Prueba en la consola (§7).
- [ ] UNKNOWN: comportamiento real de la suspensión y reanudación de UWP en Xbox; tamaño de texto **medido** en la TV; *title-safe*.
- [ ] Decidir (titular) el peso de la guía de alumnos en el TP 4 (que todavía no existe).
