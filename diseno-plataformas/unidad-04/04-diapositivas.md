# Unidad 4 — Diapositivas definitivas (texto + notas del docente)

Fuente única de los 4 decks de la Unidad 4. Basado en la arquitectura **aprobada** ([`04-diapositivas-arquitectura.md`](./04-diapositivas-arquitectura.md)).
Para regenerar los `.pptx` después de editar este archivo: `python scripts/build_decks.py` desde `diseno-plataformas/unidad-04/` (requiere `pip install python-pptx`). Opciones: `--decks 1 3` genera solo esos decks; `--version 2` agrega el sufijo `-v2` al nombre del archivo; `--out-dir RUTA` escribe en otra carpeta (útil si el .pptx está abierto). Claves adicionales: `diagrama: Capa: a, b | Capa: c || nota` dibuja capas apiladas con flechas (slide 3 de la Clase 1 v2); `cronologia: Etiqueta: 1972 | *Destacada: 2008 || nota` dibuja una cronología de barras hasta 2026, y el `*` destaca una barra (slide 6); `hitos: 1972 · Nombre · aporte | …` dibuja una línea de tiempo de hitos a todo el ancho (slide 7). También: `flujo: Paso | Paso || nota` (cadena vertical con flechas), `comparacion: +Título: a, b // nota | Título: c, d // nota` (dos columnas; el `+` agrupa los chips en un solo bloque y el `-` los dibuja a la mitad de tamaño), `tiles: 4x7 | rótulo | rótulo de la ampliación` (pantalla dividida en tiles con overdraw), `codigo: ruta/al/archivo.cs:61-73` (lee el código real del repositorio) y `vista: 5 | -8, 8 | 16:9 | 9:16` (pantallas a escala para una cámara ortográfica y un rango de spawn). `safearea: rótulo` dibuja un teléfono con muesca, barra de gestos y zona segura (Clase 2). **Regla:** las slides sin imagen real no llevan recuadro vacío; la sugerencia de imagen queda en las notas.

**Versiones:** los cuatro decks están en su **versión 2** (2026-10-05): texto breve en las slides, notas completas con glosario, sin menciones a clases futuras y gráficos nativos en lugar de recuadros de imagen. Los `.pptx` v1 se conservan como archivos; su texto fuente está en el historial de git (commit `acb7c4c`). Generar todo: `python scripts/build_decks.py --version 2`. El deck 1 en su versión 2: incorpora conceptos del artículo de Kevuru Games, con texto breve en las slides y notas del docente completas. Se genera con `python scripts/build_decks.py --decks 1 --version 2`. La v1 (`Unidad-4-Clase-1-2026.pptx`) se conserva como archivo; su texto fuente está en el historial de git (commit `acb7c4c`).

**Formato que lee el generador (no cambiar la sintaxis):**
- `# DECK n | Título | Subtítulo` empieza un deck.
- `## n | Título` empieza una slide.
- Claves de una línea: `tipo:` (portada / contenido / actividad / demo / cierre), `kicker:` (etiqueta superior), `pregunta:`, `actividad:`, `imagen:`, `video:`, `fuente:`.
- Líneas `- ` = viñetas. Líneas `|` = tabla (la primera fila es el encabezado).
- `notas:` abre las notas del docente, que siguen hasta la próxima slide.
- `imagen:` dibuja un recuadro **[IMAGEN SUGERIDA]** con la descripción; la titular la reemplaza por la imagen real.

---

# DECK 1 | Un teléfono no es una PC chica | Unidad IV · Clase 1 · v2

## 1 | Diseño según Plataforma Móvil
tipo: portada
kicker: UNIDAD IV · CLASE 1 DE 4
- Un teléfono no es una PC chica
- Diseño según Plataformas de Juego · Ing. Elsa Daniela Ramírez · FI – UNJu · 2026
notas:
Imagen sugerida (opcional, sin recuadro en la slide): Teléfono en vertical con Asteroides corriendo, sostenido con una mano.
Presentar la unidad como continuación directa del panorama del 28/09: ese día recorrimos todas las plataformas; desde hoy, y durante cuatro clases, nos quedamos en el bolsillo del jugador.
No anticipar contenidos: la clase arranca con un problema, no con una definición ni con una herramienta.
Versión 2 de la clase (2026-10-05): incorpora conceptos del artículo "What Are the Best Platforms for Games?" de Kevuru Games (definición de plataforma, rol de las tiendas móviles, criterios para elegir plataforma), leído con mirada crítica (slide 20).

## 2 | El juego que anda… hasta que no
tipo: contenido
kicker: APERTURA
- En la PC del aula: perfecto
- En el teléfono, a los 10 min: se traba
- El teléfono quema
- Llamada, volvés… y la nave explotó
pregunta: ¿Cuántos problemas distintos hay? ¿Alguno es un "bug"?
notas:
Glosario (conceptos cortos para la docente):
• Bug: error o defecto que hace que el juego se comporte distinto de lo esperado.
Imagen sugerida (opcional, sin recuadro en la slide): Captura del juego con tres íconos superpuestos: termómetro, batería baja y llamada entrante.
Relato completo: "Asteroides funciona perfecto en la PC del aula. Lo instalamos en un teléfono: a los 10 minutos empieza a trabarse, el teléfono quema en la mano, y si entra una llamada y volvemos, la nave ya explotó y perdimos la partida".
Dejar que discutan 3–4 minutos. Respuesta esperada: al menos tres problemas de distinta naturaleza: (1) calor y rendimiento sostenido, (2) consumo de batería, (3) interrupción del sistema operativo.
Ninguno aparece en el editor y ninguno es un error de lógica en sentido estricto: son supuestos de PC que el juego trae consigo. Esa es la idea de toda la unidad.
No dar todavía las explicaciones: anotarlas en el pizarrón para volver a ellas en las slides 11 a 16.

## 3 | Lo que ya vimos el 28/09
tipo: contenido
kicker: CONTINUIDAD [RECICLADO 28/09]
- Táctil sin botón físico
- Pantallas y zonas seguras
- Batería y temperatura
- Interrupciones del sistema
- Intención ≠ dispositivo
diagrama: Dispositivo: Teclado, Táctil, Gamepad | Intención: Mover, Disparar | Nave: Movimiento, Disparo, Límites || Hoy Ship.cs lee el teclado directo: falta la capa del medio
fuente: Clase 28/09/2026 — Clase2-Plataformas.pptx; código del proyecto (Ship.cs 61–73)
notas:
Glosario (conceptos cortos para la docente):
• Zona segura (safe area): parte de la pantalla libre de muescas, bordes curvos y barras del sistema, donde la interfaz se ve completa.
• Intención: lo que el jugador quiere hacer (mover, disparar), sin importar con qué control lo pide.
• Dispositivo de entrada: el medio físico con el que el jugador da órdenes (teclado, pantalla táctil, gamepad).
Recuperar, no repetir. Las cinco ideas del 28/09, completas:
- Táctil: no hay respuesta física del botón y los dedos tapan la pantalla.
- Pantallas muy variadas: muescas, bordes y zonas seguras.
- Batería y temperatura: si el equipo se calienta, baja el rendimiento.
- Interrupciones: llamadas, notificaciones, cambio de app.
- Separar QUÉ quiere hacer el jugador (mover, disparar) de CÓMO lo pide (teclado, toque, mando).
Diagrama de las tres capas (pedido por la titular, agregado en la v2):
- Dispositivo: CÓMO pide el jugador la acción (teclado, pantalla táctil, gamepad). Es lo que cambia de una plataforma a otra.
- Intención: QUÉ quiere hacer el jugador (mover, disparar). Es independiente del dispositivo.
- Nave: la lógica del juego (movimiento, disparo, límites). No debería saber de dónde vino la orden.
Leerlo de arriba hacia abajo: cada dispositivo se traduce a la misma intención, y la nave solo recibe intenciones. Así, llevar el juego a móvil significa agregar un dispositivo (táctil), no reescribir la nave.
El problema real de Asteroides (nota en rojo de la slide): hoy Ship.cs (líneas 61–73) lee Input.GetKey(KeyCode.Space / LeftArrow / RightArrow) directamente, salteando la capa de intención. Por eso, para pasar a móvil habría que modificar la clase de la nave: es el supuesto S1 del caso práctico, que los alumnos van a encontrar en la actividad A4.2.
En Unity, la capa de intención la ofrece el Input System: las Actions (Move, Fire) separan la acción de sus bindings (teclado, táctil, gamepad). Solo mencionarlo; se trabaja más adelante en la unidad, al diseñar los controles táctiles (On-Screen Controls).
Preguntar: ¿qué partes de la nave NO deberían cambiar al pasar a móvil? Respuesta: la lógica de movimiento, disparo y límites; solo cambia la capa de dispositivo (y los límites, por el aspect ratio, como vamos a ver en la slide 18).
Hoy vamos a ver por qué cada viñeta es una restricción de diseño, con números y fuentes oficiales.

## 4 | Al terminar la unidad podrán
tipo: contenido
kicker: OBJETIVOS
- Explicar las restricciones del móvil
- Detectar supuestos de PC en un juego
- Diseñar controles táctiles medibles
- Defender un modelo de monetización
- Decidir qué probar y dónde
notas:
Glosario (conceptos cortos para la docente):
• Monetización: forma en que el juego genera ingresos (venta, anuncios, compras dentro del juego).
• Supuesto de PC: algo que el juego da por hecho porque fue pensado para PC (por ejemplo, que hay teclado).
Versión completa de los objetivos:
1. Explicar por qué el rendimiento sostenido, la memoria y la batería condicionan el diseño.
2. Detectar en un juego existente los supuestos de PC que fallan en móvil.
3. Diseñar controles y HUD táctiles con medidas verificables (pt, dp, safe area).
4. Elegir y defender un modelo de monetización con sus reglas de tienda y su ética.
5. Decidir qué se prueba en el editor y qué exige un teléfono real.
Remarcar los verbos: explicar, detectar, diseñar, defender, decidir. La unidad no evalúa memorizar especificaciones, sino tomar decisiones justificadas. El TP 3 recorre las cinco.

## 5 | ¿Qué es una plataforma?
tipo: contenido
kicker: CONCEPTO
| Capa | Pregunta | Ejemplos |
| Ejecución | ¿Dónde corre? | Teléfono, consola, PC |
| Distribución | ¿Cómo llega? | Google Play, App Store, Steam |
| Servicio en la nube | ¿Dónde se procesa? | GeForce Now |
| Comunidad | ¿Dónde se mira? | Twitch, YouTube |
pregunta: ¿Cuál de estas capas cambia más el diseño del juego?
fuente: Kevuru Games, "What Are the Best Platforms for Games?" (blog comercial, sin fecha visible; consultado 2026-10-05)
notas:
[Diapositiva nueva en la versión 2.]
Glosario (conceptos cortos para la docente):
• Distribución: canal por el que el juego llega al jugador; en móvil, una tienda digital.
• Servicio en la nube (cloud gaming): el juego corre en un servidor remoto y el jugador recibe la imagen por internet.
• Streaming (Twitch, YouTube): transmisión de video en vivo; acá, gente mirando a otros jugar.
El artículo de Kevuru Games define las plataformas como "la base de cómo los jugadores se conectan con los juegos", ya sea una consola física, un gabinete arcade o un servicio en la nube que corre todo en línea. Y usa una metáfora útil: la plataforma es el escenario donde el juego "actúa", y hay escenarios más grandes que otros.
Pero el artículo mezcla bajo la palabra "plataforma" cuatro cosas distintas: hardware (PlayStation, Xbox, Nintendo), tiendas (Steam, Epic Games Store, Google Play, App Store), servicios de cloud gaming (GeForce Now) y sitios donde se mira jugar (Twitch, YouTube Gaming, Facebook Gaming). La tabla las separa en capas.
Definición de trabajo de esta materia: plataforma = el entorno de ejecución (hardware + sistema operativo) MÁS las reglas de su ecosistema (tienda, certificación, políticas). Por eso en esta unidad hablamos del teléfono y también de Google Play y del App Store.
Respuesta esperada a la pregunta: la capa de ejecución condiciona más el diseño (input, pantalla, rendimiento); la de distribución condiciona el negocio y las reglas (lo vemos más adelante en la unidad); la de comunidad influye en el diseño solo de forma indirecta (juegos pensados para ser vistos, como Among Us).

## 6 | De los arcades al bolsillo
tipo: contenido
kicker: CONTEXTO HISTÓRICO
- Arcade: la primera plataforma (Pong, 1972)
- Consola doméstica y PC
- Portátiles: Game Boy
- Teléfono: el juego va en el bolsillo
- Hoy: XR y nube
cronologia: Arcade · Pong: 1972 | Consola · Atari 2600: 1977 | PC · IBM PC: 1981 | Portátil · Game Boy: 1989 | *Teléfono · App Store: 2008 | XR · Oculus Rift: 2016 | Nube · GeForce Now: 2020 || Cada barra: desde el hito que abre la época hasta 2026
fuente: Kevuru Games (blog); Apple Newsroom (App Store, 10/07/2008); lanzamientos de Oculus Rift (28/03/2016) y GeForce Now (04/02/2020)
notas:
[Diapositiva nueva en la versión 2.]
Glosario (conceptos cortos para la docente):
• Arcade: máquina de juego de uso público que funciona con fichas o monedas.
• XR (realidad extendida): término que agrupa realidad virtual, aumentada y mixta.
• App Store: tienda oficial de aplicaciones de Apple; Google Play es la de Android.
Idea del artículo: cada época tuvo una plataforma que definió cómo se juega. Los arcades fueron las primeras plataformas reales, y además eran espacios sociales.
Los ejemplos de arcade del artículo (Pong, Space Invaders, Pac-Man, Donkey Kong, Galaga, Street Fighter II y Mortal Kombat) se desarrollan con gráfico en la slide siguiente (7).
Conexión con el diseño: el arcade se diseñaba para cobrar por partida (partidas cortas y difíciles, "insert coin"); la consola, para el sillón y la TV; el teléfono, para el bolsillo y las interrupciones. La plataforma siempre moldeó el diseño: no es un fenómeno nuevo.
Dato a remarcar: Asteroids, el juego que inspira nuestro proyecto, es justamente un clásico arcade (Atari, 1979). Estamos llevando un diseño de arcade al teléfono.
Cómo leer la cronología (pedido de la titular): cada barra arranca en el hito que abre una época y llega hasta hoy (2026). Las barras no "terminan" porque ninguna plataforma desapareció: los arcades, las consolas y la PC siguen vigentes, y cada época nueva se SUMA a las anteriores en lugar de reemplazarlas. La barra destacada es la del teléfono (2008, lanzamiento del App Store), la época de esta unidad.
Hitos usados: Pong (1972, arcade); Atari 2600 (1977, popularizó la consola doméstica con cartuchos); IBM PC (1981); Game Boy (1989); App Store (10/07/2008, verificado en Apple Newsroom); Oculus Rift (28/03/2016, primer visor de VR de consumo masivo); GeForce Now (04/02/2020, lanzamiento comercial del cloud gaming de NVIDIA). Son hitos de referencia, no "inventos" de cada época: por ejemplo, la primera consola doméstica fue la Magnavox Odyssey (1972) y en PC se jugaba antes de 1981.
Pregunta posible: ¿qué tiene de distinto la época del teléfono respecto de las anteriores? Respuesta esperada: el jugador no compra el dispositivo para jugar, porque ya lo lleva en el bolsillo por otros motivos; por eso el juego compite con llamadas, mensajes y notificaciones (lo que vemos hoy en las slides 13 y 14).
No detenerse más de 3 minutos: es contexto, no contenido evaluable.

## 7 | Clásicos del arcade
tipo: contenido
kicker: CONTEXTO HISTÓRICO
hitos: 1972 · Pong · tenis en pantalla | 1978 · Space Invaders · nace el shooter | 1980 · Pac-Man · fenómeno cultural | 1981 · Donkey Kong · debuta Mario | 1981 · Galaga · riesgo y recompensa | 1991 · Street Fighter II · comunidad de pelea | 1992 · Mortal Kombat · lleva a la ESRB
pregunta: ¿Qué diseño impone una máquina que cobra por partida?
fuente: Kevuru Games (blog); ESRB: Game Developer, "A Brief History of the ESRB"
notas:
[Diapositiva nueva en la versión 2, pedida por la titular: los ejemplos del artículo, con gráfico.]
Glosario (conceptos cortos para la docente):
• Shooter: juego de disparos.
• ESRB (Entertainment Software Rating Board): organismo que clasifica los videojuegos por edad en EE. UU. y Canadá.
Los ejemplos que da el artículo de Kevuru Games, con lo que aportó cada uno:
- Pong (1972): dos paletas y una pelota. Se lo llama "el abuelo de los videojuegos": para mucha gente fue la primera vez que una pantalla de TV resultó interactiva.
- Space Invaders (1978): filas de alienígenas que bajan y una música que se acelera hasta poner nervioso a cualquiera. Según el artículo, prácticamente inventó la plantilla del género shooter.
- Pac-Man (1980): un círculo amarillo comiendo puntos en un laberinto que se volvió un fenómeno cultural (dibujos animados, cereales y merchandising).
- Donkey Kong (1981): primera aparición de Mario, entonces llamado "Jumpman". Subir escaleras y esquivar barriles: el comienzo de los juegos de plataformas.
- Galaga (1981): los enemigos podían capturar tu nave y, si la recuperabas, duplicabas tu poder de fuego. Riesgo y recompensa en una sola mecánica.
- Street Fighter II (1991): en los arcades de los 90 estaba en el centro de la escena; rivalidades y combos que construyeron la comunidad de los juegos de pelea.
- Mortal Kombat (1992): tan conocido por su polémica como por su jugabilidad. Sus personajes digitalizados y las "Fatalities" contribuyeron a la creación de la ESRB. Dato verificado: tras las audiencias del Congreso de EE. UU. de diciembre de 1993, donde se mostraron Mortal Kombat y Night Trap, la industria creó en 1994 la ESRB como sistema voluntario de clasificación por edades (Game Developer, "A Brief History of the ESRB"). La retomamos en la Unidad V (certificación y clasificación).
Las fechas son las de lanzamiento original en arcade, según el artículo. Coinciden con las fuentes de referencia habituales, pero no se verificaron una por una en esta sesión.
Respuesta esperada a la pregunta: una máquina que cobra por ficha impone partidas cortas, dificultad creciente y un "Game Over" que invita a pagar de nuevo. Conexión con móvil: ese mismo patrón reaparece en el "continuar" con un anuncio o con una compra (lo analizamos más adelante en la unidad, al ver monetización). Y Asteroids, el juego que inspira nuestro proyecto, también es un clásico arcade de esa época (Atari, 1979).
Recorrer el gráfico de izquierda a derecha y no detenerse más de 3 minutos.

## 8 | Las tiendas cambiaron quién publica
tipo: contenido
kicker: DISTRIBUCIÓN MÓVIL
- Estudios chicos llegan a millones
- Éxitos casuales: Candy Crush, Clash of Clans
- Éxito tardío: Among Us
- Marcas grandes también: PUBG Mobile
pregunta: Si cualquiera puede publicar, ¿qué hace que un juego se encuentre?
fuente: Kevuru Games (blog, consultado 2026-10-05)
notas:
[Diapositiva nueva en la versión 2.]
Glosario (conceptos cortos para la docente):
• Juego casual: juego de reglas simples y partidas cortas, pensado para un público amplio.
Idea del artículo: con Google Play y el App Store, "los estudios pequeños e incluso desarrolladores solos" pudieron poner sus juegos frente a millones de personas. Los ejemplos que da:
- Éxitos casuales que atrajeron jugadores de todo el mundo: Candy Crush y Clash of Clans.
- Among Us se volvió viral años después de su lanzamiento (salió en 2018 y explotó en 2020).
- Marcas de consola que funcionan en el teléfono: PUBG Mobile y FIFA Mobile.
Conclusión del artículo: el juego móvil no es una moda pasajera, es una parte central de la industria.
Matiz docente (importante): que la tienda esté abierta no significa que no tenga reglas. Para publicar hay que cumplir políticas de pago, de anuncios, de privacidad y de nivel de API (lo vemos más adelante en la unidad). Y que cualquiera pueda publicar crea otro problema: la visibilidad entre millones de juegos.
Respuesta esperada a la pregunta: la visibilidad depende de la propia tienda (búsqueda, destacados, calificaciones), de la comunidad (streamers, boca en boca) y de la calidad técnica (Android vitals puede bajar la visibilidad de un juego con muchos cierres inesperados; lo vemos más adelante en la unidad).

## 9 | Adentro del teléfono
tipo: contenido
kicker: LA MÁQUINA
- CPU, GPU y memoria en un chip (SoC)
- Comparten energía y calor
- Núcleos y relojes variables
- Sin ventilador
fuente: Android Developers — ADPF; Arm GPU Best Practices §2.3
comparacion: +Teléfono: CPU, GPU, Memoria // Un solo chip (SoC), sin ventilador | PC: CPU, GPU dedicada, RAM // Componentes separados, con ventiladores
notas:
Glosario (conceptos cortos para la docente):
• SoC (System on a Chip): un solo chip que integra CPU, GPU, memoria y otros componentes.
• CPU (unidad central de procesamiento): ejecuta la lógica del juego (reglas, física, IA).
• GPU (unidad de procesamiento gráfico): dibuja la imagen que se ve en pantalla.
• Núcleo: cada unidad de procesamiento dentro de la CPU; los teléfonos combinan núcleos de distinta potencia.
• Reloj (frecuencia): velocidad a la que trabaja un procesador; se mide en GHz.
En un teléfono, CPU, GPU y memoria viven en un mismo chip (SoC, System on a Chip). Comparten la energía de la batería y el calor que generan. El calor se disipa por la carcasa: no hay ventilador.
La documentación de Android (ADPF) menciona explícitamente la diversidad de topologías de núcleos (núcleos de distinto tamaño y potencia) y los relojes que cambian en tiempo real como complejidades propias del móvil, que no existen en PC ni en consola.
No dar arquitectura de hardware: alcanza con la idea de que todo comparte energía y calor.
Pregunta rápida: ¿qué pasa con la GPU si la CPU se calienta? Respuesta: comparten el presupuesto térmico; si uno se calienta, ambos pueden bajar su frecuencia.

## 10 | Dibujar dos veces cuesta más
tipo: contenido
kicker: LA MÁQUINA
- GPU por tiles (TBDR)
- Memoria = ancho de banda = batería
- Overdraw: el mismo píxel varias veces
- Partículas y transparencias pesan más
fuente: Apple — Tailor your apps for Apple GPUs and TBDR; Arm GPU Best Practices §2.3, p. 15
tiles: 4x7 | 1 tile ampliado | Partículas superpuestas: el mismo píxel se pinta 3 veces (overdraw)
notas:
Glosario (conceptos cortos para la docente):
• Tile: porción rectangular de la pantalla; la GPU móvil dibuja la imagen tile por tile.
• TBDR (Tile-Based Deferred Rendering): técnica de dibujo por tiles que usan las GPU móviles.
• Ancho de banda de memoria: cantidad de datos que se pueden leer o escribir en memoria por segundo.
• Overdraw: pintar el mismo píxel más de una vez en un mismo cuadro.
• Píxel: cada punto de la imagen en pantalla.
• Partículas: muchos elementos gráficos pequeños (chispas, humo) que forman un efecto.
Las GPU móviles dibujan la pantalla por porciones (tiles): técnica TBDR, tile-based deferred rendering. Leer y escribir memoria consume ancho de banda, y el ancho de banda consume batería.
Overdraw: pintar varias veces el mismo píxel, típico de transparencias y partículas. Por eso una explosión con muchas partículas pesa más en un teléfono que en una PC.
Citas de Arm para leer en voz alta: "Overdraw causes excess memory bandwidth use" y "Excess memory bandwidth use causes excess power use".
Llegar solo hasta acá: no explicar el pipeline de la GPU. Conectar con Asteroides: la explosión de la nave usa partículas con transparencia, candidata a medir en el teléfono, más adelante en la unidad.

## 11 | Pico vs. sostenido
tipo: contenido
kicker: LA MÁQUINA · CONCEPTO CLAVE
- Calor → throttling → caen los fps
- Importa el minuto 10, no el 1
- Usar ~65 % del tiempo de frame
pregunta: ¿Cómo medirían que un juego es "estable"?
video: WWDC19 sesión 422 (Apple), 19:40–31:00 — tarea
fuente: Unity e-book Optimize… mobile, XR and web (Unity 6), p. 19; Android Thermal API
flujo: Uso intenso del chip | Sube la temperatura | Throttling: baja la frecuencia | Caen los fps || Por eso importa el fps del minuto 10
notas:
Glosario (conceptos cortos para la docente):
• fps (frames per second): cantidad de imágenes que el juego dibuja por segundo.
• Throttling térmico: reducción automática de la frecuencia del procesador para que no se sobrecaliente.
• Tiempo de frame (frame time): tiempo que tarda en prepararse un cuadro; a 30 fps son 33,3 ms y a 60 fps, 16,7 ms.
• ms: milisegundo, la milésima parte de un segundo.
• Refrigeración activa: ventiladores u otros sistemas que extraen el calor; los teléfonos no la tienen.
Es el concepto más importante de la clase.
Cadena causal: el chip se calienta → el sistema baja la frecuencia de CPU y GPU para protegerlo (throttling) → caen los fps. Lo que importa es el fps del minuto 10, no el del minuto 1.
Recomendación de Unity: usar alrededor del 65 % del tiempo de frame disponible, es decir, ~22 ms a 30 fps y ~11 ms a 60 fps. Motivo oficial textual: "Most mobile devices do not have active cooling".
Respuesta esperada a la pregunta: medir durante un tiempo largo (10 minutos o más), registrar el frame time (no solo el promedio de fps) y hacerlo en un dispositivo de gama baja.
Para mencionar, sin profundizar: Android ofrece getThermalHeadroom e iOS ofrece thermalState para que el juego reaccione al calor; Unity 6.3 trae Adaptive Performance como módulo integrado.

## 12 | 30 fps no es un error
tipo: contenido
kicker: LA MÁQUINA · BATERÍA
- Unity móvil: 30 fps por defecto
- 60 fps = el doble de trabajo
- El fps es una decisión de diseño
fuente: Unity 6.3 Scripting API — Application.targetFrameRate; Android — Optimize power efficiency
notas:
Glosario (conceptos cortos para la docente):
• targetFrameRate: opción de Unity que fija los fps objetivo del juego.
• Frecuencia de refresco: veces por segundo que se actualiza la pantalla; se mide en Hz.
• Frame pacing: entregar los cuadros a intervalos regulares, sincronizados con la pantalla.
En Android e iOS, por defecto Unity renderiza a 30 fps fijos "to conserve battery power" (texto de la documentación de Application.targetFrameRate: abrir la página y leer la frase).
60 fps duplica el trabajo por segundo: más calor y menos batería. Elegir el fps es una decisión de diseño, no un detalle técnico.
En Asteroides no se define targetFrameRate: nadie tomó la decisión (supuesto S12 del caso práctico).
Preguntar: ¿qué juegos necesitan 60 fps y cuáles no? Respuesta: acción rápida o competitiva sí; puzzle, estrategia o narrativa, generalmente no.
Android recomienda además igualar la frecuencia de refresco de la pantalla al fps objetivo (frame pacing).

## 13 | El sistema operativo manda
tipo: contenido
kicker: LA MÁQUINA · CICLO DE VIDA
- Salir de la app = segundo plano
- Sin memoria, el SO cierra procesos
- onTrimMemory no lo evita
- Diseño: guardar estado
fuente: Android — Low memory killers (2026-09-21); Apple — applicationDidReceiveMemoryWarning
flujo: Jugando | Llamada o cambio de app | Segundo plano | Falta memoria: el sistema cierra el juego || Si no se guardó el estado, la partida se pierde
notas:
Glosario (conceptos cortos para la docente):
• Segundo plano: estado de una app que sigue abierta pero no se ve ni recibe input.
• Proceso: programa en ejecución.
• Low Memory Killer: componente de Android que cierra procesos cuando falta memoria.
• onTrimMemory: aviso de Android a una app para que libere memoria.
• Estado: datos de la partida (posición, puntaje, vidas) que hay que guardar para poder retomarla.
Cuando el jugador sale de la app (llamada, notificación, cambio de app), el juego pasa a segundo plano. Si falta memoria, el sistema operativo cierra procesos en segundo plano: en Android lo hace el Low Memory Killer; en iOS, el sistema termina la app si no libera memoria.
Corrección de un mito frecuente: los callbacks onTrimMemory de Android NO evitan el cierre. Android los declara deprecados salvo dos niveles (UI_HIDDEN y BACKGROUND) y dice textualmente que "haven't been helpful at preventing low-memory kills".
Conclusión de diseño: el juego puede morir sin aviso. Si puede retomarse, hay que guardar estado; si no puede, al menos no castigar al jugador por algo que hizo el sistema.

## 14 | Qué hace Unity con eso
tipo: contenido
kicker: LA MÁQUINA · UNITY
- OnApplicationPause(bool)
- OnApplicationFocus(bool)
- Teclado en Android → pierde el foco
- Asteroides no los usa (S8)
fuente: Unity 6.3 Scripting API — MonoBehaviour.OnApplicationPause / OnApplicationFocus
notas:
Glosario (conceptos cortos para la docente):
• Callback: función que el motor o el sistema llama automáticamente cuando ocurre un evento.
• OnApplicationPause / OnApplicationFocus: callbacks de Unity para cuando la app pasa a segundo plano o pierde el foco.
• Foco: la app está al frente y recibe el input del jugador.
• MonoBehaviour: clase base de los scripts de Unity.
OnApplicationPause(bool) avisa que la app pasa a segundo plano o vuelve. OnApplicationFocus(bool) avisa que la app pierde o recupera el foco. Dato práctico: en Android, abrir el teclado en pantalla dispara OnApplicationFocus(false).
Asteroides no implementa ninguno de los dos (supuesto S8 del caso práctico).
No escribir código todavía: eso se hace más adelante en la unidad, con el defecto deliberado. Solo mostrar que el motor avisa y que el juego base no escucha.
Anticipar: ¿alcanza con escuchar el aviso? No: si el sistema mata el proceso, no se llama nada.

## 15 | Actividad A4.1 — Diagnóstico
tipo: actividad
kicker: ACTIVIDAD · 15 MIN · PAREJAS
| Reporte del jugador | ¿Restricción? | ¿Evidencia? | ¿Qué prueba? |
| Se cerró al volver de WhatsApp | | | |
| A los 10 min se traba y quema | | | |
| Pausa bajo la cámara | | | |
| Score diminuto en la tablet | | | |
| Sin batería en media hora | | | |
| En el emulador anda, en mi teléfono no | | | |
actividad: Una restricción por fila. Prohibido "el teléfono es lento".
notas:
Glosario (conceptos cortos para la docente):
• Emulador: programa que imita un teléfono dentro de la PC.
• Restricción de plataforma: límite que impone el dispositivo o su sistema operativo.
• Evidencia: dato que permite confirmar un problema (modelo del teléfono, capturas, video, registros).
Consigna completa: para cada reporte, indicar (a) la restricción de plataforma más probable, (b) qué evidencia le pedirían al tester, y (c) qué tipo de prueba lo habría detectado antes.
Respuestas esperadas (detalle en 05, A4.1):
1. Ciclo de vida / Low Memory Killer → QA manual en dispositivo.
2. Térmica → rendimiento sostenido en dispositivo.
3. Safe area → Device Simulator + dispositivo.
4. Escalado de UI → Device Simulator con varios perfiles.
5. fps y energía → medición en dispositivo.
6. El emulador no representa el rendimiento → Profiler en un teléfono de gama baja.
Error típico a corregir: proponer un unit test para los casos 2, 3 o 5. Recordar pedir siempre el modelo del dispositivo.

## 16 | Demo: el simulador y sus límites
tipo: demo
kicker: DEMO EN VIVO
- Player Settings de Android
- Device Simulator: qué simula
- Y qué NO simula
- Asteroides en vertical
fuente: Unity 6.3 Manual — Device Simulator introduction; Android Player settings
notas:
Glosario (conceptos cortos para la docente):
• Player Settings: configuración del proyecto de Unity para cada plataforma de destino.
• Device Simulator: ventana de Unity que muestra el juego con la forma de pantalla de un dispositivo real.
• Nivel de API de Android: número que identifica cada versión de Android (por ejemplo, API 36 = Android 16).
• Application Category: categoría con la que Unity declara la app ante Android; para juegos, "Game".
• Giroscopio: sensor que mide la rotación del teléfono.
Imagen sugerida (opcional, sin recuadro en la slide): Device Simulator con Asteroides en vertical y los asteroides apareciendo fuera de pantalla.
Pasos de la demo:
1. Player Settings de Android: Application Category = Game (por defecto en Unity 6.3; exime a los juegos del cambio de Android 16 que ignora la orientación en pantallas grandes), orientación y API mínima.
2. Abrir la página oficial del Device Simulator y leer la lista de lo que NO simula ANTES de usarlo: rendimiento, memoria, capacidades de render y giroscopio. La herramienta llega con sus límites.
3. Lo que sí simula: safe area, rotación y toque de un dedo.
4. Poner Asteroides en un perfil de teléfono en vertical. Confirmar en vivo el supuesto de que la cámara está centrada en x = 0.
No revelar todavía el problema del spawn: lo descubren en A4.2.

## 17 | Actividad A4.2 — Supuestos de PC
tipo: actividad
kicker: ACTIVIDAD · 20 MIN · GRUPOS
- Ship.cs 61–73: el control
- Ship.cs 46–47 y 99–115: los límites
- Spawner.cs 101–106: el spawn
- Prefab Game: Canvas y cámara
actividad: 5 supuestos: dónde (archivo:línea), qué pasaría, qué eje.
codigo: ../../proyectos-unity/Asteroides/asteroide-final/Assets/Scripts/Ship.cs:61-73
notas:
Glosario (conceptos cortos para la docente):
• Spawn: aparición de un objeto en el juego; acá, los asteroides.
• Prefab: objeto de Unity guardado como plantilla reutilizable.
• Canvas: contenedor de la interfaz (UI) en Unity.
• Input.GetKey: lectura directa de una tecla en el sistema de input clásico de Unity.
Consigna completa: listar al menos 5 supuestos que dejan de valer en un teléfono, indicando dónde están (archivo:línea), qué pasaría en móvil y a qué eje pertenecen (input, pantalla, UI, ciclo de vida, rendimiento).
La respuesta completa es la tabla S1–S13 de 02-caso-practico. Para aprobar alcanza con S1 (teclado), S3/S4/S5 (límites, cámara, spawn), S6 (Canvas en Constant Pixel Size) y S8 (sin pausa).
Pista si se traban: "¿qué pasa con la cámara si la pantalla es más angosta que alta?".

## 18 | Lo que encontramos
tipo: contenido
kicker: PUESTA EN COMÚN
- Vista: 5 × aspect a cada lado
- 16:9 → ≈ 8,9 · vertical → ≈ 2,8
- Spawn en x ∈ [−8, 8]
- En vertical, nacen fuera de pantalla
fuente: Código del proyecto (Spawner.cs:101-106; prefab Game, Camera)
vista: 5 | -8, 8 | 16:9 | 9:16
notas:
Glosario (conceptos cortos para la docente):
• Cámara ortográfica: cámara sin perspectiva; su tamaño (orthographicSize) es la mitad de la altura visible, en unidades del mundo.
• Relación de aspecto (aspect ratio): ancho dividido por alto de la pantalla (16:9, 9:16).
• Coordenadas de mundo: posiciones dentro de la escena, independientes de la pantalla.
La cámara es ortográfica de tamaño 5: el semiancho visible es 5 × aspect. A 16:9 se ven ≈ 8,9 unidades a cada lado; en vertical 9:16, ≈ 2,8.
El Spawner crea asteroides en x ∈ [−8, 8] (coordenadas de mundo). En vertical, la mayoría de los asteroides nace fuera de pantalla.
No hay error de lógica: hay un supuesto de plataforma. Ningún archivo tiene un error por sí solo; el problema aparece en la combinación cámara + spawner + orientación.
Mostrarlo en el Device Simulator. Conectar con el testing de integración de la U3: es un defecto de integración con la plataforma.

## 19 | ¿Cómo se elige una plataforma?
tipo: contenido
kicker: DECISIÓN
- Audiencia
- Modelo de monetización
- Herramientas y soporte
- Vigencia en el tiempo
- + Restricciones técnicas (hoy)
pregunta: Con estos criterios: ¿Asteroides es un juego para móvil?
fuente: Kevuru Games (blog, consultado 2026-10-05) + criterio de la cátedra
notas:
[Diapositiva nueva en la versión 2.]
Glosario (conceptos cortos para la docente):
• Audiencia: público al que apunta el juego.
• Vigencia (future-proofing): que la plataforma siga activa y evolucionando con el tiempo.
El artículo de Kevuru propone cuatro consideraciones para elegir plataforma, y concluye que el desafío no es encontrar la "mejor" plataforma, sino la que encaja con la visión del juego y su público:
1. Audiencia: saber para quién se construye. Un puzzle casual puede encontrar su público en móvil; un RPG con mucha narrativa puede funcionar mejor en consola o PC.
2. Modelos de monetización: suscripción, free-to-play con compras integradas o venta premium. Cada plataforma se inclina por estrategias distintas y el modelo de ingresos tiene que coincidir.
3. Integración y soporte: algunas plataformas ofrecen mejores herramientas, documentación o ayuda directa; una buena integración ahorra meses.
4. Vigencia (future-proofing): preferir plataformas que sigan evolucionando para que el juego no quede desactualizado en uno o dos años.
Lo que agrega la cátedra: un quinto criterio, las restricciones técnicas y de diseño de la plataforma (todo lo que vimos hoy: calor, batería, memoria, interrupciones, pantalla). El artículo no lo menciona y es justamente el núcleo de esta materia.
Respuesta esperada a la pregunta: Asteroides encaja en móvil por audiencia (partidas cortas y casuales) y por sus requisitos técnicos bajos, pero exige rediseñar el control, la pantalla y la pausa (lo que encontramos en A4.2). La monetización se decide más adelante en la unidad.

## 20 | Leer con lupa
tipo: actividad
kicker: LECTURA CRÍTICA · 5 MIN
- Lo escribe un estudio que vende servicios
- Google Stadia: cerró el 18/01/2023
- "Origin": reemplazada por la EA app (2022)
- Cifras de mercado sin fuente
actividad: Antes de citar un dato, busquen la fuente primaria.
fuente: Google — mensaje oficial sobre el cierre de Stadia (2022); EA — anuncio de la EA app (06/10/2022)
notas:
[Diapositiva nueva en la versión 2.]
Glosario (conceptos cortos para la docente):
• Fuente primaria: documento original de quien produce el dato (por ejemplo, el comunicado oficial de la empresa).
• Stadia: servicio de cloud gaming de Google (2019–2023).
• EA app: lanzador de juegos de PC de Electronic Arts, que reemplazó a Origin.
El artículo que usamos para las slides 5, 6, 7, 8 y 19 es útil para los conceptos, pero tiene problemas que conviene mostrar:
1. Es el blog de un estudio de desarrollo (Kevuru Games) que termina ofreciendo sus servicios y un formulario de cotización: es una fuente comercial, no una autoridad.
2. Presenta Google Stadia como un servicio activo. Google anunció el cierre el 29/09/2022 y fue efectivo el 18/01/2023, con reembolsos (verificado en la investigación de la Unidad VII, fuente oficial de Google).
3. Nombra la tienda "Origin" entre las plataformas de PC. EA anunció el 06/10/2022 que la EA app la reemplaza como su plataforma principal de PC (fuente oficial de EA).
4. Da cifras de ingresos y usuarios proyectadas desde 2023 (por ejemplo, ingresos del sector y cantidad de usuarios a 2027) sin citar de dónde salen. No las usamos en clase.
5. Mezcla bajo "plataforma" hardware, tiendas, cloud y sitios de streaming (lo ordenamos en la slide 5).
Mensaje para los alumnos: el mismo criterio que aplicamos a los tests (¿qué demuestra y qué no?) se aplica a las fuentes. Un blog sirve para ideas; los datos se verifican en la documentación oficial o en papers. Es el mismo criterio que van a usar en el TP 3.

## 21 | Qué no resuelve esto · TP 3
tipo: cierre
kicker: CIERRE
- El simulador no mide calor ni batería
- Eso se mide en su teléfono
- TP 3: Dossier Asteroides móvil
- Tarea: Build Support + depuración USB
fuente: Unity 6.3 Manual — Android environment setup; Android — Configure on-device developer options
notas:
Glosario (conceptos cortos para la docente):
• Build Support: módulo de Unity que permite compilar el juego para una plataforma; acá, Android.
• Depuración USB: opción de Android que permite a la PC instalar y analizar apps en el teléfono por cable.
• TP: trabajo práctico.
Cerrar con el límite de la herramienta, no con la herramienta: el simulador encontró el problema de la pantalla, pero no mide calor ni batería. Eso lo vamos a medir en sus teléfonos, más adelante en la unidad.
TP 3: Dossier de plataforma, Asteroides móvil (consigna en el aula virtual).
Tarea técnica obligatoria (sin ella no se puede hacer la práctica en el teléfono):
1. Instalar el módulo Android Build Support (con OpenJDK, Android SDK y NDK) en Unity 6000.3.11f1 desde Unity Hub.
2. En el teléfono: tocar 7 veces "Número de compilación" para habilitar las Opciones de desarrollador y activar "Depuración USB" (en Android 9 o superior: Ajustes > Sistema > Avanzado > Opciones de desarrollador).

# DECK 2 | Diseñar para el pulgar | Unidad IV · Clase 2 · v2

## 1 | Diseñar para el pulgar
tipo: portada
kicker: UNIDAD IV · CLASE 2 DE 4
- UI táctil, pantallas y accesibilidad
- Diseño según Plataformas de Juego · FI – UNJu · 2026
notas:
Recordar de dónde venimos: la Clase 1 fue la máquina (calor, batería, memoria, sistema operativo). Hoy: las manos y la pantalla.
Imagen sugerida (opcional, sin recuadro en la slide): mano sosteniendo un teléfono, con el arco de alcance del pulgar dibujado.

## 2 | ¿Cuánto mide un dedo?
tipo: contenido
kicker: APERTURA
- Score bajo la cámara
- Botón de inicio diminuto
- El pulgar tapa la acción
pregunta: ¿Qué tamaño mínimo debería tener un botón?
notas:
Glosario (conceptos cortos para la docente):
• HUD: información superpuesta al juego (puntaje, vidas, botones).
• Muesca (notch): recorte de la pantalla donde van la cámara y los sensores.
Situación completa: en un teléfono con muesca, el score de Asteroides queda debajo de la cámara frontal; el botón de inicio, pensado para un mouse, es diminuto; y el pulgar tapa justo la zona por donde caen los asteroides.
Dejar que propongan números en píxeles y mostrar que la respuesta en píxeles no sirve (slide 4). Recuperar el supuesto S6 de la Clase 1 (Canvas en Constant Pixel Size).
Imagen sugerida (opcional, sin recuadro en la slide): captura del HUD de Asteroides en un teléfono con muesca.

## 3 | Hay mínimos oficiales
tipo: contenido
kicker: UI TÁCTIL
| Plataforma | Tamaño mínimo táctil | Fuente |
| iOS | 44 × 44 pt (mínimo 28 × 28) | Apple HIG |
| Android | 48 × 48 dp | Android Developers |
| visionOS (referencia) | 60 × 60 pt | Apple HIG |
fuente: Apple HIG — Buttons, Accessibility; Android — Make apps more accessible
notas:
Glosario (conceptos cortos para la docente):
• pt (punto): unidad de Apple independiente de la densidad de la pantalla.
• dp (density-independent pixel): unidad equivalente de Android.
• Objetivo táctil: área de la pantalla que responde a un toque.
• HIG (Human Interface Guidelines): guías de diseño oficiales de Apple.
Son números verificables: convierten "botón cómodo" en un criterio de prueba.
Detalle: Apple pide 44 × 44 pt por defecto, con un mínimo absoluto de 28 × 28 pt; Android pide al menos 48 × 48 dp, "Larger is even better". Apple sugiere separar los controles ~12 pt si tienen borde visible y ~24 pt si no lo tienen.
Para juegos en iOS, Apple fija además texto de 17 pt por defecto y 11 pt como mínimo (HIG, Designing for games).

## 4 | pt, dp, px
tipo: contenido
kicker: UI TÁCTIL · DENSIDAD
- px: puntos físicos de pantalla
- pt y dp: independientes de la densidad
- Unity: el Canvas Scaler decide
comparacion: Baja densidad: Botón de 100 px // Se ve grande | -Alta densidad: Botón de 100 px // El mismo botón se ve chico (esquema, no a escala exacta)
fuente: Unity uGUI 2.0 — Canvas Scaler; Designing UI for Multiple Resolutions
notas:
Glosario (conceptos cortos para la docente):
• Densidad de pantalla: cantidad de píxeles por pulgada; cuantos más, más chico se ve cada píxel.
• px (píxel): punto físico de la pantalla.
• Canvas Scaler: componente de Unity que decide cómo escala la interfaz según la pantalla.
Idea: el mismo botón de 100 px es grande en un teléfono viejo y diminuto en uno de alta densidad. Por eso se diseña en unidades independientes de la densidad (pt, dp) y se deja que el motor escale.
Modos del Canvas Scaler: Constant Pixel Size (el que usa Asteroides), Scale With Screen Size y Constant Physical Size. No hace falta la fórmula de conversión.

## 5 | No todo el rectángulo es tuyo
tipo: contenido
kicker: UI TÁCTIL · SAFE AREA
- Muescas, bordes y barras
- Screen.safeArea en Unity
- UI esencial adentro
safearea: Zona segura (safe area)
fuente: Unity 6.3 — Screen.safeArea; Android — Support display cutouts
notas:
Glosario (conceptos cortos para la docente):
• Safe area (zona segura): rectángulo de la pantalla donde la interfaz se ve completa, sin muescas ni barras del sistema.
• Cutout: recorte de la pantalla (muesca o cámara perforada).
• Edge-to-edge: el contenido ocupa la pantalla de borde a borde.
• Barra de gestos: franja inferior que el sistema usa para navegar.
Detalle: muescas, cámaras perforadas, bordes curvos y barras de gestos ocupan partes de la pantalla. Screen.safeArea devuelve el rectángulo donde la interfaz está a salvo, en píxeles.
En Android 15 con target SDK 35, el contenido va de borde a borde obligatoriamente; Unity ignora la opción "Render Outside Safe Area". Por eso hay que leer safeArea y no confiar en que el sistema deje márgenes.
La UI esencial va dentro de la safe area; el fondo puede salir de ella.
Android permite simular un cutout desde las opciones de desarrollador: útil para la práctica en el teléfono, más adelante en la unidad.

## 6 | Dónde llega el pulgar
tipo: contenido
kicker: ERGONOMÍA [RECICLADO 28/09]
- Una mano, dos manos, acunado
- El agarre cambia todo el tiempo
- HUD editable: CoD Mobile, Fortnite
pregunta: ¿Qué zona tapa el pulgar que dispara?
fuente: Hoober, UXmatters 2013 (profesional); Activision blog CoD Mobile 2019; Epic — Fortnite mobile development
notas:
Glosario (conceptos cortos para la docente):
• Ergonomía: adaptación del diseño al cuerpo de quien lo usa.
• Agarre: forma de sostener el teléfono (una mano, dos manos, acunado).
Datos de Hoober (2013, 1.333 personas observadas): 49 % una mano, 36 % acunado, 15 % dos manos; los usuarios cambian de agarre todo el tiempo.
Advertencia para decir en clase: es una fuente profesional, no académica, y tiene más de una década, con teléfonos más chicos que los actuales. Sirve como disparador, no como norma.
CoD Mobile y Fortnite permiten mover y redimensionar los controles del HUD: una respuesta de diseño a la diversidad de manos y de teléfonos.
Imagen sugerida (opcional, sin recuadro en la slide): HUD táctil con las zonas de los pulgares superpuestas.

## 7 | Vertical u horizontal
tipo: contenido
kicker: PANTALLA · ORIENTACIÓN
- Cambia el campo de juego
- Asteroides arranca en AutoRotation
- Android 16 exceptúa a los juegos
vista: 5 | -8, 8 | 16:9 | 9:16
pregunta: ¿Asteroides es vertical u horizontal?
fuente: Android 16 behavior changes; Unity 6.3 Android Player settings; código del proyecto
notas:
Glosario (conceptos cortos para la docente):
• AutoRotation: la pantalla gira sola cuando el jugador gira el teléfono.
• Orientación: vertical (portrait) u horizontal (landscape).
El gráfico es el mismo hallazgo de la Clase 1, a escala: en vertical, la mayor parte del rango de spawn queda fuera de la pantalla.
Detalle: Android 16 ignora las restricciones de orientación en pantallas grandes, salvo en juegos; Unity 6.3 marca Application Category = Game por defecto.
No hay una respuesta correcta única: vertical favorece una mano; horizontal favorece el campo de visión y los dos pulgares. Se evalúa que la decisión considere sus consecuencias (rango de spawn, límites, HUD).

## 8 | Gestos
tipo: contenido
kicker: INTERACCIÓN
- No redefinir gestos del sistema
- Gesto propio: nunca la única vía
- No depender de gestos (Android)
comparacion: Un dedo: Tocar, Deslizar, Arrastrar, Mantener // Gestos estándar | Dos dedos: Pellizcar // Zoom y escala
fuente: Apple HIG — Gestures; Android — accessibility
notas:
Glosario (conceptos cortos para la docente):
• Gesto: movimiento del dedo sobre la pantalla que el sistema interpreta como una orden.
• Gestos del sistema: los que usa el sistema operativo (volver, ir al inicio, abrir notificaciones).
• Descubribilidad: qué tan fácil es que el jugador encuentre una función sin que se la expliquen.
Detalle: los gestos estándar son tocar, deslizar, arrastrar, mantener y pellizcar. No hay que redefinir los gestos del sistema. Un gesto inventado nunca debe ser la única forma de hacer algo importante (Apple), y las apps no deberían depender de gestos para funciones básicas (Android).
Relacionarlo con descubribilidad: si un gesto no se ve, el jugador no lo encuentra; por eso los gestos propios se acompañan de una alternativa visible.

## 9 | Sin botón físico
tipo: contenido
kicker: INTERACCIÓN · TÁCTIL
- Joystick virtual: tapa la pantalla
- Toque directo: el dedo cubre
- Un dedo: Alto's Adventure
- Háptica: opcional
video: Zach Gage — "Controls You Can Feel" (GDC 2012, gratuito). Fragmento a definir
fuente: Apple HIG — Playing haptics; Android — Haptics design principles; App Store — Alto's Adventure
notas:
Glosario (conceptos cortos para la docente):
• Joystick virtual: control dibujado en pantalla que imita una palanca.
• Háptica: vibraciones del teléfono usadas como respuesta al jugador.
Detalle: el joystick virtual es familiar, pero no tiene tope físico y tapa la pantalla; el toque directo o el arrastre son precisos, pero el dedo cubre lo que se toca; Alto's Adventure se juega con un solo toque.
Háptica: complementaria, consistente y desactivable. Recomendación de Android: entre una vibración molesta y ninguna, elegir ninguna. Que sea opcional también es accesibilidad.

## 10 | Accesibilidad móvil
tipo: contenido
kicker: ACCESIBILIDAD
- Controles grandes y separados
- Alternativa a cada gesto
- Háptica y efectos desactivables
- Sin toques repetidos rápidos
- Texto legible
fuente: Game Accessibility Guidelines (nivel básico); Apple HIG — Accessibility, Designing for games
notas:
Glosario (conceptos cortos para la docente):
• Accesibilidad: que el juego pueda jugarlo la mayor cantidad posible de personas, incluidas personas con discapacidad.
• Discapacidad situacional: limitación temporal del contexto (por ejemplo, jugar con una mano en el colectivo).
• Button mashing: tocar un botón muchas veces seguidas y rápido.
Detalle: controles grandes y bien separados; una alternativa a cada gesto; háptica y efectos de pantalla desactivables; evitar la repetición rápida de toques; texto de 17 pt por defecto y 11 pt como mínimo en iOS.
Accesible no es un extra: amplía quiénes pueden jugar y mejora la experiencia de todos. Estos puntos van al checklist del TP 3.

## 11 | La primera sesión
tipo: contenido
kicker: ONBOARDING
- Jugar apenas se instala
- Descarga inicial corta
- Enseñar jugando
- Permisos cuando hacen falta
fuente: Apple HIG — Designing for games; Apple GameKit — juegos con descargas grandes
notas:
Glosario (conceptos cortos para la docente):
• Onboarding: la primera experiencia del jugador, en la que aprende a jugar.
• Permiso: autorización que el sistema pide al usuario (cámara, notificaciones).
Detalle: que se pueda jugar apenas termina la instalación; descarga inicial corta (Apple sugiere 30 minutos o menos); enseñar jugando, no con pantallas de texto; pedir permisos en el momento en que se necesitan.
Tema importante pero no imprescindible: no profundizar en Play Asset Delivery; solo la idea de que el tamaño de descarga define qué entra en la primera sesión.

## 12 | Demo: escalar la UI
tipo: demo
kicker: DEMO EN VIVO
- Canvas: Constant Pixel Size
- Cambiar a Scale With Screen Size
- Comparar en el Device Simulator
- Leer Screen.safeArea
video: Unity — "Input System Mobile controls" (opcional, de tarea)
fuente: Unity uGUI 2.0 — Canvas Scaler; Unity 6.3 — Screen.safeArea
notas:
Glosario (conceptos cortos para la docente):
• Resolución de referencia: tamaño de pantalla para el que se diseña la UI; el Canvas Scaler escala a partir de ese tamaño.
Pasos: el Canvas del prefab Game está en Constant Pixel Size con referencia 800 × 600. Cambiarlo a Scale With Screen Size, elegir una resolución de referencia y comparar en el Device Simulator con dos teléfonos y una tablet. Después, leer Screen.safeArea y ver dónde cae el score.
Hacerlo en una copia o rama del proyecto. Mostrar el antes y el después. Remarcar el orden: primero apareció el problema (slide 2), ahora la herramienta.

## 13 | Actividad A4.3 — Dos esquemas
tipo: actividad
kicker: ACTIVIDAD · 25 MIN · GRUPOS
- Dos esquemas de control
- Boceto con safe area
- Medidas en pt/dp
- Comparar con 5 criterios
safearea: Plantilla: dibujen acá su HUD
actividad: Elijan uno y justifíquenlo con dos fuentes.
notas:
Glosario (conceptos cortos para la docente):
• Esquema de control: forma en que el jugador da órdenes (por ejemplo, joystick virtual + botón, o arrastrar + disparo automático).
• Autodisparo: la nave dispara sola, sin que el jugador toque un botón.
Consigna completa: diseñar dos esquemas (por ejemplo, joystick virtual + botón vs. arrastrar + autodisparo); boceto sobre una pantalla de teléfono con la safe area marcada (la plantilla de la slide); medidas en pt/dp y orientación elegida; comparación con cinco criterios: oclusión, precisión, una mano, accesibilidad y descubribilidad.
Buena respuesta: decide la orientación sabiendo su efecto sobre el spawn, respeta 44 pt / 48 dp, no pone controles bajo la muesca, reconoce que el autodisparo cambia el game design (baja la habilidad requerida y cambia el balance) y ofrece una alternativa accesible.

## 14 | Probalo con tu mano · A4.6
tipo: actividad
kicker: PLAYTEST DE PAPEL · 15 MIN + A4.6 · 15 MIN
- HUD a escala sobre tu teléfono
- ¿Llegás a todo?
- A4.6: 60 fps → 35 fps a los 8 min
pregunta: ¿Cuello de botella, métrica, herramienta? ¿Qué NO sirve?
notas:
Glosario (conceptos cortos para la docente):
• Playtest de papel: prueba con personas usando un prototipo dibujado, antes de programar.
• Cuello de botella: la parte del sistema que limita el rendimiento.
• Métrica: valor que se mide (por ejemplo, el tiempo de frame).
Consigna del playtest: dibujar el HUD a escala sobre la silueta del propio teléfono, sostenerlo y comprobar si se llega a todo y qué tapa el pulgar. Es barato y se hace con personas reales: la comodidad no se prueba en el editor.
A4.6, situación completa: "60 fps al empezar, 35–40 fps a los 8 minutos en un teléfono de gama media; en el editor, 200 fps".
Respuesta esperada: throttling térmico agravado por el overdraw de las partículas; medir el tiempo de frame a lo largo del tiempo y el estado térmico con el Profiler en el dispositivo; fijar 30 fps o un presupuesto del 65 % y reducir el overdraw. El editor y el Device Simulator no sirven para esto.
Cierre: un buen layout no garantiza comodidad; eso lo dicen las personas. Verificar quién ya tiene la depuración USB funcionando.

# DECK 3 | El negocio y la prueba | Unidad IV · Clase 3 · v2

## 1 | El negocio y la prueba
tipo: portada
kicker: UNIDAD IV · CLASE 3 DE 4
- Monetización como diseño · Testing en móvil
- Diseño según Plataformas de Juego · FI – UNJu · 2026
notas:
Hoy cambiamos de restricción: ya no es el hardware ni la mano, son las reglas de la tienda y cómo probamos lo que diseñamos.

## 2 | USD 520 millones por una pantalla de compra
tipo: contenido
kicker: APERTURA
- FTC vs. Epic Games (2022)
- USD 275 M + USD 245 M
- Botones confusos al comprar
pregunta: ¿Monetizar es negocio o diseño?
fuente: FTC, comunicado de prensa del 19/12/2022
notas:
Glosario (conceptos cortos para la docente):
• FTC (Federal Trade Commission): organismo de EE. UU. que protege a los consumidores.
• COPPA: ley de EE. UU. que protege la privacidad de los menores de 13 años en línea.
• Dark patterns: diseños de interfaz que empujan al usuario a hacer algo que no quería.
Caso completo: en 2022 la FTC acusó a Epic Games por Fortnite. Epic pagó USD 275 millones por privacidad de menores (COPPA) y USD 245 millones en reembolsos. El motivo: dark patterns en la compra, con una configuración de botones "counterintuitive, inconsistent, and confusing".
Respuesta buscada: las dos cosas. Una decisión de interfaz (dónde va un botón, qué confirma una compra) tuvo consecuencias legales. Desde hoy la monetización se analiza como diseño, con reglas y con ética.
Imagen sugerida (opcional, sin recuadro en la slide): titular del comunicado oficial de la FTC del 19/12/2022.

## 3 | Cuatro modelos
tipo: contenido
kicker: MONETIZACIÓN
| Modelo | Quién paga | Qué cambia en el diseño |
| Premium | Al comprar | Sin interrupciones |
| Freemium + IAP | Algunos jugadores | Tienda y progresión |
| Anuncios | El anunciante | Cuándo interrumpir |
| Híbrido | Combinación | Todo lo anterior |
fuente: App Store — Alto’s Adventure (ficha consultada 2026-10-04)
notas:
Glosario (conceptos cortos para la docente):
• Premium: el juego se paga una vez, al comprarlo.
• Freemium: el juego es gratis y se cobra por contenido o ventajas dentro de él.
• IAP (in-app purchase): compra dentro de la aplicación.
• Híbrido: combinación de modelos (por ejemplo, anuncios + compra para quitarlos).
Detalle por modelo:
- Premium: el jugador paga una vez, al comprar; no hay interrupciones, pero el alcance es menor. Ejemplo: Alto's Adventure, pago único, sin anuncios ni IAP.
- Freemium + IAP: pagan algunos jugadores, dentro del juego; la progresión y la tienda interna se piensan para vender.
- Con anuncios: paga el anunciante y el jugador "paga" con tiempo; hay que decidir en qué momento interrumpir.
- Híbrido: combina los anteriores.
Agregar el modelo premium es una corrección al programa, que solo nombra freemium e híbridos. Ninguno es "el bueno": cada uno cambia el juego de distinta manera.

## 4 | Tres formatos de anuncio
tipo: contenido
kicker: MONETIZACIÓN · ADS
| Formato | Cómo funciona | Regla clave |
| Rewarded | El jugador elige verlo | Con recompensa, opt-in |
| Interstitial | Pantalla completa | Solo en transiciones |
| Banner | Franja fija | Ocupa UI y safe area |
fuente: Google AdMob — Rewarded ads; Interstitial ad guidance
notas:
Glosario (conceptos cortos para la docente):
• Rewarded: anuncio que el jugador elige ver a cambio de una recompensa.
• Interstitial: anuncio de pantalla completa entre momentos del juego.
• Banner: franja publicitaria fija en la pantalla.
• Opt-in: el usuario elige activamente participar.
Cita de AdMob sobre rewarded: "served after a user explicitly chooses to view". El interstitial va solo en transiciones naturales del juego.
Remarcar la diferencia de consentimiento: el rewarded lo pide el jugador, el interstitial se lo imponen. Eso cambia la experiencia y, como vemos en la slide siguiente, también las reglas.
Imagen sugerida (opcional, sin recuadro en la slide): tres mockups de pantalla de Asteroides, uno por formato.

## 5 | Lo que AdMob prohíbe
tipo: contenido
kicker: MONETIZACIÓN · REGLAS EXTERNAS
- Al abrir o salir de la app
- Después de cada acción
- Uno detrás de otro
- Inesperados durante el juego
pregunta: ¿Un anuncio en cada Game Over cumple?
fuente: Google AdMob — Disallowed interstitial implementations
notas:
Glosario (conceptos cortos para la docente):
• AdMob: plataforma de anuncios de Google para apps.
• Política: regla obligatoria que impone la plataforma o la tienda.
Las cuatro prohibiciones completas para interstitials: al abrir o al salir de la app; después de cada acción del usuario (como máximo, uno cada dos acciones); inmediatamente después de otro interstitial; de forma inesperada mientras el usuario está jugando.
Discutir la pregunta: si cada partida es corta y cada Game Over muestra un anuncio, se acerca a "después de cada acción". No hay respuesta automática: hay que leer la política y justificar.
Dato de herramienta: Unity recomienda migrar de Unity Ads directo a LevelPlay (mediación) desde abril de 2026; no se integra en esta materia.

## 6 | La tienda pone las reglas
tipo: contenido
kicker: MONETIZACIÓN · REGLAS EXTERNAS
- Apple 3.1.1: IAP obligatorio
- Probabilidades visibles al comprar
- Google Play Billing obligatorio
- Niños: sin publicidad personalizada
fuente: Apple App Review Guidelines 3.1.1 y 1.3; Google Play — Payments policy y Families policy
notas:
Glosario (conceptos cortos para la docente):
• Loot box: caja con premios al azar que se compra sin saber qué contiene.
• Google Play Billing: sistema de pagos obligatorio de Google Play.
• SDK: biblioteca de un tercero que se integra al juego (por ejemplo, para mostrar anuncios).
Detalle:
- Apple 3.1.1: para desbloquear contenido digital se debe usar la compra integrada (IAP).
- Apple y Google: las cajas con premios al azar deben mostrar las probabilidades antes de comprar.
- Google Play Billing es obligatorio, con excepciones por país.
- Apps para niños: sin publicidad personalizada ni SDKs no certificados.
IAP no es una estrategia libre: la tienda la impone y la regula. Por eso el diseño de la tienda interna empieza leyendo estas políticas.

## 7 | Monetizar cambia el juego
tipo: contenido
kicker: MONETIZACIÓN = GAME DESIGN
- "Continuar" cambia el Game Over
- Dificultad para vender: cambia el balance
- Anuncios: cambian el ritmo
- Vampire Survivors: nunca interrumpir
pregunta: Con "continuar", ¿qué rebalancearían?
fuente: Kotaku (2023), citando a poncle
notas:
Glosario (conceptos cortos para la docente):
• Balance: equilibrio entre la dificultad y las herramientas del jugador.
• Ritmo: alternancia entre momentos intensos y de descanso en la partida.
Detalle: "continuar con un anuncio" cambia el significado del Game Over; subir la dificultad para vender vidas cambia el balance; las pausas para anuncios cambian el ritmo de la sesión.
Caso: en Vampire Survivors para móvil, la monetización está "designed to never interrupt your game, always be optional" (Kotaku, 2023, citando a poncle).
Respuesta posible a la pregunta: la cantidad de vidas, la velocidad de los asteroides y la duración de la partida; además, cómo se calcula el puntaje si alguien continúa. Es el puente entre economía y game design.

## 8 | El lado oscuro
tipo: contenido
kicker: ÉTICA
- Dark patterns (Zagal et al., 2013)
- Loot boxes: correlación, no causa
- 35 técnicas predatorias (2022)
- Bélgica las prohibió (2018)
video: "Dark Patterns: How Good UX Can Be Bad UX", Anisa Sanusi, GDC 2017 (gratuito). Fragmento a definir
fuente: PLOS ONE 2018; Journal of Business Ethics 2022; UK Gambling Commission
notas:
Glosario (conceptos cortos para la docente):
• Correlación: dos cosas aparecen juntas, pero eso no prueba que una cause la otra.
• Monetización predatoria: técnicas que aprovechan vulnerabilidades del jugador para que gaste.
Detalle:
- Dark patterns: diseños que juegan en contra del interés del jugador (Zagal, Björk y Lewis, 2013).
- Loot boxes: asociadas con el juego problemático (Zendle y Cairns, 2018, PLOS ONE, n = 7.422). Es una correlación, no una causa demostrada.
- 35 técnicas de monetización percibidas como predatorias (Petrovskaya y Zendle, 2022, Journal of Business Ethics).
- Regulación: Bélgica prohibió mecánicas de loot box en 2018 (según la UK Gambling Commission).
Cuidar la precisión: no decir que las loot boxes "causan" adicción. Zagal et al. se cita sin enlace hasta verificar una copia legal (pendiente en el status).

## 9 | Actividad A4.5: ¿cuál publicarían?
tipo: actividad
kicker: ACTIVIDAD · 25 MIN · GRUPOS + DEBATE
| Propuesta | Modelo |
| P1 | Premium, US$ 2,99, sin anuncios ni compras |
| P2 | Gratis + rewarded "continuar" + IAP "quitar anuncios" |
| P3 | Interstitial al abrir y en cada Game Over + cofres al azar sin probabilidades |
actividad: ¿Cumple políticas? ¿Qué cambia? ¿Riesgos éticos? Elijan una.
notas:
Glosario (conceptos cortos para la docente):
• Cofre al azar: equivalente a una loot box.
Propuestas completas: P1 premium a US$ 2,99, sin anuncios ni compras. P2 gratis, rewarded "continuar con 1 vida" (una vez por partida) + IAP "quitar anuncios". P3 gratis, interstitial al abrir y en cada Game Over + cofres pagos al azar sin probabilidades + dificultad aumentada para empujar a comprar.
Respuesta esperada: P3 viola políticas (interstitial al abrir; probabilidades no informadas) y manipula la dificultad. P2 cumple, pero cambia el balance. P1 es viable, con menor alcance. Vale cualquier elección defendida con criterios y fuentes.

## 10 | ¿Qué prueba cada herramienta?
tipo: contenido
kicker: TESTING EN MÓVIL
| Nivel | Prueba | No prueba |
| 1. Device Simulator | Layout, safe area | Rendimiento, memoria |
| 2. Emulador | Lógica y flujos | Rendimiento real, térmica |
| 3. Teléfono + Profiler | Rendimiento real | Otros modelos |
| 4. Tests en el Player | Tests en el dispositivo | Lo no escrito como test |
| 5. Granjas en la nube | Muchos modelos | Ergonomía |
| 6. Android vitals | Fallas reales publicadas | Nada antes de publicar |
fuente: Unity 6.3 — Device Simulator, Run tests in a Player, Profiling on target; Firebase Game Loop; AWS Device Farm; Android vitals
notas:
Glosario (conceptos cortos para la docente):
• Profiler: herramienta de Unity que mide en qué se gasta el tiempo de cada frame.
• Granja de dispositivos: servicio con muchos teléfonos reales para correr pruebas a distancia (Firebase Test Lab, AWS Device Farm).
• Android vitals: métricas de calidad que Google Play mide sobre las apps publicadas.
• ANR (Application Not Responding): la app deja de responder.
Es la escalera que conecta con la Unidad 3: cada nivel tiene un "qué no prueba". El Device Simulator no prueba rendimiento, memoria ni render; el emulador no prueba térmica ni la GPU del teléfono.
Android vitals mide fallas como la tasa de cierres inesperados (umbral general 1,09 %) y de ANR (0,47 %); la memoria pasa a afectar la visibilidad en la tienda desde febrero de 2027.

## 11 | La plataforma se mueve
tipo: contenido
kicker: DISTRIBUCIÓN
- Google Play: AAB y API 36
- Unity 6.3: Android 7.1+
- iOS requiere macOS
- En la cátedra: iOS conceptual
fuente: Android — target API level requirement; Unity 6.3 — Android/iOS requirements y build process
notas:
Glosario (conceptos cortos para la docente):
• AAB (Android App Bundle): formato de publicación que exige Google Play.
• Target API: versión de Android para la que se declara compilado el juego.
• Xcode: entorno de Apple para compilar apps de iOS; solo corre en macOS.
Detalle: Google Play exige AAB y, desde el 31/08/2026, apuntar a Android 16 (API 36). Unity 6.3 soporta Android 7.1 (API 25) o superior. Para iOS, Unity genera un proyecto de Xcode, y Xcode solo corre en macOS. En la cátedra no hay Mac: iOS se estudia de forma conceptual.
Las reglas de tienda cambian todos los años: un juego publicado en 2025 puede necesitar cambios en 2026 sin que nadie toque el diseño. Decir explícitamente el límite del curso con iOS; no esconderlo.

## 12 | Demo: el test de pausa en rojo
tipo: demo
kicker: DEMO EN VIVO
- Pausa defectuosa: reanuda sola
- Test de Edit Mode: rojo
- Test de Play Mode: rojo
fuente: Unity 6.3 — Unity Test Framework (Edit/Play mode)
notas:
Glosario (conceptos cortos para la docente):
• Edit Mode: tests que corren sin ejecutar el juego.
• Play Mode: tests que corren con el juego en marcha.
• Test en rojo: test que falla; es lo esperado cuando el código tiene el defecto.
Requiere tener en el repositorio la versión de Asteroides con el sistema de pausa defectuoso (tarea del status): al volver, el juego reanuda solo.
Mostrar el rojo y no corregir: lo corrigen los grupos. Recordar el ciclo de la Unidad 3: rojo, corrección, verde, regresión.
La pestaña Player del Test Runner (correr los tests en el teléfono) se usa más adelante en la unidad, en la práctica con el dispositivo.

## 13 | Actividad A4.4: la llamada que mata la nave
tipo: actividad
kicker: ACTIVIDAD · 25 MIN · GRUPOS
- Comportamiento esperado
- Regla separada del adaptador
- Test de Edit Mode
- ¿Qué NO demuestra?
flujo: Sistema operativo | Adaptador (MonoBehaviour) | Regla de pausa (C# puro) | Estado del juego
actividad: El resto del ciclo se completa en el TP 3.
notas:
Glosario (conceptos cortos para la docente):
• Adaptador: clase que traduce los avisos del motor (OnApplicationPause) en órdenes para la lógica del juego.
• Regla: lógica pura en C#, sin dependencias de Unity, que decide si el juego está en pausa; se puede probar sin abrir el juego.
• Regresión: un defecto ya corregido que vuelve a aparecer.
Consigna completa: escribir el comportamiento esperado ante una interrupción como criterio verificable; separar la regla (C# puro) del adaptador (MonoBehaviour que recibe OnApplicationPause); escribir el test de Edit Mode de la regla; completar qué NO demuestra el test. El test de Play Mode y la corrección se terminan en el TP 3, y el QA manual se hace más adelante en la unidad, con los teléfonos.
El diagrama muestra el camino del aviso: el sistema operativo avisa al adaptador, el adaptador llama a la regla y la regla cambia el estado del juego.
Respuesta esperada de "qué no demuestra": que el sistema operativo llame al callback cuando corresponde; qué pasa si el sistema mata el proceso (no se llama nada); el caso del teclado en pantalla en Android.

# DECK 4 | Asteroides en tu bolsillo | Unidad IV · Clase 4 · v2

## 1 | Asteroides en tu bolsillo
tipo: portada
kicker: UNIDAD IV · CLASE 4 DE 4 · PRÁCTICA EN DISPOSITIVO
- Build, medición y QA manual en sus teléfonos
- Diseño según Plataformas de Juego · FI – UNJu · 2026
notas:
Clase 100 % práctica. Antes de empezar, verificar cables, depuración USB y Android Build Support instalado.

## 2 | ¿Qué no sabemos todavía?
tipo: contenido
kicker: APERTURA
- Todo fue en el editor
- "Qué no demuestra" sigue abierto
- Hoy: el teléfono real
pregunta: ¿Qué esperan que cambie?
notas:
Glosario (conceptos cortos para la docente):
• Editor: el entorno de Unity en la PC, donde se arma y prueba el juego.
Situación: todo lo que probamos hasta ahora fue en el editor; la columna "qué no demuestra" de A4.4 sigue abierta. Hoy vemos cómo se comporta el juego en un teléfono real.
Que anoten su predicción: sirve para contrastarla al final de la clase.
Imagen sugerida (opcional, sin recuadro en la slide): editor de Unity y teléfono, con un signo de pregunta entre ambos.

## 3 | De la PC al teléfono
tipo: demo
kicker: DEMO EN VIVO + GRUPOS · 20 MIN
- Primero la docente
- Después cada grupo
flujo: Development Build + Autoconnect Profiler | Cable USB y depuración activada | Build and Run | El juego abre en el teléfono
fuente: Unity 6.3 — Build your application for Android; Collect performance data on a target platform
notas:
Glosario (conceptos cortos para la docente):
• Build: versión compilada del juego, lista para instalar.
• Development Build: build con información de depuración que permite conectar el Profiler.
• Autoconnect Profiler: opción para que el Profiler se conecte solo al iniciar el juego.
• Build and Run: compilar e instalar en el dispositivo conectado en un solo paso.
Pasos: en Build Profiles, elegir Android y marcar Development Build y Autoconnect Profiler; conectar el teléfono por USB con la depuración activada; Build and Run; el juego se instala y se abre en el teléfono. Primero lo hace la docente; después cada grupo, con el teléfono de un integrante.
La primera build tarda: prever ese tiempo. Si un teléfono no aparece, revisar el cable (de datos, no solo de carga) y aceptar el diálogo de depuración en el teléfono.

## 4 | Plan B
tipo: contenido
kicker: GESTIÓN DE RIESGO
- Falla la build: APK de la docente
- Se pierde: el Profiler
- No se pierde: QA y matriz
- Lo no medido se declara
notas:
Glosario (conceptos cortos para la docente):
• APK: archivo instalable de una app de Android.
Detalle: si la build falla en la máquina del grupo, se instala el APK de la docente. Se pierde el Profiler conectado; no se pierden el QA manual de interrupciones ni la matriz de compatibilidad. Lo que no se pudo medir se declara en el dossier.
Normalizar el plan B: en la industria también fallan las builds. Lo importante es documentar qué quedó sin medir.

## 5 | Medir, no opinar
tipo: actividad
kicker: MEDICIÓN · 20 MIN
- H1: ¿picos de GC al disparar?
- H2: ¿fps estable 10 minutos?
- Anotar modelo y versión
actividad: Capturen el Profiler y anoten los valores.
fuente: Unity 6.3 — Profiling on a target device; e-book Unity 6, p. 11
notas:
Glosario (conceptos cortos para la docente):
• GC (garbage collector): proceso que libera memoria que ya no se usa; si trabaja mucho, produce tirones.
• GC Alloc: memoria reservada en cada frame que después tendrá que liberar el GC.
• Hipótesis: suposición que se comprueba midiendo.
Hipótesis completas: H1, ¿cada disparo (Instantiate del láser) genera picos de GC? Métrica: GC Alloc por frame. H2, ¿el juego sostiene el fps durante 10 minutos? Métrica: tiempo de frame a lo largo del tiempo. Registrar modelo de teléfono, versión de Android y temperatura percibida.
Advertencia honesta: Asteroides es liviano y lo más probable es que ande bien en casi cualquier teléfono. Si la medición no muestra problemas, la respuesta correcta es decirlo con los datos. El objetivo es aprender a formular y medir hipótesis.
Imagen sugerida (opcional, sin recuadro en la slide): Profiler conectado a un teléfono con un pico de GC marcado.

## 6 | Editor vs. teléfono
tipo: actividad
kicker: COMPARAR
| Medición | Editor (PC) | Teléfono |
| fps promedio | | |
| Tiempo de frame máximo | | |
| GC Alloc por disparo | | |
| fps a los 10 minutos | | |
actividad: Completen con sus mediciones.
notas:
Glosario (conceptos cortos para la docente):
• fps promedio: cantidad media de imágenes por segundo durante la medición.
• Tiempo de frame máximo: el cuadro que más tardó; muestra los tirones que el promedio esconde.
Conclusión esperada: el número del editor no predice el del teléfono. Retomar el caso A4.6 de la Clase 2 (200 fps en el editor).

## 7 | Interrumpir a propósito
tipo: actividad
kicker: QA MANUAL · 20 MIN
| Caso | Acción | Esperado | Real |
| QA-01 | Llamada o alarma | Pausa y espera un toque | |
| QA-02 | Inicio y volver | Pausado, sin daño | |
| QA-03 | Bloquear la pantalla | Pausado | |
| QA-04 | Teclado en pantalla | Documentar | |
| QA-05 | Cierre forzado | Qué se pierde | |
fuente: Unity 6.3 — OnApplicationPause / OnApplicationFocus; Android — activity lifecycle
notas:
Glosario (conceptos cortos para la docente):
• QA manual: prueba hecha por una persona, siguiendo pasos definidos.
• Cierre forzado: terminar la app desde los ajustes del sistema.
Casos completos: QA-01 llamada o alarma durante la partida (esperado: el juego se pausa y espera un toque); QA-02 botón de inicio y volver (pausado, sin daño a la nave); QA-03 bloquear y desbloquear la pantalla (pausado); QA-04 abrir el teclado en pantalla, si aplica (documentar qué pasa); QA-05 cierre forzado y reabrir (documentar qué se pierde).
Mismo formato de caso de prueba de la Unidad 2 (esperado vs. real). Si los grupos todavía no corrigieron el defecto, probar la versión con defecto: el resultado real va a contradecir al esperado, y eso es un hallazgo.

## 8 | Lo que el test automático no vio
tipo: contenido
kicker: LÍMITES
- ¿Coinciden tests y QA manual?
- ¿Qué apareció solo en el teléfono?
- ¿Qué no se puede automatizar?
pregunta: ¿Qué protege el test y qué solo el QA manual?
notas:
Glosario (conceptos cortos para la docente):
• Test automático: prueba que corre sola y compara el resultado con lo esperado.
Respuesta esperada: los tests protegen la regla y el adaptador ante regresiones; el QA manual comprueba que el sistema operativo dispare los callbacks y qué pasa cuando se cierra el proceso. Es la frontera entre automatización y hardware real, la misma de la Unidad 3 aplicada a la plataforma.

## 9 | La matriz del curso
tipo: actividad
kicker: COMPATIBILIDAD · 15 MIN
| Grupo | Modelo | Android | RAM | Resolución | fps | ¿Spawn visible en vertical? |
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
pregunta: ¿Alcanza para decir "anda en Android"?
fuente: Unity e-book (probar en gama mínima y máxima, p. 20); Android vitals
notas:
Glosario (conceptos cortos para la docente):
• Matriz de compatibilidad: tabla que cruza dispositivos con resultados de prueba.
• Muestra de conveniencia: los casos que se tienen a mano, no elegidos para representar al mercado.
Respuesta esperada: no. Es una muestra de conveniencia; faltan gamas, fabricantes, versiones de Android y tablets. Por eso existen las granjas de dispositivos y Android vitals. Igual es evidencia real y vale más que el editor.

## 10 | Defensa del TP 3
tipo: actividad
kicker: DEFENSA · 3 MIN POR GRUPO · COEVALUACIÓN
- Una decisión de plataforma
- La evidencia del teléfono
- Lo que quedó sin probar
| Criterio de coevaluación | Sí / En parte / No |
| La decisión está justificada | |
| Hay evidencia del dispositivo | |
| Se declaran los límites | |
notas:
Glosario (conceptos cortos para la docente):
• Coevaluación: los grupos se evalúan entre sí con criterios compartidos.
• Decisión de plataforma (PDR): registro de contexto, opciones, decisión y consecuencias.
Formato de la defensa: una decisión de plataforma (contexto, opciones, decisión, consecuencias); la evidencia del teléfono que la respalda o la contradice; lo que quedó sin probar, dicho explícitamente.
Los criterios de coevaluación son una versión reducida de la rúbrica del TP 3 (ver 05). La entrega final del dossier se sube al aula virtual.

## 11 | En móvil, el límite lo pone el dispositivo
tipo: cierre
kicker: CIERRE DE UNIDAD · PUENTE A UNIDAD V
- Energía, calor, pantalla, interrupciones
- El teléfono muestra lo que el editor no
- Consolas: el límite lo pone el fabricante
pregunta: En consola, ¿quién decide si se publica?
notas:
Glosario (conceptos cortos para la docente):
• Certificación: revisión que hace el fabricante de la consola antes de permitir que un juego se publique.
Síntesis: en móvil el límite lo ponen la energía, el calor, la memoria, la pantalla táctil, las interrupciones y las reglas de tienda. Lo que el editor no muestra, lo muestra el teléfono.
Pregunta puente: en consola, el fabricante certifica el juego antes de publicarlo (Microsoft publica sus requisitos; Sony y Nintendo, no). La idea transversal de las Unidades IV a VII: ¿quién pone el límite?
Imagen sugerida (opcional, sin recuadro en la slide): un teléfono que se transforma en un gamepad frente a una TV.
