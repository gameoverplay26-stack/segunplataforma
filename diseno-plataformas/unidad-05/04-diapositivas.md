# Unidad 5 — Diapositivas (texto + notas del docente)

Fuente única de las diapositivas de la Unidad 5, tema "Diseño según plataforma: consolas". Contenido desarrollado en `01-desarrollo-tema-consolas.md`; datos y fuentes en `datos/`.

Generar desde `diseno-plataformas/unidad-05/`:
1. `python scripts/graficos_consolas.py --slides` (gráficos sin título, en `imagenes/slides/`; requiere `matplotlib`) y `python scripts/capturas_xbox.py` (imágenes del Anexo B, en `imagenes/xbox/`; requiere Pillow).
2. `python scripts/build_decks.py` → `Unidad-5-2026-completa.pptx`. Con `--version N` se genera `-vN` sin pisar la anterior (requiere `python-pptx` y Pillow).

El generador reutiliza el de la Unidad 4 (`unidad-04/scripts/build_decks.py`): misma paleta, mismo layout y **la misma sintaxis** (ver el encabezado de `unidad-04/04-diapositivas.md`). Única diferencia: el destacado de la unidad es `consola:` ("PARA CONSOLA") en lugar de `movil:`.

**Versión 1 (2026-10-24).** Pedido del usuario: generar las diapositivas del tema con formato similar a `unidad-04/Unidad-4-2026-completa.pptx`.
- **Clase 1 — La consola tiene dueño** (90 min, teoría 36 / práctica 54): apertura con *Asteroides*, qué es una consola para quien diseña, categorías, consolas actuales, modelos dentro de una generación, hitos históricos, ranking, histograma, ciclo de vida, regiones, precios 2026, actividad de lectura de gráficos, de los datos a las decisiones, matriz de decisión para *Asteroides*, límites, errores frecuentes y cierre.
- **Anexo: datos y fuentes** (consulta, no se expone): tablas completas, ventas por ejercicio, fuentes y lo no verificado.
- Estado: **PROPUESTO**. Certificación, mandos, accesibilidad, multijugador y optimización (investigación preliminar) se tratan más adelante en la unidad.

**Versión 2 (2026-10-26): unidad completa.** Pedido del usuario: terminar la Unidad 5 en **un solo archivo**, con unos **150 minutos de exposición** sin contar los prácticos, y avanzar según el tiempo. Arquitectura aprobada por el usuario el 2026-10-26: `03-arquitectura-unidad.md`. Archivo: `Unidad-5-2026-completa-v2.pptx` (`python scripts/build_decks.py --version 2`); la versión 1 no se pisa.
- La Clase 1 pasa a ser el **Bloque 1** (todavía no se dio). Solo cambia el kicker de la portada.
- Bloques nuevos: 2 certificación, 3 mando y TV, 4 demo en Xbox (Developer Mode), 5 multijugador y rendimiento, 6 cierre y TP 4 (PROPUESTO).
- Anexo A (datos y fuentes, antes slides 21–24, ahora 64–67) y **Anexo B** nuevo: Xbox en Developer Mode, paso a paso (68–74), resumen de `../laboratorio-adaptacion/GUIA-XBOX-DOCENTE.md`.
- El pie dice "Bloque N" en lugar de "Clase N": los bloques se dan según el tiempo, no son encuentros fijos.

**Versión 3 (2026-10-26): Anexo B paso a paso con imágenes.** Pedido del usuario: una sección de guía bien detallada, con capturas de pantalla generadas desde el script. El Anexo B pasa de 7 a 20 slides (68–87), un paso por slide, con su imagen y círculos numerados que coinciden con las viñetas. Las imágenes las genera `scripts/capturas_xbox.py`. Las de la PC (slides 77 y 78) salen de datos reales: el log `proyectos-unity/Tools-Xbox/ultima-corrida.log` y la carpeta del paquete de Asteroides original. Las de la consola, el Partner Center y el Device Portal son **recreaciones esquemáticas**, rotuladas en cada imagen, porque no hay capturas de la consola. Una captura real guardada en `imagenes/xbox/reales/` con el mismo nombre reemplaza a la recreación. Archivo: `Unidad-5-2026-completa-v3.pptx` (87 slides, `--version 3`). Los bloques 1–6 y el Anexo A no cambian. La v2 no se pisa.

**Versión 4 (2026-10-26): rasgos de la adaptación a consola.** Pedido del usuario: sumar a la unidad los rasgos principales de la adaptación del juego original a consola. Slide nueva **46 "Original y consola, lado a lado"** en el Bloque 4, después de "Qué agregó la capa": tabla de cinco rasgos (foco con mando, pausa, texto mínimo, botón Salir, gameplay), verificada contra el código de `asteroide-final`, `2D-Platformer-Unity-v2` y la capa `Assets/Scripts/Console/`. Las slides 46–87 pasan a 47–88 y se corrigieron las referencias internas. El Bloque 4 sube de 25 a 27 minutos de exposición. Archivo: `Unidad-5-2026-completa-v4.pptx` (88 slides, `--version 4`). La v3 no se pisa.

Reparto en minutos (los minutos van en el kicker; el generador no los muestra en la slide). La exposición incluye apertura, teoría y la demo de la docente:

| Bloque | Slides | Exposición | Práctica (aparte) |
|---|---|---|---|
| 1. La consola tiene dueño | 1–20 | 36 | 54 (A5.1, A5.2) |
| 2. Las reglas del dueño: certificación | 21–29 | 25 | 30 (A5.3) |
| 3. Mando y TV a tres metros | 30–38 | 25 | 30 (A5.4) |
| 4. Asteroides llega a la Xbox | 39–49 | 27 (con demo de 10) | 25 (A5.5) |
| 5. El modelo más débil manda | 50–60 | 30 | 30 (A5.6) |
| 6. Cierre de la unidad y TP 4 | 61–64 | 9 | — |
| Anexos A y B (consulta, no se exponen) | 65–88 | — | — |
| **Total** | **88** | **152** | **169** |

Con 150 minutos de exposición, el 40/60 pediría unos 225 de práctica. Las actividades suman 169, y cada una indica si se puede pasar a tarea.

---

# DECK 1 | La consola tiene dueño | Unidad V · Bloque 1

## 1 | Diseño según Plataforma: Consolas
tipo: portada
kicker: UNIDAD V · BLOQUE 1
- Bloque 1: La consola tiene dueño
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

# DECK 2 | Las reglas del dueño: certificación | Unidad V · Bloque 2

## 21 | Diseño según Plataforma: Consolas
tipo: portada
kicker: UNIDAD V · BLOQUE 2
- Bloque 2: Las reglas del dueño, certificación
- Diseño según Plataformas de Juego · Ing. Elsa Daniela Ramírez · FI – UNJu · 2026
notas:
Glosario (conceptos cortos para la docente):
• Certificación: revisión técnica que hace el fabricante antes de dejar publicar un juego o un parche.
• Requisito: condición que el juego debe cumplir para que el fabricante lo acepte.
Bloque de 25 minutos de exposición más la actividad A5.3 (30 minutos, en clase o de tarea).
Idea fuerza: en consola, "terminado" no lo decide el equipo sino el fabricante. Hay requisitos escritos y pruebas que el juego tiene que pasar.
Rigor: de los tres fabricantes, solo Microsoft publica sus requisitos y sus casos de prueba. De Sony y Nintendo se enseñan únicamente los pasos públicos del alta. No describir TRC ni Lotcheck: están bajo NDA y lo que circula son rumores.

## 22 | ¿Lo publicamos?
tipo: contenido
kicker: APERTURA · 3 MIN
- Asteroides ya se juega con mando
- Lo enviamos a la tienda
- Vuelve rechazado
- ¿Qué pidió el fabricante?
pregunta: ¿Quién decide que el juego está terminado?
notas:
Glosario (conceptos cortos para la docente):
• Tienda: el único canal de venta de la consola (Microsoft Store en Xbox, PlayStation Store, Nintendo eShop).
• Rechazo de certificación: devolución del juego con la lista de requisitos que no cumple.
Relato: "Llevamos Asteroides a consola con la matriz del bloque anterior. Funciona con mando. Lo enviamos y vuelve rechazado".
Dejar que propongan motivos durante 2 minutos y anotarlos. Respuestas esperadas: se cuelga, no se puede usar sin mouse, no pausa si se desconecta el mando, textos chicos, nombres de botones incorrectos.
Cerrar: varias de esas intuiciones son requisitos escritos. Microsoft los publica y los vamos a leer.

## 23 | Cómo se entra a una consola
tipo: contenido
kicker: CERTIFICACIÓN · 4 MIN
| Fabricante | Paso público | Bajo NDA |
| Microsoft | ID@Xbox: mayor de 18, NDA | GDK para consola |
| Sony | PlayStation Partners + GDPA | Requisitos (TRC) |
| Nintendo | Registro, NDA, revisión | Guías (Lotcheck) |
| Unity | Pro o clave del fabricante | — |
fuente: Microsoft Game Dev, Publish (ID@Xbox); microsoft/GDK; SIE, Showing your Game to PlayStation; Nintendo Developer Portal, The Process; Unity, Console development
notas:
Glosario (conceptos cortos para la docente):
• NDA: acuerdo de confidencialidad.
• GDK: Game Development Kit de Microsoft. Es público para PC desde julio de 2021; la versión para consolas (GDKX) es solo para socios licenciados.
• GDPA: Global Developer and Publisher Agreement, el contrato de Sony que da acceso a las herramientas.
• TRC y Lotcheck: nombres de los requisitos y la revisión de Sony y de Nintendo. No son públicos.
Desarrollo de cada fila (todo verificado en fuentes oficiales):
- Microsoft (ID@Xbox): ser mayor de 18 años, firmar un NDA, estar en un país donde Microsoft opere. El GDK está en GitHub desde julio de 2021, pero el que compila para consola es solo para socios.
- Sony: registro en PlayStation Partners con un plan de proyecto; después de la aprobación y la firma del GDPA se accede a herramientas y documentación. Desde 2022, Sony presta un dev kit y un test kit a socios nuevos aprobados (a devolver en dos años).
- Nintendo: registro (mayoría de edad), aceptar NDA y términos, formulario de acceso a Switch; para publicar: acuerdo de publicación, clasificación por edad y "submit your game for review by Nintendo".
- Unity: para compilar a plataformas cerradas hace falta Unity Pro activo o una clave de plataforma que entrega el fabricante, más la aprobación de cada fabricante. No citar precios de Unity Pro (no verificados).
Error a evitar: decir que el GDK "se liberó en 2024". Fue en 2021, y solo para PC.

## 24 | Qué es público y qué no
tipo: contenido
kicker: CERTIFICACIÓN · 3 MIN
| Qué | Xbox | PlayStation | Nintendo |
| Requisitos completos | Público | NDA | NDA |
| Casos de prueba | Público | NDA | NDA |
| Terminología | Pública (parte NDA) | NDA | NDA |
| Pasos de alta | Públicos | Públicos | Públicos |
consola: Solo Xbox deja leer el reglamento antes de firmar
fuente: Microsoft, XBOX Requirements v16.4 y Test Cases (Microsoft Learn); 00-investigacion-preliminar.md, sección F
notas:
Glosario (conceptos cortos para la docente):
• XR (Xbox Requirements): requisitos que un juego debe cumplir para publicarse en Xbox. Versión 16.4, septiembre de 2026.
• Caso de prueba: procedimiento paso a paso que usa el fabricante para comprobar un requisito.
Desarrollo:
- Microsoft publica en Microsoft Learn el texto completo de los XR y sus casos de prueba, sin pedir cuenta. Es el único corpus oficial abierto de certificación de consola.
- Aun en Xbox hay partes reservadas: la lista de requisitos de terminología enlaza a una "Forbidden Terms List" marcada como tema bajo NDA. Es la prueba de que existe esa frontera.
- Sony y Nintendo publican cómo darse de alta, no qué revisan.
- Por eso en la materia usamos los XR como modelo de lo que pide un fabricante. No suponer que Sony y Nintendo piden exactamente lo mismo.
Dato que cambió en 2026: el XR-017 (clasificación por edad) se eliminó de los XR en agosto de 2026; según Microsoft, la clasificación se sigue validando al enviar el juego. No enseñarlo como requisito vigente.

## 25 | Obligatorio y recomendado
tipo: contenido
kicker: CERTIFICACIÓN · 3 MIN
comparacion: +XR (requisitos): Obligatorios, Se certifican // Sin cumplirlos, no se publica | XAG (accesibilidad): Recomendadas, Buenas prácticas // No son una lista de control
panel: ancho
fuente: Microsoft, XBOX Requirements v16.4; Microsoft, Xbox Accessibility Guidelines (índice)
notas:
Glosario (conceptos cortos para la docente):
• XAG (Xbox Accessibility Guidelines): guías de accesibilidad de Microsoft para juegos.
• Accesibilidad: que el juego pueda jugarlo la mayor cantidad posible de personas, incluidas personas con discapacidad.
Dos capas que se confunden seguido:
- Los XR son la condición para publicar: el juego se certifica contra ellos.
- Las XAG son buenas prácticas. Microsoft aclara que no están pensadas como una lista de control de cumplimiento.
- Algunas ideas aparecen en las dos capas: el XR-003 exige que el juego sea navegable con mando, y la XAG 112 recomienda que toda la UI se pueda recorrer solo con entrada digital.
Error frecuente: "si cumplo las XAG, certifico" o "la accesibilidad es un requisito de certificación". Son cosas distintas: la accesibilidad es una decisión de diseño que se toma igual.

## 26 | Seis requisitos que tocan a Asteroides
tipo: contenido
kicker: CERTIFICACIÓN · 5 MIN
| XR | Qué pide |
| 003 | Todo navegable con mando |
| 112 | Al reanudar, revisar usuario y mando |
| 115 | Mando quitado: pedir otro |
| 130 | Mismos modos en toda la generación |
| 022 | Nombres oficiales de botones |
| 074 | Avisar si se pierde la conexión |
consola: El XR-003 solo ya deja fuera al Asteroides original
fuente: Microsoft, XBOX Requirements for XBOX Games v16.4 (XR-003, XR-022, XR-074, XR-112, XR-115, XR-130)
notas:
Glosario (conceptos cortos para la docente):
• Suspender y reanudar: la consola congela el juego cuando el jugador sale al menú del sistema, y lo retoma después.
• Mando activo: el que está usando el jugador en ese momento.
• Generación: la familia de consolas de una época (Series S y Series X son la misma generación).
Desarrollo de cada fila:
- XR-003 (calidad): "On consoles, the game must be fully navigable with a controller". Incluye que el audio se comporte bien al conectar o desconectar auriculares.
- XR-112: al reanudar después de suspender, el juego tiene que validar el par usuario-mando (el jugador puede haber cambiado de perfil).
- XR-115: si se quita el mando activo, el juego tiene que permitir establecer un nuevo mando activo.
- XR-130: los mismos modos de juego en todos los modelos de la generación. Por eso el modelo más débil fija el piso (lo vimos en el bloque anterior).
- XR-022: usar la terminología oficial: "Menu button", "View button", "XBOX button", "LB". Nada de "Start" ni "Select".
- XR-074: avisar al jugador si se pierde la conectividad. Asteroides no usa red: N/A, pero hay que decirlo.
Pregunta rápida: ¿cuáles de estos cumple hoy el Asteroides original? Respuesta esperada: ninguno de los cuatro primeros. El menú depende del mouse y no hay pausa.

## 27 | Un caso de prueba público
tipo: contenido
kicker: CERTIFICACIÓN · 3 MIN
flujo: Jugando | Se sacan las pilas del mando | El juego avisa | Se conecta otro mando | La partida sigue || Caso 115-02: pasa si el juego pide un nuevo mando activo
panel: ancho
fuente: Microsoft, XBOX Requirements and Test Cases (casos 115-02 y 112-08)
notas:
Glosario (conceptos cortos para la docente):
• Caso de prueba: procedimiento paso a paso para comprobar un requisito, con un criterio claro de "pasa" o "no pasa".
Desarrollo:
- El caso 115-02 retira las pilas del mando en distintos momentos del juego (menú, partida, carga). Pasa si "the user is prompted to re-establish a new active controller".
- Otro caso público, el 112-08: suspender el juego 10 minutos, cambiar del perfil A al perfil B y reanudar.
- Estos casos sirven como plantilla del plan de pruebas del TP 4: precondición, pasos, resultado esperado.
- En el aula se pueden ejecutar con un mando en la PC, salvo lo que depende del sistema de la consola (suspender, perfiles), que queda como UNKNOWN o se prueba en la demo en Xbox.

## 28 | Del registro a la tienda
tipo: contenido
kicker: CERTIFICACIÓN · 4 MIN
flujo: Registro y NDA | Kit de desarrollo | Desarrollo | Clasificación por edad | Certificación | Tienda | Parches, también certificados
panel: ancho
fuente: Nintendo, The Process; SIE, Showing your Game to PlayStation; IARC (globalratings.com); PEGI; ESRB
notas:
Glosario (conceptos cortos para la docente):
• Clasificación por edad: etiqueta que indica para qué edades es apto el juego (PEGI en Europa, ESRB en América del Norte).
• IARC: sistema internacional de clasificación para juegos digitales. Es gratuito para el desarrollador.
• Parche: actualización de un juego ya publicado.
Recorrido genérico, armado con lo que publican los tres fabricantes:
1. Registro y NDA (ver la slide 23).
2. Kit de desarrollo: Sony los presta a socios nuevos; las condiciones de Microsoft y Nintendo no son públicas.
3. Desarrollo con el SDK del fabricante.
4. Clasificación por edad: Nintendo la pide explícitamente antes de enviar. Lo que se diseña cambia la etiqueta: PEGI tiene descriptores como "In-game purchases" y "Unrestricted communication"; la ESRB informa "interactive elements" como compras o interacción entre usuarios.
5. Certificación: el fabricante prueba el juego contra sus requisitos.
6. Material de tienda y lanzamiento. Nintendo permite autopublicar en su eShop, con precio y fecha decididos por el desarrollador.
7. Parches: también se certifican. Un error que en PC se arregla en una hora, en consola puede tardar días.
Consecuencia de diseño: el chat libre, el contenido generado por usuarios y las compras dentro del juego cambian la clasificación y suman requisitos (privacidad y comunicación). Diseñar eso cuesta más que programarlo.

## 29 | Actividad A5.3: auditar Asteroides
tipo: actividad
kicker: ACTIVIDAD · 30 MIN · GRUPOS DE 3 · O TAREA
| XR | Qué pide | Asteroides hoy (archivo:línea) | ¿Cumple? |
| 003 | | | |
| 112 | | | |
| 115 | | | |
| 130 | | | |
| 022 | | | |
| 074 | | | |
actividad: Evidencia en el código + 2 casos de prueba como el 115-02
notas:
Glosario (conceptos cortos para la docente):
• Evidencia: el archivo y la línea que demuestran por qué se cumple o no un requisito.
• N/A: no aplica, con el motivo escrito.
Consigna completa (25 min de trabajo + 5 de puesta en común):
1. Abrir `proyectos-unity/Asteroides/asteroide-final` (la versión original).
2. Para cada XR, completar qué pide (slide 26), qué hace hoy el juego con archivo y línea, y el estado: cumple, no cumple o N/A con motivo.
3. Escribir dos casos de prueba con el formato del 115-02: precondición, pasos y resultado esperado.
Respuestas esperadas:
- 003: no cumple. El botón Start no se puede apretar con mando: el EventSystem del prefab Game usa el StandaloneInputModule y no hay botón con foco inicial.
- 112 y 115: no cumple. No hay pausa ni reacción a la desconexión del mando (no hay OnApplicationPause ni onDeviceChange).
- 130: N/A en PC. En consola, cumple si el juego tiene un solo modo y lo ofrece en todos los modelos.
- 022: N/A hoy (no hay textos de botones); se vuelve obligatorio cuando se agregue la ayuda de controles.
- 074: N/A: el juego no usa red.
Si el tiempo no alcanza: pasa a tarea y es la base del checklist del TP 4.

# DECK 3 | Mando y TV a tres metros | Unidad V · Bloque 3

## 30 | Diseño según Plataforma: Consolas
tipo: portada
kicker: UNIDAD V · BLOQUE 3
- Bloque 3: Mando y TV a tres metros
- Diseño según Plataformas de Juego · Ing. Elsa Daniela Ramírez · FI – UNJu · 2026
notas:
Glosario (conceptos cortos para la docente):
• Experiencia de 10 pies: diseño de interfaz pensado para una pantalla a unos tres metros, que se usa con mando desde un sillón.
Bloque de 25 minutos de exposición más la actividad A5.4 (30 minutos, en clase o de tarea).
Idea fuerza: el mando no es "otro teclado". Cambia cómo se navega, qué se ve a distancia y quién puede jugar.
Continuidad: en el porteo a móvil separamos la intención del dispositivo. Acá la misma idea sirve para el mando, el remapeo y los mandos adaptados.

## 31 | Sin mouse, a tres metros
tipo: contenido
kicker: APERTURA · 3 MIN
- Sillón a tres metros
- Solo un mando en la mano
- Asteroides pide "Start"
- ¿Cómo lo apretás?
pregunta: ¿Qué parte de Asteroides depende del mouse?
notas:
Glosario (conceptos cortos para la docente):
• Foco: el elemento de la interfaz que está seleccionado y responde al botón de confirmar.
Relato: "Conectamos Asteroides a la TV, le damos un mando a alguien en el sillón. La nave ya se mueve con el stick, porque en el porteo a móvil le agregamos el Input System. Pero en la pantalla de inicio hay un botón Start y nadie lo puede apretar".
Respuesta esperada: el menú. El gameplay ya está desacoplado del dispositivo; la interfaz no.
Dato del código (verificado): el prefab Game de Asteroides trae un EventSystem con StandaloneInputModule (el módulo del Input Manager antiguo) y ningún botón tiene el foco al arrancar.

## 32 | Acción, no botón
tipo: contenido
kicker: MANDO · 5 MIN
diagrama: Dispositivo: Teclado, Mando, Táctil, Mando adaptado | Acción: Mover, Disparar, Pausa, Confirmar | Juego: Nave, Menús || El remapeo cambia la flecha de abajo, no el juego
- Acciones: qué quiere el jugador
- Bindings: con qué control
- Esquemas: teclado, mando, táctil
fuente: Unity, Input System, Input Bindings (control schemes, rebinding)
notas:
Glosario (conceptos cortos para la docente):
• Acción (Input Action): algo que el jugador quiere hacer, con nombre propio (Mover, Disparar).
• Binding: la asociación entre una acción y un control concreto (barra espaciadora, botón A).
• Esquema de control (Control Scheme): grupo de bindings para un tipo de dispositivo (teclado y mouse, mando, táctil).
• Mando adaptado: control diseñado para personas con discapacidad motriz (Xbox Adaptive Controller, Access Controller de PS5).
Desarrollo:
- Es la misma idea de capas del porteo a móvil, con un nombre técnico: acciones y bindings del Input System.
- Los esquemas de control usan grupos de bindings para asignar las acciones a distintos tipos de dispositivo.
- Si el juego trabaja con acciones, agregar un mando o permitir el remapeo no toca la nave: solo cambia la flecha entre dispositivo y acción.
- En Asteroides, ShipInputAdapter ya define Mover y Disparar con teclado y mando. Falta lo mismo para los menús y para la pausa.

## 33 | Remapear es accesibilidad
tipo: contenido
kicker: MANDO · 3 MIN
- Cada jugador elige sus botones
- Se guarda entre partidas
- Guía: nivel básico
fuente: Game Accessibility Guidelines ("Allow controls to be remapped / reconfigured", nivel Basic); Unity, Input System (PerformInteractiveRebinding, SaveBindingOverridesAsJson)
notas:
Glosario (conceptos cortos para la docente):
• Remapeo: que el jugador cambie qué botón hace cada acción.
• Game Accessibility Guidelines: guía colaborativa de estudios, especialistas y académicos, con niveles básico, intermedio y avanzado.
Desarrollo:
- Las Game Accessibility Guidelines ponen "permitir remapear o reconfigurar los controles" en el nivel básico de la categoría motriz: es de lo primero que se espera.
- En el Input System: PerformInteractiveRebinding() espera a que el jugador apriete el control nuevo, y SaveBindingOverridesAsJson() / LoadBindingOverridesFromJson() lo guardan y lo recuperan.
- El remapeo sirve a quien tiene una mano con menos movilidad, a quien usa un mando adaptado y a quien simplemente prefiere otra distribución.
Límite: remapear no resuelve todo. Si el juego exige mantener apretados dos botones a la vez o tocarlos muy rápido, el problema es de diseño, no de mapeo.

## 34 | Mandos especiales: mejora, no requisito
tipo: contenido
kicker: MANDO · 4 MIN
| Mando | Lo propio | En Unity sin SDK |
| DualSense | Gatillos adaptativos, hápticos | Luz y vibración en PC |
| Joy-Con 2 | Sensor de mouse, HD Rumble 2 | No |
| Xbox Adaptive | 19 entradas de 3,5 mm | Mando común |
| Access (PS5) | 4 entradas, 30 perfiles | Mando común |
consola: El juego tiene que andar con cualquier mando
fuente: SIE, Introducing DualSense; PlayStation, DualSense en PC; Nintendo, Switch 2 Tech Specs; Microsoft, Xbox Adaptive Controller; SIE, Access controller; Unity, Input System Gamepad support
notas:
Glosario (conceptos cortos para la docente):
• Gatillo adaptativo: gatillo del DualSense que cambia su resistencia según lo que pasa en el juego.
• Háptica (HD Rumble): vibración precisa que transmite texturas, no solo un temblor.
• SDK de plataforma: kit de desarrollo del fabricante; para consola está bajo NDA.
Desarrollo:
- DualSense: hápticos y gatillos adaptativos en L2 y R2. En PC, la háptica "requires a USB connection" y no funciona en Mac ni en móviles. En Unity, sin el SDK de Sony: color de la barra de luz (SetLightBarColor) y vibración simple (SetMotorSpeeds) en escritorio.
- Joy-Con 2: acelerómetro, giroscopio, sensor de mouse, HD Rumble 2 y botón C (datos oficiales de Nintendo). Sus funciones distintivas dependen del SDK de Nintendo.
- Unity aclara que la vibración de los mandos de consola conectados a su consola solo funciona instalando los paquetes de entrada de cada consola (bajo NDA).
- Xbox Adaptive Controller: 19 entradas de 3,5 mm y 2 USB, desarrollado con AbleGamers, SpecialEffect y otras organizaciones. Access Controller de PS5: 4 entradas de 3,5 mm, hasta 30 perfiles.
Regla de diseño: las funciones de un mando son una mejora opcional. Nunca pueden ser la única forma de jugar ni de recibir una información importante, porque el jugador puede usar otro mando o uno adaptado.
Aclaración sobre la columna "Mando común": no verificamos cómo ve Unity cada mando adaptado. La idea es que el juego no suponga un mando estándar.

## 35 | Glifos y nombres oficiales
tipo: contenido
kicker: MANDO · 3 MIN
- Glifo del mando que se usa
- "Menu", no "Start"
- Lista prohibida: bajo NDA
fuente: Microsoft, XBOX Required Terminology List; Valve, Steam Deck Compatibility Review
notas:
Glosario (conceptos cortos para la docente):
• Glifo: el dibujo del botón en pantalla (la A verde del mando de Xbox, el triángulo de PlayStation).
Desarrollo:
- Los glifos tienen que coincidir con el dispositivo que el jugador está usando. Valve lo exige para el sello "Verified" de Steam Deck, y es lo esperable en cualquier consola.
- Microsoft publica una lista de términos obligatorios: "Menu button", "View button", "XBOX button", "left bumper" o "LB", "vibration". Esa lista enlaza a una "Forbidden Terms List" que es un tema bajo NDA.
- En Asteroides no hay textos de botones todavía. Cuando se agregue una ayuda de controles, hay que mostrar el glifo y el nombre según el mando activo.
Error frecuente: escribir "Press Start" en una versión para Xbox. Ese botón se llama Menu.

## 36 | Texto que se lee desde el sillón
tipo: contenido
kicker: TV · 4 MIN
| Dónde | Texto mínimo |
| Consola, 1080p | 26 px |
| Consola, 4K | 52 px |
| PC, 1080p | 18 px |
| Steam Deck (a 30 cm) | 9 px |
consola: Además, escalable hasta el 200 %
fuente: Microsoft, XAG 101 Text display; Valve, Steam Deck Compatibility Review
notas:
Glosario (conceptos cortos para la docente):
• px a 1080p: altura del texto medida en píxeles cuando la pantalla tiene 1080 líneas.
Desarrollo:
- La XAG 101 recomienda, en consola, un mínimo por defecto de 26 px de altura a 1080p (52 px en 4K). En PC, 18 px a 1080p. Recomienda también que el jugador pueda escalar el texto hasta el 200 %, glifos incluidos.
- Valve pide, para Steam Deck Verified, texto legible a 12 pulgadas (unos 30 cm), con un mínimo de 9 px.
- Por qué la diferencia: la TV está a unos tres metros; la Steam Deck, en las manos.
- En Unity se mide la altura real del texto en pantalla, no el número de fontSize: depende del Canvas Scaler. La capa de consola de Asteroides hace esa cuenta (lo vemos en el bloque de la demo).

## 37 | Zona segura y foco visible
tipo: contenido
kicker: TV · 3 MIN
- Nada esencial en el 5 % del borde
- Siempre un elemento con foco
- Todo con cruceta, sin mouse
fuente: Microsoft, Designing for Xbox and TV (UWP, archivado); Microsoft, XAG 112 UI navigation
notas:
Glosario (conceptos cortos para la docente):
• Zona segura de TV: margen de la pantalla que algunas TV recortan; no conviene poner ahí información importante.
• Cruceta (D-pad): el botón en cruz del mando.
Desarrollo:
- Microsoft recomendaba, para apps en TV, dibujar solo elementos no esenciales dentro del 5 % de los bordes. La guía está archivada y es para apps UWP, no para juegos: se usa como referencia del concepto, no como requisito.
- XAG 112: la UI tiene que ser navegable solo con teclado o con la entrada digital del mando, con un orden de foco lógico y menús lineales que den la vuelta.
- Foco visible: el elemento seleccionado tiene que distinguirse a distancia. El "Selected" por defecto de Unity casi no cambia de color.
Continuidad con móvil: la zona segura de la TV es la prima de la safe area del teléfono (muescas y bordes). Mismo problema, otra causa.

## 38 | Actividad A5.4: solo con mando
tipo: actividad
kicker: ACTIVIDAD · 30 MIN · GRUPOS DE 3 · O TAREA
| Acción | Teclado | Mando | Mando adaptado |
| Mover | | | |
| Disparar | | | |
| Confirmar (menú) | | | |
| Pausa | | | |
actividad: Jugar sin mouse, mapear, bocetar el remapeo y medir el texto
notas:
Glosario (conceptos cortos para la docente):
• Boceto: dibujo a mano de la pantalla, sin implementarla.
Consigna completa (25 min de trabajo + 5 de puesta en común):
1. Abrir `asteroide-final` y jugar **sin tocar el mouse**: con mando o con teclado. Anotar dónde se traba.
2. Completar el mapa de controles. En la columna "Mando adaptado", pensar en un jugador que solo puede usar dos botones grandes.
3. Bocetar en papel la pantalla de remapeo: cómo se elige la acción, cómo se espera el botón nuevo y cómo se vuelve atrás, todo con cruceta.
4. Medir un texto del juego: con el Game view a 1920×1080, ¿llega a 26 px? (captura y regla de píxeles, o la cuenta con el Canvas Scaler).
Respuesta esperada para el paso 1: el juego no pasa de la pantalla de inicio con mando; con teclado tampoco, porque nada tiene foco.
Si el tiempo no alcanza: los pasos 3 y 4 pasan a tarea y alimentan la parte de adaptación del TP 4.

# DECK 4 | Asteroides llega a la Xbox | Unidad V · Bloque 4

## 39 | Diseño según Plataforma: Consolas
tipo: portada
kicker: UNIDAD V · BLOQUE 4
- Bloque 4: Asteroides llega a la Xbox
- Diseño según Plataformas de Juego · Ing. Elsa Daniela Ramírez · FI – UNJu · 2026
notas:
Glosario (conceptos cortos para la docente):
• Developer Mode: modo de una Xbox comercial que permite instalar y probar software propio sin publicarlo.
Bloque de 25 minutos de exposición (incluye la demo en la consola de la docente) más la actividad A5.5 (25 minutos).
Preparación antes de clase: seguir el Anexo B. La consola tiene que estar en Developer Mode, con los cuatro paquetes instalados y probados. Llevar un mando con pilas de repuesto (se usan en la demo).
Plan B si la consola no está o falla: mostrar las dos versiones en el Editor con un mando conectado a la PC (`asteroide-final` y `Asteroides-Xbox`). La idea se ve igual; lo que se pierde es la TV y el sistema de la consola.

## 40 | Compila... ¿se juega?
tipo: contenido
kicker: APERTURA · 2 MIN
- Mismo juego, dos versiones
- Original: sin cambios
- Consola: una capa encima
- Hoy, en una Xbox real
pregunta: ¿Cuál de las dos pasaría el XR-003?
notas:
Glosario (conceptos cortos para la docente):
• Versión original: Asteroides tal como quedó después del porteo a móvil.
• Capa de consola: código agregado que adapta la UI y el ciclo de vida, sin tocar el gameplay.
Relato: "Les traje Asteroides y el Platformer en dos versiones cada uno, instalados en mi Xbox. Las originales no tienen ningún cambio para consola. Las otras tienen una capa agregada. Antes de verlas, ustedes van a predecir qué pasa".
Unir con lo anterior: en la actividad A5.3 encontraron que el original no cumple el XR-003. Ahora lo vamos a ver en la TV.

## 41 | Dos caminos a la consola
tipo: contenido
kicker: XBOX · 4 MIN
| Camino | Acceso | Sirve para |
| GDK (ID@Xbox) | Socio, NDA | Publicar |
| Developer Mode | Cuenta gratuita | Probar, no publicar |
consola: Un juego en Developer Mode: 5 GB y 4 núcleos
fuente: Microsoft, Xbox Developer Mode activation; System resources for UWP apps and games; UWP on Xbox FAQ; Open a developer account (Partner Center)
notas:
Glosario (conceptos cortos para la docente):
• UWP (Universal Windows Platform): formato de aplicaciones de Windows que también corre en Xbox en Developer Mode.
• Partner Center: portal de Microsoft para desarrolladores. Abrir la cuenta individual no tiene costo.
Desarrollo:
- El camino oficial para publicar es el GDK con extensiones de Xbox, que exige ser socio (ID@Xbox), firmar NDA y usar un kit de desarrollo.
- Cualquier Xbox comercial se puede pasar a Developer Mode con la app Xbox Dev Mode y una cuenta de Partner Center, que no cobra registro (verificado el 2026-10-26 en Microsoft Learn; pide verificar la identidad).
- En Developer Mode se instalan paquetes UWP por red local. Microsoft ya no acepta juegos UWP en la tienda de Xbox: sirve para probar, no para publicar.
- Recursos de un juego UWP en la consola: hasta 5 GB de memoria, 4 núcleos exclusivos y 2 compartidos, la GPU completa. Si se instala como "app", baja a 1 GB.
- Unity 6000.3 todavía genera UWP con la familia Xbox. Que corra en la consola lo comprobamos hoy.
Límite: esto no es certificar ni usar el sistema de Xbox (usuarios, logros, guardado en la nube).

## 42 | Del proyecto a la TV
tipo: contenido
kicker: XBOX · 3 MIN
flujo: Unity: build UWP x64 | Visual Studio: paquete .msix | Device Portal: instalar | Dev Home: jugar || Sin tienda ni nube: todo por la red local
panel: ancho
fuente: PORTEO-XBOX.md; GUIA-XBOX-DOCENTE.md; Microsoft, Device Portal for Xbox
notas:
Glosario (conceptos cortos para la docente):
• Paquete .msix: archivo instalable de una aplicación de Windows, firmado con un certificado.
• Device Portal: página web que sirve la consola en Developer Mode para instalar y administrar paquetes desde la PC.
• Dev Home: la pantalla de inicio de la consola en Developer Mode.
Recorrido real que se hizo para esta clase (evidencia en PORTEO-XBOX.md):
1. Unity 6000.3 genera una solución de Visual Studio para UWP, x64, con las familias Xbox y Desktop (script BuildXbox.cs).
2. Visual Studio compila el C++ que genera IL2CPP y arma el paquete .msix firmado con un certificado de prueba.
3. Desde el navegador de la PC, en el Device Portal de la consola, se instala el paquete con su dependencia (VCLibs).
4. El juego aparece en Dev Home y se juega con el mando.
Todo lo hace un script: `proyectos-unity/Tools-Xbox/generar_builds_xbox.ps1`. Los cuatro paquetes pesan entre 28 y 38 MB.
Problema que apareció al hacerlo: faltaba el Windows SDK; sin él, Unity no genera UWP. El detalle de instalación está en el Anexo B.

## 43 | A5.5 · Predecir
tipo: actividad
kicker: ACTIVIDAD · 8 MIN · INDIVIDUAL
| Prueba | Original | Consola |
| Se abre en la Xbox | | |
| Start solo con mando | | |
| Nave con stick y A | | |
| Botón con foco visible | | |
| Menu pausa | | |
| Mando desconectado: aviso | | |
actividad: PASS o FAIL, con una razón de una línea
notas:
Glosario (conceptos cortos para la docente):
• PASS / FAIL: pasa o no pasa la prueba.
Consigna: cada alumno completa la predicción antes de ver la demo, sin mirar el código de la versión de consola. Es la parte 1 de la guía de alumnos (`unidad-05/06-guia-alumnos-de-pc-a-xbox.md`).
Pista si nadie arranca: "la nave ya se movía con mando en la versión de móvil. ¿Y el menú?".
Las respuestas esperadas (hipótesis del código) están en la tabla de la guía de la docente, paso 8. No darlas ahora.

## 44 | Demo: las dos versiones en la Xbox
tipo: demo
kicker: DEMO DE LA DOCENTE · 10 MIN
- 1. Asteroides original: Start con el mando
- 2. Asteroides de consola: foco amarillo
- 3. En partida: Menu pausa y reanuda
- 4. Sacar las pilas: aviso y pausa
- 5. Platformer: lo mismo, más rápido
notas:
Glosario (conceptos cortos para la docente):
• Overlay de pausa: capa semitransparente con un mensaje que tapa el juego mientras está en pausa.
Guion de la demo (la cámara del aula enfocando la TV, o captura del Device Portal en el proyector):
1. Abrir "Asteroides (original)". Intentar empezar con el mando. Resultado esperado según el código: no se puede, porque ningún botón tiene el foco y el módulo de UI es el antiguo. Dejar que lo vean fallar. Es el centro de la clase.
2. Abrir "Asteroides (consola)". El botón Start aparece resaltado en amarillo; con A empieza la partida.
3. Jugar, apretar Menu (≡): la partida se congela con el cartel "PAUSA". Volver a apretar: sigue.
4. Sacar las pilas del mando en plena partida: aparece "Se desconectó el control". Volver a ponerlas y apretar Menu. Es el caso de prueba 115-02 hecho en vivo.
5. Platformer original y de consola: el menú del original tampoco tiene foco; el de consola, sí, y no muestra el botón Quit.
Registrar lo que pase: los resultados reales van a la tabla del paso 8 de la guía de la docente y a PORTEO-XBOX.md. Si algo no sale como se esperaba, es un resultado válido: mostrarlo y discutirlo.
Estado al preparar estas slides: los paquetes se generaron y los tests pasan; el comportamiento en la consola era UNKNOWN hasta la primera prueba de la docente.

## 45 | Qué agregó la capa
tipo: contenido
kicker: XBOX · 3 MIN
codigo: ../../proyectos-unity/Asteroides-Xbox/Assets/Scripts/Console/ConsoleLayer.cs:144-147,156-157 ## 144–147: cambia el módulo de UI antiguo por el del Input System ; 156–157: si nada tiene foco, se lo da al botón de más arriba
panel: ancho
fuente: proyectos-unity/Asteroides-Xbox/Assets/Scripts/Console/ConsoleLayer.cs
notas:
Glosario (conceptos cortos para la docente):
• EventSystem: componente de Unity que decide qué elemento de la UI recibe la entrada.
• Input module: la pieza del EventSystem que lee los dispositivos. El StandaloneInputModule lee el Input Manager antiguo; el InputSystemUIInputModule lee el Input System.
Lectura del código (líneas reales del archivo; el método completo va de la 140 a la 158):
- 144–147: si el EventSystem tiene el módulo antiguo, lo quita y agrega el del Input System con sus acciones por defecto (navegar con cruceta y stick, confirmar con A).
- 156–157: cada cuadro, si no hay nada seleccionado (o lo seleccionado ya no está activo), selecciona el botón usable de más arriba en pantalla.
- Se instala sola al arrancar: no se tocó ninguna escena.
Lo que la capa hace además lo resume la slide siguiente: foco amarillo, pausa, texto de 26 px y sin botón Salir.
Decisión de diseño: la capa se instala sola con [RuntimeInitializeOnLoadMethod]. No se editaron escenas ni prefabs, y el gameplay (Ship.cs) es el mismo en las dos versiones.

## 46 | Original y consola, lado a lado
tipo: contenido
kicker: XBOX · 2 MIN
| Rasgo | Original | Consola |
| Menú con mando | Sin foco | Foco amarillo |
| Pausa | No existe | Menu, mando, foco |
| Texto mínimo | Sin control | 26 px a 1080p |
| Botón Salir | Visible | Oculto |
| Gameplay | Ship.cs | Ship.cs, sin cambios |
consola: Se agrega una capa; el juego no se reescribe
fuente: PORTEO-XBOX.md, sección 3; proyectos-unity/Asteroides-Xbox/Assets/Scripts/Console/ (ConsoleLayer.cs, ConsoleRules.cs, PauseState.cs, ConsoleText.cs)
notas:
Glosario (conceptos cortos para la docente):
• Foco: el elemento de la UI que recibe la entrada del mando; tiene que verse siempre.
• XAG 101: guía de accesibilidad de Xbox sobre el tamaño del texto (26 px de cuerpo a 1080p en consola).
• Capa de consola: los cinco archivos de Assets/Scripts/Console/, iguales en Asteroides y en el Platformer salvo ConsoleText.cs.
Rasgos principales de la adaptación, fila por fila (todo verificado en el código de las dos versiones):
- Menú con mando: en el original nada tiene el foco y Asteroides trae el módulo de UI del Input Manager (StandaloneInputModule), así que con el mando no se puede empezar. La capa cambia el módulo por el del Input System, da el foco al botón de más arriba y lo pinta de amarillo (XR-003 y XAG 112, vistos en los bloques 2 y 3).
- Pausa: ninguno de los dos originales tiene pausa. La capa pausa por tres motivos: botón Menu (≡) durante la partida, mando físico desconectado y pérdida de foco de la aplicación. Congela el tiempo (Time.timeScale = 0), silencia el audio y muestra un cartel. Los adaptadores de entrada dejan de leer el mando mientras dura. La pausa por mando desconectado es el primer paso hacia el XR-115 (no elige un mando activo nuevo: eso pide el GDK).
- Texto mínimo: la capa sube a 26 px a 1080p los textos más chicos (Text y, en el Platformer, también TextMesh Pro), con la misma cuenta que hace el Canvas Scaler.
- Botón Salir: solo lo tiene el Platformer (Asteroides original no tiene). En consola la aplicación la cierra el sistema, por eso la capa oculta los botones que llaman a Quit.
- Gameplay: Ship.cs y PlayerController.cs son los mismos. En los adaptadores de entrada solo se agregó SetConsolePaused.
Idea para cerrar: adaptar a consola fue sumar UI, ciclo de vida y legibilidad alrededor del juego, no reescribirlo. Es la misma estrategia que el porteo a móvil de la Unidad 4: un adaptador por plataforma y el gameplay intacto.
Límite: la tabla dice qué hace el código. Que en la TV se vea y se sienta así es lo que comprobó (o no) la demo; el tamaño real del texto en la TV no se midió.

## 47 | El error que encontraron los tests
tipo: contenido
kicker: XBOX · 2 MIN
flujo: El joystick en pantalla se oculta | Se quita su mando virtual | La capa cree que se desconectó un mando | El juego se pausa solo || Corrección: solo cuentan los mandos físicos
panel: ancho
fuente: PORTEO-XBOX.md, sección 3; ConsoleRules.cs, líneas 14–17
notas:
Glosario (conceptos cortos para la docente):
• Mando virtual: dispositivo que crea el Input System para los controles en pantalla (OnScreenStick, OnScreenButton); el juego lo ve como un gamepad.
• Mando físico: un dispositivo real; en el Input System, device.native es verdadero.
Historia real de esta adaptación:
- Los tests de Play Mode de Asteroides de consola dieron 5 fallas en la primera corrida.
- Causa: en PC y en consola, el script que oculta los controles táctiles los apaga al arrancar. Al apagarse, el joystick en pantalla quita su mando virtual. La capa lo interpretaba como "se desconectó el mando" y pausaba durante la carga.
- Corrección: solo pausa si el dispositivo es un mando y es físico (device.native). Después de corregir, los 5 tests pasaron y no hubo regresiones.
Moraleja para el TP: lo agregado para una plataforma (los controles táctiles de móvil) puede romper otra. Sin tests, este error se habría descubierto en la consola, delante del curso.

## 48 | Qué NO resuelve esta demo
tipo: contenido
kicker: XBOX · 1 MIN
- No es certificación
- Sin usuarios ni logros de Xbox
- Rendimiento: solo observado
- Nada sobre PlayStation ni Nintendo
notas:
Glosario (conceptos cortos para la docente):
• PLM (Process Lifetime Management): cómo el sistema suspende, reanuda y cierra las aplicaciones.
Desarrollo:
- No se cumplen los XR por correr en Developer Mode: certificar exige el programa de socios.
- No se usa el GDK: no hay usuarios de Xbox, logros, partidas en la nube ni el PLM real del sistema. La pausa por pérdida de foco es una aproximación con OnApplicationFocus.
- El rendimiento se observa en el Device Portal, pero 5 GB y 4 núcleos no son el hardware completo de un kit de desarrollo.
- Los requisitos de Sony y Nintendo no son públicos: no se puede decir que esta adaptación alcance para esas consolas.

## 49 | A5.5 · Comprobar y leer el código
tipo: actividad
kicker: ACTIVIDAD · 17 MIN · GRUPOS DE 3
- ¿Qué predicciones fallaron y por qué?
- Encontrar en el código las 3 pausas
- ¿Por qué Menu no pausa en un menú?
- ¿Qué cambió en Ship.cs? (pista: nada)
actividad: Guía de alumnos, partes 3 y 4
notas:
Glosario (conceptos cortos para la docente):
• PauseReason: el enum con los tres motivos de pausa (botón Menu, mando perdido, foco perdido).
Consigna: partes 3 y 4 de `unidad-05/06-guia-alumnos-de-pc-a-xbox.md`.
1. Completar la columna "Resultado" y marcar cada predicción como acertada o no, con una línea de explicación.
2. En `proyectos-unity/Asteroides-Xbox/Assets/Scripts/Console/`, responder las seis preguntas de la guía.
Respuestas esperadas:
- Tres pausas: botón Menu (MenuPressed), mando físico desconectado (OnDeviceChange) y pérdida de foco (OnApplicationFocus).
- Menu no pausa en un menú porque la capa considera que se está jugando solo si no hay ningún botón a la vista (GameplayActive).
- Ship.cs no cambió. ShipInputAdapter solo agrega SetConsolePaused, para dejar de leer el mando mientras el juego está en pausa.
Si se extiende: comparar con git los archivos de `asteroide-final` y `Asteroides-Xbox`.

# DECK 5 | El modelo más débil manda | Unidad V · Bloque 5

## 50 | Diseño según Plataforma: Consolas
tipo: portada
kicker: UNIDAD V · BLOQUE 5
- Bloque 5: El modelo más débil manda, multijugador y rendimiento
- Diseño según Plataformas de Juego · Ing. Elsa Daniela Ramírez · FI – UNJu · 2026
notas:
Glosario (conceptos cortos para la docente):
• Presupuesto de rendimiento: tiempo de cuadro, memoria y almacenamiento que el juego puede usar en un modelo de consola.
Bloque de 30 minutos de exposición más la actividad A5.6 (30 minutos, en clase o de tarea).
Idea fuerza: una limitación de hardware puede quitar un modo de juego entero, no solo bajar los gráficos. Y optimizar sin medir es adivinar.
Alcance: el multijugador en línea se da solo a nivel conceptual. Implementar netcode es otra materia.

## 51 | Dos jugadores en el sillón
tipo: contenido
kicker: APERTURA · 2 MIN
- Asteroides cooperativo
- Dos naves, una TV
- ¿Pantalla dividida?
pregunta: ¿Qué cuesta agregar un segundo jugador?
notas:
Glosario (conceptos cortos para la docente):
• Multijugador local (couch co-op): varios jugadores en la misma consola y la misma pantalla.
Relato: "El publisher pide un modo cooperativo para dos en el sillón, porque en consola se vende bien".
Respuestas esperadas: un segundo mando, una segunda nave, quizá dividir la pantalla. Casi nadie piensa en la memoria ni en el rendimiento: ahí va el bloque.

## 52 | Compartida o dividida
tipo: contenido
kicker: MULTIJUGADOR · 4 MIN
comparacion: +Pantalla compartida: Una cámara, Más barata // Los jugadores no pueden separarse | Pantalla dividida: Una cámara por jugador, Cada uno ve su zona // N cámaras: N veces el render
panel: ancho
fuente: R. Terrell, Shared-Multi-Split Screen Design (Game Developer, 2011); Unity, Player Input Manager component
notas:
Glosario (conceptos cortos para la docente):
• Pantalla dividida (split-screen): la pantalla se parte en una vista por jugador.
• Pantalla compartida: todos los jugadores en la misma vista; la cámara los encuadra a todos.
• Render: el trabajo de dibujar un cuadro.
Desarrollo:
- Pantalla compartida: una sola cámara. Es la opción natural de Asteroides, donde la acción ocurre en una sola pantalla fija. Costo bajo; límite: los jugadores no pueden alejarse.
- Pantalla dividida: cada jugador tiene su cámara y su vista. Libertad de movimiento, pero cada cámara repite el trabajo de dibujar la escena.
- Hay variantes, como la pantalla dividida dinámica, que se une cuando los jugadores están cerca (Terrell cita Bionic Commando Rearmed). Es un artículo de opinión profesional: sirve para discutir, no como dato.
Conexión con el bloque: en una consola de memoria justa, "N veces el render" puede no entrar. Es el caso de la slide 54.

## 53 | Sumar jugadores con el Input System
tipo: contenido
kicker: MULTIJUGADOR · 3 MIN
- Se une apretando un botón
- Un mando por jugador
- Pantalla dividida automática
- Límite de jugadores
fuente: Unity, Input System 1.20, Player Input Manager component; Microsoft, XR-045
notas:
Glosario (conceptos cortos para la docente):
• PlayerInputManager: componente del Input System que crea un jugador por cada mando que se une.
Desarrollo:
- El PlayerInputManager permite unirse al apretar un botón en un mando que no está asignado, por una acción o de forma manual.
- Tiene una opción de pantalla dividida que reparte el espacio entre los jugadores activos, y un límite de jugadores.
- Cada jugador recibe sus propias acciones: la idea de acción contra botón de este bloque se repite por jugador.
- Requisito público relacionado: el XR-045 (privilegios de multijugador) aclara que el privilegio de juego en línea no aplica al multijugador local en el mismo dispositivo. De ahí se infiere que jugar en el sillón no exige la suscripción en línea (INFERENCIA).
Para la práctica (opcional): la lista de videos oficial del Input System tiene uno de multijugador local con el Player Input Manager (ver fuentes del bloque en la investigación).

## 54 | Caso: Baldur's Gate 3 en Series S
tipo: contenido
kicker: MULTIJUGADOR · 4 MIN
flujo: Series S: 10 GB de memoria | Pantalla dividida: dos vistas | No entra al lanzar | Sin pantalla dividida en S | Patch 8 la agrega || XR-130: los mismos modos en toda la generación
panel: ancho
fuente: Kotaku (24-ago-2023), Wccftech (28-ago-2023), Shacknews (28-ene-2025): prensa; las fuentes primarias no se pudieron abrir
notas:
Glosario (conceptos cortos para la docente):
• Series S / Series X: los dos modelos de la generación actual de Xbox: 10 GB de memoria contra 16 GB.
• Paridad: que todos los modelos de la generación ofrezcan los mismos modos de juego.
El caso, como lo contó la prensa:
- Larian, el estudio, anunció que la versión de Series S no tendría cooperativo en pantalla dividida (declaración de Swen Vincke citada por Kotaku). La causa señalada fue la memoria.
- Phil Spencer (Xbox), citado por Kotaku, reconoció que hay funciones de Series X que no están en Series S. La cuenta oficial de Xbox, citada por Wccftech, dijo que seguirían trabajando en el tema.
- Según Shacknews, el Patch 8 agregó la pantalla dividida en Series S.
- El XR-130 exige los mismos modos de juego en toda la generación. Cómo se resolvió formalmente para BG3 no es público: decir que hubo una "excepción" es una INFERENCIA.
Advertencia: las fuentes primarias (el posteo de Vincke, la nota de Eurogamer, la página del Patch 8) no se pudieron abrir. Se cita como lo relata la prensa.
Lección: una limitación de memoria quitó un modo de juego, no solo gráficos. Por eso el diseño parte del modelo más débil.

## 55 | En línea: el modelo mental
tipo: contenido
kicker: MULTIJUGADOR · 3 MIN
| Concepto | Qué resuelve |
| Servidor con autoridad | Una sola verdad, menos trampas |
| Predicción del cliente | Respuesta inmediata |
| Interpolación | Otros jugadores sin saltos |
| Compensación de lag | Quién disparó primero |
fuente: G. Gambetta, Fast-Paced Multiplayer (partes I, II y IV)
notas:
Glosario (conceptos cortos para la docente):
• Servidor autoritativo: el servidor decide qué pasó; los clientes solo proponen.
• Latencia (lag): demora entre que el jugador actúa y el servidor se entera.
Desarrollo (nivel conceptual, sin implementar):
- Servidor con autoridad: "the one and only authority" es el servidor. Evita que cada cliente tenga su propia versión del mundo.
- Predicción del cliente y reconciliación: el cliente aplica la acción enseguida y la corrige cuando llega la respuesta del servidor.
- Interpolación: los demás jugadores se muestran un poco en el pasado para que se muevan sin saltos (la parte III de Gambetta, sobre interpolación, no se abrió: se cita el concepto desde la parte I).
- Compensación de lag: el servidor "rebobina" para decidir si un disparo acertó con lo que veía el jugador.
Fuera de alcance: rollback propio, snapshots, NAT, servidores dedicados. En Unity hay herramientas para demostrarlo (Multiplayer Play Mode, Network Simulator), no para enseñar netcode a fondo.

## 56 | ¿Cuánta latencia tolera tu juego?
tipo: contenido
kicker: MULTIJUGADOR · 3 MIN
| Tipo de acción | Tolerancia medida |
| Tiro preciso en primera persona | −35 % de precisión a 100 ms |
| Tercera persona, deportes | Sin caída hasta unos 500 ms |
| Para probar | 100, 200, 500 y 1000 ms |
fuente: M. y K. Claypool, Latency and Player Actions in Online Games (CACM, 2006); Unity, Testing multiplayer games with artificial network conditions
notas:
Glosario (conceptos cortos para la docente):
• Precisión y plazo: Claypool clasifica las acciones según cuánta precisión piden y cuánto tiempo hay para hacerlas.
• Jitter: variación de la latencia de un paquete a otro.
Desarrollo:
- Claypool y Claypool (2006) clasifican las acciones por precisión y plazo, y distinguen el modelo de avatar (primera o tercera persona) del omnipresente (estrategia). En tiro de precisión en primera persona, la precisión cae alrededor de un 35 % a 100 ms; en tercera persona y deportes no hay caída significativa hasta unos 500 ms.
- La guía de Unity para probar multijugador sugiere probar a 100, 200, 500 y 1000 ms, y advierte que probar solo con demora, sin pérdida de paquetes ni jitter, no es realista. Valores de referencia de Boss Room en escritorio: 100–150 ms y 5–10 % de pérdida.
Pregunta: ¿qué tipo de acción es disparar en Asteroides? Precisa y con plazo corto: tolera poca latencia. Un Asteroides en línea necesitaría predicción.

## 57 | Medir antes de optimizar
tipo: contenido
kicker: RENDIMIENTO · 4 MIN
flujo: Objetivo: 60 fps = 16,6 ms | Medir con el Profiler | ¿CPU o GPU? | Aislar la causa | Aplicar una técnica | Volver a medir
panel: ancho
fuente: Unity 6000.3 Manual, Profiler Highlights module y Frame Debugger; Unity, Ultimate guide to profiling Unity games (Unity 6 edition)
notas:
Glosario (conceptos cortos para la docente):
• Presupuesto de cuadro: tiempo máximo para dibujar un cuadro: 16,6 ms a 60 fps, 33,3 ms a 30 fps (es aritmética: 1000 / fps).
• CPU-bound / GPU-bound: el cuadro tarda por culpa del procesador o de la placa de video.
• Profiler: la herramienta de Unity que mide cuánto tarda cada parte del juego.
El ciclo:
1. Objetivo: elegir fps por modelo (por ejemplo, 60 en Series X y 30 en el modo más débil).
2. Medir: Profiler conectado al build, no solo en el Editor.
3. ¿CPU o GPU? El módulo Highlights marca en rojo los cuadros donde la CPU se pasa del objetivo y en amarillo los de GPU.
4. Aislar: Frame Debugger (recorre los pasos de dibujo de un cuadro), Profile Analyzer y Memory Profiler.
5. Aplicar una sola técnica (slide siguiente).
6. Volver a medir: si no mejora, se deshace.
Error frecuente: "optimizar" bajando la calidad de todo sin medir. Puede que el problema esté en la CPU y bajar texturas no cambie nada.

## 58 | Cada técnica, su problema
tipo: contenido
kicker: RENDIMIENTO · 4 MIN
| Problema | Técnica en Unity 6.3 |
| Muchas llamadas de dibujo (CPU) | GPU Resident Drawer, SRP Batcher |
| Geometría lejana | LOD Group, Mesh LOD |
| Objetos tapados | Occlusion culling |
| Memoria de texturas | Compresión, mipmaps, streaming |
| GPU que no llega | Resolución dinámica |
consola: "Dynamic batching" ya no se recomienda
fuente: Unity 6000.3 Manual: Choose a method for optimizing draw calls; GPU Resident Drawer; Static and dynamic batching; Level of detail; Occlusion culling; Introduction to mipmaps; Dynamic Resolution
notas:
Glosario (conceptos cortos para la docente):
• Draw call (llamada de dibujo): pedido de la CPU a la GPU para dibujar algo. Muchas llamadas cargan la CPU.
• LOD (nivel de detalle): versiones más simples de un objeto para cuando está lejos.
• Mipmaps: copias reducidas de una textura; ocupan un 33 % más de memoria y disco, pero se ven mejor de lejos.
Desarrollo (orden actualizado a Unity 6.3):
- Llamadas de dibujo, en URP/HDRP: primero GPU Resident Drawer (requiere Forward+ y compute shaders, no OpenGL ES), después SRP Batcher, después GPU instancing. "For most uses, dynamic batching is no longer recommended".
- Geometría: LOD Group (más flexible) y, nuevo en 6.3, Mesh LOD (reduce polígonos con poca memoria).
- Objetos tapados: occlusion culling horneado o, en URP/HDRP, por GPU.
- Texturas: compresión, mipmaps (+33 %) y Mipmap Streaming para cargar solo los niveles necesarios.
- GPU variable: Dynamic Resolution dibuja a menor resolución cuando hace falta.
Importante para la actividad: Asteroides usa el pipeline Built-in y el Platformer usa URP 2D. Las técnicas de URP no aplican a Asteroides. Elegir la técnica según el pipeline es parte del ejercicio.
Error frecuente: aplicar recetas de Unity 2019 en Unity 6 (por ejemplo, empezar por dynamic batching).

## 59 | Un juego, varios presupuestos
tipo: contenido
kicker: RENDIMIENTO · 3 MIN
| Modelo | Pantalla | Memoria |
| Switch 2 portátil | 7,9", 1920×1080 | No publicada |
| Switch 2 en dock | Hasta 3840×2160 a 60 | No publicada |
| Xbox Series S | Objetivo 1440p | 10 GB |
| Xbox Series X | 4K | 16 GB |
consola: Se diseña para el piso y se escala hacia arriba
fuente: Nintendo, Switch 2 Tech Specs; Microsoft, Xbox Series S y Series X
notas:
Glosario (conceptos cortos para la docente):
• Piso de diseño: la configuración mínima en la que el juego tiene que funcionar bien.
• Escalar: agregar resolución, efectos o detalle cuando el modelo lo permite.
Desarrollo:
- Switch 2 es una sola consola con dos presupuestos: portátil (pantalla de 7,9" a 1920×1080) y dock (hasta 3840×2160 a 60 fps). La memoria (12 GB) aparece en buscadores, pero no está en el texto oficial que se pudo leer: no usarla como dato.
- Xbox: Series S, objetivo 1440p con 10 GB; Series X, 4K con 16 GB.
- Con el XR-130 (mismos modos en toda la generación), el modelo más débil fija qué se puede ofrecer; el más potente solo mejora la imagen.
- Asteroides y el Platformer son livianos: el problema no es si corren, sino tener la medición que lo demuestre (actividad A5.6).

## 60 | Actividad A5.6: medir antes de optimizar
tipo: actividad
kicker: ACTIVIDAD · 30 MIN · GRUPOS DE 3 · O TAREA
| Medición | Asteroides | Platformer |
| Pipeline | | |
| ms por cuadro (peor) | | |
| ¿CPU o GPU? | | |
| Causa principal | | |
| Técnica elegida y por qué | | |
actividad: Captura del Profiler + presupuesto de 16,6 ms + una técnica
notas:
Glosario (conceptos cortos para la docente):
• Peor cuadro: el más lento del tramo medido; importa más que el promedio, porque es el que se siente como tirón.
Consigna completa (25 min de trabajo + 5 de puesta en común):
1. Abrir el Profiler (Window → Analysis → Profiler) y jugar un minuto de cada juego en el Editor; si hay tiempo, con un build de desarrollo conectado.
2. Anotar el peor cuadro en ms y si el problema es de CPU o de GPU (módulo Highlights).
3. Identificar la causa principal con el Profiler o el Frame Debugger.
4. Elegir UNA técnica de la slide 58 que corresponda al pipeline de cada juego y explicar por qué; no hace falta aplicarla.
Respuestas esperadas: los dos juegos entran holgados en 16,6 ms en una PC del aula. La respuesta correcta puede ser "no hace falta optimizar, y esta es la medición que lo muestra". En Asteroides, si aparece algo, suele ser la creación de objetos (asteroides y láseres): conecta con el defecto del pool del porteo a móvil.
Error a vigilar: proponer GPU Resident Drawer para Asteroides, que usa Built-in.
Si el tiempo no alcanza: pasa a tarea y es el presupuesto de rendimiento del TP 4.

# DECK 6 | Cierre de la unidad y TP 4 | Unidad V · Bloque 6

## 61 | Errores frecuentes de la unidad
tipo: contenido
kicker: CIERRE · 3 MIN
| Error | Corrección |
| "Si compila para Windows, anda en Xbox" | Paquete UWP en Dev Mode o GDK |
| "Si la nave se mueve, está listo" | Menús, foco y pausa también |
| "Accesibilidad = certificación" | XR obliga, XAG recomienda |
| "Uso los gatillos del DualSense" | Mejora opcional, nunca requisito |
| "Optimizo y después mido" | Primero medir |
| "Sony pide lo mismo que Xbox" | Sus requisitos no son públicos |
notas:
Glosario (conceptos cortos para la docente):
• Paridad: mismos modos de juego en todos los modelos de una generación.
Desarrollo de cada error, con el bloque donde se trató:
- Windows y Xbox: un .exe no se instala en una Xbox. En Developer Mode se instala un paquete UWP; para publicar hace falta el GDK (bloque 4).
- "Si la nave se mueve": el original de Asteroides lo demostró en la demo: el gameplay funcionaba y el menú no (bloques 3 y 4).
- Accesibilidad y certificación: dos capas distintas (bloque 2).
- Funciones de un mando: siempre opcionales; el jugador puede usar otro mando o uno adaptado (bloque 3).
- Medir: el ciclo medir → aislar → aplicar → volver a medir (bloque 5).
- Sony y Nintendo: solo se conocen sus pasos de alta (bloque 2).

## 62 | TP 4: dossier de plataforma, consola
tipo: contenido
kicker: TP 4 · 3 MIN · PROPUESTO
| Entregable | Sale de |
| Consola elegida, con datos y fecha | A5.2 |
| Checklist XR aplicado | A5.3 |
| Mando y UI implementados | A5.4, capa de consola |
| Plan de 4 casos de prueba | Caso 115-02 |
| Presupuesto de rendimiento medido | A5.6 |
| Qué NO resolvimos | Todo el bloque |
fuente: 03-arquitectura-unidad.md, sección 3 (PROPUESTO; peso y nota: los define la titular)
notas:
Glosario (conceptos cortos para la docente):
• Dossier de plataforma: documento del integrador con un capítulo por plataforma (móvil, consola, PC, emergentes) para el mismo juego.
Consigna (PROPUESTA; el peso en la nota y la fecha los define la titular):
- Sobre Asteroides o el 2D Platformer, el grupo entrega el capítulo "Consola" del dossier:
1. Consola elegida, justificada con al menos tres datos con fuente y fecha (A5.2).
2. Checklist de los seis XR de la slide 26, con evidencia en el código (A5.3).
3. Adaptación implementada en Unity: menús sin mouse con foco visible, pausa con Menu y al desconectarse el mando, texto de 26 px o más a 1080p. Se puede partir de la capa de consola del repo o escribirla desde cero; si se parte del repo, se explica cada parte con palabras propias.
4. Plan de pruebas con cuatro casos al estilo de los XR, ejecutados en PC con mando, con resultado PASS, FAIL o UNKNOWN y evidencia (captura o test).
5. Presupuesto de rendimiento medido (A5.6).
6. Qué no resolvieron y por qué.
Evidencia mínima: un test de Unity que pase (por ejemplo, que el menú tenga foco al cargar) y las capturas.

## 63 | Rúbrica del TP 4 (borrador)
tipo: contenido
kicker: TP 4 · 2 MIN · PROPUESTO
| Criterio | Logrado si... |
| Datos y fuentes | Cada dato con fuente y fecha |
| Requisitos | Cada XR con evidencia o N/A |
| Implementación | Funciona sin mouse, con test |
| Pruebas | 4 casos con resultado y evidencia |
| Rendimiento | Medición real, técnica justificada |
notas:
Glosario (conceptos cortos para la docente):
• Rúbrica: tabla de criterios y niveles para corregir de forma pareja.
Borrador de cuatro niveles por criterio (insuficiente, en proceso, logrado, destacado). En la slide se muestra solo el nivel "logrado".
- Datos y fuentes: insuficiente si hay datos sin fecha o fuentes inventadas; destacado si marca lo que falta (por ejemplo, Xbox sin cifras).
- Requisitos: insuficiente si dice "cumple" sin evidencia; destacado si propone cómo comprobar lo que en PC queda UNKNOWN.
- Implementación: insuficiente si necesita mouse en algún punto; destacado si agrega remapeo o glifos según el mando.
- Pruebas: insuficiente si no tiene resultado esperado; destacado si un caso es un test automático.
- Rendimiento: insuficiente si "optimiza" sin medir; destacado si muestra antes y después.
Pendiente de la titular: la equivalencia con la nota (como en la U4, D4-05) y si la defensa es oral o en video.

## 64 | Cierre de la unidad
tipo: cierre
kicker: CIERRE · 1 MIN
- La consola tiene dueño
- El dueño pone las reglas
- El modelo más débil manda
- Medir, probar, recién después afirmar
notas:
Glosario (conceptos cortos para la docente):
• Límite de plataforma: lo que el juego no puede hacer o tiene que hacer por la plataforma donde corre.
Síntesis con la pregunta de la materia, "¿quién pone el límite?":
- En móvil lo ponía el dispositivo (batería, temperatura, pulgar).
- En consola lo pone el fabricante: modelos, mandos, requisitos, certificación, tienda.
- El diseño parte del modelo más débil y de las reglas públicas, y se demuestra con mediciones y pruebas, no con opiniones.
Más adelante en la materia: el límite pasa a ser la diversidad del hardware de PC.

# DECK 7 | Anexo A: datos y fuentes | Unidad V · Anexo de consulta

## 65 | Ventas de vida: tabla completa
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

## 66 | Ventas por ejercicio fiscal
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

## 67 | Fuentes de los datos
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

## 68 | No verificado: no usar como dato
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
6. Ventas de PS5 de los tres primeros ejercicios (ver slide 66).

# DECK 8 | Anexo B: Xbox en Developer Mode, paso a paso | Unidad V · Anexo de consulta

## 69 | Antes de empezar
tipo: contenido
kicker: ANEXO B · CONSULTA
| Qué | Detalle |
| Consola | Xbox One o Series, 5 GB libres |
| Cuenta | Partner Center, individual, gratis |
| PC | Visual Studio 2022 + UWP + SDK |
| Unity | 6000.3.11f1 con soporte UWP |
| Red | La misma, mejor con cable |
consola: En Developer Mode no corren los juegos comprados
fuente: GUIA-XBOX-DOCENTE.md (sección 0); Microsoft, Getting started with UWP app development on Xbox One
notas:
Glosario (conceptos cortos para la docente):
• Windows SDK: kit de desarrollo de Windows; sin él, Unity no genera proyectos UWP.
Este anexo es la versión paso a paso, con imágenes, de `diseno-plataformas/laboratorio-adaptacion/GUIA-XBOX-DOCENTE.md`. Ante cualquier duda, manda la guía.
Sobre las imágenes (versión 3): las de la PC (slides 78 y 79) salen de datos reales, del log de la última corrida y de la carpeta del paquete. Las de la consola, el Partner Center y el Device Portal son RECREACIONES ESQUEMÁTICAS dibujadas por `scripts/capturas_xbox.py`, porque no hay capturas de la consola. Cada imagen lo dice en la franja de abajo: verde = real, naranja = recreación. Los números en círculo coinciden con los pasos de la slide. Las etiquetas exactas pueden variar con la versión del sistema de la consola.
Para reemplazar una recreación por una captura real: guardar el PNG con el mismo nombre en `imagenes/xbox/reales/` y volver a correr `capturas_xbox.py` y `build_decks.py`.
Detalle de la PC: Visual Studio 2022 con la carga de trabajo "Desarrollo de la Plataforma universal de Windows", las herramientas C++ de UWP (v143) y el Windows SDK 10.0.19041 o posterior. En la PC de la cátedra se instalaron el 2026-10-26 (SDK 10.0.26100).
Mientras la consola está en Developer Mode, los juegos y apps comerciales no corren. Se vuelve al modo normal en un minuto, sin perder nada (slide 87).

## 70 | El recorrido completo
tipo: contenido
kicker: ANEXO B · CONSULTA
| Dónde | Pasos | Slides |
| Navegador de la PC | Cuenta y activación | 70–72 |
| Consola | Developer Mode y Dev Home | 73–75 |
| Navegador de la PC | Device Portal | 76 |
| PowerShell | Generar los paquetes | 77–78 |
| Device Portal | Instalar | 79–82 |
| Consola | Jugar y medir | 83–85 |
consola: Slides 70–76: una sola vez por consola. Slides 77–85: cada vez que cambia el juego
fuente: GUIA-XBOX-DOCENTE.md, pasos 1 a 9
notas:
Glosario (conceptos cortos para la docente):
• Developer Mode: modo de la consola comercial que permite instalar paquetes propios. No es un kit de desarrollo.
La primera vez lleva más o menos una hora: el registro, la verificación de identidad y el primer reinicio son lo que más tarda. Después, reinstalar un juego lleva unos minutos.

## 71 | Paso 1 · La cuenta de desarrollador
tipo: contenido
kicker: ANEXO B · CONSULTA
- 1. storedeveloper.microsoft.com → Get started for free
- 2. Elegir Individual developer
- Verificar identidad: documento y selfie
- Entrar al Partner Center
captura: imagenes/xbox/xb-01-registro.png | Registro sin costo: entrar por storedeveloper.microsoft.com
fuente: Microsoft, Steps to open a Microsoft Store developer account
notas:
Glosario (conceptos cortos para la docente):
• Partner Center: el panel de Microsoft para desarrolladores. Acá solo se usa para activar la consola.
Detalle:
- El registro sin costo solo funciona entrando por storedeveloper.microsoft.com. Otros caminos muestran el flujo viejo, que cobraba.
- La verificación se hace desde el celular, con buena luz.
- Si el Partner Center (Apps & Games) no aparece enseguida, esperar unos 5 minutos y recargar.
- La cuenta no publica nada: solo habilita la consola.

## 72 | Paso 2 · El código en la consola
tipo: contenido
kicker: ANEXO B · CONSULTA
- Tienda de la consola: Xbox Dev Mode
- Instalarla y abrirla
- 1. Anotar el código que muestra
- No cerrar la app hasta activar
captura: imagenes/xbox/xb-02-codigo.png | La app Xbox Dev Mode muestra el código de activación
fuente: Microsoft, Xbox Developer Mode activation
notas:
Glosario (conceptos cortos para la docente):
• Código de activación: identifica a esta consola. Se ingresa una vez en el Partner Center.
El código de la imagen es de ejemplo. El real lo genera la consola.
Consola de modelo japonés: no se verificó si la app aparece con la región de Japón. Si no aparece, cambiar la región en Configuración → Sistema → Idioma y ubicación, y buscarla de nuevo.

## 73 | Paso 3 · Activar desde la PC
tipo: contenido
kicker: ANEXO B · CONSULTA
- partner.microsoft.com/xboxconfig/devices
- 1. Escribir el código
- 2. Agree and activate
- La consola muestra el progreso
captura: imagenes/xbox/xb-03-activar.png | Partner Center: activar la consola con el código
fuente: Microsoft, Xbox Developer Mode activation
notas:
Glosario (conceptos cortos para la docente):
• Activación: vincular la consola a la cuenta de desarrollador. Cada cuenta tiene un número limitado de activaciones.
Iniciar sesión con la misma cuenta del paso 1. Desde esta misma página se desactiva la consola, por ejemplo si se vende (slide 87).

## 74 | Paso 4 · Reiniciar en Developer Mode
tipo: contenido
kicker: ANEXO B · CONSULTA
- Al terminar la activación:
- 1. Switch and restart
- El reinicio tarda más de lo normal
- Al volver, abre Dev Home
captura: imagenes/xbox/xb-04-switch.png | Xbox Dev Mode al terminar la activación
fuente: Microsoft, Xbox Developer Mode activation
notas:
Glosario (conceptos cortos para la docente):
• Dev Home: la pantalla de inicio de la consola en Developer Mode. Si aparece Dev Home, la consola está en Developer Mode.
No apagar la consola durante el reinicio.

## 75 | Paso 5 · Dev Home: usuario e IP
tipo: contenido
kicker: ANEXO B · CONSULTA
- 1. Iniciar sesión con un usuario
- 2. Anotar la IP (arriba a la izquierda)
- Después: Remote Access Settings
captura: imagenes/xbox/xb-05-dev-home.png | Dev Home: usuario con sesión iniciada e IP de la consola
consola: Sin usuario con sesión iniciada, la instalación falla con 0x87e10008
fuente: GUIA-XBOX-DOCENTE.md, paso 3; Microsoft, UWP on Xbox FAQ
notas:
Glosario (conceptos cortos para la docente):
• IP: la dirección de la consola en la red local. Es la que se escribe en el navegador de la PC.
La IP de la imagen (192.168.0.50) es de ejemplo. Dev Home la muestra arriba a la izquierda. La PC y la consola tienen que estar en la misma red, mejor con cable.

## 76 | Paso 6 · Habilitar el Device Portal
tipo: contenido
kicker: ANEXO B · CONSULTA
- Home → Remote Access Settings
- 1. Enable Xbox Device Portal
- 2. Set username and password
- 3. Anotar la URL que aparece
captura: imagenes/xbox/xb-06-remote-access.png | Remote Access Settings en Dev Home
fuente: Microsoft, Device Portal for Xbox
notas:
Glosario (conceptos cortos para la docente):
• Device Portal: página web de la consola en Developer Mode. Desde la PC permite instalar y administrar paquetes, capturar la pantalla y medir el rendimiento.
Usar un usuario y una contraseña solo para esto, no los de la cuenta de Microsoft. La URL tiene la forma https://<IP>:11443.

## 77 | Paso 7 · Abrir el Device Portal en la PC
tipo: contenido
kicker: ANEXO B · CONSULTA
- Abrir la URL en el navegador
- 1. Aviso de certificado: es esperable
- 2. Avanzado → 3. Continuar a la IP
- Usuario y clave del paso 6
- Una vez: Treat UWP apps as games
captura: imagenes/xbox/xb-07-certificado.png + imagenes/xbox/xb-08-preferencias.png | Aviso del navegador · Settings → Preference Settings
fuente: Microsoft, Device Portal for Xbox; Microsoft, UWP on Xbox FAQ
notas:
Glosario (conceptos cortos para la docente):
• Certificado propio: la consola firma su página con un certificado que el navegador no conoce. Por eso avisa, y en este caso es esperable.
Detalle:
- Según el navegador y su versión, el aviso dice "Avanzado → Continuar a … (no seguro)" o "Detalles → Ir a la página web". Es lo mismo.
- "Treat UWP apps as games by default" (Settings → Preference Settings): sin esto, el paquete corre como app, con 1 GB de memoria y parte de la GPU, en lugar de 5 GB y la GPU completa. Se tilda una sola vez, antes de instalar. Si un juego ya se instaló sin esto, reinstalarlo.

## 78 | Paso 8 · Generar los paquetes en la PC
tipo: contenido
kicker: ANEXO B · CONSULTA
- 1. Cerrar Unity
- 2. PowerShell en la raíz del repositorio
- 3. Correr generar_builds_xbox.ps1
- 4. Esperar Unity y msbuild
captura: imagenes/xbox/pc-01-powershell.png | Salida real del script (26/10/2026)
fuente: proyectos-unity/Tools-Xbox/generar_builds_xbox.ps1; PORTEO-XBOX.md, sección 5
notas:
Glosario (conceptos cortos para la docente):
• Certificado de prueba: certificado autofirmado que firma el paquete; sirve para instalar en Developer Mode, no para publicar.
• Master: configuración de compilación optimizada, sin herramientas de depuración.
Comando (desde la raíz del repositorio):
powershell -ExecutionPolicy Bypass -File proyectos-unity\Tools-Xbox\generar_builds_xbox.ps1
Para algunos proyectos: agregar -Proyectos "Asteroides-Xbox,2D-Platformer-Xbox".
Qué hace el script con cada proyecto:
1. Crea el certificado de prueba en Certificados/ (no se versiona: tiene clave privada).
2. Corre Unity en batchmode con BuildXbox.Build: UWP, x64, familias Xbox y Desktop.
3. Compila con msbuild en Master x64 y arma el paquete.
4. Deja todo en Builds/Xbox-Paquete/<Nombre>_1.0.0.0_x64_Master_Test/.
Cuánto tarda: de 1 a 5 minutos de Unity y varios minutos de compilación de C++ por proyecto.
La imagen muestra solo los proyectos que terminaron en la última corrida registrada (ultima-corrida.log). Antes de la clase, comprobar que estén los cuatro paquetes.
Si falla: Logs/build-xbox.log (Unity) o Logs/build-xbox-msbuild.log (Visual Studio).

## 79 | Paso 9 · Qué archivos se suben
tipo: contenido
kicker: ANEXO B · CONSULTA
- Por cada juego, dos archivos:
- El .msix del juego
- Dependencies/x64: VCLibs x64
- El .cer, solo si el portal lo pide
- ARM, ARM64 y x86: no (la Xbox es x64)
captura: imagenes/xbox/pc-02-carpeta.png | Carpeta real del paquete de Asteroides (original)
fuente: PORTEO-XBOX.md, sección 5; Microsoft, Windows Device Portal overview
notas:
Glosario (conceptos cortos para la docente):
• Dependencia: paquete que el juego necesita para correr (acá, las bibliotecas de C++ de Visual Studio).
• .appxsym: símbolos de depuración. Sirven para leer un crash en la PC, no se instalan.
Install.ps1 y Add-AppDevPackage.ps1 son para instalar en una PC con Windows, no en la consola.
Para llevar el paquete a otra PC, copiar la carpeta completa.

## 80 | Paso 10 · Device Portal: Add
tipo: contenido
kicker: ANEXO B · CONSULTA
- Device Portal → Home
- Sección My games & apps
- 1. Add
- Se abre el asistente de instalación
captura: imagenes/xbox/xb-10-add.png | Home del Device Portal, antes de instalar
fuente: Microsoft, Windows Device Portal overview (instalar paquetes)
notas:
Glosario (conceptos cortos para la docente):
• Sideload: instalar un paquete sin pasar por la tienda. Es lo que hace el Device Portal.
Instalar de a un juego. Repetir los pasos 10 a 13 por cada paquete.

## 81 | Paso 11 · Elegir el paquete
tipo: contenido
kicker: ANEXO B · CONSULTA
- 1. Choose file → el .msix
- No elegir los .appx de Dependencies
- 2. Next
captura: imagenes/xbox/xb-11-msix.png | Asistente, primera pantalla: el paquete del juego
fuente: Microsoft, Windows Device Portal overview (instalar paquetes)
notas:
Glosario (conceptos cortos para la docente):
• .msix: el paquete de instalación de una app de Windows (UWP). Contiene el juego compilado y su manifiesto.
Según la versión del Device Portal, el asistente puede mostrar los pasos en una sola pantalla. El orden es el mismo: paquete, dependencias, instalar.

## 82 | Paso 12 · Dependencia y certificado
tipo: contenido
kicker: ANEXO B · CONSULTA
- 1. Agregar VCLibs x64 (.appx)
- Si la consola ya la tiene, la saltea
- El .cer, solo si lo pide
- 2. Start y esperar
captura: imagenes/xbox/xb-12-dependencias.png | Asistente, segunda pantalla: dependencias
fuente: GUIA-XBOX-DOCENTE.md, paso 6; Microsoft, Windows Device Portal overview
notas:
Glosario (conceptos cortos para la docente):
• VCLibs: las bibliotecas de ejecución de C++ de Visual Studio. El código de IL2CPP las necesita para correr.
Archivo: Dependencies/x64/Microsoft.VCLibs.x64.14.00.appx, junto al paquete.
Si falta la dependencia, la instalación falla. La solución es repetir este paso.

## 83 | Paso 13 · Instalado: lanzar o quitar
tipo: contenido
kicker: ANEXO B · CONSULTA
- Aparece en My games & apps
- 1. Actions → Launch
- 2. Actions → Remove, para reinstalar
captura: imagenes/xbox/xb-13-instalado.png | El juego instalado y el menú Actions
fuente: Microsoft, Device Portal for Xbox
notas:
Glosario (conceptos cortos para la docente):
• Reinstalar: el portal rechaza un paquete con el mismo nombre y versión que uno instalado. Primero se quita el viejo.
Para quitar: cerrar el juego, Actions → Remove, y volver a hacer los pasos 10 a 12.
Plan B de instalación: abrir la solución de Builds/UWP en Visual Studio, x64, Master, Remote Machine con la IP de la consola, autenticación Universal (Unencrypted Protocol), y F5. La primera vez pide el PIN que se ve en Dev Home con "Show Visual Studio pin".

## 84 | Paso 14 · Jugar con el control
tipo: contenido
kicker: ANEXO B · CONSULTA
- 1. Dev Home → elegir el juego
- Usar solo el control
- Menú, partida, pausa y fin
- Comparar original y consola
captura: imagenes/xbox/xb-14-jugar.png | Dev Home con los cuatro paquetes instalados
fuente: GUIA-XBOX-DOCENTE.md, paso 7
notas:
Glosario (conceptos cortos para la docente):
• Foco: el botón que el control tiene seleccionado. En consola tiene que verse siempre.
La idea de la prueba es comprobar qué pasa cuando no hay mouse ni teclado. También se puede lanzar desde el Device Portal (Actions → Launch).

## 85 | Paso 15 · Evidencia: captura y rendimiento
tipo: contenido
kicker: ANEXO B · CONSULTA
- 1. Device Portal → Media capture
- 2. Capture Screenshot
- 3. Performance: CPU y frame rate
- Guardar con fecha
captura: imagenes/xbox/xb-15-evidencia.png | Media capture y Performance, desde la PC
fuente: Microsoft, Device Portal for Xbox
notas:
Glosario (conceptos cortos para la docente):
• Evidencia: la captura o la medición que respalda un PASS o un FAIL.
Las capturas que se tomen acá pueden reemplazar las recreaciones de este anexo (ver notas de la slide 69).
Las capturas y mediciones van a PORTEO-XBOX.md, sección 7, con fecha.

## 86 | Paso 16 · Protocolo de prueba
tipo: contenido
kicker: ANEXO B · CONSULTA
| Prueba | Original | Consola |
| Se instala y abre | PASS? | PASS? |
| Todo el flujo con mando | FAIL? | PASS? |
| Foco visible | FAIL? | PASS? |
| Menu pausa | FAIL? | PASS? |
| Sin pilas: aviso | FAIL? | PASS? |
| Frame rate estable | Medir | Medir |
fuente: GUIA-XBOX-DOCENTE.md, paso 8 (hipótesis del código, no resultados)
notas:
Glosario (conceptos cortos para la docente):
• Hipótesis: lo que se espera según el código; se confirma o se refuta en la consola.
Los signos de pregunta son a propósito: es lo esperado, no lo observado. Al probar, reemplazar por PASS, FAIL o UNKNOWN y pasar los resultados a PORTEO-XBOX.md, sección 7, con fecha y capturas del Device Portal.
La tabla completa, con los dos juegos y diez pruebas (incluidas Quit, imagen dentro de la TV y frame rate), está en el paso 8 de la guía de la docente.

## 87 | Paso 17 · Volver al modo normal
tipo: contenido
kicker: ANEXO B · CONSULTA
- 1. Dev Home → Quick Actions
- 2. Leave developer mode
- La consola reinicia en modo normal
- Para volver: Xbox Dev Mode → Switch and restart
captura: imagenes/xbox/xb-16-salir.png | Quick Actions en Dev Home
consola: No se pierden juegos ni partidas, y no hace falta activar de nuevo
fuente: GUIA-XBOX-DOCENTE.md, paso 9; Microsoft, Xbox Developer Mode activation
notas:
Glosario (conceptos cortos para la docente):
• Desactivar: quitar la consola de la cuenta de desarrollador desde el Partner Center (por ejemplo, si se vende la consola). Es distinto de salir del Developer Mode.

## 88 | Problemas frecuentes
tipo: contenido
kicker: ANEXO B · CONSULTA
| Síntoma | Qué hacer | Slide |
| No aparece Xbox Dev Mode | Cambiar la región | 71 |
| Error 0x87e10008 | Iniciar sesión en la consola | 74 |
| No abre el Device Portal | Misma red, cable | 75 |
| Falta una dependencia | Agregar VCLibs x64 | 81 |
| "Ya está instalado" | Quitar y reinstalar | 82 |
| El juego va lento | Instalar como juego | 76 |
fuente: GUIA-XBOX-DOCENTE.md, paso 10; Microsoft, UWP on Xbox FAQ
notas:
Glosario (conceptos cortos para la docente):
• Región: configuración de país de la consola; define qué apps muestra la tienda.
Detalle:
- Unity con el error "Could not find any supported UWP SDK": falta el Windows SDK (slide 69).
- Unity avisa que el proyecto está abierto: cerrarlo y volver a correr el script (slide 78).
