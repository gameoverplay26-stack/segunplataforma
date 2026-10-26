# Unidad 4 — Caso práctico: llevar "nave + asteroides" a móvil

Proyecto: `proyectos-unity/Asteroides/asteroide-final/` (Unity 6000.3.11f1). Es el mismo juego base que la clase del 28/09/2026 usó para presentar las plataformas, y el mismo que tiene la suite de tests de integración de la Unidad 3 (`Assets/Tests/`).

## Por qué este caso, y no Cryptbound

Las Unidades 2 y 3 usaron **Cryptbound**, un caso **narrativo** que nunca se construyó como juego. Para hablar de plataformas hace falta **código y escenas reales** que se puedan abrir, medir y compilar para Android, y la clase del 28/09 ya instaló Asteroides como juego base de las Unidades IV–VII. Se mantiene esa continuidad. Cryptbound no se abandona: puede reaparecer como contraejemplo, porque un dungeon-crawler tiene otro ritmo de sesión. Pero no es el laboratorio.

> Advertencia: este Asteroides (Crashteroids, Unity Learn) **no** es el proyecto SDD "Asteroid Survival" de `docs/00-discovery/…`. Son proyectos separados.

---

## 1. Inventario de supuestos de PC que el código ya trae

Todos los datos se verificaron leyendo el proyecto el 2026-10-05.

| # | Supuesto en el código o la configuración | Dónde | Qué pasa en móvil | Eje |
|---|---|---|---|---|
| S1 | Input leído directamente del teclado: `Input.GetKey(KeyCode.Space / LeftArrow / RightArrow)` | `Assets/Scripts/Ship.cs:61-73` | No hay teclado. Hay que cambiar la clase `Ship` para poder jugar | Input |
| S2 | El proyecto usa el **Input Manager clásico** (`activeInputHandler: 0`) | `ProjectSettings/ProjectSettings.asset:872` | `Input.touches` es legacy; Unity lo desaconseja para proyectos nuevos (B-36) | Input |
| S3 | Límites de la nave **fijos** en ±40 (coordenadas **locales**), sin relación con la cámara ni con el aspect ratio. `MoveLeft` traslada con `-Vector3.left` (+x local) y limita en `maxLeft = 40`: que "izquierda" sea +x depende de la orientación del modelo y la cámara. *Corrección del 2026-10-05: en la versión anterior se afirmó que los nombres estaban "invertidos"; no está demostrado y se retira.* Qué rango de pantalla representan ±40 **se confirma en la demo** con el Device Simulator | `Ship.cs:46-47, 99-115` | En otro aspect ratio la nave puede quedar parcialmente fuera de la vista, o no llegar al borde | Pantalla |
| S4 | Cámara **ortográfica, tamaño 5**. El semiancho visible es `5 × aspect`: ≈ 8,9 a 16:9, pero ≈ **2,8 en vertical 9:16** | `Resources/Prefabs/Game.prefab` (Camera) | — | Pantalla |
| S5 | El Spawner genera asteroides en `x ∈ [−8, 8]`, asignado a `transform.position` (coordenadas de **mundo**, verificado) | `Assets/Scripts/Spawner.cs:101-106` | En vertical, **la mayoría de los asteroides aparecería fuera de pantalla** (S4). El juego "funciona" pero el diseño se rompe. *Supuesto a confirmar en la demo:* la cámara está centrada en x = 0 | Pantalla / gameplay |
| S6 | Canvas del prefab `Game` en **Constant Pixel Size** (`m_UiScaleMode: 0`), referencia 800×600. La escena `Game.unity` instancia solo ese prefab. Existe un `UICanvas.prefab` con Scale With Screen Size 1920×1080, pero **no está en la escena** | `Resources/Prefabs/Game.prefab:5225`, `Scenes/Game.unity:223` | En pantallas de alta densidad, el texto de score y el botón de inicio quedan diminutos | UI |
| S7 | La partida se inicia con un **botón de UI pensado para clic** | `Game.cs:40, 54, 67` | En táctil funciona, pero hay que verificar tamaño ≥ 44 pt / 48 dp y posición respecto de la safe area | UI / accesibilidad |
| S8 | **No hay pausa ni manejo del ciclo de vida.** No existe `OnApplicationPause` ni `OnApplicationFocus` en ningún script | `Assets/Scripts/*.cs` (búsqueda sin resultados) | Llega una llamada, el jugador vuelve y la nave ya explotó; o el SO mata el proceso y se pierde el estado | Ciclo de vida |
| S9 | Cada disparo hace `Instantiate(laser)` (sin pool), con una cadencia de 0,4 s | `Ship.cs:85, 92-97` | Genera basura (GC) y picos de frame; en móvil se notan más | Rendimiento |
| S10 | `Spawner` declara un `ObjectPool` que nunca usa con `Get()` (defecto ya documentado en INT-AST-13/14) | `Spawner.cs:38, 52` | Mismo riesgo que S9, más los defectos de integración ya conocidos | Rendimiento / calidad |
| S11 | `defaultScreenOrientation: 4` (AutoRotation) | `ProjectSettings.asset:11` | Si el jugador gira el teléfono, el juego pasa a vertical y se cumplen S4/S5 | Pantalla |
| S12 | No hay `Application.targetFrameRate`; en Android e iOS, Unity renderiza a **30 fps** por defecto (B-01). La calidad por defecto en Android es el nivel 2 (Medium) | `QualitySettings.asset:177-190` | Es una decisión de diseño que nadie tomó explícitamente | Rendimiento / batería |
| S13 | Built-in Render Pipeline (`m_CustomRenderPipeline: {fileID: 0}`) y Quality Settings de plantilla, con plataformas obsoletas (3DS, PSP2, WiiU) | `GraphicsSettings.asset:43`, `QualitySettings.asset` | Algunas técnicas de Unity 6 (GPU Resident Drawer, STP) son solo de URP/HDRP: no aplican sin migrar | Rendimiento |

**Uso didáctico:** el inventario **no se entrega resuelto**. En la Clase 1 los estudiantes reciben solo la pregunta "¿qué supuestos de PC tiene este juego?" y el código. La tabla es la respuesta esperada del docente (ver `05`, actividad A4.2).

---

## 2. Decisiones de diseño que el caso obliga a tomar

| Decisión | Alternativas | Criterio para elegir | Fuente del criterio |
|---|---|---|---|
| Orientación | Horizontal fija / vertical fija / ambas | Una mano o dos; campo visual; S4–S5. Android 16 exceptúa a los juegos (Application Category = Game) | B-24, B-25 |
| Control de movimiento | Joystick virtual / arrastrar el dedo / tocar mitad izquierda o derecha / inclinar (giroscopio) | Oclusión por el pulgar; precisión; accesibilidad (alternativa a gestos); descubribilidad | B-18, B-58, B-35 |
| Disparo | Botón / autodisparo / tocar para disparar | Carga cognitiva con dos pulgares; Vampire Survivors reduce el control a "moverse" | Clase 28/09 slide 8; dato E-41 |
| Límites de juego | Derivar los límites de `Camera.orthographicSize × aspect` / fijar el aspect con letterbox | Justicia entre dispositivos: ¿todos ven la misma porción del mundo? | Inferencia docente, a discutir |
| HUD | Scale With Screen Size + anclas + safe area | 44 pt / 48 dp; texto legible | B-02, B-15, B-21, B-32 |
| Interrupciones | Pausa automática + "tocar para continuar" / solo pausar | No castigar al jugador por algo que el SO hizo | B-37, B-38 |
| Rendimiento | 30 fps estables vs. 60 fps con riesgo térmico | Rendimiento sostenido, batería, tipo de juego (acción simple) | B-01, e-book p. 19 |
| Monetización | Premium / rewarded "continuar" / interstitial en Game Over / IAP | Políticas (AdMob, 3.1.1), ética y efecto sobre la dificultad | B-46–B-55 |

---

## 3. El defecto deliberado de la unidad: "la llamada que mata la nave"

Mantiene la filosofía de la Unidad 3: código con un defecto, escribir el test, encontrar el fallo, corregir, volver a correr y dejar un test de regresión.

**Escenario (S8):** el jugador está en partida, entra una llamada o cambia de app, vuelve a los 20 segundos y encuentra la nave destruida y el score perdido.

**Qué se le pide al estudiante** (detalle y rúbrica en `05`, A4.4):
1. Diseñar el comportamiento esperado: pausa automática, overlay "Tocá para continuar" y no reanudar sola.
2. Separar la **regla** (un objeto C# puro, por ejemplo `PauseState`, que decide si el juego está pausado) del **adaptador** de Unity (un `MonoBehaviour` que recibe `OnApplicationPause(bool)` y llama a la regla). Es la misma idea de "intención vs. dispositivo" de la clase del 28/09, aplicada al sistema operativo.
3. Escribir:
   - **un test de Edit Mode** sobre la regla, por ejemplo "si llega `pause=true` en partida, queda pausado; si llega `pause=false`, sigue pausado hasta que el jugador toque";
   - **un test de Play Mode** que invoque el callback del adaptador y verifique que `Time.timeScale == 0` y que la nave no recibió daño.
4. Ejecutar la versión con el defecto (el docente entrega una implementación que **reanuda sola** al volver), ver el test en rojo, corregir y dejarlo como regresión.
5. **Declarar los límites del test**, que es la parte que más se evalúa:
   - El test llama al callback a mano. **No demuestra** que Android o iOS lo invoquen en el momento esperado. Por ejemplo: el teclado en pantalla dispara `OnApplicationFocus(false)` en Android (B-37), y si el SO mata el proceso no se llama nada.
   - Eso **solo** se comprueba con QA manual en un dispositivo real: recibir una llamada, cambiar de app, bloquear la pantalla y forzar el cierre desde las opciones de desarrollador.

> El código del defecto y de la solución **no está implementado todavía** en `proyectos-unity/Asteroides/asteroide-final/`. Implementarlo (rama propia y validación en batch mode, como en U3) figura como tarea pendiente en `diseno-plataformas/status-unidad.md`. No se presenta como hecho.

---

## 4. Hipótesis de rendimiento para medir (no para afirmar)

| Hipótesis | Métrica | Herramienta | Qué no sirve |
|---|---|---|---|
| H1: `Instantiate` por disparo genera picos de GC (S9) | GC Alloc por frame; picos de frame time | Unity Profiler conectado a un Development Build en el teléfono (B-31) | Device Simulator: no simula rendimiento (B-04) |
| H2: el juego sostiene 30 fps, pero ¿sostiene 60? ¿Y después de 10 minutos? | Frame time a lo largo del tiempo; temperatura y estado térmico | Profiler en dispositivo; partidas de 10 min o más | Medir solo el minuto 1 |
| H3: las transparencias de la explosión generan overdraw | Tiempo de GPU en la escena de explosión | Profiler / Frame Debugger; AGI como mención (B-60) | El editor en una PC con GPU de escritorio |

Es un caso **muy liviano** a propósito: lo más probable es que Asteroides corra bien en casi cualquier teléfono. El objetivo es aprender **a formular y medir** hipótesis, no encontrar un problema dramático. Si la medición no muestra nada, esa es la respuesta correcta y hay que decirlo así.

---

## 5. Qué parte del caso es automatizable y cuál requiere hardware real

| Riesgo | Prueba principal | ¿Automatizable? | ¿Requiere dispositivo real? |
|---|---|---|---|
| Lógica de pausa (regla) | Unitaria (Edit Mode) | Sí | No |
| Adaptador de pausa + nave + spawner | Integración (Play Mode) | Sí | No |
| El SO dispara el callback correcto (llamada, home, teclado) | QA manual | No (o muy costoso) | **Sí** |
| Límites y spawn en 16:9, 19.5:9, 4:3 y vertical | Compatibilidad visual (Device Simulator) + Play Mode parametrizado por aspect | Parcialmente | Recomendable, para confirmar |
| HUD dentro de la safe area | Device Simulator (B-04) | Parcial (inspección) | Recomendable |
| Tamaño de los botones ≥ 44 pt / 48 dp | Inspección + medición | Parcial | Sí, para la ergonomía real |
| ¿Se juega cómodo con una mano? | Usabilidad / playtesting | No | **Sí** |
| fps sostenido y temperatura | Rendimiento | Parcial (logging) | **Sí** |
| Consumo de batería | Rendimiento | No | **Sí** |
| Distintas GPU y fabricantes | Compatibilidad | Granja en la nube (Firebase / AWS, costo o cuota) | **Sí** |

Este cuadro es la versión móvil del criterio "qué merece automatizarse" de la Unidad 3.

**Revisión del 2026-10-05:** como los estudiantes tienen teléfono Android, todas las filas marcadas "Sí" o "Recomendable" en la columna de dispositivo real **se ejecutan** en la Clase 4 sobre sus teléfonos (build de desarrollo, Profiler y QA manual). iOS queda fuera de la práctica (no hay Mac): cualquier conclusión sobre iOS es conceptual y debe decirse así en el dossier.
