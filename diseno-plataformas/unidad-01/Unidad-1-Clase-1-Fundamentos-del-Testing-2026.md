# Unidad 1 — Clase 1: Fundamentos del Testing

**Materia:** Diseño según Plataformas de Juego
**Carrera:** Tecnicatura Universitaria en Diseño Integral de Videojuegos (Plan 2020)
**Docente:** Ing. Elsa Daniela Ramírez
**Ciclo lectivo:** 2026
**Unidad:** 1 — Fundamentos, Tipos y Técnicas de diseño de testing
**Clase:** 1 de 2 (corresponde a la Semana 1 del programa analítico)
**Duración:** 90 minutos

**Resultado de aprendizaje vinculado:** RA01 — Analiza y compara las características técnicas y de usabilidad de distintas plataformas de videojuegos, identificando criterios de diseño adecuados (aplicado aquí a criterios de calidad y testing).
**Competencias específicas vinculadas:** CE01 (interpretar y planificar mecánicas/dinámicas), CE02 (implementar y documentar), CE05 (diseñar casos de prueba — se introduce en esta clase, se profundiza en Unidad 2).

> **Nota de fuentes:** el contenido marcado **[RECICLADO]** proviene de las diapositivas 2025 (`Fundamentos del Testing-. 1era parte.pdf` = PDF1, `Fundamentos del Testing - Parte 2.pdf` = PDF2, con número de página de origen). El contenido marcado **[NUEVO 2026]** no estaba en las diapositivas viejas y se agrega porque lo exige el programa analítico oficial (anexo del docx de planificación de cátedra).

---

## 1. Objetivos de la clase

Al finalizar la clase, el estudiante debe poder:

1. Explicar con sus palabras qué es el testing de software y por qué es necesario, citando al menos una fuente (Myers o ISTQB).
2. Distinguir la relación entre Testing y QA (Quality Assurance): cuál es subconjunto de cuál y por qué importa la diferencia.
3. Diferenciar **error**, **defecto**, **fallo** y **causa raíz** aplicando el concepto a un ejemplo propio (no el del programador visto en clase).
4. Clasificar un caso de testing según su **tipo** (funcional/no funcional, manual/automatizado) y su **nivel** (unitario/integración/sistema/aceptación).
5. Redactar un **test case** básico con su estructura mínima (identificador, descripción, pasos, resultado esperado).
6. Enunciar los 7 principios del testing y dar un ejemplo de videojuego para al menos 3 de ellos.

---

## 2. Guía de tiempos (90 min)

| # | Min | Bloque | Objetivo del bloque | Modalidad |
|---|-----|--------|----------------------|-----------|
| 1 | 0–5 | Apertura y enganche: bugs reales con impacto | Motivar, mostrar que testing importa fuera del aula | Expositiva |
| 2 | 5–15 | ¿Qué es la calidad? ¿Qué es el testing y por qué es necesario? | Instalar definiciones base citando fuentes | Expositiva + pregunta disparadora |
| 3 | 15–25 | **[NUEVO]** Relación Testing–QA + Objetivos del testing | Ubicar el testing dentro de un marco más amplio de calidad | Expositiva |
| 4 | 25–40 | Errores, defectos, fallos y causa raíz | Distinguir los 4 conceptos con un caso narrativo | Expositiva + mini-actividad individual |
| 5 | 40–55 | Test del lápiz aplicado a videojuegos | Practicar pensar atributos de calidad más allá de "funciona/no funciona" | Actividad grupal |
| 6 | 55–70 | Tipos y **[NUEVO]** niveles de testing | Clasificar testing por tipo y por nivel, con ejemplos de videojuegos | Expositiva + ejemplos guiados |
| 7 | 70–80 | **[NUEVO]** Test cases y test suites | Aprender la estructura formal de un caso de prueba | Expositiva + ejercicio guiado |
| 8 | 80–88 | **[NUEVO]** Los 7 principios del testing | Cerrar con los principios que enmarcan todo lo anterior | Expositiva + participación rápida |
| 9 | 88–90 | Cierre y preview de la próxima clase | Sintetizar y conectar con Semana 2 y el TP N°1 | Expositiva |

**Total: 90 minutos.**

---

## 3. Desarrollo por bloque

### Bloque 1 (0–5 min) — Apertura: bugs reales con impacto

**[RECICLADO — PDF1 p.4, p.6]**

Arrancar mostrando 3 imágenes sin mucho preámbulo, dejar que los estudiantes reaccionen:

- Diálogo de error crítico falso usado como estafa ("League of Legends Critical Error Fix") superpuesto a una captura de Clash of Clans — para generar la pregunta "¿esto es un bug real o no?".
- Titular de Forbes: *"New York Stock Exchange's 'Manual Error' Briefly Wiped Billions Of Dollars In Market Value"* (2023).
- Titular sobre el crash del Boeing 737 MAX y la pregunta "¿el QA de software podría haberlo evitado?".

**Pregunta disparadora:** "¿Qué tienen en común estos tres casos? Ninguno es un videojuego, pero los tres tienen algo que ver con lo que van a aprender hoy."

**Gancho a la clase:** el testing no es exclusivo de los videojuegos — es lo mismo que evita pérdidas económicas, de reputación, o en casos extremos, pone en riesgo vidas.

---

### Bloque 2 (5–15 min) — ¿Qué es la calidad? ¿Qué es el testing y por qué es necesario?

**[RECICLADO — PDF1 p.2, p.3, p.5]**

**Calidad:**
- La calidad de un videojuego es, principalmente, la **ausencia de bugs** — pero hay que gestionar las **expectativas del jugador**.
- Un **bug** es un comportamiento que se sale de las expectativas del jugador.
- Un videojuego sin ningún bug puede ser extremadamente aburrido — eso tampoco está en las expectativas del jugador. La calidad no es "cero bugs", es "cumplir o superar la expectativa".
- Ejemplos visuales: un mundo generado de Minecraft (funciona como se espera) vs. un bug de modelado en Cyberpunk 2077 (rompe la expectativa).

**Qué es el testing:**

> "Las pruebas de software son un proceso, o una serie de procesos, diseñados para garantizar que el código informático hace lo que debe hacer y, a la inversa, que no hace nada no previsto. El software debe ser predecible y coherente, sin sorpresas para los usuarios."
> — J. Myers, 2011, p. 2

> "El testing de software es un conjunto de actividades para descubrir defectos y evaluar la calidad de los artefactos del software."
> — ISTQB, 2023, p. 16

**Por qué es necesario:** un software que falla puede causar pérdidas económicas, de tiempo, de reputación, y en casos extremos, lesiones o muerte (conectar con los ejemplos del Bloque 1: NYSE, Boeing).

**Pregunta disparadora:** "¿Alguna vez un bug les arruinó una partida o los hizo perder algo (tiempo, un logro, una partida de ranked)? ¿Cómo se sintieron respecto a las expectativas que tenían del juego?"

---

### Bloque 3 (15–25 min) — Relación Testing–QA + Objetivos del testing

**[NUEVO 2026]** Relación entre Testing y QA:

- **QA (Quality Assurance / Aseguramiento de la Calidad)** es el marco más amplio: un conjunto de actividades y procesos orientados a **prevenir** que los defectos ocurran (procesos de desarrollo, estándares de código, revisiones, capacitación del equipo).
- **Testing** es una de las actividades dentro de QA, enfocada en **detectar** defectos ya presentes en el producto, ejecutando el software y observando su comportamiento.
- Analogía simple: QA es como cuidar la alimentación y el entrenamiento de un equipo de fútbol para que no se lesionen (prevención); testing es como el chequeo médico antes de cada partido para detectar si algo ya está mal (detección).
- Consecuencia práctica para el estudiante: como *tester*, van a encontrar defectos, pero como parte de un equipo de *QA*, también van a poder proponer mejoras de proceso para que esos defectos no se repitan.

**[RECICLADO — PDF1 p.7]** Objetivos del testing (ISTQB):

- Evaluar productos de trabajo (requisitos, historias de usuario, diseños, código).
- Provocar fallos y encontrar defectos.
- Asegurar la cobertura necesaria de un objeto de prueba.
- Reducir el riesgo asociado a una calidad inadecuada.
- Verificar que se cumplen los requisitos especificados, contractuales, legales y normativos.
- Dar información a los implicados para tomar decisiones informadas.
- Generar confianza en la calidad del objeto de prueba.
- Validar que el objeto de prueba funciona como esperaban los implicados.

**Punto de énfasis:** testing no es solo "buscar bugs" — también es generar **información** y **confianza** para que el equipo tome decisiones (ej. "¿lanzamos el juego esta semana o no?").

---

### Bloque 4 (25–40 min) — Errores, defectos, fallos y causa raíz

**[RECICLADO — PDF1 p.8-9]**

Cuatro conceptos con tarjetas/diagrama:

| Concepto | Definición |
|---|---|
| **Error** | Lo que hace un ser humano al equivocarse (ej. piensa mal la lógica del código que está programando). Produce uno o varios defectos. |
| **Defecto** | Algo incorrecto creado por un ser humano. Puede producir un fallo. |
| **Fallo** | Si se ejecuta un código con un defecto, produce un fallo. También puede ocurrir por otros motivos (CPU defectuosa, sobrecalentamiento). |
| **Causa raíz** | La causa original por la que se produce un error. |

**Ejemplo narrativo (PDF1 p.9):**

1. Un programador sufre una ruptura amorosa (**causa raíz**).
2. Al estar desconcentrado, comete un **error** al pensar la lógica del código.
3. Ese error se traduce en un **defecto**: escribe `<0` en vez de `<=0` en una comparación.
4. Cuando el código se ejecuta y la variable toma el valor `0`, se produce un **fallo** (el comportamiento real no coincide con el esperado).

**Mini-actividad individual (5 min):** cada estudiante escribe en el chat/aula virtual un ejemplo propio (real o inventado) de error → defecto → fallo → causa raíz, aplicado a un videojuego que conozca. Se leen 2-3 al azar.

---

### Bloque 5 (40–55 min) — Test del lápiz aplicado a videojuegos

**[RECICLADO — PDF1 p.10-11]**

Introducir la pregunta: "¿Es esto (un lápiz) algo sencillo de testear?" — dejar que los estudiantes digan que sí, y después mostrar que no.

**Dimensiones de testing del lápiz (ejemplo del docente):**

- **Funcionalidad básica:** debería escribir.
- **Condiciones límite:** la mina debería estar presente dentro de la madera.
- **Condiciones de estrés:** el lápiz no se rompe al ser sujetado o caer al suelo.
- **Usabilidad:** el lápiz es fácil de agarrar.
- **Seguridad (security):** agarrar el lápiz no es perjudicial para la salud.
- **Accesibilidad:** ¿puede la gente daltónica leer el texto escrito en lápiz?
- **Testing de edad:** ¿puedo seguir usando el lápiz en 2030?
- **Experiencia de usuario:** ¿puedo coger el lápiz cómodamente?
- **Eficiencia:** ¿cuánto puedo escribir hasta que la mina se termine?
- **Interfaz de usuario:** ¿tiene el lápiz las dimensiones esperadas?

**Actividad grupal (12 min):** en grupos de 3-4, elegir un elemento de un videojuego conocido (un botón de menú, un ítem de inventario, una mecánica de salto, un arma) y repetir el mismo ejercicio: pensar al menos 6 de las 10 dimensiones anteriores aplicadas a ese elemento. Cada grupo comparte 1 dimensión que les resultó sorprendente o no obvia.

**Cierre del bloque:** esto es la semilla de lo que en el Bloque 7 vamos a convertir en un test case formal.

---

### Bloque 6 (55–70 min) — Tipos y niveles de testing

**Tipos de testing** — **[RECICLADO — PDF1 p.17, p.19]**

- **Funcional:** evalúa las funciones que debe realizar el objeto de prueba — "aquello que debe hacer" (ISTQB, 2023, p.33).
  - Ejemplos: pulsar "guardar" guarda la partida; recoger 3 manzanas en Minecraft suma 3 unidades al inventario.
- **No funcional:** evalúa atributos distintos de las funciones — "qué tan bien" se comporta el sistema (ISTQB, 2023, p.33; ISO/IEC 25010). Categorías: eficiencia de desempeño, compatibilidad, usabilidad, fiabilidad, seguridad, mantenibilidad, portabilidad.
  - Conectar con el test del lápiz: usabilidad, eficiencia, seguridad ya aparecieron ahí.

**[NUEVO 2026]** Manual vs. automatizado:

- **Manual:** una persona ejecuta los pasos del caso de prueba y compara el resultado real contra el esperado.
- **Automatizado:** un script o herramienta ejecuta los pasos y compara automáticamente (ej. Unity Test Runner, que se va a ver en Unidad 3).
- No son excluyentes: un buen plan de testing combina ambos según el caso.

**[NUEVO 2026]** Niveles de testing:

| Nivel | Qué prueba | Ejemplo en un videojuego |
|---|---|---|
| **Unitario** | Una unidad de código aislada (una función, un método) | Probar que la función `CalcularDaño(ataque, defensa)` devuelve el valor correcto para distintos inputs |
| **Integración** | La interacción entre dos o más unidades/módulos | Probar que el sistema de inventario actualiza correctamente la UI cuando el sistema de combate agrega un ítem |
| **Sistema** | El sistema completo, de punta a punta | Jugar un nivel completo y verificar que todas las mecánicas conviven sin romperse |
| **Aceptación** | Si el sistema cumple lo que el cliente/stakeholder espera | El productor del juego juega la build y valida que cumple el Game Design Document |

**Pregunta disparadora:** "El test del lápiz que hicieron antes, ¿en qué nivel estaba? ¿Y si en cambio probáramos solo la función que calcula cuánto dura la mina?"

---

### Bloque 7 (70–80 min) — Test cases y test suites

**[NUEVO 2026]**

- **Test case (caso de prueba):** un conjunto documentado de condiciones, pasos de ejecución y datos de entrada, con un resultado esperado, que permite verificar si una función del software cumple con lo requerido.
- **Test suite (suite de pruebas):** un conjunto de test cases agrupados por algún criterio común (una funcionalidad, un módulo, un nivel de testing).

**Estructura mínima de un test case** (se profundiza en Unidad 2, acá se introduce):

- Identificador
- Descripción
- Condiciones previas (pre-requisitos)
- Pasos de ejecución
- Datos de entrada
- Resultado esperado
- Resultado real / Estado (Pasado / Fallido)

**Ejercicio guiado (10 min):** retomar el elemento del videojuego elegido en el Bloque 5 (test del lápiz aplicado) y convertir UNA de las dimensiones exploradas en un test case formal con esta estructura, usando una tabla simple. El docente resuelve un ejemplo en el pizarrón (ej. sobre "botón guardar partida") y cada grupo redacta el suyo.

**Ejemplo resuelto (para el pizarrón):**

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

---

### Bloque 8 (80–88 min) — Los 7 principios del testing

**[NUEVO 2026]** (ISTQB — principios clásicos del testing de software)

1. **Las pruebas muestran la presencia de defectos, no su ausencia.** Testear un juego y no encontrar bugs no significa que no los tenga.
2. **Las pruebas exhaustivas son imposibles.** No se puede probar todas las combinaciones posibles de inputs en un juego con física, IA y multijugador — hay que priorizar (esto conecta con las técnicas combinatorias de la próxima clase).
3. **Cuanto antes, mejor (testing temprano).** Encontrar un bug de diseño en el GDD es mucho más barato que encontrarlo con el juego ya publicado.
4. **Agrupación de defectos (Pareto).** Un pequeño número de módulos suele concentrar la mayoría de los bugs (ej. el sistema de físicas o el multijugador online).
5. **Paradoja del pesticida.** Si siempre se ejecutan los mismos test cases, dejan de encontrar bugs nuevos — hay que revisar y variar las pruebas.
6. **El testing depende del contexto.** No se testea igual un juego mobile casual que un shooter competitivo online.
7. **Falacia de ausencia de errores.** Un juego sin bugs conocidos igual puede fracasar si no cumple lo que el jugador espera (conecta directo con el Bloque 2: calidad = expectativas).

**Actividad rápida (participación oral, sin preparación):** el docente tira 3-4 principios al azar y pide a distintos estudiantes que propongan un ejemplo de videojuego en el momento.

---

### Bloque 9 (88–90 min) — Cierre y preview de la próxima clase

- Síntesis en una frase por bloque (recorrido relámpago de los 8 bloques).
- Preview Semana 2 (Clase 2 de Unidad 1): técnicas clásicas de testing (ad hoc/exploratory, reproducción de fallos, partición de equivalencia, análisis de valores frontera, testing negativo) y técnicas basadas en modelos y combinatorias (estados y transiciones, pairwise testing, árboles de clasificación, tablas de decisión).
- Recordatorio: el **Trabajo Práctico N°1** (individual y/o grupal) arranca la semana que viene y abarca toda la Unidad 1 y 2 — el test case que redactaron hoy en el Bloque 7 es la base de ese TP.
- Recordatorio de actividad obligatoria de aula virtual de esta semana (video + apunte + actividad autoevaluativa).

---

## 4. Actividad práctica en clase (resumen)

Encadenada a lo largo de la clase, no es un bloque aislado:

1. **Bloque 5:** en grupos, aplicar las 10 dimensiones del test del lápiz a un elemento de un videojuego elegido por el grupo.
2. **Bloque 7:** convertir una de esas dimensiones en un test case formal con la estructura vista.
3. **Puente al TP N°1:** ese test case queda como punto de partida documentado para la primera entrega práctica de la cátedra (que integra Unidad 1 y 2).

---

## 5. Notas para la conversión a PowerPoint

| Bloque de la clase | Diapositivas reutilizables (origen) | Diapositivas nuevas a diseñar |
|---|---|---|
| 1. Apertura | PDF1 p.4 (imagen error falso + Clash of Clans), PDF1 p.6 (Forbes NYSE + Boeing) | — |
| 2. Calidad y testing | PDF1 p.2 (¿Qué es la calidad?), PDF1 p.3 y p.5 (¿Qué es el testing?) | — |
| 3. Testing–QA + objetivos | PDF1 p.7 (Objetivos del testing) | 1 slide nueva: relación Testing–QA (diagrama prevención vs. detección) |
| 4. Error/defecto/fallo/causa raíz | PDF1 p.8 (las 4 tarjetas), PDF1 p.9 (ejemplo narrativo) | 1 slide de consigna para la mini-actividad |
| 5. Test del lápiz | PDF1 p.10 (portada), PDF1 p.11 (las 10 dimensiones) | 1 slide de consigna de la actividad grupal aplicada a videojuegos |
| 6. Tipos y niveles | PDF1 p.17 (funcional), PDF1 p.19 (no funcional) | 2-3 slides nuevas: manual vs. automatizado, tabla de niveles de testing con ejemplos |
| 7. Test cases/suites | — | 2 slides nuevas: definiciones + estructura, más la tabla del ejemplo resuelto (TC-001) |
| 8. 7 principios | — | 1-2 slides nuevas: los 7 principios con íconos, ejemplos gamer |
| 9. Cierre | — | 1 slide de síntesis + 1 slide de preview de la clase siguiente |

**Nota:** las diapositivas de PDF1 p.15-16 (caja negra/caja blanca) y PDF2 completo (BVA, testing negativo, pairwise, árboles de clasificación, tablas de decisión) NO se usan en esta clase — quedan reservadas para la Clase 2 (Semana 2), que es donde el programa analítico las ubica.

---

## 6. Bibliografía citada

- Myers, G. (J.). (2011). *The Art of Software Testing*. p. 2.
- ISTQB. (2023). *Foundation Level Syllabus*. pp. 16, 33, 46, 48-49.
- ISO/IEC 25010 — Modelo de calidad de producto software (características no funcionales).
- Kaner, C., Falk, J., & Nguyen, H. Q. (2009). *Testing de Software*. Ediciones Ra-ma. (Bibliografía básica de la cátedra, Unidad 1-2).
- Stumpe, J. (2018). *Practical Game Testing: A Guide for Game Designers and Testers*. CRC Press. (Bibliografía básica de la cátedra, ejemplos aplicados a videojuegos).
- Schultz, C., & Bryant, R. (2016), citado en PDF1 p.16, sobre técnicas de caja blanca — referencia para la Clase 2.
