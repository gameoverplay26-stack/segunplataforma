# clases-en-vivo

Repositorio de trabajo docente: material de la cátedra **Diseño según Plataformas de Juego** (FI – UNJu), proyectos Unity usados en clase, el proyecto académico SDD y la guía de transmisión de clases en vivo.

Motor de todos los proyectos: **Unity 6000.3.11f1**.

## Estructura

| Carpeta | Qué contiene |
|---|---|
| [`diseno-plataformas/`](diseno-plataformas/README.md) | **Materia.** Programa, unidades 1–7, clases fechadas, material transversal, herramientas y control de avance (`status-unidad.md`) |
| [`proyectos-unity/`](proyectos-unity/) | **Código.** Proyectos Unity de la cátedra: `Asteroides/` (juego base de las unidades de testing y de plataformas) y `Unidad03-TestingUnity/`. Los proyectos de terceros o pesados (`Match-3-Game/`, Boss Room, `_archivos/`) quedan locales e ignorados por git |
| [`docs/`](docs/) | **Proyecto académico SDD** (Discovery, Concept, GDD…). Lo gobierna `CLAUDE.md` §2–§10 |
| [`streaming/`](streaming/README.md) | Guía para transmitir clases en vivo (OBS, ZoomIt, checklist) |

## Notas

- Los proyectos Unity se abren desde `proyectos-unity/…`. Si Unity Hub los tenía registrados en la ruta anterior (raíz del repo), hay que quitarlos y volver a agregarlos.
- Las diapositivas de cada unidad o clase se generan con el script de su propia carpeta `scripts/`, que lee el `.md` de contenido (requiere `pip install python-pptx`).
