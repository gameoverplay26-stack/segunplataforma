# Unidad03-TestingUnity

Proyecto práctico de la Unidad 3 — **Pruebas Unitarias, Unity Test Runner y TDD**.
Fuente pedagógica principal: `docs/unidad03/05-actividad-practica-y-evaluacion.md`
(cátedra "Diseño según Plataformas de Juego", UNJu).

## Unity Version

```
6000.3.11f1 LTS
```

No usar una versión distinta. No hay dependencias que requieran actualizarla.

## Objetivo

No es un videojuego. Es un proyecto para practicar, paso a paso:
Edit Mode, Play Mode, patrón AAA, detección y corrección de bugs mediante
tests, tests de regresión, casos límite, valores inválidos y TDD
(Red-Green-Refactor).

## Estructura

```
Assets/_Project/
├── Runtime/
│   ├── Player/
│   │   └── PlayerHealth.cs        → Actividad R (con bug deliberado)
│   ├── Systems/
│   │   ├── AbilityCooldown.cs     → Actividad T (práctica de evaluación)
│   │   └── PlayerExperience.LEEME.md → Actividad S (se construye con TDD)
│   ├── PlayModeDemo/
│   │   └── FrameCounter.cs        → ejemplo mínimo de por qué hace falta Play Mode
│   └── Game.Runtime.asmdef
├── Tests/
│   ├── EditMode/
│   │   ├── Game.Tests.EditMode.asmdef
│   │   └── LEEME.md               → qué tests escribir (PlayerHealth, PlayerExperience)
│   └── PlayMode/
│       ├── Game.Tests.PlayMode.asmdef
│       └── FrameCounterTests.cs
├── Scenes/
│   └── PlayModeDemo.unity
└── Documentation/
    ├── Bugs-CRYPT-y-Tipos-de-Testing.md
    └── Errores-Conceptuales-Frecuentes.md
```

## Runtime vs. Tests

`Game.Runtime` es el código de producción. `Game.Tests.EditMode` y
`Game.Tests.PlayMode` referencian a `Game.Runtime`, nunca al revés — evita
que el juego final arrastre dependencias de NUnit/Test Framework.

## Edit Mode

Se usa para lógica pura que no depende de la escena, un `GameObject` ni el
ciclo de ejecución de Unity: `PlayerHealth`, `PlayerExperience`,
`AbilityCooldown`. Es más rápido y debe preferirse siempre que sea posible.

## Play Mode

Necesario quando la lógica sí depende del entorno de ejecución real de
Unity. Ejemplo mínimo: `FrameCounter`, un `MonoBehaviour` cuyo `Update()`
solo se ejecuta si Unity está corriendo el ciclo de frames — no se puede
verificar en Edit Mode. Play Mode no es "mejor" que Edit Mode: es necesario
cuando el comportamiento depende del runtime.

## Unity Test Runner

`Window → General → Test Runner` (Unity 6000.3.x). Dos pestañas: EditMode
y PlayMode, cada una lista los tests del ensamblado correspondiente.

## Actividad R — PlayerHealth

`PlayerHealth.TakeDamage` tiene un bug deliberado (no hace clamp del daño,
la vida puede quedar negativa). **No corregirlo de entrada.** La consigna
completa está en `docs/unidad03/05-actividad-practica-y-evaluacion.md`,
Sección R: escribir `PlayerHealthTests.cs`, encontrar el fallo en el Test
Runner, corregir con `Mathf.Max(0, CurrentHealth - amount)`, volver a
ejecutar, y agregar un test de regresión nombrado según el bug que protege.

## Actividad S — PlayerExperience (TDD)

`PlayerExperience.cs` todavía no existe — se construye en clase siguiendo
RED → GREEN → REFACTOR. Ver
`Assets/_Project/Runtime/Systems/PlayerExperience.LEEME.md` y la Sección S
del material.

## Actividad T — AbilityCooldown

`AbilityCooldown.cs` es una clase de práctica para la evaluación: escribir
al menos 3 tests AAA, decidiendo con criterio Edit Mode o Play Mode. No es
la evaluación en sí — sirve para practicar antes de recibir una clase
similar no vista.

## Orden recomendado

1. Introducción al testing
2. `PlayerHealth`
3. Escribir los tests
4. Test Runner
5. Detectar el bug
6. Corregir el bug
7. Test de regresión
8. `PlayerExperience`
9. TDD — RED
10. TDD — GREEN
11. TDD — REFACTOR
12. Segundo requisito (subir de nivel)
13. Edit Mode (repaso de criterio)
14. Play Mode (`FrameCounter`)
15. `AbilityCooldown`
16. Preparación de evaluación
