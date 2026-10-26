# Investigación Unidad 7: "Diseño según Plataformas Emergentes"

Materia: Diseño según Plataformas de Juego (UNJu). Fecha de la investigación: 2026-10-04. Motor de referencia: Unity 6000.3.11f1 (Unity 6.3 LTS).

**Método.** Cada URL de este documento se abrió con WebFetch (o con `curl` cuando el sitio tenía un certificado roto, como ENACOM). Los DOIs se verificaron en la API de Crossref (`api.crossref.org/works/<DOI>`) cuando el sitio del editor devolvía 403. Los videos de YouTube se verificaron con oEmbed. Lo que no se pudo verificar está en la sección H.

**Convenciones.**
- [HECHO] = dato textual de la fuente.
- [INFERENCIA] = conclusión mía a partir de las fuentes.
- [MARKETING] = fuente comercial con interés en el producto.
- "Gratis/Pago" indica el acceso al recurso.

**Advertencia de herramienta.** Algunas páginas que usan mucho JavaScript (Apple HIG, ARKit, soporte de Xbox) devolvieron resúmenes genéricos. En esos casos, la URL se marca como "existe/abre", pero las citas textuales **no** se toman de ahí.

---

## A) Auditoría del programa

| # | Qué dice el programa | Veredicto | Problema | Qué enseñar | Por qué | Fuente |
|---|---|---|---|---|---|---|
| A1 | "VR: Concepto de inmersión y presencia" | CORRECTO PERO INCOMPLETO | En el uso común "inmersión" y "presencia" se usan como sinónimos. En la literatura no lo son. | **Inmersión** = propiedad objetiva del sistema (qué acciones sensoriomotoras válidas soporta). **Presencia** = respuesta subjetiva. Slater (2009) la divide en *Place Illusion* (PI, "estar ahí") y *Plausibility Illusion* (Psi, "esto está pasando de verdad"). Además: cybersickness como el costo de la inmersión (LaViola 2000; SSQ de Kennedy et al. 1993). | Sin esta distinción, el alumno cree que "más gráficos = más presencia". Slater muestra que la coherencia de los eventos (Psi) importa tanto como la fidelidad. | Slater 2009 (PMC2781884); Slater & Wilbur 1997; LaViola 2000 |
| A2 | "Interacción mediante controladores VR" | CORRECTO PERO INCOMPLETO | Deja afuera hand tracking, eye+pinch (Vision Pro no tiene controladores) y locomoción. | Las modalidades de entrada son controladores, manos y mirada+pellizco. La locomoción es un tema de diseño en sí: teleport, snap turn, movimiento continuo y viñeta. Mostrar los providers de XRI 3.x (Teleportation, Snap Turn, Continuous Move/Turn, Climb, Grab Move). | La locomoción es la decisión de diseño de VR que más afecta al confort. Half-Life: Alyx ofrece 4 modos justamente por eso. | XRI 3.3 manual locomotion; Meta Locomotion Best Practices; Valve Locomotion Deep Dive; Apple "Design for spatial input" |
| A3 | "Consideraciones de performance y optimización" | REQUIERE PRECISIÓN | Así de genérico no dice qué cambia en VR respecto de la Unidad 6. | Los números duros son los requisitos de la tienda (VRC de Meta). Estrategias: frame rate sostenido, single-pass instanced, foveated rendering (fijo vs. eye-tracked), Application SpaceWarp y render scale. Hay que explicar que en VR la caída de FPS **no es solo estética: causa malestar físico**. | Conecta con la U6 (optimización) sin repetirla, porque agrega la dimensión fisiológica. | VRC.Quest.Performance.1 y .4; Unity XR graphics 6.3; Meta AppSW; GDC Vlachos 2015/2016 |
| A4 | "AR y MR: Aplicaciones actuales en videojuegos" | REQUIERE PRECISIÓN | AR, MR y XR no están definidos. "MR" hoy es en parte término de marketing: Microsoft lo usó para HoloLens/WMR y Meta para el passthrough del Quest 3. | Continuo realidad-virtualidad (Milgram & Kishino 1994). Definición operativa de AR de Azuma (1997): combina real y virtual, es interactiva en tiempo real y está registrada en 3D. XR como término paraguas (Unity, Khronos). Distinguir AR *móvil* (ARCore/ARKit, Pokémon GO) de MR *en headset* (passthrough, Scene/MRUK, First Encounters). | Sin una definición, el debate termina en nombres comerciales. Con la de Azuma, el alumno puede clasificar cualquier producto. | Azuma 1997 (PDF del autor); Unity Manual XR 6.3; Khronos OpenXR |
| A5 | "Limitaciones técnicas y de experiencia de usuario" | CORRECTO PERO INCOMPLETO | Faltan la privacidad (cámaras) y la seguridad física concreta. | Límites técnicos: tracking/SLAM (falla con poca luz o superficies sin textura), oclusión, FOV de captura, latencia de cámara (PCA: 20–40 ms), batería y peso. Límites de UX: seguridad física (Pokémon GO pide "lugar seguro, bien iluminado"; First Encounters deja un margen de 0,3 m en las paredes), fatiga de brazos, contexto social y privacidad. Por defecto Meta **no da imágenes de cámara a las apps**; desde v74 existe una API con permiso explícito. | Son limitaciones verificables con la doc oficial, no opiniones. | Niantic Help AR; Meta Passthrough; Meta PCA overview; Meta blog First Encounters |
| A6 | "Casos de uso y ejemplos destacados" | FALTA DESARROLLAR | No hay casos concretos. | Pokémon GO (AR móvil opcional; venta a Scopely por USD 3.500 M en 2025), First Encounters (MR que viene en el Quest 3), Demeo (multiplataforma, llegó a Android XR), Half-Life: Alyx, Beat Saber, SUPERHOT VR (mecánica diseñada para VR). | Cada caso ilustra una decisión de diseño distinta: AR opcional, la habitación como nivel, ritmo sin locomoción, "el tiempo se mueve cuando te movés". | Scopely; Meta Store; Steam |
| A7 | "Cloud Gaming: Principios de streaming" | CORRECTO PERO INCOMPLETO | Falta el pipeline. | Input (subida) → servidor (simulación + render) → encode (H.264/H.265/AV1) → red → decode → display. **Latencia total ≠ ping.** Jitter, pérdida de paquetes, bitrate adaptativo. Caso Stadia: cerró el 18/01/2023. | Sin el pipeline no se entiende por qué un ping de 30 ms puede terminar en más de 100 ms entre el input y lo que se ve en pantalla. [INFERENCIA, falta cifra verificada; ver H] | Chen et al. 2014; Claypool & Finkel 2014; Google blog Stadia |
| A8 | "Impacto de la latencia y ancho de banda" | CORRECTO | Bien planteado. Hay que darle números y consecuencias de diseño. | Requisitos oficiales: GeForce NOW 15/25/35/45 Mbps según la calidad y <80 ms al datacenter; Xbox 10 Mbps en móvil y 20 Mbps recomendados; PS Portal 5/7/13 Mbps. La QoE se degrada linealmente con la latencia (Claypool & Finkel). Diseño: los juegos por turnos toleran latencia; ritmo, fighting y shooters no. UI legible después de la compresión. | Así se convierte "latencia" en decisiones de diseño. | NVIDIA, xbox.com, playstation.com, Claypool |
| A9 | "Accesibilidad y democratización del gaming" | REQUIERE PRECISIÓN (simplificación) | "Democratización" presenta como hecho algo que es parcial: baja la barrera de **hardware** pero sube la de **red**, la de suscripción y la de disponibilidad regional. | Datos de ENACOM: velocidad media de bajada en 2026-T2 de **264,56 Mbps a nivel nacional, pero 101,71 Mbps en Jujuy** (CABA 372,42). PS Plus cloud en Portal **no está disponible en Argentina** (solo CA, EE. UU., JP y 27 países europeos). Xbox Cloud sí está desde 2022. GeForce NOW llega vía ABYA, con nivel gratuito y anuncios. El ancho de banda no garantiza baja latencia: importa la distancia al datacenter. | Ejercicio situado en Jujuy, con datos oficiales. Evita el discurso de marketing. | ENACOM; PlayStation support; Xbox Wire 2022; ABYA |
| A10 | "Plataformas Web y HTML5" | DESACTUALIZADO / impreciso | "HTML5" es un paraguas de marketing de ~2010–2014. Hoy el stack real es HTML + JS/TypeScript + WebAssembly + WebGL 2 / **WebGPU** + Web Audio (+ WebXR). Además, Unity renombró su plataforma "WebGL" a **"Web"**. | Nombrar las tecnologías concretas. WebGPU está disponible por defecto en Chrome/Edge 113+ (Win/macOS/ChromeOS), Android 121+, Firefox 141 (Windows) y Safari 26 (2025). Todavía no en Linux, y MDN lo marca como "Limited availability". En Unity 6.3 el backend WebGPU es **experimental**. | El término viejo esconde las restricciones reales (WASM, sin threads en C#, sin sockets, etc.). | Unity blog 2023; Unity Manual 6.3; web.dev 2025; MDN |
| A11 | "Ventajas: accesibilidad multiplataforma, sin instalación" | CORRECTO PERO INCOMPLETO | "Sin instalación" no quiere decir "sin descarga". El tamaño inicial es crítico. | Poki recomienda ≤5 MB iniciales y 8 MB en total, y advierte que los jugadores se van si la carga supera ~10 s. CrazyGames pide ≤50 MB iniciales (≤20 MB para la home móvil). Según Poki, Unity sin optimizar pesa ~11 MB. Unity: Brotli vs. Gzip. | Conecta "sin instalación" con la optimización de build (U6). | Poki docs; CrazyGames docs; Unity webgl-deploying |
| A12 | "Restricciones: rendimiento y limitaciones gráficas" | CORRECTO PERO INCOMPLETO | No son solo gráficas. | Unity Web: sin multithreading en C#, sin sockets IP/System.Net, heap contiguo de hasta 4 GB, GC solo al final del frame, audio bloqueado hasta un gesto del usuario (política de autoplay), sin micrófono, física no determinista entre plataformas, sin Reflection.Emit. Godot 4: C# no exporta a web. Accesibilidad: `<canvas>` "es solo un bitmap" para las ayudas técnicas (MDN). | Son restricciones de plataforma que obligan a cambiar el diseño (pantalla "click to start", sin UI que dependa de lectores de pantalla). | Unity technical overview/audio/memory; Chrome autoplay; Godot docs; MDN canvas |
| A13 | "Herramientas y frameworks más usados" | FALTA DESARROLLAR | Sin lista. "Más usados" no está respaldado por ninguna fuente. | Mostrar categorías, no un ranking: 2D JS (Phaser 4, MIT; PixiJS 8 con WebGPU), 3D JS (Three.js, Babylon.js 9, PlayCanvas MIT con WebGPU), motores con export web (Unity Web, Godot, Defold gratis, Construct). Poki compara 14 motores por tamaño inicial. | No hay datos públicos confiables de "más usados". Decirlo así evita inventar. | Sitios oficiales; Poki web-engine guide |
| A14 | "Tendencias: Integración de IA y experiencias adaptativas" | CONFUSO / vago | "IA" mezcla IA de juego clásica (FSM, behaviour trees, DDA), IA generativa en la *producción* (assets, código) e IA generativa en *runtime* (NPCs con LLM). | Separar las tres. DDA es existente desde hace décadas (Hunicke 2005; Zohaib 2018). GenAI en la producción ya es existente y controvertida: GDC 2026 informa 36 % de uso personal y 52 % que cree que tiene impacto negativo. Steam exige divulgarla desde el 10/01/2024 (Pre-Generated vs. Live-Generated). Unity AI (Assistant/Generators, desde 6.2). NPCs con LLM en runtime: emergente (NVIDIA ACE, [MARKETING]). | Sin separar, el alumno confunde ChatGPT con la IA de los enemigos. | GDC 2026; Game Developer (Valve); Unity docs; NVIDIA ACE |
| A15 | "Hibridación entre plataformas físicas y virtuales" | CONFUSO | Puede leerse de dos formas: (a) mundo físico + virtual (AR/MR, location-based) o (b) híbrido de *hardware* (Switch 2, Steam Deck, cross-play y cross-progression). | Enseñar ambas, separadas. (a) es AR/MR de la sección 2. (b) incluye consolas híbridas (Switch 2, 5/6/2025, 3,5 M en 4 días), PC handheld (Steam Deck; GDC 2026: 28 % desarrolla para Steam Deck) y Xbox Cloud en TVs/Quest. | Evita la ambigüedad y conecta con U1–U5 (plataformas). | Nintendo IR; GDC 2026; xbox.com |
| A16 | "Posibilidades de expansión del metaverso y ecosistemas interactivos" | DESACTUALIZADO / término de marketing | "Metaverso" fue el término central del rebranding de Meta (2021). Hoy la fuente primaria muestra un giro: en el call del Q4 2025, Meta dice que dirige "most of our investment towards glasses and wearables" y quiere que Horizon sea un éxito *en móvil*. Reality Labs perdió **USD 19.193 M** en 2025 (17.729 M en 2024). | Reformular como "plataformas sociales persistentes y ecosistemas UGC" (Roblox, Fortnite Creative, Horizon) y tratar "metaverso" como **especulación/visión corporativa**, con datos financieros reales. | Hechos primarios en lugar de hype. Enseña a leer fuentes. | Meta Q4 2025 Exhibit 99.1 y transcript |
| A17 | (ausente) | FALTA UN TEMA IMPORTANTE | No hay estándares ni portabilidad. | **OpenXR** (Khronos, v1.1) como capa común. En Unity: XR Plug-in Management + providers (OpenXR, OpenXR: Meta, OpenXR: Android XR, visionOS, ARKit, ARCore). Es el equivalente XR de la "abstracción de plataforma" de U1–U5. | Muestra por qué un juego XR puede portarse (Demeo: "most commercially available platforms"). | Khronos OpenXR; Unity xr-support-packages 6.3; Android Dev Blog |
| A18 | (ausente) | FALTA UN TEMA IMPORTANTE | Faltan salud, seguridad y privacidad como requisitos de plataforma. | Cybersickness (SSQ como instrumento), clasificaciones de confort, datos de cámara como "Device User Data" (Meta) y edad mínima o cuentas adultas (PS Portal cloud solo para cuentas adultas). | Son requisitos de certificación o tienda, en el mismo espíritu de U5/U6. | Meta PCA; PlayStation support; Kennedy 1993 |
| A19 | (ausente) | FALTA UN TEMA IMPORTANTE | Faltan el estado del hardware y su fecha (para no enseñar especulación como presente). | Línea de tiempo verificada: Vision Pro (2/2/2024, USD 3.499), Android XR (anunciado el 12/12/2024), Galaxy XR (21/10/2025, USD 1.799,99, el primer dispositivo Android XR), Quest 3/3S, Switch 2 (5/6/2025). | Ancla "emergente" con fechas. | Apple Newsroom; blog.google; Samsung Mobile Press; Nintendo |

---

## B) Fichas (45)

> Nivel: I = introductorio, M = medio, A = avanzado. Confiabilidad: Alta (oficial/académica revisada), Media (profesional/prensa especializada), Baja (blog). O = obligatorio, C = complementario.

### B.1 VR: presencia, inmersión, cybersickness

**F01**
- **Título:** Place illusion and plausibility can lead to realistic behaviour in immersive virtual environments
- **Autor:** Mel Slater
- **Tipo:** Paper de revista (Phil. Trans. R. Soc. B 364(1535):3549–3557)
- **Fecha:** 12/2009
- **URL:** https://pmc.ncbi.nlm.nih.gov/articles/PMC2781884/
- **DOI:** 10.1098/rstb.2009.0138
- **Tema:** Inmersión vs. presencia (PI/Psi)
- **Concepto:** La inmersión es una propiedad del sistema; PI es "the strong illusion of being in a place in spite of the sure knowledge that you are not there"; Psi es "the illusion that what is apparently happening is really happening"
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Base teórica de la clase 1
- **Obligatorio/Complementario:** **O**
- **Verificación:** PMC abierto (Gratis, acceso abierto). Royal Society devolvió 403.

**F02**
- **Título:** A Framework for Immersive Virtual Environments (FIVE): Speculations on the Role of Presence in Virtual Environments
- **Autor:** M. Slater & S. Wilbur
- **Tipo:** Paper (Presence 6(6):603–616)
- **Fecha:** 12/1997
- **URL:** https://api.crossref.org/works/10.1162/pres.1997.6.6.603
- **DOI:** 10.1162/pres.1997.6.6.603
- **Tema:** Definición de inmersión
- **Concepto:** Origen de la distinción inmersión/presencia
- **Nivel:** A
- **Confiabilidad:** Alta
- **Uso en clase:** Cita histórica
- **Obligatorio/Complementario:** C
- **Verificación:** Metadatos verificados en Crossref. Texto completo: pago (MIT Press). Sin copia libre verificada.

**F03**
- **Título:** A Discussion of Cybersickness in Virtual Environments
- **Autor:** Joseph J. LaViola Jr.
- **Tipo:** Paper (ACM SIGCHI Bulletin 32(1):47–56)
- **Fecha:** 01/2000
- **URL:** https://cs.brown.edu/people/jlaviola/pubs/cybersick.pdf
- **DOI:** 10.1145/333329.333344
- **Tema:** Cybersickness
- **Concepto:** Abstract: el usuario suele estar quieto pero tiene "a compelling sense of self motion through moving visual imagery". Teorías: conflicto sensorial, inestabilidad postural, veneno
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Por qué la locomoción continua marea
- **Obligatorio/Complementario:** **O**
- **Verificación:** PDF descargado del sitio del autor (Brown) y texto extraído (Gratis). Crossref confirma los metadatos.

**F04**
- **Título:** Simulator Sickness Questionnaire: An Enhanced Method for Quantifying Simulator Sickness
- **Autor:** R. S. Kennedy, N. E. Lane, K. S. Berbaum, M. G. Lilienthal
- **Tipo:** Paper (Int. J. Aviation Psychology 3(3):203–220)
- **Fecha:** 07/1993
- **URL:** https://api.crossref.org/works/10.1207/s15327108ijap0303_3
- **DOI:** 10.1207/s15327108ijap0303_3
- **Tema:** Medición del malestar
- **Concepto:** SSQ: instrumento estándar (16 síntomas, 3 subescalas: náusea, oculomotor, desorientación. Este detalle sale del resumen de búsqueda, no lo leí en el paper)
- **Nivel:** A
- **Confiabilidad:** Alta
- **Uso en clase:** Mostrar que "marea" se mide
- **Obligatorio/Complementario:** C
- **Verificación:** Crossref verificado. Texto: pago (T&F 403).

**F05**
- **Título:** Virtual Reality Sickness: A Review of Causes and Measurements
- **Autor:** E. Chang, H. T. Kim, B. Yoo
- **Tipo:** Review (IJHCI 36(17):1658–1682)
- **Fecha:** 2020 (online 2/7/2020)
- **URL:** https://api.crossref.org/works/10.1080/10447318.2020.1778351
- **DOI:** 10.1080/10447318.2020.1778351
- **Tema:** Causas del malestar
- **Concepto:** Causas agrupadas en hardware, contenido y factores humanos
- **Nivel:** A
- **Confiabilidad:** Alta
- **Uso en clase:** Lectura para quien quiera profundizar
- **Obligatorio/Complementario:** C
- **Verificación:** Crossref verificado. Pago.

### B.2 VR: performance, plataforma, Unity

**F06**
- **Título:** VRC.Quest.Performance.1
- **Autor:** Meta
- **Tipo:** Requisito oficial de tienda
- **Fecha:** Vigente al 10/2026
- **URL:** https://developers.meta.com/horizon/resources/vrc-quest-performance-1/
- **Tema:** Frame rate mínimo
- **Concepto:** "The app must run at an allowed refresh rate and maintain a rendering rate (fps) of at least 60 fps". Refresh permitidos para apps interactivas: 72/80/90/96/100/120 Hz. Con AppSW se puede renderizar a la mitad del refresh
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Número citable; comparar con el "30/60 fps" de consolas
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK. Gratis. **Corrige la premisa de "72 fps mínimo"** (ver E).

**F07**
- **Título:** Meta Quest VRC guidelines (índice)
- **Autor:** Meta
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://developers.meta.com/horizon/resources/publish-quest-req/
- **Tema:** Certificación de tienda XR
- **Concepto:** Performance.3: gráficos con head tracking en ≤4 s o un indicador de carga. Performance.4: render scale ≥85 % (recomendado)
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Paralelo con la certificación de consolas (U5)
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F08**
- **Título:** Application SpaceWarp (Unity)
- **Autor:** Meta
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://developers.meta.com/horizon/documentation/unity/unity-asw/
- **Tema:** Optimización VR
- **Concepto:** Renderizar a la mitad de la frecuencia con motion vectors. "up to 70 percent additional compute". Requiere Vulkan, URP con soporte y Unity 6000.0.9f1+
- **Nivel:** A
- **Confiabilidad:** Alta (cifra de Meta = [MARKETING] técnico)
- **Uso en clase:** Ejemplo de técnica exclusiva de plataforma
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F09**
- **Título:** Locomotion Best Practices
- **Autor:** Meta
- **Tipo:** Guía de diseño oficial
- **Fecha:** Vigente
- **URL:** https://developers.meta.com/horizon/design/locomotion-best-practices/
- **Tema:** Confort y locomoción
- **Concepto:** "Keep acceleration events brief and infrequent"; viñetas; blinks, snap turns, teleports. Presets Recommended/Comfortable/Advanced
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Checklist de diseño
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F10**
- **Título:** Comfort (Meta design)
- **Autor:** Meta
- **Tipo:** Guía oficial
- **Fecha:** Vigente
- **URL:** https://developers.meta.com/vr/design/comfort/
- **Tema:** Confort en MR/VR
- **Concepto:** "Motion sickness can occur when there is a mismatch between what the user sees and how they move"
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Cita breve
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F11**
- **Título:** XR Interaction Toolkit: Locomotion
- **Autor:** Unity
- **Tipo:** Doc oficial (XRI 3.3)
- **Fecha:** Vigente
- **URL:** https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.3/manual/locomotion.html
- **Tema:** Implementación de locomoción
- **Concepto:** Providers: Teleportation, Snap Turn, Continuous Turn/Move, Grab Move, Two-Handed Grab Move, Climb, Gravity; Locomotion Mediator
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Demo en Unity 6.3
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F12**
- **Título:** XR Interaction Toolkit (página del paquete en el Manual 6.3)
- **Autor:** Unity
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.xr.interaction.toolkit.html
- **Tema:** Versión vigente
- **Concepto:** Versión released para 6000.3: **3.3.2**; las 3.x posteriores son compatibles
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Fijar la versión del proyecto
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F13**
- **Título:** Tunneling Vignette Controller
- **Autor:** Unity
- **Tipo:** Doc oficial (XRI 3.1)
- **Fecha:** Vigente
- **URL:** https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.1/manual/tunneling-vignette-controller.html
- **Tema:** Viñeta de confort
- **Concepto:** "a comfort mode option intended to mitigate motion sickness in VR"
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Demo
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK. La URL equivalente de la 3.3 dio 404 (ver H).

**F14**
- **Título:** XR graphics (Unity 6.3), incluye Foveated rendering
- **Autor:** Unity
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/xr-graphics.html y https://docs.unity3d.com/6000.3/Documentation/Manual/xr-foveated-rendering.html
- **Tema:** Rendering XR
- **Concepto:** Foveated: fijo vs. eye-tracked. Multiview Render Regions, tile-based rendering, resolution control
- **Nivel:** M/A
- **Confiabilidad:** Alta
- **Uso en clase:** Diapositiva de técnicas
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F15**
- **Título:** Stereo rendering (single-pass instanced)
- **Autor:** Unity
- **Tipo:** Doc oficial 6.3
- **Fecha:** Vigente
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/SinglePassStereoRendering.html
- **Tema:** Rendering estéreo
- **Concepto:** Single-pass instanced "significantly decreases CPU usage and slightly decreases GPU usage compared to the multi-pass mode"
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Explicar el costo de "dos ojos"
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F16**
- **Título:** XR packages (Unity 6.3)
- **Autor:** Unity
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/xr-support-packages.html
- **Tema:** Ecosistema de plug-ins
- **Concepto:** Providers: ARKit, ARCore, OpenXR, OpenXR: Meta, OpenXR: Android XR, visionOS, PS VR2 (solo devs registrados), HoloLens. PolySpatial visionOS requiere suscripción Pro/Enterprise
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Mapa de plataformas XR
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK. Dato de pago: PolySpatial requiere Pro.

**F17**
- **Título:** Unity Manual: XR (6.3)
- **Autor:** Unity
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/XR.html
- **Tema:** Definición de XR
- **Concepto:** XR es paraguas de VR ("simulates a self-contained environment"), MR ("combines its own environment with the user's real-world environment") y AR ("layers content over a view of the real world")
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Definiciones de trabajo
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F18**
- **Título:** OpenXR (página oficial)
- **Autor:** Khronos Group
- **Tipo:** Estándar
- **Fecha:** Vigente (OpenXR 1.1)
- **URL:** https://www.khronos.org/openxr/
- **Tema:** Portabilidad XR
- **Concepto:** "royalty-free, open standard that provides a common set of APIs for developing XR applications"
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Tema faltante A17
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK. Paquete Unity OpenXR **1.16.1** released para 6.3 (Manual com.unity.xr.openxr).

**F19**
- **Título:** Choose and configure XR provider plug-ins (6.3)
- **Autor:** Unity
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/xr-configure-providers.html
- **Tema:** XR Plug-in Management
- **Concepto:** Cada provider se habilita en Project Settings > XR Plug-in Management
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Práctica
- **Obligatorio/Complementario:** C
- **Verificación:** Aparece en el resultado de búsqueda; **no se le hizo fetch directo** (la URL está en la búsqueda y es del mismo árbol que F16. Ver H si se exige rigor total).

### B.3 AR / MR

**F20**
- **Título:** A Survey of Augmented Reality
- **Autor:** Ronald T. Azuma
- **Tipo:** Paper (Presence 6(4):355–385)
- **Fecha:** 08/1997
- **URL:** https://ronaldazuma.com/papers/ARpresence.pdf
- **DOI:** 10.1162/pres.1997.6.4.355
- **Tema:** Definición de AR
- **Concepto:** AR = "1) Combines real and virtual 2) Interactive in real time 3) Registered in 3-D". Excluye el cine ("Jurassic Park") porque no es interactivo
- **Nivel:** I/M
- **Confiabilidad:** Alta
- **Uso en clase:** Definición obligatoria, en clase con ejercicio de clasificación
- **Obligatorio/Complementario:** **O**
- **Verificación:** PDF del sitio del autor, texto extraído (Gratis, copia del autor).

**F21**
- **Título:** A Taxonomy of Mixed Reality Visual Displays
- **Autor:** P. Milgram & F. Kishino
- **Tipo:** Paper (IEICE Trans. Inf. & Syst. E77-D(12):1321–1329)
- **Fecha:** 12/1994
- **URL:** (ver H; la URL de IEICE dio 405)
- **Tema:** Continuo realidad-virtualidad
- **Concepto:** RE → AR → AV → VE
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Diagrama del continuo
- **Obligatorio/Complementario:** **O** (cita)
- **Verificación:** Referencia bibliográfica confirmada indirectamente (Azuma 1997 lo cita como [Milgram94a]). URL **NO VERIFICADA**.

**F22**
- **Título:** AR Foundation 6.3 (manual)
- **Autor:** Unity
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.3/manual/index.html
- **Tema:** Features AR
- **Concepto:** Plane detection, anchors, meshing, occlusion, image/face/body tracking, raycasts, etc. "Not all features are available on all platforms". Versión released para 6000.3: **6.3.5**
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Tabla de capacidades
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK (también el Manual com.unity.xr.arfoundation).

**F23**
- **Título:** Unity OpenXR: Meta (2.3)
- **Autor:** Unity
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://docs.unity3d.com/Packages/com.unity.xr.meta-openxr@2.3/manual/index.html
- **Tema:** MR en Quest con AR Foundation
- **Concepto:** Planes, anchors, meshing, occlusion, colocation, display refresh rate
- **Nivel:** A
- **Confiabilidad:** Alta
- **Uso en clase:** Referencia técnica
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK. No verifiqué qué versión del paquete corresponde a 6.3.

**F24**
- **Título:** Passthrough API Overview
- **Autor:** Meta
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://developers.meta.com/horizon/documentation/unity/unity-passthrough/
- **Tema:** Passthrough y privacidad
- **Concepto:** "Because apps cannot access images or videos of a user's physical environment, they create a special passthrough layer. The XR Compositor replaces this layer..."
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Privacidad por diseño
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F25**
- **Título:** Passthrough Camera API Overview
- **Autor:** Meta
- **Tipo:** Doc oficial
- **Fecha:** Vigente (pública desde v76 según el resultado de búsqueda)
- **URL:** https://developers.meta.com/horizon/documentation/unity/unity-pca-overview/
- **Tema:** Acceso a cámara (2025)
- **Concepto:** Quest 3/3S, Horizon OS v74+. Permisos `android.permission.CAMERA` o `horizonos.permission.HEADSET_CAMERA`. 1280×960 (1280×1280 desde v83), latencia de captura 20–40 ms, 60 Hz. Los datos son "Device User Data"
- **Nivel:** A
- **Confiabilidad:** Alta
- **Uso en clase:** Límites técnicos y privacidad
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK. El dato "pública en v76" sale solo de la búsqueda.

**F26**
- **Título:** Mixed Reality Utility Kit (MRUK) overview
- **Autor:** Meta
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://developers.meta.com/horizon/documentation/unity/unity-mr-utility-kit-overview/
- **Tema:** Scene understanding
- **Concepto:** Scene queries, environment raycasting, rooms/anchors, Space Sharing
- **Nivel:** A
- **Confiabilidad:** Alta
- **Uso en clase:** Mencionar
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F27**
- **Título:** Making a Mesh: Global Mesh Destruction in First Encounters
- **Autor:** Alexander Dawson (Meta)
- **Tipo:** Blog técnico oficial
- **Fecha:** 1/12/2023
- **URL:** https://developers.meta.com/horizon/blog/scene-mesh-destruction-first-encounters-meta-quest-developers-mixed-reality/
- **Tema:** Caso MR
- **Concepto:** Scene Mesh con shader de passthrough; algoritmo de seguridad con margen de 0,3 m en los bordes y que conserva lo que está por debajo de 0,75 m. Límite: "Scene Mesh does not offer texture data"
- **Nivel:** M
- **Confiabilidad:** Alta (fuente de la propia empresa)
- **Uso en clase:** Caso de estudio MR
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F28**
- **Título:** ARCore Geospatial API
- **Autor:** Google
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://developers.google.com/ar/develop/geospatial
- **Tema:** AR a escala mundial
- **Concepto:** Basada en VPS con imágenes de Street View; requiere cobertura de Street View
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** AR basada en ubicación (y su límite: cobertura en Jujuy, [INFERENCIA] a verificar)
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F29**
- **Título:** Catching Pokémon in AR mode (Help Center)
- **Autor:** Niantic/Pokémon GO
- **Tipo:** Soporte oficial
- **Fecha:** Vigente
- **URL:** https://niantic.helpshift.com/hc/en/6-pokemon-go/faq/28-catching-pokemon-in-ar-mode/
- **Tema:** AR móvil en un juego masivo
- **Concepto:** AR opcional. Pide ubicación segura, buena iluminación y evitar superficies irregulares
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Caso: AR como *feature opcional*, no como núcleo
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F30**
- **Título:** Scopely to acquire Niantic's games business
- **Autor:** Scopely
- **Tipo:** Comunicado corporativo
- **Fecha:** Anuncio 12/3/2025; cierre 29/5/2025
- **URL:** https://www.scopely.com/en/news/scopely-to-acquire-niantic-games-business-which-includes-pokemon-go-one-of-the-most-successful-mobile-games-of-all-time
- **Tema:** Mercado AR
- **Concepto:** USD 3.500 M. Niantic Spatial se separa como empresa de "geospatial AI" y se queda con Ingress y Peridot
- **Nivel:** I
- **Confiabilidad:** Alta (comunicado, [MARKETING] corporativo)
- **Uso en clase:** Caso de negocio
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F31**
- **Título:** Android XR: The Gemini era comes to headsets and glasses
- **Autor:** Shahram Izadi (Google)
- **Tipo:** Blog oficial
- **Fecha:** 12/12/2024
- **URL:** https://blog.google/products/android/android-xr/
- **Tema:** Nueva plataforma XR
- **Concepto:** SO para headsets y lentes. Soporte de ARCore, Android Studio, Jetpack Compose, Unity y OpenXR
- **Nivel:** I
- **Confiabilidad:** Alta ([MARKETING])
- **Uso en clase:** Línea de tiempo
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F32**
- **Título:** Introducing Android XR SDK Developer Preview
- **Autor:** Android Developers Blog
- **Tipo:** Blog oficial
- **Fecha:** 12/12/2024
- **URL:** https://android-developers.googleblog.com/2024/12/introducing-android-xr-sdk-developer-preview.html
- **Tema:** Unity + Android XR
- **Concepto:** Paquete "Unity OpenXR: Android XR". Conforme a OpenXR 1.1. Cita de Resolution Games sobre portar Demeo
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Portabilidad vía OpenXR
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F33**
- **Título:** Introducing Galaxy XR: Opening New Worlds
- **Autor:** Samsung
- **Tipo:** Comunicado de prensa
- **Fecha:** 21–22/10/2025
- **URL:** https://www.samsungmobilepress.com/press-releases/galaxy-xr-opening-new-worlds/
- **Tema:** Hardware emergente
- **Concepto:** Primer producto comercial con Android XR. USD 1.799,99. Snapdragon XR2+ Gen 2
- **Nivel:** I
- **Confiabilidad:** Alta ([MARKETING])
- **Uso en clase:** Línea de tiempo
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F34**
- **Título:** Apple Vision Pro available in the U.S. on February 2
- **Autor:** Apple Newsroom
- **Tipo:** Comunicado
- **Fecha:** 8/1/2024 (disponible el 2/2/2024)
- **URL:** https://www.apple.com/newsroom/2024/01/apple-vision-pro-available-in-the-us-on-february-2/
- **Tema:** Hardware emergente
- **Concepto:** Desde USD 3.499. Apple lo llama "spatial computer". Input por ojos, manos y voz
- **Nivel:** I
- **Confiabilidad:** Alta ([MARKETING]: "The era of spatial computing has arrived")
- **Uso en clase:** Ejemplo de lenguaje de marketing a desarmar
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

### B.4 Cloud gaming

**F35**
- **Título:** On the Quality of Service of Cloud Gaming Systems
- **Autor:** K.-T. Chen, Y.-C. Chang, H.-J. Hsu, D.-Y. Chen, C.-Y. Huang, C.-H. Hsu
- **Tipo:** Paper (IEEE Trans. Multimedia 16(2):480–495)
- **Fecha:** 02/2014
- **URL:** https://api.crossref.org/works/10.1109/TMM.2013.2291532
- **DOI:** 10.1109/TMM.2013.2291532
- **Tema:** Medición de QoS
- **Concepto:** Técnicas de medición, con OnLive y StreamMyGame como casos (según el resumen de búsqueda)
- **Nivel:** A
- **Confiabilidad:** Alta
- **Uso en clase:** Cita
- **Obligatorio/Complementario:** C
- **Verificación:** Crossref verificado. Pago (IEEE).

**F36**
- **Título:** The Effects of Latency on Player Performance in Cloud-based Games
- **Autor:** M. Claypool & D. Finkel
- **Tipo:** Paper (ACM NetGames 2014, Nagoya)
- **Fecha:** 12/2014
- **URL:** http://web.cs.wpi.edu/~claypool/papers/cloud-games/
- **Tema:** Latencia y QoE
- **Concepto:** "quality of experience and user performance degrade linearly with an increase in latency". El cloud gaming es tan sensible como un juego en primera persona
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Dato central de la clase de cloud
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK (página del autor con PDF; Gratis).

**F37**
- **Título:** A network analysis on cloud gaming: Stadia, GeForce Now and PSNow
- **Autor:** Di Domenico, Perna, Trevisan, Vassio, Giordano
- **Tipo:** Preprint arXiv (2012.06774)
- **Fecha:** 12/2020 (rev. 10/2021)
- **URL:** https://arxiv.org/abs/2012.06774
- **Tema:** Ancho de banda medido
- **Concepto:** Stadia y GFN, hasta ~45 Mbit/s (RTP/WebRTC); PS Now, ≤13 Mbit/s
- **Nivel:** M
- **Confiabilidad:** Media-Alta (preprint; revisar si se publicó)
- **Uso en clase:** Mediciones independientes contra lo que dicen los proveedores
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK. Gratis.

**F38**
- **Título:** ITU-T G.1072: Opinion model predicting gaming quality of experience for cloud gaming services
- **Autor:** ITU-T
- **Tipo:** Recomendación
- **Fecha:** 01/2020 (+ Corrigendum 10/2020)
- **URL:** https://www.itu.int/rec/T-REC-G.1072
- **Tema:** Estándar de QoE
- **Concepto:** Modelo estándar para predecir QoE en cloud gaming
- **Nivel:** A
- **Confiabilidad:** Alta
- **Uso en clase:** Mostrar que existe un estándar
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK. Gratuidad del PDF: **no verificada**.

**F39**
- **Título:** A message about Stadia and our long term streaming strategy
- **Autor:** Phil Harrison (Google)
- **Tipo:** Blog oficial
- **Fecha:** 29/9/2022
- **URL:** https://blog.google/products/stadia/message-on-stadia-streaming-strategy/
- **Tema:** Caso de fracaso
- **Concepto:** Cierre el 18/1/2023 con reembolsos. "it hasn't gained the traction with users that we expected"
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Caso: una tecnología robusta no garantiza un modelo viable
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F40**
- **Título:** GeForce NOW system requirements
- **Autor:** NVIDIA
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://www.nvidia.com/en-us/geforce-now/system-reqs/
- **Tema:** Ancho de banda y latencia
- **Concepto:** 15 Mbps (720p60), 25 (1080p60), 35 (1440p120), 45 (4K120), 65 (5K120), 55 (240/360 fps). "<80ms of network latency from an NVIDIA data center". Ethernet o Wi-Fi 5 GHz
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Tabla de números
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F41**
- **Título:** Xbox Cloud Gaming (xbox.com) + Getting Started with Xbox Cloud Gaming (Xbox Wire, 19/12/2025) + Xbox Cloud Gaming Now Available in Argentina (Xbox Wire, 9/6/2022)
- **Autor:** Microsoft
- **Tipo:** Oficial
- **Fecha:** Ver título
- **URL:** https://www.xbox.com/en-US/cloud-gaming ; https://news.xbox.com/en-us/2025/12/19/getting-started-with-xbox-cloud-gaming/ ; https://news.xbox.com/en-us/2022/06/09/xbox-cloud-gaming-now-available-in-argentina-and-new-zealand/
- **Tema:** Requisitos, modelo de negocio, Argentina
- **Concepto:** Mínimo 10 Mbps (móvil), 20 Mbps recomendados, Wi-Fi 5 GHz. Cloud incluido en Game Pass Essential/Premium/Ultimate con tope de horas mensuales según la página consultada (5/10/15 h). Free-to-play con cuenta Microsoft. Argentina desde 2022
- **Nivel:** I
- **Confiabilidad:** Alta ([MARKETING]: precios y planes cambian seguido)
- **Uso en clase:** Caso local
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK de las 3. support.xbox.com no devolvió contenido (JS).

**F42**
- **Título:** Cloud streaming for PS5 games on PlayStation Portal
- **Autor:** Sony Interactive
- **Tipo:** Soporte oficial
- **Fecha:** Vigente
- **URL:** https://www.playstation.com/en-us/support/subscriptions/psportal-cloud-game-streaming/
- **Tema:** Requisitos y alcance regional
- **Concepto:** 5 Mbps para iniciar sesión, 7 para 720p, 13 para 1080p. Requiere PS Plus Premium y cuenta adulta. Regiones: CA, EE. UU., JP y 27 países europeos (**Argentina no figura**)
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** "Democratización" con matices
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F43**
- **Título:** ENACOM: Velocidad Media de Descarga (totales y por provincia) + Indicadores del Mercado TIC 2º trim. 2025
- **Autor:** ENACOM
- **Tipo:** Datos abiertos oficiales (Argentina)
- **Fecha:** Serie hasta 2026-T2
- **URL:** https://indicadores.enacom.gob.ar/DatosAbiertos/Internet/velocidad-media-totales ; https://indicadores.enacom.gob.ar/DatosAbiertos/Internet/velocidad-media-provincias ; https://www.enacom.gob.ar/institucional/indicadores-del-mercado-tic-del-segundo-trimestre-del-2025_n4789
- **Tema:** Brecha digital
- **Concepto:** Nacional 264,56 Mbps (2026-T2); Jujuy 101,71; CABA 372,42. 82 % de los hogares con internet fija (jun-2025). El indicador es velocidad media *contratada*
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Ejercicio local
- **Obligatorio/Complementario:** **O**
- **Verificación:** Abierto con `curl -k` (el certificado TLS del sitio falla en WebFetch). Gratis.

**F44**
- **Título:** GeForce NOW Powered by ABYA
- **Autor:** ABYA (socio de NVIDIA)
- **Tipo:** Sitio comercial
- **Fecha:** Vigente
- **URL:** https://abya.com/gfn/
- **Tema:** Cloud en el Cono Sur
- **Concepto:** AR, BR, CL, PY, UY. Nivel gratuito con anuncios de hasta 2 min y prioridad baja. Hay que tener los juegos en Steam/Epic/Ubisoft
- **Nivel:** I
- **Confiabilidad:** Media ([MARKETING])
- **Uso en clase:** Caso local
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK. La ubicación de los servidores (Montevideo) **no se verificó** (ver H).

### B.5 Web

**F45**
- **Título:** Web runtime updates are here
- **Autor:** B. Craven, M. Buscemi, A. Bowker (Unity)
- **Tipo:** Blog oficial
- **Fecha:** 30/11/2023
- **URL:** https://unity.com/blog/engine-platform/web-runtime-updates-enhance-browser-experience
- **Tema:** Renombre WebGL → Web
- **Concepto:** El renombre busca "separate WebGL technology from Unity's web platform". Soporte de navegadores móviles en Unity 6. WebGPU "not recommend[ed] for production" (en 2023)
- **Nivel:** I
- **Confiabilidad:** Alta ([MARKETING] parcial)
- **Uso en clase:** Justifica A10
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F46**
- **Título:** Unity Manual 6.3: Web technical limitations / audio / memory / deploying / browser compatibility / WebGPU
- **Autor:** Unity
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:**
  - https://docs.unity3d.com/6000.3/Documentation/Manual/webgl-technical-overview.html
  - https://docs.unity3d.com/6000.3/Documentation/Manual/webgl-audio.html
  - https://docs.unity3d.com/6000.3/Documentation/Manual/webgl-memory.html
  - https://docs.unity3d.com/6000.3/Documentation/Manual/webgl-deploying.html
  - https://docs.unity3d.com/6000.3/Documentation/Manual/webgl-browsercompatibility.html
  - https://docs.unity3d.com/6000.3/Documentation/Manual/WebGPU-features.html
  - https://docs.unity3d.com/6000.3/Documentation/Manual/webgl-gettingstarted.html
- **Tema:** Restricciones Web
- **Concepto:** Ver la sección E
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Clase práctica de build Web
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK de todas. `Manual/web.html` dio 404.

**F47**
- **Título:** WebGPU is now supported in major browsers
- **Autor:** François Beaufort (web.dev)
- **Tipo:** Blog oficial de Chrome/Google
- **Fecha:** 25/11/2025
- **URL:** https://web.dev/blog/webgpu-supported-major-browsers
- **Tema:** Estado de WebGPU
- **Concepto:** Chrome/Edge 113 (Win D3D12, macOS, ChromeOS), Android 121+, Firefox 141 (Win) y 145 (macOS ARM), Safari 26. Linux en progreso
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Tabla de soporte
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK. Complementos verificados: Mozilla Gfx 15/7/2025 (https://mozillagfx.wordpress.com/2025/07/15/shipping-webgpu-on-windows-in-firefox-141/) y Chrome overview (https://developer.chrome.com/docs/web-platform/webgpu/overview).

**F48**
- **Título:** MDN: WebGPU API / WebXR Device API / `<canvas>` accesibilidad
- **Autor:** MDN
- **Tipo:** Referencia
- **Fecha:** Vigente
- **URL:**
  - https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API
  - https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API
  - https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas
- **Tema:** Estándares web
- **Concepto:** WebGPU: "Limited availability", solo en secure context. WebXR: "Experimental". Canvas: "just a bitmap and does not provide information about any drawn objects... you should avoid using canvas in an accessible website"
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Límites de la web
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F49**
- **Título:** W3C WebGPU (CRD 15/9/2026) y W3C WebXR Device API (CRD 9/6/2026)
- **Autor:** W3C
- **Tipo:** Especificación
- **Fecha:** Ver título
- **URL:** https://www.w3.org/TR/webgpu/ ; https://www.w3.org/TR/webxr/
- **Tema:** Estado de estandarización
- **Concepto:** Ambas son Candidate Recommendation Draft, es decir, todavía no son Recommendation
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** "Emergente" con evidencia
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F50**
- **Título:** Khronos WebGL
- **Autor:** Khronos
- **Tipo:** Estándar
- **Fecha:** Vigente
- **URL:** https://www.khronos.org/webgl/
- **Tema:** WebGL 2
- **Concepto:** "WebGL 2.0 exposes the OpenGL ES 3.0 API"
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Base técnica
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F51**
- **Título:** Autoplay policy in Chrome
- **Autor:** Chrome Developers
- **Tipo:** Doc oficial
- **Fecha:** 2018 (Chrome 66; Web Audio desde Chrome 71)
- **URL:** https://developer.chrome.com/blog/autoplay
- **Tema:** Audio web
- **Concepto:** Un AudioContext creado antes de un gesto del usuario queda "suspended" y hay que llamar a `resume()`
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Explica la pantalla "click to play"
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F52**
- **Título:** Godot: Exporting for the Web
- **Autor:** Godot docs (stable)
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_web.html
- **Tema:** Comparación de motores
- **Concepto:** Godot 4 solo WebGL 2 (Compatibility). C# no exporta a web. Threads requieren COOP/COEP; single-threaded por defecto desde 4.3
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Comparar con Unity Web
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F53**
- **Título:** Frameworks oficiales: Phaser, PixiJS, Babylon.js, Three.js, PlayCanvas, Defold
- **Autor:** Cada proyecto
- **Tipo:** Sitios oficiales
- **Fecha:** Vigente
- **URL:**
  - https://github.com/phaserjs/phaser
  - https://pixijs.com/
  - https://www.babylonjs.com/
  - https://threejs.org/
  - https://playcanvas.com/
  - https://defold.com/
- **Tema:** Herramientas
- **Concepto:** Phaser 4.2.1 (MIT, WebGL/Canvas). PixiJS 8 (WebGPU/WebGL). Babylon.js 9.0. Three.js r186. PlayCanvas (MIT, WebGPU + WebXR, editor freemium). Defold (gratis, sin regalías)
- **Nivel:** I
- **Confiabilidad:** Alta (autodescripciones = [MARKETING])
- **Uso en clase:** Mapa de herramientas
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK. phaser.io dio 403, se usó GitHub.

**F54**
- **Título:** Poki: Choosing your web game engine / Requirements · CrazyGames: Technical requirements
- **Autor:** Poki / CrazyGames
- **Tipo:** Docs de portales
- **Fecha:** Vigente
- **URL:**
  - https://developers.poki.com/guide/web-engine
  - https://developers.poki.com/guide/requirements-quality
  - https://docs.crazygames.com/requirements/technical/
- **Tema:** Distribución web
- **Concepto:** Poki: ≤5 MB iniciales / 8 MB total; Unity sin optimizar ~11 MB. CrazyGames: ≤50 MB iniciales (≤20 MB para la home móvil), 250 MB total, 1500 archivos; Unity deshabilitado por defecto en iOS por crashes de memoria
- **Nivel:** I
- **Confiabilidad:** Media-Alta (reglas de un tercero comercial)
- **Uso en clase:** Requisitos de "tienda web"
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

**F55**
- **Título:** Popular puzzle game Wordle is being purchased by The New York Times
- **Autor:** Aisha Malik (TechCrunch)
- **Tipo:** Prensa
- **Fecha:** 31/1/2022
- **URL:** https://techcrunch.com/2022/01/31/popular-puzzle-game-wordle-is-being-purchased-by-the-new-york-times
- **Tema:** Caso web
- **Concepto:** Compra por "low-seven figures"
- **Nivel:** I
- **Confiabilidad:** Media
- **Uso en clase:** Caso: un juego web sin instalación con alcance masivo
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK. El comunicado de nytco.com **no se pudo abrir** (bloqueado).

### B.6 Tendencias

**F56**
- **Título:** GDC 2026 State of the Game Industry Reveals Impact of Layoffs, Generative AI, and More
- **Autor:** GDC
- **Tipo:** Encuesta de la industria (más de 2.300 respondentes)
- **Fecha:** 01/2026
- **URL:** https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/
- **Tema:** IA generativa y plataformas
- **Concepto:** 36 % usa GenAI. 52 % cree que tiene impacto negativo (7 % positivo). Usos: brainstorming 81 %, código 47 %. Steam Deck: 28 % desarrolla para la plataforma
- **Nivel:** I
- **Confiabilidad:** Media-Alta (encuesta autoseleccionada)
- **Uso en clase:** Datos contra el hype
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK. El informe completo es gratis con formulario (reg.gdconf.com/2026-SOTI, sin fetch).

**F57**
- **Título:** Valve welcomes AI games onto Steam...
- **Autor:** Chris Kerr (Game Developer)
- **Tipo:** Prensa profesional
- **Fecha:** 10/1/2024
- **URL:** https://www.gamedeveloper.com/business/valve-welcomes-ai-games-onto-steam-but-only-if-devs-promise-they-aren-t-doing-anything-illegal-
- **Tema:** Política de plataforma sobre IA
- **Concepto:** Pre-Generated vs. Live-Generated. Divulgación en la Content Survey. Reporte de contenido ilegal por parte de los jugadores
- **Nivel:** I
- **Confiabilidad:** Media-Alta
- **Uso en clase:** La IA como requisito de tienda
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK. El post original de Steamworks no se pudo leer (JS).

**F58**
- **Título:** Unity 6.3: AI menu / Sentis (com.unity.ai.inference 2.6.1)
- **Autor:** Unity
- **Tipo:** Doc oficial
- **Fecha:** Vigente
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/ai-menu-access.html ; https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.ai.inference.html
- **Tema:** IA en el motor
- **Concepto:** Assistant, Generators y Sentis (inferencia local). Requiere proyecto vinculado a Unity Cloud. Sistema de puntos o créditos
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Diferenciar IA de producción de IA de runtime
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK. **Ojo:** en la doc 6.3 el paquete figura como **"Sentis"**, no como "Inference Engine" (ver E).

**F59**
- **Título:** Unity's AI tools in beta: what's included and how to get started
- **Autor:** Unity
- **Tipo:** Blog
- **Fecha:** La página mostraba 5/5/2026
- **URL:** https://unity.com/blog/unity-ai-how-to-get-started
- **Tema:** Unity AI
- **Concepto:** Modelos de terceros vía "AI Gateway". MCP Server. Personal: 1000 créditos de prueba por 14 días
- **Nivel:** I
- **Confiabilidad:** Media ([MARKETING])
- **Uso en clase:** Contexto
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F60**
- **Título:** The case for dynamic difficulty adjustment in games
- **Autor:** Robin Hunicke
- **Tipo:** Paper (ACE 2005, pp. 429–433)
- **Fecha:** 2005
- **URL:** https://api.crossref.org/works?query.bibliographic=Hunicke+The+case+for+dynamic+difficulty+adjustment+in+games&rows=2
- **DOI:** 10.1145/1178477.1178573
- **Tema:** Experiencias adaptativas
- **Concepto:** DDA como tecnología existente
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** "Adaptativo" no es nuevo
- **Obligatorio/Complementario:** **O** (cita)
- **Verificación:** Crossref. Pago (ACM 403).

**F61**
- **Título:** Dynamic Difficulty Adjustment (DDA) in Computer Games: A Review
- **Autor:** Mohammad Zohaib
- **Tipo:** Review (Advances in HCI, 2018)
- **Fecha:** 2018
- **URL:** https://api.crossref.org/works?query.bibliographic=Zohaib+Dynamic+Difficulty+Adjustment+in+Computer+Games+A+Review&rows=2
- **DOI:** 10.1155/2018/5681652
- **Tema:** DDA
- **Concepto:** Revisión de técnicas
- **Nivel:** M
- **Confiabilidad:** Alta
- **Uso en clase:** Lectura complementaria
- **Obligatorio/Complementario:** C
- **Verificación:** Crossref verificado. Acceso abierto **probable** (Hindawi), no verificado.

**F62**
- **Título:** Meta Reports Fourth Quarter and Full Year 2025 Results (Exhibit 99.1) + Q4 2025 Earnings Call Transcript
- **Autor:** Meta Platforms
- **Tipo:** Documento financiero primario
- **Fecha:** 01/2026
- **URL:** https://s21.q4cdn.com/399680738/files/doc_financials/2025/q4/Meta-12-31-2025-Exhibit-99-1-FINAL.pdf ; https://s21.q4cdn.com/399680738/files/doc_financials/2025/q4/META-Q4-2025-Earnings-Call-Transcript.pdf
- **Tema:** Metaverso con datos
- **Concepto:** Pérdida operativa de RL en 2025: USD 19.193 M (2024: 17.729 M). Q4 2025: −6.021 M. Ingresos de RL en 2025: 2.207 M. Zuckerberg: "directing most of our investment towards glasses and wearables... making Horizon a massive success on mobile and making VR a profitable ecosystem"
- **Nivel:** I/M
- **Confiabilidad:** Alta (los números son hechos; las declaraciones son visión corporativa)
- **Uso en clase:** Desarmar "metaverso"
- **Obligatorio/Complementario:** **O**
- **Verificación:** PDFs descargados y texto extraído.

**F63**
- **Título:** NVIDIA ACE for Games
- **Autor:** NVIDIA
- **Tipo:** Página de producto
- **Fecha:** Vigente
- **URL:** https://developer.nvidia.com/ace
- **Tema:** NPCs con IA
- **Concepto:** ASR, LLM pequeños on-device, TTS, Audio2Face. "autonomous game characters that inhabit living, breathing worlds"
- **Nivel:** I
- **Confiabilidad:** Baja-Media (**[MARKETING]**)
- **Uso en clase:** Ejemplo de cómo se presenta lo emergente
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F64**
- **Título:** Nintendo Switch 2 Sells Over 3.5 Million Units Worldwide in First Four Days
- **Autor:** Nintendo
- **Tipo:** Comunicado
- **Fecha:** 11/6/2025
- **URL:** https://www.nintendo.co.jp/corporate/release/en/2025/250611.html
- **Tema:** Hibridación de hardware
- **Concepto:** Lanzamiento el 5/6/2025; más de 3,5 M de unidades en 4 días
- **Nivel:** I
- **Confiabilidad:** Alta
- **Uso en clase:** Consola híbrida como plataforma existente
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F65**
- **Título:** Steam Deck
- **Autor:** Valve
- **Tipo:** Sitio oficial
- **Fecha:** Vigente
- **URL:** https://www.steamdeck.com/en/
- **Tema:** PC handheld
- **Concepto:** "Powerful, portable PC gaming". Programa Deck Verified
- **Nivel:** I
- **Confiabilidad:** Alta ([MARKETING])
- **Uso en clase:** Certificación de compatibilidad en PC
- **Obligatorio/Complementario:** C
- **Verificación:** Fetch OK.

**F66**
- **Título:** Casos VR en Steam: Half-Life: Alyx (546560), Beat Saber (620980), SUPERHOT VR (617830); First Encounters en Meta Store
- **Autor:** Valve / Beat Games / SUPERHOT Team / Meta
- **Tipo:** Fichas de tienda
- **Fecha:** Alyx 23/3/2020; Beat Saber 21/5/2019; SUPERHOT VR 25/5/2017
- **URL:**
  - https://store.steampowered.com/app/546560/
  - https://store.steampowered.com/app/620980/
  - https://store.steampowered.com/app/617830/
  - https://www.meta.com/experiences/first-encounters/6236169136472090/
- **Tema:** Casos
- **Concepto:** SUPERHOT VR: "Time moves only when you move". First Encounters es gratis
- **Nivel:** I
- **Confiabilidad:** Alta (datos de tienda)
- **Uso en clase:** Casos de estudio
- **Obligatorio/Complementario:** **O**
- **Verificación:** Fetch OK.

*(Son 66 entradas porque varias fichas agrupan documentación del mismo emisor. Las de calidad "núcleo" marcadas O son unas 30.)*

---

## C) Videos

Todos verificados por fetch de la página oficial o por oEmbed.

| Título | Canal/Emisor | Duración | Fecha | Fragmento sugerido | Concepto | Uso | URL |
|---|---|---|---|---|---|---|---|
| Half-Life: Alyx – Locomotion Deep Dive | Valve (YouTube, oEmbed OK) | ~11 min (dato de UploadVR; no verificado en YouTube) | 04/2020 (nota UploadVR del 6/4/2020) | Completo | Evolución del teleport de The Lab a Blink/Shift/Continuous; validez de la posición final; audio en la locomoción | Clase de locomoción VR | https://www.youtube.com/watch?v=TX58AbJq-xo |
| Principles of spatial design (WWDC23, sesión 10072) | Apple Developer | ~18–21 min (la página indica capítulos hasta 18:24; duración exacta no confirmada) | 06/2023 | 5:26–8:22 ("Human-centered") y 12:39–18:24 ("Immersive") | Ergonomía, campo visual, "anchor content in people's space, not their view", fade en transiciones | Diseño MR/espacial | https://developer.apple.com/videos/play/wwdc2023/10072/ |
| Design for spatial input (WWDC23, 10073) | Apple Developer | ~18–19 min | 06/2023 | 2:22–12:21 (Eyes); 12:21–18:36 (Hands) | Mirada + pellizco, target mínimo de 60 pt, fatiga de manos y falta de feedback táctil | Interacción sin controladores | https://developer.apple.com/videos/play/wwdc2023/10073/ |
| Design great visionOS apps (WWDC24, 10086) | Apple Developer | ~20 min | 06/2024 | Sección "Comfortable" (a determinar) | Intencional / inmersivo / cómodo / disfrutable; minimizar el movimiento físico | Complementario | https://developer.apple.com/videos/play/wwdc2024/10086/ |
| The Portal Locomotion of 'Budget Cuts' | GDC Vault (VRDC@GDC 2018), Freya Holmer. **Gratis** | No verificada | 2018 | A determinar | Locomoción por portales como alternativa al teleport | Caso de diseño de locomoción | https://gdcvault.com/play/1024795/The-Portal-Locomotion-of-Budget |
| Developing Virtual Reality Games and Experiences | GDC Vault (GDC 2014), Tom Forsyth (Oculus). **Gratis** | No verificada | 2014 | A determinar | Lecciones del port de TF2 a VR; decisiones que en VR son críticas | Histórico/fundacional | https://www.gdcvault.com/play/1020714 |
| Advanced VR Rendering | GDC Vault (GDC 2015), Alex Vlachos (Valve). **Gratis** | No verificada | 2015 | A determinar | "shade over 4 million pixels per frame at a minimum of 90 fps"; stereo, latencia | Performance VR (avanzado) | https://www.gdcvault.com/play/1021771/Advanced-VR |
| Advanced VR Rendering Performance | GDC Vault (GDC 2016), Alex Vlachos. **Gratis** | No verificada | 2016 | A determinar | Adaptive fidelity para sostener 90 fps | Avanzado/opcional | https://www.gdcvault.com/play/1023522/Advanced-VR-Rendering |

**Sin video verificado (buscar antes de la clase):** cloud gaming (GDC o académico), WebGPU (Chrome Developers / Google I/O), XR Interaction Toolkit oficial de Unity, Meta Connect developer sessions. Ver H.

---

## D) PDFs de acceso legal y gratuito (verificados)

| Documento | URL | Estado |
|---|---|---|
| Azuma (1997) A Survey of Augmented Reality (copia del autor, 48 pp.) | https://ronaldazuma.com/papers/ARpresence.pdf | Descargado y texto extraído. OK |
| LaViola (2000) A Discussion of Cybersickness (copia del autor, 10 pp.) | https://cs.brown.edu/people/jlaviola/pubs/cybersick.pdf | Descargado y texto extraído. OK |
| Slater (2009) Place illusion and plausibility (PMC, acceso abierto) | https://pmc.ncbi.nlm.nih.gov/articles/PMC2781884/ | HTML abierto en PMC (el PDF se descarga desde ahí) |
| Claypool & Finkel (2014): página del paper con PDF | http://web.cs.wpi.edu/~claypool/papers/cloud-games/ | Página verificada; enlaza `paper.pdf` |
| Di Domenico et al. (2020) arXiv | https://arxiv.org/abs/2012.06774 | OK (PDF en arXiv) |
| Meta Q4 2025 Exhibit 99.1 | https://s21.q4cdn.com/399680738/files/doc_financials/2025/q4/Meta-12-31-2025-Exhibit-99-1-FINAL.pdf | OK |
| Meta Q4 2025 Earnings Call Transcript | https://s21.q4cdn.com/399680738/files/doc_financials/2025/q4/META-Q4-2025-Earnings-Call-Transcript.pdf | OK |

**No disponibles gratis o no verificados:** Milgram & Kishino 1994 (IEICE 405), Slater & Wilbur 1997 (MIT Press, pago), Kennedy 1993 (T&F, pago), Chang 2020 (T&F, pago), Chen 2014 (IEEE, pago), Hunicke 2005 (ACM, pago), ITU-T G.1072 (gratuidad no confirmada). No encontré e-books oficiales de XR de Unity o Meta verificables (ver H).

---

## E) Datos técnicos verificados y citables

**VR / Meta Quest**
- [HECHO] VRC.Quest.Performance.1: "maintain a rendering rate (fps) of at least 60 fps". Refresh permitidos para apps interactivas: 72, 80, 90, 96, 100, 120 Hz. 96/100/120 Hz no están en todos los dispositivos. Las apps de *media* pueden usar 60 Hz. Con AppSW se puede renderizar a la mitad del refresh (p. ej., 36 fps a 72 Hz). Verificación: OVR Metrics Tool durante 45 min.
  - → **Corrección a la consigna:** el "mínimo de 72 FPS" que circula en resúmenes **no coincide** con la redacción vigente. El refresh mínimo para apps interactivas es 72 Hz, pero el piso de render es 60 fps (o la mitad con AppSW).
- [HECHO] VRC.Quest.Performance.3: head-tracking en ≤4 s desde el lanzamiento o un indicador de carga en VR. VRC.Quest.Performance.4 (recomendado): render scale ≥85 %.
- [HECHO] AppSW: "up to 70 percent additional compute" (cifra de Meta). Vulkan only. Unity 2022.3.15f1+ o 6000.0.9f1+.
- [HECHO] Passthrough clásico: la app no accede a imágenes; el compositor reemplaza la capa.
- [HECHO] PCA: Quest 3/3S, OS v74+, 1280×960 (1280×1280 desde v83), captura de 20–40 ms, 60 Hz, ~1–2 % de GPU por cámara, "not supported in XR Simulator".
- [HECHO] First Encounters: margen de seguridad de 0,3 m en los bordes de la habitación; conserva los triángulos por debajo de 0,75 m.
- [HECHO] (GDC 2015, Valve) "shade over 4 million pixels per frame at a minimum of 90 fps" (contexto PC VR de primera generación).

**Unity 6.3 (6000.3)**
- [HECHO] Versiones de paquetes released para 6000.3: XR Interaction Toolkit **3.3.2**, AR Foundation **6.3.5**, OpenXR Plugin **1.16.1**, Sentis (com.unity.ai.inference) **2.6.1**.
- [HECHO] Single-pass instanced reduce mucho la CPU y un poco la GPU frente a multi-pass.
- [HECHO] Foveated: fijo vs. eye-tracked, según el dispositivo.
- [HECHO] Plataforma Web:
  - Requiere navegador con WebGL 2, WebAssembly y 64 bits.
  - Móvil: iOS Safari 15+ y Chrome 58+ en Android.
  - Sin multithreading en C# (los threads nativos C/C++ son experimentales).
  - Sin sockets IP ni System.Net.
  - Heap contiguo de hasta 4 GB. En móvil se recomienda fijar Initial Memory Size.
  - GC solo cuando no se ejecuta código administrado / al final del frame.
  - Audio: los navegadores lo bloquean hasta que el usuario interactúa. Sin micrófono. Web Audio en lugar de FMOD. Glitch en el loop de AAC.
  - Física no determinista respecto de otras plataformas. Sin Reflection.Emit.
  - Brotli: más chico pero más lento de comprimir; Chrome y Firefox solo lo soportan nativo sobre HTTPS. Servir `.wasm` con `Content-Type: application/wasm`. No se puede abrir desde `file://`.
  - WebGPU en 6.3: **experimental**, no se habilita solo, requiere HTTPS o localhost. Soporta compute shaders, indirect rendering, GPU skinning y VFX Graph. **No** soporta async compute, dynamic resolution ni cubemap arrays.
- [HECHO] Unity renombró "WebGL" a "Unity Web" (blog del 30/11/2023). [INFERENCIA] En la doc 6.3 conviven ambos nombres (las URLs siguen siendo `webgl-*`).
- [HECHO] En la doc 6.3 el paquete de inferencia local figura con el nombre **"Sentis"**, aunque en 6.2 se anunció como "Inference Engine". [INFERENCIA] Unity revirtió el nombre comercial. Conviene decirlo en clase para que no busquen "Inference Engine" en 6.3 y no lo encuentren.

**Web**
- [HECHO] WebGPU (web.dev, 25/11/2025):
  - Chrome/Edge 113+ en Windows (D3D12), macOS y ChromeOS.
  - Android desde Chrome 121 (Android 12+, GPUs Qualcomm/ARM).
  - Firefox 141 en Windows y 145 en macOS Tahoe ARM.
  - Safari en macOS/iOS/iPadOS/visionOS 26.
  - Linux en progreso.
- [HECHO] MDN: WebGPU tiene "Limited availability" y requiere secure context. WebXR es "Experimental".
- [HECHO] W3C: WebGPU CRD (15/9/2026), WebXR CRD (9/6/2026).
- [HECHO] Chrome autoplay: un AudioContext creado antes de un gesto del usuario queda "suspended".
- [HECHO] Godot 4: solo WebGL 2. C# no exporta a web.
- [HECHO] Poki: ≤5 MB iniciales / 8 MB total; Unity sin optimizar ~11 MB; Phaser ~290 KB; PixiJS ~130 KB; Defold ~1,03 MB; Godot ~10 MB. CrazyGames: ≤50 MB iniciales, ≤20 MB para la home móvil, ≤250 MB total, ≤1500 archivos.
- [HECHO] Unity (blog 2023, cifra propia = [MARKETING]): "With just a 25% drop in load time, active sessions grew by 50%..."

**Cloud**
- [HECHO] GeForce NOW:
  - 15 Mbps: 720p60
  - 25 Mbps: 1080p60
  - 35 Mbps: 1440p120
  - 45 Mbps: 4K120
  - 65 Mbps: 5K120
  - 55 Mbps: 240/360 fps
  - Requisito de red: menos de 80 ms al datacenter de NVIDIA.
- [HECHO] Xbox Cloud: mínimo 10 Mbps (móvil, algunos dispositivos 20). Xbox Wire 2025: "at least 20 Mbps". Wi-Fi 5 GHz. Disponible en Argentina desde el 9/6/2022.
- [HECHO] PS Portal cloud: 5/7/13 Mbps (sesión/720p/1080p). PS Plus Premium. Solo cuentas adultas. No disponible en Argentina.
- [HECHO] Stadia: cierre anunciado el 29/9/2022, efectivo el 18/1/2023, con reembolsos de hardware y juegos.
- [HECHO] Claypool & Finkel 2014: degradación **lineal** de la QoE y del rendimiento con la latencia.
- [HECHO] Di Domenico et al.: Stadia/GFN hasta ~45 Mbit/s; PS Now ≤13 Mbit/s (mediciones de 2020).
- [HECHO] ENACOM:
  - Velocidad media de bajada nacional: 2026-T2 = 264,56 Mbps (2023-T4 = 139,04).
  - 2026-T2 por provincia: Jujuy 101,71; Salta 176,16; Tucumán 186,83; CABA 372,42; La Rioja 93,92 (la más baja).
  - 82 % de hogares con internet fija (jun-2025).
  - 217.812 accesos satelitales (2025-T2).

**Tendencias / mercado**
- [HECHO] Meta Reality Labs:
  - Pérdida operativa: 2025 = USD −19.193 M; 2024 = −17.729 M; Q4 2025 = −6.021 M.
  - Ingresos 2025: USD 2.207 M.
  - Para 2026, Meta espera pérdidas "similar to 2025 levels".
- [HECHO] GDC 2026 (más de 2.300 respondentes): 36 % usa GenAI; 52 % ve impacto negativo; 7 % positivo.
- [HECHO] Steam (10/1/2024): divulgación obligatoria de IA, Pre-Generated vs. Live-Generated, guardrails.
- [HECHO] Fechas: Vision Pro, 2/2/2024 (USD 3.499). Android XR, anunciado el 12/12/2024. Galaxy XR, 21/10/2025 (USD 1.799,99). Switch 2, 5/6/2025 (más de 3,5 M en 4 días). Scopely–Niantic: USD 3.500 M, cerró el 29/5/2025.

---

## F) Tabla de tendencias

| Tema | Clasificación | Evidencia | Fuente |
|---|---|---|---|
| VR standalone (Quest 3/3S) con tienda y certificación | **Existente** | VRC públicos, tienda activa, Reality Labs con USD 2.207 M de ingresos en 2025 | Meta VRC; Meta 10-K/99.1 |
| MR con passthrough a color en headsets | **Existente** (nicho) | First Encounters preinstalado; MRUK; Passthrough API | Meta docs/blog |
| Acceso de las apps a la cámara del headset (CV/ML) | **Emergente** | PCA desde v74/v76; solo Quest 3/3S | Meta PCA |
| AR móvil en juegos (ARCore/ARKit) | **Existente** (como feature opcional) | Pokémon GO AR opcional | Niantic Help |
| AR geoespacial a escala ciudad | **Emergente** | ARCore Geospatial (depende de Street View); Niantic Spatial como empresa aparte | Google; Scopely |
| Android XR / Galaxy XR | **Emergente** | Primer dispositivo en oct-2025 | Samsung; Google |
| Lentes AR/IA de consumo como plataforma de juego | **Tendencia** (declarada por Meta) / **especulación** para juegos | Meta: "most of our investment towards glasses and wearables". No hay evidencia de juegos relevantes ahí | Meta transcript Q4 2025 |
| OpenXR como estándar común | **Existente** | OpenXR 1.1; Android XR "conforme" | Khronos; Android Dev Blog |
| Cloud gaming por suscripción | **Existente** (con límites regionales y de red) | Xbox (AR desde 2022), GFN/ABYA, PS Portal (no en AR) | Oficiales |
| Cloud gaming como reemplazo del hardware local | **Especulación** | Stadia cerró; Xbox impone topes de horas cloud por plan; requisitos de red | Google; xbox.com |
| "Negative latency" (Stadia) | **Marketing** / no verificado | Sin fuente primaria abierta | H |
| Unity Web (WebGL 2) en desktop y móvil | **Existente** | Doc 6.3 | Unity |
| WebGPU en navegadores | **Emergente → en adopción** | Por defecto en Chrome/Edge/Safari/Firefox-Win; falta Linux; MDN "Limited availability"; W3C CRD | web.dev; MDN; W3C |
| WebGPU en Unity | **Emergente** (experimental) | "experimental" en 6.3 | Unity Manual |
| WebXR | **Emergente** | MDN "Experimental"; W3C CRD | MDN; W3C |
| DDA / dificultad adaptativa | **Existente** (desde hace décadas) | Hunicke 2005; Zohaib 2018 | ACM; Hindawi |
| GenAI en la producción (assets, código, brainstorming) | **Existente** y controvertida | 36 % de uso; 52 % negativo; Unity AI; política de Steam | GDC 2026; Steam; Unity |
| NPCs con LLM en runtime | **Emergente** | NVIDIA ACE ([MARKETING]); categoría "Live-Generated" de Steam | NVIDIA; Game Developer |
| "Juegos generados enteramente por IA" | **Especulación** | Sin fuente verificada | — |
| Consolas híbridas / PC handheld | **Existente** | Switch 2; Steam Deck (28 % de devs) | Nintendo; GDC 2026 |
| Cross-play / cross-progression | **Existente** | Beat Saber multiplayer con cross-play (ficha Steam) | Steam |
| Metaverso (mundo virtual único e interoperable) | **Especulación / visión corporativa** | Pérdidas acumuladas de RL; giro de Meta hacia lentes y Horizon en móvil | Meta 99.1 y transcript |
| Plataformas sociales persistentes y UGC | **Existente** | (Roblox/Fortnite no verificados en esta sesión → H) | — |

---

## G) Fuera de alcance (para no convertir la unidad en un curso de XR o de redes)

- Programar shaders estéreo, foveated a mano, modificar URP para AppSW: solo mencionarlos como técnicas.
- SLAM/VIO a nivel algorítmico (filtros, bundle adjustment): basta con "el dispositivo estima su pose 6DoF a partir de cámaras e IMU y falla con poca luz o sin textura".
- Codecs de video en detalle (GOP, rate control), protocolos (RTP/WebRTC/QUIC) y modelos de QoE como G.1072: solo los conceptos.
- Netcode, rollback y lag compensation: son de una unidad de multijugador, no de esta.
- WebGPU/WGSL a nivel de API, WebAssembly a mano, Emscripten.
- Entrenar modelos de ML, LLMs, prompt engineering, Sentis en profundidad.
- Economía y finanzas de Meta más allá de un par de cifras ilustrativas.
- Hardware óptico (lentes pancake, micro-OLED, IPD) más allá de una mención.
- Desarrollo para visionOS/PolySpatial: requiere Mac y Unity Pro.

---

## H) NO VERIFICADO (no usar como dato sin chequear)

1. **Milgram & Kishino 1994**: la URL de IEICE (https://globals.ieice.org/en_transactions/information/10.1587/e77-d_12_1321/_p) devolvió 405. No hay copia libre verificada. La referencia bibliográfica es correcta (Azuma 1997 la cita).
2. **Motion-to-photon latency ~20 ms** (cifra que se suele citar): no encontré una fuente oficial que la diga textualmente en esta sesión.
3. **"Negative latency" de Stadia**: no se verificó la fuente primaria (se suele atribuir a declaraciones de 2019 a la revista Edge). Si se menciona, marcarlo como marketing.
4. **Pipeline de cloud con cifras de latencia total** (p. ej., "100–150 ms input-to-display"): sin fuente verificada en esta sesión.
5. **Jarschel et al. 2011** (IMIS 2011, pp. 330–335): solo aparece en resultados de búsqueda; no se abrió ni el DOI ni el PDF.
6. **Apple visionOS HIG** (https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos): la URL abre, pero el resumen fue genérico (JS) y **no se tomaron citas** de ahí. Usar los videos WWDC (C).
7. **ARKit** (https://developer.apple.com/augmented-reality/arkit/): abre, pero el contenido se resumió de forma genérica. No citar textualmente.
8. **support.xbox.com**: las páginas abren, pero no devuelven contenido (JS). Las cifras salen de xbox.com y Xbox Wire.
9. **Post original de Steamworks sobre IA**: el link (https://steamcommunity.com/groups/steamworks/announcements/detail/3862463747997849619) no devolvió contenido. Se cita vía Game Developer.
10. **nytco.com, comunicado de Wordle**: bloqueado. Se cita vía TechCrunch.
11. **Servidores de GeForce NOW/ABYA en Montevideo**: solo en el resumen de búsqueda.
12. **Passthrough Camera API "pública en v76"**: solo en el resumen de búsqueda. La doc verificada dice v74+ como requisito.
13. **XRI Tunneling Vignette en 3.3**: la URL `@3.3/manual/tunneling-vignette.html` dio 404. Se usa la página de 3.1.
14. **Choose and configure XR provider plug-ins (6.3)**: la URL salió de la búsqueda pero no tuvo fetch directo.
15. **Zohaib 2018 en acceso abierto**: probable (Hindawi), no verificado.
16. **ITU-T G.1072, descarga gratuita**: no confirmada.
17. **Krunker, Demeo MR (modo MR concreto), Roblox, Fortnite Creative, Xbox Play Anywhere / cross-progression oficial, Quest 3 "Meta Horizon Store" Comfort ratings, e-books XR de Unity y Meta**: no verificados (me quedé sin presupuesto de búsquedas web). Demeo solo está verificado como "portado a Android XR" (cita en Android Dev Blog).
18. **Videos sin verificar** (a buscar): charla GDC sobre cloud gaming, Google I/O/Chrome Developers sobre WebGPU, video oficial de Unity sobre XRI 3.x, sesiones de Meta Connect, charla de Valve "The Design of Half-Life: Alyx". Video de "Harvey Newman" sobre GDC 2026 (oEmbed OK, pero es de un tercero): **descartado**.
19. **Duraciones exactas de los videos de GDC Vault y Apple**: aproximadas o no verificadas.
20. **Fecha del blog "Unity AI how to get started" (5/5/2026)**: es la que mostraba la página. Puede ser una fecha de actualización y no la de publicación original.
21. **Precios o planes de Xbox Game Pass con horas cloud (5/10/15 h)**: es lo que mostraba xbox.com/en-US el 4/10/2026. Pueden variar por región (incluida Argentina) y cambian seguido.
