# PORTEO-ASTEROIDES: registro de implementación (entrada multiplataforma)

- **Proyecto:** `C:\Developer\unity\2026\clases-en-vivo\proyectos-unity\Asteroides\asteroide-final`
- **Fecha:** 2026-10-10 · **Unity:** 6000.3.11f1 · **Rama:** `main`, por pedido del usuario.
- **Autorización:** DEC-LAB-002 (modificar P1 para pruebas y clase), DEC-LAB-006 (instalar Input System). Ver `DECISIONS.md`.
- **Propuestas que implementa:** MOB-AST-01 (entrada desacoplada) y, de forma **provisional**, MOB-AST-02 (esquema joystick + botón; ver DEC-LAB-007).
- **Código original de referencia:** commit `e766f8c`. La slide 17 de la Clase 1 v3 lo lee de ahí.

## 1. Qué problema resuelve

`Ship.Update()` leía `Input.GetKey(KeyCode.Space/LeftArrow/RightArrow)` (EV-007). En un teléfono se puede tocar "Start" (uGUI), pero la nave no se mueve ni dispara. Tampoco respondía a un gamepad.

## 2. Diseño: dispositivo → intención → nave

| Capa | Archivo | Responsabilidad |
|---|---|---|
| Dispositivo | `Assets/Scripts/ShipInputAdapter.cs` (nuevo) | Define dos `InputAction`: **Move** (flechas como composite 1DAxis, `<Gamepad>/leftStick/x`, `<Gamepad>/dpad/x`) y **Fire** (`<Keyboard>/space`, `<Gamepad>/buttonSouth`). Cada frame llama a `ship.SetIntent(move, fire)` |
| Táctil | Prefab `Assets/Prefabs/UICanvas.prefab`: `MobileControls` → `StickBase/StickHandle` (`OnScreenStick`, `<Gamepad>/leftStick`, rango 100) y `FireButton` (`OnScreenButton`, `<Gamepad>/buttonSouth`) | Simulan un gamepad virtual: el adaptador no distingue el dedo de un gamepad físico (SRC-016) |
| Visibilidad | `Assets/Scripts/MobileControlsVisibility.cs` (nuevo) | Activa los controles solo si `Application.isMobilePlatform` |
| Intención | `Assets/Scripts/Ship.cs` (modificado) | `SetIntent(float horizontal, bool fire)`; `Update()` aplica la intención con una zona muerta de 0,2. `MoveLeft`, `MoveRight` y `ShootLaser` **no cambiaron** |

Decisiones técnicas:
- **Active Input Handling = Both** (`activeInputHandler: 2`). El menú sigue usando el `StandaloneInputModule` clásico; con "New" solo, ese módulo dejaría de funcionar.
- Acciones definidas **en código**, no en un asset `.inputactions`, para que el mapeo se lea en una sola slide y no haya que editar YAML.
- Movimiento digital (signo + zona muerta), igual que antes: un stick a medio recorrido mueve a la misma velocidad. Es una decisión de conservar el comportamiento, no de diseño definitivo.
- Los prefabs se modificaron con `Assets/Editor/PorteoSetup.cs`, ejecutado en batchmode e idempotente, en lugar de editar el YAML a mano.

## 3. Archivos tocados

| Archivo | Cambio |
|---|---|
| `Packages/manifest.json`, `packages-lock.json` | `com.unity.inputsystem` **1.19.0**, la versión incluida en el editor (`Editor/Data/Resources/PackageManager/Editor/com.unity.inputsystem-1.19.0.tgz`) |
| `ProjectSettings/ProjectSettings.asset` | `activeInputHandler: 0 → 2` |
| `Assets/Scripts/GameAssembly.asmdef` | Referencia a `Unity.InputSystem` |
| `Assets/Scripts/Ship.cs` | Lectura de teclas reemplazada por la intención |
| `Assets/Scripts/ShipInputAdapter.cs`, `MobileControlsVisibility.cs` | Nuevos |
| `Assets/Editor/PorteoSetup.cs` | Nuevo (herramienta de setup) |
| `Assets/Tests/ShipIntentTests.cs` | Nuevo: 3 tests de la intención, con el adaptador desactivado para aislar la nave |
| `Assets/Resources/Prefabs/Game.prefab` | `ShipInputAdapter` en `ShipModel`. El diff incluye campos que Unity 6 agrega al volver a serializar un prefab antiguo (`m_RootOrder`, parámetros de cámara física y otros); no son cambios funcionales |
| `Assets/Prefabs/UICanvas.prefab` | `MobileControls` con joystick y botón |

No se tocaron: escenas, `Asteroid.cs`, `Laser.cs`, `Spawner.cs`, `Game.cs`, la orientación (DEC-LAB-005 pendiente) ni la safe area (MOB-AST-04 pendiente).

## 4. Evidencia (Test Runner en batchmode, Play Mode)

Archivos en `diseno-plataformas/laboratorio-adaptacion/evidencia/`.

| Corrida | Archivo | Total | Pasan | Fallan | Fallas |
|---|---|---|---|---|---|
| Línea base, sin cambios | `asteroides-01-baseline-playmode.xml` | 11 | 7 | 4 | 3 hipótesis + `LaserMovesUp` |
| Después del porteo (1) | `asteroides-03-after-input-playmode.xml` | 14 | 10 | 4 | 3 hipótesis + `GameOverStopsSpawningAndDisablesShip` |
| Después del porteo (2) | `asteroides-03-after-input-playmode-run2.xml` | 14 | 11 | 3 | 3 hipótesis |
| Después del porteo (3) | `asteroides-03-after-input-playmode-run3.xml` | 14 | 10 | 4 | 3 hipótesis + `GameOverStopsSpawningAndDisablesShip` |
| Final (código con líneas acortadas para la slide) | `asteroides-04-final-playmode.xml` | 14 | 10 | 4 | 3 hipótesis + `GameOverStopsSpawningAndDisablesShip` |

Compilación: sin errores (`error CS` = 0 en los logs `asteroides-02b-setup.log` y `asteroides-04-final-playmode.log`). El primer intento de setup (`asteroides-02a-install-setup-error.log`) falló por un error del script de setup: accedía al objeto después de descargar el prefab. Se corrigió y se reejecutó; el script es idempotente.

**Interpretación:**
- Los **3 tests nuevos pasan en las 4 corridas**.
- Las **3 hipótesis de integración fallan siempre**, antes y después del cambio, por defectos reales del juego (R-AST-01, R-AST-02): un segundo `NewGame` acelera el spawn (9 asteroides en 2,1 s contra 6 o menos esperados); `NewGame` no borra los asteroides previos; y "Trying to release an object that has already been released to the pool" (`Laser.cs:52`).
- La **cuarta falla es inestable** y cambia de test entre corridas. Antes del porteo afectaba a `LaserMovesUp`; después, a `GameOverStopsSpawningAndDisablesShip`, y en una corrida no apareció. Su stack trace lleva al mismo defecto del pool: `Laser.OnCollisionEnter` (`Laser.cs:52`) → `ObjectPool.Release` → `Spawner.PlayExplosion` sobre un `AudioSource` destruido. **No** proviene del cambio de entrada.
- **Sin regresiones atribuibles al porteo**, dentro de lo que cubren estos tests.

## 5. Lo que esta evidencia NO demuestra (UNKNOWN)

- Que los controles táctiles funcionen en el **Device Simulator** o en un **teléfono**: no se ejecutó el juego de forma interactiva. Que `Application.isMobilePlatform` sea verdadero en el Device Simulator es un supuesto que hay que verificar en la demo.
- Mover y disparar con **dos dedos** a la vez: el Device Simulator simula un solo dedo; solo se prueba en el teléfono (QA-06 de la Clase 4).
- Tamaño real en dp de los controles (220 y 300 unidades de referencia sobre un Canvas de 1920×1080 que escala por ancho): hay que medirlo en el dispositivo (QA-07).
- Respuesta de un **gamepad físico**: no se probó.
- El adaptador no tiene test automático propio: requeriría el `InputTestFixture` de Input System, con dispositivos simulados. Candidato a integration test; queda pendiente.

## 6. Pendientes

1. Prueba manual en el Device Simulator y en un teléfono Android (ensayo de la docente antes de la Clase 4).
2. DEC-LAB-005 (orientación) y MOB-AST-03/04 (spawn según la cámara, safe area).
3. R-AST-01 (pool): no se corrige ahora, porque las hipótesis en rojo se usan en clase como evidencia. Decidir cuándo corregirlo.
4. Platformer: mismo patrón, en otra sesión.
