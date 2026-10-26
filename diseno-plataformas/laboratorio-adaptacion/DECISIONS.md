# DECISIONS: decisiones pendientes de aprobación humana

Ninguna de estas decisiones se resolvió por inferencia. Estado inicial de todas: **PENDIENTE**.
Prefijo `DEC-LAB-` para no colisionar con los `DEC-###` del proyecto SDD "Arena".

## Registro de resoluciones

| ID | Estado | Fecha | Resolución del usuario |
|---|---|---|---|
| DEC-LAB-001 | **RESOLVED** | 2026-10-10 | Opción (a): la documentación se guarda en `diseno-plataformas/laboratorio-adaptacion/`, dentro del repositorio. |
| DEC-LAB-002 | **RESOLVED** | 2026-10-10 | Se modifica el código de P1 solo para pruebas internas de porteo y para preparar las diapositivas de clase sobre el porteo de este juego y de P2. El usuario asume la decisión sobre la restricción de licencia de Kodeco, que se mantiene documentada en EV-004. |
| DEC-LAB-003 | **RESOLVED** | 2026-10-10 | Opción (a): el estado migrado a Unity 6 es la línea base de P2. Se hace un commit inicial de la línea base y un push antes de cualquier modificación. |
| DEC-LAB-006 | **RESOLVED** | 2026-10-10 | Opción (a): se autoriza instalar el paquete Input System (`com.unity.inputsystem`). **Instalado en P1 el 2026-10-10:** versión 1.19.0, Active Input Handling = Both (ver `PORTEO-ASTEROIDES.md`). **P2: instalado el 2026-10-19 en la copia `2D-Platformer-Unity-v2`** (1.19.0, Active Input Handling = New; ver `PORTEO-PLATFORMER.md`). El original no se modificó. |
| DEC-LAB-009 a 012 | **PENDIENTE** | 2026-10-10 | El usuario las deja abiertas explícitamente: copia y perfil de *Unravel*, duración de la clase, grabaciones y desafío del capítulo 10. |
| DEC-LAB-007 | PENDIENTE (con implementación provisional) | 2026-10-10 | En P1 se implementó joystick + botón como **referencia** para la demo. El esquema final lo eligen los grupos en A4.3/A4.7. |
| DEC-LAB-008 | **RESOLVED** | 2026-10-26 | Ni (a) ni (b) tal como estaban: demo **real** en la Xbox Series X de la docente (modelo japonés, 1 TB) en **Developer Mode**, con paquetes UWP instalados por red local (sin tienda ni nube, sin ID@Xbox ni GDK). Se muestran **dos versiones** de cada juego: la actual **sin cambios de gameplay** y una **adaptada a consola** (copias `Asteroides-Xbox/` y `2D-Platformer-Xbox/`). Guía para la docente y guía para alumnos. Registro: `PORTEO-XBOX.md`. |
| DEC-LAB-017 | **RESOLVED** | 2026-10-26 | Se autoriza instalar en Visual Studio 2022 Pro la carga de trabajo de UWP, las herramientas C++ de UWP y el Windows SDK, y todo lo necesario para la demo en Xbox ("autorizo a lo que necesites"). |
| DEC-LAB-004, 005, 013, 014 | PENDIENTE | — | — |
| DEC-LAB-015 | **RESOLVED** | 2026-10-19 | Corregir el salto infinito (R-PLT-09) en P2 v2: el detector de suelo ignora al jugador y a los triggers, y `groundLayer` incluye la capa `ground`. Se aplica a los dos niveles. |
| DEC-LAB-016 | **RESOLVED** | 2026-10-19 | Vidas en P2 v2: 3 vidas (los 3 corazones del HUD). Cada muerte resta una y reinicia el nivel actual. Con 0 vidas, panel GAME OVER con "Retry" (nivel 1, 3 vidas) y "Menu". |

| ID | Decisión | Alternativas | Impacto | Recomendación de Claude | Bloquea |
|---|---|---|---|---|---|
| DEC-LAB-001 | **Ubicación de la documentación** | (a) `diseno-plataformas/laboratorio-adaptacion/` en el repo; (b) otra carpeta; (c) mantenerla fuera del repo | (a) la versiona con el material de cátedra sin tocar los proyectos ni `docs/` (Arena) | (a) | Persistir el paquete en el repo |
| DEC-LAB-002 | **Licencia de Kodeco en P1**: los scripts prohíben el uso "pedagógico o instruccional" | (a) Consultar a Kodeco o al área legal de la institución; (b) reescribir P1 desde cero con código propio, conservando solo el arte CC0 de Kenney; (c) excluir P1 del trabajo; (d) usar P1 solo como caso de análisis, sin distribuirlo | Legal e institucional. Hoy P1 ya está versionado en el repo y se usa en clase (TP3) | (a) y, mientras tanto, no modificar ni distribuir P1 | Toda implementación sobre P1 |
| DEC-LAB-003 | **Línea base de P2**: ya fue migrado a Unity 6 (10/10/2026 16:13) y el API Updater modificó `PlayerController.cs`; el proyecto no está versionado | (a) Aceptar el estado actual como línea base y versionarlo (requiere un commit autorizado); (b) restaurar el ZIP 2022.3.13f1 y migrar de forma controlada | Trazabilidad de cualquier cambio futuro | (a), con un commit de línea base antes de cualquier modificación | Implementación sobre P2 |
| DEC-LAB-004 | **Plataforma móvil** | Android solo / Android + iOS | El módulo de iOS no está instalado (EV-023) | Android solo | Fase 1 |
| DEC-LAB-005 | **Orientación de P1** | Vertical / horizontal | Esquema táctil, rango de spawn y HUD | Vertical, por la dinámica de caída en Y (es una cuestión de diseño y la decide el usuario) | MOB-AST-02/03 |
| DEC-LAB-006 | **Sistema de entrada**: migrar al paquete Input System | (a) Instalarlo y unificar teclado, táctil y gamepad; (b) seguir con el Input Manager y agregar botones uGUI | (a) requiere **instalar un paquete** (autorización explícita por paquete) y sirve para móvil y Xbox | (a) | Fases 1 y 2 |
| DEC-LAB-007 | **Esquemas de control táctil y ajustes de sensación** | P1: botones / arrastre + autodisparo / mitades de pantalla. P2: coyote time y buffer sí o no | Cambian el diseño del juego | Prototipar 2 esquemas y probarlos con usuarios | MOB-AST-02, MOB-PLT-03 |
| DEC-LAB-008 | **Alcance de la fase Xbox** | (a) Solo análisis + simulación con gamepad en PC; (b) gestionar el acceso real (ID@Xbox, Unity Pro o clave de plataforma) | (b) tiene costos, plazos y requisitos de terceros | (a) | Fase 2 ejecutable |
| DEC-LAB-009 | **Copia de *Unravel*** y partida guardada | Xbox One / Series; disco / digital / EA Play; perfil con los capítulos accesibles | Sin perfil preparado, el laboratorio queda BLOCKED | Que el docente juegue de antemano y deje los segmentos accesibles | Laboratorio |
| DEC-LAB-010 | **Duración real de la clase, matrícula y número de grupos** | 80 / 120 min / dos clases; 4 o 5 grupos | Planificación | Fijar los valores antes de imprimir el material | Laboratorio |
| DEC-LAB-011 | **Grabaciones** | Sin grabar / grabar la pantalla / grabar personas | Ética, consentimiento y almacenamiento | Sin grabar; solo notas y conteos | — |
| DEC-LAB-012 | **Desafío del capítulo 10**: confirmar que existe un "salto" analizable y fijar su inicio y su fin | Salto confirmado / reemplazo (por ejemplo, el balanceo de la ventana según SRC-014) / otro capítulo | Validez del protocolo G4 | Confirmarlo en la partida de reconocimiento | Grupo G4 |
| DEC-LAB-013 | **Licencia del arte de P2** (`Assets/cat`, `dog`, `png`, tiles) | Investigar el origen / reemplazar | Distribución de builds | Investigar antes de distribuir APK | Distribución |
| DEC-LAB-014 | **Configuración Android de compilación**: IL2CPP + ARM64 y target API | Cambiar `ProjectSettings` (fase autorizada) / mantenerla | Instalación en dispositivos actuales y publicación en Play | Cambiarla solo en la fase de implementación autorizada | Builds Android |
