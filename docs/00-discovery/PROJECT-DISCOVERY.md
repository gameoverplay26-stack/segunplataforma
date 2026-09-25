# PROJECT DISCOVERY — Proyecto académico de videojuego (Diseño según Plataforma)

## Objetivo del proyecto

Construir un proyecto académico pequeño, progresivo y demostrable en Unity 6000.3.11f1 LTS que permita practicar simultáneamente: diseño de videojuegos, diseño según plataforma (PC → Mobile), arquitectura básica de gameplay, Unit Testing, Integration Testing, control de versiones con Git por etapas, y Spec-Driven Development (SDD). No es un juego comercial: el criterio de éxito es la demostrabilidad pedagógica, no la riqueza de contenido.

## Contexto académico

Este proyecto es independiente de la convención `docs/unidadNN/` usada para preparar el material de clase de la cátedra "Diseño según Plataformas de Juego" (UNJu). No reemplaza ni continúa el hilo narrativo "Cryptbound" usado en esas unidades — es un proyecto propio, nuevo, que se desarrollará dentro de este mismo repositorio (`clases-en-vivo`) bajo `docs/00-discovery/` en adelante, siguiendo el flujo SDD pedido explícitamente.

Punto de partida conceptual (no copiar Brawl Stars, solo su núcleo): partidas cortas (3–5 min) + personaje controlable + objetivo claro + enemigos + recompensas + progresión.

## Alternativas analizadas

Se evaluó la idea inicial **"Arena"** más 4 alternativas, sin declarar una "mejor" — la decisión final del concepto queda a cargo del usuario.

### Arena (idea inicial)

- **Core loop:** moverse → atacar → derrotar enemigos → puntos → recoger recursos/power-ups → mejora temporal → fin de partida → recompensa.
- **Mecánica principal:** combate (potencialmente cuerpo a cuerpo y a distancia) contra múltiples enemigos en una arena.
- **Sistemas:** Input, Movimiento, Combate, Salud, IA de enemigos (varios tipos), Power-ups, Score, Timer, Recompensa.
- **Unit testing:** `Health.TakeDamage()`, cálculo de daño, `ScoreManager`, temporizador de power-ups.
- **Integration testing:** jugador ataca → enemigo recibe daño → muere → puntaje; recolección de power-up → buff temporal → expira.
- **PC vs Mobile:** movimiento + apuntado deben abstraerse; con dos formas de atacar (melee + ranged) hay dos contratos de input a separar en vez de uno.
- **Complejidad estimada:** media-alta.
- **Riesgos de alcance:** alto — combina 5+ sistemas nuevos a la vez en la primera iteración.
- **Pertinencia:** alto valor de "gancho" pero riesgo real de scope creep para un vertical slice inicial.

### Alternativa 1 — "Dodge & Shoot" (arena de proyectiles simplificada)

- **Concepto:** mismo espíritu de Arena, combate exclusivamente a distancia, un tipo de enemigo inicial.
- **Core loop:** moverse → esquivar → disparar → enemigo recibe daño → muere → puntos.
- **Mecánica principal:** disparo con cooldown + movimiento libre top-down.
- **Sistemas:** Input, Movimiento, Arma/Cooldown, Proyectil, Salud, IA mínima (persigue), Score, GameManager/Timer.
- **Unit testing:** `Health.TakeDamage()`, `Weapon.CanFire()`, `ScoreManager.AddPoints()`.
- **Integration testing:** jugador dispara → proyectil impacta → enemigo recibe daño → vida llega a cero → muerte → puntaje (coincide con el ejemplo de la consigna).
- **PC vs Mobile:** apuntado con mouse vs. joystick virtual/auto-aim; disparo con click/tecla vs. botón táctil.
- **Complejidad estimada:** baja-media.
- **Riesgos de alcance:** bajo; el riesgo es agregar variedad de armas/enemigos antes de cerrar el slice base.
- **Pertinencia:** muy alta para testing — el loop completo cabe en un flujo de integración corto y claro.

### Alternativa 2 — "Point Defense" (defensa de punto único)

- **Concepto:** el jugador coloca/mejora una torreta que dispara automáticamente contra oleadas.
- **Core loop:** recolectar recursos → colocar/mejorar defensa → sobrevivir oleada → puntos → siguiente oleada.
- **Mecánica principal:** spawner de oleadas + torreta con daño automático.
- **Sistemas:** Input (colocación, no movimiento continuo), WaveSpawner, Turret, Health (enemigo), ResourceManager, Score.
- **Unit testing:** `WaveSpawner.GetNextWaveComposition()`, `Turret.CalculateDamage()`, `ResourceManager.CanAfford()`.
- **Integration testing:** oleada spawnea → torreta detecta y dispara → enemigo pierde vida → muere → recurso/puntaje otorgado.
- **PC vs Mobile:** click-and-drag vs. tap-and-drag — es un input de selección/colocación, no de movimiento continuo; demuestra peor el patrón "joystick vs. teclado" pedido.
- **Complejidad estimada:** media (lógica de grilla/colocación).
- **Riesgos de alcance:** medio — UI de colocación y balance de oleadas pueden crecer sin límite.
- **Pertinencia:** se aleja del "personaje controlable"; sistemas muy desacoplados mutuamente, valioso como contraste pero menos alineado a la referencia dada.

### Alternativa 3 — "Capture the Zone" (control de zona)

- **Concepto:** misma base de movimiento/combate simple que Arena/Alt.1, pero la victoria se define por tiempo controlando una zona, no por bajas.
- **Core loop:** moverse a la zona → permanecer dentro → acumular puntaje por tiempo → (opcional) defenderse de disputa.
- **Mecánica principal:** trigger de zona con acumulación de puntaje mientras está ocupada.
- **Sistemas:** Input, Movimiento, ZoneController (independiente de combate), Score, Timer, (opcional) Health/Combate.
- **Unit testing:** `ZoneController.Tick()` (acumula/detiene según ocupación), `ScoreManager`.
- **Integration testing:** jugador entra a la zona → acumula → sale → deja de acumular → puntaje final correcto al fin del timer.
- **PC vs Mobile:** solo cambia el input de movimiento; la lógica de zona es 100% independiente de plataforma.
- **Complejidad estimada:** baja si el combate queda como COULD HAVE.
- **Riesgos de alcance:** bajo, salvo que se agregue combate desde el inicio (converge con Alt.1).
- **Pertinencia:** muy alta para demostrar desacople Score/Combate — valor arquitectónico que Arena y Alt.1 no obligan a resolver.

### Alternativa 4 — "Brawler Runner" (corredor con combate)

- **Concepto:** auto-scroll en carriles, el jugador cambia de carril/esquiva y ataca obstáculos/enemigos en el camino.
- **Core loop:** avance automático → cambiar de carril/esquivar → atacar → recolectar → fin de recorrido → puntaje.
- **Mecánica principal:** movimiento lateral discreto + ataque a objetivos fijos en el carril.
- **Sistemas:** Input (swipe/carril), spawner procedural de obstáculos, Combate simple, Score.
- **Unit testing:** lógica de cambio de carril, `ObstacleSpawner`, `Health` de obstáculos.
- **Integration testing:** obstáculo aparece → jugador ataca → destruido → puntaje; o colisión sin ataque → jugador pierde vida.
- **PC vs Mobile:** el diseño "nativo" es Mobile (swipe); PC pasa a ser la adaptación — invierte el orden PC-primero de la consigna sin invalidarlo.
- **Complejidad estimada:** media (generación procedural agrega una capa extra).
- **Riesgos de alcance:** medio — variar obstáculos/carriles puede crecer rápido.
- **Pertinencia:** el concepto más alejado de la referencia "Brawl Stars"; útil como contraste, menor conexión directa con la idea original.

## Comparación técnica (matriz)

Escala 1–5, más alto = más favorable / menor riesgo en todos los criterios (incluido "Riesgo técnico", donde 5 = riesgo más bajo).

| Criterio | Arena | Alt.1 Dodge&Shoot | Alt.2 Point Defense | Alt.3 Capture Zone | Alt.4 Brawler Runner |
|---|---:|---:|---:|---:|---:|
| Alcance controlable | 2 | 4 | 3 | 3 | 3 |
| Facilidad de implementación | 2 | 4 | 3 | 3 | 3 |
| Unit Testing | 3 | 5 | 4 | 4 | 3 |
| Integration Testing | 3 | 5 | 3 | 4 | 3 |
| Diseño PC/Mobile | 3 | 4 | 2 | 4 | 5 |
| Separación Input/GameLogic | 3 | 4 | 3 | 4 | 4 |
| Posibilidad de regresión (didáctica) | 4 | 4 | 3 | 4 | 3 |
| Valor académico | 4 | 5 | 3 | 4 | 2 |
| Riesgo técnico (5=más bajo) | 2 | 4 | 3 | 3 | 3 |

No se declara un "ganador". Fortalezas, debilidades, riesgos y dependencias de cada concepto están detallados en la sección anterior, por concepto.

## Concepto provisional

Ninguno fue seleccionado todavía. "Arena" sigue siendo la semilla conceptual (referencia de Brawl Stars: partidas cortas, personaje controlable, enemigos, recompensas, progresión), pero las 4 alternativas están abiertas para elección consciente. **Esta decisión queda exclusivamente a cargo del usuario.**

## Decisiones pendientes (requieren aprobación del usuario)

1. Selección del concepto final (Arena / Alt.1 / Alt.2 / Alt.3 / Alt.4, o una combinación acotada — ej. Alt.1 + Alt.3 con zona como variante de modo de juego).
2. Si el concepto elegido incluye combate cuerpo a cuerpo, a distancia, o ambos (afecta directamente cuántos contratos de Input hay que abstraer).
3. Cantidad de tipos de enemigo para el vertical slice inicial (1 vs. 2+).
4. Si el combate es MUST HAVE u opcional/COULD HAVE en conceptos donde no es el núcleo (Alt.3).
5. Estrategia de Input System de Unity a usar en la Architecture Specification (Input System nuevo con Action Maps/Control Schemes vs. interfaz propia `IPlayerInputSource` inyectada) — no se decide en esta fase.
6. Alcance real de "power-ups"/progresión para el MVP (¿MUST HAVE o SHOULD HAVE?).
7. Uso de tags de Git por etapa vs. ramas por etapa (ver Estrategia Git) — recomendación dada, confirmación pendiente.

## Riesgos identificados

- **Scope creep:** cualquier concepto puede crecer si se agregan mecánicas antes de cerrar el vertical slice base (mayor en Arena, menor en Alt.1/Alt.3).
- **Sobrearquitectura temprana:** definir capas/interfaces antes de tener claro el concepto final puede generar abstracciones innecesarias — por eso la Architecture Specification es una etapa separada, posterior a la selección de concepto.
- **Desalineación testing-diseño:** si el concepto final no separa claramente lógica pura (testeable por Unit Test) de comportamiento dependiente de Unity (MonoBehaviour/física/colisiones), el valor pedagógico de Unit Testing baja.
- **Confusión de input entre plataformas:** si no se define un contrato de input único desde la Technical/Architecture Specification, la adaptación PC→Mobile obligará a duplicar lógica de gameplay (justo lo que el proyecto busca evitar demostrar).

## Alcance preliminar (MoSCoW, a nivel de plantilla — se completa recién al fijar el concepto)

El GDD mínimo (sección "Concept / Gameplay / Scope") se definirá en la etapa **Concept Definition + GDD**, posterior a esta. Como criterio transversal ya acordado para cualquier concepto elegido, quedan explícitamente fuera de alcance (**OUT OF SCOPE**) desde ahora:

- Multiplayer real, servidores, matchmaking, backend.
- Monetización y tienda real.
- Decenas/cientos de personajes o contenido generado por usuarios.
- Cualquier sistema no necesario para demostrar el objetivo académico (SDD + testing + diseño por plataforma).

## Estrategia SDD (Spec-Driven Development)

Secuencia acordada: `Idea → Concept Definition → Game Design Specification → Technical Specification → Architecture Specification → Test Strategy → Implementation → Verification → Integration Testing → Platform Adaptation → Regression Testing`.

| Etapa | Objetivo | Alcance | Entradas | Entregables | Criterios de aceptación | Evidencia esperada | Estado | Riesgos | Decisiones pendientes |
|---|---|---|---|---|---|---|---|---|---|
| Idea | Plantear la semilla conceptual | Referencia conceptual únicamente | Brief del usuario | Enunciado de idea | Idea articulable en 1 párrafo | Este documento | **Completo** | — | — |
| Discovery (esta fase) | Evaluar alternativas y decidir criterios | Comparación técnica, sin código | Idea | `PROJECT-DISCOVERY.md` | Alternativas + matriz + checkpoint aprobado por el usuario | Este documento | **Completo, pendiente de revisión del usuario** | Ver "Riesgos" | Ver "Decisiones pendientes" |
| Concept Definition | Fijar el concepto elegido | 1 concepto, sin detalle de sistemas | Este documento + elección del usuario | `docs/01-concept/*` | Concepto aprobado por escrito | Documento de concepto | Pendiente | Elegir mal por presión de tiempo | Selección de concepto (#1) |
| Game Design Specification (GDD mínimo) | Definir gameplay y alcance MoSCoW | Concept + Gameplay + Scope | Concept Definition | `docs/02-gdd/*` | GDD mínimo completo y acotado | GDD aprobado | Pendiente | Alcance demasiado amplio | #2, #3, #4, #6 |
| Technical Specification | Traducir GDD a requerimientos técnicos | Sistemas, datos, plataformas objetivo | GDD | `docs/03-technical-design/*` | Requisitos técnicos verificables | Documento técnico | Pendiente | Definir de más antes de tiempo | #5 |
| Architecture Specification | Definir componentes, interfaces, eventos | Arquitectura conceptual → concreta | Technical Spec | `docs/04-architecture/*` | Arquitectura validada contra puntos de testing | Diagrama + documento | Pendiente | Sobrearquitectura | #5 |
| Test Strategy | Definir qué se prueba y cómo | Unit + Integration, sin bugs aún | Architecture Spec | `docs/05-testing/*` | Casos de unit/integration listados por sistema | Documento de estrategia | Pendiente | Cobertura desalineada con arquitectura | — |
| Implementation | Construir el vertical slice | Código Unity según specs previas | Todas las specs anteriores | Proyecto Unity funcional | Cumple GDD MUST HAVE | Build + repo | Pendiente | Desviarse de la spec sin registrarlo | — |
| Verification | Validar unit tests contra implementación | Unit Tests | Implementation | Suite de Unit Tests en verde | Cobertura de los puntos definidos en Test Strategy | Reporte de test runner | Pendiente | Tests que no reflejan casos reales | — |
| Integration Testing | Validar flujos completos | Integration Tests | Verification | Suite de Integration Tests en verde | Flujos end-to-end pasan | Reporte de test runner | Pendiente | Flujos no identificados a tiempo | — |
| Platform Adaptation | Adaptar input a Mobile sin duplicar gameplay | Input Mobile (joystick/touch) | Integration Testing | Build Mobile funcional | Mismo gameplay, distinto input, sin duplicar lógica | Build + demo | Pendiente | Duplicación de lógica de gameplay | — |
| Regression Testing | Introducir bugs controlados y detectarlos con la suite existente | Bugs intencionales (ver sección) | Platform Adaptation | Reporte de regresión | Cada bug es detectado por al menos un test ya existente | Reporte de test runner antes/después | Pendiente | Bugs mal calibrados (muy obvios o muy sutiles) | — |

## Estructura documental `docs/` propuesta

```text
docs/
├── 00-discovery/        # Este documento. Evaluación de alternativas, matriz, decisiones abiertas.
├── 01-concept/          # Concepto elegido, justificación de la elección, referencia conceptual acotada.
├── 02-gdd/              # GDD mínimo viable: Concept, Gameplay, Scope (MoSCoW).
├── 03-technical-design/ # Requisitos técnicos: versión de Unity, paquetes, restricciones de plataforma.
├── 04-architecture/     # Componentes, responsabilidades, dependencias, interfaces, eventos, diagrama.
├── 05-testing/          # Estrategia de Unit/Integration Testing por sistema, antes de implementar.
├── 06-platform/         # Estrategia de separación de Input PC/Mobile y su adaptación.
├── 07-implementation/   # Notas de implementación, desvíos registrados respecto a las specs.
└── 08-validation/       # Resultados de Verification, Integration Testing y Regression Testing (bugs + detección).
```

No se crean todavía los archivos de `01-concept/` en adelante — se generan al avanzar de etapa, cada uno con la especificación correspondiente ya aprobada.

## Arquitectura conceptual (no definitiva — se cierra en Architecture Specification)

Aplica a los conceptos con movimiento + combate directo (Arena, Alt.1, Alt.3; Alt.2 y Alt.4 requerirían variantes no detalladas aquí):

```text
PC Input Provider  \
                     → IPlayerInputSource → PlayerController → Weapon → Projectile → Health → (OnDeath) → ScoreManager
Mobile Input Provider /                                  ↑                                      ↓
                                                      EnemyAI (targeting) ←――――――――――― GameManager (timer, victoria/derrota)
```

- **Input (PC/Mobile):** MonoBehaviours delgados que traducen entrada cruda (teclado/mouse o joystick virtual/touch) a un contrato común `IPlayerInputSource` (dirección de movimiento, dirección de apuntado, disparo/ataque presionado). Dependencia: ninguna hacia gameplay.
- **PlayerController (MonoBehaviour):** consume `IPlayerInputSource`, mueve al jugador y ordena disparo al Weapon. Depende de Input contract + Weapon + Health propio.
- **Weapon:** lógica de cooldown/daño idealmente en una clase C# pura (`Weapon.CanFire()`, `Weapon.Fire()`), envuelta por un MonoBehaviour que instancia el prefab de Projectile.
- **Projectile (MonoBehaviour):** al colisionar, llama a `Health.TakeDamage(amount)` del objetivo. La trayectoria puede aislarse en una clase pura para test de movimiento/tiempo de vida.
- **Health:** clase C# pura (`TakeDamage`, `CurrentHealth`, evento `OnDeath`), sin dependencia de Unity — el punto de Unit Testing más directo y valioso del proyecto.
- **EnemyAI (MonoBehaviour):** reacciona a `OnDeath` propio; la lógica de targeting (dado posiciones, elegir dirección) puede aislarse en una clase pura testeable sin instanciar GameObjects.
- **ScoreManager:** clase C#/MonoBehaviour simple que se suscribe a `OnDeath` (o a eventos de Zone en Alt.3) y expone `AddPoints()`/`CurrentScore`. Completamente unit-testeable.
- **GameManager/MatchController (MonoBehaviour):** dueño del timer y de la condición de victoria/derrota; principal superficie de Integration Testing.

**Eventos:** `OnDeath` (Health) → `OnEnemyDefeated` (Enemy→ScoreManager) → `OnScoreChanged` (ScoreManager→UI) → `OnMatchEnded` (GameManager).

**Puntos de Unit Testing:** `Health`, `Weapon` (cooldown/daño), `ScoreManager`, `ProjectileMotion` (si se aísla), `TargetingLogic` (si se aísla).

**Puntos de Integration Testing (flujos candidatos):**
1. Jugador dispara → Proyectil impacta → Enemy.Health baja → `OnDeath` → ScoreManager incrementa.
2. Enemigo ataca → Player.Health baja → jugador muere → GameManager bloquea input / termina partida.
3. (Si se elige Alt.3) Jugador entra a la zona → ZoneController acumula → jugador sale → deja de acumular → puntaje final correcto.
4. Timer llega a cero → GameManager compara puntajes → declara resultado → dispara recompensa/pantalla final.

## Testing desde el diseño

Ya cubierto arriba (puntos de Unit/Integration Testing). Se formalizará con casos concretos en la etapa **Test Strategy**, una vez fijada la arquitectura definitiva.

## Bugs intencionales candidatos (NO se introducen todavía)

| ID | Defecto | Componente | Test que debería detectarlo | Comportamiento esperado a especificar |
|---|---|---|---|---|
| BUG-CAND-01 | Enemigo recibe daño pero no muere | Health | Unit: `Health.TakeDamage_WhenDamageExceedsCurrentHealth_TriggersDeathEvent` | `OnDeath` debe dispararse exactamente una vez al cruzar 0 de vida |
| BUG-CAND-02 | Enemigo muere pero no otorga score | Enemy ↔ ScoreManager | Integration: flujo Weapon→Projectile→Enemy→Health→Death→Score | Cada muerte de enemigo incrementa el score en un valor específico, una sola vez |
| BUG-CAND-03 | Proyectil impacta pero no aplica daño | Projectile | Unit/Integration: `Projectile.OnHit_WhenTargetHasHealth_CallsTakeDamage` | Todo objetivo con Health impactado recibe exactamente el daño configurado |
| BUG-CAND-04 | Jugador puede atacar/moverse después de morir | PlayerController ↔ Health | Unit: `PlayerController.Attack_WhenDead_IsIgnored` | Ninguna acción de gameplay se ejecuta una vez que Health del jugador llega a 0 |
| BUG-CAND-05 | Doble conteo de score por el mismo enemigo | Health/Enemy lifecycle | Integration: verificar incremento único de score por instancia de enemigo | `OnDeath` se dispara una única vez por instancia, sin importar cuántos colliders tenga |
| BUG-CAND-06 (solo si se elige Alt.3) | La zona sigue sumando puntos aunque el jugador la abandonó | ZoneController | Unit: `ZoneController.Tick_WhenPlayerExited_StopsAccruing` | La acumulación se detiene inmediatamente al detectar salida de la zona |

## Estrategia multiplataforma (PC → Mobile)

```text
PC Input (Keyboard + Mouse)      \
                                   → Player Input (IPlayerInputSource) → Gameplay (independiente de plataforma)
Mobile Input (Virtual Joystick + Touch) /
```

El contrato `IPlayerInputSource` (o equivalente vía Action Maps/Control Schemes del Input System de Unity) es lo único que cambia entre plataformas; `PlayerController`, `Weapon`, `Health`, `ScoreManager`, `GameManager` no deben conocer de dónde viene el input. Esta separación se decide en detalle (interfaz propia vs. Input System nativo) en la **Architecture Specification**, no ahora.

## Estrategia Git

Evaluación de opciones:

- **Una rama por etapa (`etapa-00-concepto`, `etapa-01-gdd`, ...) de larga duración:** genera sprawl de ramas y no refleja que las etapas son secuenciales, no variantes paralelas — evitar, la consigna pide explícitamente no generar ramas innecesarias.
- **Tags por hito de etapa sobre una rama principal (trunk-based), con ramas cortas solo para trabajo en curso:** refleja mejor la naturaleza secuencial del SDD, es coherente con el patrón ya usado en este repo (ramas cortas tipo `activity-*` que se integran a `main`), y dota a cada etapa completada de un punto de referencia inmutable (`git tag etapa-00-discovery-complete`).
- **GitHub Releases:** opcional, solo si se quiere distribuir builds descargables por etapa — no es necesario para el objetivo académico, queda como COULD HAVE.

**Recomendación:** trunk-based (rama principal + ramas cortas de trabajo que se mergean) + un tag por etapa SDD completada. No crear una rama de larga duración por etapa. Confirmación pendiente del usuario (decisión #7).

## Próximos pasos

Revisión de este documento por el usuario → resolución de las decisiones pendientes (especialmente #1: selección de concepto) → avanzar a **Concept Definition + GDD Specification**.

---

```text
STATUS: DISCOVERY COMPLETE

CODE CHANGES: NONE

UNITY SCENES CHANGED: NONE

PACKAGES CHANGED: NONE

DECISIONS REQUIRING USER APPROVAL:
- Selección del concepto final (Arena / Alt.1 Dodge&Shoot / Alt.2 Point Defense / Alt.3 Capture Zone / Alt.4 Brawler Runner, o combinación acotada)
- Alcance de combate (melee / ranged / ambos) y cantidad de tipos de enemigo para el vertical slice
- Estrategia de Input System (interfaz propia vs. Input System nativo con Action Maps) — se define en Architecture Specification
- Estrategia Git: confirmar trunk-based + tags por etapa (en lugar de una rama por etapa)

NEXT AUTHORIZED STEP:
Concept selection + GDD specification
```
