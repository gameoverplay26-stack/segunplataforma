# Unidad: Testing de Integración

**Materia:** Diseño según Plataformas de Juego · FI – UNJu · 2026
**Tipo de documento:** consolidación del trabajo realizado hasta el 02/10/2026. Material de referencia para diseñar más adelante el trabajo práctico de la unidad. **No es material de clase ni consigna.**
**Proyecto guía:** nave + asteroides (Crashteroids, tutorial de Kodeco / Unity Learn), en [`proyectos-unity/Asteroides/asteroide-final/`](../../proyectos-unity/Asteroides/asteroide-final/).

## Cómo leer este documento

Cada afirmación lleva una etiqueta:

| Etiqueta | Significado |
|---|---|
| **[CONCEPTO]** | Concepto que figura en el material de clase (diapositivas y notas del docente). *Que figure en el material no garantiza que se haya dictado tal cual ni que los estudiantes lo hayan incorporado:* eso no está registrado en el repositorio. |
| **[APLICADO]** | Existe en el código o en los tests del proyecto. |
| **[VERIFICADO]** | Hay evidencia de ejecución (corrida en Unity documentada en un commit, en el README o en las notas) o se comprobó leyendo los archivos del proyecto (prefabs, `manifest.json`, reportes). Se indica cuál de los dos casos. |
| **[PROPUESTO]** | Se diseñó o sugirió en clase, pero no existe en el proyecto o no se ejecutó. |
| **[UNKNOWN]** | No hay evidencia suficiente para afirmarlo ni para descartarlo. |

**Para hacer esta consolidación no se ejecutó nada.** Las evidencias de ejecución que se citan vienen de los commits, del README y de las notas del docente. Lo que se encontró leyendo código y archivos durante la consolidación se marca como *detectado al consolidar*.

### Fuentes revisadas

| Fuente | Contenido |
|---|---|
| [`diseno-plataformas/clases/2026-09-28-integracion-y-plataformas/clase28092026.md`](2026-09-28-integracion-y-plataformas/clase28092026.md) | Plan original (borrador) de la clase 1. Las diapositivas corrigieron varios puntos de este plan (ver §2). |
| [`diseno-plataformas/clases/2026-09-28-integracion-y-plataformas/build_decks.py`](2026-09-28-integracion-y-plataformas/build_decks.py) → `Clase1-Testing-Integracion.pptx` | Clase 1 «Testing de integración en videojuegos»: 18 diapositivas con notas del docente. |
| [`diseno-plataformas/clases/integracion-II/build_deck.py`](integracion-II/build_deck.py) + [`notas.py`](integracion-II/notas.py) → `Testing-Integracion-II.pptx` | Clase 2 «Testing de integración II»: 27 diapositivas con notas del docente. |
| [`proyectos-unity/Asteroides/README.md`](../../proyectos-unity/Asteroides/README.md) | Documentación del proyecto y de la prueba de regresión hecha con el test 04. |
| [`TestSuite.cs`](../../proyectos-unity/Asteroides/asteroide-final/Assets/Tests/TestSuite.cs) | Los 7 tests originales (6 del tutorial + 1 agregado). |
| [`IntegrationHypothesesTests.cs`](../../proyectos-unity/Asteroides/asteroide-final/Assets/Tests/IntegrationHypothesesTests.cs) | 4 tests agregados para la clase 2 (INT-AST-13, 14 y 15). |
| `Assets/Scripts/*.cs`, `Resources/Prefabs/Game.prefab`, `Prefabs/Asteroid*.prefab`, `Packages/manifest.json` | Código y configuración del juego. |
| `CodeCoverage/` (no versionado, ver `.gitignore`) | Reportes de cobertura presentes en disco. |
| Commits `7f7315f`, `2865316`, `e582629`, `b20b0ae`, `af3e79e`, `7a9885d` | Historial y mensajes de commit con evidencia de las ejecuciones. |

Las diapositivas `.pptx` coinciden con sus generadores: 18 y 27 diapositivas, y se encontraron los mismos textos clave. Las imágenes figuran como espacios reservados: los `.pptx` no tienen archivos de imagen incrustados.

> **Números de línea:** todas las referencias a `Assets/Scripts/*.cs` usan la numeración real del archivo. Los scripts del proyecto tienen 29 líneas de licencia al comienzo, así que, por ejemplo, `Game.GameOver()` está en `Game.cs` 57–65. Las diapositivas usan la misma numeración.

---

## 1. Objetivo de la unidad

**[CONCEPTO]** Según las diapositivas, los objetivos de las dos clases son:

**Clase 1 — Testing de integración en videojuegos** (Unidades I–III, 120 min):
- Diferenciar los **niveles** de prueba (unitario, integración, sistema, aceptación) y reconocer el **tipo** funcional como un eje independiente.
- Identificar los sistemas de un juego que deben probarse en conjunto.
- Diseñar casos de prueba de integración, incluido un caso de valor frontera.
- Ejecutar una prueba de integración en Unity, automatizada o manual documentada.
- Registrar un defecto con un ticket completo.
- Reconocer qué **no** detecta una prueba de integración.

**Clase 2 — Testing de integración II** («De 7 tests a una estrategia»):
- Diseñar casos de integración positivos, negativos y de borde para un flujo de juego.
- Preparar fixtures y datos de prueba que aíslen cada test.
- Reconocer las causas de un test frágil (*flaky*) y corregirlas.
- Elegir qué dependencias usar reales y cuáles reemplazar por dobles de prueba.
- Interpretar un reporte de cobertura sin sobreestimarlo.
- Organizar una mini-suite de integración priorizada.

**[UNKNOWN]** No hay registro en el repositorio de cómo se dictaron las clases. No se sabe si se cumplió la agenda, qué produjeron los grupos ni qué respondieron en los tickets de salida.

---

## 2. Conceptos trabajados

Todos son **[CONCEPTO]** (figuran en las diapositivas o en las notas del docente).

### Clase 1

| Concepto | Formulación en el material |
|---|---|
| Problema motivador | MissingNo. (Pokémon Rojo/Azul): dos sistemas que funcionan por separado producen un Pokémon inexistente al interactuar. «Ninguna prueba de una sola pieza lo habría encontrado». |
| Niveles vs. tipos | Dos ejes distintos. **Niveles** (alcance): unitario, integración, sistema, aceptación. **Tipos** (aspecto): funcional / no funcional. *Manual / automatizado* tampoco es un nivel: es una forma de ejecución. |
| Corrección al borrador | El plan original ([`clase28092026.md`](2026-09-28-integracion-y-plataformas/clase28092026.md)) ponía «Funcional» como un nivel entre integración y sistema; las diapositivas lo corrigen: es un tipo de prueba. También agregan el nivel *Aceptación*. |
| Integración | Verificar las **costuras** (*seams*) entre componentes: cada flecha entre sistemas es una interfaz (un método llamado, un dato que cruza, una condición inicial). |
| Contratos invisibles | Dependencias implícitas que no están escritas en ninguna interfaz: nombres, tags, layers, orden de escenas. Ejemplo del proyecto: `Asteroid` reconoce a la nave por el nombre `"ShipModel"`. |
| Play Mode ≠ integración | Edit Mode / Play Mode = **dónde** corre el test. Unitario / integración = **qué alcance** tiene. «Una clase aislada probada en Play Mode sigue siendo una prueba unitaria». |
| Diseño de casos | Ficha con ID, nombre, precondiciones, datos, pasos, resultado esperado **verificable** («barra = 75/100», no «la barra se actualiza»), resultado obtenido y estado Pasado / Fallido. Incluye un caso de **valor frontera** (daño 100 y 99). |
| Límites del test | Falso negativo (el test pasa aunque haya un defecto) y falso positivo (el test falla sin que haya un defecto), según la Unidad I. «Una suite en verde no demuestra que no haya defectos». |
| ¿Automatizar o no? | Se automatiza lo repetitivo y verificable por código; se hace prueba manual documentada de lo visual, de los flujos largos y de la primera exploración. «Una prueba de integración manual y documentada sigue siendo una prueba de integración». |
| Puente al ticket | De la falla al ticket: título, pasos, esperado / actual, severidad ≠ prioridad, entorno, evidencia. Se trata brevemente y remite a la Unidad II. |

### Clase 2

| Concepto | Formulación en el material |
|---|---|
| Casos positivos, negativos y de borde | Analogía de una puerta con cerradura. «Negativo ≠ test que falla: el test pasa si el sistema ignora correctamente la entrada». |
| Cinco dimensiones del borde en integración | Valor / posición · Tiempo · Cantidad / simultaneidad · Repetición · Orden. |
| El resultado esperado lo decide el diseño | «Algunos bordes no tienen un resultado esperado obvio: lo decide el diseño, no quien prueba». Esas filas se marcan con ⚠ y se registran como preguntas. |
| Ficha de 8 campos | Objetivo · Componentes · Entrada · Precondiciones · Pasos · Resultado esperado · Bug que detecta · ¿Por qué integración? |
| Fixture | «El estado conocido del que parte cada test (SetUp) y la limpieza al terminar (TearDown)». Su objetivo es el aislamiento: cada test tiene que poder correr solo y en cualquier orden con el mismo resultado. |
| Datos de prueba reproducibles | Si hay azar, se controla con una semilla. |
| Test frágil (*flaky*) | «Pasa o falla sin que cambie el código». Causas (Martin Fowler, «Eradicating Non-Determinism in Tests»): tiempo, estado compartido, orden, azar, física y recursos externos. |
| Esperar por condición | Esperar a que se cumpla una condición, con un tiempo máximo, en lugar de una espera fija. Para la física, la unidad de espera es `WaitForFixedUpdate`. |
| `== null` en Unity | Un objeto destruido no es `null` para C#, pero `== null` devuelve `true` por la sobrecarga de `UnityEngine.Object`. El `Assert.IsNull` de NUnit puede no detectarlo; por eso se usa `Assert.IsTrue(obj == null)`. |
| Causa raíz vs. síntoma | «¿Falla el juego o falla el test?». Antes de levantar un ticket hay que descartar que el test esté mal armado. |
| Dobles de prueba | Dummy, Stub, Spy, Mock y Fake (Meszaros / Fowler). «En integración, lo que está en la costura bajo prueba va REAL; se reemplaza lo no determinista o lo que queda fuera de alcance». |
| Testeabilidad y entrada | Una regla mezclada con la lectura del teclado no se puede probar sin simular el dispositivo. Separar la entrada crea una costura donde enchufar un stub. |
| Cobertura | «La cobertura dice qué se ejecutó, no qué se verificó». Cobertura de líneas ≠ cobertura de ramas. Hay que saber de qué corrida viene un reporte. |
| Regresión | Primero se ve el test en **rojo** con el defecto presente; después del arreglo pasa a **verde** y queda en la suite vigilando. Retesting ≠ regresión (Unidad II). |
| Organización de la suite | Categorías Smoke · Integración · Borde · Regresión. Se etiquetan con `[Category("Smoke")]`. Convención de nombres `Flujo_Condición_Resultado`. |

---

## 3. Unit Testing vs Integration Testing

### Diferencias conceptuales — [CONCEPTO]

| | Prueba unitaria | Prueba de integración |
|---|---|---|
| Qué verifica | Un comportamiento de **una** unidad aislada | La comunicación entre dos o más componentes (las costuras) |
| Ejemplo del material | `PlayerHealth`: vida 100 → `TakeDamage(25)` → 75 | Láser choca asteroide → `Laser` avisa a `Game` → `score` +1 → HUD |
| Propiedades | Rápida, determinista, fácil de diagnosticar | Depende de escena, física, frames y estado: más lenta y más expuesta a la fragilidad |
| Qué no ve | Cómo se conecta la unidad con las demás | Lo que ningún assert comprueba (por ejemplo, el HUD) y los casos que nadie escribió |

Del material: «La prueba unitaria verifica piezas; la de integración verifica las costuras». «La cantidad de asserts no define el nivel». «Play Mode no define el nivel de la prueba».

### Diferencia entre fixture de integración y fixture unitaria en el repositorio — [APLICADO] + [VERIFICADO por lectura]

| | Unitario — `PlayerHealthTests` (Unidad III, [`Unidad03-TestingUnity`](../../proyectos-unity/Unidad03-TestingUnity/Assets/_Project/Tests/EditMode/PlayerHealthTests.cs)) | Integración — `TestSuite` / `IntegrationHypothesesTests` (Asteroides) |
|---|---|---|
| Modo | Edit Mode, `[Test]` sincrónico | Play Mode, en su mayoría `[UnityTest]` (corrutina) |
| Preparación | `new PlayerHealth(maxHealth: 100)`: una clase C# pura, sin escena | `Object.Instantiate(Resources.Load<GameObject>("Prefabs/Game"))`: prefab completo con cámara, EventSystem, UI, `Ship`, `Spawner` y la plantilla del láser |
| Ciclo de vida de Unity | No interviene | `Start()` corre en el frame siguiente a `Instantiate`; `Destroy()` se completa al final del frame; las colisiones ocurren en `FixedUpdate` |
| Estado global | Ninguno | `Game.instance` (estático), objetos raíz que sobreviven al test, `Random` sin semilla |
| Limpieza necesaria | Ninguna (el GC se encarga) | Destruir el prefab **y** todo lo que el test creó fuera de él, y esperar un frame |
| Esperas | No hay | `WaitForSeconds`, `WaitForFixedUpdate`, `yield return null` |

---

## 4. Proyecto utilizado: Nave + Asteroides

**[APLICADO] [VERIFICADO por lectura]**

- Hay dos proyectos ([`proyectos-unity/Asteroides/README.md`](../../proyectos-unity/Asteroides/README.md)): `asteroide-starter/` (sin tests) y `asteroide-final/` (con tests). Todo el trabajo de integración se hizo sobre **`asteroide-final`**.
- Unity **6000.3.11f1**. Paquetes: `com.unity.test-framework` **1.6.0** y `com.unity.testtools.codecoverage` **1.3.0**. **No** incluye `com.unity.inputsystem`, verificado en `Packages/manifest.json`.
- Assemblies: `GameAssembly` (`Assets/Scripts/GameAssembly.asmdef`) y `Tests` (`Assets/Tests/Tests.asmdef`, que referencia `GameAssembly`, `UnityEngine.TestRunner`, `UnityEditor.TestRunner` y `nunit.framework.dll`, con la restricción `UNITY_INCLUDE_TESTS`).
- Licencia: el código es de Kodeco. Las diapositivas citan el código por archivo y línea, sin copiarlo. Los fragmentos de código de las diapositivas son propios de la cátedra.
- Por qué se eligió: en las notas, es «el hilo conductor» de las dos clases. Es el proyecto que la cátedra ya usaba en la Unidad III (2024).

---

## 5. Componentes involucrados

**[APLICADO] [VERIFICADO por lectura]** de `Assets/Scripts/` y `Resources/Prefabs/Game.prefab`.

| Componente | Responsabilidad | Puntos de contacto relevantes para integración |
|---|---|---|
| `Game` ([Game.cs](../../proyectos-unity/Asteroides/asteroide-final/Assets/Scripts/Game.cs)) | Coordina la partida: puntaje, Game Over, nueva partida, UI | `private static Game instance` (46), asignado en `Start()` (50). `static GameOver()` (57–65): UI, `isGameOver = true`, `spawner.StopSpawning()` (62), `Ship.Explode()` (63), `gameOverText` (64). `NewGame()` (67–80): `BeginSpawning()` (76), `RepairShip()` (77), `ClearAsteroids()` (78). `static AsteroidDestroyed()` (82–86): `score++` y texto del HUD (85). |
| `Spawner` ([Spawner.cs](../../proyectos-unity/Asteroides/asteroide-final/Assets/Scripts/Spawner.cs)) | Genera asteroides | `ObjectPool<GameObject> asteroids` creado en `Awake` (52–53). `spawnRoutine = Spawn()` se crea **una sola vez** (56). `BeginSpawning()` hace `StartCoroutine(spawnRoutine)` (59–62). `Spawn()` crea un asteroide cada 0,4 s (64–71). `SpawnAsteroid()` usa `Random.Range(1,5)` para elegir el prefab (75) e `Instantiate` **sin padre** (73–99), sin pasar por el pool. `SetPosition` usa una X aleatoria en [−8, 8] (103). `ClearAsteroids()` hace `asteroids.Dispose()` (114–117). `StopSpawning()` (119–122). |
| `Asteroid` ([Asteroid.cs](../../proyectos-unity/Asteroides/asteroide-final/Assets/Scripts/Asteroid.cs)) | Cae y detecta el choque con la nave | Se destruye si `y < −5` (estricto, 46–48). En `OnCollisionEnter`, compara `collision.gameObject.name == "ShipModel"` (54) y llama a `Game.GameOver()` (56). |
| `Laser` ([Laser.cs](../../proyectos-unity/Asteroides/asteroide-final/Assets/Scripts/Laser.cs)) | Sube y destruye asteroides | Se destruye si `y > 10` (40–42). En `OnCollisionEnter`, filtra con `GetComponent<Asteroid>()` (48), llama a `Game.AsteroidDestroyed()` (50), hace `spawner.asteroids.Release(...)` (52) y `Destroy` (53). |
| `Ship` ([Ship.cs](../../proyectos-unity/Asteroides/asteroide-final/Assets/Scripts/Ship.cs)) | Movimiento, disparo, explosión | `isDead` arranca en `true` (en el código y en el prefab: `isDead: 1`). `Update` sale enseguida si está muerta (57). La regla `canShoot` se evalúa junto a `Input.GetKey(Space)` (61). `ShootLaser()` (77–80) **no** chequea `canShoot`. Cooldown de 0,4 s (82–90). `SpawnLaser()` usa `Instantiate` sin padre (92–97). `Explode()` / `RepairShip()`. |

**Jerarquía del prefab `Game`** ([VERIFICADO por lectura] en `Game.prefab`): contiene Main Camera, Directional Light, EventSystem, canvas de UI, `Ship` → `ShipModel`, `Spawner` y una plantilla **inactiva** `Laser`. Las plantillas de asteroide son prefabs externos (`Prefabs/Asteroid.prefab`, `Asteroid2`, `Asteroid3`, `Asteroid4`), con velocidades de 6, 8, 7 y 9.

**Consecuencia para los tests:** `Destroy(game.gameObject)` destruye `Ship` y `Spawner` (y detiene sus corrutinas), pero **no** los asteroides ni los láseres instanciados, que quedan como objetos raíz de la escena.

**Física** ([VERIFICADO por lectura] en los prefabs): los asteroides y el láser tienen `Rigidbody` dinámico sin gravedad y `BoxCollider` que no es trigger. Por eso los choques generan `OnCollisionEnter`.

### Flujos de integración identificados — [CONCEPTO] + [APLICADO]

| Flujo | Cadena | Usado en |
|---|---|---|
| A · Láser → puntaje | Láser choca asteroide → `Laser.OnCollisionEnter` → `Game.AsteroidDestroyed` → `score` → HUD | Clase 1 (diagrama de costuras), tests 06, 07, INT-AST-13 |
| B · Choque → Game Over | Asteroide choca `ShipModel` → `Game.GameOver` → `Spawner.StopSpawning` + `Ship.Explode` + UI | Clase 1 (contrato invisible), tests 02, 04 |
| C · Game Over → nueva partida | `NewGame` → `BeginSpawning` + `RepairShip` + `ClearAsteroids` + UI | Tests 03, INT-AST-14, INT-AST-15 |

---

## 6. Tests de integración existentes

En total hay **11 métodos de test** en `Assets/Tests/`: los **7** de [`TestSuite.cs`](../../proyectos-unity/Asteroides/asteroide-final/Assets/Tests/TestSuite.cs) (los que el material llama «la suite actual», numerados 01–07 en la clase 2) más los **4** de [`IntegrationHypothesesTests.cs`](../../proyectos-unity/Asteroides/asteroide-final/Assets/Tests/IntegrationHypothesesTests.cs), agregados el 28–29/09.

Todos son de Play Mode. Las dos clases de test usan el mismo `Setup` (instanciar el prefab `Game`). Los TearDown son **distintos** (ver §8).

**Clasificación de la Clase 1 [CONCEPTO]:** los grupos clasificaban los 7 tests. La resolución docente concluye que casi todos son de integración y que el comentario de `TestSuite.cs` 82–87 («solo uno es de integración») **es impreciso**.

### Test 01 · `AsteroidsMoveDown` — `TestSuite.cs` 53–61

- **Valida:** un asteroide creado con `SpawnAsteroid()` baja después de 0,1 s (`Assert.Less(y, yInicial)`).
- **Componentes:** `Spawner`, `Asteroid`, prefab `Game`.
- **Espera:** `WaitForSeconds(0.1f)`.
- **Clasificación (Clase 1):** «discutible». El comportamiento es de una sola clase, pero depende del Spawner y del prefab. En la Clase 2 se propone sacarlo de la suite de integración y llevarlo a tests por componente **[PROPUESTO]**.
- **Estado:** pasa **[VERIFICADO]** (7/7, ver §14).

### Test 02 · `GameOverOccursOnAsteroidCollision` — `TestSuite.cs` 63–71

- **Valida:** un asteroide ubicado en la posición de la nave provoca `game.isGameOver == true`.
- **Componentes:** `Spawner`, `Asteroid`, física, `ShipModel` (contrato por nombre), `Game`.
- **Espera:** `WaitForSeconds(0.1f)`.
- **Clasificación:** integración. En la Clase 1 se usa como el test que cubre el **contrato invisible** `"ShipModel"`.
- **Limitación demostrada [VERIFICADO]:** solo mira el booleano. Al quitar `spawner.StopSpawning()`, este test **siguió pasando** (ver test 04).
- **Estado:** pasa **[VERIFICADO]**.

### Test 03 · `NewGameRestartsGame` — `TestSuite.cs` 73–80

- **Valida:** después de `game.isGameOver = true` y `game.NewGame()`, `isGameOver == false`.
- **Tipo:** `[Test]` sincrónico, sin frames.
- **Componentes:** `NewGame()` toca `Spawner`, `Ship` y la UI, aunque el assert mire solo un flag.
- **Clasificación:** integración (Clase 1).
- **Problema señalado [CONCEPTO]:** parte de un **Game Over falso**: pone el flag a mano y produce un estado que el juego nunca genera así. En la Clase 2 se propone reemplazarlo por INT-AST-08, un reinicio después de un Game Over real **[PROPUESTO]**.
- **Estado:** pasa **[VERIFICADO]**.

### Test 04 · `GameOverStopsSpawningAndDisablesShip` — `TestSuite.cs` 88–115

Es el único test escrito a propósito como ejemplo de integración (commit `7f7315f`, 18/09/2026).

- **Valida:** los efectos de `Game.GameOver()` sobre tres colaboradores:
  1. `game.isGameOver == true`;
  2. `game.GetShip().isDead == true`;
  3. la cantidad de `Asteroid` en la escena **no crece** después de esperar 0,5 s (mayor que el intervalo de spawn de 0,4 s).
- **Arrange:** `BeginSpawning()` y después el mismo choque que en el test 02.
- **Esperas:** `WaitForSeconds(0.1f)` y `WaitForSeconds(0.5f)`.
- **Evidencia [VERIFICADO]** (README y commit `7f7315f`): se quitó temporalmente `spawner.StopSpawning()` de `Game.GameOver()` y:
  - el test 04 **falló**, como se esperaba;
  - el test 02 **siguió pasando**;
  - `LaserMovesUp` (test 05), que no tiene relación aparente, **también falló**: el README lo atribuye a contaminación con asteroides de más que sobrevivieron al TearDown.

  Se revirtió el cambio y la suite volvió a 7/7.
- **Riesgo de fragilidad [CONCEPTO]:** el test cuenta **todos** los asteroides de la escena, incluidos los que sobraron de otros tests. Si uno de ellos cae por debajo de y = −5 durante la espera, el conteo baja y el test falla aunque el spawner se haya detenido (falso positivo). Si el spawner no se detuvo pero un asteroide sobrante se autodestruye en el mismo lapso, los conteos pueden coincidir (falso negativo). **[UNKNOWN]**: las notas aclaran que este escenario «no se confirmó ejecutándolo».
- **Propuesta [PROPUESTO]:** reescribirlo con la fixture de limpieza y contar solo los asteroides que crea el propio test.
- **⚠ Limitación detectada al consolidar** (lectura de código, no ejecutada): el assert 2 (`isDead == true`) **no puede distinguir** si `Explode()` se ejecutó. `Ship.isDead` vale `true` desde el inicio (`Ship.cs` 36 y `isDead: 1` en `Game.prefab`), y en este test nada llama a `RepairShip()`, así que el assert pasaría igual si `GameOver()` no llamara a `Explode()`. Este punto no se trabajó en ninguna de las dos clases. El README y el comentario del test ya documentan la limitación; el assert sigue sin corregirse.
- **Estado:** pasa **[VERIFICADO]**.

### Test 05 · `LaserMovesUp` — `TestSuite.cs` 117–125

- **Valida:** un láser creado con `SpawnLaser()` sube después de 0,1 s.
- **Espera:** `WaitForSeconds(0.1f)`.
- **Clasificación:** «discutible», como el test 01. En la Clase 2 se propone sacarlo de la suite de integración **[PROPUESTO]**.
- **Observación [VERIFICADO]:** falló por contaminación de estado durante el experimento del test 04 (ver más arriba). Es el ejemplo real de dependencia entre tests que tiene el proyecto.
- **Estado:** pasa en el estado normal del repositorio **[VERIFICADO]**.

### Test 06 · `LaserDestroysAsteroid` — `TestSuite.cs` 127–137

- **Valida:** un láser y un asteroide ubicados en (0,0,0) → el asteroide queda destruido.
- **Assert:** `UnityEngine.Assertions.Assert.IsNull(asteroid)`. Es la versión de Unity, no la de NUnit; la versión de Unity tiene una sobrecarga para `UnityEngine.Object`.
- **Espera:** `WaitForSeconds(0.1f)`. Es la espera que se usa como «antes» en la diapositiva «Esperar por condición» (`TestSuite.cs` 134).
- **Clasificación:** integración. En la Clase 2 forma parte de la categoría Smoke propuesta **[PROPUESTO]**.
- **Estado:** pasa **[VERIFICADO]**.

### Test 07 · `DestroyedAsteroidRaisesScore` — `TestSuite.cs` 139–149

- **Valida:** mismo escenario que el test 06 → `game.score == 1`.
- **Espera:** `WaitForSeconds(0.1f)`.
- **Clasificación:** integración.
- **Límite señalado [CONCEPTO]:** verifica `score`, **no** el texto del HUD (`Game.cs` 85). Si se borra esa línea, la suite sigue en verde (falso negativo). La línea 85 se *ejecuta* durante el test pero ningún assert la comprueba.
- **Propuesta [PROPUESTO]:** que lo absorba INT-AST-09, que verifica el puntaje y el texto «Score: 2». El costo es perder granularidad en el diagnóstico.
- **Observación detectada al consolidar:** la llamada es `Assert.AreEqual(game.score, 1)`, con los argumentos invertidos respecto de la firma `(expected, actual)`. No cambia el resultado, pero si el test falla, el mensaje intercambia «Expected» y «But was». Este punto no se trabajó en clase.
- **Estado:** pasa **[VERIFICADO]**.

### INT-AST-13 · `TwoLasersHitSameAsteroid_ScoreIncreasesOnce` — `IntegrationHypothesesTests.cs` 36–55

- **Dimensión de borde:** cantidad / simultaneidad.
- **Valida:** dos láseres impactan el mismo asteroide en el mismo paso de física → el asteroide se destruye y el puntaje es 1.
- **Esperas:** `yield return null` (para que corra `Start()`), luego 2 × `WaitForFixedUpdate` y `yield return null`.
- **Resultado [VERIFICADO]** (batchmode, Unity 6000.3.11f1, commit `af3e79e`): **FALLA** con `InvalidOperationException: Trying to release an object that has already been released to the pool` en `Laser.cs:52`.
- **Puntaje 2:** las notas dicen que el puntaje quedó en 2 en «una corrida de diagnóstico que ignoraba la excepción». **[UNKNOWN]**: el código de esa corrida no está en el repositorio, así que ese dato no se puede reproducir con los archivos actuales.
- **Causa [CONCEPTO]:** `Destroy()` no es inmediato, así que los dos `OnCollisionEnter` del mismo paso «ven» vivo al asteroide. Además, `Release` se aplica a objetos que nunca se pidieron al pool.

### INT-AST-14 · `NewGame_RemovesLeftoverAsteroids` — `IntegrationHypothesesTests.cs` 58–73

- **Categoría:** regresión, flujo C.
- **Valida:** un asteroide que quedó de la partida anterior (ubicado en (6, 3), lejos de la nave) no existe después de `Game.GameOver()` + `game.NewGame()`.
- **Esperas:** tres `yield return null`. El primero es imprescindible: sin él, `Game.GameOver()` se ejecutaría antes de que `Start()` asigne `Game.instance` y el test fallaría por un motivo ajeno a lo que se prueba.
- **Resultado [VERIFICADO]** (batchmode, 28/09/2026): **FALLA** con `NewGame debería eliminar los asteroides previos — Expected: True But was: False`.
- **Causa:** `SpawnAsteroid()` usa `Instantiate` y nunca `Get()`. `ClearAsteroids()` → `Dispose()` vacía un pool que no contiene los asteroides en pantalla. Tiene **la misma raíz** que INT-AST-13.
- **Impacto para el jugador:** un asteroide viejo puede chocar la nave recién reparada → Game Over inmediato.
- **Se presentó como:** Actividad 3 de la Clase 2 (análisis de un test que falla).

### INT-AST-15 (línea de base) · `SingleNewGame_SpawnCountBaseline` — `IntegrationHypothesesTests.cs` 76–88

- **Valida:** con una sola llamada a `NewGame()` y la nave alejada a (1000, 1000), se generan asteroides en 2,1 s (`count > 0`).
- **Espera:** `WaitForSeconds(2.1f)`.
- **Resultado [VERIFICADO]:** se registraron **5** asteroides en 2,1 s. Ese valor coincide con 2,1 / 0,4 ≈ 5. El commit no dice explícitamente si el test pasó, pero con `count = 5` el assert `count > 0` se cumple.

### INT-AST-15 · `DoubleNewGame_DoesNotChangeSpawnRate` — `IntegrationHypothesesTests.cs` 91–104

- **Dimensión de borde:** repetición.
- **Valida:** `NewGame()` llamado dos veces seguidas no aumenta la tasa de aparición (`count ≤ 6`).
- **Resultado [VERIFICADO]:** **FALLA**, con **8** asteroides en 2,1 s contra los 5 de la línea de base.
- **Causa:** `StartCoroutine` sobre el **mismo** `IEnumerator` (`Spawner.cs` 56 y 59–62).
- **[UNKNOWN]:** por qué son 8 y no 10. El material no lo explica.

### Resumen

| # | Test | Archivo | Flujo | Caso | Resultado registrado |
|---|---|---|---|---|---|
| 01 | AsteroidsMoveDown | TestSuite | — | Positivo | PASA |
| 02 | GameOverOccursOnAsteroidCollision | TestSuite | B | Positivo | PASA |
| 03 | NewGameRestartsGame | TestSuite | C | Positivo | PASA |
| 04 | GameOverStopsSpawningAndDisablesShip | TestSuite | B | Positivo | PASA |
| 05 | LaserMovesUp | TestSuite | — | Positivo | PASA |
| 06 | LaserDestroysAsteroid | TestSuite | A | Positivo | PASA |
| 07 | DestroyedAsteroidRaisesScore | TestSuite | A | Positivo | PASA |
| 13 | TwoLasersHitSameAsteroid_ScoreIncreasesOnce | IntegrationHypotheses | A | Borde · simultaneidad | **FALLA** (defecto real) |
| 14 | NewGame_RemovesLeftoverAsteroids | IntegrationHypotheses | C | Regresión | **FALLA** (defecto real) |
| 15b | SingleNewGame_SpawnCountBaseline | IntegrationHypotheses | C | Línea de base | 5 asteroides en 2,1 s |
| 15 | DoubleNewGame_DoesNotChangeSpawnRate | IntegrationHypotheses | C | Borde · repetición | **FALLA** (defecto real) |

Las fallas de 13, 14 y 15 son **intencionales**: según el comentario del archivo, los tests documentan la intención de diseño y no el comportamiento actual. **[UNKNOWN]** Esa intención de diseño (que el reinicio limpie la pantalla y que un doble impacto sume un solo punto) se infirió del código y de los nombres de los métodos. Las notas advierten que el requisito «se confirma con diseño» y no se infiere; no hay registro de que el diseño lo haya confirmado.

### Casos diseñados que **no** existen como test — [PROPUESTO]

| ID | Caso | Tipo |
|---|---|---|
| INT-AST-08 | Reinicio completo tras un Game Over real | Positivo · flujo |
| INT-AST-09 | El HUD muestra el puntaje (2 impactos → «Score: 2») | Positivo · regresión |
| INT-AST-10 | Láser contra un objeto que no es asteroide (dummy: cubo con collider) | Negativo |
| INT-AST-11 | Choque entre asteroides no da Game Over (caso modelo de la ficha de 8 campos) | Negativo |
| INT-AST-12 | Asteroide en y = −4,99 / −5,00 / −5,01 | Borde · valor |
| INT-AST-16 | Cooldown de disparo con Espacio mantenido (3 láseres en 1 s) | Dependencia de entrada; requiere refactor o Input System |

En la tabla de la Actividad 2 también quedan dos preguntas de diseño abiertas (⚠): un láser contra dos asteroides superpuestos (¿+1 o +2?) y un punto sumado en el mismo frame del Game Over (¿cuenta o no?).

---

## 7. Fixture de integración

### Lo que existe — [APLICADO]

```text
Setup (TestSuite e IntegrationHypothesesTests, idéntico):
    Object.Instantiate(Resources.Load<GameObject>("Prefabs/Game"))
    game = ...GetComponent<Game>()
```

- Es un `[SetUp]` sincrónico: **no** espera un frame, así que `Start()` (y por lo tanto `Game.instance`) todavía no corrió cuando empieza el test.
- `IntegrationHypothesesTests` compensa esto con un `yield return null` al **comienzo de cada test**, no en el SetUp.
- Ninguna fixture fija una semilla de `Random`.

### Fixture mejorada — [PROPUESTO]

Diapositiva «Fixture mejorada (PROPUESTA)» de la Clase 2. El código es propio de la cátedra:

```text
[UnitySetUp]   → Random.InitState(12345); Instantiate prefab; yield return null   (Start ya corrió)
[UnityTearDown]→ Destroy(game); Destroy de todo Asteroid y Laser activos; yield return null
```

| Cambio propuesto | Problema que ataca | Estado |
|---|---|---|
| `Random.InitState(semilla)` | Azar del Spawner | **[PROPUESTO]**. No se ejecutó en ningún test; las notas dicen «su estado es UNKNOWN». |
| `yield return null` en el SetUp | `Game.instance` sin asignar | **[APLICADO parcialmente]**: está en cada test de `IntegrationHypothesesTests`, no en el SetUp. `TestSuite` no lo tiene. |
| Limpieza total en `[UnityTearDown]` | Objetos raíz que sobreviven | **[APLICADO]** en `IntegrationHypothesesTests` **[VERIFICADO]**: corrió en batchmode. No está aplicado en `TestSuite`. |
| `yield return null` al final del TearDown | `Destroy` diferido | **[APLICADO]** en `IntegrationHypothesesTests`. |

Detalle del material: `FindObjectsByType` ignora por defecto los objetos inactivos, así que la limpieza no destruye la plantilla inactiva del láser que está dentro del prefab.

---

## 8. Setup y TearDown

| | `TestSuite` | `IntegrationHypothesesTests` |
|---|---|---|
| SetUp | `[SetUp]` sincrónico, instancia el prefab | Igual |
| Espera inicial | Ninguna (los tests con `WaitForSeconds` dejan correr `Start()` de hecho) | `yield return null` al comienzo de cada test |
| TearDown | `[TearDown]` sincrónico: `Object.Destroy(game.gameObject)` y **nada más** | `[UnityTearDown]`: destruye `game`, todos los `Asteroid` y todos los `Laser`, y después `yield return null` |
| Qué sobrevive al test | Asteroides y láseres instanciados (objetos raíz) | Nada, en principio |

**[VERIFICADO por lectura]** El código confirma la consecuencia: `SpawnAsteroid()` y `SpawnLaser()` usan `Instantiate` sin padre. El TearDown de `TestSuite` destruye `Ship` y `Spawner` (son hijos del prefab), pero no los objetos que crearon.

---

## 9. Estado compartido y tests frágiles

### Fuentes de estado compartido identificadas — [CONCEPTO] + [VERIFICADO por lectura]

| Fuente | Dónde | Efecto |
|---|---|---|
| Objetos raíz que sobreviven | `Spawner.cs` 73–99, `Ship.cs` 92–97, TearDown de `TestSuite.cs` 47–51 | Los asteroides y láseres de un test siguen en escena en el test siguiente |
| `Game.instance` estático | `Game.cs` 46 y 50 | Hasta que corre el `Start()` del test nuevo, apunta al `Game` destruido del test anterior. `GameOver()` y `AsteroidDestroyed()` son estáticos y dependen de él. |
| `Random` global sin semilla | `Spawner.cs` 75 y 103 | Posición X distinta en cada corrida. **Detectado al consolidar** (por lectura de los prefabs): `Random.Range(1,5)` también elige cuál de los cuatro prefabs se instancia, y cada uno tiene una velocidad distinta (6, 8, 7 o 9). El azar afecta la velocidad de caída, no solo la posición. |

### Tabla de fragilidad de la Clase 2 — [CONCEPTO]

| Causa | En la suite | Remedio propuesto |
|---|---|---|
| Tiempo fijo | `WaitForSeconds(0.1)` depende de la máquina y de la física | Esperar por condición, con tiempo máximo |
| Estado compartido | Asteroides de tests anteriores siguen en escena | TearDown que limpia todo |
| Orden | El test 04 cuenta todos los asteroides de la escena | Contar solo lo que creó el test |
| Azar | Posición X aleatoria | `Random.InitState(semilla)` |
| Física | Las colisiones ocurren en `FixedUpdate` | `WaitForFixedUpdate` |

### Contaminación observada — [VERIFICADO]

Es el único caso de interferencia entre tests que se observó. Al quitar `StopSpawning()`, `LaserMovesUp` falló sin tener relación con el cambio.

**[UNKNOWN] Mecanismo exacto.** La versión original del README decía «el `Spawn()` que quedó corriendo sin detenerse contaminó el siguiente test»; se corrigió el 02/10/2026 (ver §15). Leyendo el código, la corrutina vive en el `Spawner`, que es hijo del prefab `Game`, así que debería detenerse cuando el TearDown destruye `Game`. Lo que sobreviviría serían los asteroides **ya creados** durante el test, que son objetos raíz. Ese experimento no registró qué objeto exacto causó la falla de `LaserMovesUp`.

### Tests más frágiles de la suite actual

Esto es una síntesis del material, no un ranking ejecutado:

1. **Test 04:** conteo global de asteroides con espera fija (riesgo descripto en §6).
2. **Tests 01, 02, 05, 06 y 07:** espera fija de 0,1 s en lugar de esperar por condición o por paso de física. **[UNKNOWN]** No hay registro de que alguno haya fallado intermitentemente.
3. **INT-AST-15 (los dos tests):** cuentan **todos** los asteroides de la escena durante 2,1 s. Dependen de que la limpieza del test anterior haya funcionado y de que no ocurra un Game Over; para evitarlo alejan la nave.

---

## 10. Orden de ejecución e independencia de tests

**[CONCEPTO]** «Cada test tiene que poder correr solo y en cualquier orden con el mismo resultado. Si un test depende de lo que dejó otro, un fallo puede aparecer o desaparecer según el orden de ejecución». En la Actividad 4, la independencia es el criterio general de la suite propuesta.

**[APLICADO]** No hay `[Order]` ni otro mecanismo que fije el orden de ejecución en ningún test.

**[UNKNOWN]**
- **Orden real de ejecución.** La versión original del README y el commit `7f7315f` dicen que el test 04 contaminó «el siguiente test de la suite (`LaserMovesUp`)». `LaserMovesUp` es el siguiente test **en el código fuente**, pero no hay registro del orden en que el Test Runner lo ejecutó en esa corrida.
- **Si cada test pasa ejecutado de forma aislada.** No hay evidencia de corridas individuales (Run Selected) ni en orden distinto.
- **Si `TestSuite` sigue en 7/7 cuando corre junto con `IntegrationHypothesesTests`.** El reporte de cobertura de 28/09 22:13 muestra que hubo una corrida conjunta, pero no se guardó el resultado de esa corrida (pasa/falla por test).

### Mejora propuesta para garantizar la independencia — [PROPUESTO]

Es la combinación de lo que se presentó en la Clase 2. **Nada de esto está aplicado en `TestSuite`.**

1. **Fixture común** (§7): semilla fija, un frame de espera en el SetUp para que `Game.instance` quede asignado, limpieza total de `Asteroid` y `Laser` en `[UnityTearDown]` y un frame de espera al final.
2. **Contar solo lo propio:** reescribir el test 04 para que compare solo los asteroides que crea el propio test, no el total de la escena.
3. **Esperas por condición con timeout**, y `WaitForFixedUpdate` cuando se espera física (§11).
4. **No fabricar estados artificiales:** reemplazar el test 03 (`isGameOver = true` a mano) por INT-AST-08, que llega al Game Over por el camino real.
5. **Convención de nombres `Flujo_Condición_Resultado`** y categorías (`[Category("Smoke")]`, etc.) para correr subconjuntos.

**[APLICADO parcialmente]** Los puntos 1 (sin semilla) y 3 (solo `WaitForFixedUpdate`) ya se usan en `IntegrationHypothesesTests`. La convención de nombres también: `Flujo_Condición_Resultado`, por ejemplo `NewGame_RemovesLeftoverAsteroids`.

**[UNKNOWN]** Ninguna parte de esta mejora se validó corriendo los tests en orden distinto ni de forma aislada.

---

## 11. Esperas y sincronización

### Inventario de esperas — [APLICADO] [VERIFICADO por lectura]

| Archivo | Esperas |
|---|---|
| `TestSuite.cs` | `WaitForSeconds(0.1f)` en las líneas 58, 68, 97, 122, 134 y 146 · `WaitForSeconds(0.5f)` en la línea 108 |
| `IntegrationHypothesesTests.cs` | `yield return null` en las líneas 32, 39, 50, 61, 67, 70, 79 y 94 · `WaitForFixedUpdate` en 48–49 · `WaitForSeconds(2.1f)` en 83 y 99 |

**[APLICADO] — no hay esperas por condición** en ningún test del proyecto: no se usa un bucle con timeout ni `WaitUntil`.

### Conceptos — [CONCEPTO]

- **Espera fija:** «apuesta a que en X segundos ya pasó». En una máquina lenta falla (falso positivo) y en una rápida desperdicia tiempo.
- **Espera por condición con timeout:** termina apenas se cumple lo esperado y, si nunca se cumple, falla con un mensaje claro.
- **Ciclo de vida:** `Start()` corre en el frame siguiente a `Instantiate`. `Destroy()` se completa al final del frame. Las colisiones se procesan en el paso de física.
- **Mensajes en los Assert:** «El mensaje del Assert explica QUÉ se esperaba: ayuda a diagnosticar». `IntegrationHypothesesTests` y el test 04 los usan; los tests 01–03 y 05–07 no **[APLICADO]**.

### Espera por condición — [PROPUESTO]

Diapositiva «Esperar por condición, no por tiempo fijo». Reemplaza la espera de `TestSuite.cs` 134 por:

```text
timeout = 2 s; mientras (asteroid != null && timeout > 0) { timeout -= deltaTime; yield return null; }
Assert.IsTrue(asteroid == null, "mensaje")
```

**[UNKNOWN]** No se ejecutó.

---

## 12. Random y reproducibilidad

- **[APLICADO]** El `Spawner` usa `UnityEngine.Random` sin semilla en dos lugares: la elección del prefab (`Spawner.cs` 75) y la posición X (103). Ningún test llama a `Random.InitState` (verificado con búsqueda en `Assets/`).
- **[CONCEPTO]** «Los datos de prueba deben ser reproducibles: si hay azar, se controla con una semilla». El azar se controla con una semilla, sin usar un doble de prueba.
- **[PROPUESTO]** `Random.InitState(12345)` en el SetUp de la fixture mejorada.
- **[UNKNOWN]** La semilla nunca se ejecutó. Tampoco se sabe:
  - si fijarla alcanza para que las posiciones sean idénticas entre corridas, porque otras llamadas a `Random` (por ejemplo, del motor o de otros tests) podrían consumir valores;
  - si alguno de los 7 tests es sensible a la posición o al prefab que sale.

  Lo que sí muestra el código es que los tests 06, 07 y 13 reubican explícitamente los objetos en (0,0,0), y el 14 en (6, 3), justamente para no depender de la posición aleatoria.

---

## 13. Problemas encontrados y aprendizajes

### Defectos del juego encontrados por tests de integración — [VERIFICADO]

| ID | Defecto | Causa | Evidencia |
|---|---|---|---|
| INT-AST-13 | Dos láseres sobre el mismo asteroide: excepción por doble `Release` al pool (y puntaje 2 en la corrida de diagnóstico) | `Destroy` diferido + uso inconsistente del `ObjectPool` (`Laser.cs` 52) | Test en rojo, batchmode |
| INT-AST-14 | `NewGame` no elimina los asteroides de la partida anterior | `SpawnAsteroid` no usa el pool; `ClearAsteroids` → `Dispose` de un pool vacío | Test en rojo, batchmode |
| INT-AST-15 | Doble `NewGame` → 8 asteroides en 2,1 s en lugar de 5 | `StartCoroutine` sobre el mismo `IEnumerator` | Test en rojo, batchmode |

**[CONCEPTO]** 13 y 14 comparten la raíz: el pool nunca usa `Get()`. Destruir los asteroides en `ClearAsteroids` resolvería el 14 pero no el 13; arreglar el uso del pool ataca la causa común.

**[UNKNOWN]** Ninguno de los tres defectos se corrigió. No consta que se haya levantado un ticket real; en la Actividad 3 se redactó un ticket modelo.

### Defectos de la suite de tests

| Problema | Fuente | Estado |
|---|---|---|
| Todos los tests de la suite original son casos positivos: no hay negativos ni bordes | Clase 2 | [CONCEPTO] |
| El HUD (`Game.cs` 85) no se verifica | Clases 1 y 2 | [CONCEPTO]; INT-AST-09 [PROPUESTO] |
| El test 03 parte de un estado artificial | Clase 2 | [CONCEPTO] |
| El TearDown de `TestSuite` no limpia los objetos raíz | Clase 2 | [VERIFICADO por lectura]; contaminación [VERIFICADO] en el experimento del test 04 |
| Esperas fijas | Clases 1 y 2 | [CONCEPTO]; fallas intermitentes [UNKNOWN] |
| Ningún test ejercita la entrada del jugador; la regla del cooldown no es testeable sin refactor | Clase 2 | [VERIFICADO por lectura] (`Ship.cs` 61; sin Input System) |
| El comentario de `TestSuite.cs` 82–87 dice que solo el test 04 es de integración | Clase 1 | [CONCEPTO]: «es impreciso» |
| El assert 2 del test 04 no distingue si se ejecutó `Explode()` | Detectado al consolidar | Lectura de código; no ejecutado |

### Aprendizajes con evidencia del propio proyecto

- **Un test que mira un solo valor puede no ver una regresión que otro test sí detecta** [VERIFICADO]: experimento del test 04 contra el test 02.
- **La falta de aislamiento produce fallas en tests no relacionados** [VERIFICADO]: `LaserMovesUp`.
- **Un test de regresión tiene que haberse visto en rojo** [CONCEPTO + APLICADO]: el test 04 se vio fallar a propósito; 13, 14 y 15 están en rojo.
- **Un test puede fallar por un error del propio test** [CONCEPTO + APLICADO]: el `yield return null` de INT-AST-14 existe para que el test no falle por `Game.instance` sin asignar.
- **La cobertura alta no implica verificación** [VERIFICADO]: `Game.cs` tiene 100 % de líneas cubiertas y la línea 85 no la comprueba ningún assert.

---

## 14. Qué está verificado

| Afirmación | Tipo de evidencia | Fuente |
|---|---|---|
| `TestSuite` pasa 7/7 en el estado normal del repositorio | Ejecución en batchmode (`Unity.exe -batchmode -nographics -runTests -testPlatform PlayMode`) | README, commit `7f7315f` (18/09); commit `af3e79e` (29/09: «7/7 PASS»); notas de la Clase 2 |
| Sin `StopSpawning()`: el test 04 falla, el 02 pasa y el 05 falla | Ejecución (experimento revertido) | README, commit `7f7315f` |
| INT-AST-13 falla con `InvalidOperationException` en `Laser.cs:52` | Ejecución en batchmode | Commit `af3e79e`, notas |
| INT-AST-14 falla (`Expected: True But was: False`) | Ejecución en batchmode, 28/09/2026 | Diapositiva de la Actividad 3, commit `af3e79e` |
| INT-AST-15: 5 asteroides con un `NewGame` y 8 con dos; el test doble falla | Ejecución en batchmode | Commit `af3e79e`, notas |
| La limpieza total del `[UnityTearDown]` corre sin errores | Ejecución en batchmode | Notas: «Fixture mejorada» |
| Cobertura de 73,6 % de líneas (137/186) y 87 % de métodos de `GameAssembly`. Game 100 %, Ship 43 %, Asteroid 84,2 %, Laser 81,2 %, Spawner 86,9 % | Reporte regenerado, 7 tests, solo `GameAssembly`, carpeta limpia | Notas y commit `af3e79e` (ver la salvedad en §15) |
| Líneas nunca ejecutadas: Ship 61–74 (entrada) y 99–115 (movimiento lateral), Asteroid 48, Spawner 69, Laser 42 | Mismo reporte | Notas |
| Cobertura de ramas no medida (0 de 0) | Reporte | Notas; también en el reporte en disco |
| El reporte viejo (65,5 %) mezclaba 3 corridas y el código de los tests | Lectura del reporte | Notas de la Clase 2 |
| Física de los prefabs (Rigidbody dinámico, BoxCollider no trigger) y `ScoreText` dentro del prefab `Game` | Lectura de los prefabs | Notas; confirmado al consolidar |
| `isDead: 1` en el prefab; Input System ausente en `manifest.json` | Lectura de archivos | Notas; confirmado al consolidar |
| Las líneas citadas en las diapositivas coinciden con el código actual | Lectura de archivos | Confirmado al consolidar |

---

## 15. Qué permanece UNKNOWN

### Sobre las ejecuciones

- **El reporte de 73,6 % no está en disco.** `CodeCoverage/` no se versiona (`.gitignore`). El reporte que hay hoy en `proyectos-unity/Asteroides/asteroide-final/CodeCoverage/Report/` es del **28/09/2026 22:13** y **no** corresponde a esa corrida:
  - usa `MultiReportParser (6x OpenCoverParser)`;
  - incluye los assemblies `GameAssembly` y `Tests`, y los tests de `IntegrationHypothesesTests`;
  - informa 82,7 % total y 77 % para `GameAssembly`.

  Además, `ProjectSettings/Packages/com.unity.testtools.codecoverage/Settings.json` tiene `IncludeAssemblies = "GameAssembly,Tests"`. Las cifras de 73,6 % no se pueden reproducir hoy con los archivos del repositorio.
- **El puntaje 2 de INT-AST-13** viene de una corrida de diagnóstico cuyo código no se conservó.
- **Por qué el doble `NewGame` produce 8 asteroides** y no 10.
- **El resultado de `TestSuite` en una corrida conjunta** con `IntegrationHypothesesTests`.
- **El orden real de ejecución** de los tests y si cada test pasa de forma aislada o en otro orden.
- **Si las esperas fijas producen fallas intermitentes** en otras máquinas o en el Editor (solo hay evidencia de batchmode).
- **El efecto real de `Random.InitState`:** nunca se ejecutó.
- **El mecanismo exacto de la contaminación de `LaserMovesUp`** (ver §9).
- **El escenario de falso positivo / falso negativo del test 04:** las notas lo presentan como un riesgo, no como una falla observada.

### Sobre el diseño del juego

- Si el diseño **exige** que `NewGame` limpie la pantalla (INT-AST-14) y que un doble impacto sume 1 (INT-AST-13). Se infirió del código, pero el diseño no lo confirmó.
- Las dos filas ⚠: un láser contra dos asteroides superpuestos (¿+1 o +2?) y un punto sumado en el frame del Game Over.

### Sobre el dictado

- Si las clases se dictaron como estaban planificadas, qué produjeron los grupos y qué resultados obtuvieron.
- **El «defecto sembrado»** que menciona la consigna práctica de la Clase 1. No se identificó en el repositorio a qué proyecto ni a qué defecto se refiere.
- Si se crearon tickets reales en Jira para INT-AST-13, 14 o 15.

### Documentación que estaba desactualizada respecto del código (corregida el 02/10/2026)

Detectado al consolidar y corregido después, solo en documentación y comentarios. **No se cambió ningún assert ni la lógica de ningún test.**

- [`proyectos-unity/Asteroides/README.md`](../../proyectos-unity/Asteroides/README.md) describía una suite de **7** tests en 7/7 y no mencionaba `IntegrationHypothesesTests.cs`. Ahora incluye una sección para esos 4 tests, con sus 3 fallas esperadas, y la validación separada por clase de test.
- El README decía que «6 de las 7 pruebas verifican un único efecto observable» y presentaba solo al test 04 como de integración. Ahora aclara que los 6 tests del tutorial verifican un solo efecto pero integran varios sistemas, y remite a la clasificación de la Clase 1.
- El README y el comentario del test 04 decían que el assert 2 prueba que se ejecutó `Explode()`. Ahora documentan la limitación (ver §6, test 04). **El assert sigue igual:** corregirlo es una tarea pendiente.
- El README explicaba la contaminación de `LaserMovesUp` como «el `Spawn()` que quedó corriendo». Ahora atribuye la contaminación a los asteroides que sobreviven al `TearDown` y declara que no se registró el mecanismo exacto. También agrega el riesgo de conteo global del test 04 como riesgo no observado.
- Los comentarios de `TestSuite.cs` se reescribieron **sin cambiar la cantidad de líneas**, así que las referencias por número de línea de las diapositivas y de este documento siguen siendo válidas.

---

## 16. Buenas prácticas aprendidas

Todas figuran en el material **[CONCEPTO]**. Se indica dónde ya están aplicadas en el proyecto.

| Práctica | ¿Aplicada en el proyecto? |
|---|---|
| Probar las **costuras**, no cada pieza por separado | Sí: test 04 e `IntegrationHypothesesTests` |
| Verificar **todos los efectos** de un flujo, no solo un flag | Parcialmente: el test 04 (con la salvedad del assert 2) |
| Incluir casos **negativos** y de **borde** (valor, tiempo, simultaneidad, repetición, orden) | Bordes: 13 y 15. Negativos: ninguno implementado |
| El resultado esperado sale del **diseño**, no de lo que hace el código hoy; si no está definido, se registra como pregunta | Como criterio, en las fichas |
| Fixture que **aísla**: estado conocido al empezar y **limpieza total** al terminar | Solo en `IntegrationHypothesesTests` |
| Esperar un frame después de `Instantiate` si el test depende de `Start()` | Solo en `IntegrationHypothesesTests` |
| `WaitForFixedUpdate` para la física y **espera por condición con timeout** para el resto | `WaitForFixedUpdate`: sí (INT-AST-13). Espera por condición: no |
| Controlar el azar con una **semilla** | No |
| Contar o verificar **solo lo que creó el test** | No (test 04, INT-AST-15) |
| Comparar objetos de Unity con `== null`, no con `Assert.IsNull` de NUnit | Sí: `IntegrationHypothesesTests` y test 06 (con `UnityEngine.Assertions`) |
| Assert con **mensaje** que explique qué se esperaba | Test 04 e `IntegrationHypothesesTests` |
| Ver el test en **rojo** antes de confiar en él | Sí: experimento del test 04, y 13, 14 y 15 |
| Dobles de prueba solo para lo que **no** está bajo prueba; demasiados dobles convierten el test en unitario | Sin dobles en el proyecto (todos los ejemplos de la tabla son PROPUESTA, salvo el dummy de INT-AST-10, que tampoco está implementado) |
| Separar la lectura de entrada de las reglas de juego para poder testearlas | No (requiere refactor) |
| Leer la cobertura sabiendo de qué corrida viene; **cobertura ≠ verificación** | Sí: análisis del reporte viejo contra el regenerado |
| Organizar la suite por propósito (Smoke / Integración / Borde / Regresión) con nombres `Flujo_Condición_Resultado` | Solo los nombres en `IntegrationHypothesesTests`; categorías: no |
| Automatizar lo repetitivo y verificable; hacer prueba manual documentada de lo visual o exploratorio | Como criterio |

### Mini-suite propuesta en la Actividad 4 — [PROPUESTO]

Son 11 tests:

| Categoría | Tests |
|---|---|
| Smoke | 02, 06, 08 |
| Integración | 04 (reescrito), 09 (absorbe al 07), 10, 11 |
| Borde | 12, 13, 15 |
| Regresión | 14 |
| Fuera de la suite | 01 y 05 (pasan a tests por componente) · 03 (reemplazado por 08) · 16 (pendiente del refactor) |

---

## 17. Temas posibles para continuar

Estos temas **no se trabajaron**. Los primeros se mencionaron como contenido reservado en la diapositiva «Anexo · Para una clase futura» de la Clase 2. Los últimos surgen de los huecos detectados en esta consolidación.

**Mencionados como reservados [CONCEPTO, sin desarrollar]:**
- Integración con sistemas externos (guardado del récord, tabla online) mediante fakes o entornos de prueba.
- Input System + `InputTestFixture` para simular teclado y táctil. Requiere instalar el paquete.
- Tests parametrizados (`[TestCase]`, `[ValueSource]`) para los bordes (por ejemplo, INT-AST-12).
- `LogAssert` para esperar o prohibir mensajes en el log (útil para INT-AST-13).
- Ejecución en batchmode y CI (tests en cada push).
- Cobertura de ramas y umbrales mínimos.
- Tests de rendimiento (Performance Testing).
- Relación con la plataforma: la misma suite en PC y en móvil.

**Surgidos de los huecos detectados:**
- Verificar la independencia de forma empírica: correr cada test solo y en otro orden.
- Atributo `[Order]` y por qué no debería ser la solución a la dependencia entre tests.
- Cómo hacer que un test detecte que se ejecutó un efecto cuando el estado inicial ya coincide con el estado esperado (el caso del assert 2 del test 04).
- Corrección de los defectos 13, 14 y 15 y el paso de los tests de rojo a verde (el ciclo de regresión completo).

---

## 18. Ideas que podrían servir posteriormente para un Trabajo Práctico

*Esto no es un diseño del TP: es el inventario de materia prima disponible.*

### Conocimientos que ya tienen soporte en el material

- Diferencia entre nivel y tipo de prueba, y entre unitario e integración, con la clasificación de los 7 tests como ejercicio ya resuelto.
- Ficha de caso de integración de 8 campos y las cinco dimensiones del borde.
- Fixture (SetUp / TearDown), aislamiento, estado compartido y `Game.instance`.
- Causas de fragilidad y sus remedios.
- Lectura crítica de un reporte de cobertura.
- Ciclo de regresión (rojo → arreglo → verde → queda en la suite).
- Dobles de prueba y la regla de qué va real en integración.

### Funcionalidades del proyecto que ofrecen flujos de integración

- Flujo A: láser → asteroide → puntaje → HUD.
- Flujo B: asteroide → nave (contrato por nombre `"ShipModel"`) → Game Over → spawner y nave.
- Flujo C: Game Over → `NewGame` → spawner, nave, UI y limpieza de asteroides.
- Spawner con corrutina, `ObjectPool` y azar.
- Disparo con cooldown acoplado a la entrada.
- Límites espaciales: `y < −5` para los asteroides y `y > 10` para el láser.

### Problemas reales del proyecto, con evidencia

- Tres defectos confirmados por tests en rojo (13, 14 y 15), con causa raíz identificada y sin corregir.
- Una suite con TearDown incompleto, esperas fijas, azar sin semilla y un test que cuenta objetos globales.
- Un efecto (HUD) que se ejecuta sin verificarse, y cobertura de 100 % en `Game.cs`.
- Un assert que no discrimina (test 04, assert 2).
- Una regla de juego no testeable sin refactor ni paquete adicional (INT-AST-16).
- Casos diseñados y no implementados (08, 09, 10, 11, 12 y 16).
- Preguntas de diseño abiertas (filas ⚠).
- Un caso real de documentación que había quedado desactualizada respecto de los tests (README, corregido el 02/10/2026; ver §15).

### Evidencias y herramientas disponibles

- Ejecución en batchmode documentada (comando en el README).
- Paquete Code Coverage 1.3.0 instalado y antecedentes de cómo un reporte puede engañar (reporte viejo contra regenerado, y el reporte actual en disco, que mezcla corridas).
- Formato de ticket de la Unidad II, ya conectado con el testing de integración en las dos clases.
