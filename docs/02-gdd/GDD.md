# GDD — Asteroid Survival

> **Fase SDD:** Game Design Specification (GDD), fase 6. **Estado:** DRAFT, con validación documental y pendiente de aprobación del usuario.
> **Entradas normativas:** `docs/00-discovery/PROJECT-DISCOVERY.md` (tag `etapa-00-discovery-complete`), `docs/01-concept/CONCEPT-DEFINITION.md` (tag `etapa-01-concept-complete`) y las decisiones `DEC-001`…`DEC-041` de `docs/SDD-STATUS.md`.
> **Qué es este documento:** las reglas de gameplay del MVP y los requisitos funcionales verificables (`REQ-###`) que se derivan de ellas.
> **Qué no es:** no es Technical Specification (no define implementación, componentes Unity, física, input ni valores técnicos) ni arquitectura (no define clases, interfaces ni eventos).
> **Convención:** cada regla cita su origen entre corchetes (`[DEC-0NN]`, `[CD §n]`, `[CD Mn]`, `[Discovery]`). Lo que ninguna fuente define aparece en §15 como punto abierto, **no** como regla.

## 1. Propósito, alcance y fuentes normativas

**Propósito.** Especificar el gameplay del vertical slice *Asteroid Survival* con suficiente precisión para que la Technical Specification, la Test Strategy y la implementación se deriven sin inventar reglas.

**Alcance.** Un único MVP: un jugador, una nave, un tipo de asteroide, partidas cortas, PC primero y Mobile después, con el mismo gameplay. [DEC-001] [CD §1] [Discovery § Objetivo]

**Fuentes normativas, en orden de precedencia:**

1. Decisiones `RESOLVED` en `docs/SDD-STATUS.md` (DEC-001…DEC-041). Prevalecen sobre textos anteriores cuando los precisan.
2. `CONCEPT-DEFINITION.md` (MUST HAVE M1–M12, OUT OF SCOPE, entidades, interacciones).
3. `PROJECT-DISCOVERY.md` (objetivo académico, restricciones, Alt.5).

**Glosario mínimo:**

| Término | Significado en este GDD |
|---|---|
| Partida activa | Intervalo entre el fin de la cuenta regresiva y el final de la partida |
| Área de juego | Espacio 2D visible donde transcurre el gameplay [DEC-014] |
| Destrucción | Desaparición de un asteroide por impacto de proyectil. Es el único evento que puntúa [DEC-027] |
| Eliminación por salida | Desaparición de un asteroide o proyectil al abandonar el área. **No es destrucción** [DEC-012] |
| Contacto | Colisión entre un asteroide y la nave [DEC-020] |
| Resultado | *Completado* (supervivencia) o *Game Over* (derrota) [DEC-011] |

## 2. Visión y experiencia de juego

El jugador pilota una nave en un área espacial 2D vista desde arriba. Debe sobrevivir una partida de duración limitada esquivando asteroides con el movimiento y destruyéndolos con disparos para sumar puntos. [CD §1] [CD §2] [DEC-014]

- **Experiencia:** arcade, un jugador, sesiones cortas y autocontenidas, sin narrativa. [CD §1] [CD §2]
- **Objetivo del jugador:** llegar al final de la partida con la nave activa. La puntuación mide el desempeño, pero no condiciona el resultado. [DEC-011]
- **Objetivo académico:** demostrar Unit Testing, Integration Testing, diseño PC → Mobile con gameplay independiente del dispositivo, y regresión. [Discovery § Objetivo] [CD §11]

## 3. Core loop

```text
mover → esquivar → disparar → destruir → conseguir puntos → sobrevivir
```

[DEC-001] [CD §3]

| Etapa | Regla que la sostiene |
|---|---|
| Mover | La nave se desplaza libremente en el plano 2D, sin salir del área (§5, §9) |
| Esquivar | Uso del movimiento para evitar contactos. No hay mecánica dedicada de evasión [CD §3] |
| Disparar | Disparo continuo mientras se mantiene la acción, en la dirección de la orientación (§6) |
| Destruir | Un impacto de proyectil destruye un asteroide (§7, §8) |
| Conseguir puntos | +10 por asteroide destruido (§10) |
| Sobrevivir | Llegar a la duración de la partida con vida > 0 (§4) |

## 4. Flujo de partida

```text
Pantalla previa ──(acción de inicio)──► Cuenta regresiva (3 s) ──► Partida activa (3 min)
                                               ▲
                     Reinicio (SHOULD) ────────┘  (sin pasar por la pantalla previa)
                                                                        │
                                   ┌────────────────────────────────────┴───────────┐
                                   ▼                                                ▼
                     Vida llega a 0 → GAME OVER                 Duración alcanzada con vida > 0 → COMPLETADO
                                   └──────────────► Resultado + score final ◄───────┘
```

1. **Pantalla previa.** La aplicación presenta una pantalla previa. La partida **no** comienza hasta que el jugador realiza una **acción explícita de inicio**. [DEC-015] → REQ-001
2. **Cuenta regresiva.** Tras la acción de inicio hay una cuenta regresiva de **3 s**. Ocurre **antes** de la partida y no consume su duración. Durante la cuenta regresiva la partida no está activa, así que no hay acciones de gameplay. [DEC-015] [DEC-033] [DEC-041] [CD §4] → REQ-002
3. **Estado inicial** (al terminar la cuenta regresiva):
   - nave presente y controlable;
   - vida = **5**;
   - score = **0**;
   - tiempo de partida sin consumir;
   - orientación **hacia arriba**.

   [CD §4] [DEC-032] [DEC-035] → REQ-003
4. **Duración.** El tiempo de partida empieza a correr al terminar la cuenta regresiva. La duración objetivo es **3 min**. El criterio de aceptación admite cualquier duración en **[3, 5] min, inclusive**. [DEC-008] [DEC-016] [DEC-033] [DEC-034] → REQ-004
5. **Partida activa.** Mientras no se cumpla ninguna condición de final:
   - el jugador controla la nave y dispara;
   - los asteroides aparecen y se desplazan;
   - la destrucción de asteroides puntúa.

   [CD §4]
6. **Final por supervivencia.** Si al alcanzarse la duración la nave tiene vida > 0, el resultado es **Completado**. [DEC-011] [CD M10] → REQ-005
7. **Final por derrota.** Cuando la vida de la nave llega a 0, el resultado es **Game Over** y no hay respawn. [DEC-009] [CD M11] → REQ-006
8. **Empate.** Si la vida llega a 0 en el mismo instante en que se alcanza la duración, el resultado es **Game Over**. [DEC-017] → REQ-007
9. **Después del final.** No se ejecutan acciones de gameplay: ni movimiento de la nave, ni disparo, ni cambios de score. [CD §4] [Discovery § BUG-CAND-04] → REQ-008. Los asteroides y proyectiles presentes **desaparecen**, sin puntuar. [DEC-039] → REQ-039
10. **Resultado.** Se comunica el resultado (*Completado* o *Game Over*) y el **score final**. La evaluación del desempeño consiste solo en mostrar el score final, sin categorías ni rangos. [CD M12] [DEC-011] [DEC-029] → REQ-009, REQ-010
11. **Reinicio (SHOULD).** Se puede iniciar una nueva partida sin reiniciar la aplicación. El reinicio pasa **directo a la cuenta regresiva**, sin volver a la pantalla previa, y la nueva partida parte del estado inicial. [DEC-031] [DEC-040] → REQ-031

## 5. Nave

- **Entidad única controlada por el jugador.** [CD §5]
- **Movimiento:** libre en el plano 2D, según la intención de movimiento del jugador. [CD M1, M2] [DEC-014] → REQ-011. La velocidad es TECH-DEFERRED (§15).
- **Límites:** la nave no puede abandonar el área de juego (§9). → REQ-012
- **Orientación:**
  - al empezar, apunta hacia arriba, hacia el borde superior del área [DEC-032];
  - después, es la **última dirección de movimiento intentada** por el jugador, **aunque un borde bloquee el desplazamiento**;
  - sin intención de movimiento, se conserva la orientación vigente.

  [DEC-010] [DEC-018] [DEC-019] → REQ-013
- **Vida:** inicial = 5. Cada contacto resta 1 (§8). **Nunca baja de 0.** Al llegar a 0 → Game Over (§4). Sin respawn. [DEC-009] [DEC-020] [DEC-035] [DEC-036] → REQ-036

## 6. Combate: disparo y proyectiles

- **Tipo de combate:** exclusivamente a distancia. La nave no destruye asteroides por embestida. [DEC-002]
- **Disparo:** mientras el jugador mantiene la acción de disparo, la nave dispara de forma continua, limitada por una restricción de cadencia (el valor es TECH-DEFERRED). [DEC-022] [CD M4] → REQ-016
- **Dirección:** cada proyectil sale en la dirección de la orientación de la nave en el momento del disparo. No hay apuntado independiente ni autoaim. [DEC-010] → REQ-017
- **Disponibilidad inicial:** gracias a la orientación inicial, se puede disparar desde el comienzo de la partida sin haberse movido. [DEC-018] [DEC-032] → REQ-018
- **Proyectil:**
  - avanza **en línea recta a velocidad constante** en la dirección de disparo (la velocidad es TECH-DEFERRED) [DEC-010] [DEC-037] → REQ-037;
  - desaparece al impactar su **primer** asteroide [DEC-023] → REQ-019;
  - se elimina al abandonar el área [DEC-012] → REQ-020;
  - **no daña ni afecta a la nave** en el MVP [DEC-038] → REQ-038.
- **Un solo tipo de arma.** No hay múltiples armas. [CD §7]

## 7. Asteroides

- **Un único tipo**, de comportamiento homogéneo y **sin fragmentación**. [DEC-003]
- **Aparición:** durante la partida activa, **fuera del área visible**, junto a sus bordes, entrando hacia el interior. **La aparición no es una salida.** [DEC-024] [CD §4] → REQ-021, REQ-024. La frecuencia de aparición y el máximo simultáneo son TECH-DEFERRED.
- **Movimiento:** trayectoria **recta a velocidad constante**. Sin IA ni persecución. [DEC-025] → REQ-022. La velocidad es TECH-DEFERRED.
- **Destrucción:** **un impacto** de proyectil destruye el asteroide. [DEC-026] [CD M8] → REQ-023
- **Contacto con la nave:** daña a la nave (§8) y **sigue su trayectoria**. No se destruye, no se retira y no puntúa. [DEC-021] [DEC-002] → REQ-015
- **Salida del área:** se elimina al abandonar el área. **No es destrucción** y **no puntúa**. [DEC-012] [DEC-027] → REQ-024, REQ-027
- **Entre asteroides:** no interactúan; pueden superponerse. [DEC-030] → REQ-025

## 8. Colisiones y daño

| Colisión | Efecto | Origen | REQ |
|---|---|---|---|
| Proyectil → asteroide | El asteroide se destruye, el proyectil desaparece y se suman +10 puntos, **una sola vez** | DEC-023, DEC-026, DEC-027, DEC-028, DEC-035 | REQ-019, REQ-023, REQ-026 |
| Asteroide → nave | La nave pierde **1** de vida. **Cada asteroide daña como máximo una vez**. El asteroide continúa su trayectoria | DEC-020, DEC-021, DEC-035 | REQ-014, REQ-015 |
| Asteroide ↔ asteroide | Sin efecto (superposición) | DEC-030 | REQ-025 |
| Proyectil ↔ nave | Sin efecto en el MVP | DEC-038 | REQ-038 |

**Consecuencia de las reglas vigentes (no es una regla nueva):** con vida 5, daño 1 y un daño por asteroide, la nave soporta 4 contactos, y el 5.º contacto de un asteroide distinto produce el Game Over. [DEC-021] [DEC-035]

**Contactos simultáneos:** cada asteroide aplica su daño de 1 y la vida se **limita a 0** (nunca queda negativa) → Game Over. [DEC-036] → REQ-036

## 9. Área de juego

- **Espacio 2D** delimitado. [DEC-014]
- **Nave:** borde **bloqueante**. [DEC-012] → REQ-012
- **Asteroides y proyectiles:** se **eliminan** al abandonar el área. [DEC-012] → REQ-020, REQ-024
- **Sin wrap-around ni rebote.** [DEC-012]
- Las dimensiones, la relación de aspecto y la cámara son TECH-DEFERRED (§15).

## 10. Score y evaluación del desempeño

- **Único evento que puntúa:** la destrucción de un asteroide por proyectil, **+10 puntos**, una vez por asteroide. [DEC-027] [DEC-028] [DEC-035] [CD M9] → REQ-026
- **No puntúan:** la eliminación de un asteroide por salida del área ni el contacto entre nave y asteroide. [DEC-027] → REQ-027
- **Score inicial:** 0. [CD §4] → REQ-003
- **Papel del score:** evalúa el desempeño y **no** condiciona el resultado. No hay score mínimo, umbral, categorías, ranking, recompensas ni persistencia. [DEC-011] [DEC-029] → REQ-009, REQ-010

## 11. Intención multiplataforma (PC / Mobile)

**Principio:** mismo gameplay en PC y Mobile, independiente del dispositivo de entrada. [Discovery § Estrategia multiplataforma] [CD §10] → REQ-034

**Intenciones de gameplay** (las únicas que las reglas necesitan):

| Intención | Uso | Origen |
|---|---|---|
| **Moverse** (dirección 2D) | Mover la nave y definir su orientación | DEC-010, DEC-019 |
| **Disparar** (mantener) | Disparo continuo con cadencia | DEC-022 |
| **Iniciar** | Acción explícita en la pantalla previa | DEC-015 |
| **Reiniciar** (SHOULD) | Nueva partida sin reiniciar la aplicación | DEC-031 |

**No se definen aquí:** dispositivos, controles, bindings, Input System ni arquitectura de input. Eso queda en **DEC-005 (DEFERRED), Technical / Architecture Specification**.

## 12. Alcance MVP (MoSCoW) y OUT OF SCOPE

**MUST:** M1–M12 del Concept Definition, precisados por las reglas de §4–§11 y los REQ de prioridad MUST (§13).

| Prioridad | Elemento | Origen | REQ |
|---|---|---|---|
| SHOULD | HUD de score durante la partida | DEC-031 | REQ-028 |
| SHOULD | HUD de tiempo durante la partida | DEC-031 | REQ-029 |
| SHOULD | HUD de vida durante la partida | DEC-031 | REQ-030 |
| SHOULD | Reinicio sin reiniciar la aplicación | DEC-031 | REQ-031 |
| COULD | Dificultad progresiva dentro de la partida | DEC-031 | REQ-032 |
| COULD | Feedback audiovisual básico | DEC-031 | REQ-033 |

**OUT OF SCOPE del MVP** → REQ-035:

- múltiples tipos de asteroides y fragmentación [DEC-003];
- múltiples armas [CD §7];
- power-ups y progresión (COULD futuro, no son requisito) [DEC-006];
- escudos [CD §7];
- respawn [DEC-009];
- bosses y niveles [CD §7];
- multiplayer, backend y matchmaking; monetización y tienda; contenido masivo [Discovery § Alcance preliminar];
- embestida ofensiva [DEC-002];
- evasión dedicada (*dash*) [CD §3];
- apuntado independiente y autoaim [DEC-010];
- wrap-around y rebote [DEC-012];
- categorías de score, ranking, recompensas y persistencia [DEC-011] [DEC-029];
- reutilización directa del material previo de asteroides del repositorio [DEC-013];
- extensiones A (Nave + Dodge & Shoot) y B (Nave + Point Defense) [CD §8].

**Ideas futuras registradas (no son requisito ni forman parte del MVP):**
- disparo que varía según el tiempo de presión. Si se adoptara, habría que revisar DEC-022 [DEC-037];
- proyectiles que afecten a la nave, que en el MVP no lo hacen [DEC-038];
- cambios de velocidad de los asteroides a lo largo de la partida, que corresponden a la *dificultad progresiva* (COULD, REQ-032).

## 13. Reglas de gameplay y requisitos

**Formato:**
- **Prioridad:** M = MUST, S = SHOULD, C = COULD.
- **Verificación:** `UNIT` es lógica aislada. `INT` exige ≥2 componentes reales colaborando (skill `unity-testing`). `MANUAL` es playtest o revisión en ejecución. `DOC` es revisión documental.
- **Criterio de aceptación:** *Dado / Cuando / Entonces*.
- Los IDs de test (`TEST-UNIT-###`, `TEST-INT-###`) se asignan en **Test Strategy**.

### 13.1 Flujo de partida

| REQ | P | Requisito | Criterio de aceptación | Verif. | Origen |
|---|---|---|---|---|---|
| REQ-001 | M | La partida comienza desde una pantalla previa con una acción explícita del jugador | Dado que la aplicación está en la pantalla previa, cuando no se realiza la acción de inicio, entonces la partida no comienza; cuando se realiza, comienza la cuenta regresiva | INT + MANUAL | DEC-015 |
| REQ-002 | M | Cuenta regresiva de 3 s antes de la partida, sin acciones de gameplay | Dado que se realizó la acción de inicio (o de reinicio), entonces transcurren 3 s de cuenta regresiva antes de la partida activa; durante ese intervalo no hay movimiento, disparo, puntuación ni consumo del tiempo de partida | UNIT + INT | DEC-015, DEC-033, DEC-041, DEC-040, CD §4 |
| REQ-003 | M | Estado inicial de la partida | Dado el fin de la cuenta regresiva, entonces la nave está presente y controlable, vida = 5, score = 0, tiempo de partida = 0 y orientación = hacia arriba | UNIT | CD §4, DEC-032, DEC-035 |
| REQ-004 | M | Duración de la partida | Dado el inicio de la partida activa, entonces la condición de fin por tiempo se alcanza a los 3 min (objetivo). Criterio de aceptación: la duración que use la implementación ∈ [3, 5] min inclusive | UNIT (con duración reducida, TD-1) + DOC | DEC-008, DEC-016, DEC-034 |
| REQ-005 | M | Final por supervivencia | Dado vida > 0, cuando se alcanza la duración, entonces el resultado es *Completado* | UNIT + INT | DEC-011, CD M10 |
| REQ-006 | M | Final por derrota | Cuando la vida llega a 0, entonces el resultado es *Game Over* y no hay respawn | UNIT + INT | DEC-009, CD M11 |
| REQ-007 | M | Prioridad del Game Over en empate | Dado que la vida llega a 0 en el mismo instante en que se alcanza la duración, entonces el resultado es *Game Over* | UNIT | DEC-017 |
| REQ-008 | M | Sin gameplay después del final | Dado un resultado (*Completado* o *Game Over*), cuando el jugador intenta moverse o disparar, entonces la nave no se mueve, no dispara y el score no cambia | UNIT + INT | CD §4, Discovery BUG-CAND-04 |
| REQ-009 | M | Comunicación del resultado y del score final | Dado el final de la partida, entonces se muestran el resultado y el score final; no se muestran categorías ni rangos | INT + MANUAL | CD M12, DEC-011, DEC-029 |
| REQ-010 | M | El score no condiciona el resultado | Dado vida > 0 al alcanzar la duración, con cualquier score (incluido 0), entonces el resultado es *Completado* | UNIT | DEC-011 |

### 13.2 Nave

| REQ | P | Requisito | Criterio de aceptación | Verif. | Origen |
|---|---|---|---|---|---|
| REQ-011 | M | Movimiento libre en 2D según la intención de movimiento | Dada una intención de movimiento no nula durante la partida activa, entonces la posición de la nave cambia en esa dirección dentro del plano 2D | UNIT + MANUAL | CD M1, M2, DEC-014 |
| REQ-012 | M | Borde bloqueante | Dada la nave en un borde, cuando la intención apunta hacia afuera, entonces la nave permanece dentro del área; no aparece del lado opuesto ni rebota | UNIT | DEC-012 |
| REQ-013 | M | Orientación según la dirección intentada | Dada una intención de movimiento no nula, entonces la orientación pasa a ser esa dirección, aunque un borde bloquee el desplazamiento; dada una intención nula, la orientación no cambia | UNIT | DEC-010, DEC-019 |
| REQ-014 | M | Daño por contacto | Dada una nave con vida *v* > 0, cuando un asteroide la contacta por primera vez, entonces la vida pasa a *v* − 1 | UNIT + INT | DEC-020, DEC-035 |
| REQ-015 | M | Un asteroide daña como máximo una vez | Dado un asteroide que ya dañó a la nave, cuando el contacto se mantiene o se repite, entonces la vida no cambia; el asteroide continúa su trayectoria, no se destruye y no puntúa | UNIT + INT | DEC-021, DEC-002 |

### 13.3 Combate

| REQ | P | Requisito | Criterio de aceptación | Verif. | Origen |
|---|---|---|---|---|---|
| REQ-016 | M | Disparo continuo con cadencia | Dado que el jugador mantiene la acción de disparo durante la partida activa, entonces se emiten proyectiles de forma continua, con un intervalo entre disparos no menor al que fija la cadencia (valor TECH-DEFERRED); al soltar la acción, dejan de emitirse | UNIT | DEC-022, CD M4 |
| REQ-017 | M | Dirección del proyectil = orientación de la nave | Dada una orientación *o* al disparar, entonces el proyectil sale en la dirección *o*; no hay apuntado independiente ni autoaim | UNIT | DEC-010 |
| REQ-018 | M | Disparo disponible desde el inicio | Dado el estado inicial (sin movimiento previo), cuando el jugador dispara, entonces el proyectil sale hacia arriba | UNIT | DEC-018, DEC-032 |
| REQ-019 | M | El proyectil se consume al primer impacto | Dado un proyectil que impacta un asteroide, entonces el proyectil desaparece y no afecta a otros asteroides | UNIT + INT | DEC-023 |
| REQ-020 | M | El proyectil se elimina al salir del área | Dado un proyectil que abandona el área de juego, entonces se elimina | UNIT | DEC-012 |

### 13.4 Asteroides

| REQ | P | Requisito | Criterio de aceptación | Verif. | Origen |
|---|---|---|---|---|---|
| REQ-021 | M | Aparición fuera del área, entrando al interior | Dada la partida activa, cuando aparece un asteroide, entonces lo hace fuera del área visible junto a un borde, con dirección hacia el interior; todos los asteroides son del mismo tipo | UNIT (determinismo: TD-3) | DEC-024, DEC-003, CD M6 |
| REQ-022 | M | Trayectoria recta a velocidad constante | Dado un asteroide en movimiento, entonces su dirección y su velocidad no cambian mientras exista, incluso después de contactar a la nave | UNIT | DEC-025, DEC-021 |
| REQ-023 | M | Un impacto destruye, sin fragmentación | Dado un asteroide, cuando un proyectil lo impacta, entonces el asteroide se destruye y no genera fragmentos | UNIT + INT | DEC-026, DEC-003, CD M8 |
| REQ-024 | M | Aparición ≠ salida; eliminación al salir | Dado un asteroide recién aparecido fuera del área que entra, entonces no se elimina por "salida"; dado un asteroide que abandona el área, entonces se elimina | UNIT | DEC-024, DEC-012 |
| REQ-025 | M | Los asteroides no interactúan entre sí | Dados dos asteroides que se superponen, entonces ninguno cambia su trayectoria ni se destruye | INT | DEC-030 |

### 13.5 Score

| REQ | P | Requisito | Criterio de aceptación | Verif. | Origen |
|---|---|---|---|---|---|
| REQ-026 | M | +10 puntos por asteroide destruido, una sola vez | Dado score *s*, cuando un proyectil destruye un asteroide, entonces el score pasa a *s* + 10; el mismo asteroide nunca vuelve a sumar puntos | UNIT + INT | DEC-027, DEC-028, DEC-035, CD M9 |
| REQ-027 | M | Eventos que no puntúan | Cuando un asteroide sale del área, o contacta a la nave, entonces el score no cambia | UNIT + INT | DEC-027 |

### 13.6 SHOULD / COULD

| REQ | P | Requisito | Criterio de aceptación | Verif. | Origen |
|---|---|---|---|---|---|
| REQ-028 | S | HUD de score durante la partida | Durante la partida activa se muestra el score actual y se actualiza tras cada destrucción | MANUAL + INT | DEC-031 |
| REQ-029 | S | HUD de tiempo durante la partida | Durante la partida activa se muestra información del tiempo de partida | MANUAL | DEC-031 |
| REQ-030 | S | HUD de vida durante la partida | Durante la partida activa se muestra la vida actual y se actualiza tras cada contacto | MANUAL + INT | DEC-031 |
| REQ-031 | S | Reinicio sin reiniciar la aplicación, directo a la cuenta regresiva | Dado un resultado, cuando el jugador realiza la acción de reinicio, entonces comienza la cuenta regresiva (REQ-002) sin pasar por la pantalla previa, y la nueva partida parte del estado inicial de REQ-003 | INT + MANUAL | DEC-031, DEC-040 |
| REQ-032 | C | Dificultad progresiva | Sin especificar: se detalla solo si se incorpora al alcance | N/A (COULD no planificado) | DEC-031 |
| REQ-033 | C | Feedback audiovisual básico | Sin especificar: se detalla solo si se incorpora al alcance | N/A (COULD no planificado) | DEC-031 |

### 13.7 Plataforma y alcance

| REQ | P | Requisito | Criterio de aceptación | Verif. | Origen |
|---|---|---|---|---|---|
| REQ-034 | M | Mismo gameplay en PC y Mobile | Dadas las mismas intenciones (moverse, disparar, iniciar, reiniciar), entonces las reglas de §4–§10 producen el mismo resultado en ambas plataformas; ninguna regla depende del dispositivo | INT (lógica común con intenciones simuladas) + MANUAL por plataforma | Discovery, CD §10, DEC-005 |
| REQ-035 | M | Exclusiones del MVP | Ninguno de los elementos OUT OF SCOPE de §12 está presente en el MVP | DOC (test N/A: verifica ausencia de funcionalidad) | CD §7, DEC-002, 003, 006, 009, 010, 011, 012, 013, 029 |

### 13.8 Requisitos agregados por los puntos abiertos resueltos (DEC-036 a DEC-039)

| REQ | P | Requisito | Criterio de aceptación | Verif. | Origen |
|---|---|---|---|---|---|
| REQ-036 | M | La vida se limita a 0 | Dada una vida *v*, cuando se aplica un daño total *d* ≥ *v* (incluidos contactos simultáneos, 1 por asteroide), entonces la vida resultante es 0, nunca negativa, y el resultado es *Game Over* | UNIT | DEC-036, DEC-020, DEC-021 |
| REQ-037 | M | Proyectil recto a velocidad constante | Dado un proyectil disparado con dirección *o*, entonces mantiene la dirección *o* y una velocidad constante hasta impactar o salir del área | UNIT | DEC-037, DEC-010 |
| REQ-038 | M | Los proyectiles no afectan a la nave | Dado un proyectil que coincide con la nave, entonces la vida de la nave no cambia y el proyectil no se consume por ella | UNIT + INT | DEC-038 |
| REQ-039 | M | Al terminar, asteroides y proyectiles desaparecen | Dado el final de la partida (*Completado* o *Game Over*), entonces no queda ningún asteroide ni proyectil en el área, y el score no cambia por esa desaparición | UNIT + INT | DEC-039, DEC-027 |

### 13.9 Escenarios de integración (candidatos para Test Strategy)

| Escenario | Cadena | REQ cubiertos |
|---|---|---|
| INT-A, principal | Intención de disparo → nave → arma → proyectil → asteroide → colisión → destrucción → score +10 (una vez) | REQ-016, 017, 019, 023, 026 |
| INT-B, secundaria | Asteroide → contacto con la nave → daño −1 (una vez por asteroide) → vida 0 (limitada) → Game Over → sin gameplay; asteroides y proyectiles desaparecen | REQ-014, 015, 036, 006, 008, 039 |
| INT-C, salida | Asteroide o proyectil abandona el área → eliminación → score sin cambio | REQ-020, 024, 027 |
| INT-D, supervivencia | Fin de la cuenta regresiva → partida activa → duración alcanzada con vida > 0 → *Completado* → score final comunicado | REQ-002, 004, 005, 009 (depende de TD-1) |

## 14. Trazabilidad

La matriz completa por REQ está en **`docs/TRACEABILITY.md`**. Resumen DEC → REQ:

| Decisión | REQ |
|---|---|
| DEC-002 | REQ-015, REQ-035 |
| DEC-003 | REQ-021, REQ-023, REQ-035 |
| DEC-006 | REQ-035 |
| DEC-008 / 016 / 034 | REQ-004 |
| DEC-009 | REQ-006, REQ-035 |
| DEC-010 / 019 | REQ-013, REQ-017 |
| DEC-011 / 029 | REQ-005, REQ-009, REQ-010 |
| DEC-012 | REQ-012, REQ-020, REQ-024 |
| DEC-013 | REQ-035 |
| DEC-014 | REQ-011 |
| DEC-015 / 033 | REQ-001, REQ-002 |
| DEC-017 | REQ-007 |
| DEC-018 / 032 | REQ-003, REQ-018 |
| DEC-020 / 021 | REQ-014, REQ-015 |
| DEC-022 | REQ-016 |
| DEC-023 | REQ-019 |
| DEC-024 | REQ-021, REQ-024 |
| DEC-025 | REQ-022 |
| DEC-026 | REQ-023 |
| DEC-027 / 028 | REQ-026, REQ-027 |
| DEC-030 | REQ-025 |
| DEC-031 | REQ-028 … REQ-033 |
| DEC-035 | REQ-003, REQ-014, REQ-026 |
| DEC-036 | REQ-036 |
| DEC-037 | REQ-037 |
| DEC-038 | REQ-038 |
| DEC-039 | REQ-039 |
| DEC-040 | REQ-002, REQ-031 |
| DEC-041 | REQ-002 |
| DEC-005 (DEFERRED) | REQ-034 (solo intención; el mapeo queda en Technical Specification) |

Cobertura de los MUST del Concept Definition: M1 → REQ-011, 034 · M2 → REQ-011, 012 · M3 → REQ-011 (emergente; se valida por MANUAL) · M4 → REQ-016, 017, 018 · M5 → REQ-019, 020 · M6 → REQ-021, 022 · M7 → REQ-014, 023 · M8 → REQ-023 · M9 → REQ-026, 027 · M10 → REQ-004, 005 · M11 → REQ-006, 007 · M12 → REQ-009.

## 15. Puntos abiertos y diferidos

### Puntos abiertos resueltos

| ID | Resolución |
|---|---|
| OP-01 | Vida limitada a 0; cada contacto simultáneo aplica 1 → DEC-036 (REQ-036) |
| OP-02 | Proyectil recto a velocidad constante → DEC-037 (REQ-037) |
| OP-03 | Los proyectiles no afectan a la nave → DEC-038 (REQ-038) |
| OP-04 | Al terminar, asteroides y proyectiles desaparecen → DEC-039 (REQ-039) |
| OP-05 | El reinicio pasa directo a la cuenta regresiva → DEC-040 (REQ-031) |
| OP-06 | Cuenta regresiva de 3 s → DEC-041 (REQ-002) |

### Puntos abiertos pendientes (necesitan confirmación del usuario para aprobar el GDD)

| ID | Punto | Impacto |
|---|---|---|
| OP-07 | Patrón de aparición: el usuario mencionó "bajar asteroides uno detrás de otro, a una misma velocidad". ¿Significa que aparecen **solo desde arriba**, lo que modificaría DEC-024 (junto a cualquier borde)? ¿Implica **un solo asteroide a la vez**, lo que fijaría el máximo simultáneo (hoy TECH-DEFERRED)? Que todos tengan la misma velocidad ya es coherente con DEC-003 y DEC-025. | REQ-021, REQ-022, TD-2 |
| OP-08 | "Nivel 1 / luego": ¿se confirma que significa *MVP / evolución futura* (dificultad progresiva, COULD) y **no** una reintroducción de niveles, que están OUT OF SCOPE? | §12, REQ-032, REQ-035 |

### Diferidos a Technical / Architecture Specification (TECH-DEFERRED)

| ID | Punto |
|---|---|
| TD-1 | Cómo se prueba el final por tiempo sin esperar minutos reales (REQ-004, REQ-005) |
| TD-2 | Velocidades (nave, proyectil, asteroides), valor de la cadencia, frecuencia de aparición, máximo de asteroides simultáneos |
| TD-3 | Determinismo de la aparición en pruebas (REQ-021) |
| TD-4 | Tamaño del área, relación de aspecto, cámara, resolución |
| TD-5 | Mapeo de intenciones a dispositivos y estrategia de input (DEC-005) |
| TD-6 | Representación y configuración de los valores de balance (N, daño, X, cuenta regresiva, duración) |
| TD-7 | Velocidad del proyectil (REQ-037) |
