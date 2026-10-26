# UNRAVEL-LAB-GUIDE: laboratorio de experiencia de usuario con *Unravel* en Xbox

- **Estado:** PROPUESTO. Es una actividad de **análisis de UX**, independiente de la adaptación de los proyectos Unity P1 y P2.
- **Materiales asociados:** `UNRAVEL-QUESTIONNAIRE.md`, `UNRAVEL-OBSERVATION-SHEET.md` y `UNRAVEL-ASSESSMENT-RUBRIC.md`.

## 0. Qué está verificado sobre el juego y qué no

| Dato | Estado | Fuente |
|---|---|---|
| *Unravel* (2016), de Coldwood Interactive, publicado por Electronic Arts; salió el 9/2/2016 para PS4, Windows y Xbox One | VERIFICADO (fuente secundaria) | SRC-011 |
| La ficha de la tienda Xbox lo muestra jugable en Xbox One y Xbox Series X\|S e incluido en EA Play | VERIFICADO según la ficha de la tienda (los precios y la disponibilidad varían; hay que confirmarlos en el momento) | SRC-012 |
| Yarny se desenrolla al avanzar y el hilo se recarga con ovillos; el hilo se usa para balancearse, trepar y tender puentes | VERIFICADO (fuente secundaria) | SRC-011 |
| Lista de 12 capítulos, entre ellos **10 "Rust"** | **Fuente de terceros** (sitio de guías), no oficial. Otra reseña habla de 11 niveles jugables | SRC-013 |
| Contenido del capítulo 10 según esa guía: neumáticos, varios **balanceos** (entre ellos uno "a través de una ventana"), grúa magnética, cintas transportadoras, compactadora de autos, checkpoints | Fuente de terceros, **no verificado en la copia del laboratorio** | SRC-014 |
| Versión exacta de la copia (Xbox One o Series, disco, digital o EA Play, actualizaciones) | **UNKNOWN** → DEC-LAB-009 | — |
| Existencia del "salto del nivel 10" que se quiere analizar | **UNKNOWN** hasta la partida de reconocimiento → DEC-LAB-012 | — |
| *Unravel Two* es **otro juego** (2018) y no debe confundirse con este | VERIFICADO | SRC-012 |

> **Requisito previo obligatorio (docente):** jugar la copia del laboratorio antes de la clase (partida de reconocimiento) para (1) confirmar cada segmento asignado, (2) anotar cómo se accede a él (selección de capítulo o checkpoint) y (3) confirmar o reemplazar el salto del capítulo 10. Ninguna asignación de esta guía es definitiva sin ese paso.

## 1. Objetivos

**Objetivo general:** que cada estudiante analice con evidencia la experiencia de jugador de un segmento de un juego comercial de consola y formule propuestas de mejora de UX/UI justificadas.

**Resultados de aprendizaje.** Al terminar, cada estudiante puede:
1. Distinguir una **observación** (lo que se ve y se puede contar) de una **percepción** (lo que el jugador declara).
2. Registrar intentos, tiempos y errores con un protocolo común.
3. Analizar controles, cámara, señales, feedback y diseño de niveles con vocabulario de UX.
4. Contrastar datos de varios grupos e identificar problemas recurrentes.
5. Proponer mejoras priorizadas y justificadas, y transferir el análisis a la adaptación de sus propios juegos (P1/P2) a gamepad.

**Conocimientos previos:** nociones de UI/HUD, feedback, curva de aprendizaje y diferencias de entrada por plataforma (unidades previas de la cátedra; ajustar al programa vigente).

## 2. Recursos y supuestos

| Recurso | Supuesto | Si no se cumple |
|---|---|---|
| Consolas Xbox | **1** | La planificación ya está pensada para una sola |
| Control | 1 (ideal: 2, para no perder tiempo si se agotan las pilas) | Tener pilas o cable de repuesto |
| Pantalla | TV o proyector visible para todo el aula | Si solo la ve el grupo que juega, ver la variante B de §4 |
| Partida guardada | Perfil con los capítulos asignados accesibles | **BLOCKED** hasta prepararla (DEC-LAB-009) |
| Grabación | No se asume | Solo con autorización expresa (DEC-LAB-011); la evidencia base son notas y conteos |
| Cronómetro | Celular o reloj | — |
| Material impreso | Una ficha de observación por grupo, un cuestionario por jugador y una ficha cruzada por grupo y rotación | Versión digital (formulario) |

**Grupos:** 4 estudiantes por grupo (3 a 5 es aceptable). Ejemplo: 20 estudiantes en 5 grupos. Ajustar el número de grupos a la matrícula real y a la duración de la clase (DEC-LAB-010).

**Roles dentro de cada grupo:**

| Rol | Tarea | No hace |
|---|---|---|
| Jugador/a | Cumple la consigna y responde el cuestionario | No completa la ficha de observación |
| Observador/a de acciones | Cuenta intentos, mide tiempos y clasifica la causa de cada fallo | No interpreta emociones |
| Observador/a de UX | Registra eventos de cámara, UI, señales y feedback | No da indicaciones al jugador |
| Moderador/a-registrador/a | Lee la consigna, controla el tiempo y anota frases textuales del jugador entre comillas | No ayuda a resolver el desafío |

Regla de no intervención: nadie le explica al jugador cómo resolver el desafío. Si se agota el tiempo o el límite de intentos, el desafío se registra como **"no superado"**, no se penaliza y el docente puede mostrar la solución **después** de cerrar el registro.

## 3. Asignación de grupos

Cada grupo tiene un **segmento distinto** y una **dimensión principal** distinta. Los segmentos son **candidatos** y deben confirmarse con la partida de reconocimiento.

| Grupo | Segmento candidato | Dimensión principal | Por qué ese segmento |
|---|---|---|---|
| G1 | Capítulo 1 ("Thistle and Weeds" según SRC-013), desde el inicio hasta el primer checkpoint que el docente defina | Controles, movimiento y saltos: **aprendizaje inicial** | Es el primer contacto con el esquema de control |
| G2 | Capítulo intermedio a elegir por el docente, con desplazamientos amplios o verticales | Cámara, visibilidad y orientación | Pone a prueba el encuadre |
| G3 | Capítulo a elegir, con un puzle que dependa de leer el entorno | Interfaz, señales y feedback (visual, sonoro y háptico si existe) | La tienda describe el juego como contado "sin palabras" (SRC-012): ¿cómo comunica qué hacer? |
| G4 | **Capítulo 10 ("Rust" según SRC-013)**: el desafío concreto confirmado por el docente (candidato según SRC-014: el balanceo largo a través de la ventana) | Dificultad, errores y recuperación (**caso del "salto del nivel 10"**) | Desafío de precisión acotado y medible |
| G5 | Capítulo tardío a elegir, más el menú de opciones del juego | Experiencia global y accesibilidad | Permite comparar con el inicio y revisar las opciones disponibles |

> Si no se confirma que el desafío elegido del capítulo 10 sea un "salto" (puede ser un balanceo o una combinación), se registra con su nombre real ("balanceo a través de la ventana", por ejemplo) y la ficha lo trata como **desafío de precisión**. No se renombra para que coincida con la consigna.

### 3.1 Protocolo específico del desafío del capítulo 10 (G4)

1. **Delimitación:** el docente fija un **punto de inicio** (el checkpoint previo) y un **criterio de éxito** observable (por ejemplo, "Yarny queda apoyado del otro lado de la ventana").
2. **Definición de intento:** desde que el jugador sale del punto estable de inicio hasta el éxito o el fallo (caída, reaparición en el checkpoint o abandono voluntario del intento).
3. **Límite:** 10 intentos u 8 minutos, lo que ocurra primero (ajustable).
4. **Registro por intento:** número, tiempo de inicio y fin, resultado y **causa observada** del fallo (código de la ficha: T = timing, D = distancia o impulso insuficiente, L = lectura del entorno, C = cámara u oclusión, I = input mal ejecutado, H = hilo insuficiente, O = otro).
5. **Preguntas que el grupo debe responder:**
   - ¿El juego comunica antes del primer intento que el desafío es posible y cómo se resuelve? ¿Con qué señales?
   - ¿Qué causa de fallo predomina? ¿Es del jugador (ejecución) o del diseño (lectura o cámara)?
   - ¿Cuánto cuesta un fallo (tiempo hasta reintentar, distancia al checkpoint)?
   - ¿Cambió la estrategia del jugador entre intentos? ¿Por qué señal?
   - ¿La dificultad percibida (cuestionario) coincide con los intentos observados?

### 3.2 Protocolo para todos los grupos (resumen)

| Paso | Contenido |
|---|---|
| 1. Segmento | El asignado, con inicio y fin observables |
| 2. Objetivo de observación | La dimensión principal del grupo |
| 3. Consigna del jugador | "Avanzá desde [inicio] hasta [fin]. Pensá en voz alta: decí qué creés que tenés que hacer y por qué." |
| 4. Acciones a observar | Ver la ficha (§B: intentos; §C: eventos UX) |
| 5. Evidencias | Notas de observación, tiempos, intentos, frases textuales; grabación solo si está autorizada |
| 6. Cuestionario | `UNRAVEL-QUESTIONNAIRE.md`, inmediatamente después de jugar |
| 7. Criterios de análisis | §5 de esta guía |
| 8. Conclusiones | Hallazgos y propuestas priorizadas (entregable) |

## 4. Planificación (base de 120 minutos; ajustar a la duración real)

**Variante A (pantalla visible para todos).**

| Tiempo | Actividad | Grupo que juega | Resto del curso |
|---|---|---|---|
| 0–10 | Encuadre: objetivos, roles, diferencia entre observar y percibir, regla de no intervención, consentimiento | — | Todos |
| 10–80 | **5 rotaciones de 14 min**: 2 min de preparación (cargar el segmento), 10 min de juego y 2 min de cambio. El cuestionario del jugador se completa **durante la preparación de la rotación siguiente** (unos 5 min) | Juega y registra su ficha principal | **Observación cruzada:** cada grupo observa la rotación en curso **con el foco de su propia dimensión** y completa una fila de la ficha cruzada (§D de la ficha). Así, el grupo de cámara junta datos de cámara en los 5 segmentos |
| 80–95 | Consolidación interna: contrastar la ficha con el cuestionario y redactar 3 hallazgos y 2 propuestas | — | Todos, por grupo |
| 95–115 | **Puesta en común:** cada grupo presenta 2 minutos; el docente completa en el pizarrón la matriz segmento × dimensión (§5.1) | — | Todos |
| 115–120 | Cierre: preguntas de reflexión y consigna de entrega | — | Todos |

**Variante B (solo el grupo que juega ve la pantalla).** Los grupos que esperan trabajan en: (1) preparar hipótesis sobre su segmento a partir de la consigna, sin buscar soluciones en internet; (2) definir sus criterios de severidad; (3) analizar la consolidación de los grupos que ya jugaron. Hay que evitar la espera pasiva.

**Clase de 80 minutos:** 4 grupos, rotaciones de 12 minutos y puesta en común de 12 minutos. Otra opción es dividir el laboratorio en dos clases (juego en la primera; consolidación y puesta en común en la segunda).

## 5. Análisis de resultados

### 5.1 Matriz de consolidación (pizarrón o planilla)

| Segmento \| Grupo | Intentos observados (desafío) | Tiempo total | Dificultad percibida (mediana 1–5) | Control percibido (mediana) | Problemas observados (categoría) | Coincidencia percepción/observación |
|---|---|---|---|---|---|---|
| G1 … G5 | | | | | | Sí / Parcial / No |

### 5.2 Reglas de análisis

1. **Escalas 1–5:** son ordinales. Se reportan la **mediana y la distribución** (cuántas respuestas hay en cada valor). El promedio solo se usa como dato complementario y nunca con menos de 3 respuestas.
2. **Conteos:** los intentos y errores **observados** son el dato principal; los intentos que declara el jugador se comparan con ellos.
3. **Discrepancia:** si el jugador declara una dificultad de 4–5 ("muy fácil" o "fácil") y hubo 5 o más intentos fallidos, o al revés, se registra como **hallazgo de percepción** y se discute (aprendizaje, frustración, sesgo de deseabilidad).
4. **Problema recurrente:** aparece en **2 o más segmentos** o lo registran 2 o más observadores independientes.
5. **Severidad** (escala de Nielsen adaptada): 0 = no es un problema; 1 = cosmético; 2 = menor; 3 = mayor (bloquea o frustra repetidamente); 4 = crítico (impide continuar sin ayuda).
6. **Priorización de propuestas:** severidad × frecuencia (n.º de segmentos), y luego el costo estimado (bajo, medio o alto) como desempate.
7. **Prohibido:** completar cuestionarios en nombre de otro, inventar conteos o "redondear" tiempos no medidos. Un dato faltante se marca como **"sin dato"**.

## 6. Entregables por grupo

1. Ficha de observación completa (§A–C), firmada por quienes observaron.
2. Cuestionario del jugador.
3. Filas de la ficha cruzada (§D) de cada rotación observada.
4. Informe breve (2 o 3 páginas): segmento, método, datos, 3 hallazgos con evidencia, contraste entre percepción y observación, 2 o 3 propuestas priorizadas y una **transferencia**: "¿qué aprendimos que aplica a la adaptación a gamepad o táctil de Asteroides o del Platformer?"

## 7. Preguntas de reflexión final

1. ¿Qué diferencia hubo entre lo que el jugador **dijo** y lo que **hizo**? ¿Cómo lo explican?
2. ¿Qué problemas son del jugador (falta de práctica) y cuáles son del diseño? ¿Con qué evidencia los separan?
3. ¿Cómo comunica *Unravel* sus objetivos sin texto? ¿Qué sirve de eso para un juego con HUD?
4. Si tuvieran que llevar el desafío analizado a un **celular**, ¿qué se perdería y qué habría que rediseñar?
5. ¿Qué cambiarían del protocolo para que los datos fueran más confiables?

## 8. Ética y consentimiento

- La participación como jugador es **voluntaria**; quien no quiera jugar puede tomar un rol de observación.
- La evaluación **no** depende de superar el desafío (ver la rúbrica).
- No se graba sin autorización expresa institucional y de las personas grabadas (DEC-LAB-011).
- Los datos se identifican por grupo y rol, no por nombre, en la consolidación pública.
