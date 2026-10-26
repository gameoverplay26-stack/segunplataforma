# Unidad 4 — Investigación de recursos (Fase 2 y Fase 9)

> **Cómo leer este archivo.** Es el resultado de la investigación web del 2026-10-04, con verificación real de URLs: WebFetch en páginas y PDFs, y oEmbed en YouTube. Se conserva casi literal para que las fuentes sigan siendo trazables.
> - **Sección A:** auditoría detallada con evidencia. La versión curada, con la decisión docente, está en [`01-analisis-programa-y-objetivos.md`](./01-analisis-programa-y-objetivos.md).
> - **Secciones B a E:** banco de recursos: fichas, videos, PDFs y datos citables.
> - **Sección F:** qué queda fuera de alcance.
> - **Sección G:** lo que **no** se pudo verificar. No usar en clase sin volver a verificarlo.
> - **Al final:** la tabla resumen de fuentes clasificadas.
>
> Convenciones: **[DOC]** = afirmación documentada en la fuente; **[INF]** = inferencia del investigador.


Convenciones:
- **[DOC]** = hecho documentado en la fuente citada (parafraseado o citado).
- **[INF]** = inferencia o propuesta del investigador. No es una afirmación de la fuente.
- "Fecha" = la que muestra la página ("Last updated", change log, fecha de publicación). Si la página no la muestra, se indica "sin fecha visible".

---

## A) Auditoría del programa oficial

### A.1 "Entorno de Dispositivos Móviles: Características de hardware y software"
- **Clasificación:** CORRECTO PERO INCOMPLETO.
- **Qué dice:** enuncia el tema sin decir qué características importan.
- **Problema:** así redactado, la clase puede terminar en una lista de especificaciones (GB de RAM, GHz). Para diseñar un juego lo que importa es otra cosa: el SoC (CPU, GPU y memoria en un solo chip), la GPU por tiles, el ancho de banda de memoria compartido, la ausencia de refrigeración activa y un sistema operativo que mata procesos.
- **Qué enseñar:**
  1. SoC con núcleos heterogéneos. [DOC] ADPF menciona "diverse core topology" y relojes de CPU dinámicos como complejidades que no existen en PC ni en consola.
  2. GPU tile-based (TBDR). [DOC] Apple: el render se divide en tiles, la memoria de tile es más rápida y gasta menos energía, y se descartan primitivas ocultas.
  3. Ancho de banda de memoria. [DOC] Arm: en móviles está más restringido que en escritorio, es un recurso compartido y su exceso gasta batería.
  4. El sistema operativo gestiona el ciclo de vida y la memoria (ver A.13).
- **Por qué importa:** explica por qué el overdraw, la transparencia y la resolución nativa cuestan más en un teléfono.
- **Fuentes:** https://developer.android.com/games/optimize/adpf · https://developer.apple.com/documentation/metal/tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering · Arm GPU Best Practices, sección 2.3 (PDF, ver D).

### A.2 "Diferencias con otras plataformas (PC, consolas)"
- **Clasificación:** CORRECTO PERO INCOMPLETO.
- **Problema:** se suele reducir a "el celular es menos potente". Faltan otras diferencias:
  - **Rendimiento sostenido vs. pico.** [DOC] El e-book de Unity 6 recomienda usar alrededor del 65 % del presupuesto de frame: ~22 ms a 30 fps y ~11 ms a 60 fps. Motivo: "Most mobile devices do not have active cooling".
  - **Fragmentación de dispositivos.** [DOC] El mismo e-book pide probar en dispositivos de gama mínima y máxima.
  - **Reglas de tienda obligatorias:** facturación, target API, tamaño de descarga.
  - **Input táctil sin feedback físico.**
  - **Interrupciones del sistema operativo.**
- **Qué enseñar:** una tabla comparativa PC / consola / móvil con estos ejes: refrigeración, potencia sostenida, memoria, input, interrupciones, distribución y certificación. [INF] Las consolas tienen hardware fijo y certificación del fabricante. Esa parte no se verificó en esta investigación.
- **Fuentes:** e-book Unity 6, págs. 19-20 (ver D) · https://developer.android.com/games/optimize/adpf

### A.3 "Limitaciones Técnicas: Restricciones de memoria"
- **Clasificación:** REQUIERE PRECISIÓN.
- **Problema:** "restricción de memoria" no es solo poca RAM. En móvil, el sistema **mata procesos**.
- **Android:**
  - [DOC] El daemon LMK mata los procesos menos esenciales cuando hay presión de memoria. Mata primero los de background.
  - [DOC] Para juegos, la doc recomienda `ApplicationExitInfo` (`REASON_LOW_MEMORY`) y leer `ActivityManager.MemoryInfo.totalMem` para ajustar el uso de memoria.
  - **Dato a corregir en la clase:** [DOC] los callbacks de trim están **deprecados** y "haven't been helpful at preventing low-memory kills". Solo siguen vigentes `TRIM_MEMORY_UI_HIDDEN` y `TRIM_MEMORY_BACKGROUND`. No hay que enseñar `onTrimMemory` con todos sus niveles como solución.
  - [DOC] Android vitals ahora mide memoria como core vital, con umbrales distintos para juegos (ej.: 4 GB de RAM → 2,25 GB en foreground). Desde febrero de 2027 puede afectar la visibilidad en la tienda.
- **iOS:** [DOC] `applicationDidReceiveMemoryWarning`: "If your app does not release enough memory during low-memory conditions, the system may terminate it outright."
- **Qué enseñar:** presupuesto de memoria, compresión de texturas (ASTC), carga y descarga de assets, y que el juego puede morir en background y tiene que guardar estado.
- **Fuentes:** https://developer.android.com/topic/performance/issues/lmk (actualizada 2026-09-21) · https://developer.android.com/topic/performance/vitals (2026-09-21) · https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationdidreceivememorywarning(_:)

### A.4 "Procesador y rendimiento gráfico"
- **Clasificación:** REQUIERE PRECISIÓN.
- **Problema:** falta el concepto central del móvil, que es **throttling térmico** y **rendimiento sostenido**. En el programa no figura "temperatura" ni "térmico".
- **Qué enseñar:**
  - **Android:**
    - [DOC] Thermal API: `getThermalHeadroom` predice cuánto tiempo puede sostenerse el rendimiento actual sin sobrecalentar (desde Android 11, API 30).
    - [DOC] Estados de `THERMAL_STATUS_NONE` a `SHUTDOWN`.
    - [DOC] Performance Hint API y Game Mode API.
  - **iOS:** [DOC] `ProcessInfo.thermalState`, con los valores nominal, fair, serious y critical.
  - **Unity 6.3:** [DOC] Adaptive Performance es un "built-in module" (`UnityEngine.AdaptivePerformanceModule`). El paquete `com.unity.adaptiveperformance@6.0` "now contains only samples and visual scripting nodes". Proveedores documentados: Basic provider (genérico, basado en `FrameTimingManager`) y el paquete Android provider.
  - **Precisión para el docente:** el video "Build stunning mobile games..." y el blog de Unity de 2021 describen la etapa **Samsung-only**. Están **desactualizados** para Unity 6.3.
  - **Overdraw y GPU:** [DOC] Unity e-book p. 63: "Mobile platforms are impacted by the resulting overdraw and alpha blending". [DOC] Arm: el overdraw provoca uso excesivo de ancho de banda.
- **Fuentes:** https://developer.android.com/games/optimize/adpf/thermal · https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum · https://docs.unity3d.com/6000.3/Documentation/ScriptReference/UnityEngine.AdaptivePerformanceModule.html · https://docs.unity3d.com/6000.3/Documentation/Manual/adaptive-performance/adaptive-performance.html

### A.5 "Consumo de batería"
- **Clasificación:** CORRECTO PERO INCOMPLETO.
- **Problema:** no relaciona la batería con las decisiones de diseño: fps objetivo, frecuencia de refresco, temperatura y modo de juego.
- **Qué enseñar:**
  - [DOC] En Unity, en Android e iOS con `vSyncCount = 0` y `targetFrameRate = -1` (valores por defecto), el contenido "is rendered at a fixed 30 fps to conserve battery power". El e-book dice "Unity defaults to 30 fps for mobile".
  - [DOC] Android para juegos recomienda:
    - igualar la frecuencia de refresco de la pantalla al fps objetivo (Swappy / frame pacing, integrado en Unity);
    - usar Vulkan ("more efficient than OpenGL ES");
    - responder a la Thermal API;
    - consultar el Game Mode API.
  - [DOC] Apple Energy Efficiency Guide for iOS Apps: está **archivada** (última revisión 2016-09-13). Vale como marco conceptual ("Strive to make your app absolutely idle when it is not responding to user input"), no como referencia técnica vigente.
- **Fuentes:** https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Application-targetFrameRate.html · https://developer.android.com/games/optimize/power (2026-02-26) · https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html

### A.6 FALTA UN TEMA IMPORTANTE: térmica y rendimiento sostenido
- **Clasificación:** FALTA UN TEMA IMPORTANTE. Puede integrarse en A.4 y A.5 sin agregar una unidad.
- **Qué enseñar:** el ciclo calor → throttling → caída de fps → peor experiencia, y que el diseño puede adaptar efectos y calidad. [DOC] La sesión WWDC19 422 muestra un ejemplo de respuesta por estado: en serious desactiva HDR y reduce sombras. [DOC] En Xcode, Device Conditions permite simular el estado térmico.
- **Fuentes:** https://developer.apple.com/videos/play/wwdc2019/422/ · https://developer.android.com/games/optimize/adpf/thermal

### A.7 "Diseño de Interfaz y Experiencia de Usuario: Optimización de interfaces táctiles"
- **Clasificación:** CORRECTO PERO INCOMPLETO.
- **Problema:** "optimización" es ambiguo, porque puede leerse como rendimiento de UI o como usabilidad. Faltan datos normativos.
- **Qué enseñar (normativo):**
  - [DOC] Apple HIG: hit region mínima de 44×44 pt (visionOS 60×60). En la página de Accessibility, iOS: 44×44 pt por defecto y 28×28 pt como mínimo. Separación sugerida: ~12 pt con bisel, ~24 pt sin bisel.
  - [DOC] Android: "at least 48dp×48dp. Larger is even better."
  - [DOC] Áreas seguras: HIG Layout; Android display cutout; Unity `Screen.safeArea` y `Screen.cutouts`.
  - [DOC] En Android 15+ con target SDK 35, edge-to-edge es obligatorio y los modos de cutout se interpretan como `ALWAYS`. En Unity: "Android 15+ ignores this setting entirely" (Render Outside Safe Area).
  - [DOC] Escalado de UI: Canvas Scaler (uGUI), con Constant Pixel Size, Scale With Screen Size y Constant Physical Size, más Match width/height. UI Toolkit Panel Settings tiene modos equivalentes.
  - **Profesional/académico:** Hoober 2013 (UXmatters): 49 % una mano, 36 % acunado, 15 % dos manos, sobre 1.333 observaciones. Son datos de 2013, con teléfonos más chicos: usar con esa advertencia. Parhi, Karlson & Bederson 2006 (MobileHCI): estudio de tamaño de objetivo para uso con el pulgar.
- **Fuentes:** ver fichas B-14 a B-22.

### A.8 "Uso de gestos y patrones de interacción móvil"
- **Clasificación:** CORRECTO. REQUIERE PRECISIÓN en dos puntos:
  1. [DOC] HIG Gestures: no redefinir gestos del sistema. Los gestos custom deben ser descubribles y "Not the only way to perform an important action". Los atajos complementan, no reemplazan. En juegos se aceptan varios controles en pantalla simultáneos.
  2. [DOC] Android: las apps no deberían *depender* de gestos para funciones básicas.
- **Qué enseñar:** tap, swipe, drag, hold, pinch; joystick virtual vs. toque directo; feedback háptico.
  - [DOC] HIG Playing haptics: consistente, complementario, sin abusar y **opcional**.
  - [DOC] Android haptics: "less is more"; entre háptica "buzzy" o ninguna, elegir ninguna.
  - Académico: Zaman, Natapov & Teather 2010 (pantalla táctil vs. controles físicos). El resultado concreto no se verificó en el texto primario (ver G).
- **Fuentes:** https://developer.apple.com/design/human-interface-guidelines/gestures · https://developer.apple.com/design/human-interface-guidelines/playing-haptics · https://developer.android.com/develop/ui/views/haptics/haptics-principles

### A.9 "Buenas prácticas de diseño centrado en el jugador"
- **Clasificación:** CONFUSO (genérico; aplica a cualquier plataforma).
- **Problema:** no dice qué es específico de móvil.
- **Qué enseñar (concreto y móvil):**
  - [DOC] HIG "Designing for games":
    - dejar jugar apenas termina la instalación;
    - descarga inicial de 30 minutos o menos;
    - enseñar jugando ("Teach through play");
    - pedir permisos en contexto;
    - texto en iOS de 17 pt por defecto y 11 pt mínimo.
  - Accesibilidad. [DOC] Game Accessibility Guidelines (nivel basic): controles virtuales grandes y espaciados, remapeo, toggle de háptica y controles simples.
  - Interrupciones: ver A.13.
  - [INF] Las "sesiones cortas" son práctica profesional (ej. Supercell). No se encontró en esta investigación una fuente académica verificada que la respalde como norma.
- **Fuentes:** https://developer.apple.com/design/human-interface-guidelines/designing-for-games · https://gameaccessibilityguidelines.com/full-list/

### A.10 "Estrategias de Monetización: Publicidad integrada (ads)"
- **Clasificación:** CORRECTO PERO INCOMPLETO.
- **Problema:** falta el marco de políticas, que también es diseño.
- **Qué enseñar:**
  - [DOC] AdMob: los interstitials van en transiciones naturales.
  - [DOC] AdMob prohíbe:
    - interstitials al abrir o salir de la app;
    - interstitials después de cada acción (máximo uno cada dos acciones);
    - un interstitial inmediatamente después de otro;
    - interstitials inesperados mientras el usuario juega.
  - [DOC] Rewarded ads: el usuario elige explícitamente ver el anuncio.
  - [DOC] Google Play Families: solo SDKs de anuncios autocertificados para niños; sin publicidad personalizada; sin anuncios engañosos.
  - [DOC] Apple 1.3 Kids Category: sin analítica ni publicidad de terceros, salvo excepciones limitadas.
  - [DOC] Unity: desde el 1 de abril de 2026, la integración directa de Unity Ads (Advertisement Legacy) "might see reduced ad performance". Se recomienda migrar a LevelPlay (mediación).
  - Caso: [DOC] Vampire Survivors en móvil, según Kotaku 2023 citando a poncle: "monetization is minimal and is designed to never interrupt your game, always be optional".
- **Fuentes:** https://support.google.com/admob/answer/6201362 · https://support.google.com/admob/answer/7372450 · https://support.google.com/googleplay/android-developer/answer/9893335 · https://docs.unity.com/en-us/grow/levelplay/sdk/unity/migrate-from-unity-ads-to-levelplay

### A.11 "Compras dentro de la aplicación (IAP)"
- **Clasificación:** REQUIERE PRECISIÓN.
- **Problema:** IAP no es una "estrategia" libre: las tiendas la imponen y la regulan.
- **Qué enseñar:**
  - [DOC] Apple 3.1.1: para desbloquear funciones o contenido (monedas, niveles, versión completa) "you must use in-app purchase".
  - [DOC] Apple 3.1.1: las loot boxes deben mostrar las probabilidades antes de la compra.
  - [DOC] Google Play Payments: uso obligatorio de Google Play Billing, con excepciones. Hay programas de facturación alternativa en "eligible countries/regions" (secciones 8 y 9).
  - [DOC] Google Play: divulgar las probabilidades de ítems aleatorios "in advance of, and in close and timely proximity to, that purchase".
  - [DOC] Unity IAP (`com.unity.purchasing`) 5.4.4 está publicado para 6000.3.
- **Por qué importa:** el diseño de la tienda dentro del juego está condicionado por reglas externas.
- **Fuentes:** https://developer.apple.com/app-store/review/guidelines/ · https://support.google.com/googleplay/android-developer/answer/9858738 · https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.purchasing.html

### A.12 "Modelos freemium e híbridos"
- **Clasificación:** CORRECTO PERO INCOMPLETO. Además, FALTA UN TEMA IMPORTANTE: ética y regulación.
- **Problema:**
  - Omite el modelo **premium**. Ejemplo: [DOC] Alto's Adventure en App Store, US$4,99, "no ads or in-app purchases".
  - Omite la mirada crítica.
- **Qué enseñar (mirada crítica, académica):**
  - Zagal, Björk & Lewis 2013 (FDG): dark patterns en juegos.
  - Zendle & Cairns 2018 (PLOS ONE, n = 7.422): asociación **correlacional** entre gasto en loot boxes y juego problemático.
  - Drummond & Sauer 2018 (Nature Human Behaviour): "loot boxes are psychologically akin to gambling".
  - Petrovskaya & Zendle 2021/2022 (J. Business Ethics, CC BY): 35 técnicas en 8 dominios.
  - Regulación:
    - [DOC] FTC vs. Epic 2022: USD 520 millones (275 M COPPA + 245 M en reembolsos) por dark patterns en la facturación de Fortnite.
    - [DOC] UK Gambling Commission (ABSG): Bélgica prohibió mecánicas de loot box en 2018.
- **Battle pass:** no se encontró una fuente académica verificada (ver G).

### A.13 FALTA UN TEMA IMPORTANTE: ciclo de vida e interrupciones
- **Clasificación:** FALTA UN TEMA IMPORTANTE (no aparece en el programa).
- **Qué enseñar:**
  - [DOC] Android Activity lifecycle: no usar `onPause` para guardar datos (es muy breve); usar `onStop`. El sistema mata procesos según su estado.
  - [DOC] iOS: estados active, inactive, background y suspended. Al pasar a background hay que liberar memoria y guardar datos.
  - [DOC] Unity: `OnApplicationPause` / `OnApplicationFocus`. En Android, el teclado en pantalla dispara `OnApplicationFocus(false)`.
- **Por qué importa:** llamadas, notificaciones o cambiar de app en medio de una partida son situaciones normales en móvil. Diseñar pausa automática y guardado es diseño de plataforma.

### A.14 "Testing y Portabilidad: Pruebas en diferentes resoluciones"
- **Clasificación:** CORRECTO PERO INCOMPLETO.
- **Problema:** resolución sola no alcanza. Hay que probar también relación de aspecto, densidad (dp/pt), safe area y cutouts, orientación y pantallas grandes.
- **Qué enseñar:**
  - [DOC] Unity Device Simulator simula safe area, auto-rotación y touch de un solo dedo. **No** simula rendimiento, memoria, capacidades de render ni giroscopio.
  - [DOC] **Android 16 (API 36) en pantallas de sw ≥ 600 dp:** ignora `screenOrientation`, `resizableActivity` y min/maxAspectRatio. La excepción son **los juegos, según `android:appCategory`**.
  - [DOC] En Unity 6.3, la opción Player Settings → Application Category tiene "Game" por defecto en proyectos nuevos, lo que "exempts applications from Android 16 behavior changes for large screens".
  - [INF] Conviene que el docente lo muestre en el Player Settings del proyecto: hay que revisar que un proyecto migrado no tenga cambiado ese valor.
  - [DOC] Para simular cutouts en Android: Opciones de desarrollador → "Simulate a display with a cutout".
- **Fuentes:** https://docs.unity3d.com/6000.3/Documentation/Manual/device-simulator-introduction.html · https://developer.android.com/about/versions/16/behavior-changes-16 (2026-10-01) · https://docs.unity3d.com/6000.3/Documentation/Manual/class-PlayerSettingsAndroid.html

### A.15 "Adaptación a múltiples sistemas operativos (Android, iOS)"
- **Clasificación:** REQUIERE PRECISIÓN.
- **Problema:** "adaptación" no aclara que hay toolchains, requisitos de tienda y comportamientos de sistema operativo distintos.
- **Qué enseñar:**
  - [DOC] Unity 6.3 en Android: Android 7.1 (API 25) o superior; Vulkan y OpenGL ES 3.0+; ASTC por defecto.
  - [DOC] Google Play exige AAB.
  - [DOC] Google Play, desde el 31-08-2026: apps nuevas y actualizaciones deben apuntar a **Android 16 (API 36)**. Se puede pedir una extensión hasta el 01-11-2026.
  - [DOC] iOS: Unity genera un proyecto Xcode y "Xcode is available only on macOS devices" (alternativa: Build Automation en la nube). Unity soporta iOS 15 o superior; Xcode 16 o superior recomendado.
- **Por qué importa:** en la UNJu puede no haber Mac disponible. [INF] Conviene declararlo como limitación práctica del curso.

### A.16 "Herramientas y frameworks de testing móvil"
- **Clasificación:** CORRECTO PERO INCOMPLETO / REQUIERE PRECISIÓN.
- **Problema:** mezcla en una sola línea emulación, perfilado, tests automatizados y granjas de dispositivos, que son cosas distintas.
- **Qué enseñar (taxonomía):**
  1. **Simulación en el editor:** Device Simulator, con layout únicamente.
  2. **Emulador / simulador:**
     - [DOC] Android Emulator: "In most cases, the emulator is the best option" para pruebas funcionales.
     - [DOC] Apple, WWDC19 418: el Simulator no simula los límites de memoria ni de CPU, y el rendimiento de GPU es el del Mac.
     - [DOC] Guía archivada de Apple (2018): el Simulator no usa TBDR.
  3. **Dispositivo real + profiler:**
     - [DOC] Unity Profiler con Development Build, para obtener "realistic performance metrics".
     - Android GPU Inspector, versión 3.3.3 (2026-04-28).
     - Arm Mobile Studio / Performance Studio.
     - Xcode Instruments.
  4. **Tests automatizados en dispositivo:** [DOC] Unity Test Framework, pestaña Player. Requisito: Editor y Player en la misma red.
  5. **Granjas en la nube:**
     - [DOC] Firebase Test Lab Game Loop (timeout por defecto de 3 min; Unity mencionado).
     - [DOC] AWS Device Farm (dispositivos físicos reales; solo región us-west-2).
  6. **Post-lanzamiento:** [DOC] Android vitals, con umbrales de crash 1,09 % y ANR 0,47 % en promedio general, 8 % por modelo de teléfono.
- **Por qué importa:** conecta con la Unidad 3 de testing de integración que ya se dictó (Asteroides).

### A.17 FALTA DESARROLLAR: tamaño de descarga y entrega de assets
- **Clasificación:** FALTA DESARROLLAR.
- **Qué enseñar:**
  - [DOC] Google Play: módulo base de hasta 500 MB comprimido; asset packs de 1,5 GB cada uno; install-time acumulado de 4 GB; on-demand/fast-follow de 30 GB; total de 34 GB. Play Asset Delivery tiene tres modos.
  - [DOC] Apple: 4 GB sin comprimir en iOS 9+.
  - [DOC] Apple (GameKit): ofrecer contenido suficiente en la instalación base y descargar el resto con Background Assets. On-Demand Resources figura como deprecado.
  - Detalle: [DOC] el ejecutable tiene un límite de 80 MB para el total de secciones `__TEXT`.
- **Por qué importa:** es una decisión de diseño. Define qué entra en la primera sesión.

---

## B) Fichas de recursos

Verificación: todas "fetch OK 2026-10-04" salvo que se indique otra cosa.

**B-01**
- **Título:** Application.targetFrameRate (Scripting API, Unity 6.3)
- **Autor:** Unity Technologies · **Tipo:** doc oficial · **Fecha:** Unity 6.3 LTS
- **URL:** https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Application-targetFrameRate.html
- **Tema:** fps y batería · **Concepto:** en móvil, con los valores por defecto renderiza a 30 fps fijos "to conserve battery power"
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** demo de 30 vs. 60 fps y discusión sobre batería · **Obligatorio**
- **Verificación:** fetch OK 2026-10-04

**B-02**
- **Título:** Screen.safeArea (Unity 6.3)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:** https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Screen-safeArea.html
- **Concepto:** zona visible en píxeles; origen abajo a la izquierda (distinto de UI Toolkit)
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** práctica de HUD con notch · **Obligatorio**
- **Verificación:** fetch OK

**B-03**
- **Título:** Screen.cutouts (Unity 6.3)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:** https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Screen-cutouts.html
- **Concepto:** lista de áreas sin contenido. La página no detalla las plataformas soportadas.
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** complementario a B-02 · **Complementario**
- **Verificación:** fetch OK

**B-04**
- **Título:** Device Simulator, introducción (Unity 6.3)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/device-simulator-introduction.html
- **Concepto:** qué simula (safe area, rotación, touch de un dedo) y qué **no** simula (rendimiento, memoria, render, giroscopio)
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** enseñar los límites de la herramienta antes de usarla · **Obligatorio**
- **Verificación:** fetch OK

**B-05**
- **Título:** Adaptive Performance (Manual Unity 6.3) y AdaptivePerformanceModule (API)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:**
  - https://docs.unity3d.com/6000.3/Documentation/Manual/adaptive-performance/adaptive-performance.html
  - https://docs.unity3d.com/6000.3/Documentation/ScriptReference/UnityEngine.AdaptivePerformanceModule.html
- **Concepto:** "built-in module"; ajuste de calidad según estado térmico; scalers; providers (Basic, Android)
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** mostrar que el motor tiene una respuesta a la térmica; no implementarla en profundidad · **Complementario**
- **Verificación:** fetch OK. Página de providers: https://docs.unity3d.com/6000.3/Documentation/Manual/adaptive-performance/providers.html (fetch OK)

**B-06**
- **Título:** Adaptive Performance package 6.0 (nota de estado)
- **Autor:** Unity · **Tipo:** doc de paquete
- **URL:** https://docs.unity3d.com/Packages/com.unity.adaptiveperformance@6.0/manual/index.html
- **Concepto:** el paquete "now contains only samples and visual scripting nodes" y la doc pasó al Manual
- **Nivel:** docente · **Confiabilidad:** alta
- **Uso:** explicar por qué en el proyecto aparece `com.unity.modules.adaptiveperformance` · **Complementario (docente)**
- **Verificación:** fetch OK

**B-07**
- **Título:** Unity Adaptive Performance and Android provider
- **Autor:** Android Developers (Google) · **Tipo:** doc oficial · **Fecha:** 2026-02-26
- **URL:** https://developer.android.com/games/engines/unity/unity-adpf
- **Concepto:** el provider Android implementa ADPF Performance Hint; scalers de framerate, resolución y LOD
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** puente Unity ↔ Android · **Complementario**
- **Verificación:** fetch OK

**B-08**
- **Título:** Android Dynamic Performance Framework (ADPF)
- **Autor:** Android Developers · **Tipo:** doc oficial · **Fecha:** 2026-02-26
- **URL:** https://developer.android.com/games/optimize/adpf
- **Concepto:** Thermal API, Performance Hint, Game Mode, Fixed Performance Mode; diversidad de topologías de núcleo
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** diapositiva "hardware que cambia en tiempo real" · **Obligatorio**
- **Verificación:** fetch OK

**B-09**
- **Título:** Thermal API (ADPF)
- **Autor:** Android Developers · **Tipo:** doc oficial · **Fecha:** 2026-02-26
- **URL:** https://developer.android.com/games/optimize/adpf/thermal
- **Concepto:** `getThermalHeadroom` (API 30+), estados térmicos
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** dato técnico citable · **Complementario**
- **Verificación:** fetch OK

**B-10**
- **Título:** ProcessInfo.ThermalState
- **Autor:** Apple · **Tipo:** doc oficial
- **URL:** https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum
- **Concepto:** nominal / fair / serious / critical (iOS 11+)
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** comparar Android y iOS · **Complementario**
- **Verificación:** fetch OK (contenido leído vía endpoint JSON de Apple: developer.apple.com/tutorials/data/documentation/foundation/processinfo/thermalstate-swift.enum.json)

**B-11**
- **Título:** Low memory killers
- **Autor:** Android Developers · **Tipo:** doc oficial · **Fecha:** 2026-09-21
- **URL:** https://developer.android.com/topic/performance/issues/lmk
- **Concepto:** LMK, `oom_adj_score`, `ApplicationExitInfo`; callbacks de trim deprecados salvo dos
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** corregir la idea de que `onTrimMemory` "previene" kills · **Obligatorio**
- **Verificación:** fetch OK

**B-12**
- **Título:** Android vitals
- **Autor:** Android Developers · **Tipo:** doc oficial · **Fecha:** 2026-09-21
- **URL:** https://developer.android.com/topic/performance/vitals
- **Concepto:** core vitals (crash, ANR, wake locks, memoria); umbrales; memoria por RAM para juegos; impacto en visibilidad desde febrero de 2027
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** "la tienda mide la calidad técnica" · **Obligatorio**
- **Verificación:** fetch OK

**B-13**
- **Título:** applicationDidReceiveMemoryWarning(_:)
- **Autor:** Apple · **Tipo:** doc oficial
- **URL:** https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationdidreceivememorywarning(_:)
- **Concepto:** si no se libera memoria, el sistema puede terminar la app
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** comparativo de iOS · **Complementario**
- **Verificación:** fetch OK (vía endpoint JSON)

**B-14**
- **Título:** Tailor your apps for Apple GPUs and tile-based deferred rendering
- **Autor:** Apple · **Tipo:** doc oficial
- **URL:** https://developer.apple.com/documentation/metal/tailor-your-apps-for-apple-gpus-and-tile-based-deferred-rendering
- **Concepto:** TBDR, memoria de tile (ancho de banda, latencia, energía), eliminación de superficies ocultas
- **Nivel:** intermedio/avanzado · **Confiabilidad:** alta
- **Uso:** explicar con un diagrama por qué importa el overdraw · **Obligatorio (un fragmento)**
- **Verificación:** fetch OK (vía endpoint JSON)

**B-15**
- **Título:** HIG, Buttons
- **Autor:** Apple · **Tipo:** guía oficial · **Fecha:** change log 2025-12-16
- **URL:** https://developer.apple.com/design/human-interface-guidelines/buttons
- **Concepto:** hit region de al menos 44×44 pt (visionOS 60×60)
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** regla de diseño de HUD · **Obligatorio**
- **Verificación:** fetch OK (vía endpoint JSON)

**B-16**
- **Título:** HIG, Accessibility
- **Autor:** Apple · **Tipo:** guía oficial · **Fecha:** change log 2025-06-09
- **URL:** https://developer.apple.com/design/human-interface-guidelines/accessibility
- **Concepto:** 44×44 pt por defecto y 28×28 pt mínimo (iOS); padding de 12/24 pt; alternativas a los gestos
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** checklist de accesibilidad · **Obligatorio**
- **Verificación:** fetch OK

**B-17**
- **Título:** HIG, Layout
- **Autor:** Apple · **Tipo:** guía oficial · **Fecha:** change log 2026-09-09
- **URL:** https://developer.apple.com/design/human-interface-guidelines/layout
- **Concepto:** safe areas, Dynamic Island, size classes
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** layout de HUD · **Complementario**
- **Verificación:** fetch OK

**B-18**
- **Título:** HIG, Gestures
- **Autor:** Apple · **Tipo:** guía oficial · **Fecha:** change log 2024-09-09
- **URL:** https://developer.apple.com/design/human-interface-guidelines/gestures
- **Concepto:** gestos estándar; no reemplazar gestos del sistema; un gesto custom nunca debe ser la única vía
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** diseño de controles · **Obligatorio**
- **Verificación:** fetch OK

**B-19**
- **Título:** HIG, Designing for games
- **Autor:** Apple · **Tipo:** guía oficial · **Fecha:** change log 2025-06-09 (página nueva de 2024-06-10)
- **URL:** https://developer.apple.com/design/human-interface-guidelines/designing-for-games
- **Concepto:** controles táctiles de 44×44 pt (mínimo 28×28); jugar apenas instala; descarga inicial de 30 min o menos; "Teach through play"; texto de 17/11 pt; menús adaptables 16:10, 19.5:9, 4:3
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** **recurso central** de la parte de UX · **Obligatorio**
- **Verificación:** fetch OK

**B-20**
- **Título:** HIG, Playing haptics
- **Autor:** Apple · **Tipo:** guía oficial · **Fecha:** change log 2024-05-07
- **URL:** https://developer.apple.com/design/human-interface-guidelines/playing-haptics
- **Concepto:** consistente, complementaria, sin abuso, opcional
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** feedback · **Complementario**
- **Verificación:** fetch OK

**B-21**
- **Título:** Make apps more accessible
- **Autor:** Android Developers · **Tipo:** doc oficial · **Fecha:** 2026-09-22
- **URL:** https://developer.android.com/guide/topics/ui/accessibility/apps
- **Concepto:** touch target de 48×48 dp; contraste 4.5:1 / 3:1
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** comparar pt y dp · **Obligatorio**
- **Verificación:** fetch OK

**B-22**
- **Título:** Haptics design principles
- **Autor:** Android Developers · **Tipo:** doc oficial · **Fecha:** 2026-09-29
- **URL:** https://developer.android.com/develop/ui/views/haptics/haptics-principles
- **Concepto:** clear / rich / buzzy; "less is more"; evitar vibraciones legacy
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** feedback · **Complementario**
- **Verificación:** fetch OK

**B-23**
- **Título:** Support display cutouts
- **Autor:** Android Developers · **Tipo:** doc oficial · **Fecha:** 2026-09-22
- **URL:** https://developer.android.com/develop/ui/views/layout/display-cutout
- **Concepto:** modos de cutout; edge-to-edge obligatorio en Android 15 / SDK 35; simular cutout desde opciones de desarrollador
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** práctica en dispositivo real · **Complementario**
- **Verificación:** fetch OK

**B-24**
- **Título:** Android 16, behavior changes (apps que apuntan a 16)
- **Autor:** Android Developers · **Tipo:** doc oficial · **Fecha:** 2026-10-01
- **URL:** https://developer.android.com/about/versions/16/behavior-changes-16
- **Concepto:** en sw ≥ 600 dp se ignoran orientación, resizability y aspect ratio; **los juegos quedan exceptuados (`appCategory`)**
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** caso de portabilidad (tablets y plegables) · **Obligatorio**
- **Verificación:** fetch OK

**B-25**
- **Título:** Android Player settings (Unity 6.3)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/class-PlayerSettingsAndroid.html
- **Concepto:** Application Category "Game" por defecto (exime de los cambios de Android 16); Render Outside Safe Area (ignorado en Android 15+); orientaciones permitidas; Optimized Frame Pacing
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** revisar en vivo el Player Settings del proyecto · **Obligatorio**
- **Verificación:** fetch OK

**B-26**
- **Título:** Meet Google Play's target API level requirement
- **Autor:** Android Developers · **Tipo:** doc oficial · **Fecha:** 2026-10-01
- **URL:** https://developer.android.com/google/play/requirements/target-sdk
- **Concepto:** desde el 31-08-2026, apps nuevas y actualizaciones deben apuntar a API 36; extensión hasta el 01-11-2026
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** "la plataforma cambia cada año" · **Obligatorio**
- **Verificación:** fetch OK

**B-27**
- **Título:** Android requirements and compatibility (Unity 6.3)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/android-requirements-and-compatibility.html
- **Concepto:** API 25 o superior; Vulkan y GLES 3.0+; ASTC por defecto; descompresión en runtime si el dispositivo no soporta el formato
- **Nivel:** inicial · **Confiabilidad:** alta · **Complementario**
- **Verificación:** fetch OK

**B-28**
- **Título:** Build your application for Android / Build an iOS application (Unity 6.3)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:**
  - https://docs.unity3d.com/6000.3/Documentation/Manual/android-BuildProcess.html
  - https://docs.unity3d.com/6000.3/Documentation/Manual/iphone-BuildProcess.html
- **Concepto:** APK vs. AAB (Google Play exige AAB); iOS → proyecto Xcode, que requiere macOS
- **Nivel:** inicial · **Confiabilidad:** alta · **Obligatorio**
- **Verificación:** fetch OK ambas

**B-29**
- **Título:** iOS requirements and compatibility (Unity 6.3)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/ios-requirements-and-compatibility.html
- **Concepto:** iOS 15 o superior; Xcode 16 o superior recomendado; Metal; ASTC/ETC
- **Nivel:** inicial · **Confiabilidad:** alta · **Complementario**
- **Verificación:** fetch OK

**B-30**
- **Título:** Run Play mode tests in a Player (Unity 6.3)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/test-framework/workflow-run-playmode-test-standalone.html
- **Concepto:** pestaña Player del Test Runner; misma red Editor/Player; export en Android/iOS
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** continuidad con la Unidad 3 (Asteroides) · **Obligatorio**
- **Verificación:** fetch OK

**B-31**
- **Título:** Collect performance data on a target platform (Unity 6.3)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/profiling-target-device.html
- **Concepto:** perfilar en dispositivo con Development Build
- **Nivel:** intermedio · **Confiabilidad:** alta · **Obligatorio**
- **Verificación:** fetch OK

**B-32**
- **Título:** Canvas Scaler / Designing UI for Multiple Resolutions (uGUI 2.0)
- **Autor:** Unity · **Tipo:** doc de paquete
- **URL:**
  - https://docs.unity3d.com/Packages/com.unity.ugui@2.0/manual/script-CanvasScaler.html
  - https://docs.unity3d.com/Packages/com.unity.ugui@2.0/manual/HOWTO-UIMultiResolution.html
- **Concepto:** Scale With Screen Size, Reference Resolution, Match 0–1, anchors
- **Nivel:** inicial · **Confiabilidad:** alta · **Obligatorio**
- **Verificación:** fetch OK ambas

**B-33**
- **Título:** Panel Settings (UI Toolkit, Unity 6.3)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:** https://docs.unity3d.com/6000.3/Documentation/Manual/UIE-Runtime-Panel-Settings.html
- **Concepto:** Scale Mode equivalentes a los de uGUI
- **Nivel:** inicial · **Confiabilidad:** alta · **Complementario**
- **Verificación:** fetch OK

**B-34**
- **Título:** Screen.orientation (Unity 6.3)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:** https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Screen-orientation.html
- **Concepto:** AutoRotation; las coordenadas de touch rotan con la pantalla
- **Nivel:** inicial · **Confiabilidad:** alta · **Complementario**
- **Verificación:** fetch OK

**B-35**
- **Título:** Input System, Touch support y On-screen Controls
- **Autor:** Unity · **Tipo:** doc de paquete
- **URL:**
  - https://docs.unity3d.com/Packages/com.unity.inputsystem@1.17/manual/Touch.html
  - https://docs.unity3d.com/Packages/com.unity.inputsystem@1.17/manual/OnScreen.html
- **Concepto:** `EnhancedTouchSupport.Enable()`; Finger vs. Touch; TouchSimulation; OnScreenStick y OnScreenButton (simulan control paths de gamepad)
- **Nivel:** intermedio · **Confiabilidad:** alta · **Obligatorio**
- **Verificación:** fetch OK. **Atención:** la versión publicada para 6000.3 es la **1.20.0** (https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.inputsystem.html, fetch OK), pero las URL `@1.20/manual/Touch.html` y `@1.20/manual/OnScreen.html` devolvieron 404 (la doc 1.20 parece reestructurada). Se cita la 1.17 como referencia conceptual. El docente debería ubicar la página equivalente en la 1.20.

**B-36**
- **Título:** Input.touches (legacy)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:** https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Input-touches.html
- **Concepto:** "part of the legacy Input Manager... don't use this API in new projects"
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** solo para leer código viejo · **Complementario**
- **Verificación:** fetch OK

**B-37**
- **Título:** OnApplicationPause / OnApplicationFocus (Unity 6.3)
- **Autor:** Unity · **Tipo:** doc oficial
- **URL:**
  - https://docs.unity3d.com/6000.3/Documentation/ScriptReference/MonoBehaviour.OnApplicationPause.html
  - https://docs.unity3d.com/6000.3/Documentation/ScriptReference/MonoBehaviour.OnApplicationFocus.html
- **Concepto:** interrupciones; caso del teclado en Android
- **Nivel:** inicial · **Confiabilidad:** alta · **Obligatorio**
- **Verificación:** fetch OK ambas

**B-38**
- **Título:** The activity lifecycle (Android) / Managing your app's life cycle (iOS)
- **Autor:** Google / Apple · **Tipo:** doc oficial
- **URL:**
  - https://developer.android.com/guide/components/activities/activity-lifecycle
  - https://developer.apple.com/documentation/uikit/managing-your-app-s-life-cycle
- **Concepto:** no guardar en `onPause`; los procesos se matan según su estado; background → liberar memoria y guardar
- **Nivel:** intermedio · **Confiabilidad:** alta · **Complementario**
- **Verificación:** fetch OK ambas (Apple vía endpoint JSON)

**B-39**
- **Título:** Game Loop tests (Firebase Test Lab)
- **Autor:** Google Firebase · **Tipo:** doc oficial · **Fecha:** 2026-10-01
- **URL:** https://firebase.google.com/docs/test-lab/android/game-loop
- **Concepto:** escenarios lanzados por intent; timeout de 3 min; Unity soportado
- **Nivel:** intermedio · **Confiabilidad:** alta · **Complementario**
- **Verificación:** fetch OK

**B-40**
- **Título:** What is AWS Device Farm?
- **Autor:** AWS · **Tipo:** doc oficial
- **URL:** https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html
- **Concepto:** dispositivos físicos remotos; Appium; solo us-west-2; servicio pago (tiene pricing)
- **Nivel:** intermedio · **Confiabilidad:** alta · **Complementario**
- **Verificación:** fetch OK

**B-41**
- **Título:** Android Emulator (Run apps on the Android Emulator)
- **Autor:** Android Developers · **Tipo:** doc oficial · **Fecha:** 2026-03-06
- **URL:** https://developer.android.com/studio/run/emulator
- **Concepto:** requisitos (16 GB de RAM); el emulador sirve para la mayoría de las pruebas funcionales. [INF] No reemplaza al dispositivo para rendimiento y térmica: eso se apoya en B-04, B-31 y en el e-book p. 11, no en esta página.
- **Nivel:** inicial · **Confiabilidad:** alta · **Complementario**
- **Verificación:** fetch OK

**B-42**
- **Título:** Testing and Debugging in Simulator (archivada)
- **Autor:** Apple · **Tipo:** doc oficial archivada · **Fecha:** 2018-02-15, "deprecated in Xcode 9"
- **URL:** https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/iOS_Simulator_Guide/TestingontheiOSSimulator/TestingontheiOSSimulator.html
- **Concepto:** el Simulator no usa TBDR y su rendimiento no tiene relación con el del dispositivo
- **Nivel:** docente · **Confiabilidad:** media (es histórica; complementar con B-53 / WWDC19 418)
- **Uso:** solo como apoyo · **Complementario**
- **Verificación:** fetch OK

**B-43**
- **Título:** Play Asset Delivery
- **Autor:** Android Developers · **Tipo:** doc oficial · **Fecha:** 2025-09-18
- **URL:** https://developer.android.com/guide/playcore/asset-delivery
- **Concepto:** install-time, fast-follow, on-demand
- **Nivel:** intermedio · **Confiabilidad:** alta · **Complementario**
- **Verificación:** fetch OK

**B-44**
- **Título:** Optimize your app's size / límites de tamaño
- **Autor:** Google Play Console Help · **Tipo:** ayuda oficial · **Fecha:** sin fecha visible
- **URL:** https://support.google.com/googleplay/android-developer/answer/9859372
- **Concepto:** base de 500 MB; pack de 1,5 GB; install-time de 4 GB; on-demand de 30 GB; total de 34 GB
- **Nivel:** inicial · **Confiabilidad:** alta · **Complementario**
- **Verificación:** fetch OK

**B-45**
- **Título:** Maximum build file sizes (App Store Connect) / Improving the player experience for games with large downloads (GameKit)
- **Autor:** Apple · **Tipo:** ayuda y doc oficial
- **URL:**
  - https://developer.apple.com/help/app-store-connect/reference/app-uploads/maximum-build-file-sizes
  - https://developer.apple.com/documentation/gamekit/improving-the-player-experience-for-games-with-large-downloads
- **Concepto:** 4 GB sin comprimir; Background Assets; ODR deprecado; descarga inicial de 30 min o menos
- **Nivel:** intermedio · **Confiabilidad:** alta · **Complementario**
- **Verificación:** fetch OK ambas (GameKit vía endpoint JSON)

**B-46**
- **Título:** App Review Guidelines (3.1.1, 3.1.2, 1.3)
- **Autor:** Apple · **Tipo:** política oficial · **Fecha:** sin fecha visible en la página
- **URL:** https://developer.apple.com/app-store/review/guidelines/
- **Concepto:** IAP obligatorio para contenido digital; divulgación de probabilidades de loot boxes; Kids Category sin ads de terceros
- **Nivel:** inicial · **Confiabilidad:** alta · **Obligatorio**
- **Verificación:** fetch OK

**B-47**
- **Título:** Payments policy (Google Play)
- **Autor:** Google · **Tipo:** política oficial
- **URL:** https://support.google.com/googleplay/android-developer/answer/9858738
- **Concepto:** Google Play Billing obligatorio, con facturación alternativa en regiones elegibles; divulgación de probabilidades de ítems aleatorios
- **Nivel:** inicial · **Confiabilidad:** alta · **Obligatorio**
- **Verificación:** fetch OK

**B-48**
- **Título:** Families policy (Google Play)
- **Autor:** Google · **Tipo:** política oficial
- **URL:** https://support.google.com/googleplay/android-developer/answer/9893335
- **Concepto:** SDKs de ads autocertificados; sin publicidad personalizada a niños; age screen neutral
- **Nivel:** inicial · **Confiabilidad:** alta · **Complementario**
- **Verificación:** fetch OK

**B-49**
- **Título:** Disallowed interstitial implementations / Interstitial ad guidance / Rewarded ads (AdMob)
- **Autor:** Google AdMob · **Tipo:** política oficial
- **URL:**
  - https://support.google.com/admob/answer/6201362
  - https://support.google.com/admob/answer/6066980
  - https://support.google.com/admob/answer/7372450
- **Concepto:** reglas de cuándo **no** mostrar un interstitial; rewarded con opt-in explícito
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** ejercicio de análisis de casos de ads · **Obligatorio**
- **Verificación:** fetch OK las tres

**B-50**
- **Título:** Migrate from Unity Ads to LevelPlay / Placements
- **Autor:** Unity (Grow) · **Tipo:** doc oficial
- **URL:**
  - https://docs.unity.com/en-us/grow/levelplay/sdk/unity/migrate-from-unity-ads-to-levelplay
  - https://docs.unity.com/en-us/grow/levelplay/platform/settings/placements
- **Concepto:** mediación; placements con nombre de momento del juego (Level_Complete, Game_Over); capping y pacing
- **Nivel:** intermedio · **Confiabilidad:** alta
- **Uso:** solo mostrar el concepto de placement, sin integrar · **Complementario**
- **Verificación:** fetch OK ambas

**B-51**
- **Título:** Video game loot boxes are linked to problem gambling (Zendle & Cairns)
- **Tipo:** paper académico, PLOS ONE · **Fecha:** 2018-11-21 · **Acceso:** abierto (CC BY)
- **URL:** https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0206767
- **Concepto:** n = 7.422; asociación **correlacional**
- **Nivel:** avanzado/lectura · **Confiabilidad:** alta (con límites declarados: muestra de Reddit, autoselección)
- **Uso:** debate de ética · **Obligatorio (lectura breve)**
- **Verificación:** fetch OK

**B-52**
- **Título:** Predatory Monetisation? (Petrovskaya & Zendle)
- **Tipo:** paper, Journal of Business Ethics · **Fecha:** online 2021-10-20; impreso vol. 181(4), 2022, pp. 1065-1081 · **Acceso:** CC BY 4.0
- **URL:** https://doi.org/10.1007/s10551-021-04970-6
- **Concepto:** 35 técnicas en 8 dominios, desde la perspectiva del jugador (n = 1.104)
- **Nivel:** avanzado · **Confiabilidad:** alta · **Complementario**
- **Verificación:** metadatos vía https://api.crossref.org/works/10.1007/s10551-021-04970-6 (fetch OK). La página de Springer redirige a login (no se leyó el texto completo).

**B-53**
- **Título:** Video game loot boxes are psychologically akin to gambling (Drummond & Sauer)
- **Tipo:** comentario/paper, Nature Human Behaviour 2(8), 530-532 · **Fecha:** 2018-06-18 · **Acceso:** posiblemente pago (no verificado)
- **URL:** https://doi.org/10.1038/s41562-018-0360-1
- **Concepto:** comparación psicológica entre loot boxes y juego de azar
- **Nivel:** avanzado · **Confiabilidad:** alta · **Complementario**
- **Verificación:** metadatos vía Crossref (fetch OK); nature.com redirige a login

**B-54**
- **Título:** FTC: Fortnite Video Game Maker Epic Games to Pay More Than Half a Billion Dollars...
- **Autor:** US Federal Trade Commission · **Tipo:** comunicado oficial · **Fecha:** 2022-12-19
- **URL:** https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations
- **Concepto:** dark patterns en la facturación ("counterintuitive, inconsistent, and confusing button configuration"); COPPA
- **Nivel:** inicial · **Confiabilidad:** alta
- **Uso:** caso real de diseño de UI con consecuencias legales · **Obligatorio**
- **Verificación:** fetch OK

**B-55**
- **Título:** International approaches, lootboxes (ABSG advice)
- **Autor:** UK Gambling Commission · **Tipo:** documento de regulador · **Fecha:** 2024-11-06
- **URL:** https://www.gamblingcommission.gov.uk/manual/lootboxes-advice-to-the-gambling-commission-from-absg/international-approaches-lootboxes-advice-to-the-gambling-commission-from
- **Concepto:** Bélgica prohibió mecánicas de loot box en 2018; caso Países Bajos (FIFA Ultimate Team)
- **Nivel:** inicial · **Confiabilidad:** media-alta (es fuente secundaria sobre Bélgica; la fuente primaria belga no se pudo abrir)
- **Uso:** mapa regulatorio · **Complementario**
- **Verificación:** fetch OK

**B-56**
- **Título:** How Do Users Really Hold Mobile Devices? (Steven Hoober)
- **Tipo:** artículo **profesional** (UXmatters) · **Fecha:** 2013-02-18
- **URL:** https://www.uxmatters.com/mt/archives/2013/02/how-do-users-really-hold-mobile-devices.php
- **Concepto:** 1.333 observaciones; 49 % / 36 % / 15 %; los usuarios cambian de agarre
- **Nivel:** inicial · **Confiabilidad:** media (observacional, de 2013, no revisado por pares)
- **Uso:** disparador para diseñar zonas del pulgar, con advertencia de antigüedad · **Complementario**
- **Verificación:** fetch OK

**B-57**
- **Título:** Target size study for one-handed thumb use on small touchscreen devices (Parhi, Karlson, Bederson)
- **Tipo:** paper académico, MobileHCI '06, pp. 203-210 · **Fecha:** 2006-09-12
- **URL:** https://doi.org/10.1145/1152215.1152260
- **Concepto:** tamaño de objetivo para el pulgar
- **Nivel:** avanzado · **Confiabilidad:** alta (paper revisado por pares)
- **Uso:** respaldo académico de los mínimos de tamaño · **Complementario**
- **Verificación:** metadatos vía Crossref (fetch OK). El valor "9,2 mm / 9,6 mm" no se leyó en el paper (ver G).

**B-58**
- **Título:** Game Accessibility Guidelines (lista completa)
- **Autor:** colectivo de estudios y especialistas · **Tipo:** guía profesional
- **URL:** https://gameaccessibilityguidelines.com/full-list/
- **Concepto:** niveles basic/intermediate/advanced; controles grandes, remapeo, toggle de háptica, evitar button mashing
- **Nivel:** inicial · **Confiabilidad:** alta (referencia de industria)
- **Uso:** checklist de la entrega · **Obligatorio**
- **Verificación:** fetch OK

**B-59**
- **Título:** Optimize power efficiency (juegos Android)
- **Autor:** Android Developers · **Tipo:** doc oficial · **Fecha:** 2026-02-26
- **URL:** https://developer.android.com/games/optimize/power
- **Concepto:** frecuencia de refresco = fps objetivo; Vulkan; Thermal API; Game Mode
- **Nivel:** intermedio · **Confiabilidad:** alta · **Obligatorio**
- **Verificación:** fetch OK

**B-60**
- **Título:** Android GPU Inspector
- **Autor:** Android Developers · **Tipo:** herramienta oficial gratuita
- **URL:** https://developer.android.com/agi
- **Concepto:** perfilado de sistema y de frame (Adreno, Mali, PowerVR); versión 3.3.3 del 2026-04-28
- **Nivel:** avanzado · **Confiabilidad:** alta
- **Uso:** mención, sin práctica · **Complementario**
- **Verificación:** fetch OK

**B-61**
- **Título:** Apple Unity Plug-ins
- **Autor:** Apple (GitHub oficial) · **Tipo:** repositorio
- **URL:** https://github.com/apple/unityplugins
- **Concepto:** Accessibility, CoreHaptics, GameKit, StoreKit, BackgroundAssets para Unity; iOS 15.6+
- **Nivel:** avanzado · **Confiabilidad:** alta
- **Uso:** mención · **Complementario**
- **Verificación:** fetch OK

Total de fichas B: **61** (algunas agrupan 2 o 3 URL de la misma fuente). Para la selección del docente, las marcadas "Obligatorio" son 30.

---

## C) Videos

Los títulos y canales de YouTube están verificados con oEmbed (no da duración ni fecha). En las páginas GDC Vault y Apple Developer se verificaron con fetch título, ponente, evento y nivel de acceso.

**C-01 (técnico/demostrativo):** "Unity Input System in Unity 6 (3/7): Input System Mobile controls"
- **Canal:** Unity · **URL:** https://www.youtube.com/watch?v=aI-r7ILNDug
- **Verificación:** oEmbed OK. Forma parte del curso Unity Learn "Input System Video Series" (Unity 6.3, 1 h 20 min en total; https://learn.unity.com/course/input-system-video-series, fetch OK).
- **Duración:** no verificada · **Fragmento:** a determinar por el docente
- **Uso:** On-Screen Stick y Button. **Obligatorio.**

**C-02 (conceptual/caso):** "Bridging the Gap Between UX Principles and Game Design", Jim Brown (Epic Games), GDC 2018
- **Canal:** GDC Festival of Gaming · **URL:** https://www.youtube.com/watch?v=73Pqsk74Jc0
- **Verificación:** oEmbed OK. GDC Vault https://gdcvault.com/play/1025393/Bridging-the-Gap-Between-UX: **free content**, fetch OK.
- **Duración:** no verificada (una página de terceros dice 29 min; no se usó como fuente) · **Fragmento:** a determinar
- **Uso:** UX y game design. **Complementario.**

**C-03 (conceptual, crítico):** "Monetization Design: The Dark Side of Gacha" (Pixonic, War Robots; GDC 2019 según el buscador)
- **Canal:** GDC Festival of Gaming · **URL:** https://www.youtube.com/watch?v=LnCOkQ-f8AQ
- **Verificación:** oEmbed OK (título y canal). Ponente y año: solo según el buscador; la página de Vault no se abrió.
- **Duración:** no verificada · **Fragmento:** a determinar
- **Uso:** mirada crítica a la monetización. **Obligatorio** (o fragmento).

**C-04 (conceptual):** "Controls You Can Feel: Putting Tactility Back Into Touch Controls", Zach Gage, GDC 2012 (Smartphone & Tablet Games Summit)
- **URL:** https://gdcvault.com/play/1016074/Controls-You-Can-Feel-Putting · otra entrada en Vault: https://gdcvault.com/play/1015663/Controls-You-Can-Feel-Putting
- **Verificación:** fetch OK. **Free content**, formato video. No se encontró URL de YouTube verificada.
- **Duración:** no verificada · **Fragmento:** a determinar
- **Uso:** controles táctiles sin feedback físico. **Obligatorio.**

**C-05 (caso real):** "Designing Monument Valley: Less Game, More Experience", Ken Wong (ustwo), GDC Europe 2014
- **URL:** https://gdcvault.com/play/1020878/Designing-Monument-Valley-Less-Game
- **Verificación:** fetch OK, **free content**
- **Duración:** no verificada · **Fragmento:** a determinar
- **Uso:** experiencia corta, UX de estudio de apps. **Complementario.**

**C-06 (conceptual, ética de UX):** "Dark Patterns: How Good UX Can Be Bad UX", Anisa Sanusi (Frontier), GDC 2017
- **URL:** https://gdcvault.com/play/1024180/Dark-Patterns-How-Good-UX
- **Verificación:** fetch OK, **free content**
- **Duración:** no verificada · **Fragmento:** a determinar
- **Uso:** complementa a Zagal et al. **Complementario.**

**C-07 (técnico):** WWDC19 Session 422, "Designing for Adverse Network and Temperature Conditions" (Apple)
- **URL:** https://developer.apple.com/videos/play/wwdc2019/422/
- **Verificación:** fetch OK. Gratuito.
- **Duración:** no verificada.
- **Fragmento verificado:** según la transcripción de la página, la parte térmica empieza ~19:40, las definiciones de estados ~21:30, Device Conditions de Xcode ~31:00 y la demo Fox 2 ~37:00.
- **Uso:** térmica con ejemplos de degradación de calidad. **Obligatorio (fragmento 19:40–31:00).**

**C-08 (técnico):** WWDC19 Session 606, "Delivering Optimized Metal Apps and Games" (Apple)
- **URL:** https://developer.apple.com/videos/play/wwdc2019/606/
- **Verificación:** fetch OK. Gratuito.
- **Duración:** no verificada · **Fragmento:** a determinar (contiene 18 buenas prácticas: overdraw, compresión de texturas, memoria de tile, térmica)
- **Uso:** solo para el docente o alumnos avanzados. **Complementario.**

**C-09 (técnico):** WWDC19 Session 418, "Getting the Most Out of Simulator" (Apple)
- **URL:** https://developer.apple.com/videos/play/wwdc2019/418/
- **Verificación:** fetch OK
- **Concepto:** el Simulator no simula los límites de memoria ni de CPU; el rendimiento de GPU es el del Mac
- **Duración y fragmento:** a determinar
- **Uso:** testing. **Complementario.**

**C-10 (demostrativo/técnico):** "Optimizing mobile games using Arm Mobile Studio"
- **Canal:** Arm® · **URL:** https://www.youtube.com/watch?v=gcxIuwBZyic
- **Verificación:** oEmbed OK
- **Duración y fragmento:** no verificados
- **Uso:** perfilado de hardware. **Complementario.**

**C-11 (técnico, posiblemente pago):** "Performance Tuning and Upscaling for Mobile Development in Unity (Presented by Arm)", John French (Arm) y Dominic de Graaf, GDC 2026
- **URL:** https://gdcvault.com/play/1035616/Performance-Tuning-and-Upscaling-for
- **Verificación:** fetch OK. Acceso: la página indica que los usuarios gratuitos acceden al 30 % del contenido de los últimos 2 años y el acceso completo requiere membresía. **Puede ser pago.**
- **Uso:** solo si está libre. **Complementario.**

**C-12 (histórico, DESACTUALIZADO para 6.3):** "Build stunning mobile games that run smoothly with Adaptive Performance"
- **Canal:** **Unity Middle East** (no es el canal principal de Unity) · **URL:** https://www.youtube.com/watch?v=NYiTkPCZjuk
- **Verificación:** oEmbed OK. Blog asociado: https://unity.com/blog/games/build-stunning-mobile-games-that-run-smoothly-with-adaptive-performance (2021-03-30, David Berger, fetch OK). Describe la etapa Samsung-only.
- **Uso:** no usar como referencia de Unity 6.3. Como mucho, como contexto histórico.

---

## D) PDFs descargables legales

**D-01: "Optimize your game performance for mobile, XR, and the web in Unity (Unity 6 edition)"**
- **Autor y fecha:** Unity Technologies; landing del 2024-10-17; 100 páginas.
- **Acceso:** gratis, la landing pide formulario.
- **URL landing:** https://unity.com/resources/mobile-xr-web-game-performance-optimization-unity-6 (fetch OK)
- **URL PDF:** https://cdn.bfldr.com/S5BC9Y64/at/3mp8w3wk36k2k6mmj5pbbr/Optimize_your_game_performance_for_mobile__XR__and_the_web_in_Unity_Unity_6_edition_e-book.pdf (fetch OK; texto extraído y leído)
- **Páginas recomendadas (verificadas en el índice y el texto):**
  - p. 11 "Profile early, often, and on the target device"
  - p. 18 presupuesto por frame
  - p. 19 "Account for device temperature" (regla del 65 %; ~22 ms a 30 fps y ~11 ms a 60 fps; sin refrigeración activa)
  - p. 20 probar en dispositivos de gama mínima y máxima
  - pp. 21-24 memoria y GC
  - p. 25 Adaptive Performance
  - p. 42 "Choose the right frame rate" ("Unity defaults to 30 fps for mobile")
  - p. 60 "Avoid mobile native resolution"
  - p. 63 "Minimize overdraw and alpha blending"
  - pp. 67-72 UI (uGUI y UI Toolkit, incluida la p. 69 "Use multiple resolutions and aspect ratios")
- **Uso docente:** lectura guiada de 4 o 5 secciones; no el libro entero.
- **Precisión:** el e-book es de 2024 (Unity 6.0). Algunas afirmaciones sobre Adaptive Performance pueden ser anteriores al cambio a módulo built-in de 6.3: contrastar con B-05.

**D-02: Arm GPU Best Practices Developer Guide, Revision 3.4, Issue 10**
- **Autor y fecha:** Arm; emitido el 2025-01-31; 135 páginas; Non-Confidential; gratis.
- **URL PDF:** https://documentation-service.arm.com/static/67a62b17091bfc3e0a947695 (fetch OK; texto leído)
- **Landing:** https://developer.arm.com/documentation/101897 redirige a https://support.arm.com/documentation/101897 (la landing no devolvió contenido legible)
- **Páginas recomendadas (verificadas):**
  - §1.3 "The graphics rendering pipeline" (p. 8)
  - §2.3 "Memory bandwidth" (p. 15): "Memory bandwidth requires a lot of power... more restricted in mobile devices compared to desktop systems"; "Overdraw causes excess memory bandwidth use"; "Excess memory bandwidth use causes excess power use"
  - §2.4 "Converting from desktop to mobile" (p. 16)
- **Uso docente:** la sección 2.3 completa (1 página) como lectura obligatoria corta.

**D-03: Zendle & Cairns 2018, PLOS ONE** (open access; ver B-51). Hay versión PDF desde la página del artículo.

**D-04: Petrovskaya & Zendle 2021, J. Business Ethics** (CC BY 4.0; ver B-52). El PDF debería ser accesible por DOI, pero en esta sesión Springer redirigió a login. Verificar el acceso desde la red de la UNJu.

**D-05: Zagal, Björk & Lewis 2013, "Dark Patterns in the Design of Games" (FDG 2013, pp. 39-46)**
- La URL histórica http://www.fdg2013.org/program/papers/paper06_zagal_etal.pdf falló con "certificate has expired".
- **NO VERIFICADO** (ver G). No distribuir hasta confirmar una copia legal.

**D-06: Apple WWDC19 422, slides PDF:** la página de la sesión lista "Presentation Slides (PDF)" (fetch OK de la página; el PDF no se abrió).

---

## E) Datos técnicos verificados citables

1. En Unity, en Android e iOS con `vSyncCount = 0` y `targetFrameRate = -1` (por defecto), el contenido se renderiza a 30 fps fijos "to conserve battery power". https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Application-targetFrameRate.html
2. Unity recomienda usar alrededor del 65 % del tiempo de frame disponible en móvil: ~22 ms a 30 fps y ~11 ms a 60 fps. Motivo: "Most mobile devices do not have active cooling". E-book Unity 6, p. 19 (D-01).
3. Apple HIG: "a button needs a hit region of at least 44x44 pt — in visionOS, 60x60 pt". https://developer.apple.com/design/human-interface-guidelines/buttons
4. Apple HIG Accessibility: iOS/iPadOS 44×44 pt por defecto y 28×28 pt mínimo; padding de ~12 pt con bisel y ~24 pt sin bisel. https://developer.apple.com/design/human-interface-guidelines/accessibility
5. Android: touch target "at least 48dp×48dp. Larger is even better." https://developer.android.com/guide/topics/ui/accessibility/apps
6. Apple HIG Designing for games: descarga inicial de 30 minutos o menos; texto en iOS de 17 pt por defecto y 11 pt mínimo; "Teach through play". https://developer.apple.com/design/human-interface-guidelines/designing-for-games
7. Android `getThermalHeadroom` (Android 11 / API 30): predice cuánto tiempo puede sostenerse el rendimiento sin throttling; 0,0 = sin throttling, 1,0 = `THERMAL_STATUS_SEVERE`. https://developer.android.com/games/optimize/adpf/thermal
8. iOS `ProcessInfo.ThermalState`: nominal, fair, serious, critical (iOS 11+). https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum
9. Unity 6.3: Adaptive Performance es "a built-in module". https://docs.unity3d.com/6000.3/Documentation/ScriptReference/UnityEngine.AdaptivePerformanceModule.html. El paquete 6.0 "now contains only samples and visual scripting nodes". https://docs.unity3d.com/Packages/com.unity.adaptiveperformance@6.0/manual/index.html
10. Android LMK: los callbacks de trim están deprecados y "haven't been helpful at preventing low-memory kills", salvo `TRIM_MEMORY_UI_HIDDEN` y `TRIM_MEMORY_BACKGROUND`. https://developer.android.com/topic/performance/issues/lmk
11. Android vitals, umbrales de bad behavior: tasa de crash percibida 1,09 % general y 8 % por modelo de teléfono; ANR 0,47 % general y 8 % por modelo. La memoria (juegos con 4 GB de RAM: 2,25 GB en foreground) puede afectar la visibilidad desde febrero de 2027. https://developer.android.com/topic/performance/vitals
12. Google Play: desde el 31-08-2026, apps nuevas y actualizaciones deben apuntar a Android 16 (API 36); las existentes, a API 35 o superior para seguir visibles a usuarios nuevos. https://developer.android.com/google/play/requirements/target-sdk
13. Android 16 (target 36): en pantallas de sw ≥ 600 dp se ignoran `screenOrientation`, `resizableActivity` y `min/maxAspectRatio`; los juegos están exceptuados según `android:appCategory`. https://developer.android.com/about/versions/16/behavior-changes-16
14. Unity 6.3: Application Category es "Game" por defecto en proyectos nuevos y "exempts applications from Android 16 behavior changes for large screens". https://docs.unity3d.com/6000.3/Documentation/Manual/class-PlayerSettingsAndroid.html
15. Android 15 con target SDK 35: edge-to-edge obligatorio; los modos de cutout se interpretan como `ALWAYS`. https://developer.android.com/develop/ui/views/layout/display-cutout
16. Unity Device Simulator no simula rendimiento, memoria, capacidades de render, plugins nativos, `#define` de plataforma ni giroscopio. https://docs.unity3d.com/6000.3/Documentation/Manual/device-simulator-introduction.html
17. Unity 6.3 soporta Android 7.1 (API 25) o superior; Vulkan y OpenGL ES 3.0+; ASTC por defecto. https://docs.unity3d.com/6000.3/Documentation/Manual/android-requirements-and-compatibility.html
18. Unity 6.3 soporta iOS 15 o superior; Xcode 16 o superior recomendado. https://docs.unity3d.com/6000.3/Documentation/Manual/ios-requirements-and-compatibility.html. "Xcode is available only on macOS devices". https://docs.unity3d.com/6000.3/Documentation/Manual/iphone-BuildProcess.html
19. Google Play requiere AAB. https://docs.unity3d.com/6000.3/Documentation/Manual/android-BuildProcess.html
20. Límites de Google Play (descarga comprimida): módulo base 500 MB; asset pack 1,5 GB; install-time acumulado 4 GB; on-demand/fast-follow 30 GB; total 34 GB. https://support.google.com/googleplay/android-developer/answer/9859372
21. Apple: tamaño máximo sin comprimir de 4 GB (iOS 9+). https://developer.apple.com/help/app-store-connect/reference/app-uploads/maximum-build-file-sizes
22. Input System publicado para Unity 6000.3: versión 1.20.0. https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.inputsystem.html
23. `Input.touches` es legacy: "don't use this API in new projects". https://docs.unity3d.com/6000.3/Documentation/ScriptReference/Input-touches.html
24. Unity IAP (`com.unity.purchasing`) versión 5.4.4 publicada para 6000.3. https://docs.unity3d.com/6000.3/Documentation/Manual/com.unity.purchasing.html
25. Apple 3.1.1: las apps con loot boxes "must disclose the odds of receiving each type of item to customers prior to purchase". https://developer.apple.com/app-store/review/guidelines/
26. Google Play: hay que divulgar las probabilidades de ítems aleatorios "in advance of, and in close and timely proximity to, that purchase". https://support.google.com/googleplay/android-developer/answer/9858738
27. AdMob prohíbe interstitials al cargar o salir de la app, después de cada acción del usuario (máximo uno cada dos acciones), inmediatamente después de otro interstitial, y de forma inesperada durante una tarea. https://support.google.com/admob/answer/6201362
28. Rewarded ads: "served after a user explicitly chooses to view a rewarded ad". https://support.google.com/admob/answer/7372450
29. Unity Ads: desde el 1 de abril de 2026, la integración directa vía Advertisement Legacy "might see reduced ad performance"; se recomienda LevelPlay. https://docs.unity.com/en-us/grow/levelplay/sdk/unity/migrate-from-unity-ads-to-levelplay
30. FTC 2022-12-19: Epic paga USD 275 M (COPPA) + USD 245 M (reembolsos) por dark patterns y facturación. https://www.ftc.gov/news-events/news/press-releases/2022/12/fortnite-video-game-maker-epic-games-pay-more-half-billion-dollars-over-ftc-allegations
31. Zendle & Cairns 2018: n = 7.422; relación entre gasto en loot boxes y severidad de juego problemático (η² = 0,054), mayor que la de otras compras (η² = 0,004). Es correlacional. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0206767
32. Unity Test Framework: para recibir resultados desde el Player, Editor y Player "must be on the same network". https://docs.unity3d.com/6000.3/Documentation/Manual/test-framework/workflow-run-playmode-test-standalone.html
33. Firebase Game Loop: timeout por defecto de 3 minutos; Unity figura entre los motores soportados. https://firebase.google.com/docs/test-lab/android/game-loop
34. WWDC19 418: en el Simulator, los límites de memoria y CPU del dispositivo no se simulan. https://developer.apple.com/videos/play/wwdc2019/418/
35. Android, juegos y energía: igualar la frecuencia de refresco al fps objetivo; "Vulkan is now the primary graphics API on Android and is more efficient than OpenGL ES". https://developer.android.com/games/optimize/power
36. Arm: "Memory bandwidth requires a lot of power... more restricted in mobile devices compared to desktop systems"; "Overdraw causes excess memory bandwidth use". Arm GPU Best Practices 3.4, §2.3, p. 15 (D-02).
37. Android `onPause`: "don't use onPause to save application or user data". https://developer.android.com/guide/components/activities/activity-lifecycle
38. Casos de HUD personalizable: Call of Duty: Mobile (blog de Activision, 2019-10-09: "drag, drop, and change the size and opacity of everything on-screen"; modos Simple y Advanced fire). https://blog.activision.com/call-of-duty/2019-10/Getting-a-Grip-on-the-Call-of-Duty-Mobile-Controls. Fortnite, doc para creadores: convertir elementos del HUD en botones táctiles y reposicionar, re-estilizar u ocultar los controles por defecto. https://dev.epicgames.com/documentation/fortnite/mobile-development-in-fortnite?lang=en-US
39. Alto's Adventure (App Store): "Simple one-finger controls", "one button trick system", premium a US$4,99 sin ads ni IAP (según la ficha consultada). https://apps.apple.com/us/app/altos-adventure/id950812012
40. Pokémon GO, Battery Saver: "disables your display while your device is pointed downward" y sigue registrando la distancia. https://niantic.helpshift.com/hc/en/6-pokemon-go/faq/2472-what-is-the-battery-saver-setting/. Adventure Sync registra la distancia con la app cerrada "without significantly impacting your device's battery life". https://niantic.helpshift.com/hc/en/6-pokemon-go/faq/3265-adventure-sync/
41. Vampire Survivors móvil (Kotaku, Ethan Gach, 2023-01-05, citando a poncle): "monetization is minimal and is designed to never interrupt your game, always be optional". El motivo del lanzamiento móvil fueron los clones. https://kotaku.com/vampire-survivors-free-iphone-steam-mobile-smartphone-1849955308

---

## F) Fuera del alcance (para no convertir la unidad en otro curso)

- **Programación nativa** de Android (Kotlin/Java, Jetpack Compose) o iOS (Swift/UIKit). Se mencionan las APIs (Thermal, lifecycle) para entender la plataforma, no para implementarlas.
- **Implementación completa de ADPF, Adaptive Performance o scalers custom.** Basta con mostrar el concepto y la configuración.
- **Integración real de SDKs de ads (LevelPlay/AdMob) o IAP con cuentas de tienda.** Requiere cuentas de developer pagas: Apple tiene costo anual y Google Play un pago único ([INF]: los montos no se verificaron aquí). Enseñar el diseño del momento del anuncio y de la tienda, no el SDK.
- **Firma, keystore, publicación en tiendas, privacy manifest, export compliance.** Solo mencionarlos.
- **Perfilado de GPU a bajo nivel** (AGI frame profiling, Arm Streamline, Xcode Metal debugger) y **shaders, Vulkan y Metal**. Mención y un ejemplo visual como mucho.
- **Live ops, analítica, economía de juego, UA y marketing (LTV, CPI, retención).** Es otro curso. En esta unidad, la monetización se trata como diseño y ética.
- **Build de iOS** si la cátedra no tiene Mac. Declararlo como limitación ([INF]).
- **Upscaling (FSR, DLSS, STP) y XR**, aunque estén en el e-book.

---

## G) NO VERIFICADO o descartado

1. **Zagal, Björk & Lewis 2013, "Dark Patterns in the Design of Games" (FDG):**
   - La URL fdg2013.org falló por certificado vencido. dblp devolvió un error (protección anti-bot). La API de Semantic Scholar devolvió 429 y la página web 403.
   - La existencia del paper es ampliamente referenciada, pero **ninguna URL se pudo abrir en esta sesión**. Para metadatos: FDG 2013, pp. 39-46, según los resultados del buscador.
   - No citar URL hasta confirmarla.
2. **Parhi et al. 2006: valores "9,2 mm (tareas discretas) / 9,6 mm (seriales)".** Aparecen solo en el resumen del buscador. Los metadatos del paper sí se verificaron (Crossref), el texto no.
3. **Zaman, Natapov & Teather 2010** ("Touchscreens vs. traditional controllers in handheld gaming", Future Play): metadatos verificados vía Crossref (https://api.crossref.org/works/10.1145/1920778.1920804). Los resultados ("150 % más muertes en iPhone", preferencia por el DS) vienen solo del buscador; ACM DL devolvió 403.
4. **Baxter et al. 2023** ("Virtual Joystick Control Sensitivity...", ACM MIG): metadatos verificados vía Crossref. El hallazgo (sensibilidad robusta) solo viene del buscador.
5. **Drummond & Sauer 2018:** metadatos verificados; el texto no (nature.com pide login). No se confirmó si es de acceso abierto.
6. **Belgian Gaming Commission:** la fuente primaria (gamingcommission.be/.../loot-boxes) dio 404 y la home no tiene sección sobre loot boxes. Se usó la fuente secundaria del regulador británico (B-55). Las multas "€800.000 / 5 años de prisión" solo vienen de prensa en el buscador: **no usar**.
7. **Países Bajos:** B-55 dice que EA estaba apelando. [INF] Es posible que la apelación ya se haya resuelto (no verificado). No afirmar el estado actual.
8. **Battle pass:** no se encontró una fuente académica ni oficial verificada. Se agotó el presupuesto de búsquedas de la sesión. Tratarlo solo como ejemplo descriptivo o buscar más adelante.
9. **Material Design 3** (touch target y gestos): m3.material.io se renderiza con JavaScript y no devolvió contenido. Usar la doc de Android (B-21) para 48 dp.
10. **Límite de 200 MB de descarga por red celular en App Store:** solo aparece en el resumen del buscador; la página de "Maximum build file sizes" abierta no lo menciona. No citar.
11. **Snapdragon Profiler (Qualcomm):** la página no devolvió contenido. No citar detalles.
12. **Adaptive Performance en iOS:** no se encontró un provider iOS en la doc de Unity 6.3 abierta (providers: Basic y Android). No afirmar soporte en iOS.
13. **Provider Samsung deprecado:** solo aparece en la descripción de un mirror de GitHub no afiliado a Unity (needle-mirror). No citar como oficial.
14. **Input System 1.20, páginas Touch/OnScreen:** 404 en las rutas probadas (ver B-35).
15. **Genshin Impact** (HUD/multiplataforma), **Clash Royale** (sesiones cortas): sin fuente primaria abierta. La página de GDC 2025 sobre Clash Royale ("Recent Bets & Outcomes...") dio 403. GDC 2017 "Quest for the Healthy Metagame" solo apareció en el buscador. Si se usan, decir que no están verificados.
16. **Vampire Survivors, control con un pulgar y orientación vertical:** solo según el buscador (PC Gamer no devolvió el cuerpo; Kotaku no lo menciona). La ficha de Google Play no devolvió contenido.
17. **Fortnite, HUD Layout Tool (soporte de Epic):** la página de ayuda dio 403. Se usó la doc para creadores (dato 38), que es otra cosa: dispositivos HUD en islas de UEFN.
18. **Internet Archive (charla de Monument Valley, GDCEU2014Wong):** no se abrió.
19. **Charla Arm GDC 2026 (C-11):** el acceso libre es incierto (regla del 30 %).
20. **Duraciones de video:** ninguna verificada (oEmbed no las da).

---

## Tabla final de fuentes (sección 21 del encargo)

Clasificación: **PRIMARIA** (documentación oficial de plataforma, motor, tienda o regulador) · **ACADÉMICA** (revisada por pares) · **PROFESIONAL** (GDC, industria, prensa especializada) · **COMPLEMENTARIA** (útil, con menor autoridad o vigencia).

| Recurso | Tipo | Unidad | Tema | Autoridad | Nivel | Uso |
|---|---|---|---|---|---|---|
| Unity 6.3: targetFrameRate, Screen.safeArea, Device Simulator, Player Settings Android, Run tests in a Player, Profiling on target (B-01, B-02, B-04, B-25, B-30, B-31) | Doc. oficial | 4 | Rendimiento, pantalla, testing | PRIMARIA | Intro–Interm. | Obligatorio |
| Unity 6.3: Adaptive Performance (B-05, B-06) | Doc. oficial | 4 | Térmica | PRIMARIA | Interm. | Complementario |
| Unity uGUI Canvas Scaler (B-32) / UI Toolkit Panel Settings (B-33) | Doc. oficial | 4 | Escalado de UI | PRIMARIA | Intro | Obligatorio / Complementario |
| Unity Input System: Touch y On-Screen (B-35; ref. 1.17, versión vigente 1.20) | Doc. oficial | 4 | Input táctil | PRIMARIA | Interm. | Obligatorio (verificar páginas 1.20) |
| Android: ADPF, Thermal API, Power, LMK, vitals, lifecycle, cutouts, Android 16, target API (B-08, B-09, B-59, B-11, B-12, B-38, B-23, B-24, B-26) | Doc. oficial | 4 | Hardware, ciclo de vida, compatibilidad | PRIMARIA | Interm. | Obligatorio (selección) |
| Apple HIG: Buttons, Accessibility, Layout, Gestures, Designing for games, Haptics (B-15–B-20) | Guía oficial | 4 | UX táctil | PRIMARIA | Intro | Obligatorio |
| Apple: Metal TBDR, thermalState, memory warning, app life cycle (B-14, B-10, B-13, B-38) | Doc. oficial | 4 | Hardware, ciclo de vida | PRIMARIA | Interm. | Complementario |
| Apple App Review Guidelines 3.1.1 / 1.3 (B-46) | Política oficial | 4 | IAP, loot boxes, niños | PRIMARIA | Intro | Obligatorio |
| Google Play Payments / Families (B-47, B-48); AdMob interstitial y rewarded (B-49) | Política oficial | 4 | Monetización | PRIMARIA | Intro | Obligatorio |
| Unity LevelPlay, migración desde Unity Ads (B-50) | Doc. oficial | 4 | Ads | PRIMARIA | Interm. | Complementario |
| Firebase Test Lab Game Loop (B-39) / AWS Device Farm (B-40) / Android Emulator (B-41) | Doc. oficial | 4 | Testing | PRIMARIA | Interm. | Complementario |
| Unity e-book "Optimize your game performance for mobile, XR, and the web (Unity 6)" (D-01) | PDF oficial | 4 (y 7) | Rendimiento | PRIMARIA | Interm. | Lectura guiada pp. 11, 18–20, 42, 60, 63, 69 |
| Arm GPU Best Practices 3.4, §2.3 (D-02) | PDF oficial de fabricante | 4 | Ancho de banda, overdraw | PRIMARIA | Interm.–Avanz. | 1 página obligatoria |
| FTC vs. Epic Games 2022 (B-54) | Comunicado de regulador | 4 | Dark patterns | PRIMARIA | Intro | Obligatorio (caso) |
| UK Gambling Commission, enfoques internacionales sobre loot boxes (B-55) | Documento de regulador | 4 | Regulación | PRIMARIA (secundaria respecto de Bélgica) | Intro | Complementario |
| Zendle & Cairns 2018, PLOS ONE (B-51) | Paper | 4 | Loot boxes | ACADÉMICA | Avanz. | Lectura breve |
| Petrovskaya & Zendle 2022, J. Business Ethics (B-52) | Paper | 4 | Monetización predatoria | ACADÉMICA | Avanz. | Complementario |
| Drummond & Sauer 2018, Nature Human Behaviour (B-53) | Paper | 4 | Loot boxes | ACADÉMICA | Avanz. | Complementario |
| Parhi, Karlson & Bederson 2006, MobileHCI (B-57) | Paper | 4 | Tamaño de objetivo con el pulgar | ACADÉMICA | Avanz. | Complementario (resultado no verificado en el texto) |
| Zagal, Björk & Lewis 2013, FDG | Paper | 4 | Dark patterns | ACADÉMICA | Avanz. | **Pendiente de URL verificada** |
| Hoober 2013, UXmatters (B-56) | Artículo | 4 | Agarre del teléfono | PROFESIONAL | Intro | Complementario, con advertencia de antigüedad |
| Game Accessibility Guidelines (B-58) | Guía de industria | 4–7 | Accesibilidad | PROFESIONAL | Intro | Obligatorio |
| GDC: Zach Gage 2012 (C-04), Ken Wong 2014 (C-05), Dark Patterns 2017 (C-06), Jim Brown 2018 (C-02), Gacha 2019 (C-03) | Charlas | 4 | UX táctil, monetización | PROFESIONAL | Intro–Interm. | Fragmentos en clase |
| WWDC19 422 / 606 / 418 (C-07–C-09) | Charlas oficiales | 4 | Térmica, Metal, Simulator | PRIMARIA | Interm. | 422: fragmento obligatorio |
| Unity, "Input System Mobile controls" (C-01) | Video oficial | 4 | On-Screen Controls | PRIMARIA | Interm. | Obligatorio |
| Activision (CoD Mobile), Epic (Fortnite creators), App Store (Alto's), Niantic (Pokémon GO), Kotaku (Vampire Survivors) — datos E-38 a E-41 | Blogs y fichas | 4 | Casos reales | PROFESIONAL / COMPLEMENTARIA | Intro | Ejemplos |
| Video "Adaptive Performance" de Unity Middle East 2021 (C-12) | Video | 4 | Térmica | COMPLEMENTARIA (**desactualizado**) | — | No usar como referencia de 6.3 |

---

## Recursos agregados en la versión 2 de la Clase 1 (2026-10-05)

**B-62**
- **Título:** What Are the Best Platforms for Games?
- **Autor:** Kevuru Games (estudio de desarrollo y outsourcing; Varsovia y EE. UU.) · **Tipo:** artículo de blog **comercial** · **Fecha:** sin fecha visible; menciona cifras "2023–2027"
- **URL:** https://kevurugames.com/blog/what-are-the-best-platforms-for-games/
- **Verificación:** descargado y leído completo el 2026-10-05. WebFetch dio 403; se descargó con un navegador estándar.
- **Tema / concepto:** definición de plataforma ("la base de cómo los jugadores se conectan con los juegos"); historia desde los arcades; las tiendas móviles abrieron la distribución a estudios chicos; cuatro criterios para elegir plataforma (audiencia, monetización, integración y soporte, vigencia).
- **Nivel:** introductorio · **Confiabilidad:** **baja–media**. Sirve para los conceptos, no para los datos.
- **Problemas detectados:**
  - presenta Google Stadia como activa (cerró el 18/01/2023);
  - nombra "Origin" (EA la reemplazó por la EA app, anuncio del 06/10/2022);
  - da cifras de mercado sin fuente;
  - mezcla bajo "plataforma" hardware, tiendas, cloud y sitios de streaming;
  - termina ofreciendo los servicios del estudio.
- **Uso en clase:** Clase 1 v2, slides 5, 6, 7 y 18 (conceptos) y slide 19 (ejercicio de lectura crítica). **Complementario.**
- **Clasificación (tabla final):** FUENTE COMPLEMENTARIA (profesional / comercial).

**B-63**
- **Título:** The all new EA app for Windows — EA's new optimized PC platform has officially arrived!
- **Autor:** Electronic Arts · **Tipo:** comunicado oficial · **Fecha:** 06/10/2022
- **URL:** https://www.ea.com/news/ea-app
- **Verificación:** fetch OK 2026-10-05. Cita: "The EA app has officially left its open beta phase and will soon replace Origin as our primary PC platform."
- **Uso:** respaldar la corrección sobre "Origin" en la slide 19 · **Complementario** · FUENTE PRIMARIA.
- **No verificado:** la fecha de cierre definitivo de Origin (abril de 2025) aparece solo en foros de EA, no en una página oficial abierta. No se cita.

El cierre de Google Stadia (anuncio 29/09/2022, efectivo 18/01/2023) se respalda con la ficha del blog oficial de Google de la investigación de la Unidad VII (`../unidad-07/00-investigacion-preliminar.md`).

**B-64**
- **Título:** A Brief History of the ESRB
- **Autor:** Game Developer (publicación profesional) · **Tipo:** artículo
- **URL:** https://www.gamedeveloper.com/business/a-brief-history-of-the-esrb
- **Verificación:** localizado por búsqueda web el 2026-10-05; el dato coincide con la entrada de la ESRB en Wikipedia. Página no abierta con fetch: re-verificar antes de citarla textualmente.
- **Dato:** la ESRB se creó en 1994, tras las audiencias del Congreso de EE. UU. de diciembre de 1993 sobre violencia en videojuegos, en las que se mostraron Mortal Kombat y Night Trap.
- **Uso:** notas de la slide 7 de la Clase 1 v2 (clásicos del arcade) y puente con la Unidad V (clasificación por edades) · **Complementario** · FUENTE PROFESIONAL.

**Fechas de los hitos de las slides 6 y 7 (Clase 1 v2):**
- **Verificadas el 2026-10-05:** App Store, 10/07/2008 (Apple Newsroom); Oculus Rift, 28/03/2016; GeForce Now, 04/02/2020 (TechCrunch, CNN).
- **Tomadas del artículo de Kevuru y ampliamente documentadas, sin re-verificar una por una:** Pong 1972, Space Invaders 1978, Pac-Man 1980, Donkey Kong 1981, Galaga 1981, Street Fighter II 1991, Mortal Kombat 1992, Atari 2600 1977, IBM PC 1981, Game Boy 1989.

