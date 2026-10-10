# XBOX-ADAPTATION: análisis preliminar de adaptación a Xbox (fase 2)

- **Estado del documento:** PROPUESTO / análisis preliminar. Es independiente de la adaptación móvil.
- **Principio:** que un juego compile para Windows **no** garantiza que corra en una consola Xbox. Este documento **no** afirma que se pueda publicar ni ejecutar P1 o P2 en una Xbox comercial.
- **Restricción respetada:** no se intentó acceder al programa ID@Xbox, al GDK, a kits de desarrollo ni a herramientas restringidas.

## 1. Requisitos de acceso

| Requisito | Detalle | Estado | Fuente |
|---|---|---|---|
| Onboarding en ID@Xbox | Se requiere "ID@XBOX onboarding complete" antes de empezar | CONFIRMADO (documentación oficial) | SRC-002 |
| Plug-in Xbox GDK para Unity | "granted via ID@XBOX": no es una descarga pública | CONFIRMADO | SRC-002 |
| Producto en Partner Center | Producto con las "device rows" correspondientes habilitadas | CONFIRMADO | SRC-002 |
| Versión de Unity | Unity 2022 LTS o posterior. P1 y P2 usan 6000.3.11f1 | CONFIRMADO (el requisito); compatibilidad exacta del plug-in con 6000.3.11f1: **UNKNOWN** | SRC-002 |
| Licencia de Unity | Según Unity, se necesita Unity Pro activo o una Preferred Platform license key del fabricante para compilar a plataformas cerradas | Requisito declarado por Unity (SRC-010); la vigencia de las condiciones de Xbox a hoy está **POR INVESTIGAR** | SRC-010 |
| Módulo de compilación Xbox en el Editor | Instalado en esta máquina: `AndroidPlayer`, `MetroSupport` y `windowsstandalonesupport`. **No** hay módulos GameCore/Xbox | VERIFICADO (local) | EV-023 |
| Dev kit / consola en Developer Mode | Necesario para probar en hardware | **POR INVESTIGAR** (no se consultó una fuente oficial en esta sesión) | — |
| Confidencialidad (NDA) de la documentación del GDK | Las herramientas y la documentación detallada de certificación son de acceso restringido | **POR INVESTIGAR** | — |

**Conclusión de acceso:** la adaptación ejecutable a Xbox está **BLOCKED** por requisitos externos (ID@Xbox, plug-in, licencia). Sin ellos, lo viable en el ámbito académico es **diseñar** la adaptación y **simular** la experiencia de consola en PC con un gamepad de Xbox (DEC-LAB-008).

## 2. Análisis funcional por juego

### 2.1 Mapeo de acciones al gamepad (PROPUESTO)

| Acción | P1 Asteroides | P2 Platformer |
|---|---|---|
| Moverse | Stick izquierdo X / D-pad ←→ | Stick izquierdo X / D-pad ←→ |
| Acción principal | A (disparo, mantener) o RT | A (salto, doble salto) |
| Confirmar en menús | A | A |
| Volver / cancelar | B | B |
| Pausa | Menu (≡) | Menu (≡) |
| Estado actual | **No hay soporte**: teclas fijas en `Ship.cs` (EV-007) | Ejes del Input Manager con entradas de joystick (EV-013); el funcionamiento real es **UNKNOWN** |

La recomendación es la misma que en la fase 1: una única capa de acciones (Input System, DEC-LAB-006) que sirva para teclado, táctil y gamepad, sin duplicar el gameplay.

### 2.2 Navegación sin mouse y foco visual

| Punto | P1 | P2 |
|---|---|---|
| Menú inicial | Un único botón "Start" (UnityEvent `NewGame`); no hay botón con foco inicial (UNKNOWN, hay que verificar el `EventSystem` en `Game.prefab`) | `EventSystem.m_FirstSelected` vacío (EV-018): con gamepad, ningún botón tiene foco al cargar |
| Panel de fin | Game Over: el botón Start reaparece | LEVEL COMPLETE: botones Menu/Quit |
| Propuesta | Foco inicial al mostrar cualquier panel; estado visual "Selected" claramente distinto de "Normal" | Ídem, más reasignar el foco al abrir `LevelExitPanel` |
| Botón Quit | No hay | `Application.Quit()` (`Events.cs`). En consola, cerrar la app desde el juego suele no corresponder a las convenciones de la plataforma (**POR INVESTIGAR** contra la documentación oficial) |

### 2.3 Legibilidad a distancia (pantalla de TV)

- Las Xbox Accessibility Guidelines (XAG 101) fijan como mínimo por defecto en consola **26 px de altura de cuerpo a 1080p** (52 px en 4K), y recomiendan que el jugador pueda escalar el texto (SRC-003).
- P2: fuentes TMP de 36 a 87 en un canvas de referencia 1920×1080 (EV-018). Hay que medir la **altura de cuerpo real** renderizada, no el `fontSize`. Estado: UNKNOWN.
- P1: `Text` legacy con escalado solo por ancho; tamaños no inventariados. Estado: UNKNOWN.

### 2.4 Áreas seguras de visualización
Requisito de title-safe/overscan en TV: **POR INVESTIGAR** con documentación oficial de Xbox. Mientras tanto, se propone un margen configurable del HUD reutilizando la solución de safe area de la fase 1.

### 2.5 Resolución, rendimiento y estabilidad
- P2: URP 2D. P1: Built-in con Gamma. Que Built-in y la configuración de color sean compatibles con el plug-in GDK es **UNKNOWN**.
- `QualitySettings`: P2 tiene entradas `GameCoreScarlett` y `GameCoreXboxOne` en nivel 5 (EV-010), que son valores por defecto de la plantilla y **no** prueban configuración real.
- Sin hardware no se puede medir. Estado: BLOCKED.

### 2.6 Pausa, reanudación y reconexión del control
- Ninguno de los dos juegos tiene pausa (EV-019).
- Propuesta: pausa automática al desconectarse el control y al suspender o reanudar la app; mensaje "Reconectá el control".
- El comportamiento exigido por la plataforma ante suspensión, reanudación y emparejamiento de usuario y control es **POR INVESTIGAR** en la documentación del GDK (restringida).

### 2.7 Guardado y estados
Ninguno guarda progreso (EV-019). P1 podría guardar el puntaje máximo y P2 el nivel completado y las monedas. El almacenamiento en consola usa APIs de la plataforma (**POR INVESTIGAR**).

## 3. Pruebas de aceptación (borrador)

| ID | Criterio | Ejecutable hoy |
|---|---|---|
| XB-AC-01 | Todo el flujo (menú → partida → fin → menú) se completa solo con gamepad | Sí, en PC con un gamepad Xbox (simulación) |
| XB-AC-02 | Siempre hay un elemento con foco visible en los menús | Sí, en PC |
| XB-AC-03 | Texto con altura de cuerpo de 26 px o más a 1080p | Sí, con capturas a 1080p |
| XB-AC-04 | Al desconectar el control, el juego se pausa | Parcial en PC |
| XB-AC-05 | Cumplimiento de los requisitos de certificación de Xbox | **BLOCKED** (herramientas oficiales restringidas) |

## 4. Resumen

| Categoría | Ítems |
|---|---|
| Confirmados | ID@Xbox, plug-in GDK vía ID@Xbox, Partner Center, Unity 2022 LTS o posterior (SRC-002); 26 px a 1080p (SRC-003); licencia Pro o clave de plataforma según Unity (SRC-010) |
| Por investigar | Compatibilidad plug-in/6000.3.11f1, dev kit, title-safe, PLM (suspensión/reanudación), guardado, botón Quit en consola, vigencia de las condiciones de licencia |
| Decisiones | DEC-LAB-008 (objetivo de la fase Xbox), DEC-LAB-006 (Input System) |
