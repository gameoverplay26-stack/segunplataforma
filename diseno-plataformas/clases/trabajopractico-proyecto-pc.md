**Facultad de Ingeniería**

**Diseño según Plataforma**

# Trabajo Práctico N.º ___

## Selección del proyecto para PC y análisis de plataforma

| Campo | Completar |
|---|---|
| Nombre del grupo (o «individual») |  |
| Integrantes: nombre, apellido y legajo (máximo 5) |  |
| Título del juego |  |
| Enlace al repositorio de GitHub |  |
| Versión de Unity utilizada |  |
| Fecha de entrega |  |

**Modalidad:** individual o grupal (máximo 5 integrantes).
**Entrega:** martes 27/10, hasta las 22:00 h, en un repositorio de GitHub.
**Exposición:** actividad obligatoria, con nota para el promedio final.
**Motor:** Unity 6.3 (`6000.3.x`; la cátedra usa `6000.3.11f1`).

## 1. Objetivos

Al completar este trabajo práctico, cada estudiante o grupo debe demostrar que puede:

1. Presentar un videojuego propio para PC, **jugable de principio a fin**, con una descripción clara de su diseño.
2. Analizar cómo el **género** y la **plataforma** condicionan la orientación de la pantalla, el tipo de controles, el HUD y la duración de las sesiones.
3. Detectar en el código y en la configuración del proyecto los **supuestos de PC** (teclado, mouse, monitor horizontal, resolución fija).
4. Elegir una **plataforma destino** y justificar las decisiones de diseño para un porteo posterior.
5. Planificar el **contenido extra** (niveles o funcionalidades) que necesitará la versión porteada cuando el juego original sea corto.
6. Organizar el proyecto en un **repositorio de GitHub** que otra persona pueda clonar, abrir en Unity 6.3 y jugar.
7. Exponer el trabajo con el juego funcionando y con argumentos respaldados por evidencia.

## 2. Contexto

### 2.1 Para qué sirve este trabajo

En clase analizamos el porteo de dos juegos: **Asteroides**, un arcade 2D que se puede jugar en horizontal y en vertical, pero que en cada orientación muestra los sprites muy chicos o muy grandes; y el **2D Platformer**, un juego de progresión por niveles que exige pantalla horizontal para ver lo que viene. En este trabajo el juego es **de ustedes**: lo eligen, lo describen y analizan qué haría falta para llevarlo a otra plataforma. Ese mismo proyecto es la base del porteo que se realizará más adelante en la materia.

### 2.2 Qué juego pueden presentar

- Un juego diseñado para **PC (Windows)**, con teclado o mouse como entrada principal.
- Hecho en **Unity 6.3**, o migrado a Unity 6.3. Abrirlo en esa versión y comprobar que funciona es parte del trabajo.
- **Jugable de principio a fin:** inicio o menú, al menos un nivel o una partida completa, y una condición de victoria o de derrota.
- Puede ser un trabajo de otra materia o un proyecto personal. Si parte de un tutorial, una plantilla o un proyecto de terceros, hay que declararlo en el README con el enlace y la licencia.
- Todos los assets (arte, audio, fuentes) con **origen y licencia** identificados.

### 2.3 Juegos cortos

Se considera **juego corto** el que se completa en menos de 10 minutos o tiene un solo nivel. Si el suyo es corto, el análisis debe incluir un **plan de expansión** para la versión porteada: qué nivel o niveles extra, o qué funcionalidades nuevas, van a agregar, y por qué tienen sentido en la plataforma destino (Actividad 4). En este trabajo se planifica; la implementación es parte del porteo.

## 3. Uso de las etiquetas de estado en el informe

Cada afirmación del informe lleva una de estas etiquetas:

| Etiqueta | Cuándo usarla |
|---|---|
| **VERIFICADO** | Lo comprobaron jugando o ejecutando. Indiquen la evidencia (captura, video, medida). |
| **APLICADO** | Está en el proyecto, pero ninguna prueba demuestra su efecto. |
| **PROPUESTO** | Es una decisión o un cambio planificado para el porteo; todavía no está implementado. |
| **UNKNOWN** | No tienen evidencia suficiente para afirmarlo ni para descartarlo. |

Ejemplo: decir «en el teléfono, los botones taparían el borde inferior del nivel» sin haberlo probado es **PROPUESTO** o **UNKNOWN**, nunca **VERIFICADO**.

## 4. Consigna general

Seleccionen un videojuego propio para PC, súbanlo a un repositorio de GitHub y analicen, según su **género** y la **plataforma destino** que elijan, qué habría que cambiar para portearlo: orientación de la pantalla, tipo de controles, HUD, duración de las sesiones, rendimiento y contenido. Presenten el análisis en un informe y en una exposición oral, con el juego funcionando.

## 5. Actividades

### Actividad 1 · Ficha del juego

Completen esta ficha en el README del repositorio y en el informe:

| Campo | Qué debe contener |
|---|---|
| Título y género | Género principal y subgénero (por ejemplo: plataformas 2D de precisión, arcade de disparos, puzzle por turnos). |
| Descripción | De 3 a 5 oraciones: de qué trata, qué hace el jugador, cómo se gana y cómo se pierde. |
| Mecánica principal y ciclo de juego | La acción que más se repite y el ciclo completo (por ejemplo: explorar → saltar → juntar → llegar a la meta). |
| Contenido y duración | Cantidad de niveles o modos, y cuánto dura una partida completa (**medido**, no estimado). |
| Controles actuales | Cada acción con su tecla o botón del mouse. |
| Pantalla | Resolución y relación de aspecto con las que se diseñó; si funciona en ventana o en pantalla completa. |
| Assets y licencias | Origen y licencia del arte, el audio y las fuentes; qué es propio. |
| Estado | Qué funciona y qué no, con su etiqueta (sección 3). |

### Actividad 2 · Análisis según género y plataforma

Para cada aspecto, describan cómo está hoy en PC, qué exige el género y qué problema aparecería en la plataforma destino. Cada fila necesita al menos una evidencia (captura, medida o prueba) y su etiqueta de estado.

| Aspecto | Preguntas guía |
|---|---|
| Orientación de la pantalla | ¿Horizontal, vertical o ambas? ¿Qué necesita ver el jugador para decidir (lo que viene, lo que cae, el mapa)? ¿Qué se rompe al rotar? |
| Relación de aspecto y escala | ¿Qué pasa en 16:9, 19,5:9 y 4:3? ¿Los sprites y los textos se ven muy chicos o muy grandes? ¿Se corta parte del nivel? |
| Controles | ¿Cuántas acciones simultáneas exige? ¿Necesita precisión de tiempo o de puntería? ¿Cómo se traduciría a pantalla táctil, gamepad u otro dispositivo? |
| HUD e interfaz | ¿Qué información es imprescindible? ¿Dónde quedaría con el pulgar encima, con la muesca del teléfono o con el borde de un televisor (safe area)? |
| Sesión | ¿Cuánto dura una partida? ¿Se puede pausar o guardar? ¿Qué pasa si el juego se interrumpe? |
| Rendimiento | ¿A cuántos fps corre en PC (medido)? ¿Qué podría pesar en un dispositivo más limitado? |
| Accesibilidad | Tamaño del texto, contraste y alternativas para las acciones que exigen precisión o velocidad. |

### Actividad 3 · Supuestos de PC en el proyecto

Identifiquen **al menos 5** lugares del código o de la configuración que asumen una PC: lectura directa de teclas o del mouse, resolución fija, orientación implícita, interfaz pensada para el puntero, etc. Para cada uno indiquen:

- **Ubicación:** archivo y línea, o la pantalla de *Project Settings* donde está.
- **Qué asume:** por ejemplo, `Input.GetKey(KeyCode.Space)` asume que hay un teclado.
- **Qué pasaría en la plataforma destino:** por ejemplo, en un teléfono la acción nunca se ejecuta.

### Actividad 4 · Plataforma destino y decisiones de porteo

1. Elijan la **plataforma destino** (móvil Android, consola simulada con un gamepad en la PC, web u otra) y justifiquen la elección con el género y el público del juego.
2. Decidan y justifiquen la **orientación**, el **esquema de controles** y la **disposición del HUD**, con un boceto de la pantalla en la plataforma destino.
3. Si el juego es corto (2.3), presenten el **plan de expansión**: qué niveles o funcionalidades nuevas agregarían, cuánto suman a la duración y por qué encajan en la plataforma destino. Si no es corto, expliquen por qué no hace falta.
4. Registren **al menos 3 decisiones** con el formato: contexto · opciones · decisión · consecuencias.

Todo lo de esta actividad es **PROPUESTO**: en este trabajo no se implementa el porteo.

### Actividad 5 · Exposición

- Duración: hasta 10 minutos de exposición y 5 minutos de preguntas.
- Muestren el juego funcionando, en vivo o, si falla el equipo, en un video grabado de antemano.
- Recorran la ficha, el análisis, los supuestos de PC y las decisiones de porteo.
- Si el trabajo es grupal, participan todos los integrantes, y cualquiera puede responder preguntas sobre cualquier parte.
- La exposición es una **actividad obligatoria** y tiene **nota para el promedio final**.

## 6. Repositorio de GitHub

El repositorio es la entrega. Tiene que cumplir con lo siguiente:

- Proyecto de Unity 6.3 completo: `Assets/`, `Packages/` y `ProjectSettings/`.
- `.gitignore` de Unity: sin `Library/`, `Temp/`, `Logs/`, `UserSettings/` ni builds.
- Ningún archivo de más de 100 MB (es el límite de GitHub); para archivos grandes, usar Git LFS.
- `README.md` con: título, integrantes, ficha del juego (Actividad 1), controles, versión exacta de Unity, cómo abrir y jugar, y créditos y licencias de los assets.
- Carpeta `docs/` con el informe en PDF y la presentación.
- Repositorio público, o privado con acceso para la cuenta de GitHub que indique la cátedra.
- Si el trabajo es grupal: commits de todos los integrantes. El historial muestra la participación.
- Recomendado: una *release* con la build de Windows en un .zip, para probar el juego sin abrir Unity.

## 7. Entregables

| # | Entregable | Dónde |
|---|---|---|
| 1 | Repositorio de GitHub con el proyecto de Unity 6.3 | Enlace en la tarea del aula virtual |
| 2 | `README.md` con la ficha del juego | Raíz del repositorio |
| 3 | `Informe-<Grupo>.pdf`, con las actividades 1 a 4 y las preguntas finales; máximo 12 páginas sin contar capturas | `docs/` |
| 4 | Presentación de la exposición (PDF o PPTX) | `docs/` |
| 5 | Capturas y evidencias citadas en el informe | `docs/evidencias/` |

**Fecha de entrega:** martes 27/10, hasta las 22:00 h. El enlace se sube a la tarea del aula virtual antes del cierre, y se evalúa el estado de la rama `main` a esa hora.

## 8. Criterios de evaluación

Total: 100 puntos.

### A · Ficha y descripción del juego (15 puntos)

| Ítem | Puntos |
|---|---|
| A1. Ficha completa, con la duración medida | 6 |
| A2. Descripción clara: qué hace el jugador, cómo gana y cómo pierde | 4 |
| A3. Origen y licencia de todos los assets identificados | 5 |

### B · Análisis según género y plataforma (25 puntos)

| Ítem | Puntos |
|---|---|
| B1. Los 7 aspectos analizados, cada uno con evidencia | 14 |
| B2. Relación explícita entre el género y la orientación y los controles | 6 |
| B3. Etiquetas de estado bien usadas | 5 |

### C · Supuestos de PC (10 puntos)

| Ítem | Puntos |
|---|---|
| C1. Al menos 5 supuestos con su ubicación | 6 |
| C2. Consecuencia de cada uno en la plataforma destino | 4 |

### D · Plataforma destino y decisiones (20 puntos)

| Ítem | Puntos |
|---|---|
| D1. Plataforma destino elegida y justificada | 4 |
| D2. Orientación, controles y HUD justificados, con boceto | 8 |
| D3. Al menos 3 decisiones con el formato pedido | 4 |
| D4. Plan de expansión (o justificación de por qué no hace falta) | 4 |

### E · Repositorio (10 puntos)

| Ítem | Puntos |
|---|---|
| E1. El proyecto abre en Unity 6.3 y se juega sin errores | 5 |
| E2. README completo y estructura pedida | 3 |
| E3. Participación visible en el historial de commits (grupal) o historial ordenado (individual) | 2 |

### F · Exposición (20 puntos)

| Ítem | Puntos |
|---|---|
| F1. Juego funcionando durante la exposición | 5 |
| F2. Claridad y respeto del tiempo | 5 |
| F3. Respuestas a las preguntas | 5 |
| F4. Participación de todos los integrantes | 5 |

### Penalizaciones

- Si el proyecto no abre en Unity 6.3, se evalúa solo el informe y E1 vale 0.
- Si hay assets sin origen ni licencia, A3 vale 0.
- Las entregas fuera de término se rigen por el reglamento de la cátedra.

## 9. Restricciones

### No se puede

- Usar una versión de Unity que no sea la 6.3.
- Presentar como propio contenido de terceros sin declararlo.

### Qué se puede hacer

- Mejorar el juego para PC antes de la entrega (corregir errores, completar el menú), siempre que siga siendo el mismo juego.

### Fuera del alcance de este TP

- Implementar el porteo (controles táctiles, build para la plataforma destino): se hace más adelante en la materia.
- Publicar el juego en una tienda.

## 10. Preguntas finales

Respondan en el informe y llévenlas a la exposición:

1. ¿Qué parte de su juego depende más de la PC: el input, la pantalla o la duración de las sesiones? ¿Por qué?
2. Si tuvieran que cambiar la orientación, ¿qué se rompería primero?
3. ¿Qué acción del juego es la más difícil de llevar a la plataforma destino y qué alternativa proponen?
4. ¿Qué aprendieron del porteo de Asteroides o del 2D Platformer que se aplica a su juego?
5. ¿Qué no pudieron verificar y cómo lo verificarían?
