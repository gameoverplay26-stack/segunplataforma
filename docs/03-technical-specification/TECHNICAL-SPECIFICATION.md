# Technical Specification — Asteroid Survival

> **Fase SDD:** Technical Specification, fase 7. **Estado:** APROBADA el 2026-10-26 (tag `etapa-03-technical-specification-complete`). Cambiarla requiere autorización explícita y un registro en el Historial de `docs/SDD-STATUS.md`.
> **Entradas normativas:** GDD aprobado (`docs/02-gdd/GDD.md`, tag `etapa-02-gdd-complete`, REQ-001…REQ-040) y las decisiones `DEC-046`…`DEC-061` de `docs/SDD-STATUS.md`.
> **Qué es:** los requisitos técnicos verificables (`TECH-###`) que el proyecto `Arena-SDD/` tiene que cumplir: motor, paquetes, plataformas, área de juego, valores de balance, input, colisiones, tiempo, aleatoriedad, audio, assets y testing.
> **Qué no es:** no es Architecture Specification. No define clases, interfaces, eventos ni la forma del código; eso queda para la fase siguiente (ARCH-###). Tampoco crea el proyecto Unity ni instala paquetes: eso ocurre en Implementation.
> **Convención:** cada TECH cita su origen entre corchetes y su forma de verificación. Lo marcado **PROPUESTO** se aprueba con el checkpoint de esta fase; lo marcado **PENDIENTE** espera una decisión del usuario (§12).

## 1. Motor, proyecto y versionado

**TECH-001 — Motor y lenguaje.** Unity **6000.3.11f1**, C#. No se cambia de versión del editor. [CLAUDE.md §2] [Discovery]
Verificación: `ProjectSettings/ProjectVersion.txt` = `6000.3.11f1`.

**TECH-002 — Ubicación del proyecto.** El proyecto vive en `Arena-SDD/`, en la raíz del repo. Se abre desde una ruta corta: la ruta completa de cualquier archivo del proyecto no supera los 260 caracteres, porque Unity falla al importar con rutas largas en Windows (hallazgo ENV-01 del laboratorio de porteo). [CLAUDE.md §2] [DEC-013]
Verificación: la importación inicial en batchmode termina sin errores de ruta (log).

**TECH-003 — Versionado.** Serialización de assets en **texto** y archivos `.meta` **visibles**. Se versionan `Assets/`, `Packages/` y `ProjectSettings/`; se ignoran `Library/`, `Temp/`, `Obj/`, `Logs/`, `UserSettings/` y `Builds/` (ya cubiertos por el `.gitignore` del repo).
Verificación: `EditorSettings.asset` (`m_SerializationMode: 2`) y `git status` limpio después de abrir el proyecto.

## 2. Paquetes

**TECH-004 — Paquetes del proyecto.** Solo estos paquetes, todos incluidos con el editor 6000.3.11f1 (no hay descarga de terceros):

| Paquete | Versión | Para qué | Origen |
|---|---|---|---|
| `com.unity.inputsystem` | 1.19.0 | Input de teclado (PC y WebGL) y táctil (Android) | DEC-048, DEC-056 |
| `com.unity.test-framework` | 1.6.0 | Unit e integration tests (Edit Mode y Play Mode) | Discovery, CLAUDE.md §9 |
| `com.unity.ugui` | 2.0.0 | Interfaz (incluye TextMeshPro) | DEC-057 |
| `com.unity.feature.2d` y `com.unity.render-pipelines.universal` | 2.0.2 / 17.3.0 | Plantilla 2D de Unity 6 y render URP | DEC-057 |

Cualquier paquete adicional requiere autorización explícita del usuario para ese paquete (CLAUDE.md §8).
Verificación: `Packages/manifest.json` no tiene otras dependencias directas que las de esta tabla y las que agregue la plantilla elegida.

## 3. Plataformas y rendimiento

**TECH-005 — Destinos de build.** [DEC-046]

| Destino | Configuración | Fase |
|---|---|---|
| Windows | Standalone x86_64 | Implementation |
| Android | IL2CPP, ARM64, API mínima 25 (Android 7.1) — PROPUESTO | Platform Adaptation |
| WebGL | Configuración por defecto de Unity 6 — PROPUESTO | Platform Adaptation |

iOS queda fuera (no hay Mac).
Verificación: build en batchmode de cada destino con log sin errores.

**TECH-006 — Rendimiento objetivo (PROPUESTO).** 60 fps en Windows y en WebGL de escritorio; 60 fps como objetivo en Android, con 30 fps como mínimo aceptable. [DEC-046]
Verificación: MANUAL con el Profiler o el contador de fps del editor, en una partida de 3 min.

**TECH-007 — Builds por script.** Cada destino se construye con un comando en batchmode (sin abrir el editor), con el log archivado como evidencia. [CLAUDE.md §7]
Verificación: el log de build de cada destino.

## 4. Pantalla y área de juego

**TECH-008 — Orientación.** Windows y WebGL de escritorio: **horizontal**. Android: **vertical fija** (sin rotación automática). [DEC-047]
Verificación: Player Settings de cada destino; MANUAL en el teléfono.

**TECH-009 — Área de juego fija con franjas.** El área es un rectángulo de **tamaño fijo en unidades de mundo**, con **alto de 10 unidades**, mostrado por una cámara ortográfica. Si la pantalla tiene otra proporción, el área no se deforma ni se estira: se agregan **franjas** (letterbox o pillarbox) y la interfaz queda dentro del área. Los bordes de §9 del GDD (bloqueo de la nave, eliminación de asteroides y proyectiles) son los bordes de ese rectángulo, no los de la pantalla. [DEC-059] [DEC-047] [DEC-012]
**Proporción por orientación (DEC-060):** **16:9** en Windows y WebGL (17,8 × 10 unidades) y **9:16** en Android (5,6 × 10 unidades). El alto es el mismo en los dos, así que los valores de TECH-010 y TECH-011 no cambian; cambia el ancho para moverse y para el rango de aparición (TECH-018). Es la única diferencia admitida por REQ-034.
Verificación: UNIT (los bordes del área no dependen de la resolución) + MANUAL en cada destino y en dos proporciones de pantalla.

**TECH-010 — Valores ligados al alto del área.** Las velocidades y los tamaños se definen como **fracciones del alto del área** (*H* = 10 unidades). Así, el tiempo de caída y el tamaño relativo de los objetos no dependen del dispositivo. [DEC-052] [DEC-058]
Verificación: UNIT (conversión de fracción a unidades de mundo).

## 5. Valores de balance (APROBADOS, DEC-058)

**TECH-011 — Tabla de balance inicial.** Los valores del GDD se mantienen; los que quedaban diferidos (TD-2) son estos, aprobados por el usuario el 2026-10-26 (DEC-058). *H* = alto del área (10 unidades).

| Valor | Propuesta | Origen | Comentario |
|---|---|---|---|
| Duración de la partida | 180 s | DEC-034 (aceptación [180, 300] s, DEC-016) | Ya decidido |
| Cuenta regresiva | 3 s | DEC-041 | Ya decidido |
| Vida inicial / daño por contacto | 5 / 1 | DEC-035 | Ya decidido |
| Puntos por asteroide | 10 | DEC-035 | Ya decidido |
| Tiempo de caída del asteroide (todo el alto) | **3,0 s** (velocidad = *H*/3 por s) | DEC-025, DEC-045 | Da tiempo a reaccionar sin que sea lento |
| Pausa entre un asteroide y el siguiente | **0,5 s** desde que el anterior desaparece | DEC-044 | Con 3,5 s por ciclo, unos 50 asteroides por partida |
| Velocidad de la nave | **0,6 *H*/s** | TD-2 | Cruza el alto en 1,7 s |
| Velocidad del proyectil | **1,5 *H*/s** | DEC-037 | Cruza el alto en 0,7 s |
| Cadencia de disparo | **0,25 s** entre disparos (4 por segundo) | DEC-022 | |
| Tamaño de la nave | **0,08 *H*** | TD-2 | |
| Tamaño del asteroide | **0,10 *H*** | TD-2 | |
| Tamaño del proyectil | **0,03 *H*** | TD-2 | |
| Posición inicial de la nave | Centro horizontal, a **0,15 *H*** del borde inferior | REQ-003 | El GDD no la fija; es una propuesta técnica |

Verificación: DOC (esta tabla contra la configuración de TECH-012) + MANUAL (partida de prueba).

**TECH-012 — Configuración en ScriptableObject.** Todos los valores de TECH-011 viven en un asset de configuración (ScriptableObject) editable desde el Inspector. Al cargarse se validan: ningún valor negativo ni cero (salvo la pausa entre asteroides, que puede ser 0), duración dentro de [180, 300] s (DEC-016). Los tests usan su propia configuración, creada en el test. [DEC-053]
Verificación: UNIT (validación de rangos y uso de una configuración de test).

## 6. Input

**TECH-013 — Input System con un mapa de acciones.** Un único asset de acciones con estas cuatro acciones, que son las intenciones del GDD §11. [DEC-048] [DEC-005]

| Acción | Tipo | Teclado (PC y WebGL) | Táctil (Android) |
|---|---|---|---|
| Mover | Valor `Vector2` | WASD y flechas | Joystick en pantalla |
| Disparar | Botón, se mantiene | Espacio | Botón en pantalla |
| Iniciar | Botón | Enter o Espacio en la pantalla previa | Botón de la pantalla previa |
| Reiniciar | Botón | R o Enter en la pantalla final | Botón de la pantalla final |

El táctil usa los controles en pantalla del propio Input System (On-Screen Stick y On-Screen Button). **Sin gamepad** (DEC-056).
Verificación: INT (acciones simuladas con el soporte de testing del Input System) + MANUAL en cada destino.

**TECH-014 — Solo el Input System nuevo.** *Active Input Handling* = **Input System Package (New)**, no "Both": el laboratorio de porteo registró que Unity 6.3 declara "Both" no soportado en Android. [DEC-048]
Verificación: Player Settings (`activeInputHandler: 1`).

## 7. Colisiones, reglas y tiempo

**TECH-015 — Detección con física 2D.** Los contactos se detectan con colliders 2D en modo trigger y Rigidbody2D cinemáticos. Solo se detectan dos pares: **nave–asteroide** y **proyectil–asteroide**. Asteroide–asteroide (DEC-030) y proyectil–nave (DEC-038) no generan contacto: se excluyen con capas y la matriz de colisiones 2D. [DEC-049]
Verificación: INT (Play Mode).

**TECH-016 — Reglas sin escena.** Las consecuencias de los contactos y todas las reglas de §4–§10 del GDD (vida, daño, score, resultado, cadencia, aparición, final) se pueden ejecutar y probar **sin cargar una escena** y sin MonoBehaviour. [DEC-049] [CLAUDE.md §9]
Verificación: los unit tests de esas reglas corren en Edit Mode.

**TECH-017 — Reloj reemplazable.** Ninguna regla lee el tiempo de Unity directamente (`Time.time`, `Time.deltaTime`). El tiempo de partida, la cuenta regresiva, la cadencia y la pausa entre asteroides se calculan con un tiempo que se puede reemplazar en los tests para avanzarlo a mano. [DEC-050] [TD-1]
Verificación: UNIT (por ejemplo, avanzar 180 s y comprobar *Completado* sin esperar).

**TECH-018 — Aparición con semilla.** La posición horizontal de cada asteroide sale de un generador pseudoaleatorio con **semilla configurable** y es **uniforme** entre el borde izquierdo y el derecho, con un margen de medio asteroide para que aparezca entero dentro del ancho. La misma semilla produce siempre la misma secuencia. [DEC-051] [DEC-042] [TD-3]
Verificación: UNIT (dos generadores con la misma semilla dan la misma secuencia; todas las posiciones quedan dentro del rango).

## 8. Interfaz y audio

**TECH-019 — Interfaz.** **uGUI** con TextMeshPro, dentro del área de juego (TECH-009) [DEC-057]. Pantallas: previa con la acción de iniciar (REQ-001), cuenta regresiva (REQ-002), HUD de vida, tiempo y score (REQ-028…030), pantalla final con resultado y score (REQ-009) y reinicio (REQ-031).
Verificación: MANUAL + INT.

**TECH-020 — Audio.** Un efecto por evento de la lista de `ASSETS-LICENCIAS.md` §3 (aprobada, DEC-061): disparo, asteroide destruido, nave dañada, Game Over, partida completada, cada segundo de la cuenta regresiva, e iniciar o reiniciar. Archivos OGG; audio 2D (sin posición en el espacio); sin música. [DEC-055] [REQ-033]
Verificación: INT (el evento pide reproducir el efecto correcto) + MANUAL (se escucha).

**TECH-021 — Assets de terceros.** Solo los archivos elegidos de los packs CC0 de `ASSETS-LICENCIAS.md`, cada uno con el `License.txt` de su pack, y con el ZIP verificado por su SHA-256 antes de importar. [DEC-054] [DEC-013]
Verificación: DOC (lista de archivos importados contra la propuesta y sumas SHA-256).

## 9. Testing

**TECH-022 — Infraestructura de tests.** Unity Test Framework 1.6.0, con un ensamblado de tests de Edit Mode (reglas, TECH-016) y otro de Play Mode (detección, flujo e input). Cada test lleva su ID y su trazabilidad con atributos NUnit: `[Test, Property("Id", "TEST-UNIT-001"), Property("Trace", "REQ-003")]`. [traceability.md] [CLAUDE.md §9]
Verificación: el XML del runner muestra los `Property` de cada test.

**TECH-023 — Ejecución en batchmode con evidencia.** La suite se ejecuta sin abrir el editor (`-batchmode -runTests -testPlatform EditMode|PlayMode -testResults <xml> -logFile <log>`) y el XML y el log se archivan como evidencia. [CLAUDE.md §7]
Verificación: el XML y el log archivados en `docs/08-verification/`.

## 10. Lo que esta especificación no resuelve

- La **forma** del código: qué componentes, interfaces y eventos implementan cada TECH. Es Architecture Specification, incluida la forma arquitectónica de DEC-005.
- Los **casos de test** concretos: Test Strategy.
- La parte **visual** de REQ-033: sigue sin especificar.
- La **dificultad progresiva** (REQ-032, COULD) y los **niveles futuros** (DEC-043): fuera del MVP.

## 11. Trazabilidad REQ → TECH

| REQ | TECH |
|---|---|
| REQ-001, REQ-009, REQ-028, REQ-029, REQ-030, REQ-031 | TECH-013, TECH-019 |
| REQ-002, REQ-004, REQ-005 | TECH-011, TECH-012, TECH-016, TECH-017 |
| REQ-003 | TECH-011, TECH-016 |
| REQ-006, REQ-007, REQ-008, REQ-010, REQ-014, REQ-026, REQ-027, REQ-036, REQ-039 | TECH-016 |
| REQ-015, REQ-019, REQ-023, REQ-025, REQ-038 | TECH-015, TECH-016 |
| REQ-011, REQ-013 | TECH-010, TECH-011, TECH-013 |
| REQ-012, REQ-020, REQ-024 | TECH-009, TECH-016 |
| REQ-016, REQ-018 | TECH-011, TECH-013, TECH-017 |
| REQ-017, REQ-037 | TECH-010, TECH-011, TECH-016 |
| REQ-021 | TECH-009, TECH-018 |
| REQ-022 | TECH-010, TECH-011 |
| REQ-033 | TECH-020, TECH-021 |
| REQ-034 | TECH-008, TECH-009, TECH-013, TECH-014 |
| REQ-040 | TECH-011, TECH-016, TECH-017 |
| REQ-032, REQ-035 | — (fuera del MVP) |

TECH sin REQ propio, de soporte del proceso: TECH-001…TECH-007 (motor, proyecto, paquetes, plataformas, rendimiento, builds), TECH-022 y TECH-023 (testing).

## 12. Decisiones de cierre

No quedan pendientes. Resueltos el 2026-10-26: gamepad (DEC-056, sin gamepad), render e interfaz (DEC-057, URP + uGUI), balance (DEC-058), franjas (DEC-059), proporción del área por orientación (DEC-060, cierra INC-11 y corrige REQ-034) y sonidos (DEC-061). Lo marcado PROPUESTO en TECH-005 y TECH-006 (Android IL2CPP + ARM64 con API mínima 25, WebGL por defecto, metas de fps) queda aprobado con el cierre de la fase.
