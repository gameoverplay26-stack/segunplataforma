# CONCEPT DEFINITION — Asteroid Survival

> **Fase SDD:** Concept Definition (fase 5 del plan). **Entrada:** `docs/00-discovery/PROJECT-DISCOVERY.md` (SHA-256 `47c6e17a…4f82c7c`, tag `etapa-00-discovery-complete`) + DEC-001 + DEC-007.
> **Qué es este documento:** la definición del concepto seleccionado, como puente entre Discovery y el GDD.
> **Qué no es:** no es GDD (no fija valores, reglas detalladas ni balance), ni Technical Specification (no define input, datos ni plataformas técnicamente), ni arquitectura (no define clases, interfaces ni componentes).
> **Convención de trazabilidad:** cada afirmación relevante lleva su origen entre corchetes: `[Discovery]` (con la sección citada), `[DEC-00N]`, `[Restricción académica]` o `[Concept Definition]` (propuesta nueva de esta fase, no requisito heredado). Las decisiones abiertas se marcan `DECISIÓN PENDIENTE (DEC-0NN)` y están registradas en `docs/SDD-STATUS.md`.

## 1. Identidad del concepto

```text
Concepto seleccionado:
Alt.5 — Nave + Asteroides

Vertical slice provisional:
Asteroid Survival
```

| Atributo | Definición | Origen |
|---|---|---|
| Nombre provisional | *Asteroid Survival* (nombre del vertical slice; no es un nombre comercial) | [DEC-001] [Discovery § Alt.5] |
| Nombre de trabajo | "Nave + Asteroides" (Alt.5) | [DEC-001] |
| Género | Shooter arcade de supervivencia espacial | [Discovery § Alt.5 "supervivencia espacial"] |
| Perspectiva / cámara | Vista superior (top-down) | [Discovery § Alt.5 "vista superior"] |
| Representación visual 2D o 3D | **DECISIÓN PENDIENTE (DEC-014)** | [Concept Definition] |
| Tipo de experiencia | Un jugador, partidas cortas, sesión autocontenida | [Discovery § Contexto "partidas cortas"] [Discovery § OUT OF SCOPE "multiplayer"] |
| Plataforma objetivo conceptual | PC primero; Mobile como segunda plataforma, con el mismo gameplay | [Discovery § Objetivo "PC → Mobile"] |

**Descripción breve:** el jugador pilota una nave en un área espacial vista desde arriba y debe sobrevivir durante un tiempo limitado, esquivando y destruyendo asteroides para sumar puntos.

## 2. Premisa

- **Qué controla el jugador:** una única nave espacial. [Discovery § Alt.5]
- **Dónde transcurre la acción:** en un área de juego espacial visible en pantalla, sin cambios de escenario ni niveles. [Discovery § Alt.5 "zona de juego"] [Discovery § Alt.5 "No son requisitos: niveles"] El comportamiento en los bordes del área es una **DECISIÓN PENDIENTE (DEC-012)**.
- **Qué ocurre durante una partida:** aparecen asteroides que se desplazan por el área. El jugador mueve la nave para evitarlos y les dispara para destruirlos. [Discovery § Alt.5 "Mecánica principal"]
- **Qué debe hacer el jugador:** mantenerse con vida esquivando asteroides y destruir tantos como pueda para sumar puntuación. [Discovery § Alt.5 "Objetivo"]
- **Objetivo principal:** sobrevivir hasta el final de la partida. La puntuación mide el desempeño durante la partida. [Discovery § Alt.5 "Objetivo"] Si el éxito es solo sobrevivir o además exige un puntaje: **DECISIÓN PENDIENTE (DEC-011)**.

No hay lore ni narrativa: Discovery no los define y no son necesarios para demostrar el concepto. [Discovery § Objetivo "demostrabilidad pedagógica, no riqueza de contenido"]

## 3. Core Loop

```text
mover → esquivar → disparar → destruir → conseguir puntos → sobrevivir
```

[Discovery § Alt.5 "Core loop"]

| Etapa | Acción del jugador | Respuesta del juego | Resultado | Transición |
|---|---|---|---|---|
| **Mover** | Desplaza la nave por el área de juego | La nave cambia de posición | El jugador se posiciona frente a la amenaza | Evalúa si un asteroide se acerca |
| **Esquivar** | Usa el movimiento para apartarse de la trayectoria de un asteroide | No hay colisión si la evasión tiene éxito | La nave conserva su estado | Busca una posición desde la que disparar |
| **Disparar** | Da la orden de disparo | La nave emite un proyectil | Hay un proyectil en vuelo | El proyectil puede alcanzar un asteroide |
| **Destruir** | (resultado del disparo) | El proyectil impacta un asteroide y el asteroide es destruido | El asteroide desaparece de la amenaza activa | Se genera puntuación |
| **Conseguir puntos** | (resultado de destruir) | La puntuación aumenta | El desempeño queda reflejado | El jugador continúa jugando |
| **Sobrevivir** | Repite el ciclo mientras la partida está activa | La partida continúa hasta que se cumple una condición de final | Éxito al completar la duración, o Game Over | Fin de la partida (§4) |

**Nota de interpretación [Concept Definition]:** "esquivar" es el **uso del movimiento** para evitar asteroides, no una mecánica separada. Una acción dedicada de evasión (por ejemplo, un impulso o *dash*) no forma parte del MVP.

Esta fase no define velocidades, cadencias, cooldowns, fórmulas de puntaje, física ni estructuras de datos: son responsabilidad del GDD y de la Technical Specification.

## 4. Condiciones de inicio y final

### Inicio

- La partida comienza con la nave presente y controlable en el área de juego, sin puntuación acumulada y con el tiempo de partida sin consumir. [Concept Definition]
- Para empezar tienen que estar disponibles la nave, la capacidad de disparar y la aparición de asteroides. [Discovery § Alt.5 "Sistemas"]
- Cómo inicia el jugador la partida (inmediato, con una pantalla previa, etc.) se define en el GDD.

### Durante la partida

La partida está **activa** mientras no se haya cumplido ninguna condición de final. Mientras está activa:

- el jugador controla la nave y puede disparar;
- los asteroides aparecen y se desplazan;
- la destrucción de asteroides suma puntuación.

[Discovery § Alt.5]

### Final

| Final | Condición conceptual | Origen |
|---|---|---|
| **Éxito (supervivencia)** | La nave sigue activa al completarse la duración de la partida | [Discovery § Alt.5 "sobrevivir durante un período determinado"] |
| **Derrota → Game Over** | La nave es destruida por las colisiones con asteroides, según el modelo de daño que defina el GDD | [Discovery § Alt.5 "Cadena secundaria"] |

- **Duración objetivo:** **DECISIÓN PENDIENTE PARA GDD (DEC-008)**. Discovery da como referencia general "partidas cortas (3–5 min)" [Discovery § Contexto], pero no fija un valor. Esta fase tampoco lo fija.
- **Modelo de daño y derrota del jugador:** **DECISIÓN PENDIENTE PARA GDD (DEC-009)**. Discovery deja abierto si el jugador tiene vida, varias vidas, invulnerabilidad, escudo o respawn [Discovery § Alt.5].
- **Criterio de resultado (supervivencia sola o también puntaje):** **DECISIÓN PENDIENTE PARA GDD (DEC-011)**.
- En ambos finales, el jugador debe poder conocer el resultado y su puntuación [Concept Definition, derivado de Discovery § Arquitectura conceptual, flujo 4 "pantalla final"]. La forma de presentarlo corresponde al GDD.
- Una vez terminada la partida, no se ejecutan acciones de gameplay (ni movimiento, ni disparo, ni puntuación). [Discovery § Bugs candidatos, BUG-CAND-04 "ninguna acción de gameplay… una vez que Health llega a 0"]

## 5. Entidades principales

Son entidades **conceptuales**: no son clases, componentes Unity, GameObjects ni contratos técnicos.

| Entidad | Responsabilidad conceptual | Interacción principal | Origen |
|---|---|---|---|
| **Nave (Player)** | Representa al jugador; se desplaza y dispara | Recibe las órdenes del jugador; colisiona con asteroides | [Discovery § Alt.5 "Nave/Player"] |
| **Arma** | Permite a la nave disparar, con alguna restricción de cadencia | Emite proyectiles cuando la nave dispara | [Discovery § Alt.5 "Weapon", "cooldown del arma"] |
| **Proyectil** | Transporta el disparo por el área de juego | Impacta asteroides | [Discovery § Alt.5 "Projectile"] |
| **Asteroide** | Amenaza que se desplaza por el área | Es destruido por proyectiles; colisiona con la nave | [Discovery § Alt.5 "Asteroid"] |
| **Aparición de asteroides** | Hace que aparezcan asteroides a lo largo de la partida | Introduce asteroides en el área de juego | [Discovery § Alt.5 "Spawner de asteroides"] |
| **Puntuación (Score)** | Acumula los puntos obtenidos durante la partida | Aumenta cuando se destruye un asteroide | [Discovery § Alt.5 "Score"] |
| **Partida (Game Session)** | Delimita la partida: inicio, estado activo, duración y final | Determina el éxito o el Game Over | [Discovery § Alt.5 "Timer/condición de supervivencia, Game Over"] |

## 6. Interacciones principales

| # | Comportamiento conceptual | Qué queda para fases posteriores (implementación técnica) | Origen |
|---|---|---|---|
| 1 | El jugador controla la nave | Mapeo de dispositivos y abstracción de input (Technical/Architecture Specification, DEC-005) | [Discovery § Alt.5] |
| 2 | La nave puede desplazarse por el área de juego | Modelo de movimiento, velocidades, límites (GDD / Technical Specification, DEC-012) | [Discovery § Alt.5] |
| 3 | La nave puede disparar | Dirección de disparo (DEC-010), cadencia y cooldown (GDD) | [Discovery § Alt.5] |
| 4 | Un proyectil puede alcanzar un asteroide | Detección de impacto (Technical Specification) | [Discovery § Alt.5, cadena principal] |
| 5 | El impacto puede provocar la destrucción del asteroide | Si un impacto basta o hacen falta varios (GDD, DEC-003) | [Discovery § Alt.5, cadena principal] |
| 6 | La destrucción de un asteroide produce puntuación, una sola vez por asteroide | Valor de los puntos (GDD) | [Discovery § Alt.5] [Discovery § Bugs candidatos "score duplicado"] |
| 7 | Un asteroide puede colisionar con la nave | Detección de colisión (Technical Specification) | [Discovery § Alt.5, cadena secundaria] |
| 8 | La colisión puede provocar daño a la nave | Modelo de daño (GDD, DEC-009) | [Discovery § Alt.5, cadena secundaria] |
| 9 | Cuando se cumple la condición de derrota, la partida termina en Game Over | Condición exacta (GDD, DEC-009) | [Discovery § Alt.5, cadena secundaria] |

La columna "comportamiento conceptual" describe **qué** ocurre. **Cómo** lo implementa Unity (física, colisionadores, eventos, componentes) no se define en esta fase.

## 7. Alcance MVP

### MUST HAVE

Lo indispensable para que el concepto funcione y sea demostrable:

| # | Capacidad | Origen |
|---|---|---|
| M1 | Control de la nave por el jugador | [Discovery § Alt.5] |
| M2 | Desplazamiento de la nave en el área de juego | [Discovery § Alt.5] |
| M3 | Esquiva mediante el movimiento (sin mecánica dedicada) | [Discovery § Alt.5 "Core loop"] [Concept Definition, §3] |
| M4 | Disparo. El loop conceptual usa combate a distancia; la decisión formal sobre el tipo de combate sigue pendiente para el GDD (DEC-002). DEC-004 no aplica a este concepto (N/A). | [Discovery § Alt.5] [DEC-002] [DEC-004] |
| M5 | Proyectiles | [Discovery § Alt.5] |
| M6 | Asteroides que aparecen y se desplazan | [Discovery § Alt.5 "Mecánica principal"] |
| M7 | Colisiones relevantes: proyectil–asteroide y asteroide–nave | [Discovery § Alt.5, cadenas de integración] |
| M8 | Destrucción de asteroides | [Discovery § Alt.5] |
| M9 | Puntuación por asteroide destruido | [Discovery § Alt.5] |
| M10 | Condición de finalización por supervivencia (duración: DEC-008) | [Discovery § Alt.5] |
| M11 | Game Over por derrota (modelo: DEC-009) | [Discovery § Alt.5] |
| M12 | Comunicación del resultado y de la puntuación al final de la partida | [Concept Definition, derivado de Discovery § Arquitectura conceptual, flujo 4] |

### SHOULD / COULD HAVE

Son posibilidades, **no requisitos**. Su inclusión se decide en el GDD.

| Prioridad | Posibilidad | Origen |
|---|---|---|
| SHOULD | Mostrar puntuación y tiempo restante durante la partida | [Concept Definition — propuesta] |
| SHOULD | Reiniciar la partida después del final sin reiniciar la aplicación (útil para demos y pruebas manuales) | [Concept Definition — propuesta] |
| COULD | Aumento progresivo de la dificultad dentro de una misma partida | [Concept Definition — propuesta] |
| COULD | Fragmentación de asteroides al ser destruidos | [Concept Definition — propuesta; no proviene de Discovery. Si se incorpora, se relaciona con DEC-003] |
| COULD | Retroalimentación audiovisual básica (sonido, efecto de destrucción) | [Concept Definition — propuesta] |

### OUT OF SCOPE

Excluido del MVP salvo una decisión posterior explícita:

| Excluido | Origen |
|---|---|
| Múltiples tipos de asteroides **como requisito** (la cantidad de tipos es DEC-003) | [Discovery § Alt.5 "No son requisitos"] |
| Múltiples armas | [Discovery § Alt.5 "No son requisitos"] |
| Power-ups (alcance en DEC-006) | [Discovery § Alt.5 "No son requisitos"] [DEC-006] |
| Escudos | [Discovery § Alt.5 "No son requisitos"] |
| Respawn | [Discovery § Alt.5 "No son requisitos"] |
| Bosses | [Discovery § Alt.5 "No son requisitos"] |
| Progresión (alcance en DEC-006) | [Discovery § Alt.5 "No son requisitos"] [DEC-006] |
| Niveles | [Discovery § Alt.5 "No son requisitos"] |
| Multiplayer, backend, matchmaking | [Discovery § Alcance preliminar, OUT OF SCOPE] |
| Monetización y tienda | [Discovery § Alcance preliminar, OUT OF SCOPE] |
| Contenido masivo (decenas o cientos de personajes, contenido generado por usuarios) | [Discovery § Alcance preliminar, OUT OF SCOPE] |
| Enemigos que disparan, oleadas, estación a proteger (extensiones, §8) | [Discovery § Alt.5 "Posibles extensiones futuras"] |
| Mecánica dedicada de evasión (*dash* o similar) | [Concept Definition, §3] |
| Reutilización directa del material existente de asteroides del repositorio: assets, escenas, prefabs, scripts, sistemas, implementación funcional, configuraciones específicas u otros componentes. El MVP tiene implementación y artefactos propios y no depende de ese material. Puede consultarse solo como referencia técnica y/o académica. | [DEC-013 — Opción A] [Discovery § Alt.5 "Observación de alcance"] |
| Cualquier sistema no necesario para demostrar el objetivo académico | [Discovery § Alcance preliminar, OUT OF SCOPE] |

## 8. Extensiones futuras

```text
FUERA DEL MVP ACTUAL
```

Discovery las registra como posibles evoluciones. **No son alternativas formales, no generan requisitos ni decisiones y no se diseñan aquí.** [Discovery § Alt.5 "Posibles extensiones futuras"]

| Extensión | Idea | Estado |
|---|---|---|
| **A — Nave + Dodge & Shoot** | Enemigos con capacidad ofensiva; oleadas | FUERA DEL MVP ACTUAL |
| **B — Nave + Point Defense** | Estación o base a proteger (con su propia vida); oleadas; dificultad; posibles power-ups | FUERA DEL MVP ACTUAL |

## 9. Testing como objetivo académico

Esta sección identifica **qué comportamientos** del concepto permiten demostrar testing. No define frameworks, fixtures, mocks, nombres de métodos, scripts ni escenas de test: eso corresponde a la Test Strategy.

### Unit Testing: comportamientos aislables

| Comportamiento aislable | Por qué es aislable | Origen |
|---|---|---|
| Incremento de puntuación por asteroide destruido | Regla simple de acumulación, sin depender de otras entidades | [Discovery § Alt.5 "puntos por asteroide"] |
| Restricción de cadencia del arma | Decide si se puede disparar en un momento dado | [Discovery § Alt.5 "cooldown del arma"] |
| Daño y destrucción de un asteroide | Regla propia del asteroide ante un impacto | [Discovery § Alt.5 "daño/destrucción"] |
| Reducción de vida o condición de derrota de la nave (según DEC-009) | Regla propia de la nave ante una colisión | [Discovery § Alt.5] [DEC-009] |
| Posiciones válidas de aparición de asteroides | Regla sobre dónde puede aparecer un asteroide (p. ej., no encima de la nave) | [Discovery § Alt.5 "posiciones válidas de aparición"] |
| Condición de supervivencia o fin de la partida | Regla temporal de la partida | [Discovery § Alt.5 "condición de supervivencia"] |
| Movimiento | Cambio de posición a partir de una intención de movimiento | [Discovery § Alt.5 "movimiento"] |

La aparición de asteroides involucra aleatoriedad. Para que las pruebas sean repetibles, el diseño futuro deberá permitir determinismo, sin definir aquí cómo. [Discovery § Alt.5]

### Integration Testing: cadenas conceptuales

**Escenario principal** [Discovery § Alt.5, cadena principal]:

```text
Player → Weapon → Projectile → Asteroid → Collision → Destruction → Score
```

Demuestra que la orden de disparo del jugador atraviesa todas las entidades involucradas y termina en una puntuación correcta. El proyectil tiene que existir, alcanzar el asteroide, destruirlo y sumar puntos **una sola vez**. Ninguna prueba aislada verifica esa colaboración.

**Escenario secundario** [Discovery § Alt.5, cadena secundaria]:

```text
Asteroid → Collision → Player Damage → Game Over
```

Demuestra que una colisión real entre asteroide y nave se traduce en daño, y que al cumplirse la condición de derrota (DEC-009) la partida termina en Game Over y no admite más acciones de gameplay.

### Regresión

Discovery ya registra bugs intencionales candidatos para Alt.5, que las cadenas anteriores deberían detectar:

- el proyectil no destruye;
- se destruye sin puntuar;
- el score se duplica;
- la colisión se procesa dos veces;
- el cooldown es incorrecto;
- el asteroide aparece en una posición inválida;
- el Game Over ocurre antes o después de lo esperado.

[Discovery § Alt.5 "Bugs intencionales candidatos"]

No se introducen ahora: se aprueban como `BUG-###` recién en Regression Testing.

## 10. Diseño multiplataforma

**Principio:** el gameplay debe mantenerse independiente del dispositivo de entrada. [Discovery § Estrategia multiplataforma] [Discovery § Objetivo "PC → Mobile"]

| Plataforma | Intención conceptual | Origen |
|---|---|---|
| **PC** (primera) | Movimiento con teclado; apuntado y disparo con mouse u otro mecanismo compatible | [Discovery § Alt.5 "PC vs Mobile"] |
| **Mobile** (segunda) | Controles táctiles: un mecanismo equivalente de movimiento (p. ej., joystick virtual) y uno equivalente de disparo (p. ej., botón táctil) | [Discovery § Alt.5 "PC vs Mobile"] |

- Las dos plataformas ofrecen las **mismas intenciones de juego** (moverse, disparar). Solo cambia el dispositivo que las produce. [Discovery § Estrategia multiplataforma]
- Cómo se determina la dirección de disparo (hacia donde apunta la nave, apuntado independiente o asistido) es una **DECISIÓN PENDIENTE (DEC-010)**. Afecta el comportamiento del juego (GDD) y su mapeo en cada plataforma (Technical Specification).
- **No se definen aquí:** Input Actions, Action Maps, Control Schemes, bindings, clases o APIs de input, ni arquitectura de adapters. La estrategia de input es **DEC-005 — DEFERRED — Technical / Architecture Specification**.

## 11. Restricciones académicas

| Restricción | Tipo | Origen |
|---|---|---|
| Alcance pequeño, progresivo y controlable ("no es un juego comercial") | Requisito documentado | [Discovery § Objetivo] |
| Posibilidad de demostrar Unit Testing | Requisito documentado | [Discovery § Objetivo] |
| Posibilidad de demostrar Integration Testing | Requisito documentado | [Discovery § Objetivo] |
| Diseño para más de una plataforma (PC → Mobile) | Requisito documentado | [Discovery § Objetivo] |
| Separación entre input y lógica de gameplay | Requisito documentado | [Discovery § Estrategia multiplataforma] [Discovery § Riesgos "Confusión de input"] |
| Posibilidad de regresión (bugs controlados detectados por la suite) | Requisito documentado | [Discovery § Estrategia SDD, etapa Regression Testing] |
| Unity `6000.3.11f1 LTS` | Requisito documentado | [Discovery § Objetivo] [`CLAUDE.md` §2] |
| Control de versiones con Git por etapas | Requisito documentado | [Discovery § Objetivo] [DEC-007] |
| Desarrollo guiado por especificaciones (SDD) | Requisito documentado | [Discovery § Objetivo] |

No se agregan restricciones académicas que no estén documentadas.

## 12. Riesgos conceptuales

| Riesgo | Descripción | Mitigación conceptual | Origen |
|---|---|---|---|
| Crecimiento de alcance | Sumar mecánicas antes de cerrar el vertical slice base | Mantener el MVP de §7; lo nuevo pasa por decisión explícita | [Discovery § Riesgos "Scope creep"] |
| Tipos de asteroides prematuros | Agregar variantes antes de validar el loop con un solo tipo | Tratarlo en DEC-003 (GDD); múltiples tipos no son requisito | [Discovery § Alt.5 "Riesgos de alcance"] |
| Power-ups prematuros | Incorporar mejoras temporales en el MVP | OUT OF SCOPE; alcance en DEC-006 | [DEC-006] |
| Múltiples armas | Diversificar el disparo antes de estabilizar la cadena principal | OUT OF SCOPE | [Discovery § Alt.5 "No son requisitos"] |
| Controles innecesariamente complejos | Esquemas de control que dificultan la paridad PC/Mobile | Mismas intenciones en ambas plataformas; DEC-010 y DEC-005 se resuelven en su fase | [Discovery § Riesgos "Confusión de input"] |
| Dependencia de assets externos | Que el avance dependa de conseguir o producir arte y sonido | La demostrabilidad no depende de la calidad visual. La política de assets corresponde al GDD o a la Technical Specification | [Discovery § Objetivo "no la riqueza de contenido"] |
| Confusión MVP / extensiones | Tratar las extensiones A/B como alcance actual | §8 las marca como FUERA DEL MVP ACTUAL | [Discovery § Alt.5 "Posibles extensiones futuras"] |
| Reutilización no controlada de material del curso | El repositorio contiene proyectos de cátedra sobre asteroides, fuera del alcance SDD, que podrían mezclarse con el proyecto SDD | **DEC-013 — RESOLVED, Opción A.** El material existente se usa solo como referencia técnica y/o académica (estudiar conceptos, comparar soluciones, analizar ejemplos de Unity), sin reutilización directa en el MVP (ver §7, OUT OF SCOPE). Consultarlo no lo convierte en dependencia del producto. Una reutilización directa futura requiere una decisión explícita posterior. | [Discovery § Alt.5 "Observación de alcance"] [`CLAUDE.md` §1] [DEC-013] |
| Ambigüedad del modelo de derrota | "Varias vidas" implicaría algún tipo de reaparición, y el respawn está OUT OF SCOPE | Resolverlo de forma consistente en DEC-009 (GDD) | [Discovery § Alt.5] [Concept Definition] |
