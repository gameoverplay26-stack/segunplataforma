# Assets de terceros — revisión de licencias (Asteroid Survival)

> **Fase SDD:** Technical Specification (fase 7). **Origen:** DEC-054 (pack gratuito de terceros con licencia revisada) y DEC-055 (sonido en el MVP).
> **Qué es:** la revisión de licencias y contenido de los packs candidatos, y la propuesta de qué archivo cubre cada necesidad del juego.
> **Qué no es:** la importación. Los archivos entran a `Arena-SDD/` recién en Implementation, porque el proyecto todavía no existe y la matriz de autorización no permite instalar contenido antes. El usuario ya autorizó esa importación (DEC-054).

## 1. Método

1. Se consultó cada página oficial en `kenney.nl/assets/…` (2026-10-25).
2. Se descargó cada ZIP a una carpeta aislada, fuera del repo, **solo para inspeccionarlo**: se leyó el `License.txt` incluido y se listó el contenido.
3. Se registró la suma SHA-256 de cada ZIP. En Implementation, el archivo que se importe tiene que coincidir con esa suma; si no coincide, se vuelve a revisar la licencia.

## 2. Packs revisados

Todos son de **Kenney (www.kenney.nl)** y su `License.txt` dice **Creative Commons Zero (CC0)**: uso libre en proyectos personales, educativos y comerciales; el crédito a Kenney es opcional.

| Pack | Página | Contenido verificado | SHA-256 del ZIP | ¿Se usa? |
|---|---|---|---|---|
| Space Shooter Extension | https://kenney.nl/assets/space-shooter-extension | 561 PNG: 9 naves (`Ships`), 4 meteoros (`Meteors`), 40 misiles (`Missiles`), 18 efectos (`Effects`), además de piezas, estaciones y astronautas; en tamaño normal y ×2 | `77efd54b343bbd123af8cc7f534446706731b9cf5a34f38d8fcc54e7245f9c91` | **Sí** (gráficos) |
| Sci-Fi Sounds | https://kenney.nl/assets/sci-fi-sounds | 73 OGG: láseres (`laserSmall`, `laserRetro`, `laserLarge`), explosiones (`explosionCrunch`, `lowFrequency_explosion`), impactos metálicos, motores | `119340f351a5098ad814f78719438c0da355a9ce8a4c8a3af6a8d48aa3d49e04` | **Sí** (sonidos de gameplay) |
| Interface Sounds | https://kenney.nl/assets/interface-sounds | 100 OGG: clicks, confirmaciones, errores, aperturas y cierres | `f2193d072726d6758a5f7871b2dcc54dcce0d5c35c6f0a62f92549b327c81232` | **Sí** (sonidos de pantallas y cuenta regresiva) |
| Digital Audio | https://kenney.nl/assets/digital-audio | 63 OGG: láseres, power-ups, tonos | `24e6ce28b76a6d8c89cff4d331e0965ff5c3de8a73c612028e9d363cc64e4f06` | No (alternativa de láser) |
| Impact Sounds | https://kenney.nl/assets/impact-sounds | 130 OGG: pasos e impactos de materiales | `029d734af1582474edf3a694d1b0cebc97c1c152f2f39fa34d4c2bafc5de77f8` | No (Sci-Fi Sounds ya cubre los impactos) |

**Space Shooter Redux**, el pack de naves más conocido de Kenney, ya **no tiene página en kenney.nl** (la URL devuelve 404 el 2026-10-25). Hay una copia en OpenGameArt con licencia CC0 (https://opengameart.org/content/space-shooter-redux), pero no se la toma como fuente porque no se pudo confirmar contra el sitio del autor.

## 3. Uso aprobado (sonidos: DEC-061; gráficos: aprobados con el cierre de la fase 7)

### Gráficos (Space Shooter Extension)

| Elemento del juego | Archivo propuesto | Nota |
|---|---|---|
| Nave | uno de `PNG/Sprites/Ships/spaceShips_001…009.png` | La elección es visual; se fija en Implementation |
| Asteroide | uno de `PNG/Sprites/Meteors/spaceMeteors_001…004.png` | **Un solo sprite**, para no sugerir varios tipos de asteroide (DEC-003) |
| Proyectil | uno de `PNG/Sprites/Missiles/spaceMissiles_*.png` | |
| Explosión del asteroide | uno de `PNG/Sprites/Effects/spaceEffects_*.png` | Solo visual; la parte visual de REQ-033 sigue sin especificar |

### Sonidos (DEC-055)

| Evento | Archivo propuesto | Pack |
|---|---|---|
| Disparo | `laserSmall_000.ogg` | Sci-Fi Sounds |
| Asteroide destruido | `explosionCrunch_000.ogg` | Sci-Fi Sounds |
| Nave dañada (contacto) | `impactMetal_000.ogg` | Sci-Fi Sounds |
| Game Over | `lowFrequency_explosion_000.ogg` | Sci-Fi Sounds |
| Partida completada | `confirmation_001.ogg` | Interface Sounds |
| Cada segundo de la cuenta regresiva | `click_001.ogg` | Interface Sounds |
| Iniciar / reiniciar | `open_001.ogg` | Interface Sounds |

## 4. Obligaciones

- CC0 no exige atribución. Se propone igual un crédito en el README de `Arena-SDD/`: "Gráficos y sonidos: Kenney (www.kenney.nl), CC0".
- Se importan **solo** los archivos elegidos, no el pack completo, junto con el `License.txt` de cada pack.
- Esto no contradice DEC-013: esa decisión prohíbe reutilizar el material del Asteroides de clase, no usar packs de terceros.
