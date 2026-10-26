# Guía para alumnos: de la PC a la Xbox

Unidad V · Consolas · Caso guía: *Asteroides* (y el 2D Platformer como transferencia).
Estado: **PROPUESTO**. Su peso en el TP 4 lo define la titular.

## El problema

Tenemos dos juegos que ya corren en PC y en Android. La pregunta es: **si los llevamos a una Xbox, ¿se pueden jugar?** Que compilen no alcanza. En la consola no hay mouse, el jugador está a dos o tres metros de la TV, el control se puede quedar sin batería en plena partida, y el fabricante decide qué está permitido.

La docente va a instalar en su Xbox **dos versiones de cada juego**: la **original**, sin cambios, y una versión **adaptada a consola**. Antes de verla, ustedes predicen qué va a pasar; después, lo comprueban.

## Qué van a hacer

| Parte | Dónde | Necesitan |
|---|---|---|
| 1. Predecir | En el aula o en casa | Esta guía |
| 2. Jugar sin mouse | En su PC, con Unity 6000.3.11f1 | El proyecto del repo; un control de Xbox si tienen (si no, teclado) |
| 3. Comprobar en la consola | Demo de la docente | La tabla de la parte 1 |
| 4. Leer la adaptación | En su PC | El código de `Asteroides-Xbox` |
| 5. Opcional: generar el paquete UWP | En su PC (si tienen Visual Studio) | Ver la sección 5 |

---

## 1. Predecir (antes de la demo)

Completen la columna **"Predigo"** con PASS o FAIL y una razón de una línea. La columna "Resultado" se llena en la demo.

| Prueba | Versión | Predigo (y por qué) | Resultado en la consola |
|---|---|---|---|
| Se instala y abre | Original | | |
| Puedo empezar la partida **solo con el control** | Original | | |
| La nave se mueve con el stick y dispara con A | Original | | |
| Hay un botón resaltado en el menú | Original | | |
| El botón Menu (≡) pausa | Original | | |
| Si se desconecta el control, el juego avisa | Original | | |
| Lo mismo, las seis pruebas | Consola | | |

**Pista para pensar** (sin mirar el código todavía): el porteo a Android agregó el Input System y el gamepad para mover la nave. ¿Eso alcanza para el **menú**?

## 2. Jugar sin mouse (en su PC)

1. Abrir en Unity Hub `proyectos-unity/Asteroides/asteroide-final` (la versión original) y la escena `Game`.
2. Apretar Play y **no tocar el mouse**. Con un control de Xbox, o con el teclado (flechas y Enter/Espacio), intentar empezar la partida.
3. Anotar qué pasa y por qué creen que pasa.
4. Repetir con `proyectos-unity/Asteroides-Xbox` (la versión de consola). ¿Qué cambió en pantalla? Prueben **Esc** (es el "Menu" en el teclado) en medio de la partida.
5. *Transferencia:* hacer lo mismo con `2D-Platformer-Unity-v2` y `2D-Platformer-Xbox` (escena `Menu`).

> En la PC el Editor simula la consola **solo en parte**: el control es el mismo, pero la TV, la distancia, la memoria y el sistema de la consola no lo son. Por eso la demo en la consola sigue haciendo falta.

## 3. Comprobar en la consola (durante la demo)

- Completar la columna **"Resultado"**.
- Marcar cada predicción como **acertada o no** y, si no acertaron, explicar en una línea qué no tuvieron en cuenta.
- Anotar cosas que **no** estaban en la tabla y aparecieron en la TV: tamaño del texto, bordes, tiempo de carga, ruido o pantalla.

## 4. Leer la adaptación (después de la demo)

Abrir `proyectos-unity/Asteroides-Xbox/Assets/Scripts/Console/` y responder:

1. `ConsoleLayer.cs` **no edita ninguna escena**: se instala sola al arrancar. ¿Con qué atributo? ¿Qué ventaja tiene eso para mantener dos versiones del mismo juego?
2. ¿Por qué el juego original no responde al control en el menú? Busquen en `ConsoleLayer` el método que cambia el **módulo de UI** y el que mantiene el **foco**.
3. ¿Cuándo pausa la capa? Busquen las tres causas en `PauseReason`. ¿Por qué el botón Menu **no** pausa cuando hay un menú a la vista?
4. `ConsoleRules.ShouldPauseOnDeviceChange` solo cuenta los mandos **físicos**. ¿Qué error aparecía si contaba también los controles táctiles en pantalla? (Pista: `OnScreenStick` crea un gamepad virtual.)
5. ¿Qué dice la regla de los **26 px a 1080p** y de dónde sale? Busquen `MinBodyTextPxAt1080`.
6. ¿Qué parte del **gameplay** cambió entre la versión original y la de consola?

Para comprobar la respuesta 6, comparen los archivos `Ship.cs` de los dos proyectos.

## 5. Opcional: generar el paquete UWP en su PC

Si tienen Visual Studio 2022 con la carga de trabajo de UWP, las herramientas C++ de UWP y el Windows SDK, pueden generar el mismo paquete que se instaló en la consola:

```powershell
powershell -ExecutionPolicy Bypass -File proyectos-unity\Tools-Xbox\generar_builds_xbox.ps1 -Proyectos Asteroides-Xbox
```

El paquete también incluye la familia **Desktop**, así que pueden instalarlo en su propia PC con Windows (activando *Configuración → Sistema → Para programadores → Modo de desarrollador*) haciendo doble clic en el `.msix`. Antes tienen que instalar el certificado `.cer` en *Personas de confianza* del equipo local. Es la misma build que corre en la consola, pero **en otra máquina**.

## Qué NO resuelve esta adaptación

- **No** es una versión publicable: Microsoft no acepta juegos UWP en la tienda de Xbox. Publicar exige el programa ID@Xbox, el GDK y la certificación (*Xbox Requirements*).
- **No** usa funciones del sistema de Xbox: usuarios, logros, partidas en la nube, suspensión real del sistema.
- **No** mide la "pantalla segura" de la TV ni el rendimiento: eso se observa en la demo.
- Sirve para **Xbox**. Los requisitos de PlayStation (TRC) y de Nintendo (Lotcheck) no son públicos.

## Errores frecuentes y corrección

| Error | Corrección |
|---|---|
| "Si compila para Windows, corre en Xbox" | La Xbox ejecuta paquetes UWP en Developer Mode, o juegos GDK con licencia. Un `.exe` de Windows **no** se instala |
| "Si la nave se mueve con el control, el juego está listo para consola" | El gameplay es una parte. Los menús, el foco, la pausa, el texto a distancia y el ciclo de vida también se juegan con el control |
| "Adaptar a consola es reescribir el juego" | En este caso, el gameplay no se tocó. Se agregó una capa encima |
| "El Developer Mode es un kit de desarrollo" | Es una consola comercial con límites: 5 GB y 4 núcleos exclusivos para un juego UWP |
| "Hay que ocultar Quit porque sí" | En consola, salir de la app es una función del sistema, no del juego |
