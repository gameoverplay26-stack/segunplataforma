# Cuestionario evaluativo U4 y U5 — Clave de corrección (solo docente)

Acompaña a `cuestionario-evaluativo-u4-u5.md`. Cada respuesta indica de dónde sale, para poder revisarla.

## Parte A — Opción múltiple (4 puntos cada una)

| N.º | Respuesta | Fundamento | Fuente |
|---|---|---|---|
| 1 | **b** | Pico vs. sostenido: calor → *throttling* → caen los fps. Importa el minuto 10, no el 1. El número del Editor no predice el del teléfono | U4, Clase 1 slide 11; Clase 3 slides 8–9 (A4.6) |
| 2 | **c** | Según la documentación de Unity 6.3, ARM64 "se habilita solo cuando Scripting Backend es IL2CPP". El proyecto estaba en Mono + ARMv7 | U4, Clase 3 slides 3–4 y 15 |
| 3 | **b** | El Device Simulator prueba layout y safe area; no prueba rendimiento, memoria ni térmica, y simula un solo dedo | U4, Clase 3 slide 12; `PORTEO-ASTEROIDES.md` §5 |
| 4 | **a** | XR = condición para publicar. XAG = buenas prácticas, "no pensadas como lista de control" | U5, slide 25 |
| 5 | **b** | Mismos modos en toda la generación: el modelo más débil manda (caso Baldur's Gate 3 en Series S) | U5, slides 6 y 26 |
| 6 | **c** | Developer Mode + UWP: cuenta gratuita de Partner Center, `.msix` por Device Portal. Sirve para probar, no para publicar | U5, slides 41–42; `PORTEO-XBOX.md` §1 |
| 7 | **b** | `MobileControlsVisibility` apaga los controles táctiles fuera del móvil; `OnScreenStick`/`OnScreenButton` quitan su gamepad virtual y la capa pausaba. Corrección: solo cuentan los mandos físicos (`device.native`) | U5, slide 47; `PORTEO-XBOX.md` §3 |
| 8 | **c** | R-PLT-09: el rayo nacía dentro del `CapsuleCollider2D` del jugador, `IsGrounded()` siempre era verdadero. Defecto del original, no del porteo. Después se corrigió (DEC-LAB-015) y los tests quedaron 15/15 y 17/17 | `PORTEO-PLATFORMER.md` §3, §4 y §8 |

## Parte B — Verdadero o falso (2 puntos por V/F + 2 por la justificación si es F)

| N.º | Respuesta | Justificación esperada | Fuente |
|---|---|---|---|
| 9 | **V** | — | `PORTEO-ASTEROIDES.md` §2; U4, Clase 2 slide 12 |
| 10 | **V** | — | U4, Clase 2 slide 11; `PORTEO-ASTEROIDES.md` §2 |
| 11 | **F** | Unity 6.3 declara "Both" **no soportado** en Android (aparece el aviso "Unsupported Input Handling on Android"). Asteroides lo mantuvo como aviso; el Platformer v2 usó solo "Input System Package (New)" y cambió el módulo de UI a `InputSystemUIInputModule` | U4, Clase 3 slides 4–5; `PORTEO-PLATFORMER.md` §1 |
| 12 | **F** | Se agregó una **capa de consola** (`Assets/Scripts/Console/`) que se instala sola con `[RuntimeInitializeOnLoadMethod]`. No se tocaron escenas ni prefabs, y `Ship.cs` es el mismo; en los adaptadores solo se agregó `SetConsolePaused` | U5, slides 45–46; `PORTEO-XBOX.md` §3 |
| 13 | **F** | Generar el paquete prueba que **se compila** y que declara la familia Xbox. Que corra en la consola es UNKNOWN hasta la prueba en la Xbox (tabla del paso 8 de la guía docente) | `PORTEO-XBOX.md` §5; U5, slide 40 "Compila… ¿se juega?" |
| 14 | **F** | En Asteroides, las 3 hipótesis del pool fallaban **antes y después** del porteo (defecto real del juego), y otra falla era inestable y cambiaba de test. Hay que leer el stack trace y comparar con la línea base | U4, Clase 3 slide 14; `PORTEO-ASTEROIDES.md` §4 |
| 15 | **F** | Solo Microsoft publica los XR y sus casos de prueba. Sony (TRC) y Nintendo (Lotcheck) los tienen bajo NDA; solo publican los pasos de alta | U5, slides 23–24 |

## Parte C — Respuesta corta (8 puntos cada una)

**16.** Criterios (8 puntos):
- Dispositivo = **cómo** pide el jugador la acción (teclado, táctil, mando). Es lo que cambia por plataforma (2 pts).
- Intención = **qué** quiere hacer (mover, disparar), independiente del dispositivo (2 pts).
- Lógica del juego = la nave (movimiento, disparo, límites); no sabe de dónde vino la orden (2 pts).
- Ejemplo (2 pts): flechas y espacio en PC, joystick y botón en pantalla en Android, stick y botón A en Xbox; los tres terminan en `Ship.SetIntent(mover, disparar)` a través de `ShipInputAdapter`.

Fuente: U4, Clase 1 slide 3; Clase 2 slides 11–12; Clase 3 slide 14.

**17.** Criterios (8 puntos):
- La cámara ve 5 × *aspect* a cada lado del centro: en 16:9 son unas 8,9 unidades; en vertical, unas 2,8 (4 pts).
- Los asteroides aparecen en x ∈ [−8, 8], un rango pensado para horizontal (2 pts).
- Conclusión: en vertical, la mayoría nace fuera de la vista. Es un supuesto de PC escondido en el código (`Spawner.cs`); la solución propuesta es calcular el spawn según la cámara (MOB-AST-03) (2 pts).

Fuente: U4, Clase 2 slides 4–5 (A4.2).

**18.** Tres de estos (hasta 8 puntos; 2 por cambio + 2 por la justificación en conjunto):
- Cambia el `StandaloneInputModule` por `InputSystemUIInputModule`, y **el foco** queda siempre en un botón, resaltado en amarillo. Sin mouse, el menú se navega con cruceta y A (XR-003).
- **Pausa** con Menu (≡), al desconectar el mando y al perder el foco. El original no tenía pausa.
- **Texto de al menos 26 px a 1080p** (XAG 101), porque se lee a tres metros, en una TV.
- **Oculta el botón Salir**: en consola la aplicación la cierra el sistema.

Fuente: U5, slides 36–37 y 45–46; `PORTEO-XBOX.md` §3.

**19.** Criterios (8 puntos):
- Los tres motivos (`PauseReason`): botón Menu (≡) durante la partida, mando físico desconectado y pérdida de foco de la aplicación (2 pts cada uno = 6).
- Relación (2 pts): la pausa por desconexión del mando es el primer paso hacia el **XR-115** (si se quita el mando activo, pedir otro) y su caso de prueba público **115-02** (sacar las pilas del mando). También se acepta la relación de la pérdida de foco con suspender y reanudar (XR-112), aclarando que es una aproximación con `OnApplicationFocus`.

Dato extra (no obligatorio): Menu no pausa en un menú porque pausa solo durante la partida, cuando no hay botones a la vista.

Fuente: U5, slides 26–27, 44, 46 y 49; `PORTEO-XBOX.md` §3.

**20.** Criterios (8 puntos; 1 por celda, y 2 extra si la fila de Xbox menciona la dependencia VCLibs o el certificado):

| Plataforma | Archivo | Cómo se instala |
|---|---|---|
| PC (Windows) | Carpeta `Builds/Windows/` con el `.exe` y el instalador `…-Setup.exe` (Inno Setup) | Se ejecuta el instalador: instala por usuario, sin administrador, con acceso directo y desinstalador |
| Android | `.apk` (IL2CPP + ARM64) | Copiarlo al teléfono y aceptar "fuentes desconocidas", o por cable con `adb install -r` / Build and Run |
| Xbox (Developer Mode) | Paquete `.msix` x64 (más `Microsoft.VCLibs.x64` en `Dependencies/` y el `.cer`) | Device Portal desde el navegador de la PC → *Add* → elegir el `.msix` y la dependencia → lanzar desde Dev Home |

Fuente: `PORTEO-PLATFORMER.md` §9; U4, Anexo slide 8; U5, slides 42 y 79–83.

## Notas para la docente

- **Prueba en la Xbox:** al armar este cuestionario, el resultado de la prueba en la consola **no estaba registrado** (`PORTEO-XBOX.md` §7, pendiente). Por eso las preguntas sobre Xbox se basan en el código, los tests y los paquetes generados, no en lo que se vio en la TV. Si la demo ya se hizo, se puede agregar una pregunta sobre qué predicción de A5.5 falló.
- **Prueba en teléfonos reales:** según el informe del 2026-10-25, las builds se probaron en celulares, pero no hay evidencia archivada en el repo. Ninguna pregunta depende de esos resultados.
- La pregunta 13 es la que mejor evalúa el criterio de evidencia de la materia (compila ≠ funciona): conviene discutirla en la devolución.
