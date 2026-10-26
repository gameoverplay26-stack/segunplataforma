# Unidad 2 — Presentación (slide por slide)

36 diapositivas. Las marcadas **[EXT]** son el bloque de extensión no evaluable (ver [`06-anexo-scrum-agile.md`](./06-anexo-scrum-agile.md)).

Formato por slide: **Objetivo pedagógico** · **Contenido visible** · **Visual sugerido** · **Ejemplo del videojuego** · **Pregunta para los estudiantes** (los campos que no aplican se omiten).

---

**01 — Portada**
- Contenido: Unidad II — Gestión del testing · Diseño según Plataformas de Juego.
- Visual: un ticket de bug estilizado como si fuera el "título" de la clase.

**02 — Objetivos de la clase**
- Objetivo: que el estudiante sepa qué va a poder hacer al final.
- Contenido: los 5 objetivos específicos (Sección B).
- Pregunta: ¿alguna vez jugaron algo roto y no supieron cómo avisarlo bien?

**03 — El problema: 90 minutos, 12 bugs**
- Objetivo: instalar el problema real antes de cualquier definición.
- Contenido: el playtest de Cryptbound genera reportes desordenados por WhatsApp.
- Ejemplo: mostrar 3–4 quejas coloquiales reales (sin clasificar todavía).
- Pregunta: ¿qué se pierde si esto vive solo en un chat grupal?

**04 — Repaso: testing y QA (Unidad I)**
- Objetivo: anclar el vocabulario ya visto: error/defecto/fallo, técnicas.
- Contenido: línea de tiempo Unidad I → Unidad II → Unidad III.
- Evitar: repasar de cero como si nunca lo hubieran visto — es repaso, no reintroducción.

**05 — Equipo de Cryptbound**
- Objetivo: presentar el caso guía y el rol central de QA.
- Contenido: tabla de 7 roles (Sección F).
- Visual: avatares simples por rol, con Marisol (QA) destacada.

**06 — El proyecto: concepto, alcance, hitos**
- Objetivo: fijar el vertical slice y los 4 hitos de producción.
- Contenido: ficha de Cryptbound + flujo Prototipo→Funcional→Presentable→Final.

**07 — Agile: la idea mínima que necesitamos**
- Objetivo: dar el contexto justo del Manifiesto sin abrir Scrum todavía.
- Contenido: "software funcionando" y "responder al cambio" → testing continuo, no una fase final.
- Evitar: nombrar sprints, backlog o roles Scrum en esta diapositiva.

**08 — De la queja al ticket**
- Objetivo: mostrar qué transforma una queja en información accionable.
- Ejemplo: "se rompe cuando guardás" → CRYPT-107 con pasos, entorno, esperado/real.
- Pregunta: ¿qué le falta a la frase original para que alguien más pueda reproducirlo?

**09 — Clasificar: categoría**
- Contenido: Gameplay, UI, Audio, Save, Rendimiento, Contenido/Texto.
- Ejemplo: ubicar 3 tickets del backlog de Cryptbound por categoría.

**10 — Clasificar: severidad**
- Contenido: impacto técnico. Escala Bloqueante/Alta/Media/Baja/Trivial.
- Ejemplo: CRYPT-103 (crash) vs. CRYPT-110 (typo).

**11 — Clasificar: prioridad**
- Objetivo: instalar que severidad ≠ prioridad — el núcleo conceptual de la clase.
- Ejemplo: CRYPT-102 (baja severidad, prioridad media) y CRYPT-108 (severidad media, prioridad alta).
- Pregunta: ¿puede un bug "poco grave" ser urgente igual? ¿Por qué CRYPT-108 sí?

**12 — Clasificar: dificultad de resolución**
- Contenido: un tercer eje, independiente de los otros dos.
- Ejemplo: CRYPT-111: alta severidad + alta prioridad + alta dificultad = el trade-off real.

**13 — Ejercicio rápido en vivo**
- Objetivo: practicar antes de la actividad grupal completa.
- Contenido: clasificar entre todos 3 tickets nuevos del backlog (CRYPT-104, 106, 109).
- Tiempo: 5 minutos, votación a mano alzada por severidad/prioridad.

**14 — Panorama de herramientas**
- Contenido: Jira, TestRail, QAComplete, Confluence — qué resuelve cada una.
- Visual: tabla comparativa (Sección I).

**15 — Jira: anatomía de un issue**
- Contenido: campos: resumen, descripción, pasos, entorno, adjuntos, prioridad.
- Ejemplo: el ticket CRYPT-103 completo, como se vería en Jira.

**16 — Severidad en Jira: el campo que hay que agregar**
- Objetivo: dato técnico preciso — Jira no trae severidad nativa.
- Contenido: Prioridad = campo nativo (5 niveles). Severidad = campo personalizado.
- Evitar: dar a entender que "así viene de fábrica" sin aclarar la configuración.

**17 — Workflow: el camino de un bug**
- Contenido: Nuevo → En análisis → En progreso → Retest → Verificado → Cerrado (+Reabierto).
- Visual: diagrama de estados horizontal.

**18 — El board: ver el flujo, no solo la lista**
- Contenido: cada columna del board = un estado del workflow.
- Pregunta: si una columna se llena y no avanza, ¿qué está pasando en el equipo?

**19 — Dashboards y reportes de bugs**
- Contenido: bugs por severidad, por estado, tendencia abiertos vs. cerrados.
- Evitar: presentar esto como medición de productividad individual.

**20 — Retesting**
- Contenido: repetir solo los pasos que reproducían el bug ya corregido.
- Ejemplo: retest de CRYPT-103 tras el fix del crash de inventario.

**21 — Regression testing**
- Contenido: verificar que el fix no rompió algo relacionado.
- Ejemplo: regresión de guardado tras el fix de CRYPT-107: probar los 3 slots.

**22 — Smoke testing**
- Contenido: chequeo rápido antes de invertir horas de testing profundo.
- Ejemplo: el smoke test de 10 minutos de Cryptbound.

**23 — Riesgo en testing**
- Contenido: probabilidad × impacto, bajo tiempo limitado.
- Pregunta: con 2 días de regresión y 5 sistemas para revisar, ¿por dónde empiezan?

**24 — Plan de pruebas: para qué sirve**
- Contenido: evita improvisar qué se prueba y con qué criterio se da por terminado.

**25 — Plan de pruebas: estructura**
- Contenido: alcance, objetivos, criterios de aceptación, cronograma, responsables, riesgos, entornos.
- Ejemplo: plan de pruebas completo de Cryptbound v0.3.

**26 — Diseño de casos de prueba: campos**
- Contenido: ID, descripción, precondiciones, pasos, datos de entrada, esperado/real, estado, comentarios.

**27 — Caso de prueba — género Acción**
- Ejemplo: TC-A01, ataque cuerpo a cuerpo.

**28 — Caso de prueba — género RPG**
- Ejemplo: TC-R01, subida de nivel. Conexión con valores frontera (Unidad I).

**29 — Caso de prueba — género Estrategia**
- Ejemplo: TC-E01, rango de detección del arquero. Partición de equivalencia + valores frontera.

**30 — Ciclo de vida del videojuego y el testing**
- Contenido: hitos Prototipo/Funcional/Presentable/Final y qué se testea en cada uno.
- Ejemplo: el bug de FPS (CRYPT-111) es crítico recién en "Presentable", no antes.

**31 — [EXT] Jira también gestiona producción completa**
- Objetivo: ampliar el horizonte sin desarrollarlo a fondo aquí.
- Contenido: backlog de producto, Epics/Stories, Sprints — otro uso posible de la misma herramienta.
- Evitar: evaluar este contenido; es explícitamente no evaluable.

**32 — [EXT] Gestionar bugs ≠ gestionar producción**
- Contenido: mismo software, dos configuraciones y propósitos distintos.
- Referencia: ver [`06-anexo-scrum-agile.md`](./06-anexo-scrum-agile.md) para el desarrollo completo.

**33 — Recorrido integrador**
- Contenido: bug encontrado → ticket → triage → severidad/prioridad → fix → retest → regresión → cierre.
- Visual: el flujo completo, con CRYPT-103 como hilo conductor.

**34 — Errores conceptuales frecuentes**
- Contenido: tabla de la sección homónima — repasar 3 o 4, no las 9 de corrido.

**35 — Actividad práctica: instrucciones**
- Contenido: ver [`05-actividad-practica-y-evaluacion.md`](./05-actividad-practica-y-evaluacion.md).

**36 — Cierre y preguntas**
- Contenido: "Jira no reemplaza el criterio de QA: lo hace visible y trazable."
- Pregunta: ¿qué bug de un juego que jugaron reportarían distinto ahora?
