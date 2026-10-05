# Unidad 4 — Actividades prácticas y evaluación

Fases cubiertas: **5** (actividades y evaluaciones) y **6** (capítulo móvil del proyecto integrador).
Niveles: **N1** Comprensión · **N2** Aplicación · **N3** Análisis · **N4** Diseño · **N5** Evaluación.
Regla de diseño de todas las actividades: el alumno **decide y justifica**. No hay consignas del tipo "investigar qué es…".

---

## Mapa de actividades

| ID | Actividad | Tipo | Nivel | Clase | Modalidad | Tiempo |
|---|---|---|---|---|---|---|
| A4.1 | Diagnóstico de síntomas: ¿qué restricción de plataforma explica cada bug? | Caso de testing | N1–N2 | 1 | Parejas | 15 min |
| A4.2 | ¿Qué supuestos de PC tiene Asteroides? | Caso de portabilidad | N2–N3 | 1 | Grupos de 3–4 | 25 min |
| A4.3 | Dos esquemas de control táctil para Asteroides | Caso de diseño / comparativo | N3–N4 | 2 | Grupos | 30 min |
| A4.4 | "La llamada que mata la nave" (defecto deliberado + test + regresión + QA manual en el teléfono) | Caso de testing en Unity y en dispositivo | N2–N4 | 3 (tests) y 4 (teléfono) | Grupos | 25 + 40 min + TP |
| A4.5 | Tres propuestas de monetización: ¿cuál publicarías? | Caso de evaluación ética y de diseño | N3–N5 | 3 | Grupos + debate | 25 min |
| A4.6 | "El juego anda bien… los primeros 5 minutos" | Caso de optimización | N3 | 2 | Individual | 15 min |
| TP 3 | Dossier de plataforma: Asteroides móvil (capítulo 1 del integrador) | Integradora | N4–N5 | 1→4 (se avanza en cada clase; defensa al final de la Clase 4) | Grupos | 2 semanas |

---

## A4.1 — Diagnóstico de síntomas (formativa)

**Consigna.** Para cada reporte, indicar: (a) la restricción de plataforma más probable; (b) qué evidencia pedirías al tester; (c) qué tipo de prueba lo detectaría antes.

1. "El juego se cerró solo cuando volví de responder un WhatsApp."
2. "Al principio iba fluido, a los 10 minutos empezó a trabarse y el teléfono quemaba."
3. "El botón de pausa queda debajo de la cámara frontal en mi Samsung."
4. "En la tablet el texto del score es diminuto."
5. "Me quedé sin batería en media hora."
6. "En el emulador anda perfecto, pero en mi teléfono de gama baja no."

**Respuesta esperada (docente):**

| # | Restricción | Evidencia | Prueba |
|---|---|---|---|
| 1 | Ciclo de vida / LMK: el proceso murió en background | Modelo, RAM, versión de SO, si hubo cambio de app | QA manual en dispositivo (opciones de desarrollador); Play Mode para la lógica de guardado |
| 2 | Térmica: throttling | fps en el tiempo y estado térmico | Rendimiento sostenido en dispositivo real |
| 3 | Safe area / cutout | Captura y modelo | Device Simulator + dispositivo |
| 4 | Escalado de UI (Constant Pixel Size) | Resolución y densidad | Device Simulator con varios perfiles |
| 5 | fps / energía | Duración, fps, brillo | Medición en dispositivo; revisar fps objetivo |
| 6 | El emulador no representa rendimiento ni GPU | Modelo y GPU | Profiler en dispositivo de gama mínima |

**Errores frecuentes:** atribuir todo a "el teléfono es lento"; proponer un unit test para 2, 3 o 5; olvidar pedir el modelo del dispositivo.

---

## A4.2 — ¿Qué supuestos de PC tiene Asteroides? (práctica, Clase 1)

**Consigna.** Con el proyecto abierto (o con los fragmentos impresos de `Ship.cs`, `Game.cs`, `Spawner.cs` y la configuración del Canvas y la cámara), listar al menos **5 supuestos** que dejan de valer en un teléfono. Para cada uno: dónde está (archivo:línea), qué pasaría en móvil y a qué eje pertenece (input, pantalla, UI, ciclo de vida, rendimiento).
**Objetivo:** leer código con mirada de plataforma.
**Entregable:** tabla de 5 filas o más.
**Respuesta esperada:** la tabla S1–S13 de [`02-caso-practico-asteroides-movil.md`](./02-caso-practico-asteroides-movil.md). Con S1, S3/S4/S5, S6 y S8 alcanza para aprobar. S5 (asteroides fuera de pantalla en vertical) es el hallazgo "difícil" que distingue un análisis profundo.
**Errores frecuentes:** quedarse solo con el input (S1); decir "hay que poner botones" sin ubicarlos ni dimensionarlos; no conectar la cámara (S4) con el spawner (S5).

---

## A4.3 — Dos esquemas de control táctil (práctica, Clase 2)

**Consigna.** Diseñar **dos** esquemas de control distintos para Asteroides en móvil, por ejemplo: (A) joystick virtual + botón de disparo; (B) arrastrar el dedo + autodisparo. Para cada uno:
- boceto del HUD sobre una pantalla de teléfono, con la **safe area** marcada;
- tamaños de los controles en pt/dp;
- orientación elegida, con justificación;
- comparación con 5 criterios: oclusión por los dedos, precisión, juego a una mano, accesibilidad (¿hay alternativa al gesto?), descubribilidad.

Elegir uno y justificar con fuentes (HIG Designing for games, 48 dp de Android, Game Accessibility Guidelines).
**Entregable:** una página con los dos bocetos, la tabla comparativa y la decisión.
**Respuesta esperada:** no hay una única respuesta. Una buena respuesta:
- elige vertical u horizontal **sabiendo** el efecto sobre S4/S5;
- respeta 44 pt / 48 dp;
- no pone controles bajo el notch;
- reconoce que el autodisparo cambia el game design (baja la habilidad requerida y cambia el balance);
- ofrece una alternativa accesible.

**Errores frecuentes:** copiar el layout de un shooter complejo; olvidar que el pulgar tapa la zona por donde caen los asteroides; botones de 30 px "porque se ven bien en el editor".

---

## A4.4 — "La llamada que mata la nave" (práctica en Unity, Clase 3 + TP 3)

**Consigna** (escenario completo en [`02` §3](./02-caso-practico-asteroides-movil.md)):
1. Escribir el comportamiento esperado ante una interrupción, como criterio verificable.
2. Implementar la separación regla / adaptador.
3. Test de Edit Mode sobre la regla.
4. Test de Play Mode sobre el adaptador (`Time.timeScale`, nave sin daño).
5. Correr contra la versión con defecto que entrega el docente: rojo → corregir → verde → queda como regresión.
6. Completar la tabla **"qué no demuestra este test"**.
7. **Clase 4:** ejecutar el plan de QA manual **en el teléfono Android** de un integrante (llamada o alarma, home, bloqueo, teclado, cierre forzado), registrar esperado vs. real y comparar con lo que mostraron los tests del editor.

**Objetivo:** aplicar el ciclo de la Unidad 3 a un riesgo **propio de la plataforma**, y reconocer la frontera entre automatización y hardware real.
**Entregable:** commit o zip con los tests, captura del Test Runner en rojo y en verde, una página con las limitaciones y los **casos de QA manual ejecutados en el teléfono** (modelo y versión de Android incluidos).
**Respuesta esperada:**
- dos tests, uno de cada modo;
- el defecto detectado;
- limitaciones explícitas: "no prueba que el SO llame al callback", "no prueba la muerte del proceso", "el teclado en pantalla también dispara `OnApplicationFocus(false)` en Android".

**Errores frecuentes:**
- testear solo que `OnApplicationPause` "existe";
- poner toda la lógica en el `MonoBehaviour`, lo que impide el test de Edit Mode;
- afirmar "probado en móvil" cuando solo se corrió en el Editor.

**Dependencia:** el docente tiene que preparar la versión con el defecto. Está pendiente en `status-unidad.md`.

---

## A4.5 — Tres propuestas de monetización (práctica, Clase 3)

**Consigna.** Un publisher propone tres versiones de Asteroides móvil:
- **P1.** Premium a US$ 2,99, sin ads ni IAP.
- **P2.** Gratis, con un rewarded ad opcional "Continuar con 1 vida" una vez por partida, y un IAP "Quitar anuncios".
- **P3.** Gratis, con interstitial en **cada** Game Over y al abrir la app, más "cofres" pagos con naves al azar sin mostrar probabilidades, y dificultad aumentada para empujar a comprar.

Para cada una:
- ¿cumple las políticas (AdMob, Apple 3.1.1, Google Play Payments)?
- ¿qué cambia en el **diseño** (dificultad, ritmo, progresión, frustración)?
- ¿qué riesgos éticos tiene (dark patterns, loot boxes)?
- ¿a qué jugador le sirve?

Elegir cuál publicarías y defenderla ante el grupo.
**Objetivo:** tratar la monetización como diseño con reglas y ética, no como una lista.
**Respuesta esperada:**
- **P3 viola políticas.** AdMob prohíbe interstitials al abrir la app y después de cada acción; Apple y Google exigen divulgar probabilidades. Además manipula la dificultad, un patrón señalado en la literatura de dark patterns.
- **P2 cumple:** rewarded con opt-in. Pero cambia el balance, porque "continuar" altera el sentido del Game Over y hay que discutirlo.
- **P1 es viable:** ejemplo, Alto's Adventure. Pero limita el alcance.

Cualquier elección vale si se defiende con criterios y fuentes.
**Errores frecuentes:**
- "P3 gana más plata" sin considerar las políticas;
- afirmar que las loot boxes "causan" adicción (la evidencia es correlacional);
- no ver el efecto de P2 sobre el diseño.

---

## A4.6 — "El juego anda bien… los primeros 5 minutos" (formativa, Clase 2)

**Consigna.** Escenario: "Asteroides con explosiones de partículas nuevas va a 60 fps al empezar; a los 8 minutos cae a 35–40 fps en un teléfono de gama media. En el editor nunca baja de 200 fps." Identificar: posible cuello de botella, métrica, herramienta y estrategia, y decir qué herramienta **no** sirve y por qué.
**Respuesta esperada:**
- Cuello de botella: **térmico** (throttling), posiblemente agravado por overdraw de las partículas.
- Métrica: frame time a lo largo del tiempo y estado térmico.
- Herramienta: Profiler conectado a un Development Build en el dispositivo.
- Estrategia: fijar 30 fps o un presupuesto del ~65 % del frame, reducir overdraw y escalar efectos según el estado térmico (Adaptive Performance como mención).
- No sirven: el editor y el Device Simulator.

**Errores frecuentes:** "optimizar el código C#" sin medir; confiar en el editor.

---

## TP N° 3 — Dossier de plataforma: Asteroides móvil (integradora)

Es el **capítulo 1 del proyecto integrador U4–U7**. El diseño completo del integrador está pendiente; ver `status-unidad.md`. La idea es que cada unidad agregue un capítulo sobre el **mismo juego**, de modo que el alumno compare sus propias decisiones entre plataformas.

**Consigna.** Entregar un dossier de 6 a 10 páginas con:
1. **Ficha de plataforma** (hardware, input, UX, rendimiento, testing, distribución, modelo de negocio), con fuentes.
2. **Supuestos de PC detectados** (A4.2) y decisión para cada uno.
3. **Diseño de control y HUD** (A4.3, versión final), con safe area, tamaños, orientación y accesibilidad.
4. **Interrupciones:** comportamiento definido + tests (A4.4) + plan de QA manual.
5. **Rendimiento:** fps objetivo justificado, 2 hipótesis con métrica y herramienta, y **resultado medido con el Profiler en el teléfono Android** (Clase 4), comparado con el editor.
6. **Monetización:** modelo elegido y defendido (A4.5).
7. **Estrategia de pruebas:** tabla riesgo → tipo de prueba → automatizable sí/no → requiere dispositivo sí/no → **qué no demuestra**.
8. **3 decisiones de plataforma (PDR)** con el formato: contexto · opciones · decisión · consecuencias.

**Obligatorio** (decisión D4-03): build de desarrollo de Android instalada en el teléfono de un integrante, con video de 1 minuto jugando y captura del Profiler. Si la build falla por motivos técnicos, se usa el plan B (APK del docente) y se documenta qué no se pudo medir.
**iOS:** solo conceptual (no hay Mac, D4-02). Si el dossier menciona iOS, tiene que decir que no se probó.

### Rúbrica (observable, 4 niveles)

| Criterio (peso) | Insuficiente (1) | Suficiente (2) | Bueno (3) | Muy bueno (4) |
|---|---|---|---|---|
| Diagnóstico de supuestos (15 %) | < 3 supuestos o sin ubicación en el código | 3–4, con ubicación | 5 o más, con eje y consecuencia | Incluye relaciones no obvias (cámara ↔ spawner) |
| Diseño de control y HUD (20 %) | Sin medidas ni safe area | Medidas o safe area | Medidas + safe area + orientación justificada | Además, alternativa accesible y efecto sobre el game design |
| Interrupciones y tests (20 %) | Sin tests | Un test o tests que no fallan con el defecto | Ambos tests, rojo → verde, regresión | Además, límites del test y plan manual concreto |
| Rendimiento (15 %) | "Anda bien" | fps objetivo sin justificar | Hipótesis con métrica y herramienta | Distingue pico vs. sostenido y declara qué no se midió |
| Monetización (10 %) | Lista de modelos | Modelo elegido | Modelo + políticas que cumple | Modelo + políticas + efecto sobre el diseño + ética |
| Estrategia de pruebas (15 %) | Todo "testing manual" o todo "unit test" | Tipos asignados | Automatizable / dispositivo bien asignados | Columna "qué no demuestra" correcta |
| Fuentes y justificación (5 %) | Sin fuentes | Fuentes genéricas | Fuentes oficiales | Oficiales + académicas, bien usadas |

Aprobación del TP: ≥ 2 en todos los criterios y promedio ponderado ≥ 2,5. Equivale a 7 si se mantiene el criterio de promoción del programa; la equivalencia debe ajustarla la titular.

---

## Posible evaluación (Parcial, semana 9; preguntas U4)

| # | Pregunta | Nivel | Respuesta esperada (resumen) |
|---|---|---|---|
| 1 | ¿Por qué un juego que corre a 60 fps en el minuto 1 puede no ser "estable" en móvil? | N1 | Throttling térmico; se mide el rendimiento sostenido |
| 2 | Un compañero dice "lo probé en el Device Simulator, el rendimiento está bien". ¿Qué le respondés? | N2 | El simulador no simula rendimiento, memoria ni render |
| 3 | Dado `Input.GetKey(KeyCode.Space)` dentro de `Ship.Update()`, proponé cómo cambiarías la arquitectura para soportar táctil sin duplicar la lógica de la nave | N3–N4 | Capa de intención (acciones) separada del dispositivo; Input System |
| 4 | Clasificá: rewarded ad, interstitial al abrir la app, banner. ¿Cuál viola políticas de AdMob y por qué? | N2 | Interstitial al abrir la app |
| 5 | Un test de Play Mode llama a `OnApplicationPause(true)` y pasa. ¿Qué **no** demuestra? | N5 | Que el SO lo invoque; la muerte del proceso; el caso del teclado |
| 6 | ¿Por qué S5 (spawn en x ∈ [−8, 8]) es un bug **de plataforma** y no de lógica? | N3 | Depende del aspect ratio y la orientación; en 16:9 funciona |

**Errores frecuentes a observar en el parcial:** "más RAM resuelve todo"; confundir emulador con dispositivo; monetización sin políticas; tests sin límites declarados.
