# Unidad 2 — Investigación de recursos

Investigación realizada con búsqueda web y verificación directa de URLs (fetch) en septiembre de 2026. Se priorizó documentación oficial de Atlassian, luego material académico gratuito, luego video en español, y por último referencias en inglés claramente marcadas como tales. El curso pago de GameDevStation se analizó solo por su página pública, sin acceder a contenido protegido.

---

## Recursos oficiales de Atlassian

**Plantilla de informe de errores de Jira (ES)** — ★★★★★
Atlassian · Documentación oficial · Español
`https://www.atlassian.com/es/software/jira/templates/bug-report`
Verificado por fetch directo. Define textualmente los campos mínimos de un reporte (gravedad, entorno, pasos, resultado esperado vs. real) — base directa del backlog de bugs de Cryptbound.

**Manifiesto ágil para el desarrollo de software (ES)** — ★★★★★
Atlassian · Documentación oficial · Español
`https://www.atlassian.com/es/agile/manifesto`
Fuente para la mención breve exigida por el programa. No usar como base para desarrollar Scrum completo en la unidad principal.

**Manifiesto por el Desarrollo Ágil de Software (texto canónico)** — ★★★★★
agilemanifesto.org · Fuente primaria, no Atlassian · Español
`https://agilemanifesto.org/iso/es/manifesto.html` · principios: `https://agilemanifesto.org/iso/es/principles.html`
El texto original de los 17 firmantes (2001). Preferible citarlo a él antes que a una paráfrasis de blog.

**Prácticas recomendadas para las pruebas ágiles (ES)** — ★★★★
Atlassian · Documentación oficial · Español
`https://www.atlassian.com/es/agile/software-development/testing`
Refuerza la idea de testing continuo sin necesidad de exponer Scrum completo.

**What Are Jira Workflows? / What is a Jira Board?** — ★★★★
Atlassian · Documentación oficial · **Inglés** (sin versión ES verificada)
`https://www.atlassian.com/software/jira/guides/workflows/overview` · `https://www.atlassian.com/software/jira/guides/boards/overview`
Base técnica de la sección de mapeo a Jira. Material de referencia para el docente, no para proyectar en inglés sin traducir los conceptos clave en clase.

**Get Started with Jira (guía completa para principiantes)** — ★★★
Atlassian · Documentación oficial · **Inglés**
`https://www.atlassian.com/software/jira/guides/getting-started/introduction`
Útil como referencia de fondo del docente; evitar proyectar capturas de UI que quedarán obsoletas.

---

## Videos recomendados

### En español

**🐞 Aprende cómo crear un reporte de bug o defecto en Jira (5 min)** — ★★★★
YouTube · Español · ~5 min
`https://www.youtube.com/watch?v=CWX0RakpZRw`
Corto y directo al grano: cómo se ve un ticket bien formado. Mostrar completo (dura solo 5 minutos) justo antes de la actividad práctica.

**Curso de Jira para Testers (playlist gratuita) — ep. 1 "Cómo usar Jira gratis"** — ★★★★
YouTube · Español · Playlist de varios episodios cortos
Playlist: `https://www.youtube.com/playlist?list=PLqjBJxfhRo93j22-HMybkUriF86hPhyQp` · ep. 1: `https://www.youtube.com/watch?v=LeRxpTy-eNU`
Enfocado explícitamente en el perfil de tester/QA, no en producción. El episodio 4 cubre Confluence como complemento. **No se pudo verificar el nombre exacto del canal** desde la búsqueda automatizada — el docente debería confirmarlo antes de proyectarlo en clase.

### Sobre videojuegos específicamente (referencia paga, no gratuita)

**Testing de Videojuegos: La Guía Definitiva — lección "Prioridades de los bugs y prioridad según su ruta"** — ★★★
Platzi · Español · Plataforma **de suscripción paga** · Docente: Jon Aguinaga (tester profesional, +4 años en estudios multinacionales, profesor de game testing en Tecnocampus)
No apto para asignar como lectura obligatoria gratuita. Útil solo como referencia del docente para contrastar enfoque profesional de priorización de bugs en videojuegos.

### En inglés (material de referencia para el docente)

**Artículos sobre defect/bug life cycle en Jira** — ★★★
Varios blogs especializados (StarAgile, GeeksforGeeks, The Knowledge Academy) · **Inglés** · No son documentación oficial de Atlassian.
Coinciden en un ciclo de 5–6 estados (Nuevo → Asignado → Corregido → Retest → Verificado → Cerrado) consistente con lo enseñado en la unidad. Usar como respaldo conceptual, citando que son fuentes secundarias, no oficiales.

---

## Material específicamente relacionado con videojuegos

**Guía de Game QA: Estrategias de Calidad y Testing en el Desarrollo de Videojuegos** — ★★★★★
Image Campus (institución educativa, Buenos Aires, Argentina) · Artículo gratuito · Español
`https://www.imagecampus.edu.ar/desarrollo-de-videojuegos/guia-de-game-qa-estrategias-testing-desarrollo-videojuegos`
Verificado por fetch directo. Es el recurso más alineado de toda la investigación: describe el ciclo de vida del bug en 5 etapas (identificar, amplificar, notificar, testificar, verificar), los hitos Prototype/Functional/Presentable/Final que esta unidad adoptó para Cryptbound, y nombra explícitamente Jira y TestRail como "bases de datos profesionales de la industria". Contexto latinoamericano, coherente con el público de la cátedra.

**Severidad y prioridad de un defecto** — ★★★★
Nadia Cavalleri (instructora especializada en testing/QA) · Artículo gratuito · Español (Argentina)
`https://nadiacavalleri.com.ar/en/severidad-y-prioridad-de-un-defecto/`
Explica las 4 combinaciones severidad×prioridad con el mismo enfoque usado en esta unidad. Buena lectura complementaria para estudiantes.

**Plan de Aseguramiento de la Calidad de Software — sección Pruebas** — ★★★
Universidad Nacional de la Patagonia San Juan Bosco (Argentina) · Material académico gratuito · Español
`https://unpsjb.github.io/ids3t/pruebas.html`
Verificado por fetch directo. Estructura de plan de pruebas (tipos, roles, fases, entornos, entregables) consistente con la sección de plan de pruebas de esta unidad, aunque no menciona Jira — usar solo para reforzar la estructura genérica del plan de pruebas.

---

## Comparación de recursos

| Recurso | Idioma | Gratuito | Autoridad | Valoración |
|---|---|---|---|---|
| Plantilla informe de errores (Atlassian) | ES | Sí | Oficial | ★★★★★ |
| Manifiesto Ágil (agilemanifesto.org) | ES | Sí | Fuente primaria | ★★★★★ |
| Guía de Game QA (Image Campus) | ES | Sí | Institución educativa | ★★★★★ |
| Manifiesto Ágil (Atlassian ES) | ES | Sí | Oficial | ★★★★★ |
| Severidad y prioridad (N. Cavalleri) | ES | Sí | Instructora especializada | ★★★★ |
| Jira Workflows / Boards (Atlassian) | EN | Sí | Oficial | ★★★★ |
| Curso Jira para Testers (YouTube) | ES | Sí | Canal independiente (sin verificar) | ★★★★ |
| Video "reporte de bug en 5 min" | ES | Sí | Canal independiente | ★★★★ |
| Plan de pruebas (UNPSJB) | ES | Sí | Universidad pública | ★★★ |
| Get Started with Jira (Atlassian) | EN | Sí | Oficial | ★★★ |
| Blogs sobre defect life cycle | EN | Sí | Secundaria, no oficial | ★★★ |
| Testing de Videojuegos (Platzi) | ES | **No** (pago) | Profesional de la industria | ★★★ |
| Mastering Jira for Game Producers (GameDevStation) | EN | **No** (pago) | Curso especializado | ★★ (solo referencia estructural, ver Anexo) |

---

## Bibliografía / Webgrafía

- Atlassian. *Plantilla de informe de errores*. `https://www.atlassian.com/es/software/jira/templates/bug-report`
- Atlassian. *Manifiesto ágil para el desarrollo de software*. `https://www.atlassian.com/es/agile/manifesto`
- Beck, K. et al. (2001). *Manifiesto por el Desarrollo Ágil de Software*. `https://agilemanifesto.org/iso/es/manifesto.html`
- Atlassian. *Prácticas recomendadas para las pruebas ágiles*. `https://www.atlassian.com/es/agile/software-development/testing`
- Atlassian. *What Are Jira Workflows?* / *What is a Jira Board?* `https://www.atlassian.com/software/jira/guides/workflows/overview`
- Image Campus. *Guía de Game QA: Estrategias de Calidad y Testing en el Desarrollo de Videojuegos*. `https://www.imagecampus.edu.ar/desarrollo-de-videojuegos/guia-de-game-qa-estrategias-testing-desarrollo-videojuegos`
- Cavalleri, N. *Severidad y prioridad de un defecto*. `https://nadiacavalleri.com.ar/en/severidad-y-prioridad-de-un-defecto/`
- Universidad Nacional de la Patagonia San Juan Bosco. *Plan de Aseguramiento de la Calidad de Software — Pruebas*. `https://unpsjb.github.io/ids3t/pruebas.html`
- Ramirez, E. D. (2024). *Planificación de cátedra: Diseño según Plataformas de Juego*. Facultad de Ingeniería, Universidad Nacional de Jujuy. (Documento fuente del programa analizado en `01-analisis-programa-y-objetivos.md`.)
- Referencias en inglés y de acceso pago señaladas explícitamente arriba.
