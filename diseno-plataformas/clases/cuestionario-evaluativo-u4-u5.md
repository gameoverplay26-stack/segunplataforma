# Cuestionario evaluativo — Unidades 4 y 5

**Diseño según Plataformas de Juego · FI – UNJu · 2026**
Unidad 4: Plataforma móvil · Unidad 5: Consolas · Laboratorio de adaptación (Asteroides y 2D Platformer en PC, Android y Xbox)

Nombre y apellido: ______________________________  LU: __________  Fecha: ____/____/2026

**Instrucciones**
- 20 preguntas en tres partes. Duración sugerida: 60 minutos.
- Parte A: marcá **una sola** opción.
- Parte B: marcá V o F. **Si es falsa, justificá en una línea**; sin justificación, la respuesta vale la mitad.
- Parte C: respondé en 3 a 5 líneas.

| Parte | Preguntas | Puntaje |
|---|---|---|
| A. Opción múltiple | 1 a 8 | 8 × 4 = 32 |
| B. Verdadero o falso | 9 a 15 | 7 × 4 = 28 |
| C. Respuesta corta | 16 a 20 | 5 × 8 = 40 |
| **Total** | | **100** |

---

## Parte A — Opción múltiple

**1.** Asteroides corre a 60 fps al empezar en un teléfono, pero a los 8 minutos baja a 35–40 fps. En el Editor de la PC marcaba 200 fps. ¿Cuál es la explicación más probable?

- a) El Editor mide mal los fps y el teléfono siempre estuvo a 40.
- b) El teléfono se calienta, el SoC baja sus relojes (*throttling*) y cae el rendimiento sostenido.
- c) Unity móvil limita el juego a 30 fps desde el primer minuto.
- d) El juego tiene un error de lógica que aparece después de 8 minutos.

**2.** En los Player Settings de Android de Asteroides, la opción **ARM64** aparece en gris y no se puede tildar. ¿Por qué?

- a) Porque el Minimum API Level es demasiado bajo.
- b) Porque está tildado "Build App Bundle".
- c) Porque el Scripting Backend es Mono; ARM64 se habilita solo con IL2CPP.
- d) Porque Active Input Handling está en "Both".

**3.** ¿Qué permite comprobar el **Device Simulator** de Unity?

- a) El rendimiento y la temperatura del teléfono.
- b) El layout de la UI y la safe area en distintas pantallas.
- c) Mover y disparar con dos dedos a la vez.
- d) El consumo de memoria real del dispositivo.

**4.** Sobre los documentos de Microsoft para Xbox, ¿cuál afirmación es correcta?

- a) Los XR (Xbox Requirements) son obligatorios para certificar; las XAG (accesibilidad) son recomendaciones de buenas prácticas.
- b) Las XAG son obligatorias y los XR son opcionales.
- c) Cumplir todas las XAG garantiza la certificación.
- d) Los XR y las XAG son el mismo documento con dos nombres.

**5.** El requisito **XR-130** pide los mismos modos de juego en todos los modelos de una generación (por ejemplo, Series S y Series X). ¿Qué consecuencia tiene para el diseño?

- a) Hay que publicar dos juegos distintos, uno por modelo.
- b) El modelo más débil (Series S, 10 GB) fija el piso de lo que el juego puede ofrecer.
- c) La Series X puede tener modos de juego exclusivos.
- d) Ninguna: solo afecta a la tienda.

**6.** ¿Qué vía se usó en la cátedra para llevar Asteroides y el Platformer a una Xbox Series X?

- a) GDK con el programa ID@Xbox y un kit de desarrollo.
- b) Publicación en la Microsoft Store.
- c) Developer Mode en la consola y un paquete UWP (`.msix`) instalado desde el Device Portal por la red local.
- d) Streaming del juego desde la PC con Xbox Cloud Gaming.

**7.** En la primera corrida de los tests de **Asteroides de consola**, 5 tests fallaron porque el juego se pausaba solo al cargar la escena. ¿Cuál era la causa?

- a) El mando de Xbox no estaba conectado a la PC durante los tests.
- b) Al ocultar el joystick táctil fuera del móvil, se quitaba su gamepad virtual y la capa de consola lo interpretaba como un mando desconectado.
- c) `Ship.cs` llamaba a la pausa en cada frame.
- d) Unity no soporta tests de Play Mode en proyectos UWP.

**8.** Al portear el **2D Platformer** a Android, dos tests de Play Mode fallaron (`GroundRay_InMidAir_HitsNothing` y `SecondJumpIntent_InAir_DoubleJumpsOnlyOnce`). ¿Qué revelaron?

- a) Que los botones táctiles ◀ ▶ no funcionaban.
- b) Que el porteo había roto el salto.
- c) Un defecto del juego original: el rayo de `IsGrounded()` golpeaba el collider del propio jugador, por eso el salto era infinito.
- d) Que el Input System no lee el botón Sur del gamepad.

---

## Parte B — Verdadero o falso (si es F, justificá)

**9.** ___ En el porteo de Asteroides a Android, `Ship.cs` dejó de leer `Input.GetKey` y pasó a recibir la intención con `SetIntent(mover, disparar)`; los métodos `MoveLeft`, `MoveRight` y `ShootLaser` no cambiaron.

**10.** ___ Los controles en pantalla (`OnScreenStick` y `OnScreenButton`) simulan un gamepad virtual; por eso el adaptador de entrada no distingue el dedo de un gamepad físico.

**11.** ___ En Unity 6.3, Active Input Handling = "Both" está soportado oficialmente en Android, y por eso se usó también en el Platformer v2.

**12.** ___ Para adaptar Asteroides a la Xbox hubo que reescribir `Ship.cs` y modificar las escenas del juego.

**13.** ___ Como los cuatro paquetes `.msix` (Asteroides y Platformer, original y consola) se generaron sin errores, queda demostrado que los cuatro juegos corren en la Xbox.

**14.** ___ Si un test queda en rojo después de un cambio, el cambio que acabamos de hacer es siempre la causa.

**15.** ___ Sony y Nintendo publican sus requisitos de certificación completos, igual que Microsoft con los XR.

---

## Parte C — Respuesta corta

**16.** Explicá la diferencia entre **dispositivo**, **intención** y **lógica del juego**. Dá un ejemplo con Asteroides en PC (teclado), Android (táctil) y Xbox (mando).

**17.** Al poner Asteroides en orientación vertical, los asteroides nacen fuera de la pantalla. Explicá por qué, usando el ancho visible de la cámara y el rango donde aparecen los asteroides.

**18.** Nombrá **tres** cambios que la capa de consola agrega a Asteroides y al Platformer respecto de la versión original, y explicá por qué cada uno es necesario en una consola jugada desde el sillón.

**19.** La capa de consola pausa el juego por **tres motivos**. ¿Cuáles son? ¿Qué requisito o caso de prueba de Xbox se relaciona con uno de ellos?

**20.** Completá la tabla con el archivo instalable de cada plataforma y cómo se instala.

| Plataforma | Archivo que se genera | Cómo se instala o se ejecuta |
|---|---|---|
| PC (Windows) | | |
| Android | | |
| Xbox (Developer Mode) | | |
