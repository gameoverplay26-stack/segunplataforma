# Unidad 1 — Clase 1 (v2, 120 min): Fundamentos del Testing

**Materia:** Diseño según Plataformas de Juego
**Carrera:** Tecnicatura Universitaria en Diseño Integral de Videojuegos (Plan 2020)
**Docente:** Ing. Elsa Daniela Ramírez
**Ciclo lectivo:** 2026
**Unidad:** 1 — Fundamentos, Tipos y Técnicas de diseño de testing
**Clase:** 1 de 2 (Semana 1 del programa analítico)
**Duración:** 120 minutos (incluye 10 min de recreo)

**Resultado de aprendizaje vinculado:** RA01.
**Competencias específicas vinculadas:** CE01, CE02, CE05.

> **Relación con la v1 (90 min):** este documento cubre exactamente el mismo contenido temático que `Unidad-1-Clase-1-Fundamentos-del-Testing-2026.md`, sin agregar temas nuevos de la Semana 2. Lo que cambia es la **profundidad de las actividades**, la cantidad de **checks de comprensión intermedios**, un **recreo formal de 10 min**, y una segunda vuelta de la actividad grupal (individual → grupal → puesta en común con rúbrica). Es la opción a usar si la cátedra dispone de un módulo de 2 horas en vez de 1h30.
>
> Igual que en la v1: **[RECICLADO]** = viene de las diapositivas 2025 (PDF1 = *1era parte*, PDF2 = *Parte 2*, con página de origen). **[NUEVO 2026]** = no estaba en las diapositivas viejas, se agrega por exigencia del programa analítico. **[NUEVO v2]** = no estaba ni en las diapositivas viejas ni en la v1 de 90 min; es estructura agregada específicamente para esta versión de 2 horas.

---

## 1. Objetivos de la clase

Idénticos a la v1, sin cambios (el contenido es el mismo, solo cambia el ritmo y la profundidad de las actividades):

1. Explicar qué es el testing de software y por qué es necesario, citando al menos una fuente (Myers o ISTQB).
2. Explicar la relación entre Testing y QA: cuál es subconjunto de cuál y por qué importa la diferencia.
3. Diferenciar error, defecto, fallo y causa raíz con un ejemplo propio.
4. Clasificar un caso de testing por tipo (funcional/no funcional, manual/automatizado) y por nivel (unitario/integración/sistema/aceptación).
5. Redactar un test case básico con su estructura mínima.
6. Enunciar los 7 principios del testing y ejemplificar al menos 3 con casos de videojuegos.

---

## 2. Materiales y logística **[NUEVO v2]**

- Proyector / pantalla compartida.
- Pizarra o Miro/Jamboard para las actividades grupales (permite conservar lo producido por cada grupo).
- Formularios cortos (Google Forms / Kahoot / Mentimeter) para los 2 checks de comprensión intermedios — si no hay herramienta digital, se hacen a mano alzada o por chat.
- Plantilla de test case en blanco (tabla de 7 filas) impresa o compartida por enlace, una por grupo.
- Cronómetro visible (para el docente y para los estudiantes) — con 12 bloques distintos, ayuda mucho a sostener el ritmo.

---

## 3. Guía de tiempos (120 min)

| # | Min | Bloque | Objetivo del bloque | Modalidad |
|---|-----|--------|----------------------|-----------|
| 1 | 0–5 | Apertura y enganche: bugs reales con impacto | Motivar, mostrar que el testing importa fuera del aula | Expositiva |
| 2 | 5–8 | **[NUEVO v2]** Encuadre de la clase | Presentar objetivos y agenda, fijar expectativas de ritmo | Expositiva |
| 3 | 8–20 | ¿Qué es la calidad? ¿Qué es el testing y por qué es necesario? | Instalar definiciones base citando fuentes | Expositiva + pregunta disparadora |
| 4 | 20–32 | Relación Testing–QA + Objetivos del testing | Ubicar el testing dentro de un marco más amplio de calidad | Expositiva + diagrama en vivo |
| 5 | 32–34 | **[NUEVO v2]** Check de comprensión #1 | Verificar retención de bloques 3-4 antes de avanzar | Quiz rápido (3 preguntas) |
| 6 | 34–52 | Errores, defectos, fallos y causa raíz | Distinguir los 4 conceptos con un caso narrativo | Expositiva + actividad individual + puesta en común |
| 7 | 52–62 | **[NUEVO v2]** Recreo / pausa activa | Sostener la atención en la segunda mitad de la clase | — |
| 8 | 62–84 | Test del lápiz aplicado a videojuegos | Practicar pensar atributos de calidad más allá de "funciona/no funciona" | Individual → grupal → puesta en común con rúbrica |
| 9 | 84–86 | **[NUEVO v2]** Check de comprensión #2 | Verificar retención de errores/defectos/fallos y del test del lápiz | Quiz rápido (3 preguntas) |
| 10 | 86–100 | Tipos y niveles de testing | Clasificar testing por tipo y por nivel, con ejemplos de videojuegos | Expositiva + ejemplos guiados |
| 11 | 100–112 | Test cases y test suites | Aprender la estructura formal de un caso de prueba | Expositiva + ejercicio guiado |
| 12 | 112–118 | Los 7 principios del testing | Cerrar con los principios que enmarcan todo lo anterior | Expositiva + dinámica rápida |
| 13 | 118–120 | Cierre, síntesis y preview de la próxima clase | Consolidar y conectar con Semana 2 y el TP N°1 | Expositiva |

**Total: 120 minutos** (110 min de trabajo efectivo + 10 min de recreo).

---

## 4. Desarrollo por bloque

### Bloque 1 (0–5 min) — Apertura: bugs reales con impacto

**[RECICLADO — PDF1 p.4, p.6]** — igual que en la v1.

Mostrar sin preámbulo: el falso "System Error" superpuesto a Clash of Clans, el titular de Forbes sobre el error manual de NYSE (2023), y el titular sobre si el QA de software podría haber evitado el crash del Boeing 737 MAX.

**Pregunta disparadora:** "¿Qué tienen en común estos tres casos, si ninguno es un videojuego?"

---

### Bloque 2 (5–8 min) — Encuadre de la clase **[NUEVO v2]**

- Mostrar la agenda completa de los 13 bloques en una sola diapositiva (versión resumida: "hoy vemos 8 temas, con un recreo a la mitad y 2 controles rápidos de comprensión").
- Aclarar la mecánica de los checks de comprensión (no son evaluativos, son para que ustedes mismos vean qué les quedó claro y qué no).
- Aclarar que hay una actividad grupal larga (test del lápiz) que se retoma después del recreo para redactar un test case.

**Por qué se agrega este bloque en la v2:** con 13 bloques y una duración mayor, un encuadre explícito ayuda a que los estudiantes sostengan el ritmo y sepan cuándo llega el recreo — reduce la sensación de "clase eterna" típica de los módulos de 2 horas.

---

### Bloque 3 (8–20 min) — ¿Qué es la calidad? ¿Qué es el testing y por qué es necesario?

**[RECICLADO — PDF1 p.2, p.3, p.5]** — mismo contenido que el Bloque 2 de la v1, con 3 minutos adicionales para profundizar la discusión.

**Calidad:**
- La calidad de un videojuego es principalmente la ausencia de bugs, pero hay que gestionar las expectativas del jugador.
- Un bug es un comportamiento que se sale de las expectativas del jugador.
- Un juego sin ningún bug puede ser aburrido — tampoco cumple la expectativa.
- Ejemplos visuales: Minecraft (funciona como se espera) vs. bug de modelado tipo Cyberpunk 2077.

**Qué es el testing:**

> "Las pruebas de software son un proceso, o una serie de procesos, diseñados para garantizar que el código informático hace lo que debe hacer y, a la inversa, que no hace nada no previsto. El software debe ser predecible y coherente, sin sorpresas para los usuarios."
> — J. Myers, 2011, p. 2

> "El testing de software es un conjunto de actividades para descubrir defectos y evaluar la calidad de los artefactos del software."
> — ISTQB, 2023, p. 16

**Por qué es necesario:** pérdidas económicas, de tiempo, de reputación, y en casos extremos, lesiones o muerte — conectar con el Bloque 1.

**Pregunta disparadora ampliada (nueva en v2):** después de la pregunta original ("¿Alguna vez un bug les arruinó una partida?"), agregar una segunda ronda: "¿Se les ocurre un caso en el que un juego SIN bugs igual los haya decepcionado? ¿Por qué?" — esto siembra el séptimo principio del testing que se va a ver al final de la clase (falacia de ausencia de errores).

**Cierre de bloque — check informal:** pedir a 1-2 estudiantes que resuman en una frase la diferencia entre "bug" y "mala calidad".

---

### Bloque 4 (20–32 min) — Relación Testing–QA + Objetivos del testing

**[NUEVO 2026]** Relación Testing–QA:

- **QA** = marco amplio, orientado a **prevenir** defectos (procesos, estándares, revisiones, capacitación).
- **Testing** = una actividad dentro de QA, orientada a **detectar** defectos ya presentes, ejecutando el software.
- Analogía: QA es la alimentación y entrenamiento de un equipo de fútbol (prevención); testing es el chequeo médico antes de cada partido (detección).

**[NUEVO v2] Actividad de diagrama en vivo (5 min dentro de este bloque):** el docente dibuja dos círculos concéntricos en la pizarra (QA por fuera, Testing por dentro) y va pidiendo a los estudiantes que ubiquen ejemplos de actividades ("revisar el GDD antes de programar", "jugar el nivel 3 buscando bugs", "capacitar al equipo en buenas prácticas de código", "ejecutar un test case") en el círculo que corresponda.

**[RECICLADO — PDF1 p.7]** Objetivos del testing (ISTQB): evaluar productos de trabajo, provocar fallos y encontrar defectos, asegurar cobertura, reducir riesgo, verificar requisitos (incl. contractuales/legales/normativos), dar información para decisiones, generar confianza, validar que el objeto de prueba funciona como esperaban los implicados.

**Punto de énfasis:** testing no es solo "buscar bugs", también genera información y confianza para decisiones de negocio (ej. "¿lanzamos esta semana?").

---

### Bloque 5 (32–34 min) — Check de comprensión #1 **[NUEVO v2]**

3 preguntas rápidas (Kahoot/Mentimeter o a mano alzada), sin nota, solo diagnóstico:

1. ¿Testing es lo mismo que QA? (V/F)
2. Dar un ejemplo de actividad de QA que NO sea testing.
3. Nombrar 2 de los 8 objetivos del testing vistos.

**Uso del resultado:** si más de la mitad falla la pregunta 1, el docente reserva 1-2 minutos extra al arrancar el Bloque 6 para reforzar la diferencia antes de seguir.

---

### Bloque 6 (34–52 min) — Errores, defectos, fallos y causa raíz

**[RECICLADO — PDF1 p.8-9]**, con la actividad individual ampliada respecto a la v1.

| Concepto | Definición |
|---|---|
| **Error** | Lo que hace un ser humano al equivocarse. Produce uno o varios defectos. |
| **Defecto** | Algo incorrecto creado por un ser humano. Puede producir un fallo. |
| **Fallo** | Si se ejecuta un código con un defecto, produce un fallo (también puede originarse por otros motivos, ej. hardware). |
| **Causa raíz** | La causa original por la que se produce un error. |

**Ejemplo narrativo (PDF1 p.9):** programador con ruptura amorosa (causa raíz) → error de lógica → defecto (`<0` en vez de `<=0`) → fallo cuando la variable vale `0`.

**Actividad individual ampliada (8 min, vs. 5 min en la v1):**

1. (3 min) Cada estudiante escribe su propio ejemplo de error → defecto → fallo → causa raíz aplicado a un videojuego que conozca.
2. (3 min) **[NUEVO v2]** Intercambio en pares: cada estudiante le explica su ejemplo a un compañero, que tiene que identificar cuál de los 4 elementos es cuál sin que se lo digan directamente (verificación cruzada).
3. (2 min) Puesta en común: 2-3 parejas comparten con el grupo completo.

**Cierre de bloque:** el docente destaca un ejemplo bien construido y otro que mezcló "defecto" con "fallo" (error común) para reforzar la distinción.

---

### Bloque 7 (52–62 min) — Recreo / pausa activa **[NUEVO v2]**

10 minutos de corte real. Sugerencia: dejar proyectada una diapositiva con la pregunta que se retoma al volver ("¿Qué elemento de un videojuego eligirían para el test del lápiz?") para que los estudiantes empiecen a pensarlo informalmente durante el recreo.

---

### Bloque 8 (62–84 min) — Test del lápiz aplicado a videojuegos

**[RECICLADO — PDF1 p.10-11]**, actividad ampliada a 3 rondas (individual → grupal → puesta en común con rúbrica) en vez de la ronda grupal única de la v1.

**Dimensiones del test del lápiz:** funcionalidad básica, condiciones límite, condiciones de estrés, usabilidad, seguridad (security), accesibilidad, testing de edad, experiencia de usuario, eficiencia, interfaz de usuario.

**Ronda 1 — Individual (5 min):** cada estudiante elige mentalmente un elemento de un videojuego (botón de menú, ítem de inventario, mecánica de salto, arma) y anota 2-3 dimensiones que se le ocurran aplicadas a ese elemento.

**Ronda 2 — Grupal (12 min):** en grupos de 3-4, cada integrante comparte su elemento e ideas; el grupo elige UN elemento en común y completa las 10 dimensiones lo mejor posible, con al menos una pregunta concreta por dimensión (siguiendo el estilo "¿puede la gente daltónica...?").

**Ronda 3 — Puesta en común con rúbrica (5 min):** cada grupo comparte 1 dimensión que le resultó sorprendente o no obvia. El docente evalúa oralmente contra esta rúbrica breve (no es nota, es feedback en el momento):

| Criterio | Qué se espera |
|---|---|
| Cobertura | ¿Tocaron al menos 6 de las 10 dimensiones? |
| Especificidad | ¿Las preguntas son concretas al elemento elegido, o genéricas? |
| Pensamiento crítico | ¿Encontraron alguna dimensión no obvia (ej. accesibilidad, testing de edad)? |

**Cierre del bloque:** "esto que armaron es la semilla del test case que van a redactar en el Bloque 11."

---

### Bloque 9 (84–86 min) — Check de comprensión #2 **[NUEVO v2]**

3 preguntas rápidas:

1. En el ejemplo del programador, ¿qué fue la causa raíz?
2. Nombrar una dimensión del test del lápiz que NO sea "funcionalidad básica".
3. ¿Qué diferencia hay entre un defecto y un fallo?

---

### Bloque 10 (86–100 min) — Tipos y niveles de testing

**[RECICLADO — PDF1 p.17, p.19]** Tipos de testing:

- **Funcional:** evalúa las funciones que debe realizar el objeto de prueba ("aquello que debe hacer", ISTQB 2023 p.33). Ej.: pulsar "guardar" guarda la partida; recoger 3 manzanas en Minecraft suma 3 al inventario.
- **No funcional:** evalúa atributos distintos de las funciones — "qué tan bien" se comporta (ISTQB 2023 p.33; ISO/IEC 25010): eficiencia de desempeño, compatibilidad, usabilidad, fiabilidad, seguridad, mantenibilidad, portabilidad.
  - Conectar explícitamente con el Bloque 8: usabilidad, eficiencia y seguridad ya aparecieron en el test del lápiz.

**[NUEVO 2026]** Manual vs. automatizado: una persona ejecuta y compara (manual) vs. un script/herramienta lo hace (automatizado, ej. Unity Test Runner — se retoma en Unidad 3). No son excluyentes.

**[NUEVO 2026]** Niveles de testing:

| Nivel | Qué prueba | Ejemplo en un videojuego |
|---|---|---|
| **Unitario** | Una unidad de código aislada | La función `CalcularDaño(ataque, defensa)` devuelve el valor correcto |
| **Integración** | Interacción entre módulos | El inventario actualiza la UI cuando combate agrega un ítem |
| **Sistema** | El sistema completo, de punta a punta | Jugar un nivel completo sin que las mecánicas se rompan entre sí |
| **Aceptación** | Si cumple lo que el stakeholder espera | El productor valida que la build cumple el GDD |

**Pregunta disparadora:** "El elemento que eligieron en el test del lápiz, ¿en qué nivel lo estaban probando? ¿Y si en cambio probáramos solo la función interna que calcula el daño?"

**[NUEVO v2] Ejercicio guiado breve (3 min dentro del bloque):** el docente tira 4 ejemplos sueltos (ej. "probar que dos balas del mismo arma no se cancelan entre sí", "probar que el juego abre sin crashear en Android 12", "probar que el botón X abre el inventario", "el líder de QA aprueba la build para certificación de Sony") y los estudiantes gritan a qué nivel corresponde cada uno.

---

### Bloque 11 (100–112 min) — Test cases y test suites

**[NUEVO 2026]**

- **Test case:** conjunto documentado de condiciones, pasos de ejecución y datos de entrada, con un resultado esperado, para verificar si una función cumple lo requerido.
- **Test suite:** conjunto de test cases agrupados por un criterio común (funcionalidad, módulo, nivel de testing).

**Estructura mínima:** identificador, descripción, condiciones previas, pasos de ejecución, datos de entrada, resultado esperado, resultado real/estado.

**Ejemplo resuelto en el pizarrón (mismo que la v1):**

| Campo | Valor |
|---|---|
| ID | TC-001 |
| Descripción | Verificar que el botón "Guardar" guarda la partida |
| Condición previa | Jugador con partida en curso, en el menú de pausa |
| Pasos | 1. Abrir menú de pausa. 2. Pulsar "Guardar" |
| Dato de entrada | — |
| Resultado esperado | Se genera/actualiza el archivo de guardado y aparece confirmación en pantalla |
| Resultado real | (a completar al ejecutar) |
| Estado | (Pasado/Fallido) |

**Ejercicio guiado ampliado (vs. v1):** cada grupo (mismo agrupamiento del Bloque 8) toma UNA de las dimensiones que trabajó en el test del lápiz y la convierte en un test case formal completo, usando la plantilla en blanco. **[NUEVO v2]** A diferencia de la v1, acá cada grupo redacta 2 test cases en vez de 1 (uno de tipo funcional y uno de tipo no funcional, retomando la distinción del Bloque 10), para practicar la clasificación además de la redacción.

**Puesta en común (2 min):** 1-2 grupos leen su par de test cases (funcional + no funcional) y el resto identifica cuál es cuál sin que se los digan.

---

### Bloque 12 (112–118 min) — Los 7 principios del testing

**[NUEVO 2026]** (ISTQB — principios clásicos):

1. **Las pruebas muestran presencia de defectos, no su ausencia.**
2. **Las pruebas exhaustivas son imposibles.** (Conecta con las técnicas combinatorias de la Clase 2.)
3. **Cuanto antes, mejor (testing temprano).**
4. **Agrupación de defectos (Pareto).**
5. **Paradoja del pesticida** — repetir siempre los mismos test cases deja de encontrar bugs nuevos.
6. **El testing depende del contexto** — no se testea igual un mobile casual que un shooter competitivo.
7. **Falacia de ausencia de errores** — conecta directo con la pregunta ampliada del Bloque 3 (un juego sin bugs conocidos igual puede fallar si no cumple expectativas).

**Dinámica rápida (vs. v1, con 2 minutos más de margen):** el docente tira 4 principios al azar (en vez de 3-4 informal) y pide a distintos estudiantes un ejemplo de videojuego en el momento; si el grupo ya usó el mismo ejemplo dos veces, pedir uno distinto para forzar variedad de casos.

---

### Bloque 13 (118–120 min) — Cierre, síntesis y preview de la próxima clase

- Recorrido relámpago de una frase por cada uno de los 8 temas centrales.
- Preview Clase 2 (Semana 2): técnicas clásicas (ad hoc/exploratory, reproducción de fallos, partición de equivalencia, análisis de valores frontera, testing negativo) y técnicas basadas en modelos y combinatorias (estados y transiciones, pairwise, árboles de clasificación, tablas de decisión).
- Recordatorio: el TP N°1 arranca la semana que viene y abarca Unidad 1 y 2 — los test cases redactados en el Bloque 11 son la base de esa entrega.
- Recordatorio de actividad obligatoria de aula virtual de la semana.

---

## 5. Actividad práctica en clase (resumen, versión ampliada)

1. **Bloque 6:** ejemplo individual de error/defecto/fallo/causa raíz + verificación cruzada en pares.
2. **Bloque 8:** test del lápiz en 3 rondas (individual → grupal → puesta en común con rúbrica) aplicado a un elemento de videojuego.
3. **Bloque 11:** ese mismo elemento se convierte en **2 test cases formales** (uno funcional, uno no funcional) — más ambicioso que la v1, que pedía solo 1.
4. **Puente al TP N°1:** ambos test cases quedan como punto de partida documentado para la primera entrega práctica.

---

## 6. Plan B — si sobra o falta tiempo **[NUEVO v2]**

- **Si sobra tiempo** (ej. los checks de comprensión salen muy rápido): extender la Ronda 3 del Bloque 8 pidiendo que cada grupo comparta 2 dimensiones en vez de 1, o sumar una quinta pregunta a alguno de los checks.
- **Si falta tiempo:** el primer bloque recortable sin perder objetivos es el segundo test case del Bloque 11 (volver a pedir solo 1, como en la v1). El segundo bloque recortable es la Ronda 1 individual del Bloque 8 (pasar directo a grupal). Los checks de comprensión (Bloques 5 y 9) pueden reducirse a 2 preguntas si es necesario, pero no eliminarse — son el principal termómetro de si el ritmo de 2 horas está funcionando.

---

## 7. Notas para la conversión a PowerPoint

Igual que en la v1 (mismo contenido temático), con las diapositivas adicionales que exige la nueva estructura:

| Bloque | Diapositivas reutilizables (origen) | Diapositivas nuevas a diseñar |
|---|---|---|
| 1. Apertura | PDF1 p.4, p.6 | — |
| 2. Encuadre | — | 1 slide nueva: agenda de los 13 bloques |
| 3. Calidad y testing | PDF1 p.2, p.3, p.5 | — |
| 4. Testing–QA + objetivos | PDF1 p.7 | 1 slide: diagrama de círculos concéntricos QA/Testing |
| 5. Check #1 | — | 1 slide con las 3 preguntas |
| 6. Error/defecto/fallo/causa raíz | PDF1 p.8, p.9 | 1 slide de consigna (individual + intercambio en pares) |
| 7. Recreo | — | 1 slide simple "Recreo — 10 min" con la pregunta puente |
| 8. Test del lápiz | PDF1 p.10, p.11 | 1 slide de consigna de las 3 rondas + 1 slide con la rúbrica |
| 9. Check #2 | — | 1 slide con las 3 preguntas |
| 10. Tipos y niveles | PDF1 p.17, p.19 | 2-3 slides: manual/automatizado, tabla de niveles, ejercicio de los 4 ejemplos sueltos |
| 11. Test cases/suites | — | 2-3 slides: definiciones + estructura + tabla TC-001 + consigna de los 2 test cases por grupo |
| 12. 7 principios | — | 1-2 slides con íconos y ejemplos gamer |
| 13. Cierre | — | 1 slide de síntesis + 1 slide de preview |

Las diapositivas de PDF1 p.15-16 (caja negra/blanca) y todo PDF2 (BVA, testing negativo, pairwise, árboles de clasificación, tablas de decisión) siguen reservadas para la Clase 2, igual que en la v1.

---

## 8. Bibliografía citada

Idéntica a la v1:

- Myers, G. (J.). (2011). *The Art of Software Testing*. p. 2.
- ISTQB. (2023). *Foundation Level Syllabus*. pp. 16, 33, 46, 48-49.
- ISO/IEC 25010 — Modelo de calidad de producto software.
- Kaner, C., Falk, J., & Nguyen, H. Q. (2009). *Testing de Software*. Ediciones Ra-ma.
- Stumpe, J. (2018). *Practical Game Testing: A Guide for Game Designers and Testers*. CRC Press.
- Schultz, C., & Bryant, R. (2016), citado en PDF1 p.16 — referencia para la Clase 2.
