# Unidad 2 — Caso práctico: Cryptbound

Un único proyecto ficticio recorre toda la clase — no un banco, no un e-commerce: un videojuego real que un equipo estudiantil podría estar produciendo.

---

## Sección F — El proyecto

**Concepto:** Dungeon-crawler de acción en 2D con progresión ligera de RPG (nivel, inventario) y encuentros que premian leer el comportamiento del enemigo antes de atacar.

**Objetivo del proyecto:** producir un *vertical slice* jugable de 15–20 minutos: una mazmorra completa, un personaje jugable, tres tipos de enemigo y un jefe.

**Plataforma:** PC (Windows) para el vertical slice; puerto a Android planificado a futuro (conecta con la Unidad IV de esta misma materia).

**Género:** Acción-RPG con momentos de estrategia (sigilo/rango de detección).

**Alcance:** 1 mazmorra (3 salas + sala del jefe), 1 personaje jugable, 3 tipos de enemigo, inventario básico (arma + pociones), sistema de guardado en 3 slots.

**Duración estimada:** 8 semanas de producción part-time, organizadas en 4 hitos: **Prototipo → Funcional → Presentable → Final** (terminología de la industria de QA de videojuegos, no de Scrum).

**Restricciones:** equipo de 7 personas sin presupuesto para herramientas pagas (Jira en su plan gratuito); parque de testing limitado a 2 PC de gama media y 1 celular gama media para pruebas de portabilidad futura.

### Equipo (7 personas)

| Rol | Integrante | Responsabilidad frente al testing |
|---|---|---|
| Dirección de diseño | Valentina | Define si un reporte es "bug" o "así se diseñó"; decide balance. |
| Producción / liderazgo | Bruno | Prioriza qué se arregla primero según fecha de entrega y riesgo. |
| Programación de gameplay | Iñaki | Recibe tickets de gameplay/colisión/IA, propone fix, marca "listo para retest". |
| Programación técnica / herramientas | Coty | Atiende bugs de rendimiento, guardado y estabilidad. |
| Arte 2D | Renata | Atiende bugs visuales, UI y de animación. |
| Diseño de sonido | Facundo | Atiende bugs de audio. |
| QA Lead / Tester | Marisol | Ejecuta el plan de pruebas, redacta y clasifica tickets, coordina el triage. |

En un equipo de este tamaño los roles se combinan con frecuencia (Coty también ayuda a Iñaki con gameplay; Bruno también testea de forma exploratoria). Lo que no se combina es la disciplina: alguien tiene que ser quien decide, con criterio, qué severidad y prioridad lleva cada ticket.

---

## Sección G — Backlog de bugs (playtest del vertical slice, build 0.3)

Doce tickets reales que Marisol y el resto del equipo levantaron durante una sesión de playtest de 90 minutos. Es el material que los estudiantes clasificarán en la actividad práctica ([`05-actividad-practica-y-evaluacion.md`](./05-actividad-practica-y-evaluacion.md)).

| ID | Título | Categoría | Severidad | Prioridad | Dificultad | Estado |
|---|---|---|---|---|---|---|
| CRYPT-101 | El jugador atraviesa la pared al correr contra una esquina | Colisión | Alta | Alta | Media | Nuevo |
| CRYPT-102 | El contador de pociones no se actualiza visualmente al usar una | UI | Baja | Media | Baja | Nuevo |
| CRYPT-103 | El juego crashea al abrir el inventario con el arma cargada | Estabilidad | Bloqueante | Bloqueante | Alta | Nuevo |
| CRYPT-104 | El sonido de pasos sigue sonando con el personaje quieto | Audio | Baja | Baja | Baja | Nuevo |
| CRYPT-105 | El enemigo arquero dispara a través de paredes | Gameplay/IA | Alta | Alta | Media | Nuevo |
| CRYPT-106 | El texto del NPC se corta en resolución 4:3 | UI | Media | Baja | Media | Nuevo |
| CRYPT-107 | Guardar y cargar deja al jugador fuera del mapa | Save System | Bloqueante | Bloqueante | Alta | Nuevo |
| CRYPT-108 | El jefe final no reproduce su animación de derrota | Gameplay | Media | Alta | Baja | Nuevo |
| CRYPT-109 | Doble clic en "Atacar" a veces consume 2 pociones en vez de 1 | Gameplay | Media | Media | Media | Nuevo |
| CRYPT-110 | Typo en tutorial: dice "presiona E" y es "F" | Contenido/Texto | Trivial | Baja | Trivial | Nuevo |
| CRYPT-111 | Caída notable de FPS al entrar a la sala del jefe | Rendimiento | Alta | Alta | Alta | Nuevo |
| CRYPT-112 | Duplicado — otro tester reportó el mismo bug de esquina | Colisión | — | — | — | Duplicado de CRYPT-101 |

**Por qué este backlog es pedagógicamente rico:** CRYPT-102 (severidad baja, prioridad media) y CRYPT-108 (severidad media, prioridad alta) muestran que severidad y prioridad no van de la mano. CRYPT-111 obliga a discutir qué hacer cuando severidad, prioridad *y* dificultad son altas al mismo tiempo — el trade-off real de un equipo con tiempo limitado. CRYPT-112 introduce la gestión de duplicados. CRYPT-110 muestra que no todo lo reportado merece la misma urgencia.

### Ejemplo de ticket redactado (formato Jira)

> **CRYPT-103 · Bug · Severidad: Bloqueante**
> **Título:** El juego crashea al abrir el inventario con el arma cargada
> **Pasos:** 1) Equipar cualquier arma. 2) Mantener presionado el gatillo/click de carga. 3) Sin soltar, presionar "Abrir inventario" (tecla I).
> **Esperado:** El inventario se abre y la carga del arma se cancela de forma segura.
> **Real:** La aplicación deja de responder y cierra (crash) al abrirse el inventario.
> **Entorno:** Windows 11, build 0.3, PC de gama media (referencia interna).
> **Prioridad:** Bloqueante — se fija antes de cualquier otra tarea.

---

## Sección H — Ciclo de testing de ejemplo (hito "Presentable")

No es un Sprint de Scrum: es un ciclo de pruebas real dentro del cronograma de producción de Cryptbound, ubicado en el hito "Presentable" (dirección de arte cerrada, mecánicas integradas, listo para mostrarse a jugadores externos).

### Plan de pruebas — Vertical Slice Cryptbound v0.3

| Campo | Contenido |
|---|---|
| **Alcance** | Mazmorra completa (3 salas + jefe), combate, inventario, guardado, HUD. Fuera de alcance: crafteo (no implementado), build móvil. |
| **Objetivos** | Cero crashes bloqueantes; guardar/cargar sin pérdida de progreso; HUD consistente entre salas. |
| **Criterios de aceptación** | 0 bugs Bloqueantes/Críticos abiertos · ≤3 bugs Mayores abiertos · ≥90% de los casos de prueba diseñados, ejecutados. |
| **Cronograma** | 3 días de testing exploratorio + 2 días de regresión post-fix, dentro de la semana del hito Presentable. |
| **Responsables** | Marisol coordina el ciclo; cada bug se asigna según el componente afectado (ver tabla de equipo). |
| **Riesgos** | Tiempo insuficiente para regresión completa si el build estable llega tarde. |
| **Entornos** | PC gama media (mínimo soportado) · PC gama alta (referencia) · build opcional en Steam Deck. |

### Diseño de casos de prueba — un ejemplo por género (tal como pide el programa)

**TC-A01 · Acción — Ataque cuerpo a cuerpo conecta con el enemigo**
- Precondición: jugador con arma equipada; enemigo a 1 tile de distancia.
- Pasos: 1) Presionar el botón de ataque. 2) Observar animación e hitbox.
- Datos de entrada: un input de ataque simple.
- Esperado: el enemigo recibe daño y reproduce animación de impacto.
- Real: *(a completar durante la ejecución)*
- Comentarios: repetir con el enemigo a 1.5 tiles — caso límite de alcance del hitbox.

**TC-R01 · RPG — Subida de nivel al alcanzar el umbral de experiencia**
- Precondición: jugador en nivel 1, con 95/100 XP.
- Pasos: 1) Derrotar un enemigo que otorga 10 XP. 2) Observar el HUD.
- Esperado: el jugador sube a nivel 2; se actualiza la vida máxima; el HUD lo notifica.
- Comentarios: caso de valor frontera (100 XP exactos vs. 105 XP) — reutiliza la técnica de la Unidad I.

**TC-E01 · Estrategia — Rango de detección del enemigo arquero**
- Precondición: jugador fuera del rango de detección declarado (6 tiles).
- Pasos: 1) Acercarse tile por tile. 2) Registrar en qué tile el enemigo pasa a estado "alerta".
- Esperado: el enemigo se activa exactamente al entrar al tile 6, no antes ni después.
- Comentarios: combina partición de equivalencia (dentro/fuera de rango) y valores frontera (tile 5 vs. 6 vs. 7) — Unidad I aplicada a IA.

### Regression / retesting / smoke aplicados al ciclo

- **Retest de CRYPT-103:** tras el fix, Marisol repite *solo* los 3 pasos que originalmente crasheaban el juego.
- **Regression de CRYPT-107:** tras arreglar guardado/carga, se re-ejecutan los casos de prueba de los 3 slots de guardado y de los puntos de control — no solo el paso puntual que falló.
- **Smoke test diario:** antes de empezar el ciclo, 10 minutos: abrir el juego, nueva partida, caminar, atacar una vez, abrir menú, salir. Si esto falla, no se sigue testeando ese build.

---

## Sección I — Cómo Jira representa cada concepto (y cuándo conviene TestRail, QAComplete o Confluence)

La pregunta que ordena esta sección: **¿qué problema de gestión resuelve cada función?** Ninguna se enseña "porque existe".

| Concepto de gestión | Representación en Jira | Problema que resuelve |
|---|---|---|
| Proyecto | Un espacio "CRYPT" que agrupa todos los issues del vertical slice | Separar el ruido de otros proyectos. |
| Bug (tipo de issue) | Tipo de incidencia "Error" con campos de resumen, descripción, pasos, entorno, adjuntos | Estandarizar qué información mínima trae cada reporte. |
| Prioridad | Campo nativo de 5 niveles (Bloqueante/Alta/Media/Baja/Mínima) | Ordenar qué se ataca primero. |
| Severidad | **No es nativo**: se agrega como campo personalizado (o vía un add-on) | Separar impacto técnico de urgencia de negocio. |
| Workflow | Estados configurables: Nuevo → En análisis → En progreso → En revisión/Retest → Verificado → Cerrado (con transición a Reabierto) | Que nadie "pierda" un bug entre bandejas de mail o chats. |
| Board | Tablero visual que mapea cada columna a un estado del workflow | Ver de un vistazo dónde se atasca el flujo (cuellos de botella). |
| Filtros / Dashboards | Reportes de bugs por severidad, por estado, tendencia abiertos vs. cerrados | Responder "¿vamos bien para el hito Presentable?" sin abrir cada ticket. |

> **Dato técnico preciso (no simplificado):** el workflow de Bug por defecto de Jira es deliberadamente mínimo (algo como "Por hacer / En progreso / Hecho"). Un equipo que lo deja así termina con una columna "Hecho" que mezcla "arreglado" con "verificado" — dos cosas distintas. Por eso equipos serios agregan explícitamente los estados Retest y Verificado, y un campo de Severidad separado del de Prioridad.

### Comparación: Jira vs. TestRail vs. QAComplete vs. Confluence

| Herramienta | Foco principal | Cuándo conviene |
|---|---|---|
| **Jira** | Gestión general de incidencias/proyecto; el bug como issue trazable en un workflow. | Cuando el equipo ya vive en el ecosistema Atlassian y quiere bugs, tareas y documentación conectados. |
| **TestRail** | Gestión dedicada de *casos* de prueba: suites, ejecuciones, cobertura. | Cuando el volumen de casos de prueba es grande y necesitan organizarse en suites reutilizables por ciclo — Jira nativo no tiene "caso de prueba" como tipo (de ahí que existan add-ons como Xray o Zephyr). |
| **QAComplete** | Une requisitos, pruebas y defectos organizados en torno a historias de usuario. | Cuando se quiere trazabilidad estricta requisito → prueba → defecto en un único lugar. |
| **Confluence** | Documentación (planes de prueba, actas de triage, wiki del equipo). | Como compañero de Jira, no como reemplazo — Jira gestiona el ticket, Confluence documenta el porqué. |

---

## Errores conceptuales frecuentes

| Idea errónea | Corrección |
|---|---|
| "Severidad y prioridad son lo mismo" | Son independientes: una es técnica (impacto), la otra de negocio (urgencia). |
| "Jira es lo mismo que Scrum" | Jira es una herramienta configurable; Scrum es un marco de trabajo. Se puede usar Jira solo para bugs (como en esta clase) sin usar Scrum, y viceversa. |
| "Un bug sin pasos de reproducción sirve igual" | Sin pasos claros no es accionable: es ruido que alguien más tendrá que investigar de cero. |
| "Regression testing = repetir todo el juego" | Se dirige al área afectada por el cambio, no es una repetición ciega y total. |
| "Smoke testing = testing exhaustivo" | Es una verificación superficial y rápida, previa a invertir horas de testing profundo. |
| "Más tickets cerrados = mejor QA" | Cantidad no es calidad: cerrar sin verificar produce bugs reabiertos y desconfianza en el estado "Cerrado". |
| "El testing es responsabilidad exclusiva de QA" | La calidad es responsabilidad compartida del equipo completo (conexión directa con Unidad I). |
| "Todo bug debe arreglarse antes de lanzar" | Priorizar también significa decidir, con criterio, qué NO se arregla en este ciclo (riesgo aceptado). |
| "Usar Jira ya implica tener sprints y story points" | Depende de cómo se configure el proyecto. En Cryptbound, Jira se usa para bugs — no para gestionar producción completa (ver [`06-anexo-scrum-agile.md`](./06-anexo-scrum-agile.md)). |
