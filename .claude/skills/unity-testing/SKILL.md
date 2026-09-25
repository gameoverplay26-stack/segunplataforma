---
name: unity-testing
description: Criterios de testing con Unity Test Framework para el proyecto Arena-SDD (Unity 6000.3.11f1). Edit Mode vs Play Mode, clasificación estricta Unit Test vs Integration Test, fixtures, SetUp/TearDown, determinismo, aislamiento, trazabilidad con IDs y ejecución en batchmode con evidencia. Úsalo al diseñar la Test Strategy, escribir o revisar tests, o ejecutar la suite.
---

# Unity testing — proyecto Arena

Aplica a `Arena-SDD/` y a `docs/05-testing/` / `docs/08-verification/`. Los tests de otros proyectos del repo (p. ej. `Unidad03-TestingUnity/`) son material de cátedra y no se rigen por esta skill.

## Clasificación: primero esto

Antes de escribir o nombrar un test, clasifícalo con [unit-vs-integration.md](unit-vs-integration.md).

Regla corta: **Integration Test = al menos dos componentes reales del juego colaborando a través de su integración real** (eventos, colisiones, referencias en escena). Un test sobre una sola clase, con o sin dobles, es **Unit**, aunque corra en Play Mode.

## Edit Mode vs Play Mode

| | Edit Mode | Play Mode |
|---|---|---|
| Qué ejecuta | Código sin el loop del juego | El loop de juego: `Update`, física, corrutinas |
| Ideal para | Lógica C# pura (salud, cooldowns, puntaje, targeting aislado) | MonoBehaviours, colisiones, flujos entre componentes |
| Velocidad | Rápido | Más lento |
| Assembly | `.asmdef` de tests con plataforma *Editor* | `.asmdef` de tests sin restricción *Editor* |

El modo **no** define si un test es unit o integration: lo define qué se ejercita.

## Buenas prácticas obligatorias

- **Determinismo:**
  - Sin `Random` sin seed y sin depender de `Time.deltaTime` real.
  - En Play Mode, esperar condiciones acotadas: `yield return` con límite de frames o tiempo, nunca esperas abiertas.
  - Sin dependencia del orden de ejecución entre tests.
- **Aislamiento:**
  - Cada test crea lo que usa y lo destruye en `[TearDown]` / `[UnityTearDown]` (`Object.Destroy` / `DestroyImmediate`).
  - Sin estado estático compartido entre tests.
- **Fixtures:**
  - `[SetUp]` / `[TearDown]` por test y `[OneTimeSetUp]` solo para recursos caros e inmutables.
  - Las escenas de test se cargan y descargan explícitamente.
- **Nombres:** `Metodo_Condicion_ResultadoEsperado`, por ejemplo `TakeDamage_WhenDamageExceedsHealth_RaisesDeathOnce`.
- **Trazabilidad:** `[Test, Property("Id", "TEST-UNIT-001"), Property("Trace", "REQ-###")]` (ver skill `sdd-workflow`, `traceability.md`).
- **Un comportamiento por test.** Aserciones con mensaje cuando el fallo no sea obvio.
- **No debilitar un test que falla** ni marcarlo `[Ignore]` sin autorización explícita.

## Límites (qué NO garantiza el testing)

- Una suite en verde no prueba ausencia de bugs: solo que los casos escritos se comportan como se especificó.
- Los unit tests no detectan fallos de integración, como eventos no suscriptos o referencias sin asignar en escena.
- La cobertura alta con aserciones débiles no aporta.

## Ejecución y evidencia (batchmode)

Editor instalado: `C:/Program Files/Unity/Hub/Editor/6000.3.11f1/Editor/Unity.exe`.

```bash
UNITY="/c/Program Files/Unity/Hub/Editor/6000.3.11f1/Editor/Unity.exe"
"$UNITY" -batchmode -projectPath Arena-SDD -runTests -testPlatform EditMode \
  -testResults docs/08-verification/evidence/<fecha>-editmode.xml \
  -logFile docs/08-verification/evidence/<fecha>-editmode.log
# Repetir con -testPlatform PlayMode
```

- No usar `-quit` junto con `-runTests`.
- El proyecto **no** debe estar abierto en el Editor durante la ejecución.
- La evidencia es el XML (resultado por test) más el log. "Pasó" sin XML equivale a `UNKNOWN`.
- La primera ejecución real de este comando en `Arena-SDD/` debe registrarse como VAL-### confirmando que los flags funcionan en esta instalación. Hasta entonces, el comando es **documentado pero no verificado** en este repo.
