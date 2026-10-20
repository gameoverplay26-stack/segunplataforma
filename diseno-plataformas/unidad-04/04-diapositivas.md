# Unidad 4 — Diapositivas, versión final (texto + notas del docente)

Fuente única de la Unidad 4: un solo archivo, `Unidad-4-2026-completa.pptx` (3 clases + anexo de consulta). Generar: `python scripts/build_decks.py` desde `diseno-plataformas/unidad-04/` (requiere `pip install python-pptx` y Pillow). Opciones: `--por-clase` genera además un `.pptx` por sección; `--decks 2 3` genera solo esas secciones por separado; `--out-dir RUTA` escribe en otra carpeta (útil si el .pptx está abierto).

**Versión final (2026-10-13).** Pedido del usuario: la unidad termina en **dos encuentros de 90 minutos** después de la Clase 1, que se dio hasta la slide 15. Se reorganizó todo el contenido restante con reparto **40 % teoría / 60 % práctica** (36 / 54 min por encuentro), sin perder temas:
- **Clase 1** (dada): slides 1–15, tal como se dieron.
- **Clase 2 — Del supuesto de PC al pulgar** (90 min): simulador y límites, A4.2 (supuestos de PC), elegir plataforma, UI táctil (mínimos, densidad, safe area, pulgar, orientación, gestos, accesibilidad), Input System, **A4.7** (une A4.3 y A4.7: boceto + implementación), playtest y vistazo de la build. Tarea: Build Support, depuración USB y primer APK.
- **Clase 3 — Asteroides en tu bolsillo** (90 min): build con capturas reales, instalación, medición, A4.6, QA manual, matriz, testing en móvil, **A4.8** (test de configuración), monetización como diseño, A4.5, TP 3 y cierre de unidad.
- **Anexo: Android en Unity 6** (11 slides de consulta, no se exponen): Build Support y External Tools, teléfono y depuración USB, Device Simulator, Build Profiles, Player Settings (identidad, 64 bits, pantalla, ícono), build e instalación, diagnóstico y, desde el 2026-10-19, dos slides de antes y después del 2D Platformer (PC y Android). Las slides de clase remiten a sus pasos. Las viñetas que empiezan con `1. ` se dibujan como pasos numerados.
- Pasan fuera del encuentro: "Leer con lupa" (lectura), A4.4 (pausa, en el dossier del TP 3) y la defensa del TP 3 (video, **PROPUESTO**).

**Continuación (2026-10-19).** Con todo el deck ya dado, se agregó la **Clase 4, "Del caso real al código"** (13 slides, 90 min, teoría 36 / práctica 54): de la safe area a la publicidad (UX y seguridad), el caso FTC vs. Epic leído como falla de input, el porteo PC → Android en código real (input y pantalla), orientación en los dos juegos, A4.9 y un ítem nuevo del TP 3. También se pasó a esta fuente el **anexo "Los plataformeros más vendidos"**, que se había armado directamente en el .pptx: el generador agrega `tarjetas:`, `subtabla:`, `codigo2:` y el destacado `movil:`. Archivo generado: `Unidad-4-2026-completa-v3.pptx` (`python scripts/build_decks.py --version 3`).

Las versiones anteriores (v1 a v4, `.pptx` y fuentes) están en `versiones-anteriores/`.

**Formato que lee el generador (no cambiar la sintaxis):**
- `# DECK n | Título | Subtítulo` empieza un deck. `## n | Título` empieza una slide.
- Claves de una línea: `tipo:` (portada / contenido / actividad / demo / cierre), `kicker:`, `pregunta:`, `actividad:`, `video:` (admite enlaces clicables `[etiqueta](url)`: en la slide se ve solo la etiqueta), `fuente:`, `imagen:` (recuadro de imagen sugerida; no se usa).
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
fuente: Clase 28/09/2026 — Clase2-Plataformas.pptx; código del proyecto (Ship.cs 61–73, versión original)
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
video: Consulta: [Juegos de celular, historia (21 min)](https://www.youtube.com/watch?v=kEwd_CnXvaM) · [Antes de las App Stores (9 min)](https://www.youtube.com/watch?v=omq5avbt8kw)
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
Videos de consulta, en español (agregados el 2026-10-19; existencia, título, canal y fecha verificados con YouTube el 2026-10-19; el contenido no se revisó completo):
- lucasmelor, "La historia COMPLETA de los Juegos de Celular" (21 min, 24/02/2025): https://www.youtube.com/watch?v=kEwd_CnXvaM. Canal de divulgación, no académico; incluye un segmento patrocinado.
- Aranimations ES y Cerebro Sin hueso, "Antes de las App Stores: Así Era el Increíble Gaming en Celulares Java" (9 min, 12/09/2026): https://www.youtube.com/watch?v=omq5avbt8kw. Muestra la etapa previa a 2008 (Snake, J2ME, Gameloft): el teléfono ya era plataforma de juego antes del App Store, que es el hito que usa la cronología.

## 7 | Clásicos del arcade
tipo: contenido
kicker: CONTEXTO HISTÓRICO
hitos: 1972 · Pong · tenis en pantalla | 1978 · Space Invaders · nace el shooter | 1980 · Pac-Man · fenómeno cultural | 1981 · Donkey Kong · debuta Mario | 1981 · Galaga · riesgo y recompensa | 1991 · Street Fighter II · comunidad de pelea | 1992 · Mortal Kombat · lleva a la ESRB
pregunta: ¿Qué diseño impone una máquina que cobra por partida?
fuente: Kevuru Games (blog); ESRB: Game Developer, "A Brief History of the ESRB"
video: Consulta: [Academia Play, Historia de los videojuegos 1972–1983 (7 min)](https://www.youtube.com/watch?v=KRRfb-pSZy8)
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
Video de consulta, en español (agregado el 2026-10-19; existencia, título, canal y fecha verificados con YouTube el 2026-10-19; el contenido no se revisó completo): Academia Play, "Historia de los Videojuegos (1972-1983) Parte I" (7 min, 10/07/2019): https://www.youtube.com/watch?v=KRRfb-pSZy8. Según su descripción, recorre Pong, Space Invaders, Pac-Man y Donkey Kong hasta la crisis de 1983: los mismos hitos del gráfico.

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
captura: imagenes/u4-simulator-selector.png | Pestaña Game: Game → Simulator, y la ventana Simulator con un teléfono
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
Cómo activarlo (captura real, Unity 6000.3.11f1): 1. abrir Scenes/Game (con una escena Untitled no se ve el juego); 2. en la pestaña Game, el desplegable de la izquierda cambia de Game a Simulator (o Window > General > Device Simulator); 3. elegir el dispositivo, por ejemplo Punch Hole Left (1080×2340); 4. Play y rotar desde la barra del Simulator. Si aparece "Simulator is currently not active" (marcado en la captura), el Game View sigue en modo Game. Paso a paso para los alumnos: anexo, paso 3.

## 4 | Actividad A4.2 — Supuestos de PC
tipo: actividad
kicker: ACTIVIDAD · 12 MIN · GRUPOS
- Ship.cs 61–73: el control
- Ship.cs 46–47 y 99–115: los límites
- Spawner.cs 101–106: el spawn
- Prefab Game: Canvas y cámara
actividad: 5 supuestos: dónde (archivo:línea), qué pasaría, qué eje.
codigo: git:e766f8c:../../proyectos-unity/Asteroides/asteroide-final/Assets/Scripts/Ship.cs:61-63,66-68,71-73 ## 61: si se aprieta la barra espaciadora y se puede, la nave dispara ; 66: si se aprieta la flecha izquierda, la nave va a la izquierda ; 71: si se aprieta la flecha derecha, va a la derecha
notas:
Glosario (conceptos cortos para la docente):
• Spawn: aparición de un objeto en el juego; acá, los asteroides.
• Prefab: objeto de Unity guardado como plantilla reutilizable.
• Canvas: contenedor de la interfaz (UI) en Unity.
• Input.GetKey: lectura directa de una tecla en el sistema de input clásico de Unity.
Consigna completa: listar al menos 5 supuestos que dejan de valer en un teléfono, indicando dónde están (archivo:línea), qué pasaría en móvil y a qué eje pertenecen (input, pantalla, UI, ciclo de vida, rendimiento).
La respuesta completa es la tabla S1–S13 de 02-caso-practico. Para aprobar alcanza con S1 (teclado), S3/S4/S5 (límites, cámara, spawn), S6 (Canvas en Constant Pixel Size) y S8 (sin pausa).
Pista si se traban: "¿qué pasa con la cámara si la pantalla es más angosta que alta?".
Importante (versión 3): el código de la slide es la versión **original** de Ship.cs, leída de la versión original guardada en el repositorio. En el repositorio, Ship.cs ya tiene el porteo de entrada (Ship.SetIntent + ShipInputAdapter). Los grupos analizan la versión original: si trabajan con el repositorio clonado, que lo hagan sobre ese commit (git checkout e766f8c -- proyectos-unity/Asteroides/asteroide-final/Assets/Scripts/Ship.cs) o con la copia del TP. No mostrar todavía la solución.

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
codigo: ../../proyectos-unity/Asteroides/asteroide-final/Assets/Scripts/ShipInputAdapter.cs:18-27 ## 18–21: "Mover" se hace con las flechas del teclado ; 22–23: …o con el stick y la cruz del joystick ; 25–27: "Disparar" es la barra espaciadora o el botón A ; Los botones en pantalla se hacen pasar por ese joystick
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
En el simulador el toque se hace con el mouse y es de un solo dedo. El Foldable Device del simulador sirve para ver que la relación de aspecto cambia en el mismo teléfono (plegado y desplegado). Paso a paso: anexo, paso 3.

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
- 1. File > Build Profiles
- 2. Android → Switch Platform
- 3. Botón Player Settings
- 4. Tarea: su primer APK
captura: imagenes/u4-build-profiles-android.png + imagenes/u4-switch-platform.png | Build Profiles: perfil Android activo y el botón Switch Platform
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
Switch Platform aparece abajo a la derecha mientras Android no sea la plataforma activa. Paso a paso con capturas: anexo, pasos 4 a 7.

## 16 | Qué no resuelve esto · Tarea
tipo: cierre
kicker: CIERRE · 2 MIN
- El simulador no mide calor ni manos
- TP 3: Dossier Asteroides móvil
- Tarea: Build Support + USB + APK
- Lectura: "Leer con lupa"
captura: imagenes/u4-external-tools.png | Edit > Preferences > External Tools > Android: las 4 casillas tildadas
fuente: Unity 6.3 Manual — Android environment setup; Android — Configure on-device developer options
notas:
Glosario (conceptos cortos para la docente):
• Build Support: módulo de Unity que permite compilar para una plataforma; acá, Android.
• Depuración USB: opción de Android que permite a la PC instalar y analizar apps en el teléfono por cable.
Cerrar con el límite de la herramienta: el simulador encontró el problema de la pantalla, pero no mide calor, batería ni comodidad. Eso se mide en sus teléfonos, más adelante en la unidad.
Tarea técnica obligatoria (sin ella no se puede hacer la práctica en el teléfono):
1. Instalar Android Build Support (con OpenJDK, Android SDK y NDK) en Unity 6000.3.11f1 desde Unity Hub, y verificar en Edit > Preferences > External Tools > Android que JDK, Android SDK Tools, Android NDK y Gradle estén tildados como "Installed with Unity (recommended)" (captura de la slide; anexo, paso 1).
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
Paso a paso con capturas: anexo, pasos 5 y 6 (identidad, 64 bits, orientación, safe area e ícono). Dato real: en Edit > Project Settings > Player el proyecto sigue en DefaultCompany / UnityUnitTestingTutorial; los valores Unju / AsteroideTest solo existen dentro del Build Profile.

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
Tabla de diagnóstico completa (incluye adb unauthorized, ícono negro y adb logcat): anexo, paso 8.

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
Paso a paso para los grupos: anexo, pasos 2 (teléfono), 4 (Build Profiles) y 7 (build e instalación).

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
codigo: ../../proyectos-unity/Asteroides/asteroide-final/Assets/Tests/EditMode/AndroidBuildConfigTests.cs:13-17,21-25 ## 13–17: revisa que el juego se compile con IL2CPP ; 21–25: revisa que la build incluya teléfonos de 64 bits ; Si alguien cambia esa configuración, el test se pone en rojo y avisa
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
- Países Bajos: € 1,125 M (2024)
pregunta: ¿Monetizar es negocio o diseño?
video: [La Tercera](https://www.facebook.com/watch/?v=2465461220269942) · [El Deber](https://www.facebook.com/watch/?v=541682641335363) · [El Sol de México](https://www.facebook.com/reel/657601210708360) · [DW Español (12 min)](https://www.youtube.com/watch?v=cavSjjSDdo0)
fuente: FTC, comunicado de prensa del 19/12/2022; ACM (Países Bajos), 14/01/2026
notas:
Glosario (conceptos cortos para la docente):
• FTC (Federal Trade Commission): organismo de EE. UU. que protege a los consumidores.
• COPPA: ley de EE. UU. que protege la privacidad de los menores de 13 años en línea.
• Dark patterns: diseños de interfaz que empujan al usuario a hacer algo que no quería.
Caso completo: en 2022 la FTC acusó a Epic Games por Fortnite. Epic pagó USD 275 millones por privacidad de menores (COPPA) y USD 245 millones en reembolsos. El motivo: dark patterns en la compra, con una configuración de botones "counterintuitive, inconsistent, and confusing".
Respuesta buscada: las dos cosas. Una decisión de interfaz (dónde va un botón, qué confirma una compra) tuvo consecuencias legales. Desde hoy la monetización se analiza como diseño, con reglas y con ética.
Imagen sugerida (opcional, sin recuadro en la slide): titular del comunicado oficial de la FTC del 19/12/2022.
• ACM (Autoriteit Consument & Markt): autoridad de consumo y competencia de los Países Bajos.
• Item Shop: la tienda de objetos dentro de Fortnite.
No es un caso aislado: en 2024 la ACM multó a Epic con 1.125.000 euros en total, más una orden obligatoria de cambiar la tienda, por prácticas comerciales desleales dirigidas a niños en el Item Shop de Fortnite (mensajes del tipo "consíguelo ya" y temporizadores de cuenta regresiva engañosos). Epic recurrió y el 14/01/2026 el Tribunal de Distrito de Róterdam le dio la razón a la ACM: "Epic directly exhorted children to make purchases in the Fortnite Item Shop" (ACM, "Ruling of the District Court of Rotterdam: Epic's objection declared unfounded", 14/01/2026, https://www.acm.nl/en/node/28730). Epic no discutió la infracción de los temporizadores.
Para remarcar: dos países, dos organismos y la misma conclusión: la pantalla de compra es diseño, y el diseño tiene consecuencias legales. El temporizador que apura es una decisión de interfaz, igual que el botón confuso.
Videos cortos de noticias, en español (pedido de la titular, 2026-10-19), para abrir el tema:
- La Tercera (Chile), "Millonaria multa: no fue una 'victoria magistral' para Epic Games", caso FTC: https://www.facebook.com/watch/?v=2465461220269942
- El Deber (Bolivia), "Multa millonaria a Fortnite por violar la privacidad de menores y manipulación", caso FTC: https://www.facebook.com/watch/?v=541682641335363
- El Sol de México, multa de Países Bajos por prácticas desleales con menores: https://www.facebook.com/reel/657601210708360
- DW Español, "Fortnite pagará USD 520 millones por violar privacidad de menores" (12 min, 19/12/2022): https://www.youtube.com/watch?v=cavSjjSDdo0
Verificación (2026-10-19): título y medio de los tres videos de Facebook leídos de los metadatos públicos de cada enlace; el reel de El Sol de México no muestra título, solo la descripción. Facebook puede pedir iniciar sesión para reproducirlos: probarlos antes de la clase. El video de DW se verificó en YouTube (título, canal, fecha y duración). No se miraron completos.

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

# DECK 4 | Del caso real al código | Unidad IV · Clase 4 · continuación

## 1 | Del caso real al código
tipo: portada
kicker: UNIDAD IV · CLASE 4 · CONTINUACIÓN · 90 MIN
- Publicidad, seguridad e input
- Porteo PC → Android: antes y después
notas:
Glosario (conceptos cortos para la docente):
• Porteo: llevar un juego de una plataforma a otra adaptando input, pantalla, rendimiento y distribución.
[Encuentro nuevo, agregado el 2026-10-19 a pedido de la titular: continuación después de dar todo el deck.]
Hilo del encuentro: la clase pasada cerró con la safe area ("no todo el rectángulo es tuyo"). Hoy seguimos la pregunta: ¿quién más ocupa la pantalla y el dedo del jugador? Primero el anunciante (UX y seguridad), después un caso real donde el input le costó a una empresa una sanción, y al final la respuesta técnica: el porteo PC → Android en código real.
Reparto (40/60): teoría 36 min (apertura 3, publicidad 8, caso real 5, puente 2, código 11, orientación 5, cierre 2); práctica 54 min (A4.9 30, puesta en común 8, TP 3 en clase 16).
Materiales: APK del 2D Platformer v2 (Builds/Platformer-v2.apk) y su instalador de PC (Builds/Instaladores/Platformer-v2-Setup.exe), subidos al aula virtual antes de la clase; Device Simulator como plan B. El APK es de 32 bits (ARMv7): algunos teléfonos que solo aceptan 64 bits no lo instalan. Probarlo antes con un teléfono del curso.

## 2 | La pantalla tiene dueños
tipo: contenido
kicker: APERTURA · DESDE LA SAFE AREA · 3 MIN
- Muesca y gestos: el sistema
- Controles: el pulgar
- Banner: el anunciante
- ¿Qué queda para jugar?
safearea: ¿Y si además hay un banner?
pregunta: Si suman un banner, ¿qué tapan primero?
notas:
Glosario (conceptos cortos para la docente):
• Safe area: parte de la pantalla libre de muesca, esquinas redondeadas y barra de gestos.
• Banner: anuncio en una franja fija de la pantalla, siempre visible.
• Área jugable: lo que queda para el juego después de restar sistema, controles y anuncios.
Puente con la clase pasada: la safe area la pone el sistema; los controles, el diseño; el banner, el negocio. Los tres compiten por el mismo rectángulo, y en un juego horizontal el banner tiene dos lugares posibles: abajo (donde están ◀ ▶ y SALTAR) o arriba (donde están los corazones y las monedas).
Disparador: pedir que alguien levante el teléfono en horizontal y señale dónde pondría el banner en el 2D Platformer. Respuesta esperada: no hay lugar "gratis"; cualquier franja tapa HUD, controles o nivel.
No detenerse más de 3 minutos: es la pregunta que abre el encuentro.

## 3 | Un anuncio también es input
tipo: contenido
kicker: PUBLICIDAD · UX · 4 MIN
| Formato | Qué le quita al jugador |
| Banner | Pantalla, cerca del pulgar |
| Interstitial inesperado | El toque: cae en el anuncio |
| Rewarded | Tiempo, pero lo elige |
| Sin anuncios | Nada: se cobra antes |
pregunta: Si el toque cae en el anuncio, ¿de quién es el error?
fuente: Google Play — "Understanding Google Play's Better Ads Experiences policy" (consultada el 19/10/2026)
notas:
Glosario (conceptos cortos para la docente):
• Interstitial: anuncio de pantalla completa entre dos momentos del juego.
• Rewarded: anuncio que el jugador elige ver a cambio de una recompensa.
• Better Ads Experiences: política de Google Play contra los anuncios de pantalla completa inesperados.
Idea central: en móvil, la pantalla es también el control. Un anuncio no solo ocupa espacio: compite por el mismo dedo. Si el interstitial aparece justo cuando el jugador toca SALTAR, el salto se convierte en un clic al anuncio.
Lo que dice Google Play (leído el 19/10/2026): la política busca "prevent unexpected full screen interstitials, typically when the user has chosen to do something else"; da como ejemplo de ubicación inesperada "ads that appear at the beginning of a game level"; propone como lugar adecuado "the break after the score screen in a gaming app"; los banners se aceptan si "do not interfere with normal app use or game play"; y con los rewarded "there is no concern with unexpectedness", porque el jugador eligió verlos.
Conexión: en la tercera clase vimos las reglas de AdMob (nunca al abrir ni después de cada acción). Hoy es la otra cara: el costo en UX.
Respuesta esperada a la pregunta: del diseño. Si el anuncio aparece donde el jugador ya estaba por tocar, el "clic" no es una decisión del jugador.
Qué NO resuelve esto: cumplir la política no garantiza una buena experiencia; un banner permitido igual puede quedar pegado a un botón.

## 4 | El SDK que no escribiste
tipo: contenido
kicker: PUBLICIDAD · SEGURIDAD · 4 MIN
- Goldoson (2023): 60 apps
- 100 millones de descargas
- Clics ocultos a anuncios
- Una librería de terceros
pregunta: ¿Quién responde por el código que importaron?
fuente: BleepingComputer, "Android malware infiltrates 60 Google Play apps with 100M installs" (15/04/2023), sobre el informe de McAfee Labs
notas:
Glosario (conceptos cortos para la docente):
• SDK: paquete de código de terceros que se agrega al juego (anuncios, analíticas, login).
• Adware: software que muestra o cliquea anuncios sin que el usuario lo decida.
• WebView: navegador embebido dentro de una app.
Caso (verificado el 19/10/2026 en BleepingComputer, 15/04/2023): "Goldoson" llegó a Google Play a través de 60 apps legítimas con 100 millones de descargas en total. Estaba en "a third-party library used by all sixty apps that the developers unknowingly added to their apps"; podía "perform ad fraud by clicking ads in the background without the user's consent", inyectando código en "a customized, hidden WebView". Google dijo que las apps "violated Google Play policies". El informe original es de McAfee Labs ("Goldoson: Privacy-invasive and Clicker Android Adware found in popular apps in South Korea"); el 19/10/2026 la página no abrió, así que los datos se citan a través de BleepingComputer.
Para remarcar: los desarrolladores no escribieron ese código, pero era su app. Al publicar, responde quien publica.
Qué hacer en un proyecto: usar SDKs oficiales y actualizados, revisar qué permisos agrega cada paquete, completar con honestidad la sección de seguridad de datos de la tienda e integrar lo mínimo indispensable.
Qué NO decir: "los anuncios son malware". La mayoría de los SDKs de anuncios son legítimos; el riesgo es cualquier código ajeno sin revisar (anuncios, analíticas o plugins). El 2D Platformer v2 no integra ningún SDK de anuncios.

## 5 | Caso real: el botón que cobraba
tipo: contenido
kicker: CASO REAL · INPUT · 5 MIN
- Despertar el juego: cobro
- Pantalla de carga: cobro
- Botón vecino: cobro
- Un toque, sin confirmar
pregunta: ¿Falló el código o el diseño del input?
fuente: FTC, "Fortnite Video Game Maker Epic Games to Pay More Than Half a Billion Dollars over FTC Allegations of Privacy Violations and Unwanted Charges" (19/12/2022)
notas:
Glosario (conceptos cortos para la docente):
• Input gating: bloquear la entrada mientras el juego está en un estado en el que un toque no debería hacer nada (cargando, pausado, despertando).
• Confirmación: segundo paso antes de una acción irreversible (pagar, borrar).
• Target: zona tocable de un botón; incluye el margen de separación con sus vecinos.
Es el mismo caso de la apertura de monetización de la tercera clase, ahora visto desde el input. Según la FTC, "Fortnite's counterintuitive, inconsistent, and confusing button configuration led players to incur unwanted charges based on the press of a single button": se podía pagar "while attempting to wake the game from sleep mode", "while the game was in a loading screen" o "by pressing an adjacent button while attempting simply to preview an item". La FTC lo resume así: "These tactics led to hundreds of millions of dollars in unauthorized charges for consumers." (Son alegaciones de la FTC que terminaron en un acuerdo de pago.)
Cómo leerlo con lo que ya saben: tres fallas de input con tres respuestas de diseño. Estado: el toque que despierta el juego o cae en una carga no tendría que hacer nada (input gating). Espacio: botones vecinos demasiado juntos (la slide "¿Cuánto mide un dedo?"). Confirmación: una acción que cuesta dinero no se ejecuta con un solo toque.
Respuesta esperada a la pregunta: el código hizo exactamente lo que el diseño le pidió. La falla fue de diseño del input, y la sanción fue legal.
Disparador: "¿Alguna vez compraron, borraron o saltaron algo sin querer en el teléfono? ¿En qué estado estaba la app?"

## 6 | Del caso al porteo: tres preguntas
tipo: contenido
kicker: PUENTE · 2 MIN
- Cada toque se diseña
- El porteo responde las tres
flujo: ¿Qué toca el jugador? · dispositivo | ¿Cuándo vale el toque? · estado | ¿Dónde está en pantalla? · espacio || Las slides siguientes, en código real
notas:
Glosario (conceptos cortos para la docente):
• Dispositivo: de dónde viene la entrada (teclado, gamepad, pantalla táctil).
• Estado: en qué momento del juego llega (jugando, cargando, en pausa).
• Espacio: dónde está el control y qué ocupa en pantalla (tamaño, safe area, orientación).
Transición: el caso de la FTC deja tres preguntas, y el porteo PC → Android las tiene que responder. Las dos slides siguientes muestran en código real la primera (dispositivo) y la tercera (espacio). La segunda (estado) ya la trabajaron con las interrupciones y la pausa (A4.4).

## 7 | Antes y después: el input
tipo: contenido
kicker: CÓDIGO REAL · PC → ANDROID · 2D PLATFORMER · 6 MIN
codigo2: ANTES · PC: lee el teclado = git:e766f8c:../../proyectos-unity/2D-Platformer-Unity-main/Assets/Scripts/PlayerController.cs:67-68,73,77-79 ## 67: si el personaje está parado en el suelo… ; 73: …lee las flechas o A/D del teclado para moverse ; 77: si se aprieta Espacio, salta || DESPUÉS · PC Y ANDROID: acciones = ../../proyectos-unity/2D-Platformer-Unity-v2/Assets/Scripts/PlayerInputAdapter.cs:18-21,25-26,28-30@Gamepad ## 18–21: "Mover" se hace con las flechas del teclado (y con A/D) ; 25–26: …o con el stick y la cruz del joystick ; 28–30: "Saltar" es Espacio o el botón A, y ◀ ▶ SALTAR en pantalla imitan ese joystick
panel: ancho
pregunta: ¿En qué línea de la derecha está el dedo?
notas:
Glosario (conceptos cortos para la docente):
• Input.GetAxis / GetButtonDown: lectura directa del Input Manager clásico (teclas configuradas como ejes y botones).
• InputAction: acción con nombre ("Move", "Jump") a la que se le asocian varios dispositivos (bindings).
• Binding: regla que conecta una acción con un control concreto ("<Keyboard>/space", "<Gamepad>/buttonSouth").
• Control en pantalla (OnScreenButton / OnScreenStick): botón o joystick virtual que se hace pasar por un gamepad.
• Virtual joystick: stick dibujado en la pantalla que se arrastra con el pulgar.
• Touch phase: etapa de un toque (Began, Moved, Stationary, Ended, Canceled).
Antes (izquierda, código original del juego): el PlayerController lee el teclado dentro de su propio Update. En el teléfono no hay teclado: el menú se puede tocar, pero el personaje no se mueve.
Después (derecha, versión 2): el adaptador declara dos acciones con sus bindings. Las líneas resaltadas son del gamepad, y los botones en pantalla ◀ ▶ SALTAR simulan justamente "<Gamepad>/dpad" y "<Gamepad>/buttonSouth". Cada frame, el adaptador llama a PlayerController.SetIntent(dirección, salto): el jugador recibe una intención, no una tecla. Es el mismo patrón que vieron en Asteroides ("La intención en código"), ahora en el segundo juego.
Respuesta esperada a la pregunta: en ninguna. El dedo entra como un gamepad virtual; por eso el mismo código sirve para teclado, gamepad y pantalla.
Alternativa (no usada en el proyecto), para gestos como deslizar: leer los toques directamente con EnhancedTouch. Se habilita con EnhancedTouchSupport.Enable() y se recorre Touch.activeTouches; cada toque tiene una phase (Began al apoyar, Moved al deslizar, Ended al levantar). Sirve para gestos; para botones conviene el control en pantalla, porque ya resuelve presionar y soltar.
Qué NO resuelve esto: el botón virtual no tiene relieve ni recorrido; el pulgar no sabe si lo está tocando. Por eso el tamaño, la separación y la ubicación siguen siendo decisiones de diseño.

## 8 | Antes y después: la pantalla
tipo: contenido
kicker: CÓDIGO REAL · RESOLUCIÓN Y ORIENTACIÓN · 5 MIN
codigo2: ANTES · PC: cualquier orientación = git:e766f8c:../../proyectos-unity/2D-Platformer-Unity-main/ProjectSettings/ProjectSettings.asset:62-65@Portrait ## 62: el juego puede girar a vertical (1 = sí, 0 = no) ; 63: también a vertical dado vuelta ; 64–65: y a horizontal, hacia los dos lados ; En la versión 2, las líneas 62 y 63 pasan a 0 || DESPUÉS · ANDROID: se adapta a la safe area = ../../proyectos-unity/2D-Platformer-Unity-v2/Assets/Scripts/SafeAreaFitter.cs:33-35,43-44@safe ## 33: le pregunta al teléfono qué zona no tapa la muesca ni la barra ; 34–35: mide el ancho y el alto de la pantalla ; 43–44: achica el área de los botones a esa zona libre
panel: ancho
pregunta: ¿Por qué el juego de PC nunca necesitó estas líneas?
notas:
Glosario (conceptos cortos para la docente):
• Viewport: parte de la pantalla donde la cámara dibuja.
• Aspect ratio: relación entre ancho y alto de la pantalla (16:9, 19,5:9, 4:3).
• Canvas Scaler: componente de la UI de Unity que escala la interfaz a partir de una resolución de referencia (acá, 1920 × 1080).
• Aspect ratio pinning (o letterboxing): fijar una relación de aspecto y rellenar el resto con bandas.
• Screen.safeArea: rectángulo, en píxeles, libre de muesca y barra de gestos.
Antes (izquierda, configuración original): el juego aceptaba las cuatro orientaciones, retrato incluido, para un juego de desplazamiento lateral. En PC nadie lo notaba: el monitor no rota y no tiene muesca.
Después (derecha, versión 2): SafeAreaFitter lee la safe area de la pantalla y ajusta el contenedor de los controles para que ningún botón quede bajo la muesca o la barra de gestos. Usa UnityEngine.Device.Screen, que también responde al Device Simulator. Además, la orientación quedó fija en horizontal (solo Landscape Left/Right) y el Canvas Scaler mantiene 1920 × 1080 con match 0,5.
Respuesta esperada a la pregunta: porque en PC la pantalla era un supuesto fijo (un monitor horizontal, sin muesca, con mouse). En móvil, la pantalla cambia según el teléfono, la orientación y el sistema.
Qué NO resuelve esto: la safe area protege los controles, no el nivel; si los botones tapan los pozos, hay que mover la cámara (pendiente en la v2: margen inferior de cámara).

## 9 | Un juego, dos orientaciones
tipo: contenido
kicker: ORIENTACIÓN · ASTEROIDES VS. PLATFORMER · 5 MIN
| | Asteroides (arcade) | 2D Platformer (niveles) |
| Orientación | Horizontal o vertical | Solo horizontal |
| Qué se rompe | Escala: muy chico o enorme | Se ve poco nivel |
| Por qué | Cámara fija en altura | Hay que anticipar pozos |
| Ajuste | Cámara y spawn por aspecto | Bloqueo y margen de cámara |
| Estado | Decisión pendiente | Bloqueo implementado |
pregunta: ¿La orientación la decide el género o la plataforma?
notas:
Glosario (conceptos cortos para la docente):
• Orthographic size: en una cámara 2D, la mitad de la altura visible en unidades del mundo; el ancho visible sale de multiplicarla por el aspect ratio.
• Bloqueo de orientación: desactivar en Player Settings las orientaciones que el juego no admite.
Asteroides: la cámara tiene orthographic size 5 (10 unidades de alto) y los asteroides aparecen en x ∈ [−8, 8]. En 16:9 horizontal se ven ±8,9 unidades de ancho; en 9:16 vertical, solo ±2,8: los asteroides nacen fuera de la pantalla y los sprites ocupan mucho más del ancho. Es el gráfico de la slide "Lo que encontramos" de la segunda clase. Se puede jugar en las dos orientaciones, pero hay que ajustar cámara y spawn según el aspecto. La orientación final de Asteroides sigue como decisión pendiente (DEC-LAB-005).
2D Platformer: el jugador tiene que ver lo que viene a la derecha (pozos, enemigos). En vertical vería muy poco nivel; por eso se bloqueó en horizontal. Queda pendiente el margen inferior de la cámara para que los botones no tapen el borde de las plataformas.
Respuesta esperada a la pregunta: el género propone (un arcade vertical admite las dos; un plataformero de avance lateral pide horizontal) y la plataforma obliga a decidirlo y a probarlo en pantallas reales.

## 10 | Actividad A4.9: auditar un porteo
tipo: actividad
kicker: ACTIVIDAD · 30 MIN · GRUPOS · PC Y TELÉFONO
- 1. Jugar el nivel 1 en PC
- 2. Instalar el APK y jugarlo
- 3. Completar la planilla
- 4. Ubicar un banner
| Aspecto | Qué medir |
| Controles | ¿Responden? ¿Mover y saltar a la vez? |
| Doble salto | Aciertos en 5 intentos |
| Orientación | Rotar el teléfono: ¿qué pasa? |
| Safe area | ¿Algún botón queda tapado? |
| Banner | ¿Qué taparía y dónde? |
actividad: Midan, no opinen: cada fila con una foto, una medida o un tiempo.
notas:
Glosario (conceptos cortos para la docente):
• Auditoría de porteo: revisión ordenada de qué cambió, qué mejoró y qué empeoró al pasar de plataforma.
Consigna completa (grupos de 3–4, con al menos un teléfono Android):
1. Jugar el nivel 1 en PC con el instalador (Platformer-v2-Setup.exe) o con la build de Windows. 5 min.
2. Instalar el APK en un teléfono y jugar el mismo nivel. Plan B: Device Simulator en Unity. 10 min.
3. Planilla (columnas Aspecto | PC | Android | Evidencia), 10 min: controles (¿responden?, ¿se puede mantener ◀ y saltar a la vez?); doble salto (¿sale cuando quieren?); orientación (rotar el teléfono: ¿qué pasa?); safe area (en un teléfono con muesca, ¿algún botón queda tapado?); HUD (¿se leen los corazones y las monedas?).
4. Ubicar un banner (5 min): marcar en una captura dónde iría un banner y qué taparía. Y responder: si apareciera un interstitial al empezar el nivel 2, ¿qué toque del jugador se perdería?
Errores frecuentes y corrección: "en PC anda, entonces en Android también": el input y la pantalla son otros; "el banner va donde haya lugar": en un juego horizontal no hay lugar libre.
Qué NO demuestra esta actividad: una sola sesión de juego no mide rendimiento ni batería; eso se mide con el Profiler.

## 11 | Lo que encontramos
tipo: contenido
kicker: PUESTA EN COMÚN · 8 MIN
- Un hallazgo por grupo
- Con evidencia, no opinión
- ¿Dónde empeoró más?
- ¿Dónde iría el banner?
pregunta: ¿Qué arreglarían primero y por qué?
notas:
Glosario (conceptos cortos para la docente):
• Evidencia: foto, medida o tiempo que alguien más puede revisar.
Cada grupo dice un hallazgo en una frase, con su evidencia. La docente los agrupa en tres columnas en el pizarrón: dispositivo (input), estado (cuándo vale el toque) y espacio (pantalla). Son las tres preguntas del puente.
Respuestas posibles: los botones táctiles tapan parte de la pantalla; el doble salto cuesta más en táctil que con teclado, porque no hay respuesta física del botón (por eso existen el coyote time y el buffer de salto, que siguen como decisión pendiente); en vertical la pantalla no rota, y está bien.
Pregunta de cierre del bloque: ¿qué arreglarían primero? Buena respuesta: lo que más afecta al jugar y es más barato de cambiar, justificado con su evidencia.

## 12 | TP 3: publicidad e input
tipo: contenido
kicker: TP 3 · NUEVO ÍTEM · 16 MIN EN CLASE
- Anuncios: pros y contras
- Táctil vs. teclado
- Evidencia de A4.9
- Una decisión justificada
actividad: Arranquen ahora en grupo; se entrega con el dossier del TP 3.
notas:
Glosario (conceptos cortos para la docente):
• Ítem del dossier: sección del TP 3 con consigna y criterio de evaluación propios.
Consigna del ítem 9 del TP 3, "Publicidad e input" (1 a 2 páginas):
a) Monetización con anuncios: elegir un formato (banner, interstitial o rewarded) para su juego y escribir dos ventajas y dos riesgos: de UX (área jugable, toques accidentales, interrupciones) y de seguridad (SDK de terceros). Citar al menos una política de tienda (Google Play Better Ads Experiences o AdMob).
b) Táctil vs. teclado: con la evidencia de A4.9, comparar una acción del juego (mover o saltar) en PC y en el teléfono: qué cambia en precisión, tiempo de respuesta y ocupación de pantalla.
c) Decisión: ¿lo publicarían con anuncios, sin anuncios o premium? Una decisión justificada con lo anterior y con el caso de la FTC como contraejemplo.
Criterio de evaluación propuesto: entra en "Monetización" (más efecto sobre el diseño y ética) y en "Diseño de control y HUD". El peso en la rúbrica lo define la titular (PROPUESTO).

## 13 | Qué no resuelve esto
tipo: contenido
kicker: CIERRE · 2 MIN
- Política cumplida ≠ buena UX
- Botón virtual ≠ botón físico
- Sin teléfono no hay certeza
- Todo SDK es código ajeno
notas:
Glosario (conceptos cortos para la docente):
• Error conceptual: idea que parece correcta y lleva a decisiones equivocadas.
Errores frecuentes y su corrección:
• "Si cumple la política de Google Play, el anuncio está bien": la política fija un piso; la UX se prueba jugando.
• "Un botón en pantalla es igual a uno físico": no tiene relieve ni recorrido; necesita tamaño, separación y una respuesta visual.
• "Lo probé en el Device Simulator": el simulador no tiene dedos reales, multitouch ni muesca física.
• "Los anuncios son malware": no; el riesgo es cualquier SDK de terceros que no se revisa.
Cierre: el porteo no es "compilar para Android": es volver a responder qué toca el jugador, cuándo vale y dónde está.

# DECK 5 | Anexo: Android en Unity 6 | Unidad IV · Anexo de consulta

## 1 | Anexo: Android en Unity 6
tipo: portada
kicker: UNIDAD IV · ANEXO DE CONSULTA · NO SE EXPONE
- Paso a paso con capturas de Unity 6000.3.11f1
- Para la tarea y la práctica en el teléfono
notas:
Anexo de consulta: no ocupa tiempo de clase. Los alumnos lo usan para la tarea entre encuentros y durante la práctica en el teléfono. Las slides de clase remiten acá.
Todas las capturas son de Unity 6000.3.11f1 (Windows), tomadas por la docente el 2026-10-12 y el 2026-10-13. Las marcas rojas se agregaron después.

## 2 | Build Support y External Tools
tipo: contenido
kicker: ANEXO · PASO 1 · INSTALAR
- 1. Unity Hub > Installs > Add modules
- 2. Android Build Support (+ OpenJDK, SDK, NDK)
- 3. Edit > Preferences > External Tools
- 4. Android: las 4 casillas tildadas
captura: imagenes/u4-external-tools.png | Edit > Preferences > External Tools > Android (Unity 6000.3.11f1)
fuente: Unity 6.3 Manual — Android environment setup
notas:
Glosario (conceptos cortos para la docente):
• JDK: kit de Java que usa la compilación de Android.
• SDK / NDK: herramientas de Android para compilar y para el código nativo.
• Gradle: sistema que arma el APK a partir de lo que exporta Unity.
• Preferences vs. Project Settings: Preferences son ajustes del editor en esta máquina; Project Settings son del proyecto y viajan con él.
Pasos: en Unity Hub, Installs, menú de la versión 6000.3.11f1 > Add modules > Android Build Support con OpenJDK y Android SDK & NDK Tools. Después, en el editor: Edit > Preferences > External Tools, sección Android, al final de la página. Las cuatro casillas "… Installed with Unity (recommended)" (JDK, Android SDK Tools, Android NDK y Gradle) tienen que estar tildadas, con rutas dentro de la carpeta del editor (…/PlaybackEngines/AndroidPlayer).
Si una ruta aparece en rojo o vacía, reinstalar el módulo desde Unity Hub. No apuntar a otro JDK o SDK salvo que se sepa por qué.

## 3 | El teléfono listo para probar
tipo: contenido
kicker: ANEXO · PASO 2 · TELÉFONO
- 1. 7 toques en "Número de compilación"
- 2. Opciones de desarrollador > Depuración USB
- 3. Cable de datos y aceptar el diálogo
- 4. adb devices: tiene que decir "device"
flujo: Número de compilación × 7 | Opciones de desarrollador | Depuración USB | Cable de datos + "¿Permitir depuración USB?" | adb devices → device
fuente: Android — Configure on-device developer options; Unity 6.3 Manual — Debug on Android devices
notas:
Glosario (conceptos cortos para la docente):
• adb (Android Debug Bridge): herramienta de línea de comandos que conecta la PC con el teléfono.
Pasos: Ajustes > Acerca del teléfono > tocar 7 veces "Número de compilación"; en Android 9 o superior, las Opciones de desarrollador están en Ajustes > Sistema > Avanzado. Activar "Depuración USB". Conectar con un cable de datos (muchos cables solo cargan) y aceptar en el teléfono "¿Permitir depuración USB?".
Comprobar: en Unity, Build Profiles > Android > Run Device > Refresh; o en una terminal, adb devices (adb está en la carpeta del editor: Data/PlaybackEngines/AndroidPlayer/SDK/platform-tools). "device" = listo; "unauthorized" = falta aceptar el diálogo; lista vacía = cable, puerto o driver USB del fabricante (el manual de Unity avisa que en Windows puede hacer falta).

## 4 | Device Simulator
tipo: contenido
kicker: ANEXO · PASO 3 · SIMULAR
- 1. Abrir la escena Scenes/Game
- 2. Game → Simulator
- 3. Elegir el dispositivo
- 4. Play y rotar
captura: imagenes/u4-simulator-plegable.png | Simulator con el Foldable Device (960×2658)
fuente: Unity 6.3 Manual — Device Simulator introduction
notas:
Glosario (conceptos cortos para la docente):
• Device Simulator: vista de Unity que muestra el juego con la pantalla de un dispositivo real (muesca, safe area, rotación).
Pasos: abrir Scenes/Game (si la escena es Untitled, no se ve el juego). En la pestaña Game, el desplegable de la izquierda cambia entre Game y Simulator; también se abre como ventana desde Window > General > Device Simulator. Elegir el dispositivo en el desplegable (por ejemplo, Punch Hole Left 1080×2340 o el Foldable Device, que permite ver el mismo teléfono plegado y desplegado). Dar Play y rotar desde la barra del Simulator.
Si aparece "Simulator is currently not active", el Game View está en modo Game: elegir Simulator en el desplegable.
Qué NO simula: rendimiento, memoria, capacidades de render ni giroscopio. Simula un solo dedo (con el mouse): mover y disparar a la vez solo se prueba en el teléfono.

## 5 | Build Profiles
tipo: contenido
kicker: ANEXO · PASO 4 · PLATAFORMA
- 1. File > Build Profiles
- 2. Android → Switch Platform
- 3. Build App Bundle: destildado
- 4. Development Build: para el Profiler
captura: imagenes/u4-build-profiles-android.png + imagenes/u4-switch-platform.png | Build Profiles con el perfil Android activo y el botón Switch Platform
fuente: Unity 6.3 Manual — Build your application for Android
notas:
Glosario (conceptos cortos para la docente):
• Switch Platform: cambiar la plataforma activa; Unity reimporta los assets y la primera vez tarda.
• Run Device: el teléfono en el que Build and Run instala la app.
Pasos: File > Build Profiles; en Platforms elegir Android; si todavía no es la plataforma activa, abajo a la derecha aparece Switch Platform. En Platform Settings: Build App Bundle (Google Play) destildado para obtener un .apk; Development Build y Autoconnect Profiler tildados si se va a medir con el Profiler; Run Device con el teléfono conectado (Refresh si no aparece).
El botón Player Settings (arriba a la derecha) abre los ajustes del proyecto. Cuidado: la sección Player Settings que aparece dentro del perfil crea una copia propia del perfil; para que haya una sola fuente, editar en Edit > Project Settings > Player.

## 6 | Player Settings: identidad y 64 bits
tipo: contenido
kicker: ANEXO · PASO 5 · CONFIGURAR
- 1. Edit > Project Settings > Player
- 2. Pestaña Android > Other Settings
- 3. Scripting Backend: IL2CPP
- 4. Target Architectures: ARM64
captura: imagenes/u4-player-settings-android.png | Other Settings antes de cambiar: Mono y ARM64 en gris
fuente: Unity 6.3 Manual — Android Player settings
notas:
Glosario (conceptos cortos para la docente):
• IL2CPP: backend que compila el C# a código nativo; es el único que habilita ARM64.
• Package Name: identificador único de la app (com.empresa.juego).
Pasos: arriba, Company Name y Product Name (el nombre que se ve en el teléfono); en la pestaña de Android (ícono del robot) > Other Settings: Scripting Backend = IL2CPP, tildar ARM64, Minimum API Level = Android 7.1 (API 25). El Package Name se arma con Company y Product mientras "Override Default Package Name" esté destildado.
Active Input Handling = Both: Unity 6.3 lo declara no soportado en Android; Asteroides lo mantiene por el menú (StandaloneInputModule) y al compilar aparece un aviso que se puede ignorar.
Comprobación automática: los tests de AndroidBuildConfigTests (A4.8) verifican IL2CPP, ARM64, API mínima y que la build sea .apk.

## 7 | Player Settings: pantalla
tipo: contenido
kicker: ANEXO · PASO 6 · PANTALLA
- 1. Resolution and Presentation
- 2. Default Orientation: la del esquema
- 3. Rotación: solo las permitidas
- 4. Icon: el ícono del juego
captura: imagenes/u4-resolution-presentation.png | Resolution and Presentation de Asteroides: Auto Rotation con las 4 orientaciones
fuente: Unity 6.3 Manual — Android Player settings; Unity 6.3 — Screen.safeArea
notas:
Glosario (conceptos cortos para la docente):
• Default Orientation: orientación con la que arranca el juego (fija o Auto Rotation).
• Render outside safe area: permite dibujar debajo de la muesca y las barras.
Así viene el proyecto: Default Orientation = Auto Rotation con las cuatro orientaciones permitidas, Hide Navigation Bar y Render outside safe area tildados.
Qué decidir: la orientación sale del esquema de control de A4.7. Si el juego es horizontal, dejar Landscape Left o Landscape Right (o Auto Rotation solo con esas dos). Recordar el hallazgo de A4.2: en vertical, la mayoría de los asteroides nace fuera de pantalla.
Render outside safe area: con target API 35 o superior, Android 15 dibuja de borde a borde de todos modos; por eso la UI esencial tiene que leer Screen.safeArea en lugar de confiar en esta casilla.
Ícono: en la sección Icon (o Default Icon, arriba) asignar una textura del juego. Cuidado con asignar sin querer otra textura desde el selector (en una prueba quedó un cuadro negro): si el ícono se ve negro en el teléfono, revisar este campo.

## 8 | Build e instalación
tipo: contenido
kicker: ANEXO · PASO 7 · INSTALAR
- 1. Build → Builds/AsteroideTest.apk
- 2. Copiar el .apk al teléfono y abrirlo
- 3. Aceptar "fuentes desconocidas"
- 4. Con cable: adb install -r
captura: imagenes/u4-build-botones.png | Abajo a la derecha de Build Profiles: Build (marcado) y Build And Run
video: Ejemplos de PC a Android: [Jadsa Games, Unity 6 (18 min)](https://www.youtube.com/watch?v=BuaJrjBDxK8) · [LuisCanary, .exe y .apk (13 min)](https://www.youtube.com/watch?v=nlgC6N_xfpM)
fuente: Unity 6.3 Manual — Build your application for Android
notas:
Glosario (conceptos cortos para la docente):
• Firma de depuración: firma automática de Unity para probar; no sirve para publicar en Google Play.
Pasos: botón Build (no Build And Run, que exige un teléfono conectado); carpeta Builds/ dentro del proyecto y fuera de Assets; nombre AsteroideTest.apk. Pasar el archivo al teléfono (cable, Drive o mensajería), abrirlo y aceptar "Instalar apps de fuentes desconocidas" para esa app. Con el teléfono conectado: adb install -r Builds/AsteroideTest.apk.
Alternativa desde código: Build > Android APK (Assets/Editor/BuildAndroid.cs), también en batchmode con -executeMethod BuildAndroid.Build.
Tiempo de referencia: Mono + ARMv7, 42 s y 20 MB en la PC de la docente (2026-10-12). Con IL2CPP la primera build tarda bastante más (no medido todavía).
Videos de ejemplo, en español (agregados el 2026-10-19; título, canal, fecha y descripción verificados con YouTube el 2026-10-19; no se miraron completos ni se compararon paso por paso con este anexo):
- Jadsa Games, "De PC a Android: Guía Completa para Portear y Publicar tu Juego con Unity 6" (18 min, 26/11/2025): https://www.youtube.com/watch?v=BuaJrjBDxK8. Es el que más se parece a la unidad: toma un juego de PC, agrega botones táctiles, ajusta la relación de aspecto y genera el APK y el .aab. Llega hasta la publicación en Google Play, que en esta materia no se hace.
- LuisCanary, "Generar EJECUTABLE de tu Videojuego en UNITY | Sacar .EXE y .APK (PC y Android)" (13 min, 26/02/2026): https://www.youtube.com/watch?v=nlgC6N_xfpM. Muestra la misma build para PC y para Android, útil para comparar los dos destinos. La descripción no dice la versión de Unity: si los menús no coinciden, seguir este anexo (Unity 6000.3.11f1).
- Complemento, del mismo canal que el primero: Jadsa Games, "Crear un Bundle .AAB para Android en Unity 6" (8 min): https://www.youtube.com/watch?v=COrg93Kz4o0.
Diferencia a remarcar: los videos que publican en Google Play generan .aab (Build App Bundle tildado). Para probar en el teléfono, esta unidad usa .apk (casilla destildada, paso 4).

## 9 | Diagnóstico rápido
tipo: contenido
kicker: ANEXO · PASO 8 · CUANDO ALGO FALLA
| Síntoma | Qué hacer |
| "Unsupported Input Handling on Android" | Ignore y registrarlo |
| "No Android devices connected" | Usar Build, o cable, diálogo y Refresh |
| adb dice "unauthorized" | Aceptar el diálogo en el teléfono |
| No se instala o no abre | IL2CPP + ARM64 |
| Ícono negro | Revisar Default Icon |
| Ver errores del juego | adb logcat -s Unity |
fuente: Unity 6.3 Manual — Android Player settings; Debug on Android devices
notas:
Glosario (conceptos cortos para la docente):
• Logcat: registro de mensajes del sistema Android; con -s Unity se filtran los del juego.
Detalle: el primer cartel es un aviso (deja seguir); el segundo frena Build and Run, pero no Build. "No se instala" en teléfonos que solo aceptan 64 bits: primera sospecha, falta ARM64 (documentado por Android; en el curso todavía no se vio).
Logs: con el teléfono conectado, adb logcat -s Unity muestra los mensajes de Debug.Log y los errores del juego. El paquete Android Logcat de Unity es una alternativa con ventana, pero instalarlo cambia el proyecto: no se usa sin autorización.

## 10 | Antes y después: controles
tipo: contenido
kicker: ANEXO · CASO 2D PLATFORMER · PC Y ANDROID
| Versión | Controles | Mover | Saltar | En pantalla | Orientación |
| PC · antes | Teclado y joystick (legacy) | ← → / A D, con suavizado | Espacio | Nada | Ventana |
| PC · después | Teclado y gamepad | ← → / A D, stick, cruceta | Espacio o botón A | Nada (oculto) | Ventana |
| Android · antes | Ninguno | No se puede | No se puede | Contenedor vacío | Las 4 |
| Android · después | Táctil = gamepad virtual | Botones ◀ ▶ | Botón SALTAR | ◀ ▶ SALTAR + safe area | Solo horizontal |
pregunta: ¿Qué cambió para quien juega en PC?
fuente: proyectos-unity/2D-Platformer-Unity-v2; laboratorio-adaptacion/PORTEO-PLATFORMER.md (evidencia del 19/10/2026)
notas:
Glosario (conceptos cortos para la docente):
• Input Manager (legacy): sistema de entrada clásico de Unity; los ejes y botones se configuran en Project Settings > Input Manager.
• Gamepad virtual: los botones en pantalla (OnScreenButton) se hacen pasar por un gamepad; el juego no distingue el dedo de un control físico.
• Safe area: parte de la pantalla libre de muesca y barra de gestos.
• Suavizado: el eje "Horizontal" del Input Manager acelera y frena en unos 0,3 s en lugar de saltar de 0 a 1.
Qué muestra: el mismo juego (2D Platformer, el segundo caso del laboratorio) antes y después del porteo, en las dos plataformas. La versión 2 es una copia; el original no se tocó.
PC antes: teclado (flechas o A/D, salto con Espacio) y un joystick genérico configurado en el Input Manager (el salto del joystick era "joystick button 3", que en un control de Xbox es Y, no A). PC después: las mismas teclas, más gamepad (stick, cruceta y botón A para saltar).
Android antes: el juego tenía un campo "controlmode" y un contenedor MobileControls, pero el contenedor estaba vacío; en el teléfono se podía tocar el menú, pero el personaje no se movía. Android después: botones ◀ ▶ y SALTAR, visibles solo en móvil; mantener ◀ mueve de forma continua y soltar detiene. Orientación: solo horizontal, porque es un juego de desplazamiento lateral.
Respuesta esperada a la pregunta: casi nada, y eso es lo buscado. Dos diferencias reales: ahora responde a un gamepad moderno, y el movimiento con teclado ya no tiene suavizado (respuesta inmediata). Es un cambio de sensación: hay que contarlo, no esconderlo.
Qué NO resuelve esto: el esquema táctil (botones o stick) es provisional y lo eligen los grupos; no hay coyote time ni buffer de salto; no se probó todavía en un teléfono real.

## 11 | Antes y después: proyecto
tipo: contenido
kicker: ANEXO · CASO 2D PLATFORMER · LO QUE NO SE VE
| Aspecto | Antes (original) | Después (versión 2) |
| Sistema de entrada | Input Manager | Input System 1.19 (solo "New") |
| Quién lee el input | PlayerController | Adaptador → SetIntent |
| Módulo de UI | StandaloneInputModule | InputSystemUIInputModule |
| Error "isGrounded" | 2447 por sesión | 0 |
| Build Android | Falla (URP en modo compatibilidad) | APK de 35,9 MB |
| Tests automáticos | Ninguno | 16: pasan 14, fallan 2 |
pregunta: ¿Por qué fallan 2 tests si el porteo está bien?
fuente: laboratorio-adaptacion/PORTEO-PLATFORMER.md; logs y XML en laboratorio-adaptacion/evidencia/platformer-v2-*
notas:
Glosario (conceptos cortos para la docente):
• Input System: paquete de entrada moderno de Unity; unifica teclado, gamepad y táctil.
• SetIntent: método del jugador que recibe la intención (mover, saltar) sin saber de qué dispositivo vino.
• Módulo de UI: componente del EventSystem que traduce clics y toques a eventos de botones.
• URP en modo compatibilidad: modo viejo del render de Unity; Unity 6.3 no compila builds con él activado.
Fila por fila: el input pasó del Input Manager al Input System, configurado solo en "New" porque Unity 6.3 no admite "Both" en Android. El PlayerController ya no lee teclas: un adaptador lee el dispositivo y le pasa la intención. Los menús cambiaron de módulo de UI para funcionar sin el sistema viejo.
Errores y build: el error "isGrounded" se repetía en cada frame (2447 veces en una sesión) y ahora aparece 0 veces. La build de Android del proyecto migrado fallaba por el render en modo compatibilidad; corregido eso, generó un APK de 35,9 MB (Mono, ARMv7, 9 min 25 s la primera vez).
Tests: 6 de configuración (Edit Mode) y 10 de juego (Play Mode); pasan 14.
Respuesta esperada a la pregunta: los 2 tests que fallan encontraron un defecto del juego original, no del porteo. El rayo que detecta el suelo choca con el propio jugador, así que el juego siempre cree que está en el suelo y permite saltar sin límite. Un test en rojo también es evidencia útil. Corregirlo cambia la dificultad del nivel, y esa decisión es de diseño, no técnica.
Estado: todo esto está VERIFICADO con logs y XML del 19/10/2026. La instalación en un teléfono real es UNKNOWN.

# DECK 6 | Anexo: Los plataformeros más vendidos | Unidad IV · Anexo de consulta

## 1 | Anexo: Los plataformeros más vendidos
tipo: portada
kicker: UNIDAD IV · ANEXO DE CONSULTA · DATOS DE MERCADO
- Franquicias y juegos según VGSales Wiki, con imagen de cada título
notas:
Glosario (conceptos cortos para la docente):
• VGSales Wiki: wiki colaborativa de ventas de videojuegos; publica estimaciones, no cifras auditadas.
Anexo de consulta, no se expone: datos de mercado del género del caso guía 2 (2D Platformer). Se armó directamente en el .pptx el 2026-10-19 y se pasó a esta fuente el mismo día.

## 2 | Franquicias de plataformas más vendidas (1 de 2)
tipo: contenido
kicker: ANEXO · PLATAFORMEROS · FRANQUICIAS 1–12
tarjetas: imagenes/mercado/f01.png ; 1 ; Mario (plataformas) ; 491,1 M de unidades ; 1981 · Arcade · Nintendo | imagenes/mercado/f02.png ; 2 ; Sonic (plataformas) ; 195,8 M de unidades ; 1991 · Mega Drive · Sega | imagenes/mercado/f03.png ; 3 ; Donkey Kong (plataformas) ; 104,4 M de unidades ; 1981 · Arcade · Nintendo | imagenes/mercado/f04.png ; 4 ; Crash Bandicoot ; 65,0 M de unidades ; 1996 · PS1 · Activision | imagenes/mercado/f05.png ; 5 ; Kirby ; 62,0 M de unidades ; 1992 · Game Boy · Nintendo | imagenes/mercado/f06.png ; 6 ; Mega Man ; 43,0 M de unidades ; 1987 · NES · Capcom | imagenes/mercado/f07.png ; 7 ; Ratchet & Clank ; 40,7 M de unidades ; 2002 · PS2 · Sony | imagenes/mercado/f08.png ; 8 ; Tomb Raider (plataformas) ; 40,5 M de unidades ; 1996 · Saturn · Embracer | imagenes/mercado/f09.png ; 9 ; Rayman ; 30,0 M de unidades ; 1995 · PS1 · Ubisoft | imagenes/mercado/f10.png ; 10 ; Spyro ; 30,0 M de unidades ; 1998 · PS1 · Activision | imagenes/mercado/f11.png ; 11 ; Yoshi ; 29,5 M de unidades ; 1995 · SNES · Nintendo | imagenes/mercado/f12.png ; 12 ; Castlevania ; 24,0 M de unidades ; 1986 · Famicom Disk · Konami
panel: ancho
fuente: VGSales Wiki, «Best-selling platformers» (ventas estimadas, consulta 19/10/2026); imágenes: Wikipedia, uso educativo
notas:
Glosario (conceptos cortos para la docente):
• Unidades vendidas: estimación de copias (físicas y digitales) que publica la fuente; no son cifras oficiales de las editoras.
Datos e imágenes tal como estaban en el .pptx del 2026-10-19 (fuente al pie). Las imágenes son de Wikipedia, con uso educativo.

## 3 | Franquicias de plataformas más vendidas (2 de 2)
tipo: contenido
kicker: ANEXO · PLATAFORMEROS · FRANQUICIAS 13–24
tarjetas: imagenes/mercado/f13.png ; 13 ; Metroid ; 22,8 M de unidades ; 1986 · Famicom Disk · Nintendo | imagenes/mercado/f14.png ; 14 ; Prince of Persia ; 21,0 M de unidades ; 1989 · Apple II · Ubisoft | imagenes/mercado/f15.jpg ; 15 ; SpongeBob (plataformas) ; 17,0 M de unidades ; 2001 · GBC · Nickelodeon | imagenes/mercado/f16.jpg ; 16 ; Gex ; 15,0 M de unidades ; 1995 · 3DO · Square Enix | imagenes/mercado/f17.png ; 17 ; Jak & Daxter ; 15,0 M de unidades ; 2001 · PS2 · Sony | imagenes/mercado/f18.png ; 18 ; Wario Land ; 13,4 M de unidades ; 1994 · Game Boy · Nintendo | imagenes/mercado/f19.png ; 19 ; LittleBigPlanet ; 11,5 M de unidades ; 2008 · PS3 · Sony | imagenes/mercado/f20.jpg ; 20 ; Pitfall ; 10,0 M de unidades ; 1982 · Atari 2600 · Activision | imagenes/mercado/f21.jpg ; 21 ; Adventure Island ; 10,0 M de unidades ; 1986 · NES, MSX · Hudson Soft | imagenes/mercado/f22.png ; 22 ; Oddworld ; 7,0 M de unidades ; 1997 · PS1 · Oddworld Inhabitants | imagenes/mercado/f23.png ; 23 ; Sly Cooper ; 5,4 M de unidades ; 2002 · PS2 · Sony | imagenes/mercado/f24.png ; 24 ; Banjo-Kazooie ; 5,1 M de unidades ; 1998 · N64 · Microsoft
panel: ancho
fuente: VGSales Wiki, «Best-selling platformers» (ventas estimadas, consulta 19/10/2026); imágenes: Wikipedia, uso educativo
notas:
Glosario (conceptos cortos para la docente):
• Unidades vendidas: estimación de copias (físicas y digitales) que publica la fuente; no son cifras oficiales de las editoras.
Datos e imágenes tal como estaban en el .pptx del 2026-10-19 (fuente al pie). Las imágenes son de Wikipedia, con uso educativo.

## 4 | Juegos de plataformas más vendidos (1 de 5)
tipo: contenido
kicker: ANEXO · PLATAFORMEROS · JUEGOS 1–10
tarjetas: imagenes/mercado/j01.png ; 1 ; Super Mario Bros. ; 65,9 M de unidades ; 1985 · Multiplataforma · Nintendo | imagenes/mercado/j02.jpg ; 2 ; Human: Fall Flat ; 55,0 M de unidades ; 2016 · Multiplataforma · No Brakes | imagenes/mercado/j03.jpg ; 3 ; Sonic the Hedgehog ; 51,8 M de unidades ; 1991 · Multiplataforma · Sega | imagenes/mercado/j04.png ; 4 ; Super Mario Bros. 3 ; 40,8 M de unidades ; 1988 · Multiplataforma · Nintendo | imagenes/mercado/j05.png ; 5 ; Super Mario Bros. 2 ; 37,5 M de unidades ; 1986 · Multiplataforma · Nintendo | imagenes/mercado/j06.png ; 6 ; Super Mario World ; 34,2 M de unidades ; 1990 · Multiplataforma · Nintendo | imagenes/mercado/j07.png ; 7 ; Super Mario 64 ; 32,3 M de unidades ; 1996 · Multiplataforma · Nintendo | imagenes/mercado/j08.jpg ; 8 ; New Super Mario Bros. ; 30,8 M de unidades ; 2006 · DS · Nintendo | imagenes/mercado/j09.jpg ; 9 ; Super Mario Odyssey ; 30,5 M de unidades ; 2017 · Switch · Nintendo | imagenes/mercado/j10.png ; 10 ; New Super Mario Bros. Wii ; 30,3 M de unidades ; 2009 · Wii · Nintendo
panel: ancho
fuente: VGSales Wiki, «Best-selling platformers» (ventas estimadas, consulta 19/10/2026); imágenes: Wikipedia, uso educativo
notas:
Glosario (conceptos cortos para la docente):
• Unidades vendidas: estimación de copias (físicas y digitales) que publica la fuente; no son cifras oficiales de las editoras.
Datos e imágenes tal como estaban en el .pptx del 2026-10-19 (fuente al pie). Las imágenes son de Wikipedia, con uso educativo.

## 5 | Juegos de plataformas más vendidos (2 de 5)
tipo: contenido
kicker: ANEXO · PLATAFORMEROS · JUEGOS 11–20
tarjetas: imagenes/mercado/j11.jpg ; 11 ; Sonic the Hedgehog 2 ; 25,4 M de unidades ; 1992 · Multiplataforma · Sega | imagenes/mercado/j12.png ; 12 ; New Super Mario Bros. U ; 24,2 M de unidades ; 2012 · Wii U, Switch · Nintendo | imagenes/mercado/j13.jpg ; 13 ; Sonic Dash ; 22,6 M de unidades ; 2013 · iOS · Sega | imagenes/mercado/j14.jpg ; 14 ; Donkey Kong ; 22,6 M de unidades ; 1981 · Multiplataforma · Nintendo | imagenes/mercado/j15.jpg ; 15 ; Super Mario Galaxy ; 21,9 M de unidades ; 2007 · Wii, Switch · Nintendo | imagenes/mercado/j16.jpg ; 16 ; Crash Bandicoot N. Sane Trilogy ; 20,0 M de unidades ; 2017 · Multiplataforma · Activision | imagenes/mercado/j17.png ; 17 ; It Takes Two ; 20,0 M de unidades ; 2021 · Multiplataforma · EA | imagenes/mercado/j18.jpg ; 18 ; Super Mario 3D World ; 19,1 M de unidades ; 2013 · Wii U, Switch · Nintendo | imagenes/mercado/j19.png ; 19 ; Super Mario Land ; 18,4 M de unidades ; 1989 · GB, 3DS · Nintendo | imagenes/mercado/j20.jpg ; 20 ; Sonic 3 & Knuckles ; 17,0 M de unidades ; 1994 · Multiplataforma · Sega
panel: ancho
fuente: VGSales Wiki, «Best-selling platformers» (ventas estimadas, consulta 19/10/2026); imágenes: Wikipedia, uso educativo
notas:
Glosario (conceptos cortos para la docente):
• Unidades vendidas: estimación de copias (físicas y digitales) que publica la fuente; no son cifras oficiales de las editoras.
Datos e imágenes tal como estaban en el .pptx del 2026-10-19 (fuente al pie). Las imágenes son de Wikipedia, con uso educativo.

## 6 | Juegos de plataformas más vendidos (3 de 5)
tipo: contenido
kicker: ANEXO · PLATAFORMEROS · JUEGOS 21–30
tarjetas: imagenes/mercado/j21.png ; 21 ; Super Mario Bros. Wonder ; 16,0 M de unidades ; 2023 · Switch · Nintendo | imagenes/mercado/j22.png ; 22 ; Super Mario Sunshine ; 15,4 M de unidades ; 2002 · GC, Switch · Nintendo | imagenes/mercado/j23.jpg ; 23 ; Prince of Persia: The Sands of Time ; 14,0 M de unidades ; 2003 · Multiplataforma · Ubisoft | imagenes/mercado/j24.png ; 24 ; New Super Mario Bros. 2 ; 13,4 M de unidades ; 2012 · 3DS · Nintendo | imagenes/mercado/j25.png ; 25 ; Donkey Kong Country ; 13,3 M de unidades ; 1994 · Multiplataforma · Nintendo | imagenes/mercado/j26.jpg ; 26 ; Super Mario 3D Land ; 12,9 M de unidades ; 2011 · 3DS · Nintendo | imagenes/mercado/j27.jpg ; 27 ; Super Mario All-Stars ; 12,8 M de unidades ; 1993 · SNES, Wii · Nintendo | imagenes/mercado/j28.jpg ; 28 ; Super Mario Land 2 ; 11,2 M de unidades ; 1992 · Game Boy · Nintendo | imagenes/mercado/j29.png ; 29 ; Fall Guys: Ultimate Knockout ; 11,0 M de unidades ; 2020 · Multiplataforma · Epic Games | imagenes/mercado/j30.jpg ; 30 ; Donkey Kong Country Returns ; 10,7 M de unidades ; 2010 · Multiplataforma · Nintendo
panel: ancho
fuente: VGSales Wiki, «Best-selling platformers» (ventas estimadas, consulta 19/10/2026); imágenes: Wikipedia, uso educativo
notas:
Glosario (conceptos cortos para la docente):
• Unidades vendidas: estimación de copias (físicas y digitales) que publica la fuente; no son cifras oficiales de las editoras.
Datos e imágenes tal como estaban en el .pptx del 2026-10-19 (fuente al pie). Las imágenes son de Wikipedia, con uso educativo.

## 7 | Juegos de plataformas más vendidos (4 de 5)
tipo: contenido
kicker: ANEXO · PLATAFORMEROS · JUEGOS 31–41
tarjetas: imagenes/mercado/j31.png ; 31 ; Spyro Reignited Trilogy ; 10,0 M de unidades ; 2018 · Multiplataforma · Activision | imagenes/mercado/j32.png ; 32 ; Sonic Adventure ; 9,5 M de unidades ; 1998 · Multiplataforma · Sega | imagenes/mercado/j33.jpg ; 33 ; Super Mario 3D All-Stars ; 9,1 M de unidades ; 2020 · Switch · Nintendo | imagenes/mercado/j34.png ; 34 ; Sonic Jump ; 8,8 M de unidades ; 2005 · Móvil · Sega | imagenes/mercado/j35.jpg ; 35 ; Super Mario Maker 2 ; 8,4 M de unidades ; 2019 · Switch · Nintendo | imagenes/mercado/j36.png ; 36 ; Sonic Adventure 2 ; 8,3 M de unidades ; 2001 · Multiplataforma · Sega | imagenes/mercado/j37.png ; 38 ; Mega Man X ; 7,9 M de unidades ; 1993 · Multiplataforma · Capcom | imagenes/mercado/j38.jpg ; 39 ; Sonic CD ; 7,9 M de unidades ; 1993 · Multiplataforma · Sega | imagenes/mercado/j39.jpg ; 40 ; Super Mario Maker ; 7,8 M de unidades ; 2015 · Wii U, 3DS · Nintendo | imagenes/mercado/j40.jpg ; 41 ; Crash Bandicoot 2: Cortex Strikes Back ; 7,6 M de unidades ; 1997 · PS1 · Sony
panel: ancho
fuente: VGSales Wiki, «Best-selling platformers» (ventas estimadas, consulta 19/10/2026); imágenes: Wikipedia, uso educativo. El puesto 37 no figura en la fuente
notas:
Glosario (conceptos cortos para la docente):
• Unidades vendidas: estimación de copias (físicas y digitales) que publica la fuente; no son cifras oficiales de las editoras.
Datos e imágenes tal como estaban en el .pptx del 2026-10-19 (fuente al pie). Las imágenes son de Wikipedia, con uso educativo.

## 8 | Juegos de plataformas más vendidos (5 de 5)
tipo: contenido
kicker: ANEXO · PLATAFORMEROS · JUEGOS 42–50
tarjetas: imagenes/mercado/j41.jpg ; 42 ; Kirby and the Forgotten Land ; 7,5 M de unidades ; 2022 · Switch, Switch 2 · Nintendo | imagenes/mercado/j42.jpg ; 43 ; Sonic Generations ; 7,5 M de unidades ; 2011 · Multiplataforma · Sega | imagenes/mercado/j43.jpg ; 44 ; Super Mario Galaxy 2 ; 7,5 M de unidades ; 2010 · Wii, Switch · Nintendo | imagenes/mercado/j44.jpg ; 45 ; Crash Bandicoot: Warped ; 7,1 M de unidades ; 1998 · PS1 · Sony | imagenes/mercado/j45.jpg ; 46 ; Ratchet & Clank ; 7,1 M de unidades ; 2016 · PS4 · Sony | imagenes/mercado/j46.png ; 47 ; Tomb Raider ; 7,0 M de unidades ; 1996 · Multiplataforma · Eidos | imagenes/mercado/j47.png ; 48 ; Tomb Raider II ; 7,0 M de unidades ; 1997 · Multiplataforma · Eidos | imagenes/mercado/j48.jpg ; 49 ; Yoshi's Island ; 7,0 M de unidades ; 1995 · SNES, GBA · Nintendo | imagenes/mercado/j49.jpg ; 50 ; Donkey Kong Country: Tropical Freeze ; 6,6 M de unidades ; 2014 · Wii U, Switch · Nintendo
panel: ancho
fuente: VGSales Wiki, «Best-selling platformers» (ventas estimadas, consulta 19/10/2026); imágenes: Wikipedia, uso educativo
notas:
Glosario (conceptos cortos para la docente):
• Unidades vendidas: estimación de copias (físicas y digitales) que publica la fuente; no son cifras oficiales de las editoras.
Datos e imágenes tal como estaban en el .pptx del 2026-10-19 (fuente al pie). Las imágenes son de Wikipedia, con uso educativo.

## 9 | Comparativa: franquicias y juegos
tipo: contenido
kicker: ANEXO · PLATAFORMEROS · ESTADÍSTICA
subtabla: 1 · Franquicias (top 24) por propietario
| Propietario | Cant. | Ventas (M) | % del total | Prom. (M) |
| Nintendo | 6 | 723,0 | 55,2 % | 120,5 |
| Sega | 1 | 195,8 | 15,0 % | 195,8 |
| Activision | 3 | 105,0 | 8,0 % | 35,0 |
| Sony | 4 | 72,6 | 5,5 % | 18,1 |
| Ubisoft | 2 | 51,0 | 3,9 % | 25,5 |
| Capcom | 1 | 43,0 | 3,3 % | 43,0 |
| Otros (7) | 7 | 118,6 | 9,1 % | 16,9 |
| Total | 24 | 1.309,0 | 100 % | 54,5 |
subtabla: 2 · Juegos (top 49) por editor
| Editor | Cant. | Ventas (M) | % del total | Prom. (M) |
| Nintendo | 28 | 568,1 | 63,1 % | 20,3 |
| Sega | 9 | 158,8 | 17,6 % | 17,6 |
| No Brakes | 1 | 55,0 | 6,1 % | 55,0 |
| Activision | 2 | 30,0 | 3,3 % | 15,0 |
| Sony | 3 | 21,8 | 2,4 % | 7,3 |
| Eidos | 2 | 14,0 | 1,6 % | 7,0 |
| Otros (4) | 4 | 52,9 | 5,9 % | 13,2 |
| Total | 49 | 900,6 | 100 % | 18,4 |
movil: Solo 2 de los 49 juegos nacieron en móvil (Sonic Dash y Sonic Jump). ¿Qué los hace jugables con el pulgar?
fuente: VGSales Wiki, «Best-selling platformers» (ventas estimadas, consulta 19/10/2026); imágenes: Wikipedia, uso educativo
notas:
Glosario (conceptos cortos para la docente):
• Propietario / editor: empresa dueña de la franquicia / que publicó el juego, según la fuente.
Porcentajes y promedios calculados sobre los datos de las slides anteriores (tal como estaban en el .pptx del 2026-10-19).
