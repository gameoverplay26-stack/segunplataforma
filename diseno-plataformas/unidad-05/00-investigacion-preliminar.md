# Investigación de apoyo — Unidad 5 "Diseño según Plataforma de Consolas"

Cátedra: Diseño según Plataformas de Juego (UNJu). Fecha de la investigación: 2026-10-04. Motor: Unity 6000.3.11f1 (Unity 6.3 LTS).

## Convenciones de este documento

- **[V]** = URL abierta con WebFetch durante esta investigación (YouTube: verificado con `youtube.com/oembed`). Toda URL de las secciones B–F está verificada así salvo que diga lo contrario.
- **HECHO** = lo dice la fuente citada. **INFERENCIA** = conclusión mía a partir de fuentes; se marca explícitamente.
- Jerarquía de confiabilidad usada: Oficial (Microsoft/Sony/Nintendo/Valve/Unity) > Académico (ACM) > Profesional (GDC, Digital Foundry, Game Developer, Gambetta) > Prensa/blogs.
- Lo que no pude abrir o confirmar está en la sección H. No se usa en clase sin re-verificar.

### Correcciones a premisas del pedido (importante)

1. **Microsoft GDK en GitHub NO es de 2024.** El GDK se publicó gratis en GitHub el **20/21 de julio de 2021** (blog oficial Microsoft "Meet the Microsoft Game Developer Kit (GDK)", fechado 20-jul-2021; Game Developer, 22-jul-2021). El repositorio sigue activo: última versión listada "April 2026 GDK Update 5 v2604.5.7903", 21-sep-2026. La versión para **consolas (GDKX)** sigue siendo solo para socios licenciados.
2. **Microsoft SÍ publica sus requisitos de certificación (XR) en Microsoft Learn**, de forma abierta (sin login al momento de la consulta). Es el único de los tres fabricantes que lo hace. Incluso publica los casos de prueba. Lo que sigue bajo NDA son partes puntuales (p. ej. la "Forbidden Terms List (NDA topic)").
3. **La charla de accesibilidad de The Last of Us Part II verificada NO está en el canal de GDC**, sino en el de IGDA GASIG ("The Accessibility in Last of Us Part II: A 3 Year Journey").
4. **XR-017 "Title Ratings" fue eliminado** de los XR el 6-ago-2026 (v16.4); según Microsoft, la declaración de clasificación por edad "continúa validándose al momento del envío". No enseñar "XR-017" como vigente.
5. **Multiplayer Play Mode 3.0 requiere Unity 6.3 LTS o superior**, lo que coincide con el motor del curso.
6. **Input System para Unity 6.3 es la versión 1.20.0** (no 1.14). La documentación 1.20 cambió nombres de páginas; algunas páginas de 1.14 (verificadas) tienen contenido equivalente. Ver ficha B-17.

---

## A) Auditoría del programa

| # | Qué dice el programa | Clasificación | Problema | Qué enseñar | Por qué | Fuente |
|---|---|---|---|---|---|---|
| A1 | "Diferencias entre consolas de sobremesa y portátiles" | CORRECTO PERO INCOMPLETO | La dicotomía sobremesa/portátil ya no describe el mercado: Switch y Switch 2 son **híbridas** (modo dock y portátil con perfiles de rendimiento distintos), y Steam Deck es un **PC portátil** con programa de compatibilidad propio. | Tres categorías: sobremesa (PS5/PS5 Pro, Xbox Series X/S), híbrida (Switch 2: 1080p portátil / hasta 4K60 en dock), PC portátil (Steam Deck 1280x800). Consecuencia de diseño: un mismo juego debe tener **dos presupuestos** (dock/portátil) y UI legible a distancia de TV y en pantalla de 7–8". | Las specs oficiales muestran la dualidad. | B-1, B-2, B-6 |
| A2 | "Arquitecturas y ecosistemas propietarios" | REQUIERE PRECISIÓN | "Arquitecturas" puede derivar en un curso de hardware. Lo diferencial para el diseñador no es el silicio sino el **acceso cerrado**: registro, NDA, devkits, licencias, certificación, tienda única. | Definir "plataforma cerrada" con la doc de Unity: requiere "confidentiality and legal agreements with the platform provider". Mostrar el camino de acceso real de cada fabricante (lo público). Specs: solo las cifras públicas que impactan diseño (memoria, resolución objetivo). | Es la diferencia práctica con PC/móvil, y es lo que un equipo indie enfrenta. | B-7, B-8, B-9, B-10, B-12, B-13 |
| A3 | "Integración de gamepads" | CORRECTO PERO INCOMPLETO | No menciona abstracción por acciones, esquemas de control, remapeo ni glifos. | Input System 1.20: Actions → Bindings → Control Schemes; remapeo interactivo (`PerformInteractiveRebinding`) y persistencia (`SaveBindingOverridesAsJson`); glifos según dispositivo activo. Vincular con XAG 112 (navegación por mando digital) y con criterio Steam Deck "glifos que coinciden con la entrada activa". | Remapeo y navegación por mando son a la vez accesibilidad y requisito de calidad. | B-17, B-18, B-22, B-30 |
| A4 | "Controladores específicos (ej.: Joy-Con, DualSense, Xbox Controller)" | REQUIERE PRECISIÓN + DESACTUALIZADO (parcial) | (1) Joy-Con original quedó superado por **Joy-Con 2** (sensor de mouse, HD Rumble 2, botón C). (2) En Unity, en **escritorio** hay soporte HID de DualSense y Switch Pro, pero el rumble de mandos de consola conectados a su consola "Only supported if you install console-specific input packages" (paquetes bajo NDA). Las funciones distintivas (gatillos adaptativos, hápticos HD) dependen de SDKs de plataforma. | Enseñar qué es posible en el aula (Gamepad genérico, `SetMotorSpeeds`, `SetLightBarColor` en DualShock/DualSense HID) y qué **no** (gatillos adaptativos / HD Rumble 2 requieren SDK del fabricante). Diseño: features de mando como **mejora opcional**, nunca requisito (un jugador puede usar otro mando o el Access/Adaptive Controller). | Evita prometer funcionalidades no implementables con herramientas públicas. | B-2, B-15, B-16, B-17 |
| A5 | "Testing de compatibilidad con múltiples dispositivos" | FALTA DESARROLLAR | Sin contenido operativo. | Matriz de pruebas: tipos de mando × conexión (USB/BT) × eventos (desconexión, reconexión, segundo mando, cambio de usuario, suspensión). Usar como plantilla los **casos de prueba públicos** de Microsoft (115-02 retiro de pilas del mando; 112-08 suspender y cambiar usuario) y los criterios públicos de Steam Deck Verified. | Son los únicos checklists oficiales y abiertos; dan al alumno un "estándar externo" real. | B-27, B-28, B-30 |
| A6 | "Procesos de certificación en Sony, Microsoft y Nintendo" | REQUIERE PRECISIÓN | Mayoritariamente bajo NDA. No hay material público de TRC (Sony) ni de Lotcheck/guidelines (Nintendo). Riesgo de enseñar rumores. | Enseñar el **concepto** (requisitos técnicos + prueba del fabricante antes de publicar) con el único corpus oficial público: Xbox Requirements + test cases. Para Sony y Nintendo: solo los pasos públicos (Nintendo: aceptar NDA, firmar acuerdo de publicación, obtener clasificación, "submit your game for review by Nintendo"; Sony: registro en PlayStation Partners, plan de proyecto, firma del GDPA). Decir explícitamente qué no es público (sección F). | Rigor: no inventar procesos. | B-9, B-10, B-11, B-27, B-28, F |
| A7 | "Requerimientos técnicos y de calidad" | CORRECTO PERO INCOMPLETO | Falta separar requisitos **obligatorios** (XR) de **buenas prácticas** (XAG: Microsoft aclara que "aren't intended to act as a checklist to validate any type of compliance"). | Dos capas: (1) obligatorio para publicar (estabilidad XR-001, calidad XR-003, mando/usuario XR-112/115, terminología XR-022, paridad de generación XR-130); (2) accesibilidad recomendada (XAG 101, 112). | Evita la confusión frecuente "accesibilidad = certificación". | B-22, B-23, B-24, B-27 |
| A8 | "Publicación en stores oficiales" | CORRECTO PERO INCOMPLETO | Falta clasificación por edades (IARC/ESRB/PEGI), acuerdos de publicación, self-publishing. | Flujo genérico: registro → NDA/acuerdo → devkit → desarrollo → clasificación por edad → envío a certificación → material de tienda → lanzamiento → parches (que también se certifican). IARC: gratuito para desarrolladores. Nintendo: "self-publish it on the Nintendo eShop with the price and release date entirely up to you". | Es el recorrido real y público. | B-9, B-31, B-32, B-33 |
| A9 | "Diseño de multijugador local (split-screen, cooperativo, competitivo)" | CORRECTO PERO INCOMPLETO | No conecta el diseño con su **costo técnico** ni con la UX de unión/asignación de mandos. | Pantalla compartida vs split vs split dinámico (Terrell); costo: N cámaras = N renders; caso **BG3**: sin split-screen en Series S en el lanzamiento (dic-2023), agregado en Patch 8 (2025). Implementación: `PlayerInputManager` (join por botón, split-screen automático, límite de jugadores). Evidencia académica: interdependencia y control compartido (Emmerich & Masuch 2017). | Une diseño + plataforma + optimización: es el corazón de la unidad. | B-18, B-41, B-42, B-44, C |
| A10 | "Multijugador en línea: matchmaking, servidores y latencia" | REQUIERE PRECISIÓN | Mezcla tres capas (servicio de matchmaking, topología/autoridad, percepción de latencia) y puede convertirse en curso de networking. | Nivel conceptual: autoridad del servidor, predicción, interpolación, compensación de lag (Gambetta); latencia tolerable según tipo de juego (Claypool: avatar 1ª persona más sensible; caída ~35% de precisión a 100 ms en tiro de precisión; RTS/omnipresente tolera más). Herramientas Unity solo para demostrar: Multiplayer Play Mode + Network Simulator. Matchmaker como servicio, sin implementarlo. | Lo transferible es el modelo mental; el detalle de implementación es otra materia. | B-34, B-35, B-36, B-37, B-38, B-40, B-43 |
| A11 | "Consideraciones de UX para el juego social" | FALTA DESARROLLAR | Sin contenido. Es justamente donde las consolas imponen reglas públicas. | Privacidad y permisos (XR-015 comunicación; XR-045 privilegios: multijugador, cross-network, comunicación, UGC — incluye cuentas infantiles y aprobación parental), invitaciones vía plataforma (XR-064), "jugado recientemente" (XR-067), gamertag como nombre (XR-046), silenciar jugadores de otras redes en crossplay (XR-015), UGC con reporte (XR-018). Descriptores PEGI "Unrestricted communication"/ESRB "Users Interact". | Diseñar lobbies, chat y crossplay sin esto produce un juego no publicable. | B-27, B-32, B-33 |
| A12 | "Limitaciones de hardware de consolas" | CORRECTO PERO INCOMPLETO | Falta identificar la **memoria** como limitación dominante y la existencia de **varios SKUs** dentro de una misma generación. | Series S 10 GB vs Series X 16 GB; XR-130: "identical game modes are offered across console types within the generation" → la consola más débil fija el piso de diseño. Switch 2 portátil vs dock. Presupuesto de frame (16,6 ms a 60 fps; 33,3 ms a 30 fps — aritmética, no cita). | El caso BG3 muestra que una limitación de memoria puede eliminar un **modo de juego**, no solo bajar gráficos. | B-4, B-5, B-27, B-44 |
| A13 | "Estrategias de optimización de rendimiento" | CONFUSO | No distingue **medir** de **optimizar**. Sin medición, la "estrategia" es adivinar. | Ciclo: objetivo de fps → perfilar (Profiler; módulo Highlights indica si el frame es CPU-bound o GPU-bound) → aislar (Frame Debugger, Profile Analyzer, Memory Profiler) → aplicar técnica → volver a medir. | Es el método que enseña el e-book oficial de profiling de Unity 6. | B-50, B-51, D-2 |
| A14 | "Técnicas de optimización gráfica (LOD, reducción de draw calls, texturas)" | DESACTUALIZADO (parcial) | En Unity 6 cambiaron las prioridades: para URP/HDRP Unity recomienda primero **GPU Resident Drawer** y **SRP Batcher**; "dynamic batching is no longer recommended" en la mayoría de los casos; Unity 6.3 tiene **Mesh LOD** además de LOD Group; existe **GPU occlusion culling** en URP/HDRP. | Cada técnica asociada al problema que resuelve: draw calls/estado (SRP Batcher, GPU Resident Drawer, instancing, static batching) → CPU; geometría lejana (LOD Group / Mesh LOD) → GPU/vértices; objetos ocultos (occlusion culling) → CPU+GPU; memoria de texturas (mipmaps +33%, compresión, mipmap streaming) → memoria/ancho de banda; carga de GPU variable (Dynamic Resolution). | Enseñar técnicas de Unity 2019 en Unity 6.3 es enseñar el orden equivocado. | B-45 a B-52 |
| A15 | — | FALTA UN TEMA IMPORTANTE | Accesibilidad en consola; UI de 10 pies y zona segura de TV; clasificación por edades; ciclo de vida de la app en consola (suspender/reanudar, cambio de usuario); crossplay/cross-progression; frontera consola–PC (Steam Deck/Steam Machine). | Agregar un bloque breve "La consola como entorno": TV a ~3 m (texto mínimo de consola en XAG 101: 26 px a 1080p; zona segura UWP: no poner UI esencial en el 5% del borde), suspend/resume (XR-112), accesibilidad (XAG + Adaptive/Access controller), ratings (IARC). | Todo esto es público, oficial y verificable, y afecta decisiones de diseño desde el día 1. | B-20 a B-25, B-27, B-31 |

---

## B) Fichas de recursos (52)

Formato compacto. "Verif." = cómo se verificó.

### B.1 Plataformas vigentes y acceso

**B-1** — *News Release: "Nintendo Switch 2 to be released on June 5, 2025"*
Autor: Nintendo Co., Ltd. | Tipo: comunicado oficial | Fecha: 2-abr-2025 | URL: https://www.nintendo.co.jp/corporate/release/en/2025/250402.html
Tema: lanzamiento y specs | U5: plataformas, controladores | Concepto: híbrida; Joy-Con 2 "operated like a mouse by sliding it on a surface"; GameChat (C Button, hasta 12 personas, requiere Nintendo Switch Online pago) | Nivel: introductorio | Confiabilidad: oficial primaria | Uso: dato de fecha y features | Obligatorio | Verif.: [V] WebFetch.

**B-2** — *Nintendo Switch 2 Tech Specs*
Autor: Nintendo of America | Tipo: página oficial | Fecha: no indicada | URL: https://www.nintendo.com/us/gaming-systems/switch-2/tech-specs/
Concepto: "Custom processor made by NVIDIA", 256 GB UFS, pantalla 7,9" 1920x1080 HDR10 VRR hasta 120 Hz; dock hasta 3840x2160 a 60 fps; Joy-Con 2 con acelerómetro, giroscopio, sensor de mouse, HD Rumble 2, botón C | Nivel: intro | Confiabilidad: oficial | Uso: comparativa portátil/dock | Obligatorio | Verif.: [V]. Nota: la cifra de RAM (12 GB) aparece en buscadores pero **no la vi en el texto extraído** → sección H.

**B-3** — *SIE Reveals PlayStation 5 Pro*
Autor: Sony Interactive Entertainment | Tipo: nota de prensa | Fecha: 10-sep-2024 | URL: https://sonyinteractive.com/en/press-releases/2024/sony-interactive-entertainment-reveals-playstation-5-pro-the-most-visually-compelling-way-to-play-games-on-playstation/
Concepto: "67 percent more Compute Units", "28 percent faster memory", "up to 45 percent faster rendering", PSSR (upscaling por IA), etiqueta "PS5 Pro Enhanced"; lanzamiento 7-nov-2024 | Confiabilidad: oficial | Uso: ejemplo de SKU "mid-gen" que obliga a perfiles de rendimiento | Complementario | Verif.: [V].

**B-4** — *Xbox Series S (página de consola)*
Autor: Microsoft | Tipo: página oficial | URL: https://www.xbox.com/en-US/consoles/xbox-series-s
Concepto: "10GB GDDR6 128 bit-wide bus", "4 TFLOPS, 20 CUs @1.565 GHz", objetivo 1440p, hasta 120 FPS | Confiabilidad: oficial | Uso: caso de restricción de memoria | Obligatorio | Verif.: [V].

**B-5** — *Xbox Series X (página de consola)*
Autor: Microsoft | URL: https://www.xbox.com/en-US/consoles/xbox-series-x
Concepto: "16GB GDDR6 w/320 bit-wide bus", "12 TFLOPS, 52 CUs @1.825 GHz", 4K, hasta 120 FPS | Uso: contraste con Series S dentro de la misma generación | Obligatorio | Verif.: [V].

**B-6** — *Steam Deck Tech Specs*
Autor: Valve | URL: https://www.steamdeck.com/en/tech
Concepto: 1280x800; 16 GB LPDDR5; APU Zen 2 4c/8t + 8 CUs RDNA 2, 4–15 W; SteamOS 3; modelo OLED hasta 90 Hz | Uso: frontera consola/PC | Complementario | Verif.: [V].

**B-7** — *Unity Manual 6000.3: Platform development*
Autor: Unity Technologies | Tipo: documentación oficial | URL: https://docs.unity3d.com/6000.3/Documentation/Manual/PlatformSpecific.html
Concepto: "Closed platforms": "Includes platforms that require confidentiality and legal agreements with the platform provider for using their developer tools and hardware." Ejemplos: PlayStation, Game Core for Xbox, Nintendo | Nivel: intro | Uso: definición canónica de plataforma cerrada | Obligatorio | Verif.: [V].

**B-8** — *Unity — Console game development (solutions/console)*
Autor: Unity | Tipo: página oficial (comercial) | URL: https://unity.com/solutions/console
Concepto: "an active Unity Pro subscription (or with a Preferred Platform license key provided by the respective platform holder) is required for development on these closed platforms"; "approval from each platform holder"; enlaces de registro: developer.nintendo.com/register, partners.playstation.net, ID@Xbox | Uso: requisitos de licencia | Obligatorio | Verif.: [V]. Contexto histórico (profesional): Game Developer, 4-ago-2021, regla vigente desde 30-jun-2021 para proyectos nuevos en 2021.2 — https://www.gamedeveloper.com/programming/going-forward-unity-devs-will-need-unity-pro-to-publish-on-consoles [V]. **No citar el precio de Unity Pro** de ese artículo (desactualizado).

**B-9** — *Nintendo Developer Portal — The Process*
Autor: Nintendo | URL: https://developer.nintendo.com/the-process (registro: https://developer.nintendo.com/register)
Concepto (público): 1) registro; 2) "accept the Non-Disclosure Agreement and Terms of Service to gain access to platform SDKs"; 3) desarrollo; 4) "Sign a publishing agreement, obtain an age rating, and submit your game for review by Nintendo"; 5) material de PR; 6) soporte post-lanzamiento. Registro exige mayoría de edad; acceso a Switch vía "Nintendo Switch Access Request form" | Uso: único proceso Nintendo documentable | Obligatorio | Verif.: [V].

**B-10** — *Complimentary PlayStation Development Hardware*
Autor: SIE Communications | Fecha: 26-jul-2022 | URL: https://sonyinteractive.com/en/news/blog/complimentary-development-hardware/
Concepto: socios nuevos aprobados reciben "one complimentary development kit and one complimentary test kit", a devolver en dos años; registro en partners.playstation.net | Uso: acceso a devkits | Complementario | Verif.: [V].

**B-11** — *Showing your Game to PlayStation*
Autor: John Vega y Shawne Benson (SIE) | Fecha mostrada: 7-abr-2026 (ver H: posible republicación) | URL: https://sonyinteractive.com/en/news/blog/showing-your-game-to-playstation/
Concepto: registro en PlayStation Partners con plan de proyecto; tras aprobación y firma del Global Developer and Publisher Agreement (GDPA) se accede a herramientas y documentación | Uso: único proceso Sony documentable públicamente | Obligatorio | Verif.: [V].

**B-12** — *Microsoft Game Dev — Publish (ID@Xbox)*
Autor: Microsoft | URL: https://developer.microsoft.com/en-US/games/publish (redirige desde xbox.com/developers/id)
Concepto: "you must be at least 18 years old", "you need to sign an NDA", país donde Microsoft opere; soporte a Unity, Unreal, Godot | Uso: acceso Xbox | Obligatorio | Verif.: [V].

**B-13** — *microsoft/GDK (repositorio público)*
Autor: Microsoft | Tipo: repositorio oficial | URL: https://github.com/microsoft/GDK (releases: https://github.com/microsoft/GDK/releases)
Concepto: GDK público para PC/Game Pass; "A version of the GDK with Xbox Extensions (GDKX) to target Xbox consoles is only available to licensed partners in a managed program" | Uso: frontera público/NDA | Complementario | Verif.: [V].

**B-14** — *Meet the Microsoft Game Developer Kit (GDK)*
Autor: Microsoft | Fecha: 20-jul-2021 | URL: https://developer.microsoft.com/en-us/games/articles/2021/07/meet-the-microsoft-game-developer-kit-gdk/
Concepto: GDK "previously only available to approved partners"; publicar requiere "applying to qualify for an Xbox partners program, signing a license agreement" | Uso: corrige la premisa "2024" | Complementario | Verif.: [V].

### B.2 Controladores y accesibilidad

**B-15** — *Introducing DualSense, the New Wireless Game Controller for PlayStation 5*
Autor: Hideaki Nishino (SIE) | Fecha: 7-abr-2020 | URL: https://blog.playstation.com/2020/04/07/introducing-dualsense-the-new-wireless-game-controller-for-playstation-5/
Concepto: hápticos ("slow grittiness of driving a car through mud") y gatillos adaptativos en L2/R2 ("tension of your actions, like when drawing a bow") | Uso: diseño de feedback háptico | Obligatorio | Verif.: [V].

**B-16** — *How to use DualSense wireless controllers with PC, Mac and mobile devices*
Autor: PlayStation (soporte) | URL: https://www.playstation.com/en-us/support/hardware/pair-dualsense-controller-bluetooth/
Concepto: gatillos adaptativos "available when supported by the game"; hápticos "requires a USB connection on PC. It isn't compatible with Mac computers and mobile devices" | Uso: por qué no se puede asumir una feature de mando | Obligatorio | Verif.: [V].

**B-17** — *Input System — Gamepad support* (paquete 1.14) + página de paquete para 6.3
Autor: Unity | URL: https://docs.unity3d.com/Packages/com.unity.inputsystem@1.14/manual/Gamepad.html ; versión para 6.3: https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.inputsystem.html ("Package version 1.20.0 is released for Unity Editor version 6000.3")
Concepto: `DualSenseGamepadHID` (macOS, Windows); `SwitchProControllerHID` en escritorio por Bluetooth; `SetMotorSpeeds(0.25f, 0.75f)`; `SetLightBarColor`; `PauseHaptics/ResumeHaptics/ResetHaptics`; rumble en consolas "Only supported if you install console-specific input packages" | Nivel: intermedio | Uso: práctica en aula | Obligatorio | Verif.: [V] ambas. Nota: la página equivalente en 1.20 no existe con el mismo nombre (404); usar 1.14 como referencia conceptual y revisar API en 1.20.

**B-18** — *PlayerInputManager* (1.14) y *Player Input Manager component* (1.20)
URL: https://docs.unity3d.com/Packages/com.unity.inputsystem@1.14/manual/PlayerInputManager.html ; https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/player-input-manager-component.html
Concepto: join al presionar un botón en dispositivo no emparejado / por acción / manual; "Use the Split-Screen option to automatically split the available screen space between the active players"; límite de jugadores | Uso: práctica de couch co-op | Obligatorio | Verif.: [V] ambas.

**B-19** — *Input Bindings (control schemes, rebinding)* (1.14)
URL: https://docs.unity3d.com/Packages/com.unity.inputsystem@1.14/manual/ActionBindings.html (en 1.20 existe https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/manual/interactive-rebinding.html — existencia comprobada por HTTP 200, contenido no leído)
Concepto: "Control Schemes use Binding groups to map Bindings ... to different types of Devices"; `PerformInteractiveRebinding()`; `SaveBindingOverridesAsJson()` / `LoadBindingOverridesFromJson()` | Uso: remapeo como accesibilidad | Obligatorio | Verif.: [V] 1.14.

**B-20** — *Xbox Adaptive Controller*
Autor: Microsoft | URL: https://www.xbox.com/en-US/accessories/controllers/xbox-adaptive-controller
Concepto: "Nineteen 3.5mm ports and two USB 2.0 ports"; 3 perfiles; desarrollado con AbleGamers, Cerebral Palsy Foundation, SpecialEffect, Warfighter Engaged | Uso: el juego no debe asumir un mando "estándar" | Obligatorio | Verif.: [V].

**B-21** — *Access controller for PS5 launches globally on December 6*
Autor: Isabelle Tomatis (SIE) | Fecha: 13-jul-2023 | URL: https://blog.playstation.com/2023/07/13/access-controller-for-ps5-launches-globally-on-december-6/
Concepto: 4 puertos 3,5 mm, hasta 30 perfiles, emparejar dos Access + un DualSense para juego colaborativo | Uso: ídem B-20 | Complementario | Verif.: [V].

**B-22** — *Xbox Accessibility Guidelines (índice)*
Autor: Microsoft | Fecha: v3.2 publicada 8-jun-2023 (página actualizada 2026) | URL: https://learn.microsoft.com/en-us/gaming/accessibility/guidelines (canónica: learn.microsoft.com/en-us/xbox/accessibility/guidelines)
Concepto: buenas prácticas, explícitamente **no** checklist de cumplimiento legal | Uso: marco de accesibilidad | Obligatorio | Verif.: [V].

**B-23** — *XAG 101 — Text display*
URL: https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/101
Concepto: tamaño mínimo por defecto en **consola: 26 px a 1080p, 52 px a 4K**; PC/VR: 18 px a 1080p; escalar hasta 200%; glifos también cumplen mínimo | Uso: UI de 10 pies con número concreto | Obligatorio | Verif.: [V].

**B-24** — *XAG 112 — UI navigation*
URL: https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/112
Concepto: "The UI is fully navigable by keyboard and controller digital input alone"; orden de foco lógico; bucle en menús lineales; menú de accesibilidad al primer arranque (ej. Minecraft Dungeons) | Uso: diseño de menús con mando | Obligatorio | Verif.: [V].

**B-25** — *Designing for Xbox and TV (UWP)*
Autor: Microsoft | Fecha: ms.date 24-sep-2020; **archivado** (previous-versions, UWP) | URL: https://learn.microsoft.com/en-us/windows/apps/design/devices/designing-for-tv (canónica archivada: https://learn.microsoft.com/en-us/previous-versions/windows/uwp/xbox-apps/designing-for-tv)
Concepto: "10-foot experience" ("approximately 10 feet away from the screen"); zona segura: "draw only non-essential visuals within 5% of the screen edges" (27 epx arriba/abajo, 48 epx laterales a 960x540 epx); máx. "six clicks" de borde a borde; texto ≥15 epx | Nivel: intro | Confiabilidad: oficial pero **archivado y orientado a apps UWP, no juegos** | Uso: conceptos de 10 pies y safe area, aclarando el contexto | Complementario | Verif.: [V].

**B-26** — *Game Accessibility Guidelines*
Autor: colaboración de estudios, especialistas y académicos | URL: https://gameaccessibilityguidelines.com/full-list/
Concepto: niveles Basic/Intermediate/Advanced; "Allow controls to be remapped / reconfigured" (Basic, Motor); subtítulos configurables | Confiabilidad: profesional | Uso: checklist multiplataforma | Complementario | Verif.: [V].

### B.3 Certificación, clasificación, publicación

**B-27** — *XBOX Requirements for XBOX Games* (v16.4, 08-sep-2026)
Autor: Microsoft | Tipo: requisitos oficiales públicos | URL: https://learn.microsoft.com/en-us/gaming/gdk/docs/store/policies/console/certification-requirements?view=gdk-2604
Concepto: definición de XR; XR-001 estabilidad; XR-003 calidad ("On consoles, the game must be fully navigable with a controller"; audio con auriculares conectados/desconectados); XR-130 paridad de generación; XR-022 terminología; XR-074 pérdida de conectividad; XR-013/014/015/018 seguridad, privacidad, comunicación, UGC; XR-112/115 usuario y mando; XR-045 privilegios; XR-064/067/070 multijugador y amigos | Nivel: intermedio | Uso: **fuente central del bloque de certificación** | Obligatorio | Verif.: [V]. Nota: metadatos de página marcan "permissioned-type: public".

**B-28** — *XBOX Requirements and Test Cases*
URL: https://learn.microsoft.com/en-us/gaming/gdk/docs/store/policies/console/console-certification-requirements-and-tests
Concepto: caso 115-02 (retirar pilas del mando en distintos puntos; pasa si "The user is prompted to re-establish a new active controller"); caso 112-08 (suspender 10 min, cambiar perfil A→B, reanudar) | Uso: modelo de plan de pruebas para el TP | Obligatorio | Verif.: [V] (v16.4, 11-ago-2026).

**B-29** — *Terminology (XBOX Required Terminology List)*
URL: https://learn.microsoft.com/en-us/gaming/gdk/docs/store/policies/console/console-certification-terminology
Concepto: nombres obligatorios ("View button", "Menu button", "XBOX button", "left bumper"/"LB", "vibration"); enlaza a "Forbidden Terms List (NDA topic)" → evidencia explícita de la frontera público/NDA | Uso: glifos y textos de UI | Obligatorio | Verif.: [V].

**B-30** — *Steam Deck and Steam Machine Compatibility Review*
Autor: Valve (Steamworks) | URL: https://partner.steamgames.com/doc/steamhardware/compat
Concepto: categorías Verified/Playable/Unsupported/Unknown; Verified exige soporte completo de mando, glifos acordes a la entrada activa, entrada de texto, ≥30 fps por defecto (800p Deck), texto legible a 12" (mín. 9 px), launcher navegable con mando | Uso: análogo público de certificación | Obligatorio | Verif.: [V]. Sin fecha en la página.

**B-31** — *IARC — International Age Rating Coalition*
URL: https://www.globalratings.com/
Concepto: sistema global de clasificación para juegos digitales, gratuito para desarrolladores | Uso: clasificación en tiendas digitales | Complementario | Verif.: [V]. (La lista de tiendas participantes no figuraba en el texto extraído → H.)

**B-32** — *PEGI age ratings*
URL: https://pegi.info/page/pegi-age-ratings
Concepto: PEGI 3/7/12/16/18; descriptores incl. "In-game purchases", "Unrestricted communication", "Paid random items" | Uso: UX social y monetización afectan la clasificación | Complementario | Verif.: [V].

**B-33** — *ESRB Ratings Guide*
URL: https://www.esrb.org/ratings-guide/
Concepto: E, E10+, T, M, AO, RP; "interactive elements" (compras, interacción de usuarios) no cambian la categoría pero informan | Complementario | Verif.: [V].

### B.4 Multijugador

**B-34** — *Fast-Paced Multiplayer (Parts I–IV)*
Autor: Gabriel Gambetta | Tipo: artículo profesional | URLs: https://www.gabrielgambetta.com/client-server-game-architecture.html ; https://www.gabrielgambetta.com/client-side-prediction-server-reconciliation.html ; https://www.gabrielgambetta.com/lag-compensation.html
Concepto: servidor autoritativo ("the one and only authority ... is the server"); predicción + reconciliación; interpolación; compensación de lag | Nivel: intro-intermedio | Uso: lectura base | Obligatorio | Verif.: [V] partes I, II, IV (parte III "Entity Interpolation" listada en el índice de la parte I, no abierta).

**B-35** — *Netcode for GameObjects 2.6 — manual*
URL: https://docs.unity3d.com/Packages/com.unity.netcode.gameobjects@2.6/manual/index.html
Concepto: "high-level networking library"; client-server y distributed authority; Unity 6.0+ | Uso: referencia (no implementar en profundidad) | Complementario | Verif.: [V]. Nota: `@latest` redirige a 3.1 (no leído).

**B-36** — *Netcode for Entities 1.5 — Intro to prediction*
URL: https://docs.unity3d.com/Packages/com.unity.netcode@1.5/manual/intro-to-prediction.html
Concepto: "The server is authoritative"; client prediction; `SimulationTickRate` vs `NetworkTickRate` | Uso: vocabulario de tick rate | Complementario | Verif.: [V].

**B-37** — *Multiplayer Play Mode 3.0*
URL: https://docs.unity3d.com/Packages/com.unity.multiplayer.playmode@3.0/manual/index.html
Concepto: probar varios jugadores sin salir del editor; hasta 4 Editor Players (principal + 3) y 4 instancias locales compiladas; **requiere Unity 6.3 LTS o superior** | Uso: demo en clase | Obligatorio | Verif.: [V].

**B-38** — *Network Simulator (Multiplayer Tools 2.2)*
URL: https://docs.unity3d.com/Packages/com.unity.multiplayer.tools@2.2/manual/network-simulator.html
Concepto: packet delay, jitter, packet loss, desconexiones, lag spikes; requiere Unity Transport ≥2.0 y NGO ≥1.1; funciona con la etapa de simulador de UTP | Uso: mostrar efecto de latencia | Obligatorio | Verif.: [V].

**B-39** — *Testing multiplayer games with artificial network conditions*
URL: https://docs.unity3d.com/Packages/com.unity.netcode.gameobjects@2.6/manual/tutorials/testing/testing_with_artificial_conditions.html
Concepto: valores de referencia de Boss Room (escritorio ~100–150 ms, 5–10% pérdida); probar a 100, 200, 500, 1000 ms; "testing purely with added delay and no packet loss and jitter is unrealistic"; Clumsy (Windows), Network Link Conditioner (macOS/iOS) | Uso: protocolo de prueba de latencia | Obligatorio | Verif.: [V].

**B-40** — *Matchmaker overview (Unity Gaming Services)*
URL: https://docs.unity.com/ugs/en-us/manual/matchmaker/manual/matchmaker-overview
Concepto: motor de reglas, backfill, relajación de reglas, parte del Multiplayer Services SDK | Uso: explicar qué es matchmaking como servicio | Complementario | Verif.: [V]. Precio no indicado en la página.

**B-41** — *Shared-Multi-Split Screen Design*
Autor: Richard Terrell | Tipo: blog en Game Developer | Fecha: 17-jun-2011 | URL: https://www.gamedeveloper.com/design/shared-multi-split-screen-design
Concepto: pantalla compartida vs split vs múltiples pantallas; "screen-looking"; split dinámico (Bionic Commando Rearmed) | Confiabilidad: profesional/blog | Uso: disparador de discusión | Complementario | Verif.: [V].

**B-42** — *The Impact of Game Patterns on Player Experience and Social Interaction in Co-Located Multiplayer Games*
Autores: Katharina Emmerich, Maic Masuch (U. Duisburg-Essen) | Tipo: académico (CHI PLAY '17) | Fecha: 15-oct-2017 | DOI: 10.1145/3116595.3116606 | URL verificada: https://api.crossref.org/works/10.1145/3116595.3116606 (metadatos)
Concepto (según resumen indexado, ver H): interdependencia, presión de tiempo, control compartido | Uso: base académica del couch co-op | Complementario | Verif.: [V] solo metadatos (título, autores, venue, pp. 411-422). El PDF en dl.acm.org devolvió 403.

**B-43** — *Latency and Player Actions in Online Games*
Autores: Mark Claypool, Kajal Claypool | Tipo: académico (Communications of the ACM 49(11):40-45, nov-2006) | DOI: 10.1145/1167838.1167860 | PDF del autor: https://web.cs.wpi.edu/~claypool/papers/precision-deadline/final.pdf
Concepto: acciones clasificadas por **precisión** y **deadline**; modelo avatar (1ª/3ª persona) vs omnipresente; caída "about 35%" de precisión de disparo a 100 ms; en 3ª persona y deportes sin caída significativa hasta ~500 ms | Uso: fundamentar "cuánta latencia tolera mi juego" | Obligatorio | Verif.: [V] PDF descargado y texto extraído; metadatos [V] vía Crossref.

### B.5 Optimización (Unity 6.3)

**B-44** — *Baldur's Gate 3 en Xbox Series S (caso)*
Fuentes (profesionales, no primarias): Kotaku, 24-ago-2023 — https://kotaku.com/baldurs-gate-3-xbox-series-x-s-split-screen-co-op-rpg-1850770513 [V]; Wccftech, 28-ago-2023 — https://wccftech.com/baldurs-gate-3-split-screen-on-xbox-series-s-might-still-happen-says-microsoft/ [V]; Shacknews, 28-ene-2025 — https://www.shacknews.com/article/142883/baldurs-gate-3-patch-8-xbox-series-s-splitscreen-coop [V]
Concepto: Vincke (citado por Kotaku): "Series S will not feature split-screen coop"; Phil Spencer a Eurogamer (citado por Kotaku): hay features en X que no están en S; Xbox (cuenta oficial, citada por Wccftech) prometió seguir trabajando; Patch 8 lo agregó | Uso: caso central límite de memoria ↔ modo de juego ↔ XR-130 | Obligatorio | Verif.: [V] artículos; **fuentes primarias no abiertas → H**.

**B-45** — *Choose a method for optimizing draw calls* (6000.3)
URL: https://docs.unity3d.com/6000.3/Documentation/Manual/optimizing-draw-calls-choose-method.html (landing URP: https://docs.unity3d.com/6000.3/Documentation/Manual/reduce-draw-calls-landing-urp.html [V])
Concepto: URP/HDRP: 1) GPU Resident Drawer, 2) SRP Batcher, 3) GPU instancing, BRG solo casos avanzados; Built-in: static batching, instancing, dynamic batching (legado) | Uso: orden actualizado | Obligatorio | Verif.: [V].

**B-46** — *GPU Resident Drawer (URP)*
URL: https://docs.unity3d.com/6000.3/Documentation/Manual/urp/gpu-resident-drawer.html
Concepto: usa BatchRendererGroup para instanciar automáticamente; requiere Forward+, compute shaders (no OpenGL ES); mejor con muchos objetos que comparten malla; aumenta tiempo de build | Obligatorio | Verif.: [V].

**B-47** — *Static and dynamic batching* (6000.3)
URL: https://docs.unity3d.com/6000.3/Documentation/Manual/DrawCallBatching.html
Concepto: static batching combina mallas estáticas en espacio de mundo; "For most uses, dynamic batching is no longer recommended" | Obligatorio | Verif.: [V].

**B-48** — *Level of detail (LOD)* (6000.3)
URL: https://docs.unity3d.com/6000.3/Documentation/Manual/LevelOfDetail.html
Concepto: LOD reduce carga de render; 6.3 tiene **Mesh LOD** (reducción de polígonos con poca memoria) y **LOD Group** (más flexible: material y draw calls) | Obligatorio | Verif.: [V].

**B-49** — *Occlusion culling* (6000.3)
URL: https://docs.unity3d.com/6000.3/Documentation/Manual/OcclusionCulling.html
Concepto: baked (datos precomputados por celdas) vs GPU occlusion culling (URP/HDRP) | Obligatorio | Verif.: [V].

**B-50** — *Introduction to mipmaps* (6000.3)
URL: https://docs.unity3d.com/6000.3/Documentation/Manual/texture-mipmaps-introduction.html
Concepto: mipmaps aumentan tamaño de textura 33% en disco y memoria; Mipmap Streaming controla qué niveles se cargan | Obligatorio | Verif.: [V].

**B-51** — *Profiler Highlights module* y *Frame Debugger* (6000.3)
URLs: https://docs.unity3d.com/6000.3/Documentation/Manual/ProfilerHighlights.html ; https://docs.unity3d.com/6000.3/Documentation/Manual/FrameDebugger.html ; índice: https://docs.unity3d.com/6000.3/Documentation/Manual/analysis.html
Concepto: Highlights marca frames donde CPU (rojo) o GPU (amarillo) exceden el tiempo objetivo; Frame Debugger permite recorrer los eventos de render de un frame | Obligatorio | Verif.: [V].

**B-52** — *Dynamic Resolution* (6000.3)
URL: https://docs.unity3d.com/6000.3/Documentation/Manual/DynamicResolution-landing.html
Concepto: renderizar a menor resolución dinámicamente para reducir trabajo de GPU | Complementario | Verif.: [V]. Plataformas soportadas no figuraban en el texto leído.

(Total: 52 fichas, B-1 a B-52; supera el rango pedido de 30–45. Si hay que recortar, B-1 a B-6 son páginas de especificaciones que se pueden pasar como datos a la sección E, y B-52, B-36, B-35 son prescindibles. Algunas fichas agrupan páginas hermanas del mismo sitio.)

---

## C) Videos (todos verificados con oEmbed; duración: no verificada salvo indicación)

| # | Título exacto (oEmbed) | Canal | URL | Fecha | Fragmento | Concepto | Uso |
|---|---|---|---|---|---|---|---|
| C1 | Overwatch Gameplay Architecture and Netcode | GDC Festival of Gaming | https://www.youtube.com/watch?v=W3aieHjyNvw | GDC 2017 (no verificado en el video) | a determinar | ECS, predicción, netcode preciso | consulta (avanzado) |
| C2 | 8 Frames in 16ms: Rollback Networking in Mortal Kombat and Injustice 2 | GDC Festival of Gaming | https://www.youtube.com/watch?v=7jb0FOcImdg | GDC 2018 (según buscador) | a determinar | rollback en juegos de pelea | consulta; fragmento corto en clase |
| C3 | I Shot You First: Networking the Gameplay of Halo: Reach | GDC Festival of Gaming | https://www.youtube.com/watch?v=h47zZrqjgLc | GDC 2011 (GDC Vault [V]: https://www.gdcvault.com/play/1014345/I-Shot-You-First-Networking, gratuito) | a determinar | priorización de red, autoridad, "quién disparó primero" | consulta |
| C4 | It IS Rocket Science! The Physics of Rocket League Detailed | GDC Festival of Gaming | https://www.youtube.com/watch?v=ueEmiDM94IE | GDC 2018 (GDC Vault [V], gratuito) | sección "Networking" (último tercio; tiempo exacto a determinar) | física a 60 Hz fijos + networking | clase (fragmento) |
| C5 | The Making of the Xbox Adaptive Controller | GDC Festival of Gaming | https://www.youtube.com/watch?v=33ErZIQ7AGI | no verificada | a determinar | diseño de hardware accesible | consulta |
| C6 | The Accessibility in Last of Us Part II: A 3 Year Journey | IGDA GASIG | https://www.youtube.com/watch?v=5HDdino-umA | no verificada | a determinar | accesibilidad AAA en consola | clase (fragmento) |
| C7 | Updates from Xbox: The Xbox Accessibility Guidelines & Microsoft Game Accessibility Testing Service | IGDA GASIG | https://www.youtube.com/watch?v=1MqDgM4xSns | no verificada | a determinar | XAG en la práctica | consulta |
| C8 | Boosting your game performance with Unity 6 Profiling tools \| Unite 2024 | Unity | https://www.youtube.com/watch?v=_cV1B2hqXGI | Unite 2024 | a determinar | flujo de profiling Unity 6 | clase |
| C9 | Graphics rendering: Getting the best performance with Unity 6 \| Unite 2024 | Unity | https://www.youtube.com/watch?v=Oc6T4hh5gaI | Unite 2024 | a determinar | GPU Resident Drawer, culling, etc. | clase |
| C10 | Unity Profiler Walkthrough & Tutorials (playlist, 3 videos) | Unity | https://youtube.com/playlist?list=PLX2vGYjWbI0QNVu6deCYvWGX7Gj0GmdmE | página Unity del 13-jun-2025 [V] | video 1 (Profiler) | Profiler, Profile Analyzer, Memory Profiler | clase/consulta |
| C11 | Input System Tutorials (playlist, 7 videos; el 7º: local multiplayer con Player Input Manager) | Unity | https://youtube.com/playlist?list=PLX2vGYjWbI0RpLvO3B7aH-ObfcOifMD20 | página Unity del 13-jun-2025 [V] | videos 6 y 7 | PlayerInput, PlayerInputManager, rebinding (video 5) | clase |
| C12 | Doom Eternal Switch: The Making Of An 'Impossible' Port - id Software/Panic Button Interview | Digital Foundry | https://www.youtube.com/watch?v=Zw0QEgOLhDs | no verificada | a determinar | port a hardware limitado | consulta |
| C13 | The Witcher 3 on Switch Hands-on – The Most Ambitious Switch Port Ever? | Digital Foundry | https://www.youtube.com/watch?v=QNcHI8mm9gI | no verificada (2019 según contexto) | a determinar | resolución dinámica y recortes en Switch | clase (fragmento) |
| C14 | The Witcher 3 Remastered - Switch 2 Tech Review - A Colossal Upgrade over Switch 1 | Digital Foundry | https://www.youtube.com/watch?v=qaoqPjbXk2Y | no verificada | a determinar | salto Switch → Switch 2 | consulta |
| C15 | Hogwarts Legacy - Nintendo Switch Review - Massive Downgrades... But Does It Work? | Digital Foundry | https://www.youtube.com/watch?v=QWMpPABozKo | no verificada | a determinar | LOD, texturas, densidad reducidas | clase (fragmento) |
| C16 | Hogwarts Legacy - Switch 2 Review - The Big Face-Off vs Series S, PS4 and Switch 1 | Digital Foundry | https://www.youtube.com/watch?v=MAl9NcEDO1s | no verificada | a determinar | comparación multiplataforma | clase (fragmento) |
| C17 | Xbox Series S: Would More Memory Have Improved Its Prospects? | DF Clips | https://www.youtube.com/watch?v=M4JYPqyQ-ec | no verificada | a determinar | memoria como límite | consulta |
| C18 | Did Xbox Series S 'Prepare' Developers for Switch 2 Ports? | DF Clips | https://www.youtube.com/watch?v=TqDmi8J-JBM | no verificada | a determinar | escalado entre SKUs | consulta |
| C19 | Nintendo Switch 'Impossible Ports' - The Best Of The Best | DF Clips | https://www.youtube.com/watch?v=e9silZU-l1M | no verificada | a determinar | panorama de ports | consulta |

Charla no YouTube: *Creating the Soundscape of 'It Takes Two'* — Mongeau y Enigk Sjöberg (Hazelight), GDC 2021, gratuita — https://www.gdcvault.com/play/1027157/Creating-the-Soundscape-of-It [V]. Concepto: audio en split-screen (espacialización con dos oyentes). Uso: consulta.

Advertencia: Digital Foundry es **análisis profesional de terceros**, no fuente primaria del estudio (salvo C12, que es entrevista a los desarrolladores).

---

## D) PDFs y documentos descargables

| # | Documento | Autor | Fecha | URL | Tipo / costo | Verif. |
|---|---|---|---|---|---|---|
| D1 | Optimize your game performance for consoles and PCs in Unity (Unity 6 edition) | Unity | 17-oct-2024 | https://unity.com/resources/console-pc-game-performance-optimization-unity-6 | e-book oficial, gratuito; enfoque HDRP; destaca Adaptive Probe Volumes, GPU Resident Drawer, GPU Occlusion Culling (según blog [V] https://unity.com/blog/unity-6-game-optimization-guides, 11-nov-2024, T. Krogh-Jacobsen) | [V] página de descarga; PDF no abierto |
| D2 | Ultimate guide to profiling Unity games (Unity 6 edition) | Unity | 11-jul-2025 | https://unity.com/resources/ultimate-guide-to-profiling-unity-games-unity-6 | e-book oficial, gratuito, ~100 págs. | [V] página; PDF no abierto |
| D3 | Latency and Player Actions in Online Games (CACM 2006) | M. y K. Claypool | nov-2006 | https://web.cs.wpi.edu/~claypool/papers/precision-deadline/final.pdf | paper, copia del autor | [V] PDF leído |
| D4 | Latency Can Kill: Precision and Deadline in Online Games (MMSys 2010) | M. y K. Claypool | feb-2010 | http://web.cs.wpi.edu/~claypool/papers/precision-deadline-mmsys/ | paper (página del autor con PDF) | [V] página; PDF no abierto |
| D5 | It IS Rocket Science! The physics and networking of Rocket League (slides GDC 2018) | Jared Cone (Psyonix) | 2018 | https://media.gdcvault.com/gdc2018/presentations/Cone_Jared_It_Is_Rocket.pdf | slides, 182 págs., gratuito | [V] PDF leído (agenda: Physics Engine / Vehicle Tuning / Networking; física a 60 Hz) |
| D6 | The Impact of Game Patterns on Player Experience and Social Interaction in Co-Located Multiplayer Games | Emmerich & Masuch | oct-2017 | DOI 10.1145/3116595.3116606 | paper ACM (acceso posiblemente pago) | [V] metadatos Crossref; PDF 403 |

No encontré paper académico verificable específico sobre **split-screen** (diseño de pantalla dividida); D6 es lo más cercano (juego co-localizado).

---

## E) Datos técnicos verificados citables

| Dato | Valor | Fuente |
|---|---|---|
| Lanzamiento Switch 2 | 5-jun-2025 | B-1 |
| Switch 2 pantalla / dock | 7,9" 1920x1080 HDR10, VRR hasta 120 Hz / hasta 3840x2160 a 60 fps | B-2 |
| Joy-Con 2 | acelerómetro, giroscopio, sensor de mouse, HD Rumble 2, botón C | B-2 |
| GameChat | hasta 12 personas; requiere Nintendo Switch Online pago (gratis hasta 31-mar-2026) | B-1 |
| PS5 Pro | 7-nov-2024; +67% CUs, memoria +28% más rápida, hasta +45% render; PSSR | B-3 |
| Xbox Series S | 10 GB GDDR6 (bus 128 bit), 4 TFLOPS, objetivo 1440p | B-4 |
| Xbox Series X | 16 GB GDDR6 (bus 320 bit), 12 TFLOPS, 4K | B-5 |
| Steam Deck | 1280x800, 16 GB LPDDR5, 4–15 W | B-6 |
| Plataforma cerrada (Unity) | "require confidentiality and legal agreements with the platform provider" | B-7 |
| Licencia Unity para consolas | Unity Pro o "Preferred Platform license key" + aprobación del fabricante | B-8 |
| XR paridad de generación | XR-130: saves compatibles, sin segmentar online, "identical game modes" en toda la generación | B-27 |
| XR navegación | XR-003: "On consoles, the game must be fully navigable with a controller" | B-27 |
| XR mando | XR-115: si se quita el mando activo, "titles must allow reestablishment of a new active controller" | B-27 |
| XR suspensión | XR-112: al reanudar, validar el par usuario/mando | B-27 |
| XR multijugador local | XR-045: el privilegio 254 "doesn't pertain to local multiplayer games run on the same device" | B-27 |
| Texto mínimo consola (XAG 101) | 26 px a 1080p; 52 px a 4K; escalable a 200% | B-23 |
| Zona segura TV (UWP, archivado) | UI esencial fuera del 5% del borde (27/48 epx a 960x540) | B-25 |
| Steam Deck Verified | ≥30 fps por defecto, texto ≥9 px legible a 12" | B-30 |
| Mipmaps | +33% de tamaño en disco y memoria | B-50 |
| Dynamic batching | "no longer recommended" en la mayoría de los casos | B-47 |
| Prioridad draw calls URP/HDRP | GPU Resident Drawer → SRP Batcher → GPU instancing | B-45 |
| GPU Resident Drawer | Forward+ y compute shaders; no OpenGL ES | B-46 |
| Multiplayer Play Mode 3.0 | requiere Unity 6.3 LTS+; hasta 4 Editor Players | B-37 |
| Input System para 6.3 | versión 1.20.0 | B-17 |
| Pruebas de red (NGO/Boss Room) | escritorio 100–150 ms, 5–10% pérdida; probar 100/200/500/1000 ms | B-39 |
| Latencia (Claypool 2006) | tiro de precisión en 1ª persona: caída ~35% a 100 ms; 3ª persona/deportes: sin caída significativa hasta ~500 ms; LAN <10 ms; ~50 ms intra-continente | B-43 |
| Rocket League | física con paso fijo a 60 Hz | D5 |
| GDK público en GitHub | desde jul-2021; GDKX (consola) solo socios licenciados | B-13, B-14 |
| Dev kits PS5 gratuitos | 1 dev kit + 1 test kit a socios nuevos aprobados, devolución en 2 años (jul-2022) | B-10 |
| Cyberpunk 2077 | Sony lo retiró de PS Store con reembolsos en dic-2020 | **NO verificado con fuente abierta** → H |

---

## F) Certificación: PÚBLICO vs NO PÚBLICO

| Aspecto | Microsoft (Xbox) | Sony (PlayStation) | Nintendo | Valve (Steam Deck, referencia) |
|---|---|---|---|---|
| Existencia de un proceso de aprobación previo a publicar | PÚBLICO (XR; "All products that integrate Xbox services ... must be certified") | PÚBLICO solo como hecho general (registro, GDPA) | PÚBLICO: "submit your game for review by Nintendo" | PÚBLICO (Compatibility Review) |
| Texto completo de requisitos técnicos | **PÚBLICO**: XBOX Requirements v16.4 en Microsoft Learn | **NO PÚBLICO** (TRC bajo NDA; no encontré documento oficial abierto) | **NO PÚBLICO** (guidelines/Lotcheck tras NDA del portal) | PÚBLICO |
| Casos de prueba | **PÚBLICO** (XR and Test Cases) | NO PÚBLICO | NO PÚBLICO | PÚBLICO (criterios Verified) |
| Terminología obligatoria | PÚBLICO (Terminology List); **"Forbidden Terms List" = NDA** | NO PÚBLICO | NO PÚBLICO | N/A (pide glifos correctos) |
| SDK / herramientas de consola | GDK de PC público; **GDKX = solo socios licenciados** | NO PÚBLICO (tras GDPA) | NO PÚBLICO (tras NDA) | Steamworks SDK público |
| Acceso / registro | PÚBLICO: ≥18 años, NDA, país habilitado | PÚBLICO: registro en PlayStation Partners + plan de proyecto + GDPA | PÚBLICO: registro, mayoría de edad, NDA, formulario de acceso | PÚBLICO |
| Devkits | condiciones no detalladas públicamente (no verificado) | PÚBLICO: kits gratuitos en préstamo a socios nuevos (2022) | NO PÚBLICO (no figura en lo leído) | no aplica |
| Accesibilidad | PÚBLICO: XAG (buenas prácticas, no certificación) | no hay guía pública equivalente verificada | no hay guía pública verificada | no aplica |
| Clasificación por edad | se valida al enviar (XR-017 retirado ago-2026) | PÚBLICO a nivel general (IARC/ESRB/PEGI) | PÚBLICO: "obtain an age rating" | IARC/autodeclaración (no verificado) |
| Costos de certificación / re-envío | NO PÚBLICO (no encontrado) | NO PÚBLICO | NO PÚBLICO | — |

Regla para clase: **lo de Microsoft se puede citar textualmente; de Sony y Nintendo solo los pasos públicos del proceso de alta**. No describir TRC, Lotcheck ni tiempos internos.

---

## G) Fuera de alcance (no convertir la unidad en otro curso)

- Implementación completa de netcode (snapshots, delta compression, rollback propio, NAT punch-through, relay). Se enseñan conceptos y se demuestran con Multiplayer Play Mode + Network Simulator.
- Arquitectura de hardware detallada (pipelines de GPU, caches, ISA). Solo cifras públicas que impactan diseño (memoria, resolución objetivo, modos).
- Escritura de shaders y técnicas avanzadas de rendering (ray tracing, upscalers como PSSR/DLSS en detalle).
- Backend de servicios (PlayFab, UGS a fondo, servidores dedicados, orquestación).
- Programación con SDKs de consola (imposible sin NDA y devkit).
- Legal/comercial de publicación (contratos, impuestos, precios) más allá del flujo general.
- Anti-cheat y seguridad de red.

---

## H) NO VERIFICADO (no usar en clase sin re-verificar)

1. **Valve Developer Wiki "Source Multiplayer Networking"** (https://developer.valvesoftware.com/wiki/Source_Multiplayer_Networking): WebFetch 403; con curl redirige a un desafío anti-bot. Contenido (tick rate, interpolación 100 ms, lag compensation) **no verificado**.
2. **Comunicado de Sony sobre Cyberpunk 2077 (dic-2020)**: CNBC devolvió 403; el texto citado solo apareció en resúmenes del buscador. No hay URL oficial de Sony verificada.
3. **Witcher 3 en Switch — entrevista DF/Eurogamer a Saber (3,5 GB de RAM disponible, eliminación de LOD0 en cinemáticas)**: Eurogamer bloqueado para la herramienta; dato solo visto en resúmenes de buscador.
4. **DOOM (2016) en Switch por Panic Button**: no encontré entrevista técnica verificable; solo la de **Doom Eternal** (C12).
5. **Hogwarts Legacy Switch**: fecha de lanzamiento y detalles técnicos no verificados más allá de los títulos de video de DF.
6. **Fuentes primarias de BG3**: tweet/post de Swen Vincke, declaración de Phil Spencer a Eurogamer, post de Xbox en X, página oficial de Patch 8 (baldursgate3.game devolvió 500). Solo verificadas vía prensa (B-44). La "excepción" a XR-130 para BG3 es **INFERENCIA** (Kotaku señala la ambigüedad).
7. **Switch 2: 12 GB de RAM** — aparece en buscadores atribuido a nintendo.com, pero no figura en el texto que extraje de la página.
8. **Charla GDC sobre diseño de split-screen**: no encontré ninguna verificable. La de It Takes Two verificada es de **audio**.
9. **Duraciones** de todos los videos de la sección C (oEmbed no informa duración). "42 min" de C8 viene de Class Central, no verificado.
10. **Fecha de "Showing your Game to PlayStation"** (B-11): la página indica 7-abr-2026, pero prensa reportó una guía similar en mar-2021; puede ser republicación.
11. **Requisitos de PlayStation Partners** (entidad legal, IP estática, dominio corporativo): solo en fuentes de terceros.
12. **Precio de Unity Pro** actual: no verificado (el de 2021 está desactualizado).
13. **Lista de tiendas participantes de IARC** (Nintendo eShop, PlayStation Store, Microsoft Store, Google Play): no apareció en la página leída.
14. **Contenido de los PDFs D1 y D2** (solo se verificaron las páginas de descarga).
15. **Resumen/hallazgos de Emmerich & Masuch 2017**: solo metadatos verificados; el resumen proviene del buscador.
16. **"The Last of Us Part II, más de 60 opciones de accesibilidad"**: dato de prensa, no verificado en fuente de Sony.
17. **Gambetta parte III (Entity Interpolation)**: listada en la parte I, URL no abierta.
18. **Netcode for GameObjects 3.1** (destino de `@latest`): no leído; se usó 2.6.
19. Páginas de Input System 1.20 equivalentes a "Gamepad" y "Supported devices" con tabla de mandos: no encontradas (404 o contenido distinto).
