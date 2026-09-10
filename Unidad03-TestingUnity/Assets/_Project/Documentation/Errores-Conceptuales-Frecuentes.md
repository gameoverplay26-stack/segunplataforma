# Errores conceptuales frecuentes sobre testing

| Idea errónea | Corrección |
|---|---|
| "Unit test = probar el videojuego completo." | Un unit test prueba **una unidad aislada** de código (ej. un método). Probar el juego completo es testing de sistema o playtest. |
| "Play Mode siempre es mejor que Edit Mode." | Edit Mode es más rápido y debe preferirse siempre que el código no dependa de la escena en ejecución. Play Mode es *necesario* para `MonoBehaviour`, no *superior*. |
| "Automatizar testing elimina QA." | El QA manual y el playtesting siguen siendo insustituibles para UX, balance, sensación de juego y bugs visuales — la automatización libera tiempo, no reemplaza el criterio humano. |
| "Todos los bugs pueden detectarse con unit tests." | Solo los que dependen de lógica determinista y aislable. Bugs de física, animación, rendimiento o "feel" quedan fuera. |
| "TDD significa escribir tests después del código." | Es lo opuesto: en TDD el test se escribe **antes**, y guía la implementación mínima necesaria. |
| "Si todos los tests pasan, el videojuego no tiene bugs." | Las pruebas muestran la *presencia* de ciertos defectos, no su ausencia general — solo cubren lo que efectivamente se testeó. |
| "Más tests siempre significa mejor calidad." | Un test mal diseñado (frágil, acoplado a implementación, no determinista) agrega mantenimiento sin agregar confianza real. Calidad > cantidad. |
| "Un test debe probar muchas cosas." | Un buen test verifica **un** comportamiento específico — facilita saber exactamente qué se rompió cuando falla. |
| "Los tests deben medir productividad." | Un test mide comportamiento del código, no el desempeño de quien lo escribió. |
| "Las pruebas unitarias son innecesarias en videojuegos." | Justo lo contrario: el desarrollo de un juego cambia con altísima frecuencia (balance, mecánicas, refactors) — eso es exactamente lo que más se beneficia de detectar regresiones rápido. |

Fuente: `docs/unidad03/05-actividad-practica-y-evaluacion.md`, Sección U.
