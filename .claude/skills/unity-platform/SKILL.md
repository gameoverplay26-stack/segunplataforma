---
name: unity-platform
description: Diseño multiplataforma PC → Mobile del proyecto Arena-SDD. Separar el input (teclado/mouse, joystick virtual/touch) del gameplay mediante una abstracción común, evitar duplicar lógica por plataforma y concentrar las pruebas en la lógica común. Úsalo al especificar o implementar input, controles, UI táctil o la fase Platform Adaptation. No decide qué mecanismo de abstracción se usa (decisión pendiente número 5 de Discovery).
---

# Unity platform — separación de input y gameplay

## Modelo

```text
PC Input (Keyboard + Mouse)          Mobile Input (Virtual Joystick + Touch)
             \                                  /
              →  Abstracción de input común   ←
                           ↓
        Gameplay (independiente de la plataforma)
```

Solo los **proveedores de input** conocen la plataforma. El gameplay consume intenciones (dirección de movimiento, dirección de apuntado, acción de ataque o disparo, etc.), nunca dispositivos.

## Decisión pendiente: NO resolverla aquí

El mecanismo concreto de la abstracción es la **decisión pendiente Discovery #5**. Se resuelve en Technical / Architecture Specification, por el usuario. Las opciones registradas son:

- una interfaz propia inyectada (Discovery la nombra tentativamente `IPlayerInputSource`);
- el Input System de Unity con Action Maps / Control Schemes.

Mientras no esté resuelta, presenta ambas opciones con sus consecuencias y **no elijas**. Una vez aprobada, aplica la elegida de forma consistente.

## Reglas

1. **Ningún tipo de gameplay** referencia `Keyboard`, `Mouse`, `Touchscreen`, `Gamepad`, `UnityEngine.Input` ni `Application.platform`. Esos tipos solo aparecen en los proveedores de input o en la configuración de plataforma.
2. **Sin ramas por plataforma en el gameplay:** nada de `#if UNITY_ANDROID` / `UNITY_IOS` / `UNITY_STANDALONE` en la lógica del juego. Las directivas, si hacen falta, van en la capa de input, UI o bootstrap.
3. **Sin clases duplicadas por plataforma** (`PlayerControllerPC` / `PlayerControllerMobile`). Si aparece esa necesidad, es un defecto de la abstracción: se registra como DEC o DEV, no se duplica.
4. Los **proveedores de input son delgados**: traducen la entrada cruda a intenciones y nada más. No hay reglas de juego en ellos.
5. **Tests sobre la lógica común:** el gameplay se prueba con un proveedor de input falso, determinista. Los proveedores concretos se prueban aparte, en poca cantidad, y solo si tienen lógica propia (p. ej. zona muerta del joystick).
6. La **UI táctil** (joystick virtual, botones) es parte del proveedor Mobile, no del gameplay.
7. Platform Adaptation se considera correcta solo si:
   - la suite existente sigue en verde **sin modificar los tests de gameplay**;
   - no aparecen clases de gameplay nuevas por plataforma.

## Checklist de revisión (spec o código)

- [ ] ¿El gameplay depende solo de la abstracción de input aprobada?
- [ ] ¿Hay referencias a dispositivos o a la plataforma fuera de la capa de input?
- [ ] ¿Hay `#if` de plataforma en el gameplay?
- [ ] ¿Hay clases o métodos duplicados por plataforma?
- [ ] ¿Los tests de gameplay usan un input falso y no dependen del dispositivo?
- [ ] ¿La adaptación a Mobile cambió algún test de gameplay? Si cambió, justificar como DEV.
