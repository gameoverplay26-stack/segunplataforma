# EVIDENCE-LOG: evidencias y fuentes

- **Fecha de todas las verificaciones y consultas:** 2026-10-10.
- **Tipo de evidencia:** todas las `EV-###` son **lectura de archivos o salida de comandos de solo lectura** (`ls`, `cat`, `grep`, `find`, `unzip -l/-p`, `git status`). **No** se abrió Unity, no se compiló, no se ejecutaron tests ni se hizo ningún build durante esta auditoría.
- Rutas base: P1 = `C:\Developer\unity\2026\clases-en-vivo\proyectos-unity\Asteroides\asteroide-final`; P2 = `C:\Developer\unity\2026\clases-en-vivo\proyectos-unity\2D-Platformer-Unity-main`.

## Evidencias locales

| ID | Qué se verificó | Archivo o comando | Resultado |
|---|---|---|---|
| EV-001 | Existencia e inventario de ambos proyectos | `ls -la` de P1 y P2; `find Assets -type f` | Ambos tienen `Assets`, `Packages`, `ProjectSettings` y `Library`. P1: 7 `.cs`, 9 prefabs, 1 escena. P2: 7 `.cs`, 11 prefabs, 3 `.unity` |
| EV-002 | Estado git | `git status` (repo `clases-en-vivo`) | P1: ` M …/ProjectSettings/Packages/com.unity.testtools.codecoverage/Settings.json` (previo a la auditoría). P2: `?? proyectos-unity/2D-Platformer-Unity-main/` |
| EV-003 | Versión y paquetes de P1 | `P1\ProjectSettings\ProjectVersion.txt`, `P1\Packages\manifest.json` | `6000.3.11f1 (3000ef702840)`; sin `com.unity.inputsystem` |
| EV-004 | Licencias de P1 | Cabecera de `P1\Assets\Scripts\*.cs` (líneas 1–29); `P1\Assets\uipack-space\license.txt` | Kodeco 2023, con exclusión de uso pedagógico (líneas 14–20); Kenney CC0. `Models` y `Audio` sin licencia |
| EV-005 | Player Settings de P1 | `P1\ProjectSettings\ProjectSettings.asset` | `productName: UnityUnitTestingTutorial`, 1024×768, `defaultScreenOrientation: 4`, 4 autorrotaciones = 1, `androidRenderOutsideSafeArea: 1`, `AndroidMinSdkVersion: 25`, `AndroidTargetSdkVersion: 0`, `AndroidTargetArchitectures: 5`, `scriptingBackend.Android: 0`, `activeInputHandler: 0`, `m_ActiveColorSpace: 0`, `runInBackground: 1`, `applicationIdentifier: {}` |
| EV-006 | Escenas, prefabs y UI de P1 | `P1\ProjectSettings\EditorBuildSettings.asset`; `P1\Assets\Scenes\Game.unity`; `P1\Assets\Resources\Prefabs\Game.prefab`; `P1\Assets\Prefabs\UICanvas.prefab` | Build: solo `Game.unity` (instancia del prefab GUID `3befbaa1…` = `Game.prefab`). Cámara `orthographic: 1`, `orthographic size: 5`. UICanvas: `m_UiScaleMode: 1`, 1920×1080, `m_MatchWidthOrHeight: 0`. UnityEvent `m_MethodName: NewGame` |
| EV-007 | Lógica de P1 | `P1\Assets\Scripts\{Asteroid,Game,Laser,Ship,Spawner}.cs` | Ver las líneas citadas en `PROJECT-DISCOVERY.md` §1 |
| EV-008 | Tests y cobertura de P1 | `P1\Assets\Tests\TestSuite.cs`, `IntegrationHypothesesTests.cs`, `Tests.asmdef`; `P1\CodeCoverage\Report\index.html`; búsqueda de `TestResults*.xml` en `%USERPROFILE%\AppData\LocalLow` | 7 + 4 tests. Reporte de cobertura "Generated on 28/09/2026 - 22:13:23". **No hay XML de resultados de P1** (solo de otros proyectos: Match 3 Game, UnityTestCalculadora) |
| EV-009 | Versión y paquetes de P2 | `P2\ProjectSettings\ProjectVersion.txt`, `P2\Packages\manifest.json` | `6000.3.11f1`; URP 17.3.0, Cinemachine 2.10.6, feature.2d 2.0.2, ugui 2.0.0, visualscripting 1.9.10, test-framework 1.6.0; sin Input System |
| EV-010 | Player, Build, Quality y Graphics Settings de P2 | `P2\ProjectSettings\{ProjectSettings,EditorBuildSettings,QualitySettings,GraphicsSettings}.asset` | 1920×1080, orientación 4 con 4 autorrotaciones, `AndroidTargetArchitectures: 1`, `scriptingBackend: {}`, `androidUseSwappy: 1`, `activeInputHandler: 0`, Linear. Build: `Menu.unity` (0), `Level.unity` (1). Calidad Android = 2, GameCore* = 5. URP asignado |
| EV-011 | Lógica de P2 | `P2\Assets\Scripts\*.cs` | Ver `PROJECT-DISCOVERY.md` §2 |
| EV-012 | UnityEvents en escenas de P2 y llamadas a `HurtPlayer` | `grep m_MethodName` en `P2\Assets\Scenes`; `grep -rn HurtPlayer P2\Assets` | Métodos: `Level`, `Menu`, `Quit` ×2. `HurtPlayer` solo aparece en su definición (`HealthManager.cs:33`) |
| EV-013 | Ejes de entrada | `P1\` y `P2\ProjectSettings\InputManager.asset` | Horizontal (←→/AD + joystick, tipo 2), Jump (space + botón de joystick), Fire1–3, Submit, Cancel. P2 agrega ejes "Debug" de URP |
| EV-014 | Controles móviles en escena | `P2\Assets\Scenes\Level.unity` (GameObject `MobileControls` y línea 7238) | `MobileControls`: un solo componente (RectTransform), `m_Children: []`, 100×100. `controlmode: 1` |
| EV-015 | Cámara de P2 | `P2\Assets\Scenes\Level.unity` (≈ líneas 18021–18046) | Cinemachine con `m_Follow`, `m_BoundingShape2D` y `OrthographicSize: 10` |
| EV-016 | Parámetros del Animator | `P2\Assets\dog\Animations\sr.controller` | `m_AnimatorParameters`: `run`, `jump` (no `isGrounded`) |
| EV-017 | Compilación y ejecución previas de P2 (**no generadas por esta auditoría**) | `%LOCALAPPDATA%\Unity\Editor\Editor.log` (modificado el 10/10/2026 16:27) | Compilación de Assembly-CSharp solo con advertencias CS0618 (`HealthManager.cs:26`, `GameManager.cs:93`). Play Mode: `Parameter 'isGrounded' does not exist.` ×2447 (desde la línea 10615) y `Died` ×1 (línea 30716) |
| EV-018 | UI de P2 | `P2\Assets\Scenes\Level.unity`, `Menu.unity` | CanvasScaler 1920×1080 con match 0.5; `m_fontSize` de 36 a 87.1; `m_Navigation m_Mode: 3`; `m_FirstSelected: {fileID: 0}` |
| EV-019 | Guardado, pausa y ciclo de vida | `grep -rn "PlayerPrefs\|File\.\|persistentDataPath\|Time.timeScale\|OnApplicationPause\|OnApplicationFocus"` en `Scripts` de P1 y P2 | Sin coincidencias (código de salida 1) |
| EV-020 | Origen de P2 | `unzip -l` / `unzip -p` de `proyectos-unity\2D-Platformer-Unity-main.zip`; `P2\LICENSE`; `P2\README.md` | ZIP con `ProjectVersion.txt` = `2022.3.13f1 (5f90a5ebde0f)`; MIT "Copyright (c) 2023 Hasan"; el README indica "compatible with Unity 20xx.xx". Arte sin licencia propia |
| EV-021 | Migración de paquetes de P2 | `P2\Logs\Packages-Update.log` | "Sat Oct 10 16:13:48 2026 … Packages were changed": actualizaciones y eliminación de `com.unity.textmeshpro@3.0.6` |
| EV-022 | Modificación automática de un script de P2 | `Editor.log` línea 3284 (`[ApiUpdater] … Files: 1 modified`); `stat` de `P2\Assets\Scripts\PlayerController.cs` (16:17:54) vs. el resto (16:11:22); el ZIP contiene `rb.velocity` | El API Updater modificó `PlayerController.cs` |
| EV-023 | Módulos de Unity instalados | `ls "C:\Program Files\Unity\Hub\Editor"` y `…\6000.3.11f1\Editor\Data\PlaybackEngines` | Editores 6000.2.10f1 y 6000.3.11f1. Módulos: `AndroidPlayer` (con SDK, NDK y OpenJDK), `MetroSupport`, `windowsstandalonesupport`. Sin Xbox ni iOS |

## Fuentes externas

**Modo de consulta:** "leída" = página obtenida y leída en esta sesión; "buscador" = dato tomado del resultado del buscador, sin abrir la página. Las segundas deben releerse antes de citarlas en material de clase.

| ID | Título | URL completa | Modo | Requisito o dato que respalda | Tipo y limitaciones |
|---|---|---|---|---|---|
| SRC-002 | Unity path overview (Xbox Developer Docs) | https://devdocs.xbox.com/paths/unity/overview | Leída | ID@Xbox, plug-in GDK vía ID@Xbox, Partner Center, Unity 2022 LTS o posterior | Oficial (Microsoft). No detalla el dev kit ni la matriz de versiones |
| SRC-003 | XAG 101: Text display (Xbox Accessibility Guidelines) | https://devdocs.xbox.com/build/game-principles/accessibility/xag-deep-dives/xag-101-text-display.md | Buscador | 26 px de altura de cuerpo a 1080p en consola, 52 px en 4K; texto escalable | Oficial; **releer** |
| SRC-004 | Screen.safeArea (Unity 6.0 Scripting API, versión en japonés) | https://docs.unity3d.com/ja/6000.0/ScriptReference/Screen-safeArea.html | Buscador | Uso de safe area y relación con `renderOutsideSafeArea` | Oficial; documentación de 6000.0, no de 6000.3 |
| SRC-005 | Android Player settings (Unity 6.3, espejo docs.unity.cn) | https://docs.unity.cn/6000.3/Documentation/Manual/class-PlayerSettingsAndroid.html | Buscador | Orientación por defecto y autorrotación; Render Outside Safe Area | Espejo oficial de Unity China, etiquetado como alpha |
| SRC-006 | On-screen Controls, Input System 1.8 | https://docs.unity3d.com/Packages/com.unity.inputsystem@1.8/manual/OnScreen.html | Buscador | `OnScreenStick` y `OnScreenButton` simulan controles de gamepad | Oficial; la versión del paquete compatible con 6000.3.11f1 es UNKNOWN |
| SRC-007 | Make apps more accessible (Android Developers) / Touch target size (Android Accessibility Help) | https://developer.android.com/guide/topics/ui/accessibility/apps · https://support.google.com/accessibility/android/answer/7101858 | Buscador | Objetivos táctiles de 48×48 dp o más, separados por 8 dp o más | Oficial (Google) |
| SRC-008 | Target API level requirements (Google Play) | https://developer.android.com/google/play/requirements/target-sdk | Buscador | API 36 o superior para apps nuevas y actualizaciones desde el 31/08/2026 | Oficial; **releer** antes de publicar |
| SRC-009 | Input (Unity 6.0 Manual) | https://docs.unity3d.com/6/Documentation/Manual/Input.html | Buscador | El Input Manager clásico es legacy y el paquete Input System es el recomendado | Oficial |
| SRC-010 | Console development (Unity) | https://unity.com/en/solutions/console | Buscador | Unity Pro o Preferred Platform key para plataformas cerradas; aprobación del fabricante | Oficial (Unity). Contexto histórico de terceros: https://www.gamedeveloper.com/programming/going-forward-unity-devs-will-need-unity-pro-to-publish-on-consoles (2021, **no** es requisito vigente) |
| SRC-011 | Unravel (video game), Wikipedia | https://en.wikipedia.org/wiki/Unravel_(video_game) | Leída | Desarrolladora, editora, fecha y plataformas; mecánica del hilo | Secundaria |
| SRC-012 | Unravel, Xbox Store | https://www.xbox.com/en-us/games/store/unravel/C11KKHB5H7QJ | Buscador | Xbox One y Series X\|S, EA Play, narrativa "sin palabras" | Oficial (tienda); el precio y la disponibilidad cambian |
| SRC-013 | Unravel Walkthrough (gamerwalkthroughs.com) | https://gamerwalkthroughs.com/unravel/ | Leída | Lista de 12 capítulos; 10 = "Rust" | **Terceros**, no oficial |
| SRC-014 | Unravel Chapter 10: Rust (gamerwalkthroughs.com) | https://gamerwalkthroughs.com/unravel/chapter-10-rust/ | Leída | Secuencia de desafíos del capítulo 10 (balanceos, ventana, grúa, checkpoint) | **Terceros**; se debe confirmar en la copia real |
| SRC-015 | Reckless achievement (TrueAchievements) | https://www.trueachievements.com/a212221/reckless-achievement | **No accesible** (HTTP 403) | — | No se usa como respaldo |
