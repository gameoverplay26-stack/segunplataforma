# Bugs de Unidad 2 (backlog Cryptbound) y qué tipo de prueba corresponde

Estos bugs **no se implementan** en este proyecto — son material de análisis
para la Actividad T (evaluación). Sirven para practicar el criterio de
"¿con qué tipo de prueba abordaría esto?", no para escribir tests sobre
código que no existe acá.

| Bug (Unidad 2) | Descripción | Tipo de prueba | Por qué |
|---|---|---|---|
| CRYPT-102 | El contador de pociones no se actualiza visualmente | Integration test (o QA manual si no se justifica el esfuerzo) | Involucra lógica + UI; un unit test de `Inventory` no alcanza a cubrir la actualización visual. |
| CRYPT-105 | El arquero dispara a través de paredes | Unit / Integration test (Play Mode) | Es lógica de detección/estado, determinista y aislable. |
| CRYPT-111 | Caída de FPS en la sala del jefe | Testing de rendimiento y/o QA manual | Un unit test no mide fotogramas por segundo en condiciones reales de escena. |

No se crean tests artificiales para representar estos bugs: la actividad es
de análisis y justificación escrita, no de implementación.
