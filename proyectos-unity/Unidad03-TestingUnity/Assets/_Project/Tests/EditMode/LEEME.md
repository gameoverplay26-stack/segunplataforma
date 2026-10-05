# Tests/EditMode — infraestructura lista, tests por escribir

El ensamblado `Game.Tests.EditMode` ya está configurado y referencia a
`Game.Runtime`. Acá van los scripts de test que cada equipo escribe:

## PlayerHealthTests.cs (Actividad R)

Cubrir, según la consigna de `05-actividad-practica-y-evaluacion.md`:

- el daño reduce la vida correctamente;
- la curación aumenta la vida correctamente;
- la curación no supera el máximo;
- el jugador muere (`IsDead == true`) al llegar a 0;
- `TakeDamage` con un valor negativo;
- `Heal(0)`;
- daño superior a la vida disponible;
- (después de corregir el bug) un test de regresión nombrado para
  documentar qué protege, por ejemplo
  `TakeDamage_NeverGoesBelowZero_RegressionCRYPT202`.

Usar AAA explícito (`// Arrange`, `// Act`, `// Assert`) en cada test.

## PlayerExperienceTests.cs (Actividad S)

Ver `Assets/_Project/Runtime/Systems/PlayerExperience.LEEME.md` — el test
se escribe **antes** que la clase (RED), no después.
