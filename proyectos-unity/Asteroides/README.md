# Asteroides — Crashteroids (Unity Learn / Kodeco)

Dos proyectos Unity basados en el mismo tutorial oficial (el que ya cita `diseno-plataformas/unidad-03/README.md` como material previo de la cátedra: *"basado en el tutorial oficial de Unity Learn 'Unit Testing' (proyecto Crashteroids)"*), y también resumido en `Unidad 3 -2024.pptx` (36 diapositivas, ciclo 2024).

| Proyecto | Estado |
|---|---|
| `asteroide-starter/` | Punto de partida: el juego completo, **sin** carpeta `Tests` ni `GameAssembly.asmdef` todavía. |
| `asteroide-final/` | Resultado del tutorial ya completo, más tests agregados por la cátedra: `Assets/Tests/TestSuite.cs` (7 pruebas en Play Mode) y `Assets/Tests/IntegrationHypothesesTests.cs` (4 pruebas en Play Mode, 3 de ellas en rojo a propósito — ver más abajo). |

Cada uno tiene su propio `.gitignore` (no se versiona `Library/`, `Logs/`, `UserSettings/`, `.sln`/`.csproj`, ni `CodeCoverage/` en `asteroide-final`).

## Suite de tests (`asteroide-final/Assets/Tests/TestSuite.cs`)

Las 6 pruebas del tutorial verifican **un único efecto observable** por vez (ej. `LaserMovesUp` solo chequea que el láser suba, `NewGameRestartsGame` solo chequea `isGameOver`). Eso **no** las hace unitarias: todas cargan el prefab completo `Game`, y la mayoría depende de varios sistemas reales a la vez (Spawner, Asteroid, Ship, física, Game). La clase de Testing de integración (`diseno-plataformas/clases/2026-09-28-integracion-y-plataformas/`) las clasifica una por una y concluye que la cantidad de asserts no define el nivel de la prueba: solo `AsteroidsMoveDown` y `LaserMovesUp` quedan como casos discutibles. La séptima prueba se agregó como ejemplo explícito de un test que verifica **varios efectos de un mismo flujo** a la vez:

### `GameOverStopsSpawningAndDisablesShip` — ejemplo de test de integración

`Game.GameOver()` ([Game.cs:57-65](asteroide-final/Assets/Scripts/Game.cs#L57-L65)) coordina tres colaboradores reales al mismo tiempo: pone `isGameOver = true`, le pide al `Spawner` que deje de generar asteroides, y le pide a la `Ship` que explote. La prueba ya existente `GameOverOccursOnAsteroidCollision` también integra varios sistemas (Spawner, Asteroid, física, Game), pero solo verifica el primer efecto (el booleano).

`GameOverStopsSpawningAndDisablesShip` verifica los efectos como conjunto:

1. `game.isGameOver == true`
2. `game.GetShip().isDead == true` — **limitación conocida:** `Ship.isDead` ya vale `true` desde el inicio (en [Ship.cs:36](asteroide-final/Assets/Scripts/Ship.cs#L36) y en el prefab `Game`), y en este test nada llama a `RepairShip()`. Este assert pasaría aunque `GameOver()` no llamara a `Explode()`: no demuestra que la nave haya explotado.
3. Después del Game Over, el `Spawner` **deja de aparecer asteroides nuevos** — se cuentan los `Asteroid` vivos en la escena, se espera más del intervalo de spawn automático (0.4s), y se vuelve a contar: el número no debe crecer.

**Por qué el punto 3 importa:** se comprobó deliberadamente que rompe algo real. Se quitó por un momento la línea `spawner.StopSpawning()` de `Game.GameOver()` y se corrió la suite:

- `GameOverStopsSpawningAndDisablesShip` → **falla** (como se esperaba: el `Spawner` sigue generando asteroides).
- `GameOverOccursOnAsteroidCollision` → **sigue pasando** — el booleano `isGameOver` nunca dejó de ponerse en `true`, así que ese test no detecta nada raro. Esta es la diferencia práctica entre un test que mira un solo valor y uno que verifica que varios sistemas queden consistentes entre sí.
- Bonus inesperado: `LaserMovesUp`, un test sin relación aparente, **también empezó a fallar**. Con el spawner sin detener, el test dejó asteroides de más en la escena, y el `TearDown` de `TestSuite` solo destruye el prefab `Game`: los asteroides se instancian como objetos raíz y sobreviven al test. No se registró qué objeto exacto hizo fallar a `LaserMovesUp` ni el orden en que se ejecutaron los tests en esa corrida. Igual es un ejemplo real de por qué el aislamiento entre tests (y una limpieza de estado disciplinada) importa tanto en Play Mode.

Se revirtió el cambio inmediatamente después de confirmar esto; `TestSuite` (7/7) vuelve a pasar en el estado normal del repo.

**Riesgo conocido, no observado:** como el test cuenta *todos* los asteroides de la escena, uno que haya sobrado de otro test y caiga por debajo de y = −5 durante la espera puede alterar el conteo (falso positivo o falso negativo según el caso). La propuesta de la clase 2 es reescribirlo con una limpieza total en el `TearDown` y contando solo los asteroides que crea el propio test.

## Tests de hipótesis (`asteroide-final/Assets/Tests/IntegrationHypothesesTests.cs`)

Agregados para la clase «Testing de integración II» (`diseno-plataformas/clases/integracion-II/`). El resultado esperado de cada test describe la **intención de diseño** inferida del código, no el comportamiento actual, así que tres de los cuatro están en rojo **a propósito** porque documentan defectos reales sin corregir:

| Caso | Test | Resultado (batchmode, Unity 6000.3.11f1) |
|---|---|---|
| INT-AST-13 | `TwoLasersHitSameAsteroid_ScoreIncreasesOnce` | **Falla**: `InvalidOperationException` por doble `Release` al pool en [Laser.cs:52](asteroide-final/Assets/Scripts/Laser.cs#L52) |
| INT-AST-14 | `NewGame_RemovesLeftoverAsteroids` | **Falla**: el asteroide de la partida anterior sobrevive a `NewGame()` (`ClearAsteroids()` hace `Dispose()` de un pool que no contiene los asteroides en pantalla) |
| INT-AST-15 (línea de base) | `SingleNewGame_SpawnCountBaseline` | 5 asteroides en 2,1 s con un solo `NewGame()` |
| INT-AST-15 | `DoubleNewGame_DoesNotChangeSpawnRate` | **Falla**: 8 asteroides en 2,1 s con dos `NewGame()` seguidos (`StartCoroutine` sobre el mismo `IEnumerator`) |

INT-AST-13 y 14 comparten la causa raíz: el `ObjectPool` del `Spawner` nunca se usa con `Get()`. Esta clase de test usa un `[UnityTearDown]` que destruye también todos los `Asteroid` y `Laser` de la escena, y cada test espera un frame al comenzar para que `Start()` asigne `Game.instance`.

## Validación

Corrido en batch mode (`Unity.exe -batchmode -nographics -runTests -testPlatform PlayMode`, con el Editor cerrado):

- `TestSuite`: compilación limpia y 7/7 tests en verde.
- `IntegrationHypothesesTests`: 3 fallas esperadas (INT-AST-13, 14 y 15), que pasarán a verde cuando se corrijan los defectos y quedarán como tests de regresión.
