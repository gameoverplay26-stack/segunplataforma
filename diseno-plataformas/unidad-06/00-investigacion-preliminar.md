# Investigación de apoyo — UNIDAD 6: Diseño según Plataforma de PC

Cátedra: Diseño según Plataformas de Juego (UNJu). Motor de referencia: Unity 6000.3.11f1 (Unity 6.3 LTS).
Fecha de consulta de todas las fuentes: **2026-10-04** (salvo que se indique otra cosa).
Regla aplicada: toda URL listada en B–F fue abierta con WebFetch (YouTube vía oEmbed). Lo que no se pudo abrir está en H.
Convenciones: **[HECHO]** = dicho por la fuente; **[INFERENCIA]** = conclusión docente/del investigador, no textual de la fuente.

---

## A) Auditoría del programa

| # | Qué dice el programa | Estado | Problema | Qué enseñar | Por qué | Fuente |
|---|---|---|---|---|---|---|
| 1 | "Flexibilidad de hardware y configuraciones" | CORRECTO PERO INCOMPLETO | Presenta la flexibilidad solo como ventaja; omite el costo: la combinatoria de CPU×GPU×driver×SO×resolución es el principal riesgo de QA en PC. | Heterogeneidad con datos reales (Steam Survey, septiembre 2026): 1920×1080 sigue siendo la resolución primaria más común (47,91%), 32 GB de RAM la más común (42,22%) y 16 GB la VRAM más común (27,21%). La "flexibilidad" es a la vez una oportunidad de diseño y una superficie de bugs. | Sin datos, el alumno diseña para su propia máquina. | Steam HW Survey (B1); NIST combinatorial (B30) |
| 2 | "Diversidad de componentes y compatibilidad" | REQUIERE PRECISIÓN | Mezcla "compatibilidad" con "rendimiento". En el programa no queda definido qué es compatibilidad. | Definiciones de ISO/IEC 25010 (vía iso25000.com): *Compatibilidad*, *Adaptabilidad*, *Escalabilidad* (como subcaracterística de *Flexibilidad*), *Eficiencia de desempeño*. Agregar la capa que el programa no nombra: **drivers y APIs gráficas** (DX11/DX12/Vulkan/Metal; OpenGL deprecado en macOS desde 10.14). | Una gran parte de los bugs "de PC" vienen del stack de drivers y no del código del juego (Unity lo documenta para D3D12). | B3, B4, B5, B6, B33 |
| 3 | "Uso de teclado y mouse" | CORRECTO PERO INCOMPLETO | No menciona remapeo, sensibilidad, ni accesibilidad. | Input System: Actions → Bindings → Control Schemes; remapeo interactivo (`PerformInteractiveRebinding`), guardar los overrides en JSON y el sample "Rebinding UI". La XAG 107 exige poder remapear **todos** los controles, incluido Esc en PC, y una sensibilidad ajustable ±50%. | La XAG 107 y las Game Accessibility Guidelines tratan el remapeo como requisito básico. | B9, B10, B12, B13 |
| 4 | "Compatibilidad con controladores y configuraciones híbridas" | REQUIERE PRECISIÓN | "Configuraciones híbridas" es ambiguo. Falta: detectar el dispositivo activo, cambiar los glyphs y Steam Input. | Enseñar el cambio automático de Control Scheme (`PlayerInput.onControlsChanged`, `currentControlScheme`) y prompts dinámicos. Para Steam Deck Verified, *"On-screen glyphs must match the inputs being used"*. Steam Input puede remapear por encima del juego. HID genérico/HOTAS: layouts autogenerados con limitaciones y layouts custom. | Es un criterio público de certificación (Deck Verified) y un problema real de UX. | B11, B14, B15, B16 |
| 5 | "Ajustes de calidad gráfica" | CORRECTO PERO INCOMPLETO | No distingue entre escalar contenido y escalar resolución. | Quality Levels por plataforma, un URP Asset por nivel, `QualitySettings.SetQualityLevel(i, applyExpensiveChanges)`; Render Scale + Upscaling Filter (FSR 1, STP); AA (MSAA/FXAA/SMAA/TAA, con sus incompatibilidades); sombras (distancia, cascadas, resolución); Global Mipmap Limit. | Es el núcleo práctico de la unidad y sale directo de la documentación de Unity 6.3. | B17–B22 |
| 6 | "Soporte a diferentes resoluciones" | CORRECTO PERO INCOMPLETO | Faltan aspect ratio (16:10 en Steam Deck, 21:9), modos de pantalla y HDR. | `FullScreenMode` (ExclusiveFullScreen solo en Windows; FullScreenWindow; MaximizedWindow; Windowed); `Screen.SetResolution` (refresh rate solo en exclusive); Deck: 1280×800 y fuente mínima de 9 px. HDR Output en URP: DX11 no admite HDR en exclusive fullscreen. | Muchos bugs de UI aparecen recién con aspect ratios no 16:9. | B23, B24, B16, B25 |
| 7 | "Compatibilidad con GPUs de distintos niveles" | REQUIERE PRECISIÓN | Mezcla compatibilidad (¿arranca? ¿tiene la API?) con escalabilidad (¿rinde?). | Separar: (a) piso de compatibilidad = APIs y requisitos mínimos (Unity 6.3 Player en Windows: GPU con DX10/11/12/Vulkan; Linux: OpenGL 3.2+/Vulkan; macOS: Metal); (b) escalabilidad = presets, render scale y upscalers; (c) VRAM como límite duro (caso The Last of Us Part I). Dynamic Resolution en Windows **solo con DX12**. DLSS solo en HDRP y solo en Windows 64 bits. | Evita enseñar "upscaler = compatibilidad". | B7, B19, B20, B26, B27 |
| 8 | "Cultura del modding en PC" | CORRECTO PERO INCOMPLETO | Le falta respaldo académico y la tensión económica. | Postigo 2007 (valor de los mods), Sotamaa 2010 (motivaciones), Kücklich 2005 ("playbour", trabajo no pago). Hitos: Doom (código fuente liberado en 1997), Bethesda (herramientas oficiales desde Morrowind 2002, según GDC 2015), Creation Kit. | La cultura del modding tiene literatura revisada por pares. | B34–B37, B39, V5 |
| 9 | "Impacto en la longevidad de los videojuegos" | FALTA DESARROLLAR | Es una afirmación sin evidencia. | Evidencia: Kücklich (los mods extienden el ciclo de vida del producto), Schreiner & von Mammen 2021 ("enhanced lifespan" y más esfuerzo de desarrollo), Poretski & Arazy 2017 (estudio de valor y ventas, no open access). Contraejemplo: paid mods de Skyrim, revertidos en días. | Hay que distinguir el dato de la creencia. | B36, B38, B37, B40 |
| 10 | "Herramientas y soporte para mods" | DESACTUALIZADO / REQUIERE PRECISIÓN | No aclara qué ofrece Unity. | Unity **no** trae soporte de mods "out of the box". AssetBundles: *"AssetBundles can't contain assemblies"*, así que sirven para contenido (assets, ScriptableObjects) pero no para código C# nuevo. Addressables 2.10.3 (Unity 6.3) gestiona el contenido. Steam Workshop (ISteamUGC) y mod.io sirven para distribuir. | Es una decisión de arquitectura temprana: data-driven vs. scripting. | B41–B45 |
| 11 | (ausente) Riesgos del modding | FALTA UN TEMA IMPORTANTE | No están la seguridad, el cheating ni lo legal. | Caso Cities: Skylines (feb. 2022): un mod con auto-updater que funcionaba como backdoor. Paid mods de Skyrim (abril de 2015). Cheating en multijugador [INFERENCIA docente: no hay fuente específica verificada]. EULA/ToS. | Riesgos reales y documentados. | B46, B40 |
| 12 | "Pruebas en Windows, Linux y MacOS" | REQUIERE PRECISIÓN | En 2026, "Linux" en PC de juego significa sobre todo SteamOS/Steam Deck y Proton, no solo un build nativo. macOS exige firma y notarización. | Linux: build nativo vs. Proton (Wine + DXVK + vkd3d-proton). Deck Verified como checklist público. macOS: Developer ID + notarización (obligatoria desde Catalina para software firmado con Developer ID); Apple silicon vs. Intel (build Universal); Rosetta: macOS 27 es la última versión con soporte general. | Son los requisitos de distribución reales. | B47–B52 |
| 13 | "Compatibilidad y optimización según sistema operativo" | CONFUSO | Mezcla dos actividades distintas. | Compatibilidad = matriz de configuraciones (pairwise/combinatorial testing). Optimización = profiling por plataforma (e-book de Unity 6). Telemetría: Unity Cloud Diagnostics **está deprecado**; el reemplazo es Diagnostics (Unity 6.2+). | Separar "¿funciona?" de "¿rinde?". | B30, B53, B54, D1 |
| 14 | "Uso de entornos de virtualización y contenedores para testing" | REQUIERE PRECISIÓN (riesgo de concepto erróneo) | Sugiere que VMs y contenedores reemplazan el hardware real. No es así para GPU, input, rendimiento ni macOS. | Ver la sección F. Los contenedores comparten kernel: sirven para CI headless (GameCI, `unityci/editor`), no para probar otro SO de escritorio con GPU. Las VMs sirven para instalación, rutas y permisos. La GPU virtual es limitada (VirtualBox 3D "experimental"; Hyper-V GPU-P solo en Windows Server 2025 con GPUs de datacenter). macOS en VM: hasta 2 copias y solo sobre hardware Apple (SLA). | Es la parte más débil del programa. | F, B55–B62 |
| 15 | (ausente) CI / automatización de builds | FALTA UN TEMA IMPORTANTE | No aparece. | Unity Test Framework: Play Mode tests en un Player standalone. GameCI (los builds de macOS requieren runner macOS). Unity Build Automation (servicio cloud). | Es la práctica profesional real y conecta con la unidad de testing ya dada. | B63–B66 |
| 16 | (ausente) Caso de estudio de un port fallido | FALTA DESARROLLAR | No hay casos. | Batman: Arkham Knight (venta suspendida el 24/25 de junio de 2015). The Last of Us Part I PC (2023, VRAM/CPU; Digital Foundry). Caso positivo: DOOM Eternal (análisis de settings de DF). | Los casos concretos fijan los conceptos. | B67, V1–V4 |

---

## B) Fichas de fuentes

Formato: Título / Autor / Tipo / Fecha / URL / Tema / Unidad 6 / Concepto / Nivel / Confiabilidad / Uso en clase / Obligatorio-Complementario / Verificación

**B1** Steam Hardware & Software Survey (September 2026) / Valve / dato vivo oficial / septiembre 2026 (consultado 2026-10-04) / https://store.steampowered.com/hwsurvey / heterogeneidad / §Entorno PC / [HECHO] SO: Windows 95,03%, Linux 3,05%, macOS 1,92%. RAM más común: 32 GB (42,22%). VRAM más común: 16 GB (27,21%). Resolución primaria más común: 1920×1080 (47,91%) / Inicial / Alta (es una muestra opt-in de usuarios de Steam, no de "todos los PC") / Abrir el sitio en vivo en clase; discutir el sesgo de la muestra / OBLIGATORIO / WebFetch OK.

**B2** Steam Survey – Video Card Usage / Valve / dato vivo / septiembre 2026 / https://store.steampowered.com/hwsurvey/videocard/ / GPUs / §GPUs / [HECHO] Top: RTX 5070 6,15%, RTX 5060 4,40%, RTX 5060 Ti 4,06%, RTX 4060 3,89%, RTX 3060 3,66%… GTX 1650 2,19% (en el puesto 10). ⚠ La página principal muestra RTX 5070 = 5,86%; probablemente usa otra agregación (no verificado por qué). Citar cada número con su página. / Inicial / Alta / Mostrar la "cola larga": una GPU de 2019 sigue en el top 10 / OBLIGATORIO / WebFetch OK.

**B3** Graphics API support / Unity / doc oficial 6.3 / vigente / https://docs.unity3d.com/6000.3/Documentation/Manual/GraphicsAPIs.html / APIs / §Compatibilidad / [HECHO] Unity 6.3 soporta DirectX, Metal, OpenGL y Vulkan "depending on the availability of the API on a particular platform" / Inicial / Alta / Mapa de APIs por SO / OBLIGATORIO / OK.

**B4** Configure graphics APIs / Unity / doc 6.3 / https://docs.unity3d.com/6000.3/Documentation/Manual/configure-graphicsAPIs.html / Auto Graphics API / §Compatibilidad / [HECHO] Con Auto Graphics API desactivado, la API de arriba en la lista es la default y, si el sistema no la soporta, Unity prueba la siguiente / Intermedio / Alta / Demo en Player Settings / OBLIGATORIO / OK.

**B5** New in Unity 6.1 / Unity / doc 6.3 / https://docs.unity3d.com/6000.3/Documentation/Manual/WhatsNewUnity61.html / DX12 default / [HECHO] "DirectX 12 is now the default graphics API for new projects targeting the Windows platform." / Inicial / Alta / Dato citable / COMPLEMENTARIO / OK.

**B6** Troubleshoot D3D12 GPU crashes on Windows / Unity / doc 6.3 / https://docs.unity3d.com/6000.3/Documentation/Manual/windows-troubleshoot-gpu-crash.html / drivers / §Diversidad de componentes / [HECHO] "Unity doesn't communicate directly with your GPU. Instead, it relies on a layered driver stack…". Tipos de fallo: GPU timeout, page fault, crash del driver, VRAM agotada. Herramienta: DRED (`-force-d3d12-debug`) / Avanzado / Alta / **Fuente clave para explicar por qué los drivers causan bugs específicos** / OBLIGATORIO / OK.

**B7** System requirements for Unity 6.3 / Unity / doc 6.3 / https://docs.unity3d.com/6000.3/Documentation/Manual/system-requirements.html / requisitos / §Compatibilidad / [HECHO] Player Windows: Windows 10 21H1+ (x86, x64, Arm64), GPU DX10/DX11/DX12/Vulkan. macOS: Monterey 12+, GPU Metal (Apple silicon e Intel). Linux: Ubuntu 22.04/24.04, OpenGL 3.2+/Vulkan, Gnome en X11/Wayland. Editor en Apple silicon: Ventura 13+, sin CPU lightmapping / Inicial / Alta / Tabla en diapositiva / OBLIGATORIO / OK.

**B8** OpenGL Programming Guide for Mac – About OpenGL for OS X (Retired Document) / Apple / doc oficial archivada / https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_intro/opengl_intro.html / OpenGL deprecado / [HECHO] "OpenGL was deprecated in macOS 10.14. To create high-performance code on GPUs, use the Metal framework instead." / Inicial / Alta / Cita textual / OBLIGATORIO / OK.

**B9** Input Bindings (Input System 1.14) / Unity / doc del paquete / https://docs.unity3d.com/Packages/com.unity.inputsystem@1.14/manual/ActionBindings.html / remapeo / §Periféricos / [HECHO] `PerformInteractiveRebinding()`, hay que hacer Dispose de `RebindingOperation`, `SaveBindingOverridesAsJson`/`LoadBindingOverridesFromJson`, sample "Rebinding UI" en el Package Manager. ⚠ La versión del paquete para Unity 6.3 es **1.20.0** (ver B10). La URL equivalente @1.20 dio 404 y la @1.15 aparece en el buscador / Intermedio / Alta / Base del TP de remapeo / OBLIGATORIO / OK (1.14).

**B10** Input System package page (Unity 6.3) + CHANGELOG 1.20 / Unity / doc / https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.inputsystem.html y https://docs.unity3d.com/Packages/com.unity.inputsystem@1.20/changelog/CHANGELOG.html / versión / [HECHO] "Package version 1.20.0 is released for Unity Editor version 6000.3". 1.20.0 tiene fecha 2026-07-21. Rebinding UI sample: en 1.16.0 se reemplazó el rebind de "Look" por un slider de sensibilidad del mouse y se agregó `SwapBinding()`. En 1.20.0 los samples migraron a URP (URP pasa a ser requerido) / Intermedio / Alta / Fijar la versión en clase / OBLIGATORIO / OK.

**B11** PlayerInput API (1.15) / Unity / API / https://docs.unity3d.com/Packages/com.unity.inputsystem@1.15/api/UnityEngine.InputSystem.PlayerInput.html / dispositivo activo / [HECHO] `onControlsChanged` ("triggered when the controls used by the player change"), `currentControlScheme`, `neverAutoSwitchControlSchemes` / Intermedio / Alta / Prompts/glyphs dinámicos / OBLIGATORIO / OK.

**B12** Xbox Accessibility Guideline 107 / Microsoft / guía oficial / ms.date 2022-05-09, actualizada 2026-06-17 / https://learn.microsoft.com/en-us/gaming/accessibility/xbox-accessibility-guidelines/107 / accesibilidad de input / [HECHO] Objetivo: operar el juego "through input mechanisms of their choice". Remapear **todos** los controles, incluido "the Esc key on PC games". Que los prompts reflejen el remapeo. Toggles/auto-hold. Sensibilidad ajustable "by at least 50%" / Intermedio / Alta / **El número correcto es XAG 107 (Input)** / OBLIGATORIO / OK.

**B13** Allow controls to be remapped / reconfigured / Game Accessibility Guidelines / guía / https://gameaccessibilityguidelines.com/allow-controls-to-be-remapped-reconfigured/ / remapeo / [HECHO] Nivel *Basic* (Motor). El remapeo in-game complementa al del sistema, no lo reemplaza / Inicial / Alta (consorcio de profesionales y académicos) / Argumento de diseño / OBLIGATORIO / OK.

**B14** Steam Input (Steam Controller / Steam Input handbook) / Valve / Steamworks / https://partner.steamgames.com/doc/features/steam_controller / Steam Input / [HECHO] Sistema de configuración de dispositivos: action sets, action manifest, input sources/modes, modo legacy y API nativa `ISteamInput`. Configuraciones compartibles por la comunidad / Intermedio / Alta / Explicar que Steam puede remapear "por encima" del juego [INFERENCIA: hay que testear el juego con Steam Input activo y desactivado] / COMPLEMENTARIO / OK.

**B15** HID support (Input System 1.15) / Unity / doc / https://docs.unity3d.com/Packages/com.unity.inputsystem@1.15/manual/HID.html / HOTAS/joysticks / [HECHO] HID por USB y Bluetooth en Windows, macOS y UWP. Layouts autogenerados para Joystick/Gamepad/MultiAxisController, pero "too ambiguous in practice", así que se recomiendan layouts custom (JSON o C#) / Avanzado / Alta / HOTAS/volantes / COMPLEMENTARIO / OK.

**B16** Steam Deck Compatibility Review / Valve / Steamworks / https://partner.steamgames.com/doc/steamdeck/compat / Deck Verified / [HECHO] Categorías: Verified, Playable, Unsupported, Unknown. Criterios: control por defecto que permita acceder a todo, glyphs que coincidan con el input, texto ingresable solo con mando, 1280×800 preferido, fuente ≥ 9 px a 1280×800, sin launchers incompatibles, Proton. La página actual menciona también "Steam Machine" (30 fps a 1080p) / Inicial / Alta / **Checklist de QA para el TP** / OBLIGATORIO / OK.

**B17** Quality settings / Unity / doc 6.3 / https://docs.unity3d.com/6000.3/Documentation/Manual/class-QualitySettings.html / escalabilidad / [HECHO] Matriz de niveles × plataformas; Render Pipeline Asset por nivel; VSync Count; Global Mipmap Limit (0 a 3); MSAA; sombras (distancia, cascadas) / Inicial / Alta / Demo / OBLIGATORIO / OK.

**B18** QualitySettings.SetQualityLevel / Unity / API 6.3 / https://docs.unity3d.com/6000.3/Documentation/ScriptReference/QualitySettings.SetQualityLevel.html / runtime / [HECHO] `applyExpensiveChanges` (default true). Cambiar el AA es costoso / Intermedio / Alta / Menú de opciones / OBLIGATORIO / OK.

**B19** URP Asset reference / Unity / doc 6.3 / https://docs.unity3d.com/6000.3/Documentation/Manual/urp/universalrp-asset.html / render scale y upscaling / [HECHO] Render Scale escala el render target. Upscaling Filter: Automatic, Bilinear, Nearest-Neighbor, FSR 1.0, STP 1.0. HDR. MSAA 2x/4x/8x. Sombras: Max Distance, Cascade Count ("Increasing the number of cascades reduces the performance"), resolución / Intermedio / Alta / Demo / OBLIGATORIO / OK.

**B20** Spatial-Temporal Post-Processing (STP) in URP / Unity / doc 6.3 / https://docs.unity3d.com/6000.3/Documentation/Manual/urp/stp/stp-upscaler.html / upscaler / [HECHO] Requiere Shader Model 5.0 y compute shaders; no soporta OpenGL ES; fuerza TAA / Intermedio / Alta / Upscaler propio de Unity / OBLIGATORIO / OK.

**B21** Anti-aliasing in URP / Unity / doc 6.3 / https://docs.unity3d.com/6000.3/Documentation/Manual/urp/anti-aliasing.html / AA / [HECHO] FXAA (el más barato), SMAA, TAA (ghosting; incompatible con MSAA, camera stacking y dynamic resolution), MSAA (bordes de geometría, no aliasing de shader) / Intermedio / Alta / Tabla comparativa / OBLIGATORIO / OK.

**B22** Application.targetFrameRate / Unity / API 6.3 / https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Application-targetFrameRate.html / framerate / [HECHO] En desktop, "If vSyncCount != 0, then targetFrameRate is ignored". Default −1 con vSync 0 = renderiza sin límite. Se recomienda vSyncCount porque targetFrameRate "is subject to microstuttering" / Intermedio / Alta / Error típico del alumno / OBLIGATORIO / OK.

**B23** FullScreenMode / Unity / API 6.3 / https://docs.unity3d.com/6000.3/Documentation/ScriptReference/FullScreenMode.html / modos de pantalla / [HECHO] ExclusiveFullScreen (solo Windows), FullScreenWindow (todas), MaximizedWindow (Windows/macOS), Windowed (desktop) / Inicial / Alta / Menú de video / OBLIGATORIO / OK.

**B24** Screen.SetResolution / Unity / API 6.3 / https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Screen.SetResolution.html / resoluciones / [HECHO] Se aplica al final del frame; si no hay coincidencia, usa la más cercana; el refresh rate solo cambia en exclusive fullscreen; con varios monitores, solo la pantalla primaria / Intermedio / Alta / Menú de video / OBLIGATORIO / OK.

**B25** HDR Output in URP / Unity / doc 6.3 / https://docs.unity3d.com/6000.3/Documentation/Manual/urp/post-processing/hdr-output.html / HDR / [HECHO] Windows con DX11, DX12 o Vulkan; macOS con Metal. DX11: no en el Editor y "doesn't support HDR Output in exclusive full-screen mode" / Avanzado / Alta / Ejemplo de por qué hace falta un monitor HDR real / COMPLEMENTARIO / OK.

**B26** Introduction to Dynamic Resolution / Unity / doc 6.3 / https://docs.unity3d.com/6000.3/Documentation/Manual/DynamicResolution-introduction.html / dynamic resolution / [HECHO] "iOS, macOS and tvOS (Metal only), Android (Vulkan only), Windows Standalone (DirectX 12 only), and UWP (DirectX 12 only)". **Linux no figura** / Intermedio / Alta / Dato citable / OBLIGATORIO / OK.

**B27** Deep learning super sampling (DLSS) in HDRP 17.3 / Unity / doc del paquete / https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.3/manual/deep-learning-super-sampling-in-hdrp.html / DLSS / [HECHO] Solo DX11, DX12 y Vulkan en Windows 64 bits; requiere el paquete NVIDIA. La página no menciona URP / Avanzado / Alta / Aclarar que DLSS es de HDRP / COMPLEMENTARIO / OK. (Que HDRP 17.3 corresponda a Unity 6.3 es INFERENCIA por numeración; la página no lo dice.)

**B28** What is Direct3D 12 / Microsoft / doc oficial / ms.date 2018-11-19 / https://learn.microsoft.com/en-us/windows/win32/direct3d12/what-is-directx-12- / DX12 vs DX11 / [HECHO] "lower level of hardware abstraction". La app es responsable de su gestión de memoria. "Direct3D 11 continues to be a viable option" / Intermedio / Alta / Por qué DX12 traslada responsabilidad (y bugs) al motor / COMPLEMENTARIO / OK.

**B29** Vulkan (sitio oficial) / Khronos Group / oficial / https://www.vulkan.org/ / Vulkan / [HECHO] "cross-platform industry standard". En macOS vía MoltenVK / Inicial / Alta / Mapa de APIs / COMPLEMENTARIO / OK.

**B30** Automated Combinatorial Testing for Software / NIST / oficial-académico / https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software / matrices / §Testing / [HECHO] "most software bugs and failures are caused by one or two parameters, with progressively fewer by three or more". Herramienta ACTS gratuita / Intermedio / Alta / **Fundamento del pairwise testing en la matriz SO×GPU×resolución×input** / OBLIGATORIO / OK.

**B31** Counter-Strike 2 – página de Steam / Valve / página de producto / https://store.steampowered.com/app/730/ / requisitos mín./rec. / [HECHO] Windows 10, 4 hilos de CPU, 8 GB de RAM, GPU DX11 con 1 GB. Linux: Ubuntu 20.04, "AMD GCN+ or NVIDIA Kepler+ with up-to-date Vulkan drivers". Sin macOS / Inicial / Alta / Leer una ficha de requisitos real / OBLIGATORIO / OK.

**B32** Apple Developer News: Upcoming changes to Rosetta support / Apple / oficial / fecha mostrada en la página: 2026-09-01 / https://developer.apple.com/news/?id=w5ngl9k2 / Apple silicon / [HECHO] macOS 27: "Final release to support Rosetta — Intel-only apps will no longer run…". Excepción: "Rosetta functionality for older, unmaintained gaming titles… will continue to be supported" / Inicial / Alta / Argumento para builds Apple silicon/Universal / OBLIGATORIO / OK.

**B33** ISO/IEC 25010 – Flexibility (portal iso25000.com) / iso25000.com (portal divulgativo, **no** es ISO) / web / https://iso25000.com/index.php/en/iso-25000-standards/iso-25010/64-flexibility y https://iso25000.com/en/iso-25000-standards/iso-25010 / definiciones / [HECHO] Flexibilidad, Adaptabilidad, Escalabilidad ("handle growing or shrinking workloads"), Instalabilidad; Compatibilidad; Eficiencia de desempeño. La página no indica la edición de la norma / Intermedio / Media-Alta (fuente secundaria de la norma) / Sustentar la diferencia entre compatibilidad, escalabilidad y rendimiento / OBLIGATORIO / OK. [INFERENCIA docente] La acepción de "escalabilidad gráfica" en videojuegos (adaptarse a hardware de distinta capacidad) es una extensión de "Adaptabilidad" más que de la "Escalabilidad" ISO, que habla de carga de trabajo. Conviene declararlo en clase.

**B34** Postigo, H. (2007). Of Mods and Modders: Chasing Down the Value of Fan-Based Digital Game Modifications. *Games and Culture* 2(4), 300–313. DOI 10.1177/1555412007307955 / paper revisado por pares / https://api.crossref.org/works/10.1177/1555412007307955 (metadatos verificados) / modding / [HECHO] Existe y los metadatos coinciden. Pago (SAGE) / Intermedio / Alta / Lectura de referencia / COMPLEMENTARIO / Crossref OK.

**B35** Sotamaa, O. (2010). When the Game Is Not Enough: Motivations and Practices Among Computer Game Modding Culture. *Games and Culture* 5(3), 239–255. DOI 10.1177/1555412009359765 / paper / https://api.crossref.org/works/10.1177/1555412009359765 / motivaciones / [HECHO] Existe; online el 7/5/2010. Pago / Intermedio / Alta / Motivaciones de los modders / COMPLEMENTARIO / Crossref OK.

**B36** Kücklich, J. (2005). Precarious Playbour: Modders and the Digital Games Industry. *Fibreculture Journal*, Issue 5 / paper, **acceso abierto** / https://five.fibreculturejournal.org/fcj-025-precarious-playbour-modders-and-the-digital-games-industry/ / economía del modding / [HECHO] Los mods extienden el ciclo de vida de los productos y los modders no suelen cobrar ("playbour") / Intermedio / Alta / **Lectura obligatoria (gratuita)** / OBLIGATORIO / OK.

**B37** Poretski, L. & Arazy, O. (2017). Placing Value on Community Co-creations: A Study of a Video Game "Modding" Community. CSCW '17, pp. 480–491. DOI 10.1145/2998181.2998301 / paper / https://api.crossref.org/works/10.1145/2998181.2998301 / longevidad y ventas / [HECHO] Existe (Crossref; publicado el 25/2/2017). No es open access (Semantic Scholar). La afirmación de que el modding aumenta las ventas del juego base viene **solo del resumen del buscador**; el abstract no pudo leerse (ver H) / Avanzado / Alta / Citar con cautela / COMPLEMENTARIO / Crossref OK.

**B38** Schreiner, L. & von Mammen, S. (2021). Modding Support of Game Engines. FDG '21. DOI 10.1145/3472538.3472574 / paper / https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3472538.3472574?fields=title,abstract,year,venue,isOpenAccess / soporte de mods por motor / [HECHO] Compara id Tech, Unreal, Source y **Unity**. Efectos: "enhanced lifespan for games and the requirement for more development effort". No open access / Intermedio / Alta / **Paper más directamente aplicable a Unity** / OBLIGATORIO (el abstract) / OK.

**B39** DOOM source code (id-Software/DOOM) / id Software / repositorio oficial / 23/12/1997 / https://github.com/id-Software/DOOM / historia / [HECHO] Código liberado el 23/12/1997 bajo GPL-2.0. ⚠ Los WAD de 1994 no se verificaron con fuente primaria (ver H) / Inicial / Alta / Hito histórico / COMPLEMENTARIO / OK.

**B40** Removing Payment Feature From Skyrim Workshop — cobertura de Engadget / Engadget (prensa) / 27/04/2015 / https://www.engadget.com/2015-04-27-valve-reverses-skyrim-mod-payments.html / paid mods / [HECHO] Valve revirtió y reembolsó: "didn't understand exactly what we were doing", con el apoyo de Bethesda. El anuncio primario (steamcommunity) se abrió pero su cuerpo no se renderizó (ver H) / Inicial / Media-Alta / Caso de ética y economía / OBLIGATORIO / OK.

**B41** AssetBundles (introduction) / Unity / doc 6.3 / https://docs.unity3d.com/6000.3/Documentation/Manual/AssetBundlesIntro.html / mods en Unity / [HECHO] "AssetBundles can't contain assemblies, so you can't use them to distribute new C# classes…". Sí pueden contener ScriptableObjects / Intermedio / Alta / **Límite técnico central del modding en Unity** / OBLIGATORIO / OK.

**B42** Addressables (versión para 6.3) / Unity / doc / https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.addressables.html y https://docs.unity3d.com/Packages/com.unity.addressables@2.7/manual/index.html / contenido / [HECHO] 2.10.3 es la versión publicada para 6000.3. Carga por dirección y contenido remoto. **No menciona mods** / Intermedio / Alta / [INFERENCIA] útil para mods de contenido, no es una solución de modding / COMPLEMENTARIO / OK.

**B43** Steam Workshop / Valve / Steamworks / https://partner.steamgames.com/doc/features/workshop / UGC / [HECHO] Modelos "Ready-to-Use" (sin curación) y "Curated" / Inicial / Alta / Distribución de mods / OBLIGATORIO / OK.

**B44** ISteamUGC Interface / Valve / API / https://partner.steamgames.com/doc/api/ISteamUGC / API de Workshop / [HECHO] "Functions to create, consume, and interact with the Steam Workshop". `CreateItem`, `SubmitItemUpdate`, `GetItemInstallInfo` / Avanzado / Alta / Referencia técnica / COMPLEMENTARIO / OK.

**B45** mod.io Docs / mod.io (empresa) / doc comercial / https://docs.mod.io/ / UGC multiplataforma / [HECHO] Middleware de UGC con integración Unity. **No se encontró la política de precios en la doc** / Intermedio / Media (proveedor comercial) / Alternativa a Workshop fuera de Steam / COMPLEMENTARIO / OK.

**B46** Dangerous mods in Cities: Skylines / Kaspersky (blog de una empresa de seguridad) / feb. 2022 / https://www.kaspersky.com/blog/cities-skylines-malicious-mods/44004/ / seguridad / [HECHO] Mods de un autor ("Chaos/Holy Water") con un updater desde GitHub que funcionaba como backdoor y con sabotaje dirigido a usuarios. ~50 usuarios afectados por el backdoor; los developers no hallaron keyloggers ni miners / Inicial / Media-Alta (profesional de seguridad) / **Caso de riesgo documentado** / OBLIGATORIO / OK.

**B47** Proton (README) / Valve / repositorio oficial / https://github.com/ValveSoftware/Proton / Linux / [HECHO] "allows games which are exclusive to Windows to run on the Linux operating system". Usa Wine; submódulos DXVK y vkd3d-proton; BSD-3-Clause / Intermedio / Alta / Explicar la traducción D3D→Vulkan / OBLIGATORIO / OK.

**B48** Proton guidance for Steam Deck / Valve / Steamworks / https://partner.steamgames.com/doc/steamdeck/proton / Proton / [HECHO] "most games work out of the box". Hay que habilitar EAC/BattlEye para Proton; problemas con .NET/WPF en launchers, codecs de Media Foundation y anti-cheat de kernel / Intermedio / Alta / Checklist de riesgos / OBLIGATORIO / OK.

**B49** Notarization Requirement for Mac Software / Apple / noticia oficial / 03/06/2019 / https://developer.apple.com/news/?id=06032019i / notarización / [HECHO] Las apps firmadas con Developer ID "must also be notarized by Apple in order to run on macOS Catalina" / Inicial / Alta / Requisito de distribución / OBLIGATORIO / OK.

**B50** Distributing software on macOS / Apple / oficial / https://developer.apple.com/macos/distribution/ / Gatekeeper / [HECHO] Gatekeeper existe desde macOS 10.7.5; Developer ID requiere el Apple Developer Program (pago) / Inicial / Alta / Costo de publicar en Mac / OBLIGATORIO / OK.

**B51** Build a macOS application / Unity / doc 6.3 / https://docs.unity3d.com/6000.3/Documentation/Manual/macos-building.html / Apple silicon / [HECHO] Arquitecturas: Intel 64-bit, Apple silicon, Universal. Advertencia sobre la deprecación de Rosetta / Inicial / Alta / Demo de Build Profile / OBLIGATORIO / OK.

**B52** macOS Sequoia Software License Agreement / Apple / licencia oficial (PDF) / https://www.apple.com/legal/sla/docs/macOSSequoia.pdf / virtualización de macOS / [HECHO] §2B(iii): hasta "two (2) additional copies or instances… within virtual operating system environments on each Apple-branded computer you own or control that is already running the Apple Software", para desarrollo, testing, macOS Server o uso personal no comercial / Inicial / Alta / **Dato legal: no se puede usar macOS en VM sobre PC no-Apple** / OBLIGATORIO / OK (texto extraído del PDF).

**B53** Cloud Diagnostics (deprecation notice) / Unity / doc / https://docs.unity.com/en-us/cloud-diagnostics / telemetría / [HECHO] "Cloud Diagnostics is deprecated"; reemplazo: Diagnostics en Unity 6.2+ / Intermedio / Alta / Evitar enseñar una herramienta deprecada / OBLIGATORIO / OK.

**B54** Run Play mode tests in a Player / Unity / doc 6.3 / https://docs.unity3d.com/6000.3/Documentation/Manual/test-framework/workflow-run-playmode-test-standalone.html / UTF en standalone / [HECHO] Pestaña Player del Test Runner; el Editor y el Player deben estar en la misma red / Intermedio / Alta / Continuidad con la unidad de testing / OBLIGATORIO / OK.

**B55** Isolation modes (Windows containers) / Microsoft / doc / ms.date 2025-01-23 / https://learn.microsoft.com/en-us/virtualization/windowscontainers/manage-containers/hyperv-container / contenedores / [HECHO] Process isolation: "containers share the same kernel with the host". Hyper-V isolation: cada contenedor "effectively gets its own kernel" / Intermedio / Alta / F / OBLIGATORIO / OK.

**B56** What is Docker? (.NET Microservices e-book) / Microsoft / doc / https://learn.microsoft.com/en-us/dotnet/architecture/microservices/container-docker-introduction/docker-defined / contenedores vs VM / [HECHO] "they share the OS kernel with other containers"; "Windows images can run only on Windows hosts"; "less isolation than VMs" / Inicial / Alta / F / OBLIGATORIO / OK.

**B57** Docker security / Docker / doc oficial / https://docs.docker.com/engine/security/ / namespaces / [HECHO] Aislamiento por kernel namespaces y cgroups (como LXC) / Intermedio / Alta / F / COMPLEMENTARIO / OK.

**B58** Partition and share GPUs with VMs on Hyper-V / Microsoft / doc / actualizada 2026-05-05 / https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/gpu-partitioning / GPU en VM / [HECHO] GPU-P (SR-IOV) en Windows Server 2025, con GPUs de datacenter (NVIDIA A2/A10/A16/A40/L4/L40…, AMD Radeon PRO V710) / Avanzado / Alta / **Muestra que la GPU virtual de calidad no es para la PC de un estudiante** / OBLIGATORIO / OK.

**B59** Windows Sandbox / Microsoft / doc / 2026-03-29 / https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview / sandbox / [HECHO] VM descartable con hypervisor; "supports virtual GPU"; ediciones Pro/Enterprise/Education (no Home); una sola instancia a la vez / Inicial / Alta / Probar instalación limpia / OBLIGATORIO / OK.

**B60** WSLg (repositorio) / Microsoft / repositorio oficial / https://github.com/microsoft/wslg / WSLg / [HECHO] Apps GUI de Linux (X11/Wayland) en Windows; OpenGL acelerado vía el driver Mesa d3d12 (Mesa 21.0). Overhead por copia VRAM→RAM de "up to 50%" a frame rates muy altos en GPU discreta / Avanzado / Alta / Muestra por qué WSLg no sirve para medir rendimiento de un juego Linux / OBLIGATORIO / OK.

**B61** Run Linux GUI apps with WSL / Microsoft / doc / https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps / WSLg / [HECHO] Requiere Windows 10 build 19044+ o Windows 11 y driver vGPU. "does not provide a full desktop experience" / Inicial / Alta / F / COMPLEMENTARIO / OK.

**B62** VirtualBox 7 – Known Limitations / Oracle / manual oficial / https://www.virtualbox.org/manual/ch14.html / VM / [HECHO] La aceleración 3D por hardware es "experimental". Rendimiento pobre si convive con Hyper-V / Intermedio / Alta / F / COMPLEMENTARIO / OK.

**B63** GameCI – Getting started (GitHub) / GameCI (open source) / doc / https://game.ci/docs/github/getting-started / CI / [HECHO] Test runner, builder y activación. Requiere licencia Unity (Personal/Plus/Pro). Usa imágenes game-ci/docker / Intermedio / Media-Alta (open source y profesional, no oficial de Unity) / CI headless / OBLIGATORIO / OK.

**B64** GameCI – Builder / GameCI / doc / https://game.ci/docs/github/builder / runners / [HECHO] "StandaloneOSX builds require a macOS runner". Los targets Mono pueden compilarse en forma cruzada; IL2CPP necesita un host compatible / Intermedio / Media-Alta / F / OBLIGATORIO / OK.

**B65** unityci/editor (Docker Hub) / unityci / imagen / https://hub.docker.com/r/unityci/editor / contenedor del Editor / [HECHO] "Dockerised Unity Editor made for continuous integration". Variantes ubuntu y windows; licencia MIT / Intermedio / Media-Alta / F / COMPLEMENTARIO / OK.

**B66** Unity Build Automation / Unity / doc oficial / https://docs.unity.com/en-us/build-automation y https://docs.unity.com/ugs/en-us/manual/devops/manual/build-automation/reference/supported-platforms-on-each-builder-os / CI cloud / [HECHO] "continuous integration service that automatically creates multiplatform builds in the Cloud". La tabla de plataformas por SO del builder indica Windows IL2CPP solo en builders Windows. La doc consultada no trae precios (ver H) / Intermedio / Alta / Alternativa oficial / COMPLEMENTARIO / OK.

**B67** Warner Bros Suspends Arkham Knight PC Sales / Kotaku (prensa) / 24/06/2015 / https://kotaku.com/warner-bros-says-theyre-suspending-arkham-knight-pc-sal-1713780990 / caso de port / [HECHO] Cita de WB: "decided to suspend future game sales of the PC version while we work to address these issues…", con oferta de reembolso / Inicial / Media-Alta (reproduce el comunicado; el original del foro de WB no se verificó) / **Caso disparador de la unidad** / OBLIGATORIO / OK.

**B68** Skyrim Special Edition: Creation Kit (Steam) / Bethesda / página oficial / lanzamiento 25/04/2022 / https://store.steampowered.com/app/1946180/ / herramientas oficiales / [HECHO] "free downloadable editor that allows you to create mods for Skyrim" / Inicial / Alta / Ejemplo de soporte oficial / COMPLEMENTARIO / OK.

**B69** Minecraft: Bedrock Edition Creator Documentation / Microsoft / doc oficial / https://learn.microsoft.com/en-us/minecraft/creator/ / mods oficiales / [HECHO] "Learn how to mod Minecraft with Add-Ons" (resource/behavior packs, Script API) / Inicial / Alta / Modding oficial data-driven / COMPLEMENTARIO / OK.

---

## C) Videos (verificados con YouTube oEmbed o GDC Vault)

Duración: **no verificada** en todos los casos (oEmbed no la informa). Fragmento: a determinar salvo que se indique otra cosa.

| # | Título | Canal/autor | Fecha | URL | Concepto | Uso |
|---|---|---|---|---|---|---|
| V1 | The Last of Us Part 1 PC vs PS5 - A Disappointing Port With Big Problems To Address | Digital Foundry | 2023 (fecha exacta no verificada) | https://www.youtube.com/watch?v=xQ2emuUoxrI | VRAM y CPU como límites, port deficiente | Caso de estudio; mostrar el tramo de VRAM con 8 GB (a determinar) |
| V2 | The Last Of Us Part 1: Has Naughty Dog Fixed The PC Port? | Digital Foundry | 2023 (no verificada) | https://www.youtube.com/watch?v=L8bg9coF6AA | Parches post-lanzamiento | Contrastar con V1 |
| V3 | Batman Arkham Knight's Latest PC Patch Still Under-Delivers | Digital Foundry | nov. 2015 según la descripción del buscador (no verificada) | https://www.youtube.com/watch?v=PoEO_K_xY0A | Port fallido y retiro de venta | Complementa B67 |
| V4 | Doom Eternal's Ray Tracing Upgrade Analysed - Best PC Settings + PS5/Xbox Series X Comparisons | Digital Foundry | no verificada | https://www.youtube.com/watch?v=yZ5ZyVYlq5A | Settings óptimos y escalabilidad (caso positivo) | Analizar settings |
| V5 | Level Design in a Day: How Modding Made Bethesda Better — Joel Burgess (Bethesda) | GDC Vault (contenido gratuito) | GDC 2015 | https://gdcvault.com/play/1022107/Level-Design-in-a-Day | Modding → comunidad, herramientas, DLC | Cultura del modding |
| V6 | PLAYERUNKNOWN: From Mod Creator to Creative Director of PUBG | GDC Festival of Gaming (YouTube) | 2018 según el buscador (no verificada) | https://www.youtube.com/watch?v=TJQR1Sfinjk | De modder a profesional | Motivación y trayectoria |
| V7 | Listen to a Demanding Audience: Developing the PC version of 'For Honor' — Philipp Sonnefeld (Blue Byte) | GDC Vault (gratuito) | GDC Europe 2016 | https://www.gdcvault.com/play/1023874/Listen-to-a-Demanding-Audience | Expectativas del jugador de PC: controles, settings | **Ideal para la clase 1** |
| V8 | Warface: Creating AAA Graphics for Low-End PCs — Konstantin Molchanov (Crytek) | GDC Vault (gratuito) | GDC Europe 2013 | https://www.gdcvault.com/play/1019335/Warface-Creating-AAA-Graphics-for | Escalar hacia abajo | Escalabilidad |
| V9 | Scaling from Mobile to High-End PCs: The Tech of Broken Age — Oliver Franzke (Double Fine) | GDC Vault (gratuito) | 2014 | https://www.gdcvault.com/play/1020747/Scaling-from-Mobile-to-High | Escalabilidad multiplataforma | Complementario |
| V10 | Unity Input System in Unity 6 (5/7): Rebinding Input System controls | Unity (oficial) | ~2025 según el buscador (no verificada) | https://www.youtube.com/watch?v=JfuqMaOiNPs | Remapeo interactivo | **Práctica guiada** |
| V11 | Understanding URP settings and essentials | Unity (oficial) | no verificada | https://www.youtube.com/watch?v=HCXCmHgV7Sk | URP Asset y quality | Práctica |
| V12 | Steamworks Quick Tips - Introducing Steam Deck Verified | Steamworks Development (Valve) | no verificada | https://www.youtube.com/watch?v=a8tNvhwkth8 | Criterios de Deck Verified | Testing |
| V13 | Steamworks Quick Tips - Steam Deck | Steamworks Development | no verificada | https://www.youtube.com/watch?v=5Q_C5KVJbUw | Deck para devs | Complementario |
| V14 | Development Without a Dev-Kit | Steamworks Development | no verificada | https://www.youtube.com/watch?v=Nn2Sjmkv6u0 | Testear para Deck sin hardware | Contraste con "hardware real" (F) |

---

## D) PDFs / e-books

| # | Título | Autor | Fecha | URL | Gratis/Pago | Uso |
|---|---|---|---|---|---|---|
| D1 | Optimize your game performance for consoles and PCs in Unity (Unity 6 edition) | Unity | 17/10/2024 | https://unity.com/resources/console-pc-game-performance-optimization-unity-6 | Gratis (descarga desde la página) | Profiling y optimización PC; separar optimización de compatibilidad |
| D2 | Introduction to URP for advanced creators (Unity 6 edition) | Unity (autor principal Nik Lever) | página: 17/10/2024; blog: 04/11/2024 | https://unity.com/resources/introduction-to-urp-advanced-creators-unity-6 (blog: https://unity.com/blog/biggest-edition-urp-ebook-unity-6) | Gratis | Quality settings en URP |
| D3 | Kücklich (2005) Precarious Playbour | Fibreculture Journal | 2005 | https://five.fibreculturejournal.org/fcj-025-precarious-playbour-modders-and-the-digital-games-industry/ | Acceso abierto (HTML) | Lectura sobre modding |
| D4 | macOS Sequoia SLA (PDF) | Apple | vigente | https://www.apple.com/legal/sla/docs/macOSSequoia.pdf | Gratis | Cláusula 2B(iii) de virtualización |

Nota: Postigo 2007, Sotamaa 2010, Poretski & Arazy 2017 y Schreiner & von Mammen 2021 son **pagos / no open access** (SAGE y ACM). No se encontró un PDF abierto verificado de esos papers.

---

## E) Datos técnicos verificados citables (todos consultados el 2026-10-04)

1. Steam Survey, sept. 2026: Windows 95,03% / Linux 3,05% / macOS 1,92%. 1920×1080 = 47,91%. RAM 32 GB = 42,22%. VRAM 16 GB = 27,21%. (B1)
2. GTX 1650 sigue en el top 10 de GPUs (2,19%) en sept. 2026. (B2)
3. DX12 es la API por defecto en proyectos Windows nuevos desde Unity 6.1. (B5)
4. Unity 6.3 Player: Windows 10 21H1+; macOS 12+ con Metal; Ubuntu 22.04/24.04 con OpenGL 3.2+/Vulkan. (B7)
5. OpenGL deprecado en macOS 10.14. (B8)
6. Dynamic Resolution: Windows solo con DX12; macOS solo con Metal; Linux no figura. (B26)
7. Upscalers en URP (6.3): FSR 1.0 y STP 1.0. DLSS solo en HDRP y en Windows 64 bits. STP requiere SM 5.0 + compute shaders. (B19, B20, B27)
8. TAA es incompatible con MSAA, camera stacking y dynamic resolution en URP. (B21)
9. Si `vSyncCount != 0`, se ignora `targetFrameRate`. (B22)
10. ExclusiveFullScreen solo existe en Windows. (B23)
11. HDR en DX11: no en exclusive fullscreen. (B25)
12. Input System para Unity 6.3: 1.20.0 (fecha en el changelog: 21/07/2026). (B10)
13. XAG 107: remapear todos los controles (incluido Esc en PC) y sensibilidad ±50%. (B12)
14. Steam Deck: 1280×800 y fuente ≥ 9 px; glyphs acordes al input. (B16)
15. AssetBundles no pueden contener assemblies (no hay código de mods vía AB). (B41)
16. Notarización obligatoria para Developer ID desde macOS Catalina (anuncio del 03/06/2019). (B49)
17. macOS 27 es la última versión con Rosetta general; hay excepción para juegos antiguos sin mantenimiento. (B32)
18. SLA de macOS: hasta 2 VMs adicionales y solo en hardware Apple. (B52)
19. Cloud Diagnostics deprecado; usar Diagnostics (Unity 6.2+). (B53)
20. NIST: la mayoría de las fallas se disparan por la interacción de 1 o 2 parámetros. (B30)
21. Arkham Knight: venta de PC suspendida (nota del 24/06/2015). (B67)
22. Paid mods de Skyrim revertidos el 27/04/2015. (B40)
23. Cities: Skylines, feb. 2022: mod con backdoor de auto-update. (B46)

---

## F) Análisis crítico: virtualización y contenedores para testing de PC

**Tesis [INFERENCIA fundada]:** VMs y contenedores son herramientas de **aislamiento y reproducibilidad**, no de **fidelidad de hardware**. Sirven para "¿se instala, arranca y pasa los tests lógicos en un entorno limpio?". No sirven para "¿rinde y se ve bien en la GPU, driver, monitor y mando del jugador?".

| Herramienta | Qué SÍ sirve | Qué NO sirve | Limitaciones documentadas | Fuente |
|---|---|---|---|---|
| **Contenedor Docker (Linux)** | CI headless: builds de Unity (`unityci/editor`), tests EditMode/PlayMode en batch, servidores dedicados Linux, entorno reproducible | Probar otro SO de escritorio, GPU real, input, audio, rendimiento | Comparte el kernel del host ("share the OS kernel"); imágenes Windows solo en hosts Windows | B55, B56, B57, B65 |
| **GameCI (GitHub Actions)** | Builds y tests automáticos por commit | Builds de macOS desde Linux; IL2CPP sin el toolchain del SO | "StandaloneOSX builds require a macOS runner" | B63, B64 |
| **Contenedor Windows (Hyper-V isolation)** | Aislamiento más fuerte (kernel propio) | Igual que arriba: no es un escritorio con GPU real para jugar | Process isolation comparte kernel; Hyper-V isolation = VM liviana | B55 |
| **VM de escritorio (Hyper-V / VirtualBox / VMware)** | Instalador, permisos, rutas, primera ejecución, versiones de SO (Win10 vs Win11, distintas distros), ausencia de dependencias (VC++ runtime) | Rendimiento, bugs de driver de GPU, shaders específicos de un vendor, HDR, multi-monitor, latencia de input | VirtualBox: 3D por hardware "experimental"; mal rendimiento si convive con Hyper-V. La GPU en VM queda en un driver virtual, no el de NVIDIA/AMD/Intel del jugador [INFERENCIA] | B62 |
| **Hyper-V GPU partitioning (GPU-P)** | GPU real fraccionada para VDI/IA en servidores | Testing en la PC de un estudiante | Windows Server 2025 y GPUs de datacenter específicas (A2/A10/L4/L40…). Hardware homogéneo | B58 |
| **Windows Sandbox** | Instalación limpia y descartable de un build de Windows; "supports virtual GPU" | Persistencia, rendimiento, varias instancias | No disponible en Home; una instancia a la vez | B59 |
| **WSL2 + WSLg** | Correr el build Linux de Unity para un smoke test rápido | Medir rendimiento o certificar Linux/Steam Deck | Overhead de copia VRAM→RAM de hasta ~50% a fps muy altos en GPU discreta; "does not provide a full desktop experience" | B60, B61 |
| **macOS en VM** | Testing legal en hardware Apple (hasta 2 instancias) | macOS en VM sobre PC no-Apple (**viola el SLA**) | SLA §2B(iii): "on each Apple-branded computer you own or control" | B52 |
| **Proton en Linux de escritorio** | Aproximación a Steam Deck sin el Deck | Certificar Deck Verified (pantalla 1280×800, controles, rendimiento) | Valve ofrece guías "sin dev-kit", pero los criterios son de hardware [INFERENCIA] | B48, B16, V14 |

**Cuándo es imprescindible el hardware real** [INFERENCIA respaldada por las fuentes citadas]:
- **Rendimiento y frame pacing**: la GPU virtual no representa la del jugador (B58, B60, B62).
- **Drivers de GPU**: Unity documenta crashes del UMD/KMD del vendor (B6); hay que probar al menos NVIDIA, AMD e Intel.
- **HDR y modos de pantalla**: HDR depende de API y modo (B25); exclusive fullscreen solo existe en Windows (B23); monitor real.
- **Multi-monitor y refresh rate**: `SetResolution` solo afecta a la pantalla primaria, y el refresh solo en exclusive (B24).
- **Dispositivos de input** (gamepads, HOTAS, volantes, HID): layouts y passthrough USB (B15).
- **Steam Deck / Apple silicon**: arquitectura y pantalla propias (B16, B51).
- **Audio** (latencia, dispositivos): [INFERENCIA, sin fuente específica verificada].

**Estrategia recomendada para el curso** [INFERENCIA docente]: (1) CI en contenedor para compilar y correr tests; (2) VM/Sandbox para instalación limpia; (3) matriz pairwise (NIST/ACTS) sobre hardware real disponible en el aula (PCs con distintas GPUs, notebooks con iGPU, un Mac si lo hay, un Steam Deck si lo hay); (4) telemetría (Diagnostics) en las builds que se distribuyan.

---

## G) Fuera de alcance (sugerido)

- Programación directa en DX12/Vulkan (API de bajo nivel): basta con el concepto (B28).
- Anti-cheat de kernel y DRM: solo mencionarlos como riesgo de Proton (B48).
- Monetización de UGC (revenue share de Workshop/mod.io): solo el caso Skyrim.
- HDRP en profundidad, ray tracing y DLSS: mencionar; el curso trabaja en URP.
- Certificación de consolas (corresponde a otra unidad).
- Configuración de VDI/GPU-P en servidores.

---

## H) NO VERIFICADO (no usar como dato sin revisión)

1. **Documentación de Input System 1.20**: la página `@1.20/manual/ActionBindings.html` dio 404. Se usaron 1.14/1.15 (rebinding) y el changelog 1.20. Revisar en el Editor cuál es la ruta actual de la doc.
2. **Abstract de Poretski & Arazy (2017)**: ACM y Semantic Scholar no lo devolvieron. La afirmación "el modding aumenta las ventas del producto base" viene solo del resumen del buscador.
3. **Comunicado original de WB sobre Arkham Knight** (foro de WB / Steam): no abierto. Se cita vía Kotaku. Forbes devolvió 403. La fecha exacta (24 vs 25/06/2015) varía según el medio.
4. **Anuncio primario de Valve sobre paid mods** (https://steamcommunity.com/games/SteamWorkshop/announcements/detail/208632365253244218): se abrió, pero no se renderizó el cuerpo. Se cita vía Engadget.
5. **Página de notarización de Apple** (developer.apple.com/documentation/security/notarizing-macos-software-before-distribution): no se renderizó (JS). Se usaron la noticia del 03/06/2019 y la página de distribución.
6. **Artículos de Digital Foundry en Eurogamer/digitalfoundry.net**: bloqueados para el agente. GameSpot (TLOU) devolvió 403. Se usan solo los videos verificados por oEmbed.
7. **Duración y fecha exacta de los videos de YouTube**: no disponibles por oEmbed.
8. **Doom WADs 1994 / Half-Life→Counter-Strike / Warcraft III→DotA**: sin fuente primaria abierta. Solo verificado: el código fuente de DOOM liberado en 1997 (B39) y la mención de Valve a "Dota, Counter-strike, DayZ" en el contexto de paid mods (solo vía el buscador).
9. **Precios de Unity Build Automation y mod.io**: no presentes en la documentación consultada.
10. **Tabla de Build Automation** para los targets macOS y Linux: el resumen automático fue inconsistente. Verificar en la página antes de citar más allá de "Windows IL2CPP solo en builders Windows".
11. **Discrepancia de la RTX 5070** en el Steam Survey (5,86% en la página principal vs 6,15% en la de videocards): no se investigó el motivo.
12. **Counter-Strike 2 como caso positivo de escalabilidad**: solo se verificaron los requisitos (B31), no un análisis de settings.
13. **Cyberpunk 2077 (problemas de lanzamiento)**: no se buscó ni verificó ninguna fuente.
14. **Malware genérico en Steam Workshop** más allá de Cities: Skylines: no verificado.
15. **Equivalencia HDRP 17.3 = Unity 6.3**: es inferencia por numeración.
16. **Fecha de la noticia de Rosetta (01/09/2026)**: tomada tal cual de la página según el extractor; conviene revisarla a ojo.
