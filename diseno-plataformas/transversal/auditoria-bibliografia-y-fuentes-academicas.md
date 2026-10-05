# Investigación bibliográfica: Diseño según Plataformas de Juego (U4–U7)

Fecha de consulta: 2026-10-04. Cada URL citada como "verificada" se abrió con WebFetch (YouTube vía oEmbed). Lo que no se pudo abrir se marca con **NO VERIFICADO**.
Convención: **[H]** = hecho constatado en la fuente, **[I]** = inferencia mía.

Catálogos consultados: Open Library (API search/isbn), sitio de Routledge/CRC Press (buscador), sitio Ra-Ma (fichas y materias), Google Books API (**respondió HTTP 429: no se pudo usar**), Wiley.com (el buscador no devolvió resultados legibles), Springer/Apress (redirige a login: no se pudo usar), además de búsqueda web general. WorldCat e ISBNdb no se consultaron.

---

## A) Auditoría de la bibliografía oficial

### Tabla resumen

| # | Cita del programa | Veredicto | Comentario corto |
|---|---|---|---|
| 1 | *Testing de Software*: Kaner, Falk, Nguyen. Ra-Ma, 2009 | **EXISTE CON DATOS DISTINTOS** | Existe en inglés: *Testing Computer Software*, 2.ª ed., Wiley, 1999. No se encontró edición en español ni en Ra-Ma. |
| 2 | *Practical Game Testing…*: Joe Stumpe. CRC, 2018 | **NO SE ENCONTRÓ EVIDENCIA** | No aparece en Open Library, Routledge/CRC ni en búsqueda web. |
| 3 | *Quality Assurance in Game Development*: Karl Goodman. Wiley, 2017 | **NO SE ENCONTRÓ EVIDENCIA** | En Open Library, "Karl Goodman" solo tiene novelas y un expediente judicial. |
| 4 | *Automated Testing in Game Development*: Jesse Freeman. Apress, 2020 | **NO SE ENCONTRÓ EVIDENCIA** | Jesse Freeman es un autor real (HTML5, O'Reilly/Apress 2012–2014), pero ese título no aparece. |
| 5 | *Unity Test-Driven Development*: "Example Unity Technologies", 2021 | **NO SE ENCONTRÓ EVIDENCIA** | "Example" parece texto de relleno. Unity no publica un libro con ese título; sí tiene documentación y e-books gratuitos (ver B). |
| 6 | *Designing for Mobile Games*: Steven L. Kent. CRC, 2022 | **NO SE ENCONTRÓ EVIDENCIA** | Kent es historiador de videojuegos y novelista; no figura ningún libro de diseño móvil. |
| 7 | *Programming for Graphics and Games*: John M. Zelle. Wiley, 2019 | **NO SE ENCONTRÓ EVIDENCIA** | Zelle publica *Python Programming* (Franklin, Beedle) con gráficos; no tiene ese título ni libros en Wiley. |
| 8 | *The Art of Game Design: A Book of Lenses*: Jesse Schell. CRC, 2019, 3.ª ed. | **EXISTE TAL CUAL** | En Routledge figura con fecha 27/08/2019 (en una ficha aparece "2020" como año de copyright). |
| 9 | *Game Testing: Debugging, Polishing, and Balancing*: Kim Good. CRC, 2020 | **NO SE ENCONTRÓ EVIDENCIA** | Sin resultados en Open Library, Routledge ni búsqueda web. |
| 10 | *Modern Web and HTML5 Game Development*: Gregg Tavares. CRC, 2021 | **NO SE ENCONTRÓ EVIDENCIA** | Tavares es real (autor de *WebGL Fundamentals*, recurso web gratuito), pero no figura ningún libro suyo en Open Library ni en Routledge. |

**Síntesis [I]:** de 10 entradas, solo 1 es correcta (Schell) y 1 corresponde a un libro real con datos equivocados (Kaner). Las otras 8 no aparecen en ningún catálogo consultado. Combinan autores reales o verosímiles con títulos genéricos, lo que coincide con el patrón típico de referencias generadas automáticamente. **No afirmo que no existan.** Afirmo que no se encontraron en los catálogos indicados.

### Detalle con evidencia

**1. Kaner, Falk & Nguyen**
- [H] Open Library ISBN 9780471358466 (https://openlibrary.org/isbn/9780471358466.json): *Testing Computer Software*, 2nd Edition, Wiley, 12/04/1999, 496 pp.
- [H] Open Library, búsqueda por autor "Cem Kaner" (https://openlibrary.org/search.json?author=Cem+Kaner…): ediciones de Wiley, Van Nostrand Reinhold e International Thomson (1988, 1993, 1999). Ninguna en español y ninguna de Ra-Ma.
- [H] La materia "Pruebas y verificación de software" de Ra-Ma (https://www.ra-ma.es/materia/pruebas-y-verificacion-de-software/) solo lista obras de A. J. Canosa Ferreiro.
- **Cita corregida:** Kaner, C., Falk, J., & Nguyen, H. Q. (1999). *Testing Computer Software* (2.ª ed.). Wiley. ISBN 978-0-471-35846-6.
- **Alternativas reales en español de Ra-Ma (verificadas):**
  - Izquierdo Díaz, R. (2019). *Testing de Videojuegos*. Ra-Ma. ISBN 978-84-9964-848-4, 188 pp. (https://www.ra-ma.es/libro/testing-de-videojuegos_99948/). Cubre QA, tipos de testing, reporte de bugs, testing multijugador y **testing multiplataforma (Android, iOS, consolas)**. [I] Es muy probablemente el libro que mejor reemplaza a las entradas 1, 2, 3 y 9 para un curso en español.
  - Polo Usaola, M. et al. (2012). *Técnicas combinatorias y de mutación para testing de sistemas software*. Ra-Ma. ISBN 978-84-9964-146-1, 170 pp. (https://www.ra-ma.es/libro/tecnicas-combinatorias-y-de-mutacion-para-testing-de-sistemas-software_191994/). Es testing general, no de juegos.

**2. Stumpe**
- [H] Open Library, búsqueda "practical game testing": 19 resultados, ninguno de Stumpe.
- [H] Routledge, búsqueda "game testing" (https://www.routledge.com/search?kw=game%20testing): sin Stumpe ni Good.
- Reemplazos reales: Schultz & Bryant (2016) y Ali (2023). Ver sección B.

**3. Goodman**
- [H] Open Library, autor "Karl Goodman": *Walk the Edge of Panic* (1985), *Unknown Enemy* (2006) y un expediente de la Corte Suprema. Nada sobre QA.
- [H] Open Library, búsqueda "quality assurance game development": sin coincidencia.
- No se pudo usar el buscador de Wiley.com.

**4. Freeman**
- [H] Open Library, autor "Jesse Freeman": *Introducing HTML5 Game Development* (O'Reilly, 2012), *Building HTML5 Games with ImpactJS* (O'Reilly, 2012), *Releasing HTML5 Games for Windows 8* (O'Reilly, 2013) y *HTML5 Game Development Insights* (Apress, 2014, obra colectiva). No aparece *Automated Testing…*.
- No se pudo consultar Apress/Springer (redirige a login).

**5. "Example Unity Technologies"**
- [H] Open Library, búsqueda "unity test driven development": sin coincidencia.
- [H] La página oficial de Unity "Game Development Testing and QA Best Practices" (https://unity.com/how-to/testing-and-quality-assurance-tips-unity-projects) trata UTF y TDD ("TDD is quite rare in game development") y enlaza e-books gratuitos. Ninguno se llama así.
- Reemplazo real y gratuito: documentación de Unity Test Framework 1.4 (https://docs.unity3d.com/Packages/com.unity.test-framework@1.4/manual/index.html). [H] Cubre Edit Mode y Play Mode y permite ejecutar tests "on target platforms such as Standalone, Android, iOS". Es directamente útil para U4–U6.

**6. Kent**
- [H] Open Library, autor "Steven L. Kent": *The Ultimate History of Video Games* (2001; vol. 2, 2021), *The Making of Doom III* (2004), la saga *Clone* y otros. No hay ningún libro de diseño móvil.
- [H] Routledge, búsqueda "Designing for Mobile Games": sin Kent. Sí aparecen títulos reales sobre móvil (ver B: Carman 2018, Fields 2014; también Tamer 2023 y Finley 2018, no abiertos individualmente).
- [I] Se pudo haber querido citar *The Ultimate History of Video Games* (historia, no diseño).

**7. Zelle**
- [H] Open Library, autor "John Zelle": *Python Programming: An Introduction to Computer Science* (Franklin, Beedle; 2003, 2010, 2016) y *Data Structures and Algorithms Using Python and C++*.
- [H] Open Library, búsqueda "programming for graphics and games": no aparece Zelle.
- [I] Probable confusión con *Python Programming* (usa la librería graphics.py). No es pertinente para U4–U7.

**8. Schell**
- [H] Routledge (https://www.routledge.com/The-Art-of-Game-Design-A-Book-of-Lenses-Third-Edition/Schell/p/book/9781138632059): 3.ª ed., A K Peters/CRC Press, 652 pp. El buscador muestra la fecha 27/08/2019 y la ficha muestra "2020" (copyright).
- Cita: Schell, J. (2019). *The Art of Game Design: A Book of Lenses* (3.ª ed.). CRC Press. ISBN 978-1-138-63205-9. Solo edición comercial.

**9. Good**
- [H] Open Library, búsqueda "game testing debugging polishing balancing": 0 resultados.
- [H] Routledge, búsqueda "game testing": sin Good.

**10. Tavares**
- [H] Open Library, autor "Gregg Tavares": 0 resultados.
- [H] Routledge, búsqueda "HTML5 game development": Faas (2016), Dillon (2014), Nagle (2014), David (2011, 2012). Ninguno es de Tavares.
- [H] WebGL Fundamentals (https://webglfundamentals.org/) es un recurso libre y gratuito. La página no nombra autor (la búsqueda web lo atribuye a Tavares). Reemplazo posible para U6 (web) y U7: Nagle, *HTML5 Game Engines* (CRC 2014), o Faas (CRC 2016). Ambos aparecen en el listado de Routledge, pero sus fichas no se abrieron.

---

## B) Libros reales recomendados (verificados)

| Libro | Datos verificados | Acceso | Unidades | Para qué sirve |
|---|---|---|---|---|
| Schultz, C. P. & Bryant, R. D. *Game Testing: All in One*, 3.ª ed. | Mercury Learning & Information, 2016, ISBN 978-1-942270-76-8 (búsqueda web: AbeBooks/eBay/Google Books; la ficha de De Gruyter dio error 405) | Comercial | 4–7 | Referencia central de testing de juegos: roles, métricas, plan de pruebas. **Datos parcialmente verificados** (no se abrió la ficha editorial). |
| Ali, H. H. *The Pocket Mentor for Video Game Testing* | CRC Press, 07/12/2023, 132 pp. https://www.routledge.com/The-Pocket-Mentor-for-Video-Game-Testing/Ali/p/book/9781032323978 (URL obtenida del buscador Routledge) | Comercial | 4–7 | Introducción breve al QA de juegos para alumnos. |
| Izquierdo Díaz, R. *Testing de Videojuegos* | Ra-Ma, 2019, ISBN 978-84-9964-848-4 | Comercial (en español) | 4, 5, 6 | Testing multiplataforma (Android/iOS/consolas), reporte de bugs. **Mejor reemplazo en español.** |
| Schell, J. *The Art of Game Design*, 3.ª ed. | CRC, 2019 (ver A-8) | Comercial | 4–7 | Lentes de diseño y la lente de plataforma/tecnología. |
| Fullerton, T. *Game Design Workshop: A Playcentric Approach…*, **5.ª ed.** | A K Peters/CRC, 19/04/2024, 586 pp. https://www.routledge.com/Game-Design-Workshop-A-Playcentric-Approach-to-Creating-Innovative-Games/Fullerton/p/book/9781032607009 | Comercial | 4–7 | Playtesting iterativo y prototipado. |
| Hodent, C. *The Gamer's Brain*, 1.ª ed. | Taylor & Francis/CRC, 2017, 266 pp. (Open Library ISBN 9781498775502). **La 2.ª ed. figura en Routledge como "forthcoming" (2026, 330 pp.)**: https://www.routledge.com/The-Gamers-Brain-How-Neuroscience-and-UX-Can-Impact-Video-Game-Design/Hodent/p/book/9780367638184 | Comercial | 4–7 | UX, percepción, atención, onboarding. |
| Hodent, C. *The Psychology of Video Games* | Routledge, serie *The Psychology of Everything*, 116 pp. La ficha dice **2021** (no 2020): https://www.routledge.com/The-Psychology-of-Video-Games/Hodent/p/book/9780367493134 | Comercial (breve) | 4, 7 | Ética, efectos negativos y UX. Lectura corta para alumnos. |
| Isbister, K. & Hodent, C. (eds.) *Game Usability: Advice from the Experts…*, **2.ª ed.** | CRC, 2022, 452 pp. https://www.routledge.com/Game-Usability-Advice-from-the-Experts-for-Advancing-UX-Strategy-and-Practice-in-Videogames/Isbister-Hodent/p/book/9780367619923 | Comercial | 4–7 | **Incluye capítulos de accesibilidad, móvil, VR/AR y esports** según la ficha. Muy alineado con la materia. (La 1.ª ed., Isbister & Schaffer 2008, Morgan Kaufmann, no se verificó en el catálogo editorial.) |
| Gregory, J. *Game Engine Architecture*, 3.ª ed. | CRC Press LLC, 2018, 1.240 pp. (Open Library ISBN 9781138035454). **4.ª ed. en dos volúmenes, 2026, "forthcoming"** (Vol. I: https://www.routledge.com/Game-Engine-Architecture-Volume-I-Foundations-and-Core-Engine-Systems/Gregory/p/book/9781032443089) | Comercial | 5, 6 | Hardware de consola/PC, plataformas y rendimiento. Nivel avanzado: usar capítulos puntuales. |
| Glazer, J. & Madhav, S. *Multiplayer Game Programming* | Addison-Wesley Professional, 2015, ISBN 978-0-13-403430-0 (Open Library) | Comercial | 5, 6, 7 | Redes, latencia y juego cross-platform. |
| Jerald, J. *The VR Book: Human-Centered Design for Virtual Reality* | Morgan & Claypool / ACM Books, 2015 (Open Library ISBN 9781970001129). DOI 10.1145/2792790: **la página de la ACM DL devolvió 403, NO VERIFICADO el DOI** | Comercial | 7 | Diseño VR centrado en humanos: cinetosis, interacción. |
| LaValle, S. M. *Virtual Reality* | Cambridge University Press, 2023. **PDF gratuito y legal** en http://lavalle.pl/vr/ (el autor permite descargar, imprimir y distribuir); PDF: http://lavalle.pl/vrbook.pdf (este enlace sale de la página, no se abrió por separado) | **Acceso abierto** | 7 | Percepción, tracking y latencia en VR. Nivel universitario/técnico. |
| Rogers, S. *Level Up! The Guide to Great Video Game Design* | Wiley. Ediciones de 2010, 2014 (2.ª, ISBN 9781118877166) y 2024 (ISBN 9781394298761, Open Library) | Comercial | 4–6 | Diseño práctico, controles y cámaras. [I] La edición de 2024 sería la 3.ª (Open Library la etiqueta como "First edition", así que el número de edición queda **NO VERIFICADO**). |
| Fields, T. *Mobile & Social Game Design: Monetization Methods and Mechanics*, 2.ª ed. | A K Peters/CRC, 2014, 236 pp. https://www.routledge.com/Mobile--Social-Game-Design-Monetization-Methods-and-Mechanics-Second-Edition/Fields/p/book/9781466598683 | Comercial | 4 | F2P, retención, bienes virtuales. Leer en contraste con la literatura de patrones oscuros (C-e). |
| Carman, C. *Visual Design Concepts For Mobile Games* | A K Peters/CRC, 2018, 186 pp. https://www.routledge.com/Visual-Design-Concepts-For-Mobile-Games/Carman/p/book/9781138806924 | Comercial | 4 | Arte y visual para móvil. [I] Es el libro real más cercano al inexistente "Designing for Mobile Games". |

**E-books oficiales gratuitos de Unity (verificados, descarga gratuita con formulario):**
- *Optimize your game performance for consoles and PCs in Unity (Unity 6 edition)*: https://unity.com/resources/console-pc-game-performance-optimization-unity-6 (U5, U6).
- *Optimize your game performance for mobile, XR, and the web in Unity (Unity 6 edition)*: https://unity.com/resources/mobile-xr-web-game-performance-optimization-unity-6 (U4, U6-web, U7-XR).
- *Ultimate Guide to Profiling Unity Games (Unity 6 edition)*, unos 100 pp.: https://unity.com/resources/ultimate-guide-to-profiling-unity-games-unity-6 (U4–U7).
- Contexto: el post del blog de Unity del 11/11/2024 (Krogh-Jacobsen) presenta estas guías: https://unity.com/blog/unity-6-game-optimization-guides
- Unity Test Framework (documentación): ver A-5.

---

## C) Papers académicos (fichas)

Acceso abierto según la API de Unpaywall (consultada el 2026-10-04) salvo indicación contraria.

### (a) Diseño según plataforma, ports e input

**C1.** Shen, R., Garaialde, D., & Doherty, K. (2025). Cross Platform Gaming: More Than the Sum of Its Parts? *Games: Research and Practice* (ACM). DOI 10.1145/3774417.
- Acceso: **abierto (CC-BY)**. PDF: https://dl.acm.org/doi/pdf/10.1145/3774417 (dato de Unpaywall; la ACM DL bloquea el fetch directo).
- Unidades 5, 6, 7. Experiencia de jugadores y motivaciones de desarrolladores en el juego cross-platform. Nivel intermedio.
- Uso: lectura base del debate "un juego, muchas plataformas".

**C2.** Baldauf, M., Fröhlich, P., Adegeye, F., & Suette, S. (2015). Investigating On-Screen Gamepad Designs for Smartphone-Controlled Video Games. *ACM TOMM*, 12(1s), art. 22. DOI 10.1145/2808202.
- Acceso: no verificado.
- Unidad 4. Compara cuatro diseños de gamepad táctil (Pac-Man, Super Mario Bros.). [H] "Floating joystick can reduce the glances at the device".
- Uso: caso de adaptación de controles físicos a táctiles. Se puede replicar como experimento en clase.

**C3.** Gerling, K. M., Klauser, M., & Niesenhaus, J. (2011). Measuring the impact of game controllers on player experience in FPS games. *MindTrek '11*, 83–86. DOI 10.1145/2181037.2181052.
- Acceso: no verificado.
- Unidades 5 y 6. Gamepad frente a teclado y mouse: el input cambia la experiencia.
- Uso: discusión en clase sobre consola frente a PC.

### (b) UX y playtesting

**C4.** Desurvire, H., Caplan, M., & Toth, J. A. (2004). Using heuristics to evaluate the playability of games. *CHI '04 Extended Abstracts*, 1509–1512. DOI 10.1145/985921.986102.
- Acceso: no verificado.
- Unidades 4–7. Heurísticas HEP. Nivel introductorio. Uso: checklist para evaluar el prototipo.

**C5.** Pinelle, D., Wong, N., & Stach, T. (2008). Heuristic evaluation for games: usability principles for video game design. *CHI '08*, 1453–1462. DOI 10.1145/1357054.1357282.
- Acceso: Unpaywall indica **cerrado**.
- Unidades 4–7. Diez heurísticas derivadas de reseñas de juegos. Uso: evaluación heurística grupal.

**C6.** Korhonen, H., & Koivisto, E. M. I. (2006). Playability heuristics for mobile games. *MobileHCI '06*, 9–16. DOI 10.1145/1152215.1152218.
- Acceso: Unpaywall indica **cerrado**.
- **Unidad 4.** Heurísticas específicas de móvil: interrupciones, pantalla chica, sesiones cortas. Uso: auditar un juego móvil.

### (c) Accesibilidad

**C7.** Yuan, B., Folmer, E., & Harris, F. C. Jr. (2011). Game accessibility: a survey. *Universal Access in the Information Society*, 10(1), 81–100. DOI 10.1007/s10209-010-0189-5. Publicado online en 2010.
- Acceso: Unpaywall indica **cerrado**.
- Unidades 4–7. Modelo de interacción y barreras por tipo de discapacidad. Nivel intermedio.

**C8.** *Game Accessibility Guidelines*: https://gameaccessibilityguidelines.com/
- Acceso gratuito. Colaboración entre estudios, especialistas y académicos, activa desde 2012. Niveles básico, intermedio y avanzado.
- Unidades 4–7. Uso: checklist de accesibilidad por plataforma en el TP.

**C9.** Microsoft. *Xbox Accessibility Guidelines (XAG)* v3.2 (08/06/2023; página actualizada en 08/2026): https://learn.microsoft.com/en-us/gaming/accessibility/guidelines
- Acceso gratuito.
- **Unidad 5** (guía de un fabricante de plataforma), también U6. Uso: comparar con C8.

**C10.** AbleGamers. *Includification* (2012). **El sitio oficial includification.com redirige hoy a *Accessible Player Experiences (APX)*:** https://accessible.games/accessible-player-experiences/ (22 patrones: 12 de Access y 10 de Challenge).
- **El PDF original de Includification NO se verificó en una URL oficial** (solo aparece una copia en academia.edu, no abierta).
- Recomendación: citar APX en lugar de Includification.

### (d) Testing de juegos

**C11.** Politowski, C., Petrillo, F., & Guéhéneuc, Y.-G. (2021). A Survey of Video Game Testing. *2021 IEEE/ACM Int. Conf. on Automation of Software Test (AST)*. DOI 10.1109/AST52587.2021.00018.
- Acceso abierto: arXiv 2103.06431, https://arxiv.org/abs/2103.06431
- Unidades 4–7. [H] Los desarrolladores dependen "almost exclusively" del playtesting manual. Uso: justificar por qué el testing en juegos es distinto.

**C12.** Lin, D., Bezemer, C.-P., & Hassan, A. E. (2017). Studying the urgent updates of popular games on the Steam platform. *Empirical Software Engineering*, 22(4), 2095–2126. DOI 10.1007/s10664-016-9480-2.
- Acceso: cerrado según Unpaywall. Hay PDF en el sitio del laboratorio SAIL: https://sailresearch.github.io/sail-website/data/pdfs/EMSE2016_StudyingTheUrgentUpdatesOfPopularGamesOnTheSteamPlatform.pdf (descargado, 1 MB; no pude leer el contenido para confirmar que sea la versión del autor).
- **Unidad 6 (PC/Steam).** Parches de día 0 y hotfixes. Uso: el ciclo de actualización en PC frente a la certificación de consola.

**C13.** Truelove, A., Santana de Almeida, E., & Ahmed, I. (2021). We'll Fix It in Post: What Do Bug Fixes in Video Game Update Notes Tell Us? *ICSE 2021*, 736–747. DOI 10.1109/ICSE43902.2021.00073.
- Acceso abierto: arXiv 2103.03997, https://arxiv.org/abs/2103.03997
- Unidad 6, también U5. Taxonomía de bugs (12.122 fixes, 30 juegos de Steam). Uso: clasificar bugs del propio proyecto.

**C14.** Murphy-Hill, E., Zimmermann, T., & Nagappan, N. (2014). Cowboys, ankle sprains, and keepers of quality: how is video game development different from software development? *ICSE 2014*, 1–11. DOI 10.1145/2568225.2568226.
- PDF gratuito en Microsoft Research: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/murphyhill-icse-2014.pdf (enlazado desde la ficha oficial, https://www.microsoft.com/en-us/research/publication/cowboys-ankle-sprains-and-keepers-of-quality-how-is-video-game-development-different-from-software-development/).
- Transversal. Uso: lectura de apertura sobre la reticencia al testing automatizado en juegos.

### (e) Monetización

**C15.** Zagal, J. P., Björk, S., & Lewis, C. (2013). Dark patterns in the design of games. *Proc. FDG 2013*, 39–46. SASDG, ISBN 978-0-9913982-0-1. No tiene DOI.
- Metadatos verificados en BibSLEIGH: http://bibtex.github.io/FDG-2013-ZagalB0.html
- PDF http://www.fdg2013.org/program/papers/paper06_zagal_etal.pdf: **certificado vencido, NO VERIFICADO**.
- Unidad 4, también U7. Patrones oscuros de tiempo, dinero y redes sociales.

**C16.** Zendle, D., & Cairns, P. (2018). Video game loot boxes are linked to problem gambling: Results of a large-scale survey. *PLOS ONE*, 13(11), e0206767. DOI 10.1371/journal.pone.0206767.
- Acceso abierto **gold, CC-BY**. PDF: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0206767&type=printable (vía Unpaywall).
- Unidades 4 y 5. Correlacional: no prueba causalidad [I]. Conviene enseñarlo con ese límite.

**C17.** Petrovskaya, E., & Zendle, D. (2022). Predatory Monetisation? A Categorisation of Unfair, Misleading and Aggressive Monetisation Techniques in Digital Games from the Player Perspective. *Journal of Business Ethics*, 181, 1065–1081. DOI 10.1007/s10551-021-04970-6. Online desde 2021.
- Acceso abierto **CC-BY**. PDF: https://link.springer.com/content/pdf/10.1007/s10551-021-04970-6.pdf (vía Unpaywall).
- Unidad 4. 35 técnicas agrupadas en 8 dominios, según 1.104 jugadores. Uso: grilla para analizar un juego F2P.

**C18.** King, D. L., Delfabbro, P. H., Gainsbury, S. M., Dreier, M., Greer, N., & Billieux, J. (2019). Unfair play? Video games as exploitative monetized services: An examination of game patents from a consumer protection perspective. ***Computers in Human Behavior***, 101, 131–143. DOI 10.1016/j.chb.2019.07.017.
- Ojo: la revista es *Computers in Human Behavior*, no *New Media & Society*.
- Acceso abierto **CC-BY-NC-ND**. PDF: https://www.sciencedirect.com/science/article/pii/S0747563219302602/pdf (vía Unpaywall).
- Unidad 4. Analiza patentes de monetización.

### (f) Rendimiento, FPS y experiencia

**C19.** Claypool, M., Claypool, K., & Damaa, F. (2006). The Effects of Frame Rate and Resolution on Users Playing First Person Shooter Games. *Proc. ACM/SPIE MMCN 2006* (mejor paper). DOI 10.1117/12.648609 (tomado del resultado de búsqueda de SPIE, **no abierto: NO VERIFICADO**).
- Página del autor con PDF y slides: http://web.cs.wpi.edu/~claypool/papers/fr-rez/
- Unidades 5 y 6. [H] El frame rate impacta mucho en el desempeño y el disfrute; la resolución, poco. Uso: justificar los presupuestos de FPS por plataforma.

**C20.** Claypool, M., & Claypool, K. (2009). Perspectives, frame rates and resolutions: it's all in the game. *FDG '09*, 42–49. DOI 10.1145/1536513.1536530.
- Unpaywall indica cerrado. PDF del autor: https://web.cs.wpi.edu/~claypool/papers/perspective/paper.pdf (se descargó, pero no se pudo leer el texto).
- Unidades 5 y 6.

**C21. (Extra, más actual)** Liu, S., Kuwahara, A., Scovell, J., & Claypool, M. (2023). The Effects of Frame Rate Variation on Game Player Quality of Experience. *CHI 2023*. DOI 10.1145/3544548.3580665.
- Página del autor: https://web.cs.wpi.edu/~claypool/papers/frame-variation-chi-23/
- [H] El FPS promedio predice mal la QoE; el mejor indicador es el piso del percentil 95.
- Unidades 4–6. Uso: enseñar "frame pacing" además del FPS promedio.

### (g) Cross-platform y ports
Ver C1–C3. No se encontraron otros papers académicos sólidos y verificados específicamente sobre ports.

---

## D) Videos transversales

La duración **no está verificada** en ningún caso: oEmbed no la devuelve y la página de YouTube no fue legible. Las fechas son el año del evento según el snippet de búsqueda; la fecha de subida no está verificada.

| Título (verificado por oEmbed) | Canal | Fecha | Fragmento | Concepto | Unidad | Uso |
|---|---|---|---|---|---|---|
| The Gamer's Brain: How Neuroscience and UX Can Impact Design (https://www.youtube.com/watch?v=XIpDLa585ao) | GDC Festival of Gaming | GDC 2015 (snippet) | a determinar | Percepción, atención y memoria en UX | 4–7 | Clase |
| The Gamer's Brain, Part 2: UX of Onboarding and Player Engagement (https://www.youtube.com/watch?v=Paf6B1jleCo) | GDC Festival of Gaming | GDC 2016 (snippet) | a determinar | Onboarding | 4 (móvil), 6 | Clase/consulta |
| The Gamer's Brain, Part 3: The UX of Engagement and Immersion (or Retention) (https://www.youtube.com/watch?v=CozTtfhwPX0) | GDC Festival of Gaming | GDC 2017 (snippet) | a determinar | Retención y ética | 4 | Consulta |
| Bridging the Gap Between UX Principles and Game Design (https://www.youtube.com/watch?v=73Pqsk74Jc0) | GDC Festival of Gaming | GDC 2018 (snippet), Jim Brown, Epic | a determinar | UX frente a diseño | 4–6 | Consulta |
| Building a Unified Cross-Project UI Framework (https://www.youtube.com/watch?v=VSYExV7Uz-k) | GDC Festival of Gaming | 2019 (snippet), N. Rebrova, Sybo | a determinar | Consistencia de UI entre proyectos y pantallas | 4 | Consulta |
| It's About Time: System Design for Mobile Free-to-Play (https://www.youtube.com/watch?v=tSyt0alpoyg) | GDC Festival of Gaming | no verificada | a determinar | Temporizadores y sistemas F2P móviles | 4 | Clase (contrastar con C15–C17) |
| The Accessibility in Last of Us Part II: A 3 Year Journey (https://www.youtube.com/watch?v=5HDdino-umA) | **IGDA GASIG** (no es el canal de GDC) | no verificada | a determinar | Más de 60 opciones de accesibilidad (Schatz & Gallant, Naughty Dog) | 5 | Clase |
| Introduction to Accessibility and Inclusive Design in Gaming (https://www.youtube.com/watch?v=06ydGWh_QL0) | XBOX Game Dev | no verificada | a determinar | Modelo social de la discapacidad | 5, 6 | Clase (complementa XAG) |
| Panic Button Interview: Gyro Controls in Doom & Wolfenstein II on Switch (https://www.youtube.com/watch?v=tvO7_OwOe68) | Nintendo World Report TV (entrevista, no GDC) | no verificada | a determinar | Adaptación de input en un port a Switch | 5 | Consulta |
| GDC Vault (no es YouTube): 'Witcher 3' on the Nintendo Switch: CPU & Memory Optimization (Presented by NVIDIA), Roman Lebedev, Saber Interactive (https://gdcvault.com/play/1026635/-Witcher-3-on-the) | GDC Vault | GDC 2020 | a determinar | Port: CPU, memoria y tamaño de build | 5 | Clase (técnico); **gratuito** según la ficha |
| **[ES]** Webinar: Accesibilidad en Videojuegos (https://www.youtube.com/watch?v=zzKbkCcxiBQ) | EVAD | no verificada | a determinar | Accesibilidad (según el snippet: Enrique García, Fundación ONCE; **no verificado**) | 4–7 | Consulta |
| **[ES]** Videojuegos Accesibles e Inclusivos (https://www.youtube.com/watch?v=whK04wvVGv8) | Dialogística ® | no verificada | a determinar | Accesibilidad e inclusión | 4–7 | Consulta. **Calidad no evaluada** |

No se encontró ninguna charla verificada en español sobre diseño multiplataforma o ports, y tampoco una charla GDC de Panic Button sobre el port de DOOM a Switch.

---

## E) NO VERIFICADO / pendientes

- Las 8 entradas oficiales marcadas como "no se encontró evidencia" (A-2 a A-7, A-9, A-10). Además, no se consultaron WorldCat, ISBNdb, Google Books (HTTP 429) ni los buscadores de Wiley y Apress (no se pudieron usar).
- Existencia de una traducción al español de Kaner et al.
- La ficha editorial de Schultz & Bryant 2016 (De Gruyter devolvió 405). El ISBN 978-1-942270-76-8 solo se vio en revendedores.
- DOI de *The VR Book* (10.1145/2792790): ACM DL devolvió 403.
- DOI SPIE de Claypool 2006 (10.1117/12.648609).
- PDF de Zagal et al. 2013 en fdg2013.org (certificado vencido).
- PDF de Includification en su URL oficial (hoy redirige a APX).
- Si la ACM DL ofrece hoy en acceso abierto los papers que Unpaywall marca como "cerrado" (C2–C6, C20).
- Número de edición de *Level Up!* 2024.
- Isbister & Schaffer (2008), 1.ª ed. de *Game Usability* (Morgan Kaufmann): no abierto.
- No se buscaron Brian Upton ni Ian Bogost, ni libros de monetización ética fuera de Fields 2014.
- Ninguna duración de video verificada, ni fecha de subida exacta.
- No hay charla GDC de Panic Button ni charla en español de calidad sobre multiplataforma.
