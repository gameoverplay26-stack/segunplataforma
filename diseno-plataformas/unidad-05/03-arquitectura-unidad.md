# Unidad 5: arquitectura de la unidad completa (propuesta)

- **Estado:** **APROBADA por el usuario el 2026-10-26** ("Aprobar y generar"). La Clase 1 todavía no se dio. El TP 4 va como PROPUESTO. Slides: `Unidad-5-2026-completa-v2.pptx` (74 slides), fuente `04-diapositivas.md`.
- **Pedido del usuario (2026-10-26):**
  - completar la Unidad 5 en **un solo archivo** de diapositivas;
  - **unos 150 minutos de exposición en total**, sin contar los prácticos ni los ejercicios intermedios;
  - avanzar según el tiempo disponible.
- **Insumos:** `00-investigacion-preliminar.md` (auditoría A1–A15, fichas B-1 a B-52), `01-desarrollo-tema-consolas.md`, slides de la Clase 1 (`04-diapositivas.md`, 1–20), demo en Xbox (`../laboratorio-adaptacion/PORTEO-XBOX.md`, `GUIA-XBOX-DOCENTE.md`) y guía de alumnos (`06-guia-alumnos-de-pc-a-xbox.md`).
- **Caso guía:** *Asteroides*, con el 2D Platformer como transferencia, igual que en la U4.
- **Narrativa:** "¿quién pone el límite?". En la U5, **el fabricante**.

## 1. Estructura del archivo único

Archivo: `Unidad-5-2026-completa-v2.pptx`. La versión actual no se pisa (regla 12). Numeración continua y pie con el bloque.

| Bloque | Título | Exposición (min) | Práctica (min, aparte) | Contenido | Auditoría |
|---|---|---|---|---|---|
| 1 | **La consola tiene dueño** | 36 | 54 (A5.1, A5.2) | Slides 1–20 actuales, **sin cambios** | A1, A2, A12 (datos) |
| 2 | **Las reglas del dueño: certificación** | 25 | 30 (A5.3) | Plataforma cerrada y acceso (ID@Xbox, PlayStation Partners, Nintendo); qué es **público** y qué está bajo **NDA**; XR obligatorios frente a XAG recomendados; XR-003, 112, 115, 130 y 022 (terminología); casos de prueba públicos 115-02 y 112-08; clasificación por edad (IARC, PEGI, ESRB); recorrido de publicación; los parches también se certifican | A6, A7, A8, A11 (parcial) |
| 3 | **Mando y TV a tres metros** | 25 | 30 (A5.4) | Acciones, esquemas de control y remapeo (Input System) como accesibilidad; glifos y terminología; funciones de mando propias (DualSense, HD Rumble 2) solo como **mejora opcional**; Adaptive Controller y Access Controller; XAG 101 (26 px) y 112 (todo navegable con mando); experiencia de 10 pies y zona segura | A3, A4, A5, A15 |
| 4 | **Asteroides llega a la Xbox** | 25 (incluye la **demo** de la docente) | 25 (A5.5) | Developer Mode frente a GDK; las dos versiones de cada juego; recorrido de instalación (diagrama); la capa de consola en código real (`ConsoleLayer`, `ConsoleRules`); defecto encontrado (gamepad virtual); qué no resuelve | A2, A5, A15 |
| 5 | **El modelo más débil manda: multijugador y rendimiento** | 30 | 30 (A5.6) | Multijugador local (pantalla compartida o dividida, costo de N cámaras, `PlayerInputManager`); caso **BG3 en Series S** + XR-130; en línea solo conceptos (autoridad, predicción, latencia según Claypool); ciclo **medir → aislar → aplicar → volver a medir**; orden de Unity 6 (GPU Resident Drawer, SRP Batcher; *dynamic batching* ya no se recomienda); memoria (mipmaps +33 %); resolución dinámica; dos presupuestos en Switch 2 | A9, A10, A12, A13, A14 |
| 6 | **Cierre de la unidad y TP 4** | 9 | — | Síntesis "el fabricante pone el límite"; consigna del TP 4 y rúbrica (PROPUESTAS) | — |
| Anexo A | Datos y fuentes | — | — | Slides 21–24 actuales, sin cambios | — |
| Anexo B | **Xbox en Developer Mode, paso a paso** | — | — | Procedimiento de `GUIA-XBOX-DOCENTE.md` en 8–9 slides de consulta: cuenta, Dev Mode, Dev Home, Device Portal, generar paquetes, instalar, protocolo, volver al modo normal, problemas frecuentes | — |
| **Total** | | **150** | **169** | | |

Sobre el reparto 40/60 (regla 5): con 150 minutos de exposición, el 60 % de práctica serían unos 225 minutos. La propuesta suma **169 minutos** de práctica, en bloques que se pueden **dar o pasar a tarea** según el tiempo disponible ("avanzar según el tiempo"). Cada slide de práctica indica su modalidad alternativa (en clase o como tarea).

## 2. Actividades

| ID | Bloque | Consigna (resumen) | Producto | Puente al TP 4 |
|---|---|---|---|---|
| A5.1 | 1 | Leer los gráficos (existe) | Respuestas con dato y fecha | Datos del capítulo |
| A5.2 | 1 | Matriz: Asteroides va a consola (existe) | Consola elegida + 3 cambios | Elección de consola |
| A5.3 | 2 | **Auditar Asteroides contra 6 XR públicos** (003, 112, 115, 130, 022, 074) y escribir 2 casos de prueba con el formato de 115-02 | Tabla XR: cumple, no cumple o N/A, con evidencia en el código | Checklist de requisitos |
| A5.4 | 3 | **Menú solo con mando y remapeo:** jugar `asteroide-final` sin mouse; diseñar el mapeo y la pantalla de remapeo; medir el texto contra 26 px | Mapa de controles + boceto de remapeo + medición | Adaptación de entrada y UI |
| A5.5 | 4 | **Predecir y comprobar** (guía de alumnos): tabla antes de la demo, resultado en la demo, lectura de la capa de consola | Tabla con aciertos y errores explicados | Evidencia de adaptación |
| A5.6 | 5 | **Medir antes de optimizar:** Profiler en Asteroides y en el Platformer; ¿CPU o GPU?; presupuesto de 16,6 ms; una técnica justificada | Captura del Profiler + presupuesto + técnica elegida con su motivo | Presupuesto de rendimiento |

## 3. TP 4 (PROPUESTO; peso y nota los define la titular)

**"Dossier de plataforma: consola"**, como capítulo del integrador.
- **Entregables:**
  1. elección de consola con datos y fecha (A5.2);
  2. checklist XR aplicado a Asteroides o al Platformer (A5.3);
  3. adaptación de mando y UI **implementada** en Unity: navegación sin mouse, pausa con Menu y al desconectarse el mando, texto de 26 px o más; puede partir de la capa de consola o escribirse desde cero;
  4. plan de pruebas con 4 casos al estilo de los XR, ejecutados en PC con mando o, si se puede, en la demo en Xbox;
  5. presupuesto de rendimiento medido (A5.6);
  6. "qué NO resolvimos".
- **Rúbrica (borrador):** cinco criterios con 4 niveles (datos y fuentes, requisitos, implementación con evidencia de tests, pruebas, rendimiento medido). La equivalencia con la nota la define la titular, como pasó con D4-05.

## 4. Lo que queda fuera (auditoría, sección G)

Netcode implementado, hardware en detalle, shaders, backend, SDKs de consola (NDA), contratos y anti-cheat. El multijugador en línea se da **solo a nivel conceptual**.

## 5. Reglas que se mantienen

- Viñetas breves, de 3 a 6 palabras y de 4 a 5 por slide; desarrollo completo en las notas, con glosario al inicio.
- No se nombran clases futuras: se dice "más adelante en la unidad".
- No hay recuadros de imagen vacíos.
- Toda URL se verifica. Lo no verificado de la sección H **no** se usa como dato. El caso BG3 se cita como lo cuenta la prensa (B-44), con aviso.
- Videos solo de consulta, sin minuto exacto (duraciones no verificadas).
