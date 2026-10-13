# Unidad 4 — Diapositivas, versión final (texto + notas del docente)

Fuente única de los 3 decks de la Unidad 4. Generar: `python scripts/build_decks.py` desde `diseno-plataformas/unidad-04/` (requiere `pip install python-pptx` y Pillow). Opciones: `--decks 2 3` genera solo esos decks; `--out-dir RUTA` escribe en otra carpeta (útil si el .pptx está abierto).

**Versión final (2026-10-13).** Pedido del usuario: la unidad termina en **dos encuentros de 90 minutos** después de la Clase 1, que se dio hasta la slide 15. Se reorganizó todo el contenido restante con reparto **40 % teoría / 60 % práctica** (36 / 54 min por encuentro), sin perder temas:
- **Clase 1** (dada): slides 1–15, tal como se dieron.
- **Clase 2 — Del supuesto de PC al pulgar** (90 min): simulador y límites, A4.2 (supuestos de PC), elegir plataforma, UI táctil (mínimos, densidad, safe area, pulgar, orientación, gestos, accesibilidad), Input System, **A4.7** (une A4.3 y A4.7: boceto + implementación), playtest y vistazo de la build. Tarea: Build Support, depuración USB y primer APK.
- **Clase 3 — Asteroides en tu bolsillo** (90 min): build con capturas reales, instalación, medición, A4.6, QA manual, matriz, testing en móvil, **A4.8** (test de configuración), monetización como diseño, A4.5, TP 3 y cierre de unidad.
- Pasan fuera del encuentro: "Leer con lupa" (lectura), A4.4 (pausa, en el dossier del TP 3) y la defensa del TP 3 (video, **PROPUESTO**).

Las versiones anteriores (v1 a v4, `.pptx` y fuentes) están en `versiones-anteriores/`.

**Formato que lee el generador (no cambiar la sintaxis):**
- `# DECK n | Título | Subtítulo` empieza un deck. `## n | Título` empieza una slide.
- Claves de una línea: `tipo:` (portada / contenido / actividad / demo / cierre), `kicker:`, `pregunta:`, `actividad:`, `video:`, `fuente:`, `imagen:` (recuadro de imagen sugerida; no se usa).
- Gráficos: `diagrama:`, `cronologia:`, `hitos:`, `flujo:`, `comparacion:`, `tiles:`, `codigo:` (lee el código real; `codigo: git:REV:ruta:a-b` lo lee de un commit), `vista:`, `safearea:`, `captura: imagenes/a.png + imagenes/b.png | pie` (capturas reales), `ajustes: Título | Campo: valor | Campo: *valor` (panel tipo Inspector; `*` resalta) y `panel: ancho` (el gráfico ocupa todo el ancho).
- Líneas `- ` = viñetas. Líneas `|` = tabla (la primera fila es el encabezado). `notas:` abre las notas del docente hasta la próxima slide.

---

# DECK 1 | Un teléfono no es una PC chica | Unidad IV · Clase 1 · final (dada hasta la slide 15)

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
fuente: Clase 28/09/2026 — Clase2-Plataformas.pptx; código del proyecto (Ship.cs 61–73, versión original, commit e766f8c)
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

# DECK 2 | Del supuesto de PC al pulgar | Unidad IV · Clase 2 · final

## 1 | Del supuesto de PC al pulgar
tipo: portada
kicker: UNIDAD IV · CLASE 2 DE 3 · 90 MIN
- Supuestos de PC, UI táctil y controles en Unity
- Diseño según Plataformas de Juego · FI – UNJu · 2026
notas:
Versión final de la unidad: quedan dos encuentros de 90 minutos. Este retoma la Clase 1 desde la slide 16 y suma la UI táctil y la implementación de los controles. El encuentro siguiente es la práctica en el teléfono, la prueba y el negocio.
Reparto: teoría 36 min (apertura 3, simulador 4, plataforma 3, UI táctil 14, demos de Input System 7, vistazo de la build 3, cierre 2) = 40 %; práctica 54 min (A4.2 12, puesta en común 5, A4.7 30, playtest 7) = 60 %.
Antes de empezar: proyecto Asteroides abierto en el Device Simulator; copia del proyecto original para los grupos; deck de la Clase 1 a mano por si hay que volver a A4.1.

## 2 | Dónde quedamos
tipo: contenido
kicker: APERTURA · 3 MIN
- A4.1: síntomas en el teléfono
- Hoy: qué supone el código
- Y cómo se juega con el pulgar
pregunta: ¿Por qué la nave no se mueve en el teléfono?
notas:
Glosario (conceptos cortos para la docente):
• Supuesto de plataforma: algo que el código da por cierto porque se pensó para una PC (teclado, pantalla horizontal, mouse).
Recuperar A4.1 en un minuto: los síntomas (calor, tirones, partida perdida al atender una llamada) tenían causas en la máquina. Hoy pasamos del síntoma a la causa en el código y a las manos del jugador.
Dejar la pregunta abierta: la respuesta aparece en A4.2 (Ship.cs lee teclas fijas). No dar la herramienta antes del problema.

## 3 | Demo: el simulador y sus límites
tipo: demo
kicker: DEMO EN VIVO · 4 MIN
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

## 4 | Actividad A4.2 — Supuestos de PC
tipo: actividad
kicker: ACTIVIDAD · 12 MIN · GRUPOS
- Ship.cs 61–73: el control
- Ship.cs 46–47 y 99–115: los límites
- Spawner.cs 101–106: el spawn
- Prefab Game: Canvas y cámara
actividad: 5 supuestos: dónde (archivo:línea), qué pasaría, qué eje.
codigo: git:e766f8c:../../proyectos-unity/Asteroides/asteroide-final/Assets/Scripts/Ship.cs:61-73
notas:
Glosario (conceptos cortos para la docente):
• Spawn: aparición de un objeto en el juego; acá, los asteroides.
• Prefab: objeto de Unity guardado como plantilla reutilizable.
• Canvas: contenedor de la interfaz (UI) en Unity.
• Input.GetKey: lectura directa de una tecla en el sistema de input clásico de Unity.
Consigna completa: listar al menos 5 supuestos que dejan de valer en un teléfono, indicando dónde están (archivo:línea), qué pasaría en móvil y a qué eje pertenecen (input, pantalla, UI, ciclo de vida, rendimiento).
La respuesta completa es la tabla S1–S13 de 02-caso-practico. Para aprobar alcanza con S1 (teclado), S3/S4/S5 (límites, cámara, spawn), S6 (Canvas en Constant Pixel Size) y S8 (sin pausa).
Pista si se traban: "¿qué pasa con la cámara si la pantalla es más angosta que alta?".
Importante (versión 3): el código de la slide es la versión **original** de Ship.cs, leída del commit e766f8c. En el repositorio, Ship.cs ya tiene el porteo de entrada (Ship.SetIntent + ShipInputAdapter). Los grupos analizan la versión original: si trabajan con el repositorio clonado, que lo hagan sobre ese commit (git checkout e766f8c -- proyectos-unity/Asteroides/asteroide-final/Assets/Scripts/Ship.cs) o con la copia del TP. No mostrar todavía la solución.

## 5 | Lo que encontramos
tipo: contenido
kicker: PUESTA EN COMÚN · 5 MIN
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
Cerrar la puesta en común volviendo al supuesto S1 (teclado): en el teléfono, Asteroides deja tocar "Start" pero la nave no se mueve ni dispara, porque Ship.cs lee teclas fijas. La salida es el diagrama de la slide 3: separar el dispositivo de la intención. No mostrar la herramienta todavía; alcanza con dejar planteado el problema. Se resuelve en código más adelante en la unidad.

## 6 | ¿Cómo se elige una plataforma?
tipo: contenido
kicker: DECISIÓN · 3 MIN
- Audiencia
- Modelo de monetización
- Herramientas y soporte
- Vigencia en el tiempo
- + Restricciones técnicas (hoy)
pregunta: Con estos criterios: ¿Asteroides es un juego para móvil?
fuente: Kevuru Games (blog, consultado 2026-10-05) + criterio de la cátedra
notas:
Glosario (conceptos cortos para la docente):
• Audiencia: público al que apunta el juego.
• Vigencia (future-proofing): que la plataforma siga activa y evolucionando con el tiempo.
Versión final: la slide «Leer con lupa» pasa a lectura del aula virtual (ver el cierre).
El artículo de Kevuru propone cuatro consideraciones para elegir plataforma, y concluye que el desafío no es encontrar la "mejor" plataforma, sino la que encaja con la visión del juego y su público:
1. Audiencia: saber para quién se construye. Un puzzle casual puede encontrar su público en móvil; un RPG con mucha narrativa puede funcionar mejor en consola o PC.
2. Modelos de monetización: suscripción, free-to-play con compras integradas o venta premium. Cada plataforma se inclina por estrategias distintas y el modelo de ingresos tiene que coincidir.
3. Integración y soporte: algunas plataformas ofrecen mejores herramientas, documentación o ayuda directa; una buena integración ahorra meses.
4. Vigencia (future-proofing): preferir plataformas que sigan evolucionando para que el juego no quede desactualizado en uno o dos años.
Lo que agrega la cátedra: un quinto criterio, las restricciones técnicas y de diseño de la plataforma (todo lo que vimos hoy: calor, batería, memoria, interrupciones, pantalla). El artículo no lo menciona y es justamente el núcleo de esta materia.
Respuesta esperada a la pregunta: Asteroides encaja en móvil por audiencia (partidas cortas y casuales) y por sus requisitos técnicos bajos, pero exige rediseñar el control, la pantalla y la pausa (lo que encontramos en A4.2). La monetización se decide más adelante en la unidad.

## 7 | ¿Cuánto mide un dedo?
tipo: contenido
kicker: UI TÁCTIL · 4 MIN
- Diseñar en pt/dp, no en px
- Canvas Scaler: Scale With Screen Size
| Plataforma | Mínimo táctil | Fuente |
| iOS | 44 × 44 pt (mínimo 28 × 28) | Apple HIG |
| Android | 48 × 48 dp | Android Developers |
fuente: Apple HIG — Buttons, Accessibility; Android — Make apps more accessible; Unity uGUI 2.0 — Canvas Scaler
notas:
Glosario (conceptos cortos para la docente):
• px (píxel): punto físico de la pantalla; su tamaño real depende de la densidad.
• pt / dp: unidades independientes de la densidad (iOS / Android); un botón de 48 dp mide lo mismo en cualquier teléfono.
• Canvas Scaler: componente de Unity que decide cómo se escala la UI según la pantalla.
Problema: en un teléfono con muesca, el score de Asteroides queda bajo la cámara y el botón de inicio, pensado para un mouse, es diminuto. Preguntar "¿cuántos píxeles debería medir un botón?" y mostrar que en píxeles no hay respuesta: el mismo botón de 100 px es grande en un teléfono viejo y diminuto en uno de alta densidad.
Mínimos oficiales: Apple pide 44 × 44 pt por defecto, con un mínimo absoluto de 28 × 28 pt; Android pide al menos 48 × 48 dp ("Larger is even better"). Son números verificables: convierten "botón cómodo" en un criterio de prueba.
Unity: Asteroides usa Constant Pixel Size (supuesto S6). Scale With Screen Size escala desde una resolución de referencia. Se aplica en A4.7.

## 8 | No todo el rectángulo es tuyo
tipo: contenido
kicker: UI TÁCTIL · SAFE AREA · 3 MIN
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

## 9 | Pulgar y orientación
tipo: contenido
kicker: ERGONOMÍA · 3 MIN
- El agarre cambia todo el tiempo
- HUD editable: CoD Mobile, Fortnite
- Vertical: una mano
- Horizontal: dos pulgares, más campo
pregunta: ¿Asteroides es vertical u horizontal?
fuente: Hoober, UXmatters 2013 (profesional); Activision blog CoD Mobile 2019; Android 16 behavior changes
notas:
Glosario (conceptos cortos para la docente):
• Agarre: forma de sostener el teléfono (una mano, acunado, dos manos).
• HUD: información y controles superpuestos al juego.
Datos de Hoober (2013, 1.333 personas observadas): 49 % una mano, 36 % acunado, 15 % dos manos; la gente cambia de agarre todo el tiempo. Advertir: fuente profesional, no académica, con más de una década; sirve como disparador, no como norma.
CoD Mobile y Fortnite permiten mover y redimensionar los controles: una respuesta de diseño a la diversidad de manos y teléfonos.
Orientación: lo vieron en la puesta en común de A4.2: en vertical, la mayoría de los asteroides nace fuera de pantalla. Android 16 ignora las restricciones de orientación en pantallas grandes, salvo en juegos (Unity 6.3 marca Application Category = Game por defecto). No hay respuesta única: se evalúa que la decisión considere sus consecuencias (spawn, límites, HUD).

## 10 | Gestos, controles y accesibilidad
tipo: contenido
kicker: INTERACCIÓN · 4 MIN
- Gesto propio: nunca la única vía
- Joystick virtual: tapa la pantalla
- Controles grandes y separados
- Háptica y efectos desactivables
comparacion: Joystick virtual: Familiar, Sin tope físico // Tapa la pantalla | Toque directo: Preciso, Un dedo // El dedo cubre lo que toca
fuente: Apple HIG — Gestures, Accessibility; Android — Haptics design principles; Game Accessibility Guidelines
notas:
Glosario (conceptos cortos para la docente):
• Gesto estándar: tocar, deslizar, arrastrar, mantener, pellizcar.
• Háptica: vibraciones cortas como respuesta a una acción.
• Onboarding: la primera sesión, cuando el juego enseña a jugar.
Gestos: no redefinir los gestos del sistema; un gesto inventado nunca debe ser la única forma de hacer algo importante (Apple), y las apps no deberían depender de gestos (Android).
Sin botón físico: el joystick virtual es familiar, pero no tiene tope y tapa la pantalla; el toque directo es preciso, pero el dedo cubre lo que toca; Alto's Adventure se juega con un solo toque.
Accesibilidad (al checklist del TP 3): controles grandes y separados; alternativa a cada gesto; háptica y efectos desactivables (Android: entre una vibración molesta y ninguna, elegir ninguna); sin toques repetidos rápidos; texto de 17 pt por defecto y 11 pt como mínimo en iOS.
Primera sesión, en una línea: jugar apenas se instala, descarga inicial corta, enseñar jugando y pedir permisos cuando hacen falta.
Video opcional de tarea: Zach Gage, "Controls You Can Feel" (GDC 2012).

## 11 | Una acción, tres dispositivos
tipo: demo
kicker: DEMO EN VIVO · INPUT SYSTEM · 4 MIN
- En el teléfono, la nave no se mueve
- Teclado, gamepad y dedo: la misma acción
- Los controles en pantalla simulan un gamepad
diagrama: Dispositivo: Teclado, Gamepad, Joystick en pantalla | Intención: Mover, Disparar | Nave: MoveLeft, MoveRight, ShootLaser || La nave no sabe qué dispositivo se usó
fuente: Unity Input System 1.19 — On-screen Controls; código del proyecto (ShipInputAdapter.cs, Ship.cs)
notas:
Glosario (conceptos cortos para la docente):
• Input System: paquete de Unity que reemplaza al Input Manager clásico; trabaja con acciones en lugar de teclas fijas.
• Acción: lo que el jugador quiere hacer (mover, disparar), separado del botón que la produce.
• Binding: asociación entre una acción y un control concreto (flecha izquierda, stick del gamepad).
• OnScreenStick / OnScreenButton: componentes que dibujan un control en la pantalla táctil y lo hacen pasar por un gamepad virtual.
• Active Input Handling: opción del proyecto que elige el sistema de entrada (Old, New o Both).
Primero el problema (regla de la cátedra): en el teléfono, Asteroides deja tocar "Start", pero la nave no se mueve ni dispara, porque Ship.cs leía teclas fijas (supuesto S1). Después la herramienta.
El diagrama es el mismo de las tres capas: el dispositivo cambia; la intención y la nave no. Los controles en pantalla no son un caso especial: según la documentación de Input System 1.19, un OnScreenStick con el control path <Gamepad>/leftStick crea un gamepad virtual, y el juego lo lee igual que un gamepad físico.
Pasos de la demo (versión del repositorio, ya portada):
1. Package Manager: Input System 1.19.0 instalado (viene con Unity 6000.3.11f1).
2. Project Settings > Player > Active Input Handling = Both. Se usa Both, y no solo New, para no romper el menú, que todavía usa el StandaloneInputModule clásico. Unity pide reiniciar el editor. Consecuencia (versión 4): según la documentación de Unity 6.3, Both "no está soportado en Android"; al compilar aparece el cartel "Unsupported Input Handling on Android". Es el precio de una dependencia oculta y se retoma más adelante en la unidad, con el teléfono.
3. Abrir el Device Simulator con un teléfono: aparecen el joystick abajo a la izquierda y el botón de disparo abajo a la derecha (MobileControlsVisibility los muestra solo en plataformas móviles).
4. Mover la nave con el mouse sobre el joystick. Después, en la PC, mostrar que el teclado sigue funcionando y, si hay un gamepad, que también funciona sin cambiar código.
Límite a decir en voz alta: el Device Simulator simula el toque de un dedo; mover y disparar a la vez (dos dedos) solo se prueba en el teléfono.
URL verificada (2026-10-10): https://docs.unity3d.com/Packages/com.unity.inputsystem@1.19/manual/OnScreen.html

## 12 | La intención en código
tipo: demo
kicker: DEMO · CÓDIGO REAL · 3 MIN
- Las teclas pasan a ser bindings
- El gamepad se suma sin tocar la nave
- La nave recibe SetIntent(mover, disparar)
codigo: ../../proyectos-unity/Asteroides/asteroide-final/Assets/Scripts/ShipInputAdapter.cs:18-27
fuente: Código del proyecto (ShipInputAdapter.cs; Ship.cs, método SetIntent)
notas:
Glosario (conceptos cortos para la docente):
• Composite 1DAxis: binding que arma un eje de −1 a 1 con dos teclas (negativa y positiva).
• Adaptador: clase que traduce el dispositivo a la intención; acá, ShipInputAdapter.
• Zona muerta (dead zone): margen alrededor de 0 en el que el stick se considera quieto (0,2 en Ship.cs).
Qué mostrar: las flechas y la barra espaciadora siguen ahí, pero ahora como bindings de una acción; el stick y el D-pad del gamepad y el botón A (buttonSouth) se agregan como bindings de las mismas acciones. Cada frame, el adaptador llama a ship.SetIntent(mover, disparar).
Comparar con la slide de A4.2 (versión original): las tres lecturas de Input.GetKey desaparecieron de Ship.cs. MoveLeft, MoveRight y ShootLaser no cambiaron, y por eso los tests que ya existían siguen sirviendo.
Decisión de diseño a explicitar: el esquema del repositorio (joystick + botón) es uno de los posibles; en A4.7 cada grupo elige el suyo y lo implementa.

## 13 | Actividad A4.7 — Del boceto al control
tipo: actividad
kicker: ACTIVIDAD · 30 MIN · GRUPOS · BOCETO + UNITY
- Boceto: dos esquemas (8 min)
- Elegir uno con 5 criterios
- Implementarlo con Input System
- ¿Mide 48 dp? ¿Tapa la nave?
safearea: Plantilla: boceten acá su HUD
actividad: Entreguen boceto, captura del simulador y lo que no pudieron probar.
notas:
Glosario (conceptos cortos para la docente):
• Esquema de control: forma en que el jugador da órdenes (joystick virtual + botón, o arrastrar + autodisparo).
• Autodisparo: la nave dispara sola, sin un botón.
• Device Simulator: simula el toque de un dedo, pero no el rendimiento.
Versión final: une A4.3 (bocetos) y A4.7 (implementación) en una sola actividad.
Parte 1, boceto (8 min): dos esquemas sobre la plantilla con la safe area; medidas en pt/dp y orientación; comparar con cinco criterios (oclusión, precisión, una mano, accesibilidad, descubribilidad) y elegir uno.
Parte 2, Unity (22 min, sobre su copia del proyecto original):
1. Instalar Input System 1.19.0 desde el Package Manager y poner Active Input Handling = Both (reiniciar el editor).
2. Implementar el esquema elegido: joystick + botón (OnScreenStick + OnScreenButton) o arrastre + autodisparo. La nave no lee el dispositivo: solo recibe la intención.
3. Canvas en Scale With Screen Size y controles dentro de Screen.safeArea.
4. Probar en el Device Simulator con un teléfono con muesca y uno sin muesca.
5. Anotar lo que el simulador NO pudo probar (dos dedos a la vez, comodidad, rendimiento): se prueba en el teléfono, más adelante en la unidad.
Buena respuesta: decide la orientación sabiendo su efecto sobre el spawn, respeta 44 pt / 48 dp, no pone controles bajo la muesca y reconoce que el autodisparo cambia el game design.
Referencia para destrabar (no entregar): ShipInputAdapter.cs, MobileControlsVisibility.cs y los controles del prefab UICanvas (creados con Editor/PorteoSetup.cs).
Errores frecuentes: olvidar Active Input Handling; si el código está en un asmdef, agregar la referencia a Unity.InputSystem; poner el control fuera del Canvas.
Si no terminan: completan en casa y suben la captura al aula virtual. Avance del TP 3: sección 3 (control y HUD).

## 14 | Probalo con tu mano
tipo: actividad
kicker: PLAYTEST DE PAPEL · 7 MIN
- HUD a escala sobre tu teléfono
- ¿Llegás a todo?
- ¿Qué tapa el pulgar?
pregunta: ¿Coincide con lo que mostró el simulador?
notas:
Glosario (conceptos cortos para la docente):
• Playtest de papel: prueba con personas usando un prototipo dibujado, antes de probar en el dispositivo.
Consigna del playtest: dibujar el HUD que implementaron, a escala, sobre la silueta del propio teléfono; sostenerlo y comprobar si se llega a todo y qué tapa el pulgar. Es barato y se hace con personas reales: la comodidad no se prueba en el editor.
Comparar con A4.7: el simulador dijo dónde están los controles; la mano dice si se pueden usar.
Cierre: un buen layout no garantiza comodidad; eso lo dicen las personas. Verificar quién ya tiene la depuración USB funcionando.

## 15 | Vistazo: del editor al teléfono
tipo: contenido
kicker: VISTAZO · 3 MIN · TAREA
- Build Profiles → Android
- Player Settings: identidad y 64 bits
- Build genera un .apk
- Tarea: su primer APK en casa
captura: imagenes/u4-build-profiles-android.png | Build Profiles en Unity 6000.3.11f1: perfil Android activo
fuente: Unity 6.3 Manual — Build your application for Android; Android Player settings
notas:
Glosario (conceptos cortos para la docente):
• Build Profiles: ventana de Unity 6 (File > Build Profiles) que reemplaza a Build Settings; cada perfil guarda una plataforma y sus opciones.
• Switch Platform: cambiar la plataforma activa; Unity reimporta los assets y la primera vez tarda.
• APK: archivo instalable de Android. AAB (App Bundle): formato para publicar en Google Play; no se instala a mano.
• IL2CPP: backend que convierte el C# a C++ y lo compila a código nativo; es el único que habilita ARM64.
• ARM64: arquitectura de 64 bits de los procesadores de los teléfonos actuales.
Por qué acá: acaban de implementar los controles y el paso natural es verlos en el teléfono. Es solo un vistazo del camino; el detalle y los problemas se trabajan más adelante en la unidad, con los teléfonos.
Mostrar en vivo (3 min), sin compilar: File > Build Profiles; elegir Android y Switch Platform. Recorrer las marcas rojas de la captura: el perfil activo, Build App Bundle (destildado = sale un .apk) y Development Build (lo necesita el Profiler).
Tarea (guía en el aula virtual):
1. Switch Platform a Android en su copia del proyecto.
2. Edit > Project Settings > Player > Android > Other Settings: Scripting Backend = IL2CPP y tildar ARM64. Hacerlo en Project Settings y no en la sección Player Settings del Build Profile: si se edita ahí, el perfil guarda una copia propia (en nuestro proyecto pasó: Company y Product quedaron en Assets/Settings/Build Profiles y no en ProjectSettings).
3. Botón Build (no Build And Run), carpeta Builds/ fuera de Assets, nombre AsteroideTest.apk. Si aparece "Unsupported Input Handling on Android", tocar Ignore y anotarlo.
4. Traer el .apk y anotar cuánto tardó la build y qué carteles aparecieron.
Por qué en casa: la primera build con IL2CPP tarda varios minutos (Gradle descarga y compila); hecha en casa, la práctica con el teléfono no pierde ese tiempo y los problemas de drivers llegan resueltos.
Dato verificado (Unity 6.3 Manual, Build your application for Android): Build crea el archivo en la carpeta elegida; Build and Run además lo instala en el Run Device; por defecto Unity genera APK.

## 16 | Qué no resuelve esto · Tarea
tipo: cierre
kicker: CIERRE · 2 MIN
- El simulador no mide calor ni manos
- TP 3: Dossier Asteroides móvil
- Tarea: Build Support + USB + APK
- Lectura: "Leer con lupa"
fuente: Unity 6.3 Manual — Android environment setup; Android — Configure on-device developer options
notas:
Glosario (conceptos cortos para la docente):
• Build Support: módulo de Unity que permite compilar para una plataforma; acá, Android.
• Depuración USB: opción de Android que permite a la PC instalar y analizar apps en el teléfono por cable.
Cerrar con el límite de la herramienta: el simulador encontró el problema de la pantalla, pero no mide calor, batería ni comodidad. Eso se mide en sus teléfonos, más adelante en la unidad.
Tarea técnica obligatoria (sin ella no se puede hacer la práctica en el teléfono):
1. Instalar Android Build Support (con OpenJDK, Android SDK y NDK) en Unity 6000.3.11f1 desde Unity Hub.
2. En el teléfono: tocar 7 veces "Número de compilación" y activar "Depuración USB" (Android 9 o superior: Ajustes > Sistema > Avanzado > Opciones de desarrollador).
3. Comprobar que la PC ve el teléfono: cable de datos, aceptar "¿Permitir depuración USB?" y Build Profiles > Android > Run Device > Refresh (o adb devices).
4. Generar el primer APK siguiendo la slide anterior (IL2CPP + ARM64, botón Build) y traerlo instalado o en el teléfono.
Lectura (aula virtual): "Leer con lupa", el artículo de Kevuru Games con las observaciones de la cátedra (Stadia cerrado, Origin reemplazada, cifras sin fuente).
TP 3: Dossier de plataforma, Asteroides móvil (consigna en el aula virtual).

# DECK 3 | Asteroides en tu bolsillo | Unidad IV · Clase 3 · final

## 1 | Asteroides en tu bolsillo
tipo: portada
kicker: UNIDAD IV · CLASE 3 DE 3 · 90 MIN · PRÁCTICA EN DISPOSITIVO
- Build, medición, prueba y negocio en sus teléfonos
- Diseño según Plataformas de Juego · FI – UNJu · 2026
notas:
Último encuentro de la unidad. Antes de empezar: cables, depuración USB y Android Build Support verificados; APK de la docente (IL2CPP + ARM64) en un pendrive y en Drive para el plan B.
Reparto: teoría 36 min (apertura 3, repaso de la build 6, testing 9, monetización 13, TP 3 1, cierre 4) = 40 %; práctica 54 min (build e instalación 12, medición 8, A4.6 3, QA manual 10, matriz 4, A4.8 10, A4.5 7) = 60 %.
Orden pensado para el tiempo: la build va primero porque es lo que más puede fallar; mientras un grupo espera, otro ya mide.

## 2 | ¿Qué no sabemos todavía?
tipo: contenido
kicker: APERTURA · 3 MIN
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

## 3 | Antes de compilar: así viene
tipo: actividad
kicker: REPASO DE LA BUILD · 2 MIN
panel: ancho
captura: imagenes/u4-player-settings-android.png | Player Settings > Other Settings de Asteroides en Unity 6000.3.11f1, antes de cambiar nada
pregunta: ¿Qué de esto impide instalar en un teléfono de 64 bits?
notas:
Glosario (conceptos cortos para la docente):
• Scripting Backend: cómo compila Unity el código C#: Mono (código intermedio) o IL2CPP (código nativo).
• Package Name: identificador único de la app en el teléfono y en Google Play (com.empresa.juego).
• Target Architectures: tipos de procesador para los que se compila (ARMv7 de 32 bits, ARM64 de 64 bits).
Es la captura real del proyecto (Unity 6000.3.11f1, 2026-10-12), con cuatro marcas rojas: Package Name, Scripting Backend = Mono, Active Input Handling = Both y ARM64 en gris.
Respuesta esperada: ARM64 está en gris porque el backend es Mono; según la documentación de Unity 6.3, ARM64 "se habilita solo cuando Scripting Backend es IL2CPP". Sin ARM64, la app no corre en los teléfonos que solo aceptan 64 bits (según Android, los Pixel 7 fueron los primeros con soporte solo para apps de 64 bits; Google Play exige la versión de 64 bits).
Que la lean en sus máquinas: abrir Edit > Project Settings > Player > Android > Other Settings y comparar con la captura.

## 4 | Así tiene que quedar
tipo: contenido
kicker: BUILD · 2 MIN
- Una sola fuente: Project Settings
- El Build Profile puede pisarla
- Both: aviso, no error
ajustes: Player Settings · Android | Company Name: *Unju | Product Name: *AsteroideTest | Package Name: com.Unju.AsteroideTest | Minimum API Level: API 25 (Android 7.1) | Scripting Backend: *IL2CPP | Target Architectures: *ARM64 | Build App Bundle: No: sale un .apk | Development Build: *Sí, para el Profiler
fuente: Unity 6.3 Manual — Android Player settings; Build your application for Android
notas:
Glosario (conceptos cortos para la docente):
• Build Profile: perfil de compilación de Unity 6; puede tener sus propios Player Settings, que pisan los del proyecto.
• Fuente de verdad: el único lugar donde se decide un valor.
Dos caminos: Build crea solo el archivo; Build and Run además lo instala en el Run Device (manual de Unity 6.3). Sin teléfono, siempre Build, en la carpeta Builds/ fuera de Assets. La plataforma se mueve: Google Play exige AAB y, desde el 31/08/2026, apuntar a API 36; Unity 6.3 soporta Android 7.1 (API 25) o superior. iOS: Unity genera un proyecto de Xcode, que solo corre en macOS; en la cátedra, iOS es conceptual.
Los valores resaltados son los que hay que cambiar; el resto ya viene bien. El Package Name se arma solo con Company y Product (com.Unju.AsteroideTest) mientras "Override Default Package Name" esté destildado.
Una sola fuente: cambiar todo en Edit > Project Settings > Player. Si se edita la sección Player Settings dentro del Build Profile, el perfil guarda una copia propia; en el proyecto pasó: Company y Product quedaron en Assets/Settings/Build Profiles/Android™.asset y no en ProjectSettings. Dos lugares para el mismo dato es una fuente de errores difícil de ver.
Active Input Handling = Both: la documentación de Unity 6.3 dice que no está soportado en Android. Se mantiene porque el menú usa el StandaloneInputModule clásico; al compilar se toca Ignore y queda registrado. Evidencia (2026-10-12): la build en batchmode terminó bien y el aviso solo apareció en el log. La corrección de fondo es reemplazar el módulo del EventSystem (prefab Game) por InputSystemUIInputModule y dejar solo Input System; no se hizo en el repositorio.
Orientación: la decide cada grupo según su esquema de A4.3 (Resolution and Presentation > Default Orientation).

## 5 | Cuando la build se frena
tipo: actividad
kicker: DIAGNÓSTICO · CARTELES REALES · 2 MIN
- Input: Ignore y anotar
- Sin teléfono: usar Build
- No instala: ¿y ARM64?
captura: imagenes/u4-dialogo-input-handling.png + imagenes/u4-dialogo-sin-dispositivo.png | Los dos carteles, tal como aparecieron en Unity 6000.3.11f1
pregunta: ¿Cuál es un error y cuál es un aviso?
notas:
Glosario (conceptos cortos para la docente):
• Aviso (warning): Unity informa un riesgo, pero deja seguir.
• Error: Unity no puede terminar la tarea.
• adb (Android Debug Bridge): herramienta de línea de comandos que conecta la PC con el teléfono.
Cartel 1, "Unsupported Input Handling on Android": es un aviso. Ignore sigue con la build; Cancel Build la corta. Causa: Active Input Handling = Both (ver la slide anterior).
Cartel 2, "No Android devices connected": aparece con Build and Run cuando la PC no ve ningún teléfono. Qué hacer: OK y usar Build; o conectar con un cable de datos, aceptar en el teléfono "¿Permitir depuración USB?" y tocar Refresh en Run Device. Comprobar con adb devices (el teléfono tiene que figurar como "device"; "unauthorized" significa que falta aceptar el diálogo). En Windows puede hacer falta el driver USB del fabricante.
Tercer caso, sin captura: el APK se copia, pero el teléfono no lo instala o no lo abre. Primera sospecha: se compiló sin ARM64. En el curso todavía no se vio; está documentado por Android para los teléfonos que solo aceptan 64 bits.
Respuesta a la pregunta: el primero es un aviso (deja seguir); el segundo frena Build and Run, pero no Build.

## 6 | De la PC al teléfono
tipo: demo
kicker: BUILD E INSTALACIÓN · 12 MIN · GRUPOS
- ¿Trajeron el APK? Instalar
- ¿No? Seguir los pasos
- Con cable: Build and Run
flujo: Build Profiles: Android activo | Player Settings: IL2CPP + ARM64 | Teléfono con depuración USB | Build and Run (o Build → .apk) | El juego abre en el teléfono
fuente: Unity 6.3 — Build your application for Android; Collect performance data on a target platform
notas:
Glosario (conceptos cortos para la docente):
• Build: versión compilada del juego, lista para instalar.
• Development Build: build con información de depuración que permite conectar el Profiler.
• Autoconnect Profiler: opción para que el Profiler se conecte solo al iniciar el juego.
• Build and Run: compilar, instalar y abrir en el dispositivo conectado, en un solo paso.
Plan B: si la build falla en la máquina del grupo, se instala el APK de la docente (cable y adb install -r, o Drive y aceptar «Instalar apps de fuentes desconocidas»). Se pierde el Profiler; no se pierden el QA manual ni la matriz. Lo que no se pudo medir se declara en el dossier. El APK de depuración no se publica: para Google Play hacen falta firma propia y un .aab.
Pasos con cable (para medir con el Profiler): en Build Profiles, Android activo; Development Build y Autoconnect Profiler tildados; teléfono conectado con la depuración activada; Build and Run. Según el manual de Unity 6.3, con Development Build y Build and Run Unity prepara el túnel del Profiler antes de abrir la app. Primero lo hace la docente; después cada grupo, con el teléfono de un integrante.

## 7 | Medir, no opinar
tipo: actividad
kicker: MEDICIÓN · 8 MIN
- H1: ¿picos de GC al disparar?
- H2: ¿fps estable 5 minutos?
- Anotar modelo y versión
actividad: Capturen el Profiler y anoten los valores.
fuente: Unity 6.3 — Profiling on a target device; e-book Unity 6, p. 11
notas:
Glosario (conceptos cortos para la docente):
• GC (garbage collector): proceso que libera memoria que ya no se usa; si trabaja mucho, produce tirones.
• GC Alloc: memoria reservada en cada frame que después tendrá que liberar el GC.
• Hipótesis: suposición que se comprueba midiendo.
Versión final: la partida de medición dura 5 minutos; en el TP 3 pueden extenderla a 10.
Hipótesis completas: H1, ¿cada disparo (Instantiate del láser) genera picos de GC? Métrica: GC Alloc por frame. H2, ¿el juego sostiene el fps durante 10 minutos? Métrica: tiempo de frame a lo largo del tiempo. Registrar modelo de teléfono, versión de Android y temperatura percibida.
Advertencia honesta: Asteroides es liviano y lo más probable es que ande bien en casi cualquier teléfono. Si la medición no muestra problemas, la respuesta correcta es decirlo con los datos. El objetivo es aprender a formular y medir hipótesis.
Imagen sugerida (opcional, sin recuadro en la slide): Profiler conectado a un teléfono con un pico de GC marcado.

## 8 | Editor vs. teléfono
tipo: actividad
kicker: COMPARAR
| Medición | Editor (PC) | Teléfono |
| fps promedio | | |
| Tiempo de frame máximo | | |
| GC Alloc por disparo | | |
| fps a los 5 minutos | | |
actividad: Completen con sus mediciones.
notas:
Glosario (conceptos cortos para la docente):
• fps promedio: cantidad media de imágenes por segundo durante la medición.
• Tiempo de frame máximo: el cuadro que más tardó; muestra los tirones que el promedio esconde.
Conclusión esperada: el número del editor no predice el del teléfono. Pasar a A4.6 (slide siguiente), que muestra el mismo problema con datos de 10 minutos.

## 9 | A4.6 — Anda bien los primeros 5 minutos
tipo: actividad
kicker: INDIVIDUAL · 3 MIN · ORAL
- 60 fps al empezar
- 35–40 fps a los 8 minutos
- En el editor: 200 fps
pregunta: ¿Cuello de botella, métrica, herramienta? ¿Qué NO sirve?
notas:
[En la versión 3, A4.6 se hace acá, con el teléfono y el Profiler a mano.]
Glosario (conceptos cortos para la docente):
• Cuello de botella: la parte del sistema que limita el rendimiento.
• Métrica: valor que se mide (por ejemplo, el tiempo de frame).
• Throttling térmico: el teléfono baja la frecuencia del procesador para no calentarse.
Situación completa: "60 fps al empezar, 35–40 fps a los 8 minutos en un teléfono de gama media; en el editor, 200 fps".
Respuesta esperada: throttling térmico agravado por el overdraw de las partículas; medir el tiempo de frame a lo largo del tiempo y el estado térmico con el Profiler en el dispositivo; fijar 30 fps o un presupuesto del 65 % y reducir el overdraw. El editor y el Device Simulator no sirven para esto.
Contrastar con la medición de 10 minutos que acaban de hacer: ¿su teléfono se comporta igual?

## 10 | Interrumpir a propósito
tipo: actividad
kicker: QA MANUAL · 10 MIN
| Caso | Acción | Esperado | Real |
| QA-01 | Llamada o alarma | Pausa y espera un toque | |
| QA-02 | Inicio y volver | Pausado, sin daño | |
| QA-03 | Bloquear la pantalla | Pausado | |
| QA-04 | Teclado en pantalla | Documentar | |
| QA-05 | Cierre forzado | Qué se pierde | |
| QA-06 | Mover y disparar a la vez | Responden los dos | |
| QA-07 | Controles bajo el pulgar | ≥ 48 dp, no tapan | |
fuente: Unity 6.3 — OnApplicationPause / OnApplicationFocus; Android — activity lifecycle
notas:
Glosario (conceptos cortos para la docente):
• QA manual: prueba hecha por una persona, siguiendo pasos definidos.
• Cierre forzado: terminar la app desde los ajustes del sistema.
Casos completos: QA-01 llamada o alarma durante la partida (esperado: el juego se pausa y espera un toque); QA-02 botón de inicio y volver (pausado, sin daño a la nave); QA-03 bloquear y desbloquear la pantalla (pausado); QA-04 abrir el teclado en pantalla, si aplica (documentar qué pasa); QA-05 cierre forzado y reabrir (documentar qué se pierde).
Casos nuevos de la versión 3 (controles portados): QA-06, mover con el joystick y disparar con el botón al mismo tiempo, con dos dedos (el Device Simulator simula un solo dedo, así que este caso solo se prueba acá); QA-07, medir que cada control tenga al menos 48 dp y comprobar que el pulgar no tape la zona por donde caen los asteroides.
Mismo formato de caso de prueba de la Unidad 2 (esperado vs. real). Si los grupos todavía no corrigieron el defecto, probar la versión con defecto: el resultado real va a contradecir al esperado, y eso es un hallazgo.

## 11 | La matriz del curso
tipo: actividad
kicker: COMPATIBILIDAD · 4 MIN
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

## 12 | ¿Qué prueba cada herramienta?
tipo: contenido
kicker: TESTING EN MÓVIL · 3 MIN
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

## 13 | Lo que el test automático no vio
tipo: contenido
kicker: LÍMITES · 2 MIN
- ¿Coinciden tests y QA manual?
- ¿Qué apareció solo en el teléfono?
- ¿Qué no se puede automatizar?
pregunta: ¿Qué protege el test y qué solo el QA manual?
notas:
Glosario (conceptos cortos para la docente):
• Test automático: prueba que corre sola y compara el resultado con lo esperado.
Respuesta esperada: los tests protegen la regla y el adaptador ante regresiones; el QA manual comprueba que el sistema operativo dispare los callbacks y qué pasa cuando se cierra el proceso. Es la frontera entre automatización y hardware real, la misma de la Unidad 3 aplicada a la plataforma.

## 14 | Mismo patrón, dos adaptadores
tipo: contenido
kicker: TESTING · ARQUITECTURA · 2 MIN
- Entrada: dispositivo → intención → nave
- Pausa: SO → adaptador → regla
- Se prueba la regla, no el dispositivo
comparacion: Entrada (ya portada): ShipInputAdapter, Ship.SetIntent // 3 tests de intención en verde | Pausa (A4.4): Adaptador OnApplicationPause, Regla de pausa // Su test de Edit Mode
fuente: Código del proyecto (ShipInputAdapter.cs, ShipIntentTests.cs); resultados del Test Runner en batchmode (2026-10-10)
notas:
Glosario (conceptos cortos para la docente):
• Adaptador: clase que traduce lo que pasa afuera del juego (un dispositivo, un aviso del sistema operativo) en una orden para la lógica del juego.
• Regla: lógica del juego que se puede probar sin el dispositivo real.
• Test inestable (flaky): test que a veces pasa y a veces falla sin que cambie el código.
• SO: sistema operativo (Android, iOS); es quien avisa al juego que pasa a segundo plano.
Versión final: la pausa (A4.4) se resuelve en el dossier del TP 3, con este mismo patrón.
Idea: el porteo de la entrada ya usó el mismo patrón que van a aplicar a la pausa en A4.4. ShipInputAdapter lee el teclado, el gamepad o los controles en pantalla y llama a Ship.SetIntent; los tests de ShipIntentTests prueban la nave con intenciones, sin ningún dispositivo, y desactivan el adaptador para aislarla.
Evidencia real del repositorio (Test Runner en batchmode, Play Mode, 2026-10-10; XML en laboratorio-adaptacion/evidencia):
1. Antes del porteo: 11 tests, 7 pasan y 4 fallan.
2. Después del porteo: 14 tests (11 + 3 nuevos). En tres corridas pasaron 10, 11 y 10. Los 3 tests nuevos pasaron siempre.
3. Tres fallas son siempre las mismas: las "hipótesis de integración" que detectan defectos reales del pool de asteroides (un asteroide se libera dos veces; NewGame no borra los asteroides viejos; un segundo NewGame acelera el spawn).
4. Una falla cambia de test entre corridas (LaserMovesUp en una, GameOverStopsSpawningAndDisablesShip en otras): el stack trace lleva al mismo defecto del pool (Laser.cs:52 → Spawner.PlayExplosion). Es un test inestable causado por el código del juego, no por el porteo.
Mensaje: un test en rojo no siempre es culpa del cambio que acabamos de hacer; hay que leer el stack trace antes de concluir. Es el ciclo de la Unidad 3 aplicado a la plataforma.

## 15 | La configuración también se prueba
tipo: demo
kicker: CÓDIGO REAL · TEST DE EDIT MODE · 2 MIN
panel: ancho
codigo: ../../proyectos-unity/Asteroides/asteroide-final/Assets/Tests/EditMode/AndroidBuildConfigTests.cs:12-26
fuente: Unity 6.3 — PlayerSettings.GetScriptingBackend; PlayerSettings.Android.targetArchitectures; Android Player settings
notas:
Glosario (conceptos cortos para la docente):
• Test de Edit Mode: test que corre en el editor sin dar Play; sirve para lógica pura y para leer la configuración del proyecto.
• PlayerSettings: API de C# que lee y escribe los Player Settings.
• NamedBuildTarget: identificador de la plataforma en la API (acá, Android).
• Bandera (flag): valor que junta varias opciones; con & se pregunta si una está prendida.
Problema primero: el APK se instala en un teléfono y en otro no. Nadie tocó el código del juego: el proyecto estaba en Mono y solo ARMv7. ¿Se puede proteger la configuración con un test?
Qué mostrar: dos de los cuatro tests de AndroidBuildConfigTests.cs. Los otros dos verifican que la API mínima sea 25 o más y que la build sea .apk y no .aab.
Evidencia real (2026-10-12, Unity 6000.3.11f1, batchmode): con el proyecto en Mono + ARMv7, 2 tests en verde (API mínima, APK) y 2 en rojo (IL2CPP, ARM64). Archivo: laboratorio-adaptacion/evidencia/asteroides-05-android-config-editmode-red.xml.
Datos de la documentación de Unity 6.3 (Android Player settings): ARM64 "se habilita solo cuando Scripting Backend es IL2CPP"; Active Input Handling = Both "no está soportado en Android".
Límites: el test lee los Player Settings del proyecto; si un Build Profile tiene Player Settings propios, no está comprobado qué valores ve el test (UNKNOWN). Y una configuración correcta no demuestra que la app abra en el teléfono ni que los controles respondan.

## 16 | Actividad A4.8: el test que cuida la build
tipo: actividad
kicker: ACTIVIDAD · 10 MIN · GRUPOS · EN UNITY
- Crear el test de Edit Mode
- Verlo en rojo a propósito
- Arreglar la configuración
- ¿Qué NO demuestra?
actividad: Entreguen la captura del Test Runner en rojo y en verde.
notas:
Glosario (conceptos cortos para la docente):
• Test Runner: ventana de Unity (Window > General > Test Runner) que ejecuta los tests y muestra verde o rojo.
• Assembly definition (asmdef): archivo que agrupa scripts; los tests de editor van en uno que solo incluye la plataforma Editor.
• Rojo a propósito: romper una condición para comprobar que el test es capaz de fallar.
Consigna completa (sobre su copia del proyecto):
1. Crear Assets/Tests/EditMode con un asmdef de tests que solo incluya la plataforma Editor (referencia: EditModeTests.asmdef del repositorio).
2. Escribir dos tests: Scripting Backend = IL2CPP y ARM64 tildado, con la estructura de la slide anterior.
3. Correrlos en el Test Runner, pestaña EditMode. Si hicieron la tarea de la build, deberían dar verde.
4. Romper a propósito: pasar a Mono, correr de nuevo y ver el rojo. Restaurar IL2CPP y ver el verde. Un test que nunca vieron fallar no prueba nada.
5. Escribir qué NO demuestra: que el teléfono acepte la app, que los controles respondan, el rendimiento.
Extensión para el grupo que termina: BuildAndroid.cs (Assets/Editor) genera el APK desde código con BuildPipeline.BuildPlayer, sin abrir la ventana. Se corre en batchmode y deja un log como evidencia; es el primer paso hacia la integración continua. Evidencia (2026-10-12): build correcta en 42 s, APK de 20 MB (laboratorio-adaptacion/evidencia/asteroides-06-build-android-apk.log).
Errores frecuentes: un asmdef de tests que incluye todas las plataformas (el código de UnityEditor no compila para el player); olvidar using UnityEditor.Build (NamedBuildTarget); correr los tests en la pestaña PlayMode.

## 17 | USD 520 millones por una pantalla de compra
tipo: contenido
kicker: MONETIZACIÓN · APERTURA · 2 MIN
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

## 18 | Modelos y formatos
tipo: contenido
kicker: MONETIZACIÓN · 3 MIN
| Modelo | Quién paga | Qué cambia en el diseño |
| Premium | Al comprar | Sin interrupciones |
| Freemium + IAP | Algunos jugadores | Tienda y progresión |
| Anuncios | El anunciante | Cuándo interrumpir |
| Híbrido | Combinación | Todo lo anterior |
fuente: App Store — Alto's Adventure (ficha consultada 2026-10-04); Google AdMob — Rewarded ads; Interstitial ad guidance
notas:
Glosario (conceptos cortos para la docente):
• IAP: compra dentro de la app.
• Rewarded: anuncio que el jugador elige ver a cambio de una recompensa.
• Interstitial: anuncio de pantalla completa, en las transiciones.
Modelos: premium (paga una vez; ejemplo, Alto's Adventure sin anuncios ni IAP); freemium + IAP (pagan algunos; la progresión y la tienda se piensan para vender); anuncios (paga el anunciante y el jugador "paga" con tiempo); híbrido. Agregar el premium corrige el programa, que solo nombra freemium e híbridos.
Formatos de anuncio: rewarded, "served after a user explicitly chooses to view" (AdMob); interstitial, solo en transiciones naturales; banner, franja fija que ocupa UI y safe area. La diferencia clave es el consentimiento: el rewarded lo pide el jugador, el interstitial se lo imponen.

## 19 | Las reglas las pone la tienda
tipo: contenido
kicker: MONETIZACIÓN · REGLAS EXTERNAS · 4 MIN
- AdMob: nunca al abrir ni en cada acción
- Apple 3.1.1: IAP obligatorio
- Probabilidades visibles al comprar
- Niños: sin publicidad personalizada
pregunta: ¿Un anuncio en cada Game Over cumple?
fuente: Google AdMob — Disallowed interstitial implementations; Apple App Review Guidelines 3.1.1 y 1.3; Google Play — Payments y Families policy
notas:
Glosario (conceptos cortos para la docente):
• Política de tienda: reglas que una app debe cumplir para publicarse.
• Loot box (caja con premios al azar): compra cuyo contenido se sortea.
AdMob prohíbe interstitials al abrir o al salir de la app, después de cada acción del usuario (como máximo, uno cada dos acciones), inmediatamente después de otro interstitial y de forma inesperada durante el juego.
Apple 3.1.1: el contenido digital se desbloquea con IAP. Apple y Google: las cajas al azar muestran las probabilidades antes de comprar. Google Play Billing es obligatorio, con excepciones por país. Apps para niños: sin publicidad personalizada ni SDKs no certificados.
Pregunta: si cada partida es corta y cada Game Over muestra un anuncio, se acerca a "después de cada acción". No hay respuesta automática: hay que leer la política y justificar.
Dato de herramienta: Unity recomienda migrar de Unity Ads directo a LevelPlay (mediación) desde abril de 2026; no se integra en esta materia.

## 20 | Monetizar cambia el juego
tipo: contenido
kicker: MONETIZACIÓN = GAME DESIGN · ÉTICA · 4 MIN
- "Continuar" cambia el Game Over
- Dificultad para vender: cambia el balance
- Vampire Survivors: nunca interrumpir
- Dark patterns y loot boxes
pregunta: Con "continuar", ¿qué rebalancearían?
fuente: Kotaku (2023), citando a poncle; PLOS ONE 2018; Journal of Business Ethics 2022; UK Gambling Commission
notas:
Glosario (conceptos cortos para la docente):
• Dark pattern: diseño que juega en contra del interés del jugador.
• Balance: relación entre dificultad, recursos y habilidad.
Detalle: "continuar con un anuncio" cambia el significado del Game Over; subir la dificultad para vender vidas cambia el balance; las pausas para anuncios cambian el ritmo. En Vampire Survivors para móvil, la monetización está "designed to never interrupt your game, always be optional" (Kotaku, 2023, citando a poncle).
Ética: dark patterns (Zagal, Björk y Lewis, 2013; citar sin enlace hasta verificar una copia legal); loot boxes asociadas con el juego problemático (Zendle y Cairns, 2018, PLOS ONE, n = 7.422): correlación, no causa; 35 técnicas percibidas como predatorias (Petrovskaya y Zendle, 2022); Bélgica prohibió mecánicas de loot box en 2018 (UK Gambling Commission). No decir que las loot boxes "causan" adicción.
Respuesta posible a la pregunta: cantidad de vidas, velocidad de los asteroides, duración de la partida y cómo se calcula el puntaje si alguien continúa.
Video opcional de tarea: Anisa Sanusi, "Dark Patterns: How Good UX Can Be Bad UX" (GDC 2017).

## 21 | Actividad A4.5: ¿cuál publicarían?
tipo: actividad
kicker: ACTIVIDAD · 7 MIN · GRUPOS + VOTO
| Propuesta | Modelo |
| P1 | Premium, US$ 2,99, sin anuncios ni compras |
| P2 | Gratis + rewarded "continuar" + IAP "quitar anuncios" |
| P3 | Interstitial al abrir y en cada Game Over + cofres al azar sin probabilidades |
actividad: ¿Cumple políticas? ¿Qué cambia? ¿Riesgos éticos? Elijan una.
notas:
Glosario (conceptos cortos para la docente):
• Cofre al azar: equivalente a una loot box.
Versión final: cada grupo vota y justifica en una frase; el debate largo va al foro del aula virtual.
Propuestas completas: P1 premium a US$ 2,99, sin anuncios ni compras. P2 gratis, rewarded "continuar con 1 vida" (una vez por partida) + IAP "quitar anuncios". P3 gratis, interstitial al abrir y en cada Game Over + cofres pagos al azar sin probabilidades + dificultad aumentada para empujar a comprar.
Respuesta esperada: P3 viola políticas (interstitial al abrir; probabilidades no informadas) y manipula la dificultad. P2 cumple, pero cambia el balance. P1 es viable, con menor alcance. Vale cualquier elección defendida con criterios y fuentes.

## 22 | TP 3: entrega y defensa
tipo: actividad
kicker: TP 3 · 1 MIN · CONSIGNA
- Una decisión de plataforma
- La evidencia del teléfono
- Lo que quedó sin probar
- A4.4 (la pausa) va en el dossier
| Criterio de coevaluación | Sí / En parte / No |
| La decisión está justificada | |
| Hay evidencia del dispositivo | |
| Se declaran los límites | |
notas:
Glosario (conceptos cortos para la docente):
• Coevaluación: los grupos se evalúan entre sí con criterios compartidos.
• Decisión de plataforma (PDR): registro de contexto, opciones, decisión y consecuencias.
Versión final (PROPUESTO, lo decide la titular): sin tiempo para la defensa en vivo, cada grupo sube un video de 3 minutos al aula virtual y coevalúa el de otro grupo con estos criterios.
Contenido de la defensa: una decisión de plataforma (contexto, opciones, decisión, consecuencias); la evidencia del teléfono que la respalda o la contradice; lo que quedó sin probar, dicho explícitamente.
A4.4, "La llamada que mata la nave", pasa al dossier: comportamiento esperado ante una interrupción; regla de pausa separada del adaptador (OnApplicationPause); test de Edit Mode de la regla; qué NO demuestra el test. El ejemplo para destrabar es ShipIntentTests.cs (aislar la regla del adaptador).

## 23 | En móvil, el límite lo pone el dispositivo
tipo: cierre
kicker: CIERRE DE UNIDAD · 4 MIN · PUENTE A UNIDAD V
- El teléfono muestra lo que el editor no
- Mismo patrón, otro juego: el Platformer
- Mismo input, otro control: el gamepad
- Consolas: el límite lo pone el fabricante
pregunta: En consola, ¿quién decide si se publica?
notas:
Glosario (conceptos cortos para la docente):
• Certificación: revisión que hace el fabricante de la consola antes de permitir que un juego se publique.
• Transferencia: aplicar lo aprendido en un caso a otro distinto.
Síntesis: en móvil el límite lo ponen la energía, el calor, la memoria, la pantalla táctil, las interrupciones y las reglas de tienda. Lo que el editor no muestra, lo muestra el teléfono.
Transferencia (1 min): el 2D Platformer ya tiene MobileMove, MobileJump y MobileShoot, pero su objeto MobileControls está vacío. El patrón adaptador → intención → personaje se reutiliza; el esquema no se copia: en un juego de plataformas importa el momento del salto (botón grande, bajo el pulgar; tolerancias como el coyote time).
Puente técnico: las mismas acciones de Input System que usamos para el dedo ya aceptan un gamepad; para jugar en una consola no hay que reescribir la nave. Lo que cambia es todo lo demás.
Pregunta puente: en consola, el fabricante certifica el juego antes de publicarlo (Microsoft publica sus requisitos; Sony y Nintendo, no). La idea transversal de las Unidades IV a VII: ¿quién pone el límite?
