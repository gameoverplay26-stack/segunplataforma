# Unidad 2 — Actividad práctica y evaluación

## Sección R — Actividad práctica

Equipos de 4–5 estudiantes. Cada equipo recibe el mismo "informe de playtest" crudo: una lista desordenada, en lenguaje coloquial, de lo que distintos jugadores dijeron durante una prueba de Cryptbound.

### Informe de playtest crudo (entregado a cada equipo)

- "No se ve bien el texto cuando hablo con el NPC en mi monitor viejo."
- "Se traba re feo cuando entro al cuarto del jefe."
- "Guardé la partida, la cargué de nuevo y aparecí afuera del mapa, tuve que reiniciar todo."
- "El juego se cerró solo cuando quise abrir el inventario mientras cargaba un golpe."
- "El arquero me pegó de un tiro atravesando la pared, no lo vi venir."
- "Cuando tomo una poción no cambia el numerito en la pantalla."
- "El jefe murió pero no pasó nada, ni animación ni nada, quedé esperando."
- "Ojo que dice 'presioná E' en el tutorial pero en realidad es F."
- "A veces cuando clickeo dos veces rápido para atacar me gasta dos pociones."
- "Se escuchan los pasos aunque estoy parado sin moverme, es medio molesto."
- "Yo también me choqué contra una esquina y quedé del otro lado de la pared, raro."
- "Che, el combate se siente lento, ¿no le pueden bajar el cooldown al ataque?"

> **Nota para el docente:** el último ítem es intencionalmente *una opinión de diseño*, no un bug — sirve para que los equipos practiquen descartar lo que no corresponde a un ticket de QA.

### Consigna

1. Convertir cada queja relevante en un ticket completo (título, pasos de reproducción, resultado esperado vs. real, entorno).
2. Clasificar cada ticket por categoría, severidad, prioridad y dificultad estimada.
3. Identificar duplicados (dos quejas describen el mismo bug) y descartar lo que no es un bug de QA.
4. Redactar un mini plan de pruebas para el próximo ciclo: alcance, criterios de aceptación, cronograma breve.
5. Diseñar 3 casos de prueba (uno de acción, uno de RPG, uno de estrategia) para el sistema con más bugs reportados.
6. Simular una reunión de triage: decidir, con justificación, qué 3 bugs se atacan primero.
7. Mover los tickets a través de un tablero simulado (Nuevo → En progreso → En revisión → Cerrado), en una planilla compartida o post-its.
8. Responder por escrito: ¿qué se habría perdido si esto solo hubiera vivido en un chat grupal?

### Entregable

Una plantilla (papel o planilla digital) con: la tabla de tickets clasificados, el mini plan de pruebas, los 3 casos de prueba y la justificación del triage. Tiempo sugerido: 20 minutos de trabajo en equipo dentro de la clase; cierre con 2 equipos compartiendo su triage al resto.

---

## Sección S — Evaluación de los estudiantes

Esta clase alimenta el Trabajo Práctico N°1 (Unidades I y II, según cronograma del programa) y la actividad de aula virtual de la semana.

### Rúbrica sugerida para la actividad práctica

| Criterio | Qué se observa |
|---|---|
| Calidad del ticket | Pasos reproducibles, resultado esperado/real, entorno especificado. |
| Clasificación correcta | Severidad y prioridad justificadas de forma independiente, no confundidas. |
| Detección de ruido | Identifica duplicados y descarta lo que no es un bug (la opinión de diseño). |
| Plan y casos de prueba | Estructura completa; casos de prueba con todos los campos pedidos por el programa. |
| Criterio de triage | La justificación de qué se ataca primero pondera severidad, prioridad y dificultad — no solo una de las tres. |

Consistente con la evaluación de proceso del programa (rúbricas por TP, autoevaluación de aula virtual, coevaluación grupal — ver Punto 5.3 del programa analítico).
