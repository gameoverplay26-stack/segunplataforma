# PROJECT-DISCOVERY: inventario y estado inicial

- **Fecha:** 2026-10-10 · **Modo:** solo lectura (no se abrió Unity, no se compiló, no se ejecutaron tests ni builds).
- **Método:** lectura de archivos del proyecto (`ProjectSettings/`, `Packages/`, `Assets/`), inspección textual de escenas y prefabs (YAML) y lectura de logs ya existentes del Editor. Cada afirmación remite a una evidencia `EV-###` de `EVIDENCE-LOG.md`.
- **Advertencia metodológica:** salvo donde se cita un log de ejecución, todo lo que sigue es **inspección estática**. Que el código "debería" comportarse de una forma no equivale a una prueba ejecutada.

---

## 0. Estado de acceso a las rutas originales

| Proyecto | Ruta | Existe | ¿Es un proyecto Unity completo? | Evidencia |
|---|---|---|---|---|
| P1 Asteroides | `C:\Developer\unity\2026\clases-en-vivo\proyectos-unity\Asteroides\asteroide-final` | VERIFICADO | VERIFICADO: tiene `Assets/`, `Packages/manifest.json`, `ProjectSettings/` y `Library/` generada | EV-001 |
| P2 2D Platformer | `C:\Developer\unity\2026\clases-en-vivo\proyectos-unity\2D-Platformer-Unity-main` | VERIFICADO | VERIFICADO: tiene `Assets/`, `Packages/`, `ProjectSettings/` y `Library/` generada | EV-001 |

**Estado de control de versiones:**
- P1 está versionado en el repositorio `clases-en-vivo`. Al iniciar la auditoría había un cambio previo, no hecho por esta auditoría, en `ProjectSettings/Packages/com.unity.testtools.codecoverage/Settings.json` (EV-002).
- P2 **no está versionado**: aparece como `??` (untracked) en git y no tiene `.git` propio. Su origen es `proyectos-unity\2D-Platformer-Unity-main.zip`, que está ignorado por git (EV-002, EV-020).

---

## 1. P1 Asteroides

Ruta: `C:\Developer\unity\2026\clases-en-vivo\proyectos-unity\Asteroides\asteroide-final`

### 1.1 Inventario técnico

| Aspecto | Hallazgo | Estado | Evidencia |
|---|---|---|---|
| Versión de Unity | `6000.3.11f1 (3000ef702840)` | VERIFICADO | EV-003 |
| Identidad | `productName: UnityUnitTestingTutorial`, `companyName: DefaultCompany`, `applicationIdentifier: {}` (vacío) | VERIFICADO | EV-005 |
| Origen y licencia del código | Los 5 scripts de `Assets/Scripts/` llevan cabecera **Copyright (c) 2023 Kodeco Inc.**, que **prohíbe expresamente** el uso "in any work that is designed, intended, or marketed for pedagogical or instructional purposes" (líneas 14–20 de cada archivo) | VERIFICADO (texto). Interpretación legal: UNKNOWN → **DEC-LAB-002** | EV-004 |
| Licencia del arte UI | `Assets/uipack-space/license.txt`: Kenney, CC0 | VERIFICADO | EV-004 |
| Licencia de modelos y audio | `Assets/Models/*.fbx`, `Assets/Audio/*.ogg`: sin archivo de licencia | UNKNOWN | EV-004 |
| Escenas | `Assets/Scenes/Game.unity`, única escena del build. Solo contiene una instancia del prefab `Assets/Resources/Prefabs/Game.prefab` | VERIFICADO | EV-006 |
| Flujo de navegación | Pantalla de título con botón "Start", que llama a `Game.NewGame()` por UnityEvent desde `UICanvas.prefab`. Partida → Game Over (título y botón reaparecen) → nueva partida. No hay menú de pausa, opciones ni salida | VERIFICADO (estático) | EV-006, EV-007 |
| Prefabs | `Asteroid`, `Asteroid2`, `Asteroid3`, `Asteroid4`, `Laser`, `Ship`, `Spawner`, `UICanvas`, `Resources/Prefabs/Game` | VERIFICADO | EV-001 |
| Scripts | `Asteroid.cs`, `Game.cs`, `Laser.cs`, `Ship.cs`, `Spawner.cs` en el ensamblado `GameAssembly.asmdef` | VERIFICADO | EV-007 |
| Paquetes | Sin Input System, sin URP. Incluye `com.unity.test-framework 1.6.0`, `com.unity.testtools.codecoverage 1.3.0`, `com.unity.ugui 2.0.0`, `com.unity.ai.navigation`, `com.unity.timeline` y módulos estándar | VERIFICADO | EV-003 |
| Render | Built-in Render Pipeline (`m_CustomRenderPipeline: {fileID: 0}`), espacio de color **Gamma** (`m_ActiveColorSpace: 0`) | VERIFICADO | EV-005 |
| Sistema de entrada | `activeInputHandler: 0` (Input Manager clásico). `Ship.Update()` lee teclas **fijas**: `KeyCode.Space` (disparo), `KeyCode.LeftArrow` y `KeyCode.RightArrow`. **No usa ejes**, así que el gamepad no tiene efecto sobre la nave y tampoco existe entrada táctil. El inicio de partida es un botón UI, que se acciona con el mouse | VERIFICADO (estático) | EV-005, EV-007 |
| Física | Física **3D** (`OnCollisionEnter(Collision)`) en un juego de vista 2D. El choque con la nave se detecta **por nombre de objeto** (`collision.gameObject.name == "ShipModel"`) | VERIFICADO | EV-007 |
| Cámara | Cámara ortográfica, `orthographic size: 5`, dentro de `Game.prefab` | VERIFICADO | EV-006 |
| HUD | `UnityEngine.UI.Text` (texto uGUI clásico, no TextMeshPro): "Score: N", texto de Game Over, título y botón Start. `UICanvas` usa Scale With Screen Size con referencia de 1920×1080 y `match = 0` (escala solo por ancho) | VERIFICADO | EV-006, EV-007 |
| Resolución y orientación | Por defecto 1024×768. `defaultScreenOrientation: 4` (Auto Rotation) con **las cuatro orientaciones permitidas**, retrato incluido. `fullscreenMode: 1` | VERIFICADO | EV-005 |
| Audio | `AudioSource` en la nave (disparo, `PlayOneShot`) y en el spawner (explosión, que se dispara desde el callback de destrucción del pool) | VERIFICADO (estático) | EV-007 |
| Animación | Sin Animator. Explosión por activación de un GameObject | VERIFICADO | EV-007 |
| Android (config actual) | `AndroidMinSdkVersion: 25`, `AndroidTargetSdkVersion: 0` (automático), `AndroidTargetArchitectures: 5`, `scriptingBackend.Android: 0` (Mono), `androidRenderOutsideSafeArea: 1` | VERIFICADO (valores). Compatibilidad de Mono con ARM64: UNKNOWN, hay que verificarla en el editor | EV-005 |
| Tests existentes | `Assets/Tests/TestSuite.cs` (7 tests: 6 `[UnityTest]` y 1 `[Test]`) y `Assets/Tests/IntegrationHypothesesTests.cs` (4 `[UnityTest]` formulados como "hipótesis"). Todos instancian `Resources/Prefabs/Game` | VERIFICADO (existencia) | EV-008 |
| Resultado de los tests | **No hay XML del Test Runner.** Existe un reporte de Code Coverage en `CodeCoverage/Report/index.html` generado el 28/09/2026, que prueba que alguna vez se corrió una suite, pero **no** qué tests pasaron | **UNKNOWN** | EV-008 |

### 1.2 Riesgos técnicos detectados por inspección estática (hay que confirmarlos ejecutando)

| ID | Riesgo | Archivo | Estado |
|---|---|---|---|
| R-AST-01 | **Uso incoherente de `ObjectPool`.** `Spawner` crea asteroides con `Instantiate` directo y nunca con `asteroids.Get()`. `Laser` llama a `Release()` sobre objetos que nunca salieron del pool y luego los destruye, así que el pool acumula referencias a objetos destruidos. `ClearAsteroids()` llama a `Dispose()`, que **no** elimina los asteroides activos en escena | `Spawner.cs:52-56, 73-99, 114-117`; `Laser.cs:52-53` | VERIFICADO (código). Efecto en juego: UNKNOWN. El test `NewGame_RemovesLeftoverAsteroids` lo plantea como hipótesis |
| R-AST-02 | La corrutina de spawn se guarda como un único `IEnumerator` que se detiene y se reanuda; un segundo `NewGame()` puede alterar el ritmo de aparición | `Spawner.cs:56-62, 119-122` | Hipótesis; existe el test `DoubleNewGame_DoesNotChangeSpawnRate` |
| R-AST-03 | Unidades inconsistentes: la nave se limita a `localPosition.x` ±40, mientras los asteroides aparecen en `x` mundial entre -8 y 8 | `Ship.cs:46-47`; `Spawner.cs:103` | UNKNOWN; depende de la escala o jerarquía del prefab. Hay que observarlo jugando |
| R-AST-04 | Singleton estático (`Game.instance`) y métodos estáticos (`Game.GameOver()`) acoplan toda la lógica | `Game.cs:46-65` | VERIFICADO |
| R-AST-05 | Disparo continuo mientras se mantiene `Space`, con cadencia fija de 0,4 s | `Ship.cs:61-64, 88` | VERIFICADO |
| R-AST-06 | El ancho visible depende de la relación de aspecto: con `orthographic size 5` el semiancho visible es 5×aspect (≈6,7 en 4:3, ≈8,9 en 16:9). Los asteroides aparecen en ±8, así que en 4:3 o en retrato algunos aparecerían fuera de pantalla | `Game.prefab`, `Spawner.cs:103` | Cálculo VERIFICADO; percepción en juego UNKNOWN (la cámara podría estar rotada) |

### 1.3 Análisis de jugabilidad en PC

| Pregunta | Respuesta | Estado |
|---|---|---|
| Acciones del jugador | Moverse horizontalmente, disparar e iniciar o reiniciar la partida | VERIFICADO (código) |
| Controles | `←`/`→` para moverse, `Space` (mantener) para disparar y clic en "Start" | VERIFICADO (código) |
| Información para decidir | Posición de los asteroides que caen, puntaje y estado (título o Game Over) | VERIFICADO (código) |
| Objetivo | Sobrevivir y sumar puntos (+1 por asteroide destruido). No hay meta final, niveles ni récord guardado | VERIFICADO (código) |
| Éxito | Destruir asteroides con el láser | VERIFICADO (código) |
| Fracaso | Un único choque con la nave termina la partida (no hay vidas) | VERIFICADO (código) |
| Error | Asteroides que salen por abajo sin consecuencia; no penalizan | VERIFICADO (código: `Asteroid.cs:46-49`) |
| Dificultad del control | Velocidad constante sin aceleración; spawn constante cada 0,4 s sin curva de dificultad | VERIFICADO (código). Sensación al jugar: UNKNOWN |
| Interfaz que facilita o dificulta | Texto legacy sin escalado por alto (`match 0`); no hay indicación de controles en pantalla | VERIFICADO (configuración). Legibilidad real: UNKNOWN |
| A comprobar ejecutando | Ritmo y justicia del spawn, visibilidad en distintas relaciones de aspecto, R-AST-01 a R-AST-03, feedback de audio | UNKNOWN |

---

## 2. P2 2D Platformer

Ruta: `C:\Developer\unity\2026\clases-en-vivo\proyectos-unity\2D-Platformer-Unity-main`

### 2.1 Procedencia y migración (importante)

| Hecho | Estado | Evidencia |
|---|---|---|
| El ZIP original (`proyectos-unity\2D-Platformer-Unity-main.zip`) declara `m_EditorVersion: 2022.3.13f1` | VERIFICADO | EV-020 |
| La carpeta actual declara `6000.3.11f1`: el proyecto **ya fue migrado** a Unity 6 el 10/10/2026 a las 16:13, antes de esta auditoría y no por ella | VERIFICADO | EV-009, EV-021 |
| `Logs/Packages-Update.log`: actualizó Cinemachine 2.9.7→2.10.6, URP 14.0.9→17.3.0, Test Framework 1.1.33→1.6.0, uGUI 1.0.0→2.0.0 y Visual Scripting 1.9.1→1.9.10, entre otros; **eliminó** `com.unity.textmeshpro@3.0.6`, que en Unity 6 queda integrado en uGUI 2.0 | VERIFICADO | EV-021 |
| El API Updater de Unity **modificó** `Assets/Scripts/PlayerController.cs` (`Rigidbody2D.velocity` → `linearVelocity`). El ZIP conserva `rb.velocity` | VERIFICADO | EV-022 |
| Licencia del código: MIT, "Copyright (c) 2023 Hasan" (`LICENSE`) | VERIFICADO | EV-020 |
| Licencia del arte (`Assets/cat`, `Assets/dog`, `Assets/png`, tiles) | UNKNOWN (no hay archivo de licencia) → DEC-LAB-013 | EV-020 |

### 2.2 Inventario técnico

| Aspecto | Hallazgo | Estado | Evidencia |
|---|---|---|---|
| Versión de Unity | `6000.3.11f1` (migrado desde 2022.3.13f1) | VERIFICADO | EV-009 |
| Identidad | `productName: 2D platformer`, `applicationIdentifier` solo para Standalone (`com.DefaultCompany.2D-platformer`) | VERIFICADO | EV-010 |
| Escenas y build | `Assets/Scenes/Menu.unity` (índice 0) y `Assets/Scenes/Level.unity` (índice 1). Hay además una plantilla `Assets/Settings/Scenes/URP2DSceneTemplate.unity` que no está en el build | VERIFICADO | EV-010 |
| Flujo de navegación | Menú (Play/Quit) → Level → al morir, fundido y **recarga de la escena 1** → al tocar `LevelCompleteTrigger`, fundido y panel "LEVEL COMPLETE" con monedas X/Total y botones Menu/Quit. `Events.cs` carga las escenas **por índice** | VERIFICADO (estático) | EV-011, EV-012 |
| Prefabs | `IceBox`, `Pickup/dollar`, `PickupEffect1`, `PickupEffect2`, `Sign_2`, `SnowMan`, `Tree_1`, `Tree_2`, `Objects/Objects`, `Objects/Tree_1`, `Tilemap/Tiles` | VERIFICADO | EV-001 |
| Scripts | `PlayerController`, `GameManager`, `HealthManager`, `UIManager`, `pickup`, `ExitTrigger`, `Events` (Assembly-CSharp, sin asmdef) | VERIFICADO | EV-011 |
| Paquetes | URP 17.3.0 (2D Renderer, `Light 2D`), Cinemachine 2.10.6, `com.unity.feature.2d` 2.0.2, uGUI 2.0.0 (incluye TMP), Visual Scripting 1.9.10, Test Framework 1.6.0. **Sin Input System** | VERIFICADO | EV-009 |
| Render | URP con espacio de color **Linear** | VERIFICADO | EV-010 |
| Sistema de entrada | `activeInputHandler: 0` (Input Manager clásico). Usa los ejes `Horizontal` y `Jump` y el botón `Fire1`. El `InputManager.asset` incluye ejes de joystick por defecto (`Horizontal` tipo 2 y `Jump` con botón de joystick), así que el **gamepad probablemente funciona** para moverse y saltar | Configuración VERIFICADA; comportamiento con un gamepad real: **UNKNOWN** | EV-010, EV-013 |
| Modo de control | `public enum Controls { mobile, pc }`. En `Level.unity`, `controlmode: 1` (pc). Existen `MobileMove(float)`, `MobileJump()` y `MobileShoot()` | VERIFICADO | EV-011, EV-014 |
| **Controles táctiles** | El GameObject `MobileControls` existe en `Level.unity`, pero está **vacío**: `m_Children: []`, 100×100 sin componentes visuales. Ningún UnityEvent de las escenas invoca `MobileMove`, `MobileJump` ni `MobileShoot`. **La API móvil existe, pero no hay UI táctil** | VERIFICADO | EV-014 |
| Mecánicas | Movimiento horizontal (`moveSpeed 5`), salto (`jumpForce 10`) y **doble salto** (`doubleJumpForce 8`), suelo detectado por raycast (0,25) contra la capa `ground`, partículas de pasos e impacto | VERIFICADO (código) | EV-011 |
| Disparo | `Shoot()` está **vacío** (código comentado). Además se calcula un ángulo hacia el mouse que no se usa | VERIFICADO | EV-011 |
| Vida | `HealthManager`: 6 puntos y 3 corazones con medios corazones. **Ningún script ni UnityEvent llama a `HurtPlayer()`**: los corazones son decorativos en el estado actual | VERIFICADO (búsqueda estática en scripts y escenas) | EV-011, EV-012 |
| Muerte | Solo por colisión con el tag `killzone`. Fundido a negro y recarga de la escena, con pérdida de las monedas | VERIFICADO (código) | EV-011 |
| Pickups | `coin` suma y se muestra en el HUD. `gem` suma, pero **no se muestra**. `health` está en el enum **sin comportamiento** | VERIFICADO | EV-011 |
| Cámara | Cinemachine Virtual Camera que sigue al Player, con confiner (`CameraBounds`) y `OrthographicSize 10` | VERIFICADO | EV-015 |
| Animación | `Assets/dog/Animations/sr.controller` con parámetros `run` y `jump` (y estados idle/run/walk/fall/Jump). El código también setea `isGrounded`, que **no existe** en el Animator | VERIFICADO (asset + log, ver 2.4) | EV-016, EV-017 |
| HUD | TextMeshPro (monedas, panel de nivel completado), corazones `Image` y fundido (`blackScreen`). CanvasScaler: Scale With Screen Size 1920×1080, `match 0.5`. Tamaños de fuente de 36 a 87 | VERIFICADO | EV-018 |
| Navegación con gamepad en el menú | Botones con `Navigation: Automatic` (modo 3), pero `EventSystem.m_FirstSelected: {fileID: 0}`: ningún botón recibe foco al cargar | VERIFICADO (configuración). Efecto real con gamepad: UNKNOWN | EV-018 |
| Pausa | Existe el campo `isPaused`, pero no hay UI ni lógica de pausa | VERIFICADO | EV-011 |
| Guardado | No hay (ni `PlayerPrefs` ni archivos) | VERIFICADO (búsqueda estática) | EV-011 |
| Rendimiento | `Application.targetFrameRate = 60` en `GameManager.Awake()`. Calidad por defecto: Android "Medium" (índice 2), Standalone "Ultra" | VERIFICADO | EV-010, EV-011 |
| Resolución y orientación | 1920×1080, Auto Rotation con las cuatro orientaciones permitidas (incluye retrato), `androidRenderOutsideSafeArea: 1`, `androidUseSwappy: 1` | VERIFICADO | EV-010 |
| Android (config actual) | `AndroidMinSdkVersion: 25`, `AndroidTargetSdkVersion: 0`, **`AndroidTargetArchitectures: 1` (solo ARMv7, 32 bits)** y `scriptingBackend: {}` (por defecto, Mono) | VERIFICADO (valores). Ver el riesgo R-PLT-05 | EV-010 |
| Tests | No hay carpeta de tests ni asmdef de tests | VERIFICADO | EV-001 |

### 2.3 Riesgos técnicos

| ID | Riesgo | Estado |
|---|---|---|
| R-PLT-01 | El Animator no tiene el parámetro `isGrounded`: el error se repite en cada frame (2447 veces en una sesión) y la transición de caída/aterrizaje no se controla desde el código | VERIFICADO (EV-017) |
| R-PLT-02 | El sistema de vida y daño está desconectado (`HurtPlayer` no tiene llamadas) | VERIFICADO (estático) |
| R-PLT-03 | El modo móvil está a medio implementar: el contenedor está vacío y no hay botones | VERIFICADO |
| R-PLT-04 | Hay APIs obsoletas en Unity 6: `FindObjectOfType` y `FindObjectsOfType` (advertencias CS0618 en la compilación) | VERIFICADO (EV-017) |
| R-PLT-05 | Arquitectura Android solo ARMv7. Google Play exige 64 bits, y en Unity eso implica IL2CPP. Hoy no es publicable en Play sin cambiar `ProjectSettings` | Configuración VERIFICADA; el requisito de 64 bits de Play no se consultó en esta sesión (UNKNOWN, hay que verificarlo con la fuente oficial) |
| R-PLT-06 | Escenas cargadas por índice; las referencias se cruzan entre singletons (`GameManager.instance`, `UIManager.instance`, `HealthManager.instance`) | VERIFICADO |
| R-PLT-07 | En PC, el salto inicial se lee en `Update` solo si está en suelo, y el doble salto en el aire. El movimiento horizontal se lee en `Update` (en suelo) y en `FixedUpdate` (siempre) | VERIFICADO; la sensación de control es UNKNOWN |
| R-PLT-08 | El proyecto no está bajo control de versiones y ya fue modificado por la migración: no hay forma de volver atrás salvo con el ZIP | VERIFICADO → DEC-LAB-003 |

### 2.4 Evidencia de ejecución existente (no generada por esta auditoría)

`%LOCALAPPDATA%\Unity\Editor\Editor.log` (última modificación: 10/10/2026 16:27) registra una sesión del Editor con este proyecto (EV-017):
- **Compilación sin errores**: solo advertencias CS0618.
- Una sesión de Play Mode: 2447 mensajes `Parameter 'isGrounded' does not exist.` (`PlayerController.cs:141`) y un mensaje `Died` (`GameManager.cs:86`). Se ejecutó la ruta de muerte por `killzone`.
- **Límite**: el log prueba que se ejecutó, **no** que el nivel se pueda completar ni que el control resulte satisfactorio.

### 2.5 Análisis de jugabilidad en PC

| Pregunta | Respuesta | Estado |
|---|---|---|
| Acciones | Correr, saltar, doble salto, recoger monedas y gemas, llegar a la salida | VERIFICADO (código) |
| Controles | `←`/`→` o `A`/`D` (eje Horizontal), `Space` para saltar, posible gamepad. `Fire1` (Ctrl o clic) no hace nada visible | VERIFICADO (configuración y código); gamepad UNKNOWN |
| Información necesaria | Plataformas y vacíos (killzone), monedas restantes, corazones (hoy sin función) | VERIFICADO (escena); la visibilidad real es UNKNOWN |
| Objetivo | Alcanzar `LevelCompleteTrigger`; objetivo secundario: monedas X/Total | VERIFICADO (código) |
| Éxito | Panel "LEVEL COMPLETE" con conteo de monedas | VERIFICADO (código) |
| Fracaso | Caer o tocar la killzone: reinicio completo del nivel | VERIFICADO (código) |
| Dificultad del control | Doble salto con fuerzas fijas y sin coyote time ni buffer de salto | VERIFICADO (código); la percepción es UNKNOWN |
| Interfaz | Contador de monedas; corazones que no cambian (pueden **engañar** al jugador) | VERIFICADO (estático) |
| A comprobar ejecutando | Completitud del nivel, legibilidad de los vacíos, comportamiento del gamepad, efecto visual de R-PLT-01 | UNKNOWN |

---

## 3. Comparación final

| Dimensión | P1 Asteroides | P2 2D Platformer |
|---|---|---|
| Unity | 6000.3.11f1 | 6000.3.11f1 (migrado hoy desde 2022.3.13f1) |
| Versionado | git (repo `clases-en-vivo`) | Sin versionar |
| Licencia del código | Kodeco: **prohíbe el uso pedagógico** | MIT |
| Género y vista | Shooter vertical de arcade, 3D con cámara ortográfica | Plataformas 2D side-scroller con tilemap |
| Render | Built-in, Gamma | URP 2D, Linear |
| Entrada | Teclas fijas por `KeyCode`: **no** admite gamepad sin cambios de código | Ejes del Input Manager: admite gamepad con probabilidad (UNKNOWN) |
| Preparación móvil | Ninguna | API `Mobile*` en el código; UI táctil inexistente |
| Acciones simultáneas | Mover + disparar (continuo) | Mover + saltar (pulsación con ventana temporal) |
| Exigencia de precisión | Posicionamiento horizontal | Timing de salto y doble salto |
| Tests | 11 tests (UNKNOWN si pasan) | Ninguno |
| Bugs conocidos | Pool incoherente (hipótesis con tests) | Parámetro de Animator faltante (verificado), vida desconectada |
| Orientación natural | Probablemente **vertical** (los objetos caen en Y) → DEC-LAB-005 | **Horizontal** |
| Guardado | No | No |

**Conclusión del diagnóstico:** los dos juegos **no** requieren las mismas adaptaciones. P1 necesita primero desacoplar la entrada del código, porque las teclas están cableadas en `Ship.Update()`. P2 ya tiene la abstracción mínima (`controlmode` + `Mobile*`) y le falta la capa de UI y la corrección de errores existentes. Antes de cualquier trabajo sobre P1 hay que resolver su **restricción de licencia** (DEC-LAB-002).
