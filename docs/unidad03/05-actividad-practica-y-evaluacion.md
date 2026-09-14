# Unidad 3 — Actividad práctica y evaluación

Esta actividad es la base del **Trabajo Práctico N° 2**, que según el programa analítico cubre "Toda la Unidad 03" (a diferencia de Unidad 2, que compartía el TP N°1 con Unidad 1). El desarrollo del TP tiene, según el programa, entre 2 y 3 semanas — la actividad en clase (Sección R) es el punto de partida guiado; el resto se completa fuera del horario de clase.

---

## Sección R — Actividad práctica 1: suite de tests para `PlayerHealth`

**Formato:** equipos de 4-5 estudiantes (mismo criterio que Unidad 2). Cada equipo recibe el mismo punto de partida.

### Código entregado a cada equipo (con un bug deliberado)

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
        CurrentHealth = CurrentHealth - amount; // sin clamp — bug deliberado
    }

    public void Heal(int amount)
    {
        CurrentHealth = Mathf.Min(MaxHealth, CurrentHealth + amount);
    }
}
```

> **Nota para el docente:** este código es intencionalmente distinto del que se usó en la demostración en vivo (Bloque 7 del guion) — mismo bug conceptual (falta de clamp), pero presentado "en frío" para que cada equipo tenga que *encontrarlo*, no recordarlo de la demo.

### Consigna

1. Crear la carpeta `Tests` (Edit Mode) con su `.asmdef`, referenciando el ensamblado del código de juego.
2. Escribir una suite de tests (`PlayerHealthTests`) que cubra:
   - daño reduce la vida correctamente,
   - curación aumenta la vida correctamente,
   - la curación no supera el máximo,
   - el jugador muere (`IsDead == true`) al llegar a 0,
   - **valores inválidos:** ¿qué pasa si `TakeDamage` recibe un número negativo? ¿Y si `Heal` recibe 0?
3. Ejecutar la suite en Test Runner. Encontrar el test que falla (vida negativa al recibir más daño del que queda).
4. Corregir `PlayerHealth.TakeDamage` (agregar el clamp con `Mathf.Max`).
5. Ejecutar de nuevo — todos los tests deben pasar.
6. Agregar explícitamente un **test de regresión** con un nombre que documente el bug corregido, por ejemplo `TakeDamage_NeverGoesBelowZero_Regression`, para que quede protegido a futuro. (No es el mismo bug que CRYPT-202 del backlog de la Sección I del caso práctico — ese es sobre `Heal()`, no sobre `TakeDamage`; no le asignen ese ticket.)
7. Responder por escrito: ¿cuál de los tests que escribieron NO hubiera sido necesario si el código nunca cambia? (objetivo: que noten que la protección real está en los tests que cubren los casos límite, no en los "felices").

### Entregable

El script `PlayerHealthTests.cs` completo, una captura del Test Runner en verde, y las respuestas escritas del punto 7. Tiempo sugerido en clase: 15 minutos de trabajo en equipo (el resto se completa como parte del TP N° 2); cierre con 2 equipos mostrando su test de regresión.

---

## Sección S — Actividad práctica 2: TDD con el sistema de experiencia

**Objetivo:** experimentar el ciclo Red-Green-Refactor en primera persona, no solo verlo hecho por el docente.

### Consigna

**Feature:** "El jugador puede recibir experiencia y subir de nivel cada 100 puntos."

1. **RED:** cada equipo escribe, antes de programar nada, el test `GainExperience_IncreasesTotalExperience` (ver ejemplo en [`02-caso-practico-testing-videojuego.md`](./02-caso-practico-testing-videojuego.md), Sección H). Ejecutar y confirmar que falla (o no compila).
2. **GREEN:** implementar la clase `PlayerExperience` con lo mínimo indispensable para que ese test pase. Nada más — sin adelantarse al siguiente requisito.
3. **REFACTOR:** revisar el código recién escrito — ¿hay algo que mejorar sin cambiar el comportamiento? Ejecutar el test de nuevo para confirmar que sigue en verde.
4. Repetir el ciclo completo con el segundo requisito: subir de nivel al llegar a 100 XP.
5. **Extensión opcional (si el equipo termina antes):** ¿qué pasa si `GainExperience` recibe de una sola vez 250 puntos? ¿Debería subir dos niveles? Escribir primero el test que lo exige, después implementarlo.

### Entregable

Los dos scripts (`PlayerExperienceTests.cs` y `PlayerExperience.cs`), y una anotación breve de qué se hizo en cada paso del ciclo (para verificar que el equipo escribió el test *antes* del código, no después).

---

## Sección T — Evaluación

Esta clase alimenta el TP N° 2 (Unidad III completa, según cronograma) y la actividad de aula virtual de la semana.

### Parte conceptual

Preguntas cortas sobre: qué es una prueba unitaria, diferencia entre Edit Mode y Play Mode, qué es TDD, diferencia entre testing manual y automatizado, y qué NO resuelven las pruebas unitarias.

### Parte práctica

A partir de una clase C# simple no vista en clase (ej. un sistema de cooldown de habilidades), escribir al menos 3 tests con AAA correctamente aplicado, decidiendo de forma justificada si van en Edit Mode o Play Mode.

### Parte de análisis

Dado un bug real (se sugiere reutilizar 2-3 del backlog de Unidad 2, ej. CRYPT-102, CRYPT-105, CRYPT-111), el estudiante debe responder: **¿lo abordarían con unit test, integration test, automated test, manual QA o playtest? Justificar.**

| Bug (Unidad 2) | Respuesta esperada | Por qué |
|---|---|---|
| CRYPT-102 — el contador de pociones no se actualiza visualmente | Integration test (o QA manual si no se justifica el esfuerzo) | Involucra lógica + UI; un unit test de `Inventory` no alcanza a cubrir la actualización visual. |
| CRYPT-105 — el arquero dispara a través de paredes | Unit/integration test (Play Mode) | Es lógica de detección/estado, determinista y aislable — buen candidato, similar a `EnemyArcherTests`. |
| CRYPT-111 — caída de FPS en la sala del jefe | Ninguno de los anteriores cubre esto por sí solo — requiere testing de rendimiento y/o QA manual | Un unit test no mide fotogramas por segundo en condiciones reales de escena. |

### Rúbrica sugerida

| Criterio | Qué se observa |
|---|---|
| Corrección del test | El `Assert` verifica realmente lo que el nombre del test promete. |
| Aplicación de AAA | Arrange, Act y Assert están claramente separados y son legibles. |
| Elección de modo | Edit Mode / Play Mode elegido con criterio, no al azar. |
| Test de regresión | Nombrado de forma que documente qué bug protege, no genérico (`Test1`, `TestFix`). |
| Ciclo TDD | Evidencia de que el test se escribió antes del código (no una simulación posterior). |
| Análisis de casos | Justifica con criterio técnico, no solo intuición, qué tipo de prueba corresponde a cada bug. |

Consistente con la evaluación de proceso del programa (rúbricas por TP, autoevaluación de aula virtual, coevaluación grupal — Punto 5.3 del programa analítico), igual que en Unidad 2.

---

## Sección U — Errores conceptuales frecuentes

| Idea errónea | Corrección |
|---|---|
| "Unit test = probar el videojuego completo." | Un unit test prueba **una unidad aislada** de código (ej. un método). Probar el juego completo es testing de sistema o playtest. |
| "Play Mode siempre es mejor que Edit Mode." | Edit Mode es más rápido y debe preferirse siempre que el código no dependa de la escena en ejecución. Play Mode es *necesario* para `MonoBehaviour`, no *superior*. |
| "Automatizar testing elimina QA." | El QA manual y el playtesting siguen siendo insustituibles para UX, balance, sensación de juego y bugs visuales — la automatización libera tiempo, no reemplaza el criterio humano. |
| "Todos los bugs pueden detectarse con unit tests." | Solo los que dependen de lógica determinista y aislable. Bugs de física, animación, rendimiento o "feel" quedan fuera (ver Sección 11 del programa). |
| "TDD significa escribir tests después del código." | Es lo opuesto: en TDD el test se escribe **antes**, y guía la implementación mínima necesaria. |
| "Si todos los tests pasan, el videojuego no tiene bugs." | Las pruebas muestran la *presencia* de ciertos defectos, no su ausencia general (principio ya visto en Unidad 1) — solo cubren lo que efectivamente se testeó. |
| "Más tests siempre significa mejor calidad." | Un test mal diseñado (frágil, acoplado a implementación, no determinista) agrega mantenimiento sin agregar confianza real. Calidad > cantidad. |
| "Un test debe probar muchas cosas." | Un buen test verifica **un** comportamiento específico — facilita saber exactamente qué se rompió cuando falla. |
| "Los tests deben medir productividad." | Un test mide comportamiento del código, no el desempeño de quien lo escribió — usarlos así genera incentivos perversos (tests inflados o vacíos). |
| "Las pruebas unitarias son innecesarias en videojuegos." | Justo lo contrario: el desarrollo de un juego cambia con altísima frecuencia (balance, mecánicas, refactors) — eso es exactamente lo que más se beneficia de detectar regresiones rápido. |
