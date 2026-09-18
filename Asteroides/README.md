# Asteroides — Crashteroids (Unity Learn / Kodeco)

Dos proyectos Unity basados en el mismo tutorial oficial (el que ya cita `docs/unidad03/README.md` como material previo de la cátedra: *"basado en el tutorial oficial de Unity Learn 'Unit Testing' (proyecto Crashteroids)"*), y también resumido en `Unidad 3 -2024.pptx` (36 diapositivas, ciclo 2024).

| Proyecto | Estado |
|---|---|
| `asteroide-starter/` | Punto de partida: el juego completo, **sin** carpeta `Tests` ni `GameAssembly.asmdef` todavía. |
| `asteroide-final/` | Resultado del tutorial ya completo: `Assets/Tests/TestSuite.cs` con 7 pruebas en Play Mode. |

Cada uno tiene su propio `.gitignore` (no se versiona `Library/`, `Logs/`, `UserSettings/`, `.sln`/`.csproj`, ni `CodeCoverage/` en `asteroide-final`).

## Suite de tests (`asteroide-final/Assets/Tests/TestSuite.cs`)

6 de las 7 pruebas verifican **un único efecto observable** por vez (ej. `LaserMovesUp` solo chequea que el láser suba, `NewGameRestartsGame` solo chequea `isGameOver`). La séptima, agregada como ejemplo de otro nivel de testing, es distinta a propósito:

### `GameOverStopsSpawningAndDisablesShip` — ejemplo de test de integración

`Game.GameOver()` ([Game.cs:57-65](asteroide-final/Assets/Scripts/Game.cs#L57-L65)) coordina tres colaboradores reales al mismo tiempo: pone `isGameOver = true`, le pide al `Spawner` que deje de generar asteroides, y le pide a la `Ship` que explote. La prueba ya existente `GameOverOccursOnAsteroidCollision` solo mira el primer efecto (el booleano) — por eso no es realmente un test de integración, aunque use objetos reales de la escena.

`GameOverStopsSpawningAndDisablesShip` verifica los tres efectos como conjunto:

1. `game.isGameOver == true`
2. `game.GetShip().isDead == true` (la nave realmente ejecutó `Explode()`)
3. Después del Game Over, el `Spawner` **deja de aparecer asteroides nuevos** — se cuentan los `Asteroid` vivos en la escena, se espera más del intervalo de spawn automático (0.4s), y se vuelve a contar: el número no debe crecer.

**Por qué el punto 3 importa:** se comprobó deliberadamente que rompe algo real. Se quitó por un momento la línea `spawner.StopSpawning()` de `Game.GameOver()` y se corrió la suite:

- `GameOverStopsSpawningAndDisablesShip` → **falla** (como se esperaba: el `Spawner` sigue generando asteroides).
- `GameOverOccursOnAsteroidCollision` → **sigue pasando** — el booleano `isGameOver` nunca dejó de ponerse en `true`, así que ese test no detecta nada raro. Esta es la diferencia práctica entre un test que mira un solo valor y uno que verifica que varios sistemas queden consistentes entre sí.
- Bonus inesperado: `LaserMovesUp`, un test sin relación aparente, **también empezó a fallar**. El `Spawn()` que quedó corriendo sin detenerse contaminó el siguiente test de la suite con asteroides de más en la escena — un ejemplo real de por qué el aislamiento entre tests (y una limpieza de estado disciplinada) importa tanto en Play Mode.

Se revirtió el cambio inmediatamente después de confirmar esto; la suite completa (7/7) vuelve a pasar en el estado normal del repo.

## Validación

Corrido en batch mode (`Unity.exe -batchmode -nographics -runTests -testPlatform PlayMode`, con el Editor cerrado) antes de cada commit: compilación limpia y 7/7 tests en verde.
