# Unidad 3 — Investigación de recursos

Investigación realizada con búsqueda web y verificación directa de URLs (fetch, y para YouTube también oEmbed/noembed.com) en septiembre de 2026. Se priorizó documentación oficial de Unity, luego documentación oficial de Microsoft (como referencia conceptual de C#/.NET), luego material académico gratuito, luego industria AAA vía GDC, luego video en español, y por último referencias en inglés claramente marcadas como tales. Se declaran explícitamente los casos en que una URL no pudo verificarse o resultó inexistente — no se inventó ningún recurso.

---

## Documentación oficial de Unity

**Test Framework — Manual de Unity 6** — ★★★★★
Unity Technologies · Documentación oficial · Inglés
`https://docs.unity3d.com/Manual/com.unity.test-framework.html`
Verificado por fetch directo. Página canónica embebida en el Manual de Unity 6.6. Confirma que en Unity 6 el Test Framework es un **paquete "core" fijo a la versión del Editor** — ya no se administra por separado en el Package Manager como en las LTS 2021/2022. Ver "Diferencias entre versiones" más abajo.

**Get started with Unity Test Framework** — ★★★★★
Unity Technologies · Documentación oficial · Inglés
`https://docs.unity3d.com/6000.2/Documentation/Manual/test-framework/getting-started.html`
Landing page que enlaza al flujo completo: crear ensamblado de tests → crear script de test → usar Test Runner.

**Create a test assembly** — ★★★★★
Unity Technologies · Documentación oficial · Inglés
`https://docs.unity3d.com/6000.2/Documentation/Manual/test-framework/workflow-create-test-assembly.html`
Verificado por fetch directo. Confirma textualmente el flujo usado en el Bloque 5 del guion docente: `Window ▸ General ▸ Test Runner` → *Create a new Test Assembly Folder*, o `Assets ▸ Create ▸ Testing ▸ Test Assembly Folder`. El `.asmdef` generado incluye referencias a `nunit.framework.dll`, `UnityEngine.TestRunner` y `UnityEditor.TestRunner`.

**Create a test** — ★★★★★
Unity Technologies · Documentación oficial · Inglés
`https://docs.unity3d.com/6000.2/Documentation/Manual/test-framework/workflow-create-test.html`
Verificado por fetch directo. Botón *Create a new Test Script* en la ventana Test Runner, o `Assets ▸ Create ▸ Testing ▸ C# Test Script`.

**Edit mode and Play mode tests** — ★★★★★ (fuente más importante de la unidad)
Unity Technologies · Documentación oficial · Inglés
`https://docs.unity3d.com/6000.4/Documentation/Manual/test-framework/edit-mode-vs-play-mode-tests.html`
Verificado por fetch directo. Cita textual clave: *"You can't run coroutines in Edit mode tests"*; en Play Mode, los tests `[UnityTest]` *"run as coroutines"*. Confirma la recomendación oficial: usar `[Test]` de NUnit salvo que se necesite `yield` (avanzar frames/tiempo), caso en el que corresponde `[UnityTest]`. Base directa de la tabla comparativa Edit Mode / Play Mode de esta unidad.

**Asserting and comparing** — ★★★★★
Unity Technologies · Documentación oficial · Inglés
`https://docs.unity3d.com/6000.3/Documentation/Manual/test-framework/asserting-and-comparing.html`
Verificado por fetch directo. Confirma que Unity Test Framework extiende (no reemplaza) las aserciones de NUnit, con comparadores propios para `Vector`/`Quaternion`/`Color` con tolerancia, y `LogAssert.Expect(...)` para testear mensajes de consola esperados.

**Game Development Testing and QA Best Practices** — ★★★★★
Unity Technologies · unity.com/how-to · Inglés
`https://unity.com/how-to/testing-and-quality-assurance-tips-unity-projects`
Verificado por fetch directo. Fuente oficial que respalda directamente los límites del unit testing enseñados en esta unidad. Cita textual: *"TDD is quite rare in game development [...] probably due to it being a counterintuitive process for prototyping and crafting fun and compelling gameplay"*, y: *"It's not able to test if the game does what it's designed to do"* sobre las limitaciones del unit testing frente a bugs de UI, balance o gameplay poco pulido.

**How to run automated tests for your games with the Unity Test Framework** — ★★★★☆
Unity Technologies · unity.com/how-to · Inglés
`https://unity.com/how-to/automated-tests-unity-test-framework`
Guía oficial con ejemplo de patrón AAA aplicado y exportación de resultados a CI. Escrita sobre una versión de paquete más antigua (1.3.3) — usar para conceptos, no para pasos exactos de interfaz.

**NUnit — Assert.AreEqual** — ★★★★☆
NUnit.org · Documentación oficial de NUnit (no de Unity) · Inglés
`https://docs.nunit.org/articles/nunit/writing-tests/assertions/classic-assertions/Assert.AreEqual.html`
Fuente primaria de las aserciones que Unity Test Framework reexpone vía `using NUnit.Framework;`.

---

## Documentación oficial de Microsoft (referencia conceptual, adaptar a Unity)

**Best practices for writing unit tests - .NET** — ★★★★★
Microsoft Learn · Documentación oficial · Inglés
`https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices`
Verificado por fetch directo (actualizada 2026-04-09). La mejor fuente conceptual encontrada para "qué hace bueno o malo un test": propiedades **Fast, Isolated, Repeatable, Self-Checking, Timely**, patrón Arrange-Act-Assert, convención de nombres `Método_Escenario_ResultadoEsperado`, evitar lógica condicional dentro de un test, un solo `Act` por test — todo directamente aplicable a los ejemplos de Cryptbound de esta unidad, aunque el documento use xUnit en vez de NUnit.

**Test-driven development - Visual Studio** — ★★★★★
Microsoft Learn · Documentación oficial · Inglés
`https://learn.microsoft.com/en-us/visualstudio/test/quick-start-test-driven-development-with-test-explorer?view=visualstudio`
Verificado por fetch directo (actualizada 2026-04-22). Tutorial oficial que recorre el ciclo Red-Green-Refactor completo con código real, aclarando explícitamente que un refactor "no está pensado para alterar el comportamiento del código, y por eso los tests no cambian". El propio documento indica que el enfoque "se adapta fácilmente a NUnit" — el mismo framework detrás de Unity Test Framework.

---

## TDD — fuente primaria y de referencia

**Test-Driven Development (bliki)** — ★★★★★
Martin Fowler · martinfowler.com · Inglés
`https://martinfowler.com/bliki/TestDrivenDevelopment.html`
Verificado por fetch directo (publicado 2005, actualizado 2023-12-11). Define el ciclo Red-Green-Refactor y atribuye su desarrollo a Kent Beck. Cita textual de advertencia útil para la clase: *"the most common way that I hear to screw up TDD is neglecting the third step"* (el refactor).

**Test-Driven Development: By Example** (libro) — referencia bibliográfica, no verificable online
Kent Beck · Addison-Wesley, 2002 (ISBN 978-0321146533)
Fuente primaria de TDD. **No se encontró una copia oficial y gratuita verificable en la web** — un PDF hallado en un servidor académico de tercero no pudo confirmarse como fiel al original, por lo que no se cita como enlace. Citar el libro impreso/ISBN, respaldado por el resumen verificado de Martin Fowler arriba.

---

## Videos en español

**"Testing automatizado de juegos"** — ★★★★☆ (el mejor recurso en video en español de esta investigación)
Gustavo Moreira · Nerdearla (conferencia tecnológica latinoamericana, Buenos Aires) · Español · Gratuito
`https://www.youtube.com/watch?v=0NNUkmd08Rg`
Verificado vía noembed.com. Edición Nerdearla 2021. Testing/QA automatizado aplicado a videojuegos con mención directa a Unity y a evitar depender de soluciones comerciales costosas.

**"Qué es el UNIT TEST en Unity y cómo usarlo paso a paso"** — ★★★☆☆
Codearte (canal independiente, empresa argentina de educación en gamedev) · Español · Gratuito
`https://www.youtube.com/watch?v=YxPDIgLPOSA`
Verificado vía noembed.com. Único video gratuito en español encontrado específico de Unity Test Framework. Funciona como puerta de entrada a un curso pago del mismo canal (ver abajo) — el docente debería revisarlo antes de proyectarlo, ya que no pudo transcribirse en detalle.

**"Unit Testing en C#"** (curso gratuito, no específico de Unity) — ★★★☆☆
NicoPaez · Udemy (curso gratuito) · Español
`https://www.udemy.com/course/unit-testing-nicopaez/`
2 horas en bloques cortos, usa NUnit — el mismo framework que Unity Test Framework. Buen cimiento previo, requiere que el docente haga el puente explícito hacia Unity.

**⚠️ Recurso descartado — verificado como inexistente:** un video titulado *"Tutorial de Pruebas Unitarias Automatizadas en Unity"* (ID `YsNVOvGMkS0`) aparece repetidamente en buscadores, con atribución no confirmable a un supuesto "Iván Herrera". La verificación vía oEmbed/noembed devolvió **error 404 en ambos casos**. **No usar ni enlazar este recurso.**

**Curso pago — "Unity Unit Testing Master"** (referencia, no gratuita)
Codearte · Udemy / codearte.com.ar · Español · **De pago**
`https://www.udemy.com/course/unity-unit-testing-master-crea-juegos-sin-bugs-con-pruebas/`
Contenido reportado (no verificado en profundidad, fetch bloqueado por protección anti-bot): unit testing, UI testing, CI/CD, TDD, mocks con NSubstitute. Es el contenido en español más completo y específico encontrado sobre Unity — pero de pago; no asignar como lectura obligatoria gratuita, igual que se hizo con Platzi en Unidad 2.

---

## Videos en inglés (referencia para el docente / proyección opcional subtitulada)

**"QA your code: The new Unity Test Framework"** (Unite Copenhagen 2019) — ★★★★★
Unity (canal oficial) · Inglés · Gratuito
`https://www.youtube.com/watch?v=wTiF2D0_vKA`
Verificado vía noembed.com (`author_name: "Unity"`). Única fuente oficial en video sobre el framework específico de esta unidad — migración a paquete, API del Test Runner, builds de test players.

**"Practical Unit Tests"** (GDC 2014, solo diapositivas gratis) — ★★★★★
Andrew Fray (Spry Fox) · GDC · Inglés · Gratuito (slides) / de pago (video en GDC Vault)
`https://www.slideshare.net/slideshow/practical-unit-testing-gdc-2014/32594081`
Verificado por fetch directo — 107 láminas. Anti-patrones de tests (Opaque, Wet, Deep, Wide), AAA, caso real de un juego de F1 2011 con 502 tests. Excepcionalmente concreto; requiere que el docente narre el contexto al ser solo diapositivas.

**"Unit Testing / TDD in Unity3D"** — ★★★★☆
Charles Amat (Infallible Code) en el canal Unity3D College (Jason Weimann) · Inglés · Gratuito
`https://www.youtube.com/watch?v=Q8Cw8UvgRYc`
Verificado vía noembed.com. Ambos son educadores independientes ampliamente reconocidos en la comunidad Unity.

**Serie "TDD in Unity"** (Infallible Code) — ★★★★☆
Infallible Code · Inglés · Gratuito
`https://www.youtube.com/watch?v=27h3l32S3s8` (intro) · `https://www.youtube.com/watch?v=_vd2JyX6C1Y` ("Basic Player Health (with Unit Tests) [7]")
Verificados vía noembed.com. Serie de varios episodios aplicando TDD a un sistema de salud del jugador — muy cercano al ejemplo `PlayerHealth` de esta unidad. Recomendable si la cátedra dispone de más de una clase.

**"Introduction To Unity Unit Testing"** (artículo, no video) — ★★★★☆
Anthony Uccello / Ben MacKinnon · Kodeco (ex-raywenderlich.com) · Inglés · Gratuito con registro
`https://www.kodeco.com/38240193-introduction-to-unity-unit-testing`
Actualizado 2023-03-20 para Unity 2021 LTS. Tutorial escrito más completo en inglés: EditMode/PlayMode, assemblies, convenciones de nombres, cobertura de código. Usa el mismo proyecto de ejemplo Crashteroids que `docs/Unidad 3 -2024.pptx`.

**⚠️ Canal sin verificar** — mencionado solo a título informativo, revisar antes de usar
"Test-Driven Development (TDD) by Example | Unity and C#" · canal "25games" · `https://www.youtube.com/watch?v=arzREy5zLVU`
El video existe, pero no se pudo verificar la reputación ni trayectoria del canal en ninguna fuente secundaria.

---

## Material universitario / académico

**"GamwUS: Desarrollo Dirigido por Pruebas y Videojuegos"** — ★★★★★ (el ancla académica en español de la unidad)
Javier Gutiérrez, grupo de investigación IWT2 · Universidad de Sevilla · Español · Gratuito
`https://es.slideshare.net/slideshow/gamwus-desarrollo-diriguido-por-pruebas-y-videojuegos/27015200`
Verificado por fetch directo (2013, 43 láminas). Experiencia personal con TDD en videojuegos, las 3 reglas de TDD, por qué la industria lo evita ("umbral de entrada alto"), qué partes de un juego se benefician (lógica, IA) vs. cuáles no (gráficos, colisiones, multihilo) — coincide punto por punto con la distinción de "buenos candidatos vs. casos complejos" de esta unidad.

**Curso abierto de TDD** — ★★★★☆
Juan Julián Merelo Guervós, profesor de la Universidad de Granada · Español · Gratuito (GitHub Pages)
`https://jj.github.io/curso-tdd/`
Verificado por fetch directo. Tests unitarios, AAA, principios FIRST, TDD con ejemplos multi-lenguaje (no específico de Unity/C#) — el material académico más riguroso sobre TDD general encontrado en español; requiere trasladar ejemplos a C#.

**"Pruebas" — Plan de Aseguramiento de la Calidad de Software** — ★★★☆☆
Universidad Nacional de la Patagonia San Juan Bosco (misma institución citada en Unidad 2) · Español · Gratuito
`https://unpsjb.github.io/ids3t/pruebas.html`
Verificado por fetch directo. General de ingeniería de software (pruebas unitarias, integración, regresión), no específico de videojuegos — complementa el marco conceptual.

**TFG — "Ejecución y adaptación de trazas de juegos para la automatización de pruebas"** — ★★★★☆
Luis María Costero Valero · Universidad Complutense de Madrid (repositorio institucional) · Español · Gratuito
`https://docta.ucm.es/entities/publication/1e120310-f59c-4793-bb91-81c6acb45906`
Verificado por fetch directo (2015). Propone automatizar pruebas capturando "trazas" de un jugador experto, en vez de unit testing tradicional — buen contraste académico para discutir los límites del unit testing puro en videojuegos.

**Lista de materiales sobre TDD y pruebas** — ★★★☆☆
Javier Gutiérrez (mismo autor de GamwUS) · Español · Gratuito
`https://iwt2-javierj.tumblr.com/post/78009590256/lista-actualizada-de-materiales-sobre-tdd-y-prueba`
Verificado por fetch directo (2014). Webgrafía complementaria para que los estudiantes profundicen por su cuenta; algunos enlaces internos podrían estar desactualizados por la antigüedad de la publicación.

---

## Industria de videojuegos (testing automatizado en producción real)

**"Automated Testing of Gameplay Features in 'Sea of Thieves'"** — ★★★★★
Robert Masella (Rare) · GDC · Inglés · Gratuito
`https://www.youtube.com/watch?v=X673tOi8pU8`
Verificado vía noembed.com. GDC 2019. Ejemplo de producción AAA real: unit tests de gameplay/IA en C++, tests de integración con blueprints, tests nocturnos de rendimiento/multijugador.

**"Automated Testing and Profiling for 'Call of Duty'"** — ★★★★★
Jan van Valburg (Activision) · GDC · Inglés · Gratuito
`https://www.youtube.com/watch?v=8d0wzyiikXM` · paper oficial: `https://research.activision.com/publications/archives/automated-testing-in-call-of-duty`
Ambos verificados (video vía noembed, paper vía fetch directo). Caso infrecuente: charla en video **y** publicación técnica primaria de la propia empresa, ambas gratuitas. Cubre CI, seguimiento de rendimiento/memoria y mitigación de tests intermitentes ("flaky tests") a la escala de un estudio AAA.

**"TestMonkey: Automated Testing at Santa Monica Studio"** (GDC 2023, solo diapositivas gratis) — ★★★★☆
Ben Hines · Sony Santa Monica Studio · Inglés · Gratuito (slides) / de pago (video)
`https://media.gdcvault.com/gdc2023/Slides/Testmonkey+Automated+Testing_Hines_Ben.pdf`
Framework interno de testing (visual, smoke, determinismo, gameplay) del estudio creador de *God of War*.

**"Testing manual vs. testing automatizado: ¿cuál elegir para tu proyecto?"** — ★★★★☆
Abstracta (empresa uruguaya de testing de software) · Español · Gratuito
`https://abstracta.us/es/blog/testing-manual-vs-testing-automatizado/`
Verificado por fetch directo (2021-10-06). No específico de videojuegos, pero es el recurso en español más directamente alineado con el contraste "manual vs. automatizado" que pide el programa de esta unidad.

**"Why Game Developers are afraid of Test Automation?"** — ★★★☆☆
Filipp Keks · Blog independiente · Inglés · Gratuito
`http://blog.filippkeks.com/2016/11/21/why-game-developers-are-afraid-of-test-automation.html`
Verificado por fetch directo (2016). Buen disparador de debate en clase sobre por qué la industria del videojuego adoptó testing automatizado más lento que otras áreas de software.

**Curso freemium — "Curso de Testing de Videojuegos"** (referencia, no cubre Unity/TDD)
Ricardo Izquierdo · Platzi · Español · Primera clase gratis, resto de pago
`https://platzi.com/cursos/testing-videojuegos/`
Verificado por fetch directo. **No cubre Unity ni pruebas unitarias** — es QA/testing manual general (caja negra/blanca, testing exploratorio y de regresión). Útil solo como referencia de la mitad "manual" del contraste, igual tratamiento que el curso de Platzi citado en Unidad 2.

---

## Material previo de la cátedra (2024)

**`docs/Unidad 3 -2024.pptx`** — fuente reciclada, ver [`01-analisis-programa-y-objetivos.md`](./01-analisis-programa-y-objetivos.md), Sección A
36 diapositivas basadas en el tutorial oficial de Unity Learn *"Unit Testing"* (proyecto Crashteroids). Cita como fuente `docs.unity3d.com/Packages/com.unity.test-framework@1.1/manual/index.html` — **versión de paquete desactualizada** respecto a la referencia vigente de esta investigación (ver más abajo); los pasos de configuración (Package Manager, Test Runner, assembly definitions) siguen siendo correctos en su lógica general.

---

## Diferencias entre versiones de Unity relevantes para esta clase

1. **NUnit:** tanto Test Framework 1.4.6 (Unity 2019.2+) como la versión más reciente documentada usan **NUnit 3.5** — no hay diferencia relevante entre Unity 2021/2022 LTS y Unity 6 en atributos ni assertions para esta unidad.
2. **Empaquetado:** en Unity 2019.2–2022 LTS, el Test Framework se instala/actualiza como paquete independiente vía Package Manager (ver diapositiva 18, [RECICLADO 2024]). En **Unity 6**, es un *core package* fijo a la versión del Editor — no hace falta gestionarlo por separado.
3. **Edit Mode vs. Play Mode:** el comportamiento documentado (sin corrutinas en Edit Mode, corrutinas vía `[UnityTest]` en Play Mode) es **idéntico** entre las versiones de manual consultadas (6000.2–6000.4) y las versiones de paquete 1.0.x–1.4.x — no se detectaron diferencias sustantivas.
4. **Rutas de menú** (`Window ▸ General ▸ Test Runner`, `Assets ▸ Create ▸ Testing ▸ ...`) se mantienen iguales en las versiones de Unity 6 consultadas. No se verificó directamente la UI de 2021/2022 LTS por fetch — si la cátedra usa esa versión, conviene confirmar visualmente antes de proyectar capturas.

## Qué no se pudo verificar

- El video en español más citado por buscadores sobre testing unitario en Unity (`YsNVOvGMkS0`) **no existe** (confirmado por doble verificación oEmbed) — se documenta para que la cátedra no vuelva a encontrarlo por error.
- El contenido íntegro del libro de Kent Beck sobre TDD no tiene una fuente web oficial y gratuita verificable.
- El contenido detallado de varios videos de YouTube (transcripciones, minutos exactos) no pudo extraerse por las limitaciones de la herramienta de verificación con esa plataforma — se confirmó únicamente existencia, autor y canal.
- Los TFG de la Universidad de Alicante sobre testing de videojuegos tuvieron verificación parcial o mínima (páginas renderizadas por JavaScript); uno de ellos parece centrado en Unreal Engine, no en Unity, por lo que se excluyó de la tabla comparativa.
- El video de GDC 2014 "Practical Unit Tests" y el video completo de "TestMonkey" (GDC 2023) están detrás del paywall de GDC Vault — solo sus diapositivas son de acceso gratuito y verificado.

---

## Comparación de recursos

| Recurso | Idioma | Gratuito | Autoridad | Valoración |
|---|---|---|---|---|
| Edit mode and Play mode tests (Unity) | EN | Sí | Oficial | ★★★★★ |
| Create a test assembly / Create a test (Unity) | EN | Sí | Oficial | ★★★★★ |
| Asserting and comparing (Unity) | EN | Sí | Oficial | ★★★★★ |
| Game Development Testing and QA Best Practices (Unity) | EN | Sí | Oficial | ★★★★★ |
| Best practices for writing unit tests (Microsoft) | EN | Sí | Oficial | ★★★★★ |
| Test-driven development - Visual Studio (Microsoft) | EN | Sí | Oficial | ★★★★★ |
| Test-Driven Development bliki (Martin Fowler) | EN | Sí | Autoridad reconocida | ★★★★★ |
| GamwUS: TDD y Videojuegos (U. Sevilla) | ES | Sí | Institución educativa | ★★★★★ |
| Sea of Thieves — Automated Testing (GDC/Rare) | EN | Sí | Industria AAA | ★★★★★ |
| Call of Duty — Automated Testing (GDC/Activision) | EN | Sí | Industria AAA | ★★★★★ |
| QA your code — Unite Copenhagen 2019 (Unity) | EN | Sí | Oficial | ★★★★★ |
| Practical Unit Tests, slides (Andrew Fray, GDC 2014) | EN | Sí (slides) | Industria | ★★★★★ |
| Testing automatizado de juegos (Nerdearla) | ES | Sí | Comunidad reconocida | ★★★★☆ |
| Curso TDD (JJ Merelo, U. Granada) | ES | Sí | Institución educativa | ★★★★☆ |
| TFG UCM — trazas de juego | ES | Sí | Institución educativa | ★★★★☆ |
| TestMonkey, slides (Sony Santa Monica) | EN | Sí (slides) | Industria AAA | ★★★★☆ |
| Testing manual vs. automatizado (Abstracta) | ES | Sí | Industria (testing) | ★★★★☆ |
| TDD in Unity3D (Amat/Weimann) | EN | Sí | Canal reconocido | ★★★★☆ |
| Serie TDD in Unity (Infallible Code) | EN | Sí | Canal reconocido | ★★★★☆ |
| Introduction to Unity Unit Testing (Kodeco) | EN | Sí (registro) | Institución educativa reconocida | ★★★★☆ |
| Qué es el UNIT TEST en Unity (Codearte) | ES | Sí | Canal independiente | ★★★☆☆ |
| Unit Testing en C# (NicoPaez) | ES | Sí | Autor independiente | ★★★☆☆ |
| Pruebas — cátedra UNPSJB | ES | Sí | Institución educativa | ★★★☆☆ |
| Why Game Developers are afraid of Test Automation (blog) | EN | Sí | Blog independiente | ★★★☆☆ |
| Lista de materiales TDD (tumblr, Gutiérrez) | ES | Sí | Institución educativa | ★★★☆☆ |
| Unity Unit Testing Master (Codearte) | ES | **No** (pago) | Canal independiente | ★★★☆☆ |
| Curso de Testing de Videojuegos (Platzi) | ES | Freemium | Plataforma reconocida | ★★★☆☆ |
| TDD by Example (canal 25games) | EN | Sí | Sin verificar | ★★☆☆☆ |

---

## Bibliografía / Webgrafía

- Unity Technologies. *Test Framework* (Manual Unity 6). `https://docs.unity3d.com/Manual/com.unity.test-framework.html`
- Unity Technologies. *Edit mode and Play mode tests*. `https://docs.unity3d.com/6000.4/Documentation/Manual/test-framework/edit-mode-vs-play-mode-tests.html`
- Unity Technologies. *Asserting and comparing*. `https://docs.unity3d.com/6000.3/Documentation/Manual/test-framework/asserting-and-comparing.html`
- Unity Technologies. *Game Development Testing and QA Best Practices*. `https://unity.com/how-to/testing-and-quality-assurance-tips-unity-projects`
- Microsoft. *Best practices for writing unit tests*. `https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices`
- Microsoft. *Test-driven development - Visual Studio*. `https://learn.microsoft.com/en-us/visualstudio/test/quick-start-test-driven-development-with-test-explorer?view=visualstudio`
- Fowler, M. (2005, act. 2023). *Test Driven Development*. `https://martinfowler.com/bliki/TestDrivenDevelopment.html`
- Beck, K. (2002). *Test-Driven Development: By Example*. Addison-Wesley. ISBN 978-0321146533.
- Gutiérrez, J. (2013). *GamwUS: Desarrollo Dirigido por Pruebas y Videojuegos*. `https://es.slideshare.net/slideshow/gamwus-desarrollo-diriguido-por-pruebas-y-videojuegos/27015200`
- Masella, R. (2019). *Automated Testing of Gameplay Features in Sea of Thieves*. GDC. `https://www.youtube.com/watch?v=X673tOi8pU8`
- van Valburg, J. Activision Research. *Automated Testing in Call of Duty*. `https://research.activision.com/publications/archives/automated-testing-in-call-of-duty`
- Fray, A. (2014). *Practical Unit Tests*. GDC. `https://www.slideshare.net/slideshow/practical-unit-testing-gdc-2014/32594081`
- Ramirez, E. D. (2024). *Planificación de cátedra: Diseño según Plataformas de Juego*. Facultad de Ingeniería, Universidad Nacional de Jujuy.
- Referencias en inglés, de pago, o de verificación parcial señaladas explícitamente arriba.
