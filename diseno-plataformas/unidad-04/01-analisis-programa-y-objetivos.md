# Unidad 4 — Análisis del programa, auditoría y objetivos

Fases cubiertas: **1** (auditoría de contenido), **3** (correcciones y contenidos faltantes) y **4** (objetivos pedagógicos).
Fecha de la auditoría: 2026-10-04/05. Toda fuente citada se verificó ese día; la evidencia completa con URL está en [`06-investigacion-recursos.md`](./06-investigacion-recursos.md). Los códigos **B-xx** remiten a sus fichas.

---

## A. Cita textual del programa (Plan 2020, planificación 2025)

> **UNIDAD N° 4: Diseño según Plataforma Móvil**
> Entorno de Dispositivos Móviles: Características de hardware y software. Diferencias con otras plataformas (PC, consolas).
> Limitaciones Técnicas: Restricciones de memoria. Procesador y rendimiento gráfico. Consumo de batería.
> Diseño de Interfaz y Experiencia de Usuario: Optimización de interfaces táctiles. Uso de gestos y patrones de interacción móvil. Buenas prácticas de diseño centrado en el jugador.
> Estrategias de Monetización en Juegos Móviles: Publicidad integrada (ads). Compras dentro de la aplicación (IAP). Modelos freemium e híbridos.
> Testing y Portabilidad Multiplataforma: Pruebas en diferentes resoluciones. Adaptación a múltiples sistemas operativos (Android, iOS). Herramientas y frameworks de testing móvil.

Fuente: `diseno-plataformas/programa/Diseño segun plataformas de juego Plan 2020 - Año 2025 - - Elsa Daniela Ramirez .docx`.

### A.1 Ubicación en el cronograma del programa

| Semana | Actividad según el programa | Observación |
|---|---|---|
| 7 | Socialización de contenidos U4 + **TP N° 3** ("Toda la unidad 04") | La teoría de la unidad entera está concentrada en una sola semana |
| 8 | Continuación del TP 3 | Semana de taller |
| 9 | **Parcial** (Unidades 1, 2, 3 y 4) | La U4 se evalúa casi sin tiempo de maduración |

### A.2 Inconsistencias del propio programa que afectan a la U4

1. **La tabla "UT / TP / Tema" está corrida una unidad.** Asigna "U04 / TP N° 3" a *Pruebas Unitarias con Unity* y "U05 / TP N° 4" a *Diseño según Plataforma Móvil*. El cronograma, en cambio, dice que el TP N° 3 es "Toda la unidad 04" (Móvil). **Decisión de este documento:** seguir el cronograma, donde **TP N° 3 = Unidad 4 Móvil**, porque es la sección operativa. Conviene que la titular corrija la tabla.
2. **La tabla de RA repite "Unidad II" dos veces** en RA01 y RA02, y omite la Unidad III. No afecta a la U4, pero conviene corregirlo.
3. **Bibliografía obligatoria.** De los 10 títulos, solo *The Art of Game Design* (Schell, CRC, 3.ª ed.) se confirmó tal cual. El que el programa cita como "Designing for Mobile Games — Steven L. Kent — CRC 2022", único título específico de móvil, **no apareció en los catálogos consultados**. Detalle y reemplazos verificados en [`../transversal/auditoria-bibliografia-y-fuentes-academicas.md`](../transversal/auditoria-bibliografia-y-fuentes-academicas.md). No se afirma que el libro no exista: se informa que no se encontró evidencia.

### A.3 Material previo de la cátedra

- **Clase del 28/09/2026, "Introducción a las plataformas (panorama U-IV a U-VII)"** (`diseno-plataformas/clases/2026-09-28-integracion-y-plataformas/Clase2-Plataformas.pptx`, 18 slides). Ya presentó:
  - slide 8 (móvil): táctil sin respuesta física, zonas seguras, batería y temperatura, interrupciones, sesiones cortas "como tendencia, no regla" y HUD reubicable;
  - slides 12 y 14–16: el juego **nave + asteroides** como juego base para adaptar y la idea de separar la *intención* del jugador del *dispositivo*;
  - un ejercicio de **criterios de prueba medibles**.

  Esta unidad **profundiza** ese panorama y no lo repite. Se reciclan los ejemplos y se marcan **[RECICLADO 28/09]** en las diapositivas.
- No se encontró material de años anteriores específico de la U4: no hay `.pptx` ni `.pdf` de "Unidad 4" en el repositorio.

---

## B. Auditoría del contenido (Fase 1)

Clasificación pedida: CORRECTO / CORRECTO PERO INCOMPLETO / REQUIERE PRECISIÓN / DESACTUALIZADO / CONFUSO / FALTA DESARROLLAR / FALTA UN TEMA IMPORTANTE.

| # | Qué dice el programa | Clasificación | Problema | Qué debería enseñarse | Por qué importa | Fuente |
|---|---|---|---|---|---|---|
| 1 | "Características de hardware y software" | CORRECTO PERO INCOMPLETO | Así redactado invita a una lista de especificaciones (GB, GHz) | SoC con CPU heterogénea; **GPU por tiles (TBDR)**; ancho de banda de memoria compartido; sin refrigeración activa; un sistema operativo que mata procesos | Explica por qué overdraw, transparencias y resolución nativa cuestan más en un teléfono | B-08, B-14, PDF Arm §2.3 |
| 2 | "Diferencias con otras plataformas (PC, consolas)" | CORRECTO PERO INCOMPLETO | Se reduce a "el celular es menos potente" | Ejes de comparación: rendimiento **sostenido vs. pico**, fragmentación, reglas de tienda obligatorias, input sin feedback físico, interrupciones | Es la base comparativa que se reutiliza en U5–U7 | e-book Unity 6 pp. 19–20 |
| 3 | "Restricciones de memoria" | REQUIERE PRECISIÓN | "Poca RAM" no describe el problema real | Android *Low Memory Killer* e iOS terminan el proceso; presupuesto de memoria; ASTC; guardar estado. **Corrección:** los callbacks `onTrimMemory` están deprecados salvo `UI_HIDDEN` y `BACKGROUND`, y "no han ayudado a prevenir" los cierres | Un juego que "se cierra solo" al volver de otra app es un defecto de diseño de plataforma | B-11, B-12, B-13 |
| 4 | "Procesador y rendimiento gráfico" | REQUIERE PRECISIÓN | No menciona temperatura ni *throttling*, que es el concepto central de móvil | Ciclo calor → throttling → caída de fps; usar ~**65 %** del presupuesto de frame; Thermal API (Android) / `thermalState` (iOS); Adaptive Performance como **módulo integrado** en Unity 6.3 | Un juego que corre a 60 fps en el minuto 1 y a 35 en el minuto 10 tiene un problema de diseño, no solo de código | B-05, B-08–B-10, e-book p. 19 |
| 5 | "Consumo de batería" | CORRECTO PERO INCOMPLETO | No vincula la batería con decisiones de diseño | fps objetivo (Unity usa **30 fps por defecto** en móvil); frame pacing; Vulkan; respuesta térmica; reposo cuando no hay input | La batería es parte de la experiencia del jugador | B-01, B-59 |
| 6 | (ausente) térmica y rendimiento sostenido | FALTA UN TEMA IMPORTANTE | No aparece en el programa | Integrarlo en los ítems 4–5 sin crear un tema nuevo | Sin esto, el alumno mide fps en el minuto 1 y declara "funciona" | WWDC19-422, B-09 |
| 7 | "Optimización de interfaces táctiles" | CORRECTO PERO INCOMPLETO | "Optimización" es ambiguo (¿rendimiento de UI o usabilidad?) | Mínimos normativos: **44×44 pt** (Apple) y **48×48 dp** (Android); safe area y cutouts; escalado de UI (Canvas Scaler); oclusión por los dedos | Son números verificables que convierten "buena UI" en criterio de prueba | B-15, B-16, B-21, B-02, B-32 |
| 8 | "Uso de gestos y patrones de interacción" | CORRECTO (requiere precisión en dos puntos) | — | No redefinir gestos del sistema; un gesto custom **nunca** es la única forma de hacer algo importante; joystick virtual vs. toque directo; háptica opcional y "menos es más" | Evita controles indescubribles o inaccesibles | B-18, B-20, B-22 |
| 9 | "Buenas prácticas de diseño centrado en el jugador" | CONFUSO | Es genérico: vale para cualquier plataforma | Lo específico de móvil: jugar apenas se instala, descarga inicial corta, enseñar jugando, permisos en contexto, texto mínimo, accesibilidad, pausa automática | Sin bajarlo a lo concreto no se puede evaluar | B-19, B-58 |
| 10 | "Publicidad integrada (ads)" | CORRECTO PERO INCOMPLETO | Falta el marco de políticas, que también es diseño | Rewarded (opt-in) vs. interstitial (solo en transiciones naturales) vs. banner; **lo que AdMob prohíbe**; Families/Kids; Unity Ads → LevelPlay (desde abr-2026) | El momento del anuncio es una decisión de diseño con reglas externas | B-49, B-48, B-46, B-50 |
| 11 | "Compras dentro de la aplicación (IAP)" | REQUIERE PRECISIÓN | IAP no es una "estrategia" libre: la tienda la impone | Apple 3.1.1 (IAP obligatorio para contenido digital; probabilidades de loot boxes); Google Play Billing; divulgación de probabilidades | El diseño de la tienda interna está condicionado por reglas externas | B-46, B-47 |
| 12 | "Modelos freemium e híbridos" | CORRECTO PERO INCOMPLETO + FALTA UN TEMA IMPORTANTE | Omite el modelo **premium** y la mirada **ética y regulatoria** | Premium (Alto's Adventure); freemium; híbrido. Ética: dark patterns, loot boxes (evidencia **correlacional**), FTC vs. Epic 2022 (USD 520 M), prohibición en Bélgica | La monetización modifica dificultad, progresión y ritmo: es game design | B-51–B-55, dato E-39 |
| 13 | (ausente) ciclo de vida e interrupciones | FALTA UN TEMA IMPORTANTE | No figura | `OnApplicationPause` / `OnApplicationFocus`; el SO mata procesos en background; pausa automática y guardado | Llamadas y notificaciones son la situación **normal** de uso | B-37, B-38 |
| 14 | "Pruebas en diferentes resoluciones" | CORRECTO PERO INCOMPLETO | La resolución sola no alcanza | Aspect ratio, densidad (dp/pt), safe area, orientación, tablets y plegables. Android 16 ignora restricciones de orientación en pantallas grandes, **salvo juegos** (Application Category = Game, por defecto en Unity 6.3) | Es la fuente más común de bugs visuales en móvil | B-04, B-24, B-25 |
| 15 | "Adaptación a múltiples SO (Android, iOS)" | REQUIERE PRECISIÓN | "Adaptación" esconde toolchains y reglas distintas | Android: AAB, **target API 36** desde el 31-08-2026. iOS: Xcode, que **solo corre en macOS** | Condiciona qué se puede practicar en la UNJu: Android en la práctica, iOS en forma conceptual (ver H) | B-26–B-29 |
| 16 | "Herramientas y frameworks de testing móvil" | CORRECTO PERO INCOMPLETO / REQUIERE PRECISIÓN | Mezcla en una línea cosas de naturaleza distinta | Taxonomía de 6 niveles: Device Simulator (solo layout) → emulador/simulador → dispositivo real + profiler → Unity Test Framework en el Player → granjas en la nube (Firebase Game Loop, AWS Device Farm) → Android vitals post-lanzamiento | Cada herramienta prueba algo distinto y **no prueba** otras cosas | B-04, B-30, B-31, B-39–B-42, B-12 |
| 17 | (ausente) tamaño de descarga y entrega de assets | FALTA DESARROLLAR | — | Límites de Google Play (base de 500 MB, Play Asset Delivery) y App Store; qué entra en la primera sesión | Define el onboarding y la primera impresión | B-43–B-45 |

---

## C. Qué NO debería enseñarse tal como está escrito (U4)

| Afirmación riesgosa | Por qué induce a error | Versión correcta |
|---|---|---|
| "El celular es una PC más chica" | Ignora térmica, TBDR, cierre de procesos e interrupciones | "Es una plataforma con **energía, calor e interrupciones** como restricciones de diseño" |
| "Si corre a 60 fps en mi teléfono, está optimizado" | Mide el pico, no el rendimiento sostenido, en un solo dispositivo | "Rendimiento **sostenido** durante N minutos, en un dispositivo de gama mínima" |
| "Con `onTrimMemory` evitamos que el SO cierre el juego" | Android lo declara deprecado e ineficaz (salvo dos niveles) | "El juego **puede** morir en background: hay que guardar estado" |
| "El Device Simulator de Unity sirve para testear en móvil" | Simula layout, safe area y rotación; **no** rendimiento, memoria ni render | "Sirve para el layout; el rendimiento se mide en un dispositivo real" |
| "Freemium y ads son estrategias para elegir" | Ignora reglas de tienda, políticas de ads y ética | "Son modelos regulados que **cambian el diseño** del juego" |
| "Las loot boxes causan ludopatía" | La evidencia citable es **correlacional** | "Se asocian con juego problemático (correlación); varios países las regulan" |
| "Los juegos móviles son de sesiones cortas" | Es práctica profesional, no norma verificada | "Las sesiones *suelen* ser cortas: diseñar para poder interrumpir" (así lo dijo la clase del 28/09) |
| "Adaptive Performance solo funciona en Samsung" | Desactualizado (video y blog de 2021) | "En Unity 6.3 es un módulo integrado con provider Basic y provider Android" |
| "Hay que usar `Input.touches`" | La API legacy está desaconsejada para proyectos nuevos | "Input System (EnhancedTouch, On-Screen Controls)" |

## D. Qué falta incorporar (U4)

1. Térmica y rendimiento sostenido (integrado en "Limitaciones").
2. Ciclo de vida e interrupciones del SO.
3. Safe area, cutouts, densidad, orientación y pantallas grandes.
4. Accesibilidad móvil concreta: tamaños mínimos, alternativas a gestos, háptica opcional.
5. Modelo premium y mirada ética y regulatoria de la monetización.
6. Taxonomía de herramientas de testing móvil y sus límites.
7. Tamaño de descarga y primera sesión.
8. Requisitos de tienda que cambian todos los años (target API, AAB): la plataforma es un blanco móvil.

---

## E. Correcciones: conservar / modificar / ampliar / incorporar (Fase 3)

| Acción | Tema |
|---|---|
| **Conservar** | Los 5 bloques del programa, en el mismo orden temático. Gestos y patrones de interacción (ítem 8). |
| **Modificar** | "Buenas prácticas centradas en el jugador" → "Decisiones de UX específicas de móvil" (ítem 9). "Estrategias de monetización" → "Monetización como decisión de diseño (y sus reglas)". "Herramientas de testing" → "Qué prueba cada herramienta y qué no". |
| **Ampliar** | Limitaciones (térmica, ciclo de vida, cierre de procesos); resoluciones (aspect, densidad, safe area); SO (toolchains y reglas de tienda); monetización (premium, ética, regulación). |
| **Incorporar** | Interrupciones y ciclo de vida; tamaño de descarga; accesibilidad móvil con números. |
| **Reducir** | Detalle de hardware (sin arquitectura de CPU/GPU más allá de TBDR y térmica); implementación de SDKs de ads e IAP (solo diseño, sin integración). |

Nada del programa se elimina. Lo que se reduce es la **profundidad técnica**, no el tema.

---

## F. Objetivos (Fase 4)

### F.1 Objetivo general

Que el estudiante pueda **tomar y justificar decisiones de diseño, UX, monetización y testing al llevar un videojuego a dispositivos móviles**, entendiendo que energía, calor, memoria, pantalla táctil, interrupciones y reglas de tienda son restricciones de diseño y no solo de programación.

### F.2 Objetivos específicos (al finalizar la unidad el estudiante podrá…)

| Verbo | Objetivo | Nivel (ver 05) |
|---|---|---|
| Comprender | Explicar por qué el rendimiento **sostenido**, la memoria y la batería condicionan el diseño de un juego móvil | N1 |
| Analizar | Identificar en un juego existente (Asteroides) los supuestos de PC que fallan en móvil: input, límites, UI, pausa | N2–N3 |
| Comparar | Contrastar esquemas de control táctil, y modelos premium, freemium y con ads, según criterios explícitos | N3 |
| Diseñar | Proponer la adaptación táctil de un juego: controles, HUD, safe area, orientación, accesibilidad | N4 |
| Implementar conceptualmente | Describir, con referencias al código real, qué clases cambian y cuáles no (separar intención de dispositivo) | N4 |
| Probar | Elegir para cada riesgo el tipo de prueba adecuado (unitaria, integración, automatizada, rendimiento, compatibilidad, usabilidad, QA manual, playtesting) y decir **qué no demuestra** | N3–N5 |
| Justificar | Defender una decisión de monetización o de rendimiento con fuentes y con su costo para la experiencia del jugador | N5 |

### F.3 Vínculo con RA y CE del programa

- **RA01** (analiza y compara plataformas): objetivos "comprender", "analizar" y "comparar".
- **RA02** (diseña y adapta mecánicas e interfaces): "diseñar" e "implementar conceptualmente".
- **RA03** (evalúa jugabilidad y UX aplicando testing y optimización): "probar" y "justificar".
- CE01, CE04, CE05, CE07 y CE09, más CGT03–CGT05 y CGA04. Vinculación **inferida**: el programa lista todas las unidades en todos los RA sin detallarlos.

---

## G. Conceptos esenciales (para no sobrecargar)

**IMPRESCINDIBLES** (se evalúan en el parcial y en el TP 3)
1. Rendimiento sostenido vs. pico; térmica y throttling; 30 fps por defecto y presupuesto de frame.
2. El SO controla el ciclo de vida: interrupciones, pausa, cierre de procesos en background, guardado.
3. UI táctil: tamaños mínimos (44 pt / 48 dp), safe area, escalado por resolución y aspect ratio, oclusión por los dedos.
4. Separar intención del jugador del dispositivo de entrada (continuidad con la clase del 28/09).
5. Monetización como decisión de diseño: premium / freemium / ads / híbrido, con reglas de tienda y ética.
6. Qué prueba cada herramienta y qué no: simulador, emulador, dispositivo real, profiler, tests en el Player.

**IMPORTANTES** (se trabajan en clase, con evaluación formativa)
7. Memoria: presupuesto, compresión de texturas, LMK y jetsam a nivel conceptual.
8. Gestos: estándar vs. custom; háptica.
9. Orientación, tablets y plegables (Android 16 y la excepción para juegos).
10. Fragmentación: probar en gama mínima y máxima.
11. Políticas de ads: interstitials prohibidos, rewarded opt-in.

**COMPLEMENTARIOS** (lectura o mención)
12. TBDR y ancho de banda (para entender el overdraw).
13. Adaptive Performance, ADPF y Thermal API.
14. Tamaño de descarga y Play Asset Delivery.
15. Granjas de dispositivos (Firebase Game Loop, AWS Device Farm) y Android vitals.
16. Regulación de loot boxes por país.

---

## H. Hasta dónde llega la unidad (no sobrecargar)

Cada tema técnico responde a: **¿por qué le importa esto a un diseñador o desarrollador de videojuegos?** Queda **fuera**:
- programación nativa (Kotlin, Swift) e implementación de ADPF o Adaptive Performance;
- integración real de SDKs de ads o IAP: requiere cuentas de desarrollador pagas;
- firma, publicación y compliance de tienda: solo se mencionan;
- perfilado de GPU a bajo nivel, shaders, Vulkan y Metal;
- live ops, analítica, UA y economía de juego en profundidad.

**Condiciones prácticas confirmadas (2026-10-05, decisiones D4-02 y D4-03):**
- **iOS es conceptual.** La cátedra no tiene Mac por ahora y compilar para iOS exige macOS y Xcode (B-28). Se enseñan las diferencias de plataforma (HIG, `thermalState`, ciclo de vida, App Review), pero no hay build, Simulator ni Xcode. Esto se dice explícitamente en clase como límite del curso, no se esconde.
- **Android es práctico y obligatorio.** Los estudiantes tienen teléfono Android, así que la build en dispositivo, el Profiler conectado y el QA manual de interrupciones pasan a ser parte **obligatoria** de la unidad (Clase 4 y TP 3). Como efecto lateral, el parque de teléfonos del curso se usa como matriz de compatibilidad real y se discute su representatividad: no es una muestra del mercado.
