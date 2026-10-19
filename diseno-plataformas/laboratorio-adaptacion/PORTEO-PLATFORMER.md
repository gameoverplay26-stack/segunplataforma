# PORTEO-PLATFORMER: registro de la versión 2 (porteo a móvil)

- **Proyecto nuevo:** `proyectos-unity/2D-Platformer-Unity-v2/`, una copia de P2. El original (`2D-Platformer-Unity-main/`, línea base `e766f8c`) **no se tocó**.
- **Fecha:** 2026-10-19 · **Unity:** 6000.3.11f1 · **Rama:** `main` (sin commit).
- **Autorización:** DEC-LAB-006 (Input System). Se aplicó el mismo patrón que en P1 (`PORTEO-ASTEROIDES.md`).
- **Propuestas que implementa:** MOB-PLT-01 (UI táctil), MOB-PLT-02 (modo de control según la plataforma), MOB-PLT-04 (solo el error de `isGrounded`), MOB-PLT-05 (solo la safe area) y MOB-PLT-06 (orientación horizontal).
- **No implementa (siguen pendientes):** MOB-PLT-03, coyote time y buffer de salto (DEC-LAB-007); IL2CPP + ARM64 (DEC-LAB-014); corazones y vida (R-PLT-02); cámara en móvil (resto de MOB-PLT-05); rendimiento (MOB-PLT-07); pausa y ciclo de vida (MOB-PLT-08).

## 1. Diseño: dispositivo → intención → jugador

| Capa | Archivo | Responsabilidad |
|---|---|---|
| Dispositivo | `Assets/Scripts/PlayerInputAdapter.cs` (nuevo) | Dos `InputAction` definidas en código. **Move**: flechas y A/D como composite 1DAxis, `<Gamepad>/leftStick/x` y `<Gamepad>/dpad/x`. **Jump**: `<Keyboard>/space` y `<Gamepad>/buttonSouth`. Cada frame llama a `player.SetIntent(dir, saltoPresionado)`. Usa `[DefaultExecutionOrder(-10)]` para que el salto se aplique en el mismo frame |
| Táctil | `Level.unity` → `Canvas/MobileControls`: `LeftButton` (`<Gamepad>/dpad/left`), `RightButton` (`<Gamepad>/dpad/right`) y `JumpButton` (`<Gamepad>/buttonSouth`), todos `OnScreenButton` | Gamepad virtual: el adaptador no distingue el dedo de un gamepad físico (SRC-016). Mantener ◀ mueve de forma continua; al soltar, el jugador se detiene (MOB-PLT-01) |
| Visibilidad | `UIManager.ShouldShowMobileControls` | `UnityEngine.Device.Application.isMobilePlatform`, que respeta el Device Simulator, o `forceMobileControls` para probar en el Game view. Reemplaza el enum `Controls` y el campo `controlmode` fijado en la escena (MOB-PLT-02) |
| Safe area | `Assets/Scripts/SafeAreaFitter.cs` (nuevo), en `MobileControls` | Ajusta el contenedor a `UnityEngine.Device.Screen.safeArea` |
| Intención | `Assets/Scripts/PlayerController.cs` (modificado) | `SetIntent(float, bool)`. El salto queda como pedido y se consume en el `Update` siguiente (sin buffer). La lógica de salto y doble salto es la original, unificada en `TryJump()` |

Decisiones técnicas (distintas de P1, con su motivo):
- **Active Input Handling = Input System Package (New)**, no "Both". Unity 6.3 declara "Both" no soportado en Android (ver §4.1 de `PORTEO-ASTEROIDES.md`). Para usar "New" solo, los `EventSystem` de `Menu` y `Level` pasaron de `StandaloneInputModule` a `InputSystemUIInputModule`.
- **Botones ◀ ▶ en lugar de joystick**, que es la primera opción de MOB-PLT-01. Sigue siendo **provisional** (DEC-LAB-007). Para cambiar a stick basta con reemplazar los dos botones por un `OnScreenStick` en `<Gamepad>/leftStick`: el adaptador ya lo lee.
- Movimiento **digital** (signo con zona muerta de 0,2), igual que en P1. **Cambio de sensación en PC:** `Input.GetAxis("Horizontal")` tenía suavizado (gravity/sensitivity), y ahora la respuesta es inmediata.
- Las escenas se modificaron con `Assets/Editor/PorteoSetup.cs` (idempotente, en batchmode), no a mano.

## 2. Archivos tocados (respecto del original)

| Archivo | Cambio |
|---|---|
| `Packages/manifest.json`, `packages-lock.json` | `com.unity.inputsystem` 1.19.0 (incluido en el editor) y `"testables": ["com.unity.inputsystem"]` para usar `InputTestFixture` |
| `ProjectSettings/ProjectSettings.asset` | `activeInputHandler: 0 → 1`; autorrotación a retrato desactivada (MOB-PLT-06); `productName: 2D platformer v2`; identificador Android `com.DefaultCompany.platformerv2`. El de Standalone (`…2D-platformer`) tiene un guion, que Android no acepta |
| `Assets/Scripts/PlayerController.cs` | Lectura de `Input.*` reemplazada por la intención. Se quitaron el código muerto del mouse (ángulo calculado y nunca usado), el disparo (el proyectil estaba comentado y `Shoot()` estaba vacío) y `MobileMove`/`MobileJump`. `isGrounded` solo se escribe si el Animator tiene ese parámetro (R-PLT-01) |
| `Assets/Scripts/UIManager.cs` | `forceMobileControls` y `ShouldShowMobileControls` |
| `Assets/Scripts/GameManager.cs` | `LevelComplete()` oculta los controles táctiles para que no tapen el panel final |
| `Assets/Scripts/PlayerInputAdapter.cs`, `SafeAreaFitter.cs`, `Game.asmdef` | Nuevos. El asmdef es necesario para que los tests referencien el código del juego |
| `Assets/Editor/PorteoSetup.cs`, `BuildAndroid.cs` | Nuevos (herramientas) |
| `Assets/Tests/EditMode/*`, `Assets/Tests/PlayMode/*` | Nuevos (§3) |
| `Assets/Scenes/Level.unity`, `Menu.unity` | Escritos por `PorteoSetup` (botones, adaptador, módulo de UI) |
| `Assets/TextMesh Pro/Resources/TMP Settings.asset` (y recursos TMP) | Se importaron los "TMP Essential Resources" de Unity 6 y `assetVersion: 2` (R-PLT-11) |
| `Assets/UniversalRenderPipelineGlobalSettings.asset` | `m_EnableRenderCompatibilityMode: 1 → 0` (R-PLT-10) |
| `DefaultVolumeProfile.asset`, `UniversalRP.asset`, `GraphicsSettings.asset`, `ShaderGraphSettings.asset`, `SceneTemplateSettings.json` | Reserialización automática de Unity 6 al abrir el proyecto; no son cambios funcionales |

## 3. Evidencia (batchmode, 2026-10-19)

Archivos en `evidencia/` con prefijo `platformer-v2-`. **Corridas finales:** `05-final-editmode.xml` y `05-final-playmode.xml`.

| Corrida | Total | Pasan | Fallan |
|---|---|---|---|
| Edit Mode (`MobileConfigTests`: input handler, orientación, id Android, módulo de UI en las 2 escenas, 3 botones y adaptador conectado) | 6 | 6 | 0 |
| Play Mode (`PlayerIntentTests`, `InputAdapterTests` con `InputTestFixture`, `OnScreenControlsTests`) | 10 | 8 | 2 |
| Build Android (`04-build-android.log`) | — | `[BuildAndroid] Succeeded` en 9 min 25 s (primera build); APK de 35,9 MB en `Builds/Platformer-v2.apk` (ignorado por git) | — |

Pasan, entre otros: teclado → se mueve; gamepad Sur → salta; **botón táctil ▶ mantenido → se mueve, y al soltarlo se detiene**; **botón táctil SALTAR → salta**. En la corrida final, el log de Play Mode tiene **0** apariciones de `Parameter 'isGrounded' does not exist` (antes eran 2447; EV-017) y 0 `error CS`.

Las **2 fallas** son un defecto real del juego original, no del porteo:
- `GroundRay_InMidAir_HitsNothing`: con el jugador 20 unidades sobre el suelo, el rayo de `IsGrounded()` golpea **`Player (CapsuleCollider2D)`, el propio jugador**.
- `SecondJumpIntent_InAir_DoubleJumpsOnlyOnce`: `IsGrounded()` queda en `true` durante todo el salto.

Correcciones al arnés de tests durante la sesión (las corridas 02 y 03 son intermedias):
- Los `OnScreenButton` no pueden convivir con `InputTestFixture`: al desactivarlos tras el reset del fixture, lanzan `ArgumentNullException: statePtr`. Por eso están en una clase sin fixture.
- Cada test deja una escena vacía (`LevelScene.Unload`) para no arrastrar dispositivos virtuales al test siguiente.

## 4. Hallazgos nuevos

| ID | Hallazgo | Estado |
|---|---|---|
| R-PLT-09 | **Salto infinito en el juego original.** `groundLayer` = capa *Default* (`m_Bits: 1`), el jugador está en *Default* y `Physics2D.queriesStartInColliders = 1`. El rayo nace dentro del propio `CapsuleCollider2D`, así que `IsGrounded()` siempre es verdadero y el doble salto nunca se usa. Corregirlo (poner el suelo en la capa `ground` o excluir al jugador) **cambia la dificultad del nivel**: decide el usuario | VERIFICADO (test). **No corregido** |
| R-PLT-10 | La migración a Unity 6 dejó URP en *Compatibility Mode*. Unity 6.3 **bloquea cualquier build** con `BuildFailedException` hasta desactivarlo. Afecta también al original | VERIFICADO (log). Corregido solo en v2 |
| R-PLT-11 | El `TMP Settings` del proyecto es del TMP de 2022 (sin `assetVersion`). Unity 6 intenta abrir el importador de TMP en cada Play, y en batchmode ese intento es un error que hace fallar los tests. Afecta también al original | VERIFICADO (log). Corregido solo en v2 |
| ENV-01 | **Rutas largas en Windows.** Con el repo en `C:\Users\Hilarion\Documents\2026\Videojuegos\2do cuatrimestre\segunplataforma`, la primera importación falla con `DirectoryNotFoundException` en `Library/PackageCache` (límite de 260 caracteres; `LongPathsEnabled = 0`). Se trabajó con `subst P: <...>\proyectos-unity`. Alternativas: clonar en la ruta corta recomendada en `CONTINUAR.md` o activar `LongPathsEnabled` (requiere administrador) | VERIFICADO |

## 5. Lo que esta evidencia NO demuestra (UNKNOWN)

- La instalación y el juego en un **teléfono real**. No se instaló el APK.
- La configuración Android sigue en **ARMv7 (32 bits)** (DEC-LAB-014): algunos teléfonos recientes solo de 64 bits podrían no instalarlo. Corrección del 2026-10-19: el backend es **IL2CPP** (valor por defecto de Unity 6 con `scriptingBackend` vacío; el log de build muestra `Prj/IL2CPP/Gradle`), no Mono como se había escrito. Falta solo agregar ARM64.
- El comportamiento en el **Device Simulator**. Que `UnityEngine.Device.Application.isMobilePlatform` sea verdadero allí es lo que indica la API, pero no se ejecutó de forma interactiva.
- El tamaño real en dp de los botones (220 y 280 unidades sobre 1920×1080, con match 0,5) y si tapan peligros del nivel (QA de MOB-PLT-05).
- Multitouch: mantener ▶ y tocar SALTAR a la vez. Los tests simulan un puntero por vez.
- El aspecto visual con render graph activado (R-PLT-10): los tests corren con `-nographics`.

## 6. Cómo reproducir

```bash
# Con Unity cerrado. Si la ruta del repo es larga, primero: subst P: "<repo>\proyectos-unity"
U="C:/Program Files/Unity/Hub/Editor/6000.3.11f1/Editor/Unity.exe"; P="P:/2D-Platformer-Unity-v2"
"$U" -batchmode -nographics -projectPath "$P" -executeMethod PorteoSetup.Apply -quit -logFile setup.log
"$U" -batchmode -nographics -projectPath "$P" -runTests -testPlatform EditMode -assemblyNames EditModeTests -testResults edit.xml -logFile edit.log
"$U" -batchmode -nographics -projectPath "$P" -runTests -testPlatform PlayMode -assemblyNames PlayModeTests -testResults play.xml -logFile play.log
"$U" -batchmode -nographics -projectPath "$P" -buildTarget Android -executeMethod BuildAndroid.Build -quit -logFile build.log
```

## 7. Pendientes

1. ~~Decisión sobre R-PLT-09~~: resuelta (DEC-LAB-015), ver §8.
2. Instalar el APK en un teléfono y completar el nivel solo con táctil (aceptación de MOB-PLT-01), con tiempo e intentos registrados.
3. Device Simulator: perfiles con y sin notch (safe area) y tamaño de los botones.
4. DEC-LAB-007 (botones o stick; coyote time y buffer), DEC-LAB-014 (IL2CPP + ARM64) y DEC-LAB-013 (licencia del arte, antes de distribuir el APK).
5. Decidir si R-PLT-10 y R-PLT-11 también se corrigen en el original.

## 8. Sonido, vidas y nivel 2 (2026-10-19, pedido del usuario)

Decisiones del usuario: **DEC-LAB-015** (corregir el salto infinito) y **DEC-LAB-016** (3 vidas; Game Over vuelve al nivel 1).

| Pedido | Implementación |
|---|---|
| Sonido (el proyecto no tenía audio: 0 archivos, 0 `AudioSource`) | `Tools/generar_sonidos.py` sintetiza 3 efectos de 8 bits propios, sin licencias de terceros: `Assets/Audio/sfx_moneda.wav`, `sfx_salto.wav` y `sfx_muerte.wav`. `Sfx.cs` los reproduce desde un objeto `Audio` por escena. El doble salto usa el mismo sonido con un tono más agudo |
| La vida no bajaba al morir | `GameSession.cs` (estático, sobrevive a la recarga): 3 vidas. `LivesHUD.cs` usa los 3 corazones existentes (`heart.png` = lleno, `heart (1).png` = vacío). `GameManager.Death()` resta una vida y recarga **el nivel actual** (antes, siempre `LoadScene(1)`). Con 0 vidas aparece `GameOverPanel` con "Retry" y "Menu" |
| Salto infinito (R-PLT-09) | `IsGrounded()` ignora los colliders del propio jugador y los triggers (monedas). `groundLayer` = Default + `ground`: el suelo real está en `ground`, y Default se mantiene por la IceBox |
| Nivel 2, más difícil | `Level2.unity`, generado por `GameplaySetup.cs` a partir del nivel 1. Mismo inicio; desde x = 3 hay 5 huecos de 5, 7, 5, 9 y 9 celdas (el nivel 1 tiene 2, de 6 y 4). El de 28-36 **exige doble salto** (un salto simple cubre unas 8 unidades y el doble, unas 11). Hay una plataforma flotante de 2 celdas en el hueco 45-53 y **3 enemigos que patrullan** (`PatrolEnemy.cs`, muñecos de nieve con la etiqueta `killzone`, a 2,5; 3,2 y 3,6 u/s) |
| Pasar de nivel | Botón "Next Level" en el panel de nivel completo. En el último nivel, el título dice "GAME COMPLETE!" y el botón se oculta |

Archivos nuevos: `Sfx.cs`, `GameSession.cs`, `LivesHUD.cs`, `PatrolEnemy.cs`, `Assets/Audio/*`, `Assets/Scenes/Level2.unity`, `Editor/GameplaySetup.cs`, `Editor/LevelDump.cs` (diagnóstico de solo lectura), `Tools/generar_sonidos.py` y los tests `GameSessionTests`, `Level2LayoutTests` y `GameplayTests`. Modificados: `PlayerController.cs`, `GameManager.cs`, `Events.cs`, `pickup.cs`, `BuildAndroid.cs` (las escenas salen de Build Settings), `Level.unity` y Build Settings (Menu, Level, Level2).

Evidencia: Edit Mode **15/15** y Play Mode **17/17** (`platformer-v2-07-*.xml`). Pasan, entre otros: morir resta una vida y vacía un corazón; con vidas, recarga el mismo nivel; la última muerte muestra GAME OVER; moneda, salto y muerte disparan su sonido; un enemigo del nivel 2 mata al jugador; el doble salto funciona una sola vez.

**UNKNOWN:**
- Que el sonido **se escuche**: los tests verifican que se pide el efecto correcto, porque el batchmode no tiene salida de audio. Hay que probarlo en el Editor y en el teléfono.
- Que el nivel 2 sea **completable y justo**: los huecos están dentro del alcance calculado, pero no se jugó de punta a punta.
- La sensación del nivel 1 con el salto corregido: ahora el doble salto importa, y el nivel puede sentirse más difícil que antes.
- Las monedas se reinician al perder una vida (comportamiento original al recargar la escena).

## 9. Abrir el proyecto y generar las builds (PC + Android)

- **Abrir en Unity desde `C:\Developer\unity\Platformer-v2`**, un junction a la carpeta del repo, sin administrador y permanente. Abierto desde la ruta larga, Unity falla con `DirectoryNotFoundException` en `Library\PackageCache` (ENV-01): eso le pasó al usuario el 2026-10-19. Si eso ocurre: cerrar Unity, borrar `Library\` y abrir desde la ruta corta.
- **Builds:** `powershell -ExecutionPolicy Bypass -File Tools\generar_builds.ps1`, con Unity cerrado. Genera `Builds\Platformer-v2.apk` (Android), `Builds\Windows\` (PC) y `Builds\Instaladores\Platformer-v2-Setup.exe` (Inno Setup 6: instala por usuario sin administrador, con acceso directo y desinstalador).
- Archivos: `Assets/Editor/BuildWindows.cs`, `Tools/instalador-windows.iss` y `Tools/generar_builds.ps1`.
