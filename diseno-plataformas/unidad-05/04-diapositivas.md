# Unidad 5 — Diapositivas (texto + notas del docente)

Fuente única de las diapositivas de la Unidad 5, tema "Diseño según plataforma: consolas". Contenido desarrollado en `01-desarrollo-tema-consolas.md`; datos y fuentes en `datos/`.

Generar desde `diseno-plataformas/unidad-05/`:
1. `python scripts/graficos_consolas.py --slides` (gráficos sin título, en `imagenes/slides/`; requiere `matplotlib`).
2. `python scripts/build_decks.py` → `Unidad-5-2026-completa.pptx`. Con `--version N` se genera `-vN` sin pisar la anterior (requiere `python-pptx` y Pillow).

El generador reutiliza el de la Unidad 4 (`unidad-04/scripts/build_decks.py`): misma paleta, mismo layout y **la misma sintaxis** (ver el encabezado de `unidad-04/04-diapositivas.md`). Única diferencia: el destacado de la unidad es `consola:` ("PARA CONSOLA") en lugar de `movil:`.

**Versión 1 (2026-10-24).** Pedido del usuario: generar las diapositivas del tema con formato similar a `unidad-04/Unidad-4-2026-completa.pptx`.
- **Clase 1 — La consola tiene dueño** (90 min, teoría 36 / práctica 54): apertura con *Asteroides*, qué es una consola para quien diseña, categorías, consolas actuales, modelos dentro de una generación, hitos históricos, ranking, histograma, ciclo de vida, regiones, precios 2026, actividad de lectura de gráficos, de los datos a las decisiones, matriz de decisión para *Asteroides*, límites, errores frecuentes y cierre.
- **Anexo: datos y fuentes** (consulta, no se expone): tablas completas, ventas por ejercicio, fuentes y lo no verificado.
- Estado: **PROPUESTO**. Certificación, mandos, accesibilidad, multijugador y optimización (investigación preliminar) se tratan más adelante en la unidad.

Reparto en minutos (los minutos van en el kicker; el generador no los muestra en la slide):

| Bloque | Slides | Minutos | Tipo |
|---|---|---|---|
| Apertura | 2 | 8 | Teoría |
| La consola como plataforma | 3–6 | 14 | Teoría |
| Historia y datos | 7–14 | 14 | Teoría |
| Actividad 1: leer los gráficos | 15 | 20 | Práctica |
| De los datos a las decisiones + Actividad 2 | 16–17 | 26 | Práctica |
| Puesta en común, límites, errores y cierre | 18–20 | 8 | Práctica |
| **Total** | | **90** | **Teoría 36 (40 %) · Práctica 54 (60 %)** |

---

# DECK 1 | La consola tiene dueño | Unidad V · Clase 1

## 1 | Diseño según Plataforma: Consolas
tipo: portada
kicker: UNIDAD V · CLASE 1
- La consola tiene dueño
- Diseño según Plataformas de Juego · Ing. Elsa Daniela Ramírez · FI – UNJu · 2026
notas:
Glosario (conceptos cortos para la docente):
• Plataforma: el conjunto de hardware, sistema y tienda donde corre y se vende un juego.
• Consola: equipo dedicado a jugar, fabricado y controlado por una empresa (Sony, Microsoft, Nintendo).
Presentar la unidad como continuación de la anterior: veníamos de llevar Asteroides de PC a móvil. Ahora el destino es una consola.
Idea fuerza de la clase: en PC y en móvil el desarrollador decide casi todo; en consola hay un dueño de la plataforma que fija reglas, precios, modelos de hardware y certificación.
No empezar por specs ni por la herramienta: la clase abre con un problema de decisión.
Imagen sugerida (opcional, sin recuadro en la slide): un mando de consola junto a un teléfono con Asteroides.

## 2 | Un publisher, una sola consola
tipo: contenido
kicker: APERTURA · 8 MIN
- Asteroides ya corre en PC y Android
- Un publisher financia una consola
- PS5, Xbox Series o Switch 2
- ¿Cuál? ¿Qué hay que cambiar?
pregunta: ¿Alcanza con elegir "la que más vendió"?
notas:
Glosario (conceptos cortos para la docente):
• Publisher: empresa que financia, distribuye y comercializa un juego hecho por otro equipo.
• Port: versión de un juego adaptada a otra plataforma.
Relato: "Terminamos Asteroides para PC y Android. Un publisher ofrece financiar el port a consola, pero solo a una este año: PS5, Xbox Series X|S o Nintendo Switch 2".
Dejar que voten a mano alzada y anotar en el pizarrón los argumentos. Respuesta esperada: casi todos van a decir "la que más vendió".
No corregir todavía. La clase va a mostrar tres problemas de esa respuesta:
1. Las cifras no se comparan directo: cada consola tiene otra edad, Microsoft no publica las suyas y lo publicado son despachos, no jugadores.
2. Cada consola impone condiciones de diseño: mando, TV a distancia, un modelo más débil en la misma generación, certificación y tienda única.
3. En 2026 el mercado cambió: las consolas suben de precio y las ventas de hardware caen.
Volver a esta votación en la Actividad 2 para ver si cambió.

## 3 | Una consola, vista por quien diseña
tipo: contenido
kicker: LA CONSOLA COMO PLATAFORMA · 4 MIN
| Rasgo | Consecuencia de diseño |
| Plataforma cerrada | NDA, registro y kit de desarrollo |
| Hardware fijo por modelo | Optimizar a medida, en cada modelo |
| Varios modelos por generación | El más débil fija el piso |
| Mando como entrada | Todo navegable con mando |
| TV a tres metros | UI más grande, zona segura |
| Certificación y tienda única | Requisitos antes de publicar |
fuente: Unity 6000.3 Manual, Platform development; Microsoft, XBOX Requirements (XR-003, XR-130); XAG 101
notas:
Glosario (conceptos cortos para la docente):
• Plataforma cerrada: la que exige acuerdos de confidencialidad y legales con el fabricante para usar sus herramientas y su hardware (definición del manual de Unity).
• NDA: acuerdo de confidencialidad.
• Kit de desarrollo (devkit): consola especial que presta o vende el fabricante para desarrollar y depurar.
• Certificación: revisión técnica que hace el fabricante antes de dejar publicar un juego o un parche.
• Zona segura: margen de la pantalla donde no conviene poner UI esencial porque algunas TV lo recortan.
Desarrollo de cada fila:
- Cerrada: no se publica "subiendo un archivo". Hay que registrarse, firmar NDA y conseguir devkit (Sony presta un dev kit y un test kit a socios nuevos; Nintendo pide aceptar NDA y enviar el juego a revisión).
- Hardware fijo: todos los jugadores de un modelo tienen la misma máquina; eso permite optimizar a medida, cosa imposible en PC o en Android.
- Varios modelos: Series S y Series X, PS5 y PS5 Pro, Switch 2 portátil y en dock. Microsoft exige los mismos modos de juego en toda la generación (XR-130).
- Mando: XR-003 dice literalmente "On consoles, the game must be fully navigable with a controller".
- TV: la Xbox Accessibility Guideline 101 recomienda 26 px de texto mínimo a 1080p en consola (18 px en PC).
- Certificación: también los parches pasan por ella. Más adelante en la unidad vemos los requisitos públicos de Microsoft.
Pregunta rápida: ¿cuáles de estos rasgos tenía Android? Ninguno es obligatorio en Android salvo la tienda (y ni siquiera: se puede instalar un APK).

## 4 | Cuatro categorías en 2026
tipo: contenido
kicker: LA CONSOLA COMO PLATAFORMA · 3 MIN
| Categoría | Ejemplos | Qué cambia |
| Sobremesa | PS5, Xbox Series | TV, mando, varios modelos |
| Portátil | Game Boy, DS, PSP | Absorbida por híbrida y móvil |
| Híbrida | Switch, Switch 2 | Dos presupuestos: portátil y dock |
| PC-consola | Steam Deck, Steam Machine | Sistema abierto, revisión pública |
consola: En una híbrida, el mismo juego debe rendir en 7,9" y en una TV 4K
fuente: Nintendo, Switch 2 Tech Specs; Valve, Steam Deck Tech Specs y Compatibility Review; SIE, company timeline
notas:
Glosario (conceptos cortos para la docente):
• Sobremesa: consola que se conecta a la TV y no se lleva encima.
• Híbrida: consola que funciona como portátil y también conectada a la TV (dock).
• Dock: base que conecta la Switch a la TV.
• SteamOS: sistema operativo de Valve, basado en Linux.
El programa de la materia habla de "sobremesa y portátiles". Esa dicotomía ya no alcanza:
- Desde 2017 ninguno de los tres grandes tiene una portátil pura. PlayStation Portal (nov-2023) no es una consola: reproduce a distancia lo que corre en la PS5.
- La portátil histórica (Game Boy 118,69 M; DS 154,02 M; PSP más de 76,4 M) fue absorbida por la híbrida y por el teléfono (INFERENCIA).
- Switch 2: pantalla de 7,9" 1920×1080 en portátil; en dock, hasta 3840×2160 a 60 fps (dato oficial de Nintendo). Son dos presupuestos de rendimiento y dos tamaños de UI en el mismo juego.
- Steam Deck y Steam Machine son PC con SteamOS: el sistema es abierto, pero Valve publica una revisión de compatibilidad (Verified / Playable / Unsupported) que se parece a una certificación.

## 5 | Las consolas de hoy
tipo: contenido
kicker: LA CONSOLA COMO PLATAFORMA · 4 MIN
| Consola | Lanzamiento | Dato clave | Precio EE. UU. | Vendidas |
| PS5 | nov-2020 | Pro: +67 % de cómputo | USD 650 / 900 Pro | +95 M |
| Xbox Series X | nov-2020 | 16 GB de memoria | +USD 100–150 (ago-2026) | No publica |
| Xbox Series S | nov-2020 | 10 GB de memoria | ídem | No publica |
| Switch 2 | jun-2025 | Portátil + dock 4K | USD 500 | 23,68 M |
| Steam Machine | jun-2026 | PC con SteamOS | USD 1.049 | No publica |
fuente: SIE Business Data (30-jun-2026); PlayStation Blog (27-mar-2026); Xbox Wire (25-jun-2026); Nintendo IR (30-jun-2026); Steam Store
notas:
Glosario (conceptos cortos para la docente):
• Sell-in: unidades despachadas por el fabricante a los comercios; no son consolas compradas por jugadores.
• PS5 Pro: modelo más potente de la misma generación, lanzado el 7-nov-2024.
• GDDR6: tipo de memoria rápida que comparten CPU y GPU en estas consolas.
Datos completos (todos verificados el 2026-10-24):
- PS5: lanzamiento 12-nov-2020. Más de 95 M al 30-jun-2026 (Sony). Precios desde 2-abr-2026: USD 649,99 con lectora, 599,99 Digital, 899,99 Pro. PS5 Pro: "67 percent more Compute Units", memoria 28 % más rápida, hasta 45 % más de render, escalado PSSR.
- Xbox Series X: 16 GB GDDR6, 12 TFLOPS, objetivo 4K. Series S: 10 GB, 4 TFLOPS, objetivo 1440p. Desde 1-ago-2026 suben USD 100 (512 GB) y USD 150 (1 TB); se discontinúa el modelo de 2 TB. La fecha exacta de lanzamiento (nov-2020) es conocimiento general: la página de Microsoft solo registra el anuncio.
- Switch 2: 5-jun-2025. 23,68 M de consolas y 58,17 M de juegos al 30-jun-2026. USD 449,99 → 499,99 desde 1-sep-2026.
- Steam Machine: a la venta desde 22-jun-2026; AMD Zen 4 de 6 núcleos, GPU RDNA3 de 28 CU, 16 GB DDR5 + 8 GB GDDR6. USD 1.049 (512 GB) y 1.349 (2 TB).
- Las specs base de PS5 y la RAM de Switch 2 no se verificaron con fuente oficial: no darlas como dato.
Pregunta para el grupo: ¿qué columna de esta tabla le importa más al diseñador? Respuesta esperada: la memoria (y la existencia de varios modelos), más que el precio o las ventas.

## 6 | Misma generación, dos pisos
tipo: contenido
kicker: LA CONSOLA COMO PLATAFORMA · 3 MIN
- Series S: 10 GB de memoria
- Series X: 16 GB de memoria
- Mismos modos de juego (XR-130)
- BG3: sin pantalla dividida en S
comparacion: Series S: 10 GB, 1440p, 4 TFLOPS // El piso del diseño | Series X: 16 GB, 4K, 12 TFLOPS // El techo del diseño
consola: Se diseña para el modelo más débil y se escala hacia arriba, nunca al revés
fuente: Xbox, páginas de Series S y Series X; XBOX Requirements XR-130; Kotaku (24-ago-2023) y Shacknews (28-ene-2025) sobre BG3
notas:
Glosario (conceptos cortos para la docente):
• Generación: conjunto de consolas de un fabricante que comparten catálogo (Series S y Series X son la misma generación).
• XR-130: requisito de Microsoft que exige partidas guardadas compatibles y modos de juego idénticos entre consolas de la misma generación.
• Split-screen (pantalla dividida): varios jugadores en la misma TV, cada uno con su parte de la pantalla.
Caso Baldur's Gate 3 (fuentes de prensa profesional; las fuentes primarias no se pudieron abrir):
- En agosto de 2023 Larian anunció que la versión de Series S no tendría pantalla dividida. Kotaku citó a Swen Vincke: "Series S will not feature split-screen coop".
- La pantalla dividida necesita renderizar dos vistas y más memoria; en 10 GB no entraba.
- Xbox dijo que seguiría trabajando en el tema; el Patch 8 (2025) agregó la pantalla dividida en Series S.
Lección: la memoria del modelo más débil no solo baja la calidad gráfica, puede eliminar un modo de juego entero. Y con XR-130, ese modo no se puede dejar "solo para Series X" sin negociarlo con Microsoft. Que BG3 haya salido igual es una excepción cuyo detalle no es público (INFERENCIA).
Lo mismo pasa con Switch 2: el modo portátil es el piso; el dock es el techo.

## 7 | Hitos que cambiaron el diseño
tipo: contenido
kicker: HISTORIA Y DATOS · 2 MIN
panel: ancho
hitos: 1983 · Famicom · el fabricante controla qué se publica | 1989 · Game Boy · nace la portátil masiva | 1997 · DualShock · dos sticks y vibración | 2002 · Xbox Live · el online como servicio | 2006 · Wii · control por movimiento | 2017 · Switch · consola híbrida | 2020 · Series S/X · dos potencias a la vez | 2026 · Subas de precio · la memoria encarece
fuente: Nintendo IR; playstation.com/playstation-history; Microsoft, comunicado del 13-ago-2002; Xbox Wire, PlayStation Blog y Nintendo (2026)
notas:
Glosario (conceptos cortos para la docente):
• DualShock: mando de PlayStation de 1997 con dos palancas analógicas y vibración; es la base de los mandos actuales.
• Xbox Live: servicio en línea de Xbox lanzado en noviembre de 2002, solo para banda ancha.
• Hito: hecho que cambia la forma de diseñar o de vender juegos.
Leer la línea de izquierda a derecha y preguntar en cada hito: ¿qué tuvo que cambiar el diseñador?
- 1983: Family Computer sale en Japón el 15-jul-1983. Ese mismo año, en EE. UU., el mercado de consolas colapsa por exceso de juegos de baja calidad (conocimiento general, sin fuente oficial verificada). Desde entonces el fabricante controla qué se publica: es el antecedente de la certificación.
- 1989: Game Boy (21-abr-1989), 118,69 M con Game Boy Color.
- 1997: el DualShock (nov-1997) agrega dos sticks analógicos y vibración. Es el mando que todavía usan PS5 y Xbox.
- 2002: Xbox Live sale en el primer aniversario de Xbox (nov-2002), solo banda ancha. El juego en línea pasa a tener reglas de la plataforma.
- 2006: Wii (19-nov-2006), 101,63 M, con un hardware menos potente que el de sus rivales.
- 2017: Switch (3-mar-2017), la primera híbrida de éxito: 156,59 M.
- 2020: Xbox Series S y X salen juntas, con potencias distintas desde el primer día.
- 2026: PS5, Xbox y Switch 2 suben de precio por el costo de la memoria.
La escala es ordinal (el gráfico lo aclara): la separación no es proporcional al tiempo.

## 8 | Cuatro décadas de lanzamientos
tipo: contenido
kicker: HISTORIA Y DATOS · 1 MIN
panel: ancho
captura: imagenes/slides/06-linea-de-tiempo.png | Primer lanzamiento mundial de cada consola, por fabricante. La línea punteada es hoy.
fuente: Nintendo IR (planilla por región); SIE, Expanded company timeline; Microsoft, Facts about Microsoft
notas:
Glosario (conceptos cortos para la docente):
• Línea de tiempo proporcional: aquí sí la distancia horizontal representa años, a diferencia de la slide anterior.
Qué mostrar (un minuto):
- Nintendo es el único fabricante presente desde los 80, y el único que sostuvo portátiles hasta pasarlas a la híbrida.
- Sony entra en 1994 (PlayStation, 3-dic-1994 en Japón) y Microsoft en 2001 (Xbox, 15-nov-2001).
- Las generaciones de Sony y Microsoft salen casi juntas (2005–06, 2013, 2020). Nintendo va con su propio calendario.
- Desde 2016 aparecen los modelos "de mitad de generación" (PS4 Pro, Xbox One X, PS5 Pro): un mismo juego con dos perfiles de rendimiento.
Las bandas grises marcan la crisis de 1983 en EE. UU. (conocimiento general) y la pandemia (2020–21), que disparó las ventas de Switch.

## 9 | Las más vendidas de la historia
tipo: contenido
kicker: HISTORIA Y DATOS · 2 MIN
- PS2: más de 160 M
- Switch: 156,59 M, sigue
- Wii 101,6 M → Wii U 13,6 M
- Xbox: Microsoft no publica
captura: imagenes/slides/01-ranking-ventas-consolas.png | Rayado = todavía en venta. Azul: Sony · Naranja: Nintendo
fuente: Nintendo IR, Dedicated Video Game Sales Units (30-jun-2026); SIE, Business Data & Sales
notas:
Glosario (conceptos cortos para la docente):
• Ventas de vida: total de unidades despachadas desde el lanzamiento hasta la fecha del dato.
• "More than": Sony publica cifras redondeadas hacia abajo ("más de 160 millones").
Lectura guiada:
- Podio: PS2 (más de 160 M), Switch (156,59 M, todavía en venta) y DS (154,02 M).
- El mismo fabricante tiene éxitos y fracasos seguidos: Wii vendió 101,63 M y su sucesora Wii U, 13,56 M. Una buena idea de control (el GamePad con pantalla) no garantizó ventas.
- Microsoft no aparece: no publica unidades de Xbox One ni de Series X|S. Las cifras que circulan (Xbox 360 "84 M") no se verificaron con un documento de Microsoft. Que no publique no significa que no venda.
Cuidado al comparar: las fechas de corte son distintas (PS2 al 31-mar-2012, PS4 al 30-jun-2022, Nintendo al 30-jun-2026), y las consolas rayadas siguen sumando.
Dato para la discusión: Switch está 3,4 M por debajo de PS2. Al ritmo de su último ejercicio (3,80 M) podría superarla, pero no hay dato oficial que lo anticipe (INFERENCIA).

## 10 | Histograma: no es un gráfico de barras
tipo: contenido
kicker: HISTORIA Y DATOS · 2 MIN
- Barras: una por consola
- Histograma: casos por intervalo
- 13 de 15, menos de 125 M
- Más de 150 M: excepcional
captura: imagenes/slides/02-histograma-ventas.png | 15 consolas ya discontinuadas de Sony y Nintendo, en intervalos de 25 M
fuente: Mismos datos que la slide anterior, sin las consolas en venta
notas:
Glosario (conceptos cortos para la docente):
• Histograma: gráfico que agrupa los datos en intervalos (clases) y muestra cuántos casos caen en cada uno. Las barras van pegadas porque los intervalos son continuos.
• Gráfico de barras: una barra por categoría (por consola), separadas, para comparar valores.
• Distribución: la forma en que se reparten los valores (dónde se concentran, dónde hay huecos).
Error frecuente que vale la pena corregir acá: llamar "histograma" a cualquier gráfico de barras. El ranking de la slide anterior NO es un histograma.
Cómo leer este:
- Eje horizontal: ventas de vida en intervalos de 25 M. Eje vertical: cuántas consolas.
- 13 de las 15 consolas discontinuadas vendieron menos de 125 M; solo PS2 y DS pasan los 150 M.
- Hay un hueco entre 125 y 150 M: ninguna consola discontinuada cayó ahí.
Conclusión (INFERENCIA): un éxito de la escala de Switch es la excepción. Para planificar un port, conviene pensar en la consola "típica", no en la récord.
Se excluyen las consolas en venta porque su cifra todavía crece y deformaría la distribución.

## 11 | Ciclo de vida de una consola
tipo: contenido
kicker: HISTORIA Y DATOS · 2 MIN
- Sube, pico, decae
- Switch: pico 28,8 M (pandemia)
- PS5: pico en el 4.º año
- Switch 2: 19,9 M en 10 meses
captura: imagenes/slides/03-ciclo-de-vida-anual.png | Millones por ejercicio fiscal (abril a marzo) desde el lanzamiento
fuente: Nintendo IR (planilla por región, 31-mar-2026); Sony vía 20-F y Game Developer (8-may-2026)
notas:
Glosario (conceptos cortos para la docente):
• Ejercicio fiscal: año contable de la empresa. En Sony y Nintendo va de abril a marzo.
• Base instalada: cantidad de consolas que están en los hogares. Crece año a año con las ventas.
• Ciclo de vida: subida, pico y caída de las ventas de una consola.
Lectura:
- Switch subió cuatro ejercicios, llegó a 28,83 M entre abril de 2020 y marzo de 2021 (pandemia) y cayó a 3,80 M en el ejercicio en que salió Switch 2.
- PS5 arrancó más lento (7,8 y 11,5 M; escasez de chips) y su pico (20,8 M) llegó en el cuarto ejercicio. La caída posterior coincide con las subas de precio.
- Switch 2 vendió 19,86 M en su primer ejercicio, de menos de diez meses. A los 13 meses tenía 23,68 M; Switch tenía 17,79 M en el mismo plazo.
Datos: el valor de PS5 del cuarto ejercicio (20,8 M) se obtiene restando los otros cinco al total de 93,7 M; los tres primeros vienen de los 20-F de Sony citados por el buscador y son coherentes con el hito oficial de 40 M en julio de 2023.
Por qué le importa al diseñador (INFERENCIA): lanzar en el año 1 es un público chico con poca competencia; en el año 6, mucho público, mucha competencia y quizás la sucesora ya en la calle.

## 12 | Dónde se venden
tipo: contenido
kicker: HISTORIA Y DATOS · 1 MIN
- Japón: un tercio en la NES
- Bajó con N64 y GameCube
- Switch y Switch 2: 25–29 %
- Europa y resto: 14 % → 38 %
captura: imagenes/slides/04-regiones-nintendo.png | % de las consolas Nintendo vendidas por región
fuente: Nintendo IR, Consolidated Sales Transition by Region (31-mar-2026)
notas:
Glosario (conceptos cortos para la docente):
• Localización: adaptar textos, audio, formatos y a veces contenido a otro idioma y cultura.
• Región: zona de venta que reporta el fabricante (Japón, América, Europa, otros).
Lectura:
- NES y Super Famicom: Japón era un tercio de las ventas. N64 y GameCube: menos de un quinto.
- Switch: 25 % Japón, 38 % América, 37 % Europa y resto. Switch 2 (primer ejercicio): 29 / 34 / 38.
- Antes de Switch, Nintendo no separa Europa de "otros"; por eso la tercera franja agrupa ambas.
Consecuencia de diseño (INFERENCIA): en Nintendo, más de la mitad del mercado está fuera de América. La localización al japonés y a los idiomas europeos se diseña desde el principio: textos que se alargan, fuentes con caracteres japoneses, botones que no se cortan.
Sony no publica un desglose regional comparable en las páginas consultadas.

## 13 | 2026: las consolas suben de precio
tipo: contenido
kicker: HISTORIA Y DATOS · 2 MIN
- PS5 Digital: +50 %
- Switch 2: +11 %
- Xbox: +USD 100–150
- Causa: costo de memoria
captura: imagenes/slides/05-precios-lanzamiento-vs-2026.png | Círculo vacío: precio de lanzamiento · lleno: vigente en oct-2026 (USD, EE. UU.)
fuente: PlayStation Blog (16-sep-2020 y 27-mar-2026); Nintendo (8-may-2026); Xbox Wire (25-jun-2026)
notas:
Glosario (conceptos cortos para la docente):
• Precio sugerido: el que fija el fabricante para los comercios.
• Componentes: memoria (RAM) y almacenamiento (SSD), cuyo precio subió por la demanda de los centros de datos de IA (según la prensa; los fabricantes hablan de costo de componentes).
Datos verificados:
- PS5 Digital: USD 399,99 en el lanzamiento (2020) → 599,99 desde 2-abr-2026. PS5 con lectora: 499,99 → 649,99. PS5 Pro: 899,99.
- Switch 2: 449,99 → 499,99 desde 1-sep-2026; en Japón ¥49.980 → ¥59.980 desde 25-may-2026.
- Xbox: +USD 100 (512 GB) y +USD 150 (1 TB) desde 1-ago-2026. Microsoft escribió: "console storage and memory prices have increased by more than 2.5x and we expect another doubling by the fall of 2027".
Historia: una consola solía bajar de precio con los años y eso ampliaba el público. En 2026 pasa lo contrario.
Consecuencia (INFERENCIA): si la base instalada crece más lento, la generación anterior y la PC siguen siendo mercado por más tiempo. Y la memoria, que ya limitaba el diseño (Series S), ahora también limita cuántas consolas hay.

## 14 | 2026 en cifras
tipo: contenido
kicker: HISTORIA Y DATOS · 2 MIN
| Dato | Valor |
| Mercado mundial 2025 | USD 201.600 M (Newzoo) |
| Crecimiento 2025 | PC +12 % · móvil +10,7 % · consola +2,8 % |
| Usuarios activos PlayStation | 125 M por mes |
| Switch 2 en 13 meses | 23,68 M (Switch: 17,79 M) |
| Xbox | "Hardware component crisis" |
| PlayStation | Sin discos para juegos nuevos desde 2028 |
fuente: GamesBeat (18-jun-2026) sobre Newzoo; SIE; Nintendo IR; Xbox Wire (10-jun-2026); PlayStation Blog (1-jul-2026)
notas:
Glosario (conceptos cortos para la docente):
• MAU (usuarios activos mensuales): cuentas que jugaron al menos una vez en el mes.
• Distribución digital: venta del juego como descarga, sin disco.
Detalle:
- Mercado 2025: USD 201.600 M, primera vez que supera los 200.000 M (Newzoo, citado por GamesBeat; Newzoo no fue accesible directamente). El crecimiento está en PC y móvil; la consola crece poco, pero sigue siendo donde se venden los juegos más caros (conocimiento general, sin cifra verificada).
- PlayStation: 125 M de usuarios activos mensuales (estimación de Sony) y más de 1.706 M de juegos de PS4 + PS5.
- Xbox: memo del 10-jun-2026, "We are in a hardware component crisis"; no logra fabricar todas las consolas que se le piden y sigue comprometida con su próxima consola (Helix), sin más detalles públicos.
- Sony: desde enero de 2028 los juegos nuevos de PlayStation dejan de fabricarse en disco. Consecuencia de diseño: tamaño de descarga, parches chicos y contenido descargable por partes.
- Steam Machine (jun-2026, USD 1.049): la PC se acerca a la consola.
Cierre de la parte teórica: con estos datos, volver a la pregunta de la apertura.

## 15 | Actividad 1: leer los gráficos
tipo: actividad
kicker: ACTIVIDAD · 20 MIN · GRUPOS DE 3
| Pregunta | Gráfico | Respuesta |
| ¿Qué consola tiene más base instalada hoy? | Ranking | |
| ¿Cuál crece más rápido? | Ciclo de vida | |
| ¿Qué dato falta y por qué? | Ranking | |
| ¿La consola típica vende 150 M? | Histograma | |
| ¿Qué idiomas priorizar en Nintendo? | Regiones | |
actividad: Cada respuesta cita un número y su fecha de corte
notas:
Glosario (conceptos cortos para la docente):
• Fecha de corte: el día al que corresponde un dato ("al 30-jun-2026").
• Base instalada: consolas en los hogares (ver slide 11).
Consigna completa: en grupos de tres, con los gráficos proyectados o impresos (están en imagenes/ del repositorio), responder las cinco preguntas citando el número y su fecha. 15 minutos de trabajo y 5 de puesta en común rápida.
Respuestas esperadas:
1. Base instalada hoy: Switch (156,59 M, al 30-jun-2026), aunque una parte ya no se usa: el ranking muestra despachos, no consolas activas. Si se pregunta por la generación actual: PS5 (más de 95 M) por encima de Switch 2 (23,68 M); Xbox, sin dato.
2. Crece más rápido: Switch 2 (19,86 M en su primer ejercicio; 23,68 M en 13 meses contra 17,79 M de Switch).
3. Falta Xbox One y Series X|S: Microsoft no publica unidades. Lo correcto es decir "sin dato", no "cero".
4. No: 13 de 15 consolas discontinuadas vendieron menos de 125 M. 150 M es excepcional.
5. Japonés e idiomas europeos: Japón es el 25–29 % y Europa y resto el 37–38 % en Switch y Switch 2.
Error a vigilar: comparar PS2 con PS5 sin tener en cuenta que PS5 sigue en venta y tiene 6 años.

## 16 | De los datos a las decisiones
tipo: contenido
kicker: PRÁCTICA · INSUMO DE LA ACTIVIDAD 2
| Dato | Decisión de diseño |
| Varios modelos por generación | Diseñar para el más débil |
| Mando y TV a distancia | UI por cruceta, texto ≥ 26 px |
| Switch 1 sigue en 156 M de hogares | ¿Salir también en Switch 1? |
| Sin discos desde 2028 (PlayStation) | Descargas y parches chicos |
| Japón y Europa: más de la mitad | Localizar desde el diseño |
| Precios en alza | Contar con PC y generación anterior |
fuente: 01-desarrollo-tema-consolas.md, sección 7; XAG 101; XR-130
notas:
Glosario (conceptos cortos para la docente):
• Cruceta (D-pad): botón en cruz del mando, para moverse entre opciones.
• Presupuesto de rendimiento: tiempo de cuadro, memoria y almacenamiento que el juego puede usar en un modelo.
Esta tabla es la herramienta para la Actividad 2: cada fila convierte un dato de la clase en una decisión que alguien del equipo tiene que tomar.
Ampliación de cada fila:
- Modelo más débil: Series S (10 GB) y Switch 2 portátil fijan el piso; escalar hacia arriba.
- Mando y TV: XR-003 obliga a navegar todo con mando; XAG 101 recomienda texto mínimo de 26 px a 1080p. La UI de PC no sirve tal cual. El mouse de Asteroides para menús no existe en consola.
- Switch 1: llegar a más de 180 M de consolas de la familia, con el costo de un tercer presupuesto de rendimiento.
- Digital: con PlayStation sin discos desde 2028, el tamaño de la descarga y de los parches es parte del diseño.
- Localización: textos más largos en alemán, caracteres japoneses en las fuentes.
- Precios: si la base instalada crece lento, PC (Steam Deck y Steam Machine) y la generación anterior no son un "port posterior": son parte del plan (INFERENCIA).
Mandos con funciones propias (gatillos adaptativos del DualSense, HD Rumble 2): se usan como mejora opcional; el juego tiene que funcionar con cualquier mando, incluido uno adaptado. Lo vemos más adelante en la unidad.

## 17 | Actividad 2: Asteroides va a consola
tipo: actividad
kicker: ACTIVIDAD · 26 MIN · GRUPOS DE 3
| Criterio | PS5 | Xbox Series | Switch 2 |
| Base instalada (dato + fecha) | | | |
| Modelo más débil | | | |
| Mando y UI | | | |
| Riesgo principal | | | |
| Decisión del grupo | | | |
actividad: Elegir una consola con 3 datos y listar 3 cambios obligatorios
notas:
Glosario (conceptos cortos para la docente):
• Matriz de decisión: tabla que compara opciones con los mismos criterios para justificar una elección.
• Cambio obligatorio: modificación sin la cual el juego no se puede publicar o no se puede jugar en esa consola.
Consigna completa (20 minutos de trabajo + 6 de exposición de dos grupos):
1. Completar la matriz con datos de la clase, citando la fuente y la fecha.
2. Elegir UNA consola y justificarla con al menos tres datos.
3. Listar tres cambios de diseño obligatorios para Asteroides en esa consola (usar la slide 16).
Cambios esperados para cualquier consola:
- Entrada: el juego ya separa la intención del dispositivo (lo hicimos en el porteo a móvil); falta mapear el mando y quitar la dependencia del mouse en los menús.
- UI: menús navegables por cruceta, texto más grande, zona segura de TV.
- Ciclo de vida: pausar al desconectarse el mando y al suspender la consola (XR-115 y XR-112, que veremos más adelante en la unidad).
Específicos: en Switch 2, dos presupuestos (portátil y dock) y controles con Joy-Con; en Xbox, el piso es Series S; en PS5, el modelo base (no la Pro).
No hay una respuesta única correcta: se evalúa que la decisión use datos con fecha y que los cambios sean de diseño, no "hacerlo más lindo".
Volver a la votación de la apertura: ¿cuántos grupos siguen eligiendo "la que más vendió"?

## 18 | Qué NO resuelven estos datos
tipo: contenido
kicker: PUESTA EN COMÚN · 3 MIN
- No dicen cuántos juegan tu género
- No pronostican ventas de un indie
- Certificación de Sony y Nintendo: NDA
- Sin devkit, no se compila
notas:
Glosario (conceptos cortos para la docente):
• Indie: juego de un equipo independiente, sin un gran publisher detrás.
• Devkit: consola de desarrollo que entrega el fabricante tras firmar los acuerdos.
Desarrollo:
- Las ventas de hardware sirven para dimensionar plataformas, no para predecir cuánto venderá un juego puntual ni cuántos jugadores tiene un género.
- Solo Microsoft publica sus requisitos de certificación y sus casos de prueba. Los de Sony (TRC) y Nintendo (Lotcheck) están bajo NDA: en la materia solo se enseñan los pasos públicos del proceso.
- Sin registro, NDA y kit de desarrollo no se compila para consola. En el aula lo simulamos con PC y un mando, y con los criterios públicos de Steam Deck.
- Los datos de Xbox no existen en forma oficial: cualquier comparación con Xbox es incompleta.

## 19 | Errores frecuentes
tipo: contenido
kicker: PUESTA EN COMÚN · 3 MIN
| Error | Corrección |
| "Sell-in = consolas compradas" | Son despachos a comercios |
| "La que más vendió es la mejor" | Importa tu público y el costo del port |
| "PS5 pierde contra PS2" | Comparar por años desde el lanzamiento |
| "Xbox no vende" | No publica: sin dato ≠ cero |
| "Si corre en Series X, corre en S" | El piso lo fija la más débil |
| "Las consolas bajan de precio" | En 2026, las tres suben |
notas:
Glosario (conceptos cortos para la docente):
• Sell-through: consolas efectivamente compradas por jugadores; casi nunca se publica.
Desarrollo de cada error:
- Sell-in: lo publicado por Sony y Nintendo son unidades despachadas. Puede haber consolas en depósitos.
- "La mejor": la base instalada activa del público del juego, la competencia en su género y el costo del port pesan más que el total histórico.
- PS5 vs PS2: PS5 sigue en venta y tiene 6 años; PS2 se vendió más de 12. Usar el gráfico de ciclo de vida.
- Xbox: Microsoft dejó de publicar unidades con Xbox One. Ausencia de dato no es dato cero.
- Series S/X: 10 GB contra 16 GB. Caso BG3.
- Precios: fue cierto durante décadas; en 2026 PS5, Xbox y Switch 2 subieron.
Uno más, si hay tiempo: "los specs explican el éxito". Wii (101,63 M) era menos potente que sus rivales; Wii U (13,56 M) tenía una idea de control original y fracasó.

## 20 | Cierre
tipo: cierre
kicker: CIERRE · 2 MIN
- La consola tiene dueño y reglas
- Datos con fuente y fecha
- El piso: el modelo más débil
- Más adelante: certificación y mandos
notas:
Glosario (conceptos cortos para la docente):
• Piso de diseño: la configuración mínima en la que el juego tiene que funcionar bien.
Síntesis en tres ideas:
1. En consola, el fabricante fija modelos, precios, mandos, certificación y tienda: se diseña dentro de sus reglas.
2. Los datos de mercado sirven si se leen con fuente, fecha y tipo de cifra (sell-in), y sabiendo qué falta (Xbox).
3. El diseño parte del modelo más débil de la generación y escala hacia arriba.
Más adelante en la unidad: los requisitos públicos de certificación de Microsoft, los mandos (Input System, remapeo, glifos), accesibilidad, multijugador local y optimización.
Para la próxima: traer la matriz de la Actividad 2 terminada; se usa como punto de partida.

# DECK 2 | Anexo: datos y fuentes | Unidad V · Anexo de consulta

## 21 | Ventas de vida: tabla completa
tipo: contenido
kicker: ANEXO · CONSULTA
subtabla: Nintendo (al 30-jun-2026)
| Consola | Año | Millones |
| Switch (en venta) | 2017 | 156,59 |
| DS | 2004 | 154,02 |
| Game Boy + Color | 1989 | 118,69 |
| Wii | 2006 | 101,63 |
| Game Boy Advance | 2001 | 81,51 |
| 3DS | 2011 | 75,94 |
| Famicom / NES | 1983 | 61,91 |
| Super Famicom / SNES | 1990 | 49,10 |
| Nintendo 64 | 1996 | 32,93 |
| Switch 2 (en venta) | 2025 | 23,68 |
| GameCube | 2001 | 21,74 |
| Wii U | 2012 | 13,56 |
subtabla: Sony (cifras "more than")
| Consola | Año | Millones · al |
| PS2 | 2000 | 160 · mar-2012 |
| PS4 | 2013 | 117 · jun-2022 |
| PlayStation | 1994 | 102,4 · mar-2012 |
| PS5 (en venta) | 2020 | 95 · jun-2026 |
| PS3 | 2006 | 87,4 · mar-2017 |
| PSP | 2004 | 76,4 · mar-2012 |
| PS Vita | 2011 | No publicado |
notas:
Glosario (conceptos cortos para la docente):
• Sell-in: unidades despachadas a comercios.
Fuentes: Nintendo IR, Dedicated Video Game Sales Units (https://www.nintendo.co.jp/ir/en/finance/hard_soft/index.html); SIE, Business Data & Sales (https://sonyinteractive.com/en/our-company/business-data-sales/). Datos en datos/ventas-hardware.csv.
Microsoft no publica unidades de Xbox One ni de Series X|S; las de Xbox y Xbox 360 que circulan en prensa no se verificaron.

## 22 | Ventas por ejercicio fiscal
tipo: contenido
kicker: ANEXO · CONSULTA
subtabla: Nintendo Switch (millones)
| Ejercicio | Millones |
| FY3/2017 (1 mes) | 2,74 |
| FY3/2018 | 15,05 |
| FY3/2019 | 16,95 |
| FY3/2020 | 21,03 |
| FY3/2021 | 28,83 |
| FY3/2022 | 23,06 |
| FY3/2023 | 17,97 |
| FY3/2024 | 15,70 |
| FY3/2025 | 10,80 |
| FY3/2026 | 3,80 |
subtabla: PS5 y Switch 2 (millones)
| Ejercicio | Millones |
| PS5 abr-20 a mar-21 | 7,8 |
| PS5 abr-21 a mar-22 | 11,5 |
| PS5 abr-22 a mar-23 | 19,1 |
| PS5 abr-23 a mar-24 | 20,8 (derivado) |
| PS5 abr-24 a mar-25 | 18,5 |
| PS5 abr-25 a mar-26 | 16,0 |
| Switch 2 jun-25 a mar-26 | 19,86 |
notas:
Glosario (conceptos cortos para la docente):
• FY3/2021: ejercicio de Nintendo que termina en marzo de 2021 (abril de 2020 a marzo de 2021).
Fuentes: Nintendo IR, Consolidated Sales Transition by Region (planilla al 31-mar-2026). PS5: 16,0 y 18,5 M según Game Developer (8-may-2026, resultados de Sony); 7,8, 11,5 y 19,1 M de los 20-F de Sony citados por el buscador (tabla no abierta); 20,8 M = 93,7 M menos los otros cinco ejercicios. Coherencia: 38,4 M a mar-2023 contra el hito oficial de 40 M en jul-2023.

## 23 | Fuentes de los datos
tipo: contenido
kicker: ANEXO · CONSULTA
| ID | Fuente | Aporta |
| N1–N3 | Nintendo IR y comunicado 8-may-2026 | Ventas, regiones, precio Switch 2 |
| S1–S6 | SIE, PlayStation Blog, 20-F | Ventas, precios, fechas |
| M1–M3 | Microsoft, Xbox Wire | Fechas, precios, crisis de componentes |
| V1 | Steam Store | Steam Machine |
| G1 | GamesBeat (Newzoo) | Mercado 2025 |
| B-1 a B-52 | Investigación preliminar U5 | Specs, certificación, mandos |
fuente: datos/fuentes.md (URL completas, verificadas el 2026-10-24)
notas:
Glosario (conceptos cortos para la docente):
• Fuente primaria: la del propio fabricante (IR, blog oficial, tienda).
• Fuente secundaria: prensa que cita a la primaria.
Las URL completas están en diseno-plataformas/unidad-05/datos/fuentes.md y las fichas B en 00-investigacion-preliminar.md.
Criterio de la cátedra: los conceptos pueden venir de prensa profesional; las cifras se toman de la fuente oficial. Cuando solo hubo prensa (Newzoo, BG3), se dice en la slide.

## 24 | No verificado: no usar como dato
tipo: contenido
kicker: ANEXO · CONSULTA
- Unidades de Xbox (360, Series)
- RAM de Switch 2 y specs base de PS5
- Crisis de 1983 (conocimiento general)
- Newzoo por segmento en dólares
notas:
Glosario (conceptos cortos para la docente):
• Conocimiento general: dato histórico aceptado que no se verificó con una fuente oficial en esta investigación.
Detalle:
1. Xbox 360 "84 millones" y Xbox "24 millones": prensa y Wikipedia, sin documento de Microsoft. Series X|S: solo estimaciones de terceros.
2. RAM de Switch 2 y especificaciones base de PS5: no se leyeron en una página oficial.
3. Crisis de 1983 y su relación con los sistemas de licencias de Nintendo: conocimiento general.
4. Newzoo: el total de 2025 (USD 201.600 M) y los porcentajes de crecimiento se leyeron en GamesBeat; los montos por segmento difieren entre versiones del informe.
5. Fechas exactas de lanzamiento de Xbox Series X|S (nov-2020) y Steam Deck (2022).
6. Ventas de PS5 de los tres primeros ejercicios (ver slide 22).
