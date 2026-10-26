# -*- coding: utf-8 -*-
"""
Notas del orador de Testing-Integracion-II.pptx, indexadas por título de diapositiva.
Cada nota indica qué se toca, la teoría de apoyo y aclaraciones de los puntos de la
diapositiva. Sin tiempos: la distribución horaria está en la diapositiva de agenda.
"""

NOTAS = {
"Testing de integración II": """\
QUÉ SE TOCA: presentación de la clase y continuidad con «Testing de integración».
CONTEXTO: seguimos con el proyecto nave + asteroides (Crashteroids, basado en el tutorial de Kodeco) y su TestSuite de 7 tests de Play Mode.
OBJETIVO DE LA CLASE: no se trata de escribir más tests por escribirlos, sino de pasar de una colección de tests a una estrategia: qué probar, cómo aislar cada test, cómo saber si los resultados son confiables y cómo organizar la suite.
IDEA PARA ABRIR: una suite en verde no es lo mismo que un juego sin defectos. Es uno de los 7 principios del testing (Unidad I): las pruebas muestran la presencia de defectos, no su ausencia.""",

"Dónde quedamos: la suite actual": """\
QUÉ SE TOCA: el punto de partida; qué cubren los 7 tests y qué dejan afuera.
REPASO (no reexplicar): en la clase anterior se vieron niveles vs. tipos de prueba, que Play Mode es un modo de ejecución y no un nivel, la clasificación de estos 7 tests y dos límites: el texto del HUD no se verifica y las esperas son fijas.
TEORÍA: una suite se evalúa por lo que deja afuera, no solo por lo que pasa. Tres preguntas para cualquier suite: ¿prueba lo que NO debe pasar? ¿prueba los límites? ¿cada test es independiente de los demás?
ACLARACIONES — huecos que abre esta clase:
(1) Los 7 son casos positivos: no hay negativos ni bordes.
(2) El test 03 parte de un Game Over falso: pone isGameOver = true a mano, un estado que el juego nunca produce así.
(3) El TearDown solo destruye el prefab Game: asteroides y láseres quedan en escena para el test siguiente.
(4) Ningún test ejercita la entrada del jugador.""",

"Objetivos de la clase": """\
QUÉ SE TOCA: los seis objetivos, en el mismo orden que los bloques.
ACLARACIONES — relación con los bloques: Bloque 1 → objetivo 1 (diseño de casos). Bloque 2 → objetivos 2 y 3 (fixtures y tests frágiles). Bloque 3 → objetivo 4 (dependencias y dobles de prueba). Bloque 4 → objetivos 5 y 6 (cobertura, regresión y organización de la suite).
TEORÍA: todos apuntan a una misma idea: la confianza en una suite depende de qué casos tiene, de que sus resultados sean reproducibles y de que se interprete bien lo que mide.
RELACIÓN CON EL PROGRAMA: Unidad I (partición de equivalencia, valores frontera, testing negativo, falsos positivos y negativos), Unidad II (regresión vs. retesting, casos de prueba, tickets) y Unidad III (Unity Test Framework, pruebas manuales vs. automatizadas).""",

"Agenda (120 min)": """\
QUÉ SE TOCA: la estructura de la clase.
ACLARACIONES: cada bloque sigue el mismo patrón: concepto → ejemplo simple → aplicación al juego → actividad con resolución.
Las resoluciones se hacen en plenario inmediatamente después de cada actividad, para corregir los errores mientras la consigna está fresca.
Las actividades 1, 2 y 4 son sin código. La 3 es de lectura y análisis de un test real del proyecto.""",

"La suite pasa… ¿y el juego?": """\
QUÉ SE TOCA: el problema que motiva la clase.
TEORÍA: «la suite pasa» solo dice que los casos que existen se comportan como se esperaba. Si no hay un caso para una situación, la suite no opina sobre ella. Por eso la pregunta correcta no es «¿pasa?» sino «¿qué situaciones prueba?».
ACLARACIONES — las cuatro preguntas son el mapa de la clase:
1 → Actividad 3 (INT-AST-14: reinicio con asteroides en pantalla).
2 → Actividad 2 (INT-AST-13: doble impacto).
3 → Actividad 1 (INT-AST-11: choque entre asteroides).
4 → Bloque 4 (cobertura).
Respuesta a la pregunta de la diapositiva: ninguna de las cuatro está cubierta hoy.
DATOS VERIFICADOS: la suite de 7 tests pasa completa (7/7) en Unity 6000.3.11f1 en batchmode. Cobertura regenerada en una carpeta limpia: 73,6 % de las líneas de GameAssembly; Game.cs, 100 %.""",

"Positivos, negativos y borde": """\
QUÉ SE TOCA: los tres tipos de caso y cómo se trasladan de un método a una interacción.
TEORÍA:
- Positivo: entrada válida → comportamiento esperado.
- Negativo (testing negativo, Unidad I): entrada inválida o no prevista → el sistema la ignora o la rechaza sin romperse.
- Borde: valores en el límite de una partición (análisis de valores frontera): justo antes, justo en y justo después del límite.
Estas técnicas nacieron para métodos con entradas numéricas. En integración se aplican a interacciones: qué colisiona con qué, cuándo y cuántas veces.
ACLARACIONES: error frecuente: «caso negativo» NO significa «test que tiene que fallar». El test de un caso negativo PASA cuando el sistema se comporta bien ante la entrada indebida. Ejemplo: un asteroide que choca con otro no debe dar Game Over; si no da Game Over, el test pasa.
EN EL JUEGO: Asteroid.cs 54 decide el Game Over comparando el nombre del objeto con «ShipModel». Esa condición define las particiones: «choques con la nave» y «choques con cualquier otra cosa».""",

"Cinco dimensiones del borde en integración": """\
QUÉ SE TOCA: dónde buscar bordes cuando lo que se prueba es una interacción.
TEORÍA — en integración, el límite no es solo un número:
- Valor / posición: el umbral de un dato (y < −5).
- Tiempo: intervalos y cooldowns (0,4 s).
- Cantidad / simultaneidad: 0, 1 o 2 eventos en el mismo instante.
- Repetición: llamar dos veces algo pensado para una.
- Orden: eventos que llegan en una secuencia inesperada.
ACLARACIONES: la simultaneidad es clave en Unity porque Destroy() no destruye en el acto: marca el objeto y lo elimina después del ciclo de actualización. Todas las colisiones del mismo paso de física se procesan antes, por eso dos láseres pueden «ver» vivo al mismo asteroide.
Algunos bordes no tienen respuesta en el código: la decide el diseño (¿un láser que toca dos asteroides suma 1 o 2?). Quien prueba no la inventa: la registra como pregunta.
DEMO SUGERIDA: en el Editor, pausar y avanzar frame a frame (botón Step) mientras dos láseres llegan a un asteroide.""",

"Formato de un caso de integración": """\
QUÉ SE TOCA: la ficha de 8 campos que se usa en todas las actividades.
TEORÍA: amplía la ficha de caso de prueba de la Unidad II (identificador, precondiciones, pasos, datos, resultado esperado) con tres campos propios de integración:
- Componentes: qué piezas reales participan.
- Bug que detecta: para qué existe el caso. Si no se puede completar, probablemente el caso no aporta.
- ¿Por qué integración?: qué costura (conexión entre componentes) prueba.
ACLARACIONES: el ejemplo es un caso negativo. Los asteroides aparecen en una x aleatoria entre −8 y 8 (Spawner.cs 101–107), así que el choque entre asteroides es posible en el juego real.
DATO VERIFICADO: en los prefabs, los cuatro asteroides tienen Rigidbody dinámico sin gravedad y BoxCollider que no es trigger, así que el choque genera OnCollisionEnter. Sin Rigidbody en al menos uno de los dos objetos no habría evento de colisión y el caso no probaría nada.""",

"Actividad 1 · Diseñar casos nuevos (12 min)": """\
OBJETIVO: diseñar casos positivos y negativos sin duplicar la suite actual.
CÓMO GUIAR: para encontrar negativos, preguntar «¿qué NO debería pasar en este flujo?». Para encontrar positivos nuevos, preguntar «¿qué efecto de este flujo no verifica nadie hoy?».
RESULTADO ESPERADO: 6 fichas completas, 2 por flujo.
PREGUNTAS PARA LA DISCUSIÓN: ¿un caso negativo necesita datos de prueba especiales? ¿Un positivo nuevo aporta más que agregar otro assert a un test existente?
La resolución está en la diapositiva siguiente.""",

"Actividad 1 · Resolución": """\
QUÉ SE TOCA: la resolución de la Actividad 1.
PUNTOS A REMARCAR:
(1) El flujo B ya tiene positivos (02 y 04). Si un grupo propone «el Game Over muestra el texto de Game Over» (gameOverText, Game.cs 64), es un positivo válido.
(2) INT-AST-08 reemplaza con ventaja al 03: el 03 simula el Game Over con isGameOver = true, un estado artificial; el 08 llega al Game Over por el camino real (un choque), como un jugador.
(3) INT-AST-10 necesita un objeto que no existe en el juego (un cubo con collider): es el primer ejemplo de dato de prueba artificial, un «dummy» (se retoma en el Bloque 3).
(4) El caso C− (llamar a NewGame con una partida en curso) conecta con INT-AST-15.
DATOS VERIFICADOS: el prefab Laser tiene Rigidbody dinámico y BoxCollider, así que alcanza con un cubo con collider para que ocurra OnCollisionEnter. El ScoreText está dentro del prefab Game (UICanvas), así que INT-AST-09 se puede automatizar sin cambiar el código del juego.""",

"Actividad 2 · Casos borde (10 min)": """\
OBJETIVO: aplicar el análisis de valores frontera a interacciones entre componentes.
CÓMO GUIAR: pedir valores concretos (−4,99; −5,00; −5,01), no «valores cercanos al límite». Para la dimensión tiempo, recordar que el cooldown del disparo es de 0,4 s.
RESULTADO ESPERADO: 5 filas con valores concretos y al menos 2 marcadas con ⚠.
PREGUNTAS PARA LA DISCUSIÓN: ¿qué diferencia hay entre un borde que se responde leyendo el código (y = −5) y uno que requiere una decisión de diseño (un láser contra dos asteroides)? ¿Quién decide el resultado esperado de una fila ⚠? Respuesta: el diseño o el responsable del producto; quien prueba lo registra como pregunta.""",

"Actividad 2 · Resolución": """\
QUÉ SE TOCA: la resolución de la Actividad 2 y los resultados reales de dos casos borde.
TEORÍA: el resultado esperado sale de la especificación o del diseño, no de lo que hace el código hoy. Si la especificación no lo dice, el caso queda pendiente y se registra la pregunta; no se resuelve por inferencia.
ACLARACIONES POR FILA: Valor: la condición es estricta (y < −5), así que en −5,00 el asteroide sigue vivo. Tiempo: hoy no se puede automatizar porque la regla del cooldown depende del teclado (ver Bloque 3).
RESULTADOS REALES (Unity 6000.3.11f1, batchmode, Assets/Tests/IntegrationHypothesesTests.cs):
- INT-AST-13: FALLA con «InvalidOperationException: Trying to release an object that has already been released to the pool» en Laser.cs:52. En una corrida de diagnóstico que ignoraba la excepción, el puntaje quedó en 2. Causa: los dos OnCollisionEnter se ejecutan antes de que Destroy se haga efectivo.
- INT-AST-15: FALLA. 5 asteroides en 2,1 s con una llamada a NewGame; 8 con dos llamadas seguidas (con la nave alejada para evitar un Game Over). Causa: StartCoroutine sobre el mismo IEnumerator (Spawner.cs 49–62).""",

"Fixtures y datos de prueba": """\
QUÉ SE TOCA: qué es una fixture y por qué la suite actual no aísla los tests.
TEORÍA: una fixture es el estado conocido desde el que arranca cada test (SetUp) más la limpieza al terminar (TearDown). Su objetivo es el aislamiento: cada test tiene que poder correr solo y en cualquier orden con el mismo resultado. Si un test depende de lo que dejó otro, un fallo puede aparecer o desaparecer según el orden de ejecución.
Los datos de prueba son valores y objetos preparados a propósito, y deben ser reproducibles: si hay azar, se controla con una semilla.
ACLARACIONES — los tres problemas de la suite actual:
(1) Objetos que sobreviven: Spawner.SpawnAsteroid y Ship.SpawnLaser usan Instantiate sin padre, así que quedan como objetos raíz y el TearDown (que solo destruye el prefab Game) no los alcanza.
(2) Estado estático: Game.instance es static; hasta que corre el Start() del test nuevo, apunta al Game destruido del test anterior.
(3) Azar: el Spawner usa Random.Range sin semilla.
Su efecto concreto depende del orden de ejecución (ver la diapositiva de tests frágiles).""",

"Fixture mejorada (PROPUESTA)": """\
QUÉ SE TOCA: una fixture que resuelve los tres problemas de la diapositiva anterior.
TEORÍA: [UnitySetUp] y [UnityTearDown] son la versión de SetUp y TearDown del Unity Test Framework que permite usar yield, es decir, esperar frames. Hace falta porque Start() recién se ejecuta en el frame siguiente a Instantiate, y Destroy() recién se completa después del ciclo de actualización.
ACLARACIONES — línea por línea:
- Random.InitState fija la semilla: mismas posiciones en cada corrida.
- El primer yield return null deja correr Start(): Game.instance queda asignado.
- El TearDown destruye también asteroides y láseres.
- El último yield deja que Destroy se complete antes del test siguiente.
Detalle: FindObjectsByType ignora por defecto los objetos inactivos, así que no toca la plantilla inactiva del láser que está dentro del prefab.
EVIDENCIA: una limpieza equivalente se usa en IntegrationHypothesesTests.cs y corrió en batchmode. La semilla (Random.InitState) todavía no se ejecutó: su estado es UNKNOWN.""",

"Tests frágiles (flaky)": """\
QUÉ SE TOCA: qué es un test frágil, sus causas y un riesgo concreto de la suite.
TEORÍA: un test frágil (flaky) pasa o falla sin que cambie el código. Es grave porque destruye la confianza: cuando un test falla «a veces», el equipo empieza a ignorar los fallos, incluidos los reales. Causas típicas (Martin Fowler, «Eradicating Non-Determinism in Tests»): tiempo, estado compartido, orden, azar y recursos externos.
Terminología de la Unidad I: falso positivo = el test reporta un defecto que no existe; falso negativo = el test no detecta un defecto que sí existe.
ACLARACIONES — riesgo en la suite: el test 04 (TestSuite.cs 88–115) cuenta TODOS los asteroides de la escena antes y después de esperar 0,5 s.
- Si un asteroide sobrante de otro test cae por debajo de y = −5 durante la espera, el conteo baja y el test FALLA aunque el spawner se haya detenido: falso positivo.
- Si el spawner NO se detuvo pero en ese lapso un asteroide sobrante se autodestruye, los conteos pueden coincidir y el test PASA: falso negativo.
Este escenario depende del orden y de las posiciones, y no se confirmó ejecutándolo: presentarlo como un riesgo, no como un fallo observado.""",

"Esperar por condición, no por tiempo fijo (PROPUESTA)": """\
QUÉ SE TOCA: cómo eliminar la causa «tiempo» de los tests frágiles.
TEORÍA: una espera fija (WaitForSeconds) apuesta a que «en X segundos ya pasó». En una máquina lenta o cargada la apuesta falla (falso positivo) y en una rápida se pierde tiempo. Una espera por condición con tiempo máximo termina apenas se cumple lo esperado y, si nunca se cumple, falla con un mensaje claro.
Para la física, la unidad de espera correcta es el paso de física: yield return new WaitForFixedUpdate().
ACLARACIONES: un GameObject destruido no es null para C#, pero «== null» devuelve true por la sobrecarga de UnityEngine.Object. El Assert.IsNull(obj) de NUnit puede no detectarlo; por eso se usa Assert.IsTrue(obj == null).
El mensaje del Assert explica qué se esperaba: cuando el test falla, ese mensaje es el primer dato del diagnóstico.""",

"Actividad 3 · Un test que falla (10 min)": """\
OBJETIVO: analizar la causa raíz de un fallo de integración.
TEORÍA: ante un test en rojo hay dos hipótesis iniciales: falla el juego o falla el test. Antes de levantar un ticket hay que descartar la segunda: ¿el test prepara bien el escenario? ¿El resultado esperado está respaldado por el diseño?
CÓMO GUIAR: seguir la cadena desde el assert hacia atrás: ¿qué objeto se esperaba destruido? ¿Qué método debía destruirlo? ¿Qué hace realmente ese método?
LA SALIDA ES REAL: Unity 6000.3.11f1 en batchmode; test en Assets/Tests/IntegrationHypothesesTests.cs.
ACLARACIÓN: la primera línea (yield return null) es necesaria. Sin ella, Game.GameOver() se ejecuta antes de que Start() asigne Game.instance y el test fallaría por un motivo ajeno a lo que se quiere probar: sería un error del test, no del juego.
RESULTADO ESPERADO: una cadena causal con archivo y líneas, y un ticket.
PREGUNTA PARA LA DISCUSIÓN: ¿cómo sabemos que el resultado esperado es correcto?""",

"Actividad 3 · Resolución": """\
QUÉ SE TOCA: la resolución de la Actividad 3.
TEORÍA: la causa raíz (Unidad I) es el origen del defecto, no su síntoma. El síntoma es «el asteroide sobrevive al reinicio»; la causa es «el pool de asteroides no se usa de forma consistente».
RESOLUCIÓN:
(1) ¿Juego o test? El test está bien construido: el asteroide está lejos de la nave, el spawner automático recién crea uno nuevo a los 0,4 s y se espera un solo frame. El nombre ClearAsteroids sugiere la intención, pero el requisito no se infiere: se confirma con diseño. Si el diseño dijera que los asteroides deben seguir cayendo, el que está mal es el test.
(2) Causa: el pool se crea con SpawnAsteroid como función de creación (Spawner.cs 52–53), pero nunca se llama a Get(): SpawnAsteroid se usa directamente con Instantiate. ClearAsteroids llama a Dispose(), que vacía un pool que no contiene los asteroides en pantalla. Además, Laser.cs 52 hace Release de objetos que nunca se pidieron al pool: es la misma raíz del fallo de INT-AST-13.
(3) Impacto para el jugador: con un reinicio rápido, un asteroide viejo puede chocar la nave recién reparada en (0,0,0) y provocar un Game Over inmediato.
(4) Ticket: título, pasos, esperado/actual, evidencia (salida del test), severidad y prioridad.
(5) Regresión: el test queda en rojo hasta el arreglo y después protege contra la reaparición del defecto.
ACLARACIÓN: destruir los asteroides en ClearAsteroids resuelve INT-AST-14, pero no el doble Release de INT-AST-13. Arreglar el uso del pool ataca la causa común.""",

"Dependencias y dobles de prueba": """\
QUÉ SE TOCA: los tipos de dobles de prueba y cuándo usarlos en integración.
TEORÍA: un doble de prueba (test double, término de Gerard Meszaros difundido por Martin Fowler) reemplaza a un colaborador real durante el test.
- Dummy: solo ocupa un lugar.
- Stub: devuelve respuestas fijas.
- Spy: registra cómo se lo usó, para revisarlo después.
- Mock: tiene expectativas programadas y falla si no se cumplen.
- Fake: implementación simplificada pero que funciona.
REGLA PARA INTEGRACIÓN: lo que está en la costura que se quiere probar va REAL; se reemplaza solo lo no determinista o lo que queda fuera de alcance. Con demasiados dobles, el test deja de ser de integración y se vuelve unitario.
ACLARACIONES — dependencias reales del proyecto y su estrategia:
- Entrada (Ship.cs 61–71): reemplazar con un stub o evitarla.
- Azar (Spawner.cs 75 y 103): controlar con una semilla, sin doble.
- Tiempo (corrutinas de 0,4 s): esperar por condición.
- Física: WaitForFixedUpdate.
- Estado estático (Game.instance): resolver con la fixture.
Varios ejemplos de la tabla son PROPUESTA: Game usa métodos estáticos (GameOver, AsteroidDestroyed), que no se pueden reemplazar por un doble sin modificar el código.
El proyecto no tiene sistemas externos (red, archivos, tiendas); ese tema queda para una clase futura.""",

"Caso: la regla del cooldown vive junto al teclado": """\
QUÉ SE TOCA: una regla de juego que no se puede probar por cómo está escrita.
TEORÍA: una regla de juego es testeable cuando se puede ejecutar sin su fuente de entrada real. Si la regla está mezclada con la lectura del dispositivo, para probarla hay que simular el dispositivo. Separar «qué quiere hacer el jugador» de «cómo lo pide» crea una costura (seam) donde se puede enchufar un stub.
ACLARACIONES: la regla (canShoot) se evalúa en Update junto a Input.GetKey (Ship.cs 61). ShootLaser (77–80) no la respeta: dos llamadas seguidas crean dos láseres. Respuesta a la pregunta: 3 láseres en 1 s (t = 0; 0,4; 0,8).
Conexión con la clase de plataformas: la misma separación de la entrada que permite portar el juego a móvil es la que permite testear la regla.
DATOS VERIFICADOS: Packages/manifest.json no incluye el paquete Input System, así que la opción A requiere instalarlo (no hacerlo sin autorización). En el reporte regenerado, Ship.cs 61–74 no se ejecuta nunca: durante los tests la nave está «muerta» (isDead empieza en true y solo RepairShip lo cambia), así que Update termina en la línea 57.""",

"Cobertura: qué mide y qué no": """\
QUÉ SE TOCA: cómo leer un reporte de cobertura sin sobreestimarlo.
TEORÍA: la cobertura de código mide qué líneas (o métodos, o ramas) se EJECUTARON durante los tests. No mide si algún assert verificó su efecto. Sirve para encontrar código que ningún test toca; no sirve para afirmar que el código está bien probado.
Cobertura de líneas ≠ cobertura de ramas: una línea con un if puede ejecutarse sin recorrer sus dos salidas.
Para leer un reporte hay que saber de qué corrida viene: qué tests, qué assemblies y qué fecha.
ACLARACIONES:
- Reporte VIEJO (proyectos-unity/Asteroides/asteroide-final/CodeCoverage): combinaba 6 archivos de 3 carpetas de resultados (15/09 y 18/09), incluía el código de los tests y su vista línea por línea correspondía a una corrida de un solo test. Su 65,5 % no describía la suite.
- Reporte REGENERADO (7/7 PASS, solo GameAssembly, carpeta limpia): 137 de 186 líneas (73,6 %) y 27 de 31 métodos (87 %). Asteroid 84,2 %, Game 100 %, Laser 81,2 %, Ship 43 %, Spawner 86,9 %.
- Sin cubrir: Ship 61–74 (entrada) y 99–115 (movimiento lateral); Asteroid 48 (destrucción bajo y = −5); Spawner 69 (spawn automático); Laser 42 (láser fuera de pantalla).
- Respuesta a la pregunta: Game.cs tiene 100 %, pero la línea 85 (texto del HUD) se ejecuta en los tests 06 y 07 sin que ningún assert la compruebe. 100 % de cobertura no es 100 % verificado.
Paquete usado: Code Coverage 1.3.""",

"Regresión: del bug al test que lo vigila": """\
QUÉ SE TOCA: el ciclo que convierte un defecto encontrado en protección permanente.
TEORÍA (Unidad II): retesting = volver a probar el arreglo de un defecto concreto. Testing de regresión = volver a probar lo que ya funcionaba para detectar si un cambio lo rompió. Un test automatizado que nace de un bug cumple las dos funciones: primero confirma el arreglo y después queda vigilando.
ACLARACIONES: el orden importa. El test se ve primero en ROJO, con el defecto presente: esa es la prueba de que es capaz de detectarlo. Un test de regresión que nunca se vio fallar puede estar pasando por la razón equivocada (por ejemplo, porque no prepara bien el escenario).
APLICACIÓN: INT-AST-13, 14 y 15 ya están en rojo en IntegrationHypothesesTests.cs. Cuando se corrijan los defectos pasarán a verde y quedarán en la suite.""",

"Actividad 4 · Diseñar una mini-suite (14 min)": """\
OBJETIVO: priorizar y organizar una suite, no escribir código.
TEORÍA: una suite es un producto con costo: tiempo de ejecución y mantenimiento. Se organiza por propósito:
- Smoke: pocos tests rápidos que verifican que lo esencial funciona; corren en cada cambio.
- Integración: los flujos principales entre componentes.
- Borde: los límites y los casos raros.
- Regresión: defectos ya encontrados que no deben volver.
En Unity se pueden etiquetar con [Category("Smoke")] y filtrar al ejecutar.
RESULTADO ESPERADO: una tabla de hasta 12 tests con categoría, momento de ejecución y decisión (queda / reescribir / fusionar / sale).
PREGUNTAS PARA LA DISCUSIÓN: ¿fusionar dos tests mejora o empeora el diagnóstico cuando uno falla? ¿Qué se corre en cada commit y qué de noche?""",

"Actividad 4 · Resolución": """\
QUÉ SE TOCA: la resolución de la Actividad 4. Suite final: 11 tests.
ACLARACIONES — decisiones:
- El 03 sale: simula un Game Over que el juego no produce; el 08 cubre el mismo reinicio por el camino real.
- El 07 queda absorbido por el 09, que verifica el puntaje y el texto. En contra: si el 09 falla, hay que leer el mensaje del Assert para saber cuál de los dos efectos falló (se pierde granularidad).
- El 01 y el 05 verifican el movimiento de un solo componente: van a una carpeta de tests por componente, no a la de integración.
- El 04 se reescribe con la fixture de limpieza y contando solo los asteroides que crea el propio test.
- El 13, el 14 y el 15 ya se ejecutaron y FALLAN: quedan en rojo como regresión hasta que se corrijan los defectos.
- El 16 queda pendiente del refactor de la entrada.
CRITERIO GENERAL: independencia (cada test corre solo y en cualquier orden) y un nombre que diga qué flujo se prueba, en qué condición y con qué resultado: Flujo_Condición_Resultado.""",

"Cierre": """\
QUÉ SE TOCA: las cinco ideas de la clase.
TEORÍA — resumen:
(1) Una suite solo de casos positivos no prueba lo que el juego NO debe hacer.
(2) En integración, el borde también es tiempo, cantidad, repetición y orden.
(3) Sin fixtures que limpien, los tests se contaminan entre sí y se vuelven frágiles.
(4) Los dobles de prueba se usan para lo que no está bajo prueba, no para todo.
(5) La cobertura dice qué se ejecutó, no qué se verificó.
ACTIVIDAD: el ticket de salida pide transferir lo aprendido a un juego propio: un caso negativo y uno de borde.
PREGUNTA EXTRA: ¿qué test de la suite actual les da menos confianza y por qué?""",

"Anexo · Catálogo de casos nuevos": """\
QUÉ SE TOCA: referencia rápida de los 9 casos nuevos.
ESTADOS: PROPUESTA = el caso está diseñado pero todavía no existe en el proyecto. EJECUTADO · FAIL = el test existe en Assets/Tests/IntegrationHypothesesTests.cs, se corrió en Unity 6000.3.11f1 (batchmode) y falla porque documenta un defecto real.
RESULTADOS: 13 → excepción en Laser.cs:52 y puntaje 2. 14 → el asteroide de la partida anterior sobrevive a NewGame. 15 → 8 asteroides en 2,1 s con doble NewGame, contra 5 con uno.
ACLARACIÓN: 13 y 14 comparten la raíz: el ObjectPool del Spawner no se usa de forma consistente (nunca se llama a Get()).""",

"Anexo · Para una clase futura": """\
QUÉ SE TOCA: temas valiosos que no entran en esta clase.
ACLARACIONES:
- Sistemas externos (guardado del récord, tabla online): requieren fakes o entornos de prueba.
- Input System + InputTestFixture: permite simular teclado y táctil; requiere instalar el paquete.
- Tests parametrizados ([TestCase], [ValueSource]): evitan escribir un test por cada valor de borde.
- LogAssert: permite esperar o prohibir mensajes en el log (útil para INT-AST-13).
- Batchmode y CI: automatizan la ejecución en cada cambio.
- Cobertura de ramas: mide caminos, no solo líneas.
REFERENCIAS VERIFICADAS (versiones del proyecto: Test Framework 1.6.0, Code Coverage 1.3.0): docs.unity3d.com/Packages/com.unity.test-framework@1.6 · docs.unity3d.com/Packages/com.unity.inputsystem@1.11/manual/Testing.html · docs.unity3d.com/Packages/com.unity.test-framework@1.4/api/UnityEngine.TestTools.LogAssert.html · docs.unity3d.com/ScriptReference/Pool.ObjectPool_1.html · docs.unity3d.com/Packages/com.unity.testtools.codecoverage@1.3""",
}
