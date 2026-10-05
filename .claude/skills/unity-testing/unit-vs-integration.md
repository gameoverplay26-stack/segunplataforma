# Unit Test vs Integration Test — criterio de clasificación

## Definiciones operativas (proyecto Arena)

**Unit Test:** verifica el comportamiento de **una unidad** (una clase o un método) aislada. Sus colaboradores, si los hay, son dobles (fakes/stubs/mocks) o valores simples.

**Integration Test:** verifica que **dos o más componentes reales** del juego colaboran correctamente a través de su mecanismo de integración real: eventos C#, colisiones o triggers de física, referencias entre GameObjects, carga de escena.

## Árbol de decisión

```text
¿Cuántos componentes reales del juego (no dobles) participan en lo que se afirma?
├── 1 → UNIT TEST (aunque corra en Play Mode, aunque use GameObjects)
└── ≥2 → ¿La aserción depende de la interacción entre ellos
          (evento emitido por A y consumido por B, colisión A→B, etc.)?
          ├── Sí → INTEGRATION TEST
          └── No (se prueban por separado en el mismo método) → son 2 UNIT TESTS mal agrupados: separarlos
```

## Ejemplos con componentes candidatos de Discovery (no son decisiones de arquitectura)

| Test | Clasificación | Motivo |
|---|---|---|
| `Health.TakeDamage` deja la vida en 0 y dispara `OnDeath` una vez | **Unit** (Edit Mode) | Una clase pura. |
| `Weapon.CanFire` respeta el cooldown | **Unit** (Edit Mode) | Una clase; el tiempo se inyecta. |
| Un Projectile en Play Mode que colisiona con un `FakeDamageable` y llama `TakeDamage` | **Unit** (Play Mode) | Un solo componente real; el objetivo es un doble. |
| Weapon dispara → Projectile impacta → `Enemy.Health` baja → `OnDeath` → `ScoreManager` suma | **Integration** (Play Mode) | Varios componentes reales, con evento y colisión reales. |
| El jugador muere → `GameManager` bloquea input y termina la partida | **Integration** (Play Mode) | Health + GameManager + input real. |
| `ScoreManager.AddPoints` suma, probado con un evento disparado a mano desde el test | **Unit** | El emisor no es un componente real. |

## Errores de clasificación frecuentes

| Error | Corrección |
|---|---|
| "Es Play Mode, entonces es integration." | El modo describe el entorno, no el alcance. |
| "Usa un GameObject, entonces es integration." | Un GameObject con un solo componente bajo prueba sigue siendo unit. |
| "Probé A y B en el mismo test." | Si no se afirma su interacción, son dos unit tests. |
| "El integration test reemplaza a los unit tests." | Son complementarios: el unit test localiza el defecto; el integration test detecta el cableado roto. |

## Qué documentar por test (Test Strategy)

`ID` · `Clasificación (Unit/Integration)` · `Modo (Edit/Play)` · `Componentes reales involucrados` · `Dobles usados` · `REQ/SPEC que verifica` · `Criterio de éxito`.
