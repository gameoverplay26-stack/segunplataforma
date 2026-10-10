# MOBILE-ADAPTATION: propuesta de adaptación a celulares (fase 1)

- **Estado del documento:** PROPUESTO. No se modificó ningún archivo de los proyectos.
- **Plataforma de referencia:** Android (DEC-LAB-004). iOS queda fuera hasta que se decida.
- **Base:** `PROJECT-DISCOVERY.md` (evidencias `EV-###`) y fuentes oficiales (`SRC-###` en `EVIDENCE-LOG.md`).
- **P1 y licencia:** la licencia de Kodeco prohíbe el uso pedagógico. Por DEC-LAB-002 (RESOLVED), el usuario decidió modificar P1 solo para pruebas internas de porteo y para preparar las diapositivas de clase.

## 0. Decisiones transversales que condicionan ambos juegos

| Tema | Opciones | Recomendación | Decisión |
|---|---|---|---|
| Sistema de entrada | (a) Mantener el Input Manager clásico y agregar botones uGUI que llamen a métodos; (b) migrar al paquete **Input System** y usar `OnScreenStick`/`OnScreenButton` (SRC-006), que simulan un gamepad y unifican PC, móvil y Xbox | (b), porque sirve a la vez para la fase 2 (Xbox). Implica **instalar un paquete**, lo que requiere autorización explícita | DEC-LAB-006 |
| Backend y arquitectura Android | Mono/ARMv7 (actual) vs IL2CPP/ARM64 | IL2CPP + ARM64 si se piensa publicar o probar en dispositivos modernos. Hay que verificar el requisito de 64 bits de Google Play con la fuente oficial (UNKNOWN en esta sesión) | DEC-LAB-014 |
| Target API | `AndroidTargetSdkVersion: 0` (automático) | Desde el 31/08/2026, Google Play exige API 36 o superior para apps nuevas y actualizaciones (SRC-008). Solo importa si se publica; para APK de clase no aplica | DEC-LAB-014 |
| Safe area | `androidRenderOutsideSafeArea: 1` en ambos proyectos | Mantenerlo y ajustar el HUD con `Screen.safeArea` (SRC-004), o desactivarlo para que Unity ajuste la ventana | Técnica (se puede definir en la Technical Specification) |
| Tamaño táctil | — | Mínimo **48×48 dp** y separación de 8 dp o más (SRC-007) | — |

---

## 1. P1 Asteroides

Ruta: `C:\Developer\unity\2026\clases-en-vivo\proyectos-unity\Asteroides\asteroide-final`

### MOB-AST-01: entrada cableada a teclas
1. **Problema:** la nave solo responde a `LeftArrow`, `RightArrow` y `Space`; en un celular no hay forma de jugar.
2. **Evidencia:** `Assets/Scripts/Ship.cs:61-74` (EV-007), `activeInputHandler: 0` (EV-005).
3. **Cambio:** separar la lectura de entrada de la lógica de la nave. `Ship` ya expone `MoveLeft()`, `MoveRight()` y `ShootLaser()`, que pueden invocarse desde un adaptador de entrada (teclado, táctil o gamepad) sin duplicar el gameplay.
4. **Impacto:** el juego pasa a ser jugable en pantalla táctil; PC conserva el mismo comportamiento.
5. **Riesgo técnico:** medio. Los tests existentes llaman directamente a `MoveLeft`/`MoveRight` y `ShootLaser` y deben seguir pasando.
6. **Prioridad:** Alta (bloqueante).
7. **Aceptación:** en un dispositivo Android, el jugador mueve la nave y dispara sin teclado; en PC, el teclado funciona igual que antes.
8. **Validación:** suite existente en batchmode con XML de resultados, más una prueba manual en un dispositivo real con checklist.

### MOB-AST-02: esquema de control táctil
1. **Problema:** hay que elegir cómo moverse y disparar a la vez con los dedos.
2. **Evidencia:** el juego exige mover y disparar en simultáneo, con disparo continuo cada 0,4 s (`Ship.cs:61-64, 88`).
3. **Cambio (alternativas, decide el usuario en DEC-LAB-007):**
   - (a) Dos botones ◀ ▶ abajo a la izquierda y un botón de disparo abajo a la derecha (dos manos, en horizontal).
   - (b) Arrastre horizontal del dedo con **disparo automático** (una mano, en vertical).
   - (c) Tocar la mitad izquierda o derecha de la pantalla para moverse, con disparo automático.
4. **Impacto:** (b) y (c) reducen la carga motora y permiten jugar con una mano; (a) conserva la decisión de disparar.
5. **Riesgo:** bajo a medio. El disparo automático cambia el diseño: elimina la gestión del disparo.
6. **Prioridad:** Alta.
7. **Aceptación:** controles de 48 dp o más con separación de 8 dp o más (SRC-007); ninguna pulsación del área de juego dispara acciones del HUD.
8. **Validación:** prueba con 3 a 5 personas por esquema; registrar los errores de pulsación y la posición de los dedos.

### MOB-AST-03: orientación y campo visible
1. **Problema:** Auto Rotation con las cuatro orientaciones permitidas; el campo visible depende de la relación de aspecto y los asteroides aparecen en x ∈ [-8, 8].
2. **Evidencia:** `ProjectSettings.asset` (EV-005); `orthographic size 5` en `Game.prefab`; `Spawner.cs:103` (R-AST-06).
3. **Cambio:** fijar una orientación (DEC-LAB-005) y derivar el rango de spawn y los límites de la nave del ancho visible real de la cámara, en lugar de usar constantes.
4. **Impacto:** se evitan asteroides invisibles o imposibles de alcanzar.
5. **Riesgo:** medio. Interactúa con R-AST-03 (límites de ±40).
6. **Prioridad:** Alta.
7. **Aceptación:** en 16:9, 19.5:9 y 4:3, todo asteroide aparece dentro del área visible y la nave puede alcanzar cualquier X de spawn.
8. **Validación:** Device Simulator del Editor y un test de Play Mode que verifique el rango de spawn dentro de los límites de la cámara.

### MOB-AST-04: HUD y safe area
1. **Problema:** `UICanvas` escala solo por ancho (`match 0`) y usa `Text` legacy; con renderizado fuera de la safe area, el puntaje puede quedar bajo un notch.
2. **Evidencia:** `UICanvas.prefab` (EV-006), `androidRenderOutsideSafeArea: 1` (EV-005).
3. **Cambio:** contenedor del HUD ajustado a `Screen.safeArea` (SRC-004), `match` según la orientación elegida y botones de control fuera de la zona de juego.
4. **Impacto:** puntaje y botones siempre visibles.
5. **Riesgo:** bajo.
6. **Prioridad:** Media.
7. **Aceptación:** ningún elemento interactivo ni informativo queda fuera de `Screen.safeArea` en los perfiles del simulador con notch.
8. **Validación:** Device Simulator con perfiles con recorte, más un dispositivo real.

### MOB-AST-05: pausa y ciclo de vida de la app
1. **Problema:** no hay pausa; al recibir una llamada o cambiar de app, la partida sigue o se pierde. Además, `runInBackground: 1`.
2. **Evidencia:** sin `OnApplicationPause` ni `Time.timeScale` (EV-019); `ProjectSettings.asset` (EV-005).
3. **Cambio:** pausa automática al perder el foco y botón de pausa táctil.
4. **Impacto:** se evitan muertes injustas.
5. **Riesgo:** bajo.
6. **Prioridad:** Media.
7. **Aceptación:** al volver de segundo plano, el juego está pausado y el estado se conserva.
8. **Validación:** prueba manual en un dispositivo (botón Home y vuelta a la app).

### MOB-AST-06: corrección de R-AST-01 antes de medir rendimiento
1. **Problema:** el pool de objetos no se usa realmente: cada asteroide es un `Instantiate` y un `Destroy`, lo que genera presión de GC en móviles.
2. **Evidencia:** `Spawner.cs`, `Laser.cs` (R-AST-01).
3. **Cambio:** usar `asteroids.Get()` y `Release()` de forma coherente, o quitar el pool.
4. **Impacto:** frame time más estable en gama baja.
5. **Riesgo:** medio, porque toca el comportamiento probado.
6. **Prioridad:** Media.
7. **Aceptación:** tests de integración en verde; sin picos de GC atribuibles al spawn en el Profiler.
8. **Validación:** Unity Profiler conectado al dispositivo, más la suite.

### MOB-AST-07: feedback háptico y audio
1. **Problema:** no hay vibración; el audio es el único feedback de impacto.
2. **Evidencia:** `Ship.cs`, `Spawner.cs` (EV-007).
3. **Cambio:** vibración breve en el Game Over, opcional y desactivable.
4. **Impacto:** feedback adicional al perder.
5. **Riesgo:** bajo.
6. **Prioridad:** Baja.
7. **Aceptación:** existe la opción para desactivarla y se respeta.
8. **Validación:** dispositivo real.

---

## 2. P2 2D Platformer

Ruta: `C:\Developer\unity\2026\clases-en-vivo\proyectos-unity\2D-Platformer-Unity-main`

### MOB-PLT-01: construir la UI táctil que falta
1. **Problema:** `MobileControls` está vacío; con `controlmode = mobile` el juego no tendría botones.
2. **Evidencia:** `Level.unity` (`m_Children: []`) (EV-014); `PlayerController.MobileMove/MobileJump` (EV-011).
3. **Cambio:** botones ◀ ▶ (o stick virtual) abajo a la izquierda y botón de salto abajo a la derecha. ◀ ▶ deben enviar `MobileMove(-1/1)` al presionar y `MobileMove(0)` al soltar (eventos pointer down/up, no `onClick`).
4. **Impacto:** el juego pasa a ser jugable en táctil.
5. **Riesgo:** bajo a medio. Agregar la UI implica **editar la escena**.
6. **Prioridad:** Alta (bloqueante).
7. **Aceptación:** el jugador puede completar el nivel solo con táctil; mantener ◀ mueve de forma continua y soltar detiene.
8. **Validación:** prueba manual en un dispositivo, completando el nivel, con tiempo e intentos registrados.

### MOB-PLT-02: selección del modo de control
1. **Problema:** el modo se fija a mano en la escena (`controlmode: 1`).
2. **Evidencia:** `Level.unity:7238` (EV-014).
3. **Cambio:** determinarlo por plataforma de compilación o en tiempo de ejecución, sin duplicar escenas. Si se adopta Input System (DEC-LAB-006), el enum `Controls` puede desaparecer.
4. **Impacto:** un solo build por plataforma, sin edición manual.
5. **Riesgo:** bajo.
6. **Prioridad:** Alta.
7. **Aceptación:** el build Android muestra los controles táctiles y el build PC no.
8. **Validación:** dos builds y una inspección.

### MOB-PLT-03: precisión del salto en táctil
1. **Problema:** el doble salto depende del timing; en táctil no hay respuesta física del botón, lo que aumenta los fallos. No hay coyote time ni buffer de salto.
2. **Evidencia:** `PlayerController.cs:63-89, 221-237` (EV-011).
3. **Cambio:** coyote time y buffer de salto configurables (parámetros, no lógica duplicada), y un botón de salto grande (72 dp o más, proporción a validar).
4. **Impacto:** menos muertes percibidas como injustas.
5. **Riesgo:** medio, porque cambia la sensación del juego también en PC (decisión de diseño, DEC-LAB-007).
6. **Prioridad:** Media.
7. **Aceptación:** la tasa de éxito en el salto de referencia del nivel (por definir) en táctil no es menor que en PC en más de X puntos porcentuales (X a acordar).
8. **Validación:** sesión de prueba con registro de intentos (misma ficha que el laboratorio de *Unravel*).

### MOB-PLT-04: corregir errores visibles antes de evaluar la UX móvil
1. **Problema:** falta el parámetro `isGrounded` (error en cada frame) y los corazones no reaccionan.
2. **Evidencia:** EV-016, EV-017 (R-PLT-01, R-PLT-02).
3. **Cambio:** alinear el Animator con el código y conectar `HurtPlayer` o retirar los corazones del HUD.
4. **Impacto:** el log en el dispositivo deja de llenarse de errores y el HUD deja de engañar.
5. **Riesgo:** bajo.
6. **Prioridad:** Alta (afecta el rendimiento en el dispositivo por el logging).
7. **Aceptación:** Play Mode sin el error `isGrounded`; los corazones reflejan `currentHealth`.
8. **Validación:** log del Editor o de logcat sin el mensaje; test de unidad sobre `DisplayHearts`.

### MOB-PLT-05: HUD, safe area y cámara
1. **Problema:** con `OrthographicSize 10` en pantallas pequeñas, el personaje y los vacíos pueden verse diminutos; los botones táctiles tapan la parte inferior, donde están los peligros.
2. **Evidencia:** Cinemachine `OrthographicSize 10` (EV-015); CanvasScaler 1920×1080 con `match 0.5` (EV-018).
3. **Cambio:** revisar el tamaño ortográfico en móvil, dejar margen inferior de cámara (offset) para los botones y ajustar el HUD a `Screen.safeArea`.
4. **Impacto:** se ven las plataformas y los vacíos aunque los controles estén en pantalla.
5. **Riesgo:** bajo.
6. **Prioridad:** Media.
7. **Aceptación:** con los controles visibles, el borde inferior de las plataformas pisables nunca queda oculto por un botón.
8. **Validación:** Device Simulator y capturas por perfil.

### MOB-PLT-06: orientación
1. **Problema:** se permiten las cuatro orientaciones, incluido retrato, en un side-scroller.
2. **Evidencia:** `ProjectSettings.asset` (EV-010).
3. **Cambio:** solo horizontal (Landscape Left/Right).
4. **Impacto:** no se juega accidentalmente en retrato.
5. **Riesgo:** bajo.
6. **Prioridad:** Alta.
7. **Aceptación:** al rotar a retrato, la pantalla no cambia.
8. **Validación:** dispositivo real.

### MOB-PLT-07: rendimiento URP 2D y batería
1. **Problema:** URP 2D con `Light 2D`, partículas y `targetFrameRate 60`; consumo desconocido.
2. **Evidencia:** EV-009, EV-011, EV-015.
3. **Cambio:** medir antes de cambiar nada; si hace falta, ofrecer 30 fps opcional y bajar la calidad (ya está en Medium para Android).
4. **Impacto:** autonomía y temperatura.
5. **Riesgo:** bajo.
6. **Prioridad:** Media.
7. **Aceptación:** sin umbrales definidos (UNKNOWN), hay que acordarlos tras la primera medición.
8. **Validación:** Profiler conectado, en por lo menos un dispositivo de gama baja y uno de gama media.

### MOB-PLT-08: pausa y ciclo de vida
Igual criterio que MOB-AST-05: hoy no hay pausa (`isPaused` sin uso) ni manejo de `OnApplicationPause` (EV-011, EV-019). Prioridad Media.

---

## 3. Comparación de necesidades móviles

| Necesidad | P1 Asteroides | P2 Platformer |
|---|---|---|
| Refactor de entrada | **Imprescindible** | Parcial (la API ya existe) |
| UI táctil | Nueva | Nueva (el contenedor ya existe) |
| Orientación | A decidir (vertical u horizontal) | Horizontal |
| Precisión temporal | Baja | **Alta** (doble salto) |
| Correcciones previas | Pool (R-AST-01) | Animator + vida (R-PLT-01/02) |
| Bloqueo legal | **Sí** (Kodeco) | Arte UNKNOWN |
| Config Android a revisar | Mono + ARMv7/ARM64 | **Solo ARMv7** |

## 4. Validación general en móvil (para cuando se autorice)

1. Suite existente (P1) en batchmode con XML archivado.
2. Device Simulator del Editor: perfiles con y sin notch, en 16:9, 19.5:9 y 4:3.
3. Por lo menos un dispositivo Android real (el modelo es UNKNOWN y lo define el docente).
4. Sesión de usabilidad con la misma metodología del laboratorio (ficha de observación y cuestionario adaptados).
