# Unidad 4 — Diapositivas definitivas (texto + notas del docente)

Fuente única de los 4 decks de la Unidad 4. Basado en la arquitectura **aprobada** ([`04-diapositivas-arquitectura.md`](./04-diapositivas-arquitectura.md)).
Para regenerar los `.pptx` después de editar este archivo: `python scripts/build_decks.py` desde `diseno-plataformas/unidad-04/` (requiere `pip install python-pptx`). Opciones: `--decks 1 3` genera solo esos decks; `--version 2` agrega el sufijo `-v2` al nombre del archivo.

**Versiones:** el deck 1 está en su **versión 2** (2026-10-05): incorpora conceptos del artículo de Kevuru Games, con texto breve en las slides y notas del docente completas. Se genera con `python scripts/build_decks.py --decks 1 --version 2`. La v1 (`Unidad-4-Clase-1-2026.pptx`) se conserva como archivo; su texto fuente está en el historial de git (commit `acb7c4c`).

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
imagen: Teléfono en vertical con Asteroides corriendo, sostenido con una mano.
notas:
Presentar la unidad como continuación directa del panorama del 28/09: ese día recorrimos todas las plataformas; desde hoy, y durante cuatro clases, nos quedamos en el bolsillo del jugador.
No anticipar contenidos: la clase arranca con un problema, no con una definición ni con una herramienta.
Versión 2 de la clase (2026-10-05): incorpora conceptos del artículo "What Are the Best Platforms for Games?" de Kevuru Games (definición de plataforma, rol de las tiendas móviles, criterios para elegir plataforma), leído con mirada crítica (slide 19).

## 2 | El juego que anda… hasta que no
tipo: contenido
kicker: APERTURA
- En la PC del aula: perfecto
- En el teléfono, a los 10 min: se traba
- El teléfono quema
- Llamada, volvés… y la nave explotó
pregunta: ¿Cuántos problemas distintos hay? ¿Alguno es un "bug"?
imagen: Captura del juego con tres íconos superpuestos: termómetro, batería baja y llamada entrante.
notas:
Relato completo: "Asteroides funciona perfecto en la PC del aula. Lo instalamos en un teléfono: a los 10 minutos empieza a trabarse, el teléfono quema en la mano, y si entra una llamada y volvemos, la nave ya explotó y perdimos la partida".
Dejar que discutan 3–4 minutos. Respuesta esperada: al menos tres problemas de distinta naturaleza: (1) calor y rendimiento sostenido, (2) consumo de batería, (3) interrupción del sistema operativo.
Ninguno aparece en el editor y ninguno es un error de lógica en sentido estricto: son supuestos de PC que el juego trae consigo. Esa es la idea de toda la unidad.
No dar todavía las explicaciones: anotarlas en el pizarrón para volver a ellas en las slides 10 a 15.

## 3 | Lo que ya vimos el 28/09
tipo: contenido
kicker: CONTINUIDAD [RECICLADO 28/09]
- Táctil sin botón físico
- Pantallas y zonas seguras
- Batería y temperatura
- Interrupciones del sistema
- Intención ≠ dispositivo
imagen: Miniaturas de las slides 8 (móvil) y 12 (intención vs. dispositivo) de la clase del 28/09.
fuente: Clase 28/09/2026 — Clase2-Plataformas.pptx
notas:
Recuperar, no repetir. Las cinco ideas del 28/09, completas:
- Táctil: no hay respuesta física del botón y los dedos tapan la pantalla.
- Pantallas muy variadas: muescas, bordes y zonas seguras.
- Batería y temperatura: si el equipo se calienta, baja el rendimiento.
- Interrupciones: llamadas, notificaciones, cambio de app.
- Separar QUÉ quiere hacer el jugador (mover, disparar) de CÓMO lo pide (teclado, toque, mando).
Preguntar quién recuerda el diagrama de tres capas (dispositivo → intención → nave). Hoy vamos a ver por qué cada viñeta es una restricción de diseño, con números y fuentes oficiales.

## 4 | Al terminar la unidad podrán
tipo: contenido
kicker: OBJETIVOS
- Explicar las restricciones del móvil
- Detectar supuestos de PC en un juego
- Diseñar controles táctiles medibles
- Defender un modelo de monetización
- Decidir qué probar y dónde
notas:
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
El artículo de Kevuru Games define las plataformas como "la base de cómo los jugadores se conectan con los juegos", ya sea una consola física, un gabinete arcade o un servicio en la nube que corre todo en línea. Y usa una metáfora útil: la plataforma es el escenario donde el juego "actúa", y hay escenarios más grandes que otros.
Pero el artículo mezcla bajo la palabra "plataforma" cuatro cosas distintas: hardware (PlayStation, Xbox, Nintendo), tiendas (Steam, Epic Games Store, Google Play, App Store), servicios de cloud gaming (GeForce Now) y sitios donde se mira jugar (Twitch, YouTube Gaming, Facebook Gaming). La tabla las separa en capas.
Definición de trabajo de esta materia: plataforma = el entorno de ejecución (hardware + sistema operativo) MÁS las reglas de su ecosistema (tienda, certificación, políticas). Por eso en esta unidad hablamos del teléfono y también de Google Play y del App Store.
Respuesta esperada a la pregunta: la capa de ejecución condiciona más el diseño (input, pantalla, rendimiento); la de distribución condiciona el negocio y las reglas (Clase 3); la de comunidad influye en el diseño solo de forma indirecta (juegos pensados para ser vistos, como Among Us).

## 6 | De los arcades al bolsillo
tipo: contenido
kicker: CONTEXTO HISTÓRICO
- Arcade: la primera plataforma (Pong, 1972)
- Consola doméstica y PC
- Portátiles: Game Boy
- Teléfono: el juego va en el bolsillo
- Hoy: XR y nube
imagen: Línea de tiempo: gabinete arcade → consola en la TV → PC → Game Boy → teléfono → visor XR / nube.
fuente: Kevuru Games (blog, consultado 2026-10-05); ejemplos históricos ampliamente documentados
notas:
[Diapositiva nueva en la versión 2.]
Idea del artículo: cada época tuvo una plataforma que definió cómo se juega. Los arcades fueron las primeras plataformas reales, y además eran espacios sociales.
Ejemplos que da el artículo, por si alguien pregunta: Pong (1972), Space Invaders (1978), Pac-Man (1980), Donkey Kong (1981, primera aparición de Mario como "Jumpman"), Galaga (1981), Street Fighter II (1991) y Mortal Kombat (1992), cuya polémica contribuyó a la creación de la ESRB (el sistema de clasificación por edades que vamos a ver en la Unidad V).
Conexión con el diseño: el arcade se diseñaba para cobrar por partida (partidas cortas y difíciles, "insert coin"); la consola, para el sillón y la TV; el teléfono, para el bolsillo y las interrupciones. La plataforma siempre moldeó el diseño: no es un fenómeno nuevo.
Dato a remarcar: Asteroids, el juego que inspira nuestro proyecto, es justamente un clásico arcade (Atari, 1979). Estamos llevando un diseño de arcade al teléfono.
No detenerse más de 3 minutos: es contexto, no contenido evaluable.

## 7 | Las tiendas cambiaron quién publica
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
Idea del artículo: con Google Play y el App Store, "los estudios pequeños e incluso desarrolladores solos" pudieron poner sus juegos frente a millones de personas. Los ejemplos que da:
- Éxitos casuales que atrajeron jugadores de todo el mundo: Candy Crush y Clash of Clans.
- Among Us se volvió viral años después de su lanzamiento (salió en 2018 y explotó en 2020).
- Marcas de consola que funcionan en el teléfono: PUBG Mobile y FIFA Mobile.
Conclusión del artículo: el juego móvil no es una moda pasajera, es una parte central de la industria.
Matiz docente (importante): que la tienda esté abierta no significa que no tenga reglas. Para publicar hay que cumplir políticas de pago, de anuncios, de privacidad y de nivel de API (lo vemos en la Clase 3). Y que cualquiera pueda publicar crea otro problema: la visibilidad entre millones de juegos.
Respuesta esperada a la pregunta: la visibilidad depende de la propia tienda (búsqueda, destacados, calificaciones), de la comunidad (streamers, boca en boca) y de la calidad técnica (Android vitals puede bajar la visibilidad de un juego con muchos cierres inesperados; lo vemos en la Clase 3).

## 8 | Adentro del teléfono
tipo: contenido
kicker: LA MÁQUINA
- CPU, GPU y memoria en un chip (SoC)
- Comparten energía y calor
- Núcleos y relojes variables
- Sin ventilador
imagen: Diagrama de bloques: SoC del teléfono (CPU+GPU+memoria juntos) vs. PC (CPU, GPU dedicada y RAM separadas, con ventiladores).
fuente: Android Developers — ADPF; Arm GPU Best Practices §2.3
notas:
En un teléfono, CPU, GPU y memoria viven en un mismo chip (SoC, System on a Chip). Comparten la energía de la batería y el calor que generan. El calor se disipa por la carcasa: no hay ventilador.
La documentación de Android (ADPF) menciona explícitamente la diversidad de topologías de núcleos (núcleos de distinto tamaño y potencia) y los relojes que cambian en tiempo real como complejidades propias del móvil, que no existen en PC ni en consola.
No dar arquitectura de hardware: alcanza con la idea de que todo comparte energía y calor.
Pregunta rápida: ¿qué pasa con la GPU si la CPU se calienta? Respuesta: comparten el presupuesto térmico; si uno se calienta, ambos pueden bajar su frecuencia.

## 9 | Dibujar dos veces cuesta más
tipo: contenido
kicker: LA MÁQUINA
- GPU por tiles (TBDR)
- Memoria = ancho de banda = batería
- Overdraw: el mismo píxel varias veces
- Partículas y transparencias pesan más
imagen: Pantalla dividida en tiles; en un tile, varias capas de partículas superpuestas sobre el mismo píxel.
fuente: Apple — Tailor your apps for Apple GPUs and TBDR; Arm GPU Best Practices §2.3, p. 15
notas:
Las GPU móviles dibujan la pantalla por porciones (tiles): técnica TBDR, tile-based deferred rendering. Leer y escribir memoria consume ancho de banda, y el ancho de banda consume batería.
Overdraw: pintar varias veces el mismo píxel, típico de transparencias y partículas. Por eso una explosión con muchas partículas pesa más en un teléfono que en una PC.
Citas de Arm para leer en voz alta: "Overdraw causes excess memory bandwidth use" y "Excess memory bandwidth use causes excess power use".
Llegar solo hasta acá: no explicar el pipeline de la GPU. Conectar con Asteroides: la explosión de la nave usa partículas con transparencia, candidata a medir en la Clase 4.

## 10 | Pico vs. sostenido
tipo: contenido
kicker: LA MÁQUINA · CONCEPTO CLAVE
- Calor → throttling → caen los fps
- Importa el minuto 10, no el 1
- Usar ~65 % del tiempo de frame
pregunta: ¿Cómo medirían que un juego es "estable"?
imagen: Gráfico de fps en el tiempo que cae a los 8 minutos, superpuesto a una curva de temperatura que sube.
video: WWDC19 sesión 422 (Apple), 19:40–31:00 — tarea
fuente: Unity e-book Optimize… mobile, XR and web (Unity 6), p. 19; Android Thermal API
notas:
Es el concepto más importante de la clase.
Cadena causal: el chip se calienta → el sistema baja la frecuencia de CPU y GPU para protegerlo (throttling) → caen los fps. Lo que importa es el fps del minuto 10, no el del minuto 1.
Recomendación de Unity: usar alrededor del 65 % del tiempo de frame disponible, es decir, ~22 ms a 30 fps y ~11 ms a 60 fps. Motivo oficial textual: "Most mobile devices do not have active cooling".
Respuesta esperada a la pregunta: medir durante un tiempo largo (10 minutos o más), registrar el frame time (no solo el promedio de fps) y hacerlo en un dispositivo de gama baja.
Para mencionar, sin profundizar: Android ofrece getThermalHeadroom e iOS ofrece thermalState para que el juego reaccione al calor; Unity 6.3 trae Adaptive Performance como módulo integrado.

## 11 | 30 fps no es un error
tipo: contenido
kicker: LA MÁQUINA · BATERÍA
- Unity móvil: 30 fps por defecto
- 60 fps = el doble de trabajo
- El fps es una decisión de diseño
fuente: Unity 6.3 Scripting API — Application.targetFrameRate; Android — Optimize power efficiency
notas:
En Android e iOS, por defecto Unity renderiza a 30 fps fijos "to conserve battery power" (texto de la documentación de Application.targetFrameRate: abrir la página y leer la frase).
60 fps duplica el trabajo por segundo: más calor y menos batería. Elegir el fps es una decisión de diseño, no un detalle técnico.
En Asteroides no se define targetFrameRate: nadie tomó la decisión (supuesto S12 del caso práctico).
Preguntar: ¿qué juegos necesitan 60 fps y cuáles no? Respuesta: acción rápida o competitiva sí; puzzle, estrategia o narrativa, generalmente no.
Android recomienda además igualar la frecuencia de refresco de la pantalla al fps objetivo (frame pacing).

## 12 | El sistema operativo manda
tipo: contenido
kicker: LA MÁQUINA · CICLO DE VIDA
- Salir de la app = segundo plano
- Sin memoria, el SO cierra procesos
- onTrimMemory no lo evita
- Diseño: guardar estado
imagen: Diagrama de estados: activa → segundo plano → terminada, con una llamada entrante como disparador.
fuente: Android — Low memory killers (2026-09-21); Apple — applicationDidReceiveMemoryWarning
notas:
Cuando el jugador sale de la app (llamada, notificación, cambio de app), el juego pasa a segundo plano. Si falta memoria, el sistema operativo cierra procesos en segundo plano: en Android lo hace el Low Memory Killer; en iOS, el sistema termina la app si no libera memoria.
Corrección de un mito frecuente: los callbacks onTrimMemory de Android NO evitan el cierre. Android los declara deprecados salvo dos niveles (UI_HIDDEN y BACKGROUND) y dice textualmente que "haven't been helpful at preventing low-memory kills".
Conclusión de diseño: el juego puede morir sin aviso. Si puede retomarse, hay que guardar estado; si no puede, al menos no castigar al jugador por algo que hizo el sistema.

## 13 | Qué hace Unity con eso
tipo: contenido
kicker: LA MÁQUINA · UNITY
- OnApplicationPause(bool)
- OnApplicationFocus(bool)
- Teclado en Android → pierde el foco
- Asteroides no los usa (S8)
fuente: Unity 6.3 Scripting API — MonoBehaviour.OnApplicationPause / OnApplicationFocus
notas:
OnApplicationPause(bool) avisa que la app pasa a segundo plano o vuelve. OnApplicationFocus(bool) avisa que la app pierde o recupera el foco. Dato práctico: en Android, abrir el teclado en pantalla dispara OnApplicationFocus(false).
Asteroides no implementa ninguno de los dos (supuesto S8 del caso práctico).
No escribir código todavía: eso se hace en la Clase 3 con el defecto deliberado. Solo mostrar que el motor avisa y que el juego base no escucha.
Anticipar: ¿alcanza con escuchar el aviso? No: si el sistema mata el proceso, no se llama nada.

## 14 | Actividad A4.1 — Diagnóstico
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
Consigna completa: para cada reporte, indicar (a) la restricción de plataforma más probable, (b) qué evidencia le pedirían al tester, y (c) qué tipo de prueba lo habría detectado antes.
Respuestas esperadas (detalle en 05, A4.1):
1. Ciclo de vida / Low Memory Killer → QA manual en dispositivo.
2. Térmica → rendimiento sostenido en dispositivo.
3. Safe area → Device Simulator + dispositivo.
4. Escalado de UI → Device Simulator con varios perfiles.
5. fps y energía → medición en dispositivo.
6. El emulador no representa el rendimiento → Profiler en un teléfono de gama baja.
Error típico a corregir: proponer un unit test para los casos 2, 3 o 5. Recordar pedir siempre el modelo del dispositivo.

## 15 | Demo: el simulador y sus límites
tipo: demo
kicker: DEMO EN VIVO
- Player Settings de Android
- Device Simulator: qué simula
- Y qué NO simula
- Asteroides en vertical
imagen: Device Simulator con Asteroides en vertical y los asteroides apareciendo fuera de pantalla.
fuente: Unity 6.3 Manual — Device Simulator introduction; Android Player settings
notas:
Pasos de la demo:
1. Player Settings de Android: Application Category = Game (por defecto en Unity 6.3; exime a los juegos del cambio de Android 16 que ignora la orientación en pantallas grandes), orientación y API mínima.
2. Abrir la página oficial del Device Simulator y leer la lista de lo que NO simula ANTES de usarlo: rendimiento, memoria, capacidades de render y giroscopio. La herramienta llega con sus límites.
3. Lo que sí simula: safe area, rotación y toque de un dedo.
4. Poner Asteroides en un perfil de teléfono en vertical. Confirmar en vivo el supuesto de que la cámara está centrada en x = 0.
No revelar todavía el problema del spawn: lo descubren en A4.2.

## 16 | Actividad A4.2 — Supuestos de PC
tipo: actividad
kicker: ACTIVIDAD · 20 MIN · GRUPOS
- Ship.cs 61–73: el control
- Ship.cs 46–47 y 99–115: los límites
- Spawner.cs 101–106: el spawn
- Prefab Game: Canvas y cámara
actividad: 5 supuestos: dónde (archivo:línea), qué pasaría, qué eje.
imagen: Fragmento de Ship.cs 61–73 con las tres llamadas a Input.GetKey resaltadas.
notas:
Consigna completa: listar al menos 5 supuestos que dejan de valer en un teléfono, indicando dónde están (archivo:línea), qué pasaría en móvil y a qué eje pertenecen (input, pantalla, UI, ciclo de vida, rendimiento).
La respuesta completa es la tabla S1–S13 de 02-caso-practico. Para aprobar alcanza con S1 (teclado), S3/S4/S5 (límites, cámara, spawn), S6 (Canvas en Constant Pixel Size) y S8 (sin pausa).
Pista si se traban: "¿qué pasa con la cámara si la pantalla es más angosta que alta?".

## 17 | Lo que encontramos
tipo: contenido
kicker: PUESTA EN COMÚN
- Vista: 5 × aspect a cada lado
- 16:9 → ≈ 8,9 · vertical → ≈ 2,8
- Spawn en x ∈ [−8, 8]
- En vertical, nacen fuera de pantalla
imagen: Dos capturas lado a lado, 16:9 y 9:16, con el rango de spawn [−8, 8] marcado sobre cada una.
fuente: Código del proyecto (Spawner.cs:101-106; prefab Game, Camera)
notas:
La cámara es ortográfica de tamaño 5: el semiancho visible es 5 × aspect. A 16:9 se ven ≈ 8,9 unidades a cada lado; en vertical 9:16, ≈ 2,8.
El Spawner crea asteroides en x ∈ [−8, 8] (coordenadas de mundo). En vertical, la mayoría de los asteroides nace fuera de pantalla.
No hay error de lógica: hay un supuesto de plataforma. Ningún archivo tiene un error por sí solo; el problema aparece en la combinación cámara + spawner + orientación.
Mostrarlo en el Device Simulator. Conectar con el testing de integración de la U3: es un defecto de integración con la plataforma.

## 18 | ¿Cómo se elige una plataforma?
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
El artículo de Kevuru propone cuatro consideraciones para elegir plataforma, y concluye que el desafío no es encontrar la "mejor" plataforma, sino la que encaja con la visión del juego y su público:
1. Audiencia: saber para quién se construye. Un puzzle casual puede encontrar su público en móvil; un RPG con mucha narrativa puede funcionar mejor en consola o PC.
2. Modelos de monetización: suscripción, free-to-play con compras integradas o venta premium. Cada plataforma se inclina por estrategias distintas y el modelo de ingresos tiene que coincidir.
3. Integración y soporte: algunas plataformas ofrecen mejores herramientas, documentación o ayuda directa; una buena integración ahorra meses.
4. Vigencia (future-proofing): preferir plataformas que sigan evolucionando para que el juego no quede desactualizado en uno o dos años.
Lo que agrega la cátedra: un quinto criterio, las restricciones técnicas y de diseño de la plataforma (todo lo que vimos hoy: calor, batería, memoria, interrupciones, pantalla). El artículo no lo menciona y es justamente el núcleo de esta materia.
Respuesta esperada a la pregunta: Asteroides encaja en móvil por audiencia (partidas cortas y casuales) y por sus requisitos técnicos bajos, pero exige rediseñar el control, la pantalla y la pausa (lo que encontramos en A4.2). La monetización se decide en la Clase 3.

## 19 | Leer con lupa
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
El artículo que usamos para las slides 5, 6, 7 y 18 es útil para los conceptos, pero tiene problemas que conviene mostrar:
1. Es el blog de un estudio de desarrollo (Kevuru Games) que termina ofreciendo sus servicios y un formulario de cotización: es una fuente comercial, no una autoridad.
2. Presenta Google Stadia como un servicio activo. Google anunció el cierre el 29/09/2022 y fue efectivo el 18/01/2023, con reembolsos (verificado en la investigación de la Unidad VII, fuente oficial de Google).
3. Nombra la tienda "Origin" entre las plataformas de PC. EA anunció el 06/10/2022 que la EA app la reemplaza como su plataforma principal de PC (fuente oficial de EA).
4. Da cifras de ingresos y usuarios proyectadas desde 2023 (por ejemplo, ingresos del sector y cantidad de usuarios a 2027) sin citar de dónde salen. No las usamos en clase.
5. Mezcla bajo "plataforma" hardware, tiendas, cloud y sitios de streaming (lo ordenamos en la slide 5).
Mensaje para los alumnos: el mismo criterio que aplicamos a los tests (¿qué demuestra y qué no?) se aplica a las fuentes. Un blog sirve para ideas; los datos se verifican en la documentación oficial o en papers. Es el mismo criterio que van a usar en el TP 3.

## 20 | Qué no resuelve esto · TP 3
tipo: cierre
kicker: CIERRE
- El simulador no mide calor ni batería
- Eso se mide en su teléfono (Clase 4)
- TP 3: Dossier Asteroides móvil
- Tarea: Build Support + depuración USB
fuente: Unity 6.3 Manual — Android environment setup; Android — Configure on-device developer options
notas:
Cerrar con el límite de la herramienta, no con la herramienta: el simulador encontró el problema de la pantalla, pero no mide calor ni batería. Eso lo vamos a medir en sus teléfonos, en la Clase 4.
TP 3: Dossier de plataforma, Asteroides móvil (consigna en el aula virtual).
Tarea técnica obligatoria (sin ella la Clase 4 no se puede hacer):
1. Instalar el módulo Android Build Support (con OpenJDK, Android SDK y NDK) en Unity 6000.3.11f1 desde Unity Hub.
2. En el teléfono: tocar 7 veces "Número de compilación" para habilitar las Opciones de desarrollador y activar "Depuración USB" (en Android 9 o superior: Ajustes > Sistema > Avanzado > Opciones de desarrollador).

# DECK 2 | Diseñar para el pulgar | Unidad IV · Clase 2

## 1 | Diseñar para el pulgar
tipo: portada
kicker: UNIDAD IV · CLASE 2 DE 4
- UI táctil, pantallas y accesibilidad
- Diseño según Plataformas de Juego · FI – UNJu · 2026
imagen: Mano sosteniendo un teléfono, con el arco de alcance del pulgar dibujado.
notas:
Recordar de dónde venimos: la Clase 1 fue la máquina. Hoy: las manos y la pantalla.

## 2 | ¿Cuánto mide un dedo?
tipo: contenido
kicker: APERTURA
- El score de Asteroides queda bajo la cámara frontal
- El botón de inicio, diseñado para un mouse, es diminuto
- Y el pulgar tapa justo la zona por donde caen los asteroides
pregunta: ¿Qué tamaño mínimo debería tener un botón para un dedo? ¿Cómo lo sabríamos?
imagen: HUD de Asteroides en un teléfono con notch: score tapado y botón de inicio diminuto.
notas:
Dejar que propongan números en píxeles y mostrar que la respuesta en píxeles no sirve (la siguiente slide). Recuperar el supuesto S6 de la Clase 1.

## 3 | Hay mínimos oficiales
tipo: contenido
kicker: UI TÁCTIL
| Plataforma | Tamaño mínimo de objetivo táctil | Fuente |
| iOS (Apple HIG) | 44 × 44 pt (mínimo absoluto 28 × 28 pt) | HIG Buttons / Accessibility |
| Android | 48 × 48 dp — "Larger is even better" | Android Developers — accessibility |
| visionOS (referencia) | 60 × 60 pt | HIG Buttons |
- Separar los controles: ~12 pt con borde visible, ~24 pt sin borde (HIG)
fuente: Apple HIG — Buttons, Accessibility; Android — Make apps more accessible
notas:
Son números verificables: convierten "botón cómodo" en un criterio de prueba. Las unidades no son píxeles (siguiente slide). Comentar que Apple también fija texto de 17 pt por defecto y 11 pt mínimo para juegos en iOS (HIG Designing for games).

## 4 | pt, dp, px
tipo: contenido
kicker: UI TÁCTIL · DENSIDAD
- px: puntos físicos de la pantalla; cambian de un teléfono a otro
- pt (Apple) y dp (Android): unidades independientes de la densidad
- El mismo botón de 100 px es grande en un teléfono viejo y diminuto en uno de alta densidad
- En Unity: el Canvas Scaler decide cómo escala la UI (Asteroides usa Constant Pixel Size)
imagen: El mismo botón de 100 px dibujado en dos teléfonos de distinta densidad, uno grande y uno chico.
fuente: Unity uGUI 2.0 — Canvas Scaler; Designing UI for Multiple Resolutions
notas:
No hace falta la fórmula de conversión. La idea: diseñar en unidades independientes de la densidad y dejar que el motor escale. Modos del Canvas Scaler: Constant Pixel Size, Scale With Screen Size, Constant Physical Size.

## 5 | No todo el rectángulo es tuyo
tipo: contenido
kicker: UI TÁCTIL · SAFE AREA
- Muescas, cámaras perforadas, bordes curvos, barras de gestos
- Screen.safeArea: el rectángulo donde la UI está a salvo (en píxeles)
- Android 15 con target SDK 35: el contenido va de borde a borde, obligatoriamente
- La UI esencial va dentro de la safe area; el fondo puede salir de ella
imagen: Teléfono con notch y barra de gestos, con la safe area sombreada en verde.
fuente: Unity 6.3 — Screen.safeArea; Android — Support display cutouts
notas:
Dato: en Android 15+, Unity ignora la opción "Render Outside Safe Area" porque el sistema impone edge-to-edge. Por eso hay que leer safeArea y no confiar en que el sistema deje márgenes. Android permite simular un cutout desde las opciones de desarrollador: útil en la Clase 4.

## 6 | Dónde llega el pulgar
tipo: contenido
kicker: ERGONOMÍA [RECICLADO 28/09]
- Observación de Hoober (2013, 1.333 personas): 49 % una mano, 36 % acunado, 15 % dos manos
- Los jugadores cambian de agarre todo el tiempo
- Advertencia: dato de 2013, con teléfonos más chicos que los actuales
- CoD Mobile y Fortnite permiten mover y redimensionar los controles del HUD
pregunta: En Asteroides, ¿qué zona de la pantalla tapa el pulgar que dispara?
imagen: HUD táctil con las zonas de los pulgares superpuestas en semitransparente.
fuente: Hoober, UXmatters 2013 (profesional); Activision blog CoD Mobile 2019; Epic — Fortnite mobile development
notas:
Hoober es una fuente profesional, no académica, y tiene más de una década: decirlo. Sirve como disparador, no como norma. El HUD editable es una respuesta de diseño a la diversidad de manos y de teléfonos.

## 7 | Vertical u horizontal
tipo: contenido
kicker: PANTALLA · ORIENTACIÓN
- Cambiar la orientación cambia el campo de juego (S4/S5 de la Clase 1)
- Asteroides arranca en AutoRotation: gira solo si el jugador gira el teléfono
- Android 16 ignora las restricciones de orientación en pantallas grandes… salvo en juegos
- Unity 6.3 marca Application Category = Game por defecto
pregunta: ¿Asteroides es un juego vertical o horizontal? Justifiquen.
imagen: El mismo nivel de Asteroides en vertical y en horizontal, con el área visible marcada.
fuente: Android 16 behavior changes; Unity 6.3 Android Player settings; Screen.orientation
notas:
No hay una respuesta correcta única: vertical favorece una mano; horizontal favorece el campo de visión y dos pulgares. Lo que se evalúa es que la decisión considere sus consecuencias (rango de spawn, límites, HUD).

## 8 | Gestos
tipo: contenido
kicker: INTERACCIÓN
- Gestos estándar: tocar, deslizar, arrastrar, mantener, pellizcar
- No redefinir los gestos del sistema (volver, inicio, notificaciones)
- Un gesto inventado nunca debe ser la única forma de hacer algo importante
- Las apps no deberían depender de gestos para funciones básicas (Android)
imagen: Íconos de los cinco gestos estándar.
fuente: Apple HIG — Gestures; Android — accessibility
notas:
Relacionar con descubribilidad: si un gesto no se ve, el jugador no lo encuentra. Por eso los gestos custom se acompañan de una alternativa visible.

## 9 | Sin botón físico
tipo: contenido
kicker: INTERACCIÓN · TÁCTIL
- Joystick virtual: familiar, pero sin tope físico y tapa la pantalla
- Toque directo o arrastre: preciso, pero el dedo cubre lo que se toca
- Un dedo: Alto's Adventure juega con un solo toque
- Háptica: complementaria, consistente y desactivable ("menos es más")
video: Zach Gage — "Controls You Can Feel" (GDC 2012, GDC Vault, gratuito). Fragmento a definir por la docente
fuente: Apple HIG — Playing haptics; Android — Haptics design principles; App Store — Alto's Adventure
notas:
Recomendación de Android sobre háptica: entre una vibración molesta y ninguna, elegir ninguna. Que la háptica sea siempre opcional es también accesibilidad.

## 10 | Accesibilidad móvil
tipo: contenido
kicker: ACCESIBILIDAD
- Controles grandes y bien separados
- Alternativa a cada gesto
- Háptica y efectos de pantalla desactivables
- Evitar la repetición rápida de toques (button mashing)
- Texto legible: 17 pt por defecto, 11 pt mínimo en iOS
fuente: Game Accessibility Guidelines (nivel básico); Apple HIG — Accessibility, Designing for games
notas:
Accesible no es un extra: amplía quiénes pueden jugar y mejora la experiencia de todos (jugar con una mano en el colectivo es una discapacidad situacional). Estos puntos van al checklist del TP 3.

## 11 | La primera sesión
tipo: contenido
kicker: ONBOARDING
- Que se pueda jugar apenas termina la instalación
- Descarga inicial corta (Apple sugiere 30 minutos o menos)
- Enseñar jugando, no con pantallas de texto
- Pedir permisos en el momento en que se necesitan
fuente: Apple HIG — Designing for games; Apple GameKit — juegos con descargas grandes
notas:
Tema importante pero no imprescindible: no profundizar en Play Asset Delivery; solo la idea de que el tamaño de descarga define qué entra en la primera sesión.

## 12 | Demo: escalar la UI
tipo: demo
kicker: DEMO EN VIVO
- Canvas del prefab Game: Constant Pixel Size, referencia 800 × 600
- Cambiar a Scale With Screen Size y elegir una resolución de referencia
- Comparar en el Device Simulator con dos teléfonos y una tablet
- Leer Screen.safeArea y ver dónde cae el score
video: Unity — "Input System in Unity 6 (3/7): Input System Mobile controls" (opcional, de tarea)
fuente: Unity uGUI 2.0 — Canvas Scaler; Unity 6.3 — Screen.safeArea
notas:
Hacerlo en una copia o rama del proyecto. Mostrar el antes y el después. Remarcar el orden: primero apareció el problema (slide 2), ahora la herramienta.

## 13 | Actividad A4.3 — Dos esquemas de control
tipo: actividad
kicker: ACTIVIDAD · 25 MIN · GRUPOS
- Diseñen dos esquemas: por ejemplo, joystick virtual + botón vs. arrastrar + autodisparo
- Boceto sobre una pantalla de teléfono con la safe area marcada
- Medidas en pt/dp y orientación elegida
- Comparación: oclusión, precisión, una mano, accesibilidad, descubribilidad
actividad: Elijan uno y justifíquenlo con al menos dos fuentes de la clase.
imagen: Plantilla de pantalla de teléfono vacía, con la safe area marcada.
notas:
Buena respuesta: decide la orientación sabiendo su efecto sobre el spawn, respeta 44 pt / 48 dp, no pone controles bajo el notch, reconoce que el autodisparo cambia el game design (baja la habilidad requerida, cambia el balance) y ofrece una alternativa accesible.

## 14 | Probalo con tu mano · A4.6
tipo: actividad
kicker: PLAYTEST DE PAPEL · 15 MIN + A4.6 · 15 MIN
- Dibujen su HUD a escala sobre la silueta de su propio teléfono
- Sostengan el teléfono: ¿llegan a todo? ¿Qué tapa el pulgar?
- A4.6: "60 fps al empezar, 35–40 fps a los 8 minutos; en el editor, 200 fps"
pregunta: ¿Cuello de botella, métrica, herramienta, estrategia? ¿Qué herramienta NO sirve?
notas:
El playtest de papel es barato y se hace con personas reales: la comodidad no se prueba en el editor. A4.6, respuesta esperada: throttling térmico agravado por overdraw de partículas; medir frame time en el tiempo y estado térmico con el Profiler en el dispositivo; fijar 30 fps o un presupuesto del 65 % y reducir el overdraw. El editor y el Device Simulator no sirven para esto. Cierre de la clase: un buen layout no garantiza comodidad, eso lo dicen las personas. Verificar quién ya tiene la depuración USB funcionando.

# DECK 3 | El negocio y la prueba | Unidad IV · Clase 3

## 1 | El negocio y la prueba
tipo: portada
kicker: UNIDAD IV · CLASE 3 DE 4
- Monetización como decisión de diseño · Testing en móvil
- Diseño según Plataformas de Juego · FI – UNJu · 2026
notas:
Hoy cambiamos de restricción: ya no es el hardware ni la mano, son las reglas de la tienda y cómo probamos lo que diseñamos.

## 2 | USD 520 millones por una pantalla de compra
tipo: contenido
kicker: APERTURA
- 2022: la FTC (EE. UU.) acusó a Epic Games por Fortnite
- USD 275 millones por privacidad de menores (COPPA) + USD 245 millones en reembolsos
- Motivo: "dark patterns" en la compra; botones "counterintuitive, inconsistent, and confusing"
pregunta: ¿Monetizar es una decisión de negocio o de diseño?
imagen: Titular del comunicado oficial de la FTC del 19/12/2022.
fuente: FTC, comunicado de prensa del 19/12/2022
notas:
Respuesta buscada: las dos cosas. Una decisión de interfaz (dónde va un botón, qué confirma una compra) tuvo consecuencias legales. Desde hoy la monetización se analiza como diseño con reglas y con ética.

## 3 | Cuatro modelos
tipo: contenido
kicker: MONETIZACIÓN
| Modelo | Quién paga y cuándo | Qué cambia en el diseño |
| Premium | Al comprar, una vez | Sin interrupciones; menor alcance (Alto’s Adventure: pago único, sin ads ni IAP) |
| Freemium + IAP | Algunos jugadores, dentro del juego | Progresión y tienda interna pensadas para vender |
| Con anuncios | El anunciante; el jugador "paga" con tiempo | Hay que decidir en qué momento interrumpir |
| Híbrido | Combinación (ads + "quitar anuncios") | Todas las anteriores a la vez |
fuente: App Store — Alto’s Adventure (ficha consultada 2026-10-04)
notas:
Agregar el modelo premium es una corrección al programa, que solo nombra freemium e híbridos. Ninguno es "el bueno": cada uno cambia el juego de distinta manera.

## 4 | Tres formatos de anuncio
tipo: contenido
kicker: MONETIZACIÓN · ADS
| Formato | Cómo funciona | Regla clave |
| Rewarded | El jugador elige verlo a cambio de una recompensa | "served after a user explicitly chooses to view" (AdMob) |
| Interstitial | Pantalla completa entre momentos del juego | Solo en transiciones naturales |
| Banner | Franja fija en pantalla | Ocupa espacio de la UI y de la safe area |
imagen: Tres mockups de pantalla de Asteroides, uno con cada formato.
fuente: Google AdMob — Rewarded ads; Interstitial ad guidance
notas:
Remarcar la diferencia de consentimiento: el rewarded lo pide el jugador, el interstitial se lo imponen. Eso cambia la experiencia y, como vamos a ver, también las reglas.

## 5 | Lo que AdMob prohíbe
tipo: contenido
kicker: MONETIZACIÓN · REGLAS EXTERNAS
- Interstitials al abrir o al salir de la app
- Un interstitial después de cada acción (como máximo, uno cada dos acciones)
- Un interstitial inmediatamente después de otro
- Interstitials inesperados mientras el usuario está jugando
pregunta: ¿Un anuncio en cada Game Over de Asteroides cumple estas reglas?
fuente: Google AdMob — Disallowed interstitial implementations
notas:
Discutir la pregunta: si cada partida es corta y cada Game Over muestra un anuncio, se acerca a "después de cada acción". No hay respuesta automática: hay que leer la política y justificar. Dato de herramienta: Unity recomienda migrar de Unity Ads directo a LevelPlay (mediación) desde abril de 2026; no se integra en esta materia.

## 6 | La tienda pone las reglas
tipo: contenido
kicker: MONETIZACIÓN · REGLAS EXTERNAS
- Apple 3.1.1: para desbloquear contenido digital se debe usar la compra integrada (IAP)
- Apple y Google: las cajas con premios al azar deben mostrar las probabilidades antes de comprar
- Google Play Billing es obligatorio (con excepciones por país)
- Apps para niños: sin publicidad personalizada ni SDKs no certificados
fuente: Apple App Review Guidelines 3.1.1 y 1.3; Google Play — Payments policy y Families policy
notas:
IAP no es una estrategia libre: la tienda la impone y la regula. Por eso el diseño de la tienda interna empieza leyendo estas políticas.

## 7 | Monetizar cambia el juego
tipo: contenido
kicker: MONETIZACIÓN = GAME DESIGN
- "Continuar con un anuncio" cambia el significado del Game Over
- Subir la dificultad para vender vidas cambia el balance
- Las pausas para anuncios cambian el ritmo de la sesión
- Vampire Survivors en móvil: monetización "designed to never interrupt your game, always be optional"
pregunta: Si Asteroides ofrece "continuar" con un rewarded, ¿qué parámetros del juego habría que rebalancear?
fuente: Kotaku (2023), citando a poncle
notas:
Respuesta posible: la cantidad de vidas, la velocidad de los asteroides y la duración de la partida; además, cómo se calcula el puntaje si alguien continúa. Es el puente entre economía y game design.

## 8 | El lado oscuro
tipo: contenido
kicker: ÉTICA
- Dark patterns: diseños que juegan en contra del interés del jugador (Zagal, Björk y Lewis, 2013)
- Loot boxes: asociadas con el juego problemático (Zendle y Cairns, 2018, n = 7.422); es una correlación, no una causa demostrada
- 35 técnicas de monetización percibidas como predatorias (Petrovskaya y Zendle, 2022)
- Regulación: Bélgica prohibió mecánicas de loot box en 2018
video: "Dark Patterns: How Good UX Can Be Bad UX", Anisa Sanusi, GDC 2017 (GDC Vault, gratuito). Fragmento a definir
fuente: PLOS ONE 2018; Journal of Business Ethics 2022; UK Gambling Commission (enfoques internacionales)
notas:
Cuidar la precisión: no decir que las loot boxes "causan" adicción; la evidencia citable es correlacional. Zagal et al. se cita sin enlace hasta verificar una copia legal (pendiente en el status).

## 9 | Actividad A4.5: ¿cuál publicarían?
tipo: actividad
kicker: ACTIVIDAD · 25 MIN · GRUPOS + DEBATE
| Propuesta | Modelo |
| P1 | Premium, US$ 2,99, sin anuncios ni compras |
| P2 | Gratis, rewarded "continuar con 1 vida" (una vez por partida) + IAP "quitar anuncios" |
| P3 | Gratis, interstitial al abrir y en cada Game Over + cofres pagos al azar sin probabilidades + dificultad aumentada |
actividad: Para cada una: ¿cumple las políticas? ¿Qué cambia en el diseño? ¿Qué riesgos éticos tiene? Elijan una y defiéndanla.
notas:
P3 viola políticas (interstitial al abrir; probabilidades no informadas) y manipula la dificultad. P2 cumple, pero cambia el balance. P1 es viable con menor alcance. Vale cualquier elección defendida con criterios y fuentes.

## 10 | ¿Qué prueba cada herramienta?
tipo: contenido
kicker: TESTING EN MÓVIL
| Nivel | Prueba | No prueba |
| 1. Device Simulator | Layout, safe area, rotación | Rendimiento, memoria, render |
| 2. Emulador | Lógica y flujos funcionales | Rendimiento real, térmica, GPU del teléfono |
| 3. Teléfono + Profiler | Rendimiento real, GC, frame time | Otros modelos de teléfono |
| 4. Tests en el Player | Tests automáticos en el dispositivo | Lo que no está escrito como test |
| 5. Granjas en la nube | Muchos modelos (Firebase Test Lab, AWS Device Farm) | Ergonomía, comodidad |
| 6. Android vitals | Fallas reales después de publicar | Nada antes de publicar |
fuente: Unity 6.3 — Device Simulator, Run tests in a Player, Profiling on target; Firebase Game Loop; AWS Device Farm; Android vitals
notas:
Es la escalera que conecta con la U3: cada nivel tiene un "qué no prueba". Android vitals mide fallas como la tasa de cierres inesperados (umbral general 1,09 %) y de ANR (0,47 %); la memoria pasa a afectar la visibilidad en la tienda desde febrero de 2027.

## 11 | La plataforma se mueve
tipo: contenido
kicker: DISTRIBUCIÓN
- Google Play exige AAB y, desde el 31/08/2026, apuntar a Android 16 (API 36)
- Unity 6.3 soporta Android 7.1 (API 25) o superior
- iOS: Unity genera un proyecto de Xcode, y Xcode solo corre en macOS
- En la cátedra no hay Mac: iOS se estudia de forma conceptual
fuente: Android — target API level requirement; Unity 6.3 — Android/iOS requirements y build process
notas:
Las reglas de tienda cambian todos los años: un juego publicado en 2025 puede necesitar cambios en 2026 sin que nadie toque el diseño. Decir explícitamente el límite del curso con iOS; no esconderlo.

## 12 | Demo: el test de pausa en rojo
tipo: demo
kicker: DEMO EN VIVO
- Versión de Asteroides con un sistema de pausa defectuoso: al volver, reanuda solo
- Test de Edit Mode sobre la regla de pausa: rojo
- Test de Play Mode sobre el adaptador: rojo
- La pestaña Player del Test Runner la usamos en la Clase 4, en el teléfono
fuente: Unity 6.3 — Unity Test Framework (Edit/Play mode; Run Play mode tests in a Player)
notas:
Requiere tener en el repositorio la versión con el defecto (tarea del status). Mostrar el rojo y no corregir: lo corrigen los grupos. Recordar el ciclo de la U3: rojo, corrección, verde, regresión.

## 13 | Actividad A4.4: la llamada que mata la nave
tipo: actividad
kicker: ACTIVIDAD · 25 MIN · GRUPOS
- Escriban el comportamiento esperado ante una interrupción, como criterio verificable
- Separen la regla (C# puro) del adaptador (MonoBehaviour que recibe OnApplicationPause)
- Escriban el test de Edit Mode de la regla
- Completen: ¿qué NO demuestra este test?
actividad: El test de Play Mode y la corrección se terminan en el TP 3; el QA manual, en la Clase 4 con sus teléfonos.
imagen: Diagrama: sistema operativo → adaptador (MonoBehaviour) → regla de pausa (C# puro) → estado del juego.
notas:
Respuesta esperada de "qué no demuestra": que el sistema operativo llame al callback cuando corresponde; qué pasa si el sistema mata el proceso (no se llama nada); el caso del teclado en pantalla en Android. Cierre: lo que el test no demuestra lo probamos la próxima clase en el teléfono.

# DECK 4 | Asteroides en tu bolsillo | Unidad IV · Clase 4

## 1 | Asteroides en tu bolsillo
tipo: portada
kicker: UNIDAD IV · CLASE 4 DE 4 · PRÁCTICA EN DISPOSITIVO
- Build, medición y QA manual en sus teléfonos Android
- Diseño según Plataformas de Juego · FI – UNJu · 2026
notas:
Clase 100 % práctica. Antes de empezar, verificar cables, depuración USB y Android Build Support instalado.

## 2 | ¿Qué no sabemos todavía?
tipo: contenido
kicker: APERTURA
- Todo lo que probamos fue en el editor
- La columna "qué no demuestra" de A4.4 sigue abierta
- Hoy: ¿cómo se comporta el juego en un teléfono real?
pregunta: ¿Qué esperan que cambie entre el editor y su teléfono?
imagen: Editor de Unity a la izquierda, teléfono a la derecha, un signo de pregunta entre ambos.
notas:
Que anoten su predicción: sirve para contrastar al final de la clase.

## 3 | De la PC al teléfono
tipo: demo
kicker: DEMO EN VIVO + GRUPOS · 20 MIN
- Build Profiles, Android: Development Build + Autoconnect Profiler
- Conectar el teléfono por USB con la depuración activada
- Build and Run: se instala y se abre en el teléfono
- Primero lo hace la docente; después cada grupo con el teléfono de un integrante
imagen: Ventana de Build Profiles de Android con Development Build y Autoconnect Profiler marcados.
fuente: Unity 6.3 — Build your application for Android; Collect performance data on a target platform
notas:
La primera build tarda: prever ese tiempo. Si un teléfono no aparece, revisar el cable (de datos, no solo de carga) y aceptar el diálogo de depuración en el teléfono.

## 4 | Plan B
tipo: contenido
kicker: GESTIÓN DE RIESGO
- Si la build falla en la máquina del grupo: instalar el APK de la docente
- Se pierde: el Profiler conectado
- No se pierde: el QA manual de interrupciones ni la matriz de compatibilidad
- Lo que no se pudo medir se declara en el dossier
notas:
Normalizar el plan B: en la industria también fallan las builds. Lo importante es documentar qué quedó sin medir.

## 5 | Medir, no opinar
tipo: actividad
kicker: MEDICIÓN · 20 MIN
- H1: ¿cada disparo (Instantiate del láser) genera picos de GC? Métrica: GC Alloc por frame
- H2: ¿el juego sostiene el fps durante 10 minutos? Métrica: frame time a lo largo del tiempo
- Registren modelo de teléfono, versión de Android y temperatura percibida
actividad: Capturen el Profiler y anoten los valores para el dossier.
imagen: Profiler conectado a un teléfono, con un pico de GC marcado en la línea de tiempo.
fuente: Unity 6.3 — Profiling on a target device; e-book Unity 6, p. 11
notas:
Advertencia honesta: Asteroides es liviano y lo más probable es que ande bien en casi cualquier teléfono. Si la medición no muestra problemas, la respuesta correcta es decirlo con los datos. El objetivo es aprender a formular y medir hipótesis.

## 6 | Editor vs. teléfono
tipo: actividad
kicker: COMPARAR
| Medición | Editor (PC) | Teléfono |
| fps promedio | | |
| Frame time máximo | | |
| GC Alloc por disparo | | |
| fps a los 10 minutos | | |
actividad: Completen la tabla con sus mediciones.
notas:
Conclusión esperada: el número del editor no predice el del teléfono. Retomar el caso A4.6 de la Clase 2 (200 fps en el editor).

## 7 | Interrumpir a propósito
tipo: actividad
kicker: QA MANUAL · 20 MIN
| Caso | Acción | Resultado esperado | Resultado real |
| QA-01 | Llamada o alarma durante la partida | El juego se pausa y espera un toque | |
| QA-02 | Botón de inicio y volver | Pausado, sin daño a la nave | |
| QA-03 | Bloquear y desbloquear la pantalla | Pausado | |
| QA-04 | Abrir el teclado en pantalla (si aplica) | Documentar qué pasa | |
| QA-05 | Cierre forzado y reabrir | Documentar qué se pierde | |
fuente: Unity 6.3 — OnApplicationPause / OnApplicationFocus; Android — activity lifecycle
notas:
Mismo formato de caso de prueba de la U2 (esperado vs. real). Si los grupos todavía no corrigieron el defecto, probar la versión con defecto: el resultado real va a contradecir al esperado, y eso es un hallazgo.

## 8 | Lo que el test automático no vio
tipo: contenido
kicker: LÍMITES
- ¿Coinciden los tests del editor (A4.4) con el QA manual?
- ¿Apareció algo solo en el teléfono?
- ¿Qué caso no se puede automatizar en esta materia?
pregunta: ¿Qué parte de la pausa protegen los tests y qué parte solo protege el QA manual?
notas:
Respuesta esperada: los tests protegen la regla y el adaptador ante regresiones; el QA manual comprueba que el sistema operativo dispare los callbacks y qué pasa cuando se cierra el proceso. Es la frontera entre automatización y hardware real, la misma de la U3 aplicada a la plataforma.

## 9 | La matriz del curso
tipo: actividad
kicker: COMPATIBILIDAD · 15 MIN
| Grupo | Modelo | Android | RAM | Resolución | fps medido | ¿Asteroides visibles en vertical? |
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
pregunta: ¿Alcanzan nuestros teléfonos para afirmar "anda en Android"?
fuente: Unity e-book (probar en gama mínima y máxima, p. 20); Android vitals
notas:
Respuesta esperada: no. Es una muestra de conveniencia que no representa al mercado; faltan gamas, fabricantes, versiones de Android y tablets. Por eso existen las granjas de dispositivos y Android vitals. Igual es evidencia real y vale más que el editor.

## 10 | Defensa del TP 3
tipo: actividad
kicker: DEFENSA · 3 MIN POR GRUPO · COEVALUACIÓN
- Una decisión de plataforma: contexto, opciones, decisión, consecuencias
- La evidencia del teléfono que la respalda (o la contradice)
- Lo que quedó sin probar, dicho explícitamente
| Criterio de coevaluación | Sí / En parte / No |
| La decisión está justificada | |
| Hay evidencia del dispositivo | |
| Se declaran los límites | |
notas:
Los criterios de coevaluación son una versión reducida de la rúbrica del TP 3 (ver 05). La entrega final del dossier se sube al aula virtual.

## 11 | En móvil, el límite lo pone el dispositivo
tipo: cierre
kicker: CIERRE DE UNIDAD · PUENTE A UNIDAD V
- Móvil: energía, calor, memoria, pantalla táctil, interrupciones y reglas de tienda
- Lo que el editor no muestra, lo muestra el teléfono
- Próxima unidad, consolas: el límite lo pone el fabricante
pregunta: Si Asteroides fuera a una consola, ¿quién decidiría si está listo para publicarse?
imagen: Un teléfono que se transforma en un gamepad frente a una TV.
notas:
Pregunta puente: en consola, el fabricante certifica el juego antes de publicarlo (Microsoft publica sus requisitos; Sony y Nintendo, no). Idea transversal de las unidades IV a VII: ¿quién pone el límite?
