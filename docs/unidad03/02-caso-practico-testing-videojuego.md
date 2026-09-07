# Unidad 3 — Caso práctico: pruebas unitarias sobre Cryptbound

Continúa el mismo proyecto de Unidad 2 — no se cambia de videojuego. El equipo de 7 personas siguió iterando: el vertical slice pasó de la build 0.3 (hito "Presentable", playtest documentado en Unidad 2) a la **build 0.4**, camino al hito "Final". Con más sistemas terminados, empezaron a aparecer regresiones que el playtest manual ya no detectaba a tiempo.

---

## Sección A — Por qué Cryptbound es un buen caso para esta unidad

Cryptbound ya tiene, desde Unidad 2, sistemas con lógica de reglas clara y determinista: vida, daño, inventario, detección de enemigos. Son exactamente el tipo de código que la Sección 9 del programa distingue como "buen candidato" para unit testing — en oposición a la física, la animación o el "feel" del combate, que Cryptbound también tiene pero que esta unidad **no** promete poder testear con NUnit.

## Sección B — Arquitectura simplificada (solo lo relevante para testing)

```
Cryptbound (build 0.4)
├── Assets/Scripts/            → código de producción (GameAssembly.asmdef)
│   ├── PlayerHealth.cs        → clase C# pura (no MonoBehaviour) — vida, daño, curación, muerte
│   ├── Inventory.cs           → clase C# pura — agregar/quitar objetos, capacidad
│   ├── CombatSystem.cs        → MonoBehaviour — ataque, cooldown, aplica daño al objetivo
│   ├── EnemyArcher.cs         → MonoBehaviour — estados (Patrulla/Alerta/Ataque), rango de detección
│   └── PlayerExperience.cs    → clase C# pura — sistema de XP (se construye con TDD en esta unidad)
└── Assets/Tests/               → código de prueba (Tests.asmdef, referencia a GameAssembly)
    ├── EditMode/
    │   ├── PlayerHealthTests.cs
    │   ├── InventoryTests.cs
    │   └── PlayerExperienceTests.cs
    └── PlayMode/
        ├── CombatSystemTests.cs
        └── EnemyArcherTests.cs
```

**Decisión de diseño deliberada y su porqué:** `PlayerHealth`, `Inventory` y `PlayerExperience` son clases C# comunes, **no heredan de `MonoBehaviour`**. Esto no es un detalle menor: es lo que permite probarlas en Edit Mode, sin instanciar una escena. `CombatSystem` y `EnemyArcher` sí son `MonoBehaviour` porque necesitan vivir en un `GameObject` de la escena (posición, colisiones, coroutines) — por eso sus tests van en Play Mode. Esta separación es, en sí misma, una buena práctica que se explicita en el guion docente (Bloque 6): **separar la lógica de reglas del código que depende del motor hace que esa lógica sea más fácil de probar**.

---

## Sección C — Sistema 1: `PlayerHealth` (el ejemplo central de la clase)

### Código de producción

```csharp
using UnityEngine;

public class PlayerHealth
{
    public int MaxHealth { get; }
    public int CurrentHealth { get; private set; }
    public bool IsDead => CurrentHealth <= 0;

    public PlayerHealth(int maxHealth)
    {
        MaxHealth = maxHealth;
        CurrentHealth = maxHealth;
    }

    public void TakeDamage(int amount)
    {
        CurrentHealth = Mathf.Max(0, CurrentHealth - amount);
    }

    public void Heal(int amount)
    {
        CurrentHealth = Mathf.Min(MaxHealth, CurrentHealth + amount);
    }
}
```

### Primer test (Edit Mode) — demostración pedagógica central (ver programa, punto 14)

```csharp
using NUnit.Framework;

public class PlayerHealthTests
{
    [Test]
    public void TakeDamage_ReducesHealthByAmount()
    {
        // Arrange
        var health = new PlayerHealth(maxHealth: 100);

        // Act
        health.TakeDamage(25);

        // Assert
        Assert.AreEqual(75, health.CurrentHealth);
    }
}
```

**Guion de la demostración en vivo (paso a paso, para reproducir en clase):**

1. Se escribe `PlayerHealth` sin tests todavía. Se pregunta: "¿cómo confirmamos que esto funciona?"
2. Se crea la carpeta `Tests` (Edit Mode) y `PlayerHealthTests.cs`, se escribe el test de arriba.
3. Se abre `Window ▸ General ▸ Test Runner`, pestaña **EditMode**, se ejecuta con **Run All**.
4. Resultado: ✅ **PASS** — círculo verde.
5. **Se provoca el fallo a propósito:** se cambia `Mathf.Max(0, CurrentHealth - amount)` por `CurrentHealth - amount` (se quita el clamp). Se agrega un segundo test:
   ```csharp
   [Test]
   public void TakeDamage_NeverGoesBelowZero()
   {
       var health = new PlayerHealth(maxHealth: 100);
       health.TakeDamage(150);
       Assert.AreEqual(0, health.CurrentHealth);
   }
   ```
6. Se ejecuta de nuevo: ❌ **FAIL** — el Test Runner muestra `Expected: 0, But was: -50`. Se lee el mensaje de error en voz alta con la clase: esto **es** la prueba unitaria funcionando como se espera, no un error del sistema.
7. Se corrige el código (se restaura `Mathf.Max`). Se ejecuta de nuevo: ✅ **PASS** en ambos tests.

Esta secuencia completa —código, test, PASS, fallo provocado, FAIL, corrección, PASS— es la que cada estudiante repite después, con variaciones, en la actividad práctica.

---

## Sección D — Ejemplos progresivos de mecánicas (Edit Mode)

**Ejemplo 1 — Daño**
```
Arrange: PlayerHealth con 100 HP
Act:     TakeDamage(30)
Assert:  CurrentHealth == 70
```

**Ejemplo 2 — Curación**
```csharp
[Test]
public void Heal_IncreasesHealthByAmount()
{
    var health = new PlayerHealth(100);
    health.TakeDamage(50); // 50/100
    health.Heal(20);
    Assert.AreEqual(70, health.CurrentHealth);
}
```

**Ejemplo 3 — No superar el máximo**
```csharp
[Test]
public void Heal_DoesNotExceedMaxHealth()
{
    var health = new PlayerHealth(100);
    health.TakeDamage(10); // 90/100
    health.Heal(30);       // intenta pasarse de 100
    Assert.AreEqual(100, health.CurrentHealth);
}
```

**Ejemplo 4 — Muerte**
```csharp
[Test]
public void TakeDamage_SetsIsDead_WhenHealthReachesZero()
{
    var health = new PlayerHealth(20);
    health.TakeDamage(20);
    Assert.IsTrue(health.IsDead);
}
```

## Sección E — Sistema 2: `Inventory` (Edit Mode)

Código de producción mínimo, alineado al inventario de pociones ya presente en el backlog de Cryptbound (Unidad 2, CRYPT-102 y CRYPT-109):

```csharp
using System.Collections.Generic;

public class Inventory
{
    private readonly Dictionary<string, int> items = new();
    public int Capacity { get; }

    public Inventory(int capacity) => Capacity = capacity;

    public bool AddItem(string itemName, int quantity = 1)
    {
        int totalItems = 0;
        foreach (var kv in items) totalItems += kv.Value;
        if (totalItems + quantity > Capacity) return false;

        items.TryGetValue(itemName, out int current);
        items[itemName] = current + quantity;
        return true;
    }

    public bool RemoveItem(string itemName, int quantity = 1)
    {
        if (!items.TryGetValue(itemName, out int current) || current < quantity) return false;
        items[itemName] = current - quantity;
        return true;
    }

    public int GetQuantity(string itemName) => items.TryGetValue(itemName, out int q) ? q : 0;
}
```

**Ejemplo 5 — Inventario**
```csharp
[Test]
public void AddItem_PotionIsInInventory()
{
    var inventory = new Inventory(capacity: 10);
    inventory.AddItem("Potion");
    Assert.AreEqual(1, inventory.GetQuantity("Potion"));
}

[Test]
public void AddItem_RespectsCapacity()
{
    var inventory = new Inventory(capacity: 1);
    inventory.AddItem("Potion");
    bool added = inventory.AddItem("Sword"); // ya no hay espacio
    Assert.IsFalse(added);
}
```

---

## Sección F — Sistema 3: `CombatSystem` y el bug de regresión (Play Mode)

Este es el hilo narrativo central de la unidad (Sección 6 del encargo). Retoma explícitamente el problema de las regresiones.

### Versión 1 — funciona correctamente

```csharp
using UnityEngine;

public class CombatSystem : MonoBehaviour
{
    public float cooldownSeconds = 1f;
    private float lastAttackTime = -999f;

    public bool TryAttack(PlayerHealth target, int damage)
    {
        if (Time.time - lastAttackTime < cooldownSeconds) return false;

        target.TakeDamage(damage);
        lastAttackTime = Time.time;
        return true;
    }
}
```

### Se modifica CombatSystem (build 0.4): se agrega un "golpe crítico" con probabilidad

Iñaki (programador de gameplay) agrega la mecánica de crítico pedida por Valentina (diseño). En el apuro, introduce un bug:

```csharp
public bool TryAttack(PlayerHealth target, int damage)
{
    if (Time.time - lastAttackTime < cooldownSeconds) return false;

    target.TakeDamage(damage);
    if (Random.value < 0.2f)
    {
        target.TakeDamage(damage); // "golpe crítico" — pero esto duplica el daño normal, no lo aumenta
    }
    lastAttackTime = Time.time;
    return true;
}
```

**El bug real (CRYPT-201, ver Sección I):** el "crítico" no multiplica el daño de un solo golpe — aplica el método `TakeDamage` **dos veces**, lo cual además rompe silenciosamente cualquier lógica futura que dependa de "un golpe = una llamada a TakeDamage" (por ejemplo, contadores de combos). Es exactamente el patrón de la Sección 6 del encargo: `Player.TakeDamage()` funcionaba correctamente en la build 0.3; una modificación de `CombatSystem` en 0.4 lo rompió sin que nadie tocara `PlayerHealth`.

### El test que lo detecta (Play Mode, porque `CombatSystem` es un `MonoBehaviour`)

```csharp
using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

public class CombatSystemTests
{
    [UnityTest]
    public IEnumerator TryAttack_AppliesDamageExactlyOnce()
    {
        // Arrange
        var combatGO = new GameObject();
        var combat = combatGO.AddComponent<CombatSystem>();
        var target = new PlayerHealth(maxHealth: 100);

        // Act
        combat.TryAttack(target, damage: 20);
        yield return null; // deja pasar un frame

        // Assert
        Assert.AreEqual(80, target.CurrentHealth); // falla si el crítico duplicó el daño a 60
    }
}
```

Con la probabilidad de crítico activa, este test falla de forma intermitente (a veces 80, a veces 60) — lo cual, discutido en clase, es en sí mismo un segundo error conceptual útil: **un test que depende de `Random` es un test frágil** (no determinista). La corrección de diseño real es separar "decidir si hay crítico" (que si se quiere probar, se hace inyectando o mockeando el generador aleatorio — fuera del alcance de esta unidad) de "aplicar daño" (que debe llamarse una sola vez, con el monto ya calculado):

```csharp
public bool TryAttack(PlayerHealth target, int damage)
{
    if (Time.time - lastAttackTime < cooldownSeconds) return false;

    int finalDamage = Random.value < 0.2f ? damage * 2 : damage; // el crítico se decide antes
    target.TakeDamage(finalDamage); // TakeDamage se llama una sola vez, siempre

    lastAttackTime = Time.time;
    return true;
}
```

Con este fix, el test anterior deja de ser válido tal cual (ahora 80 *o* 40, nunca 60) — lo cual es la excusa perfecta para introducir en clase el matiz de **tests deterministas**: se reemplaza `Random.value` por un parámetro inyectado en el test, o se separa la prueba en "sin crítico, aplica daño exacto" fijando la probabilidad a 0 desde el test. No hace falta resolverlo con herramientas de mocking — alcanza con exponer un método interno testeable.

## Sección G — Sistema 4: `EnemyArcher` (Play Mode, estados)

Retoma directamente el caso TC-E01 de Unidad 2 (rango de detección del arquero, partición de equivalencia + valores frontera).

```csharp
using UnityEngine;

public enum EnemyState { Patrol, Alert, Attack }

public class EnemyArcher : MonoBehaviour
{
    public float detectionRange = 6f;
    public EnemyState CurrentState { get; private set; } = EnemyState.Patrol;
    public Transform player;

    void Update()
    {
        float distance = Vector3.Distance(transform.position, player.position);
        CurrentState = distance <= detectionRange ? EnemyState.Alert : EnemyState.Patrol;
    }
}
```

```csharp
[UnityTest]
public IEnumerator EnemyArcher_EntersAlertState_AtExactDetectionRange()
{
    // Arrange — reutiliza el valor frontera de Unidad 2: tile 6 (6 unidades)
    var enemyGO = new GameObject();
    var archer = enemyGO.AddComponent<EnemyArcher>();
    var playerGO = new GameObject();
    archer.player = playerGO.transform;

    playerGO.transform.position = new Vector3(6f, 0, 0); // justo en el borde

    // Act
    yield return null; // deja correr un frame de Update()

    // Assert
    Assert.AreEqual(EnemyState.Alert, archer.CurrentState);
}
```

Este test **no existiría sin Unidad 1 y 2**: la posición exacta que se elige para el `Arrange` (`6f`, ni 5 ni 7) es directamente la técnica de valores frontera ya enseñada — la Unidad 3 no la reemplaza, la ejecuta como código.

---

## Sección H — TDD aplicado: `PlayerExperience` (el ciclo completo)

Feature pedida por Valentina: *"El jugador puede recibir experiencia y subir de nivel"* — mismo feature del encargo pedagógico (Sección 19), llevado a Cryptbound.

### RED — se escribe el test antes de que exista la clase

```csharp
[Test]
public void GainExperience_IncreasesTotalExperience()
{
    var xp = new PlayerExperience();
    xp.GainExperience(30);
    Assert.AreEqual(30, xp.CurrentExperience);
}
```
Al ejecutar: **no compila** (la clase `PlayerExperience` no existe todavía). Esto también cuenta como RED — el ciclo empieza en rojo, sea por fallo de compilación o por assertion fallida.

### GREEN — la implementación mínima que hace pasar el test, nada más

```csharp
public class PlayerExperience
{
    public int CurrentExperience { get; private set; }
    public void GainExperience(int amount) => CurrentExperience += amount;
}
```
Se ejecuta: ✅ PASS. Deliberadamente **no** se agrega todavía el nivel ni el umbral — eso no lo pide el test actual.

### REFACTOR — nada que mejorar aún (el código ya es mínimo); se repite el ciclo con el siguiente requisito

**RED 2:**
```csharp
[Test]
public void GainExperience_LevelsUp_WhenThresholdReached()
{
    var xp = new PlayerExperience(); // nivel inicial 1, umbral 100
    xp.GainExperience(100);
    Assert.AreEqual(2, xp.Level);
}
```
FAIL: `PlayerExperience` no tiene `Level`.

**GREEN 2:**
```csharp
public class PlayerExperience
{
    public int CurrentExperience { get; private set; }
    public int Level { get; private set; } = 1;
    private const int ExperiencePerLevel = 100;

    public void GainExperience(int amount)
    {
        CurrentExperience += amount;
        if (CurrentExperience >= ExperiencePerLevel)
        {
            Level++;
            CurrentExperience -= ExperiencePerLevel;
        }
    }
}
```
PASS en ambos tests.

**REFACTOR 2:** con los dos tests en verde como red de seguridad, se anima a la clase a proponer una mejora (ej. soportar subir *varios* niveles de una vez si la ganancia de XP es muy grande) y a escribir primero el test que lo exige — cerrando el ciclo una vuelta más frente a la clase.

---

## Sección I — Backlog de bugs de la build 0.4 (continúa la numeración de Unidad 2)

| ID | Título | Detectado por | Sistema | Severidad | ¿Protegido por unit test tras el fix? |
|---|---|---|---|---|---|
| CRYPT-201 | El "golpe crítico" duplica el daño aplicando `TakeDamage` dos veces | Playtest + regresión no detectada a tiempo | Combat | Alta | Sí — `TryAttack_AppliesDamageExactlyOnce` |
| CRYPT-202 | `Heal()` permite superar la vida máxima si se llama justo al límite | Unit test durante desarrollo (nunca llegó a jugarse) | Player | Media | Sí — `Heal_DoesNotExceedMaxHealth` |
| CRYPT-203 | El arquero queda en `Patrol` un frame de más al entrar exactamente en el rango | Unit test (valor frontera) | Enemy | Baja | Sí — `EnemyArcher_EntersAlertState_AtExactDetectionRange` |

**Lectura pedagógica de la tabla:** CRYPT-201 es el caso "de libro" de una regresión detectada tarde, sin protección. CRYPT-202 y CRYPT-203 son la contracara: bugs que **ni siquiera llegaron a un playtest** porque el test los atrapó durante el desarrollo — el argumento más fuerte a favor de escribir tests junto con el código, no después.

---

## Sección J — Qué de Cryptbound NO se testea con NUnit en esta unidad (y por qué)

- **Animación de impacto del arma** (Sección 9, "más complejos para unit testing"): se verifica jugando, no con `Assert`.
- **Sensación del cooldown de ataque** ("¿se siente lento?", queja real del informe de playtest de Unidad 2): es una opinión de diseño/balance, no un comportamiento verificable con una aserción — mismo criterio que Unidad 2 usó para descartarla como bug.
- **Iluminación de la sala del jefe y caída de FPS (CRYPT-111, Unidad 2):** es un problema de rendimiento; un unit test no mide frames por segundo en condiciones reales de escena.
- **Si el juego "es divertido":** ninguna prueba unitaria responde esa pregunta — la responde el playtest.

Esta sección se retoma explícitamente en el guion docente y en la actividad práctica para que quede instalada como límite real, no como comentario al pasar.
