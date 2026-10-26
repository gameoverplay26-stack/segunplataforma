# Guía de la docente: probar Asteroides y el Platformer en la Xbox (Developer Mode)

- **Para quién:** la docente, que hace la demo con su propia consola.
- **Consola:** Xbox Series X de 1 TB, modelo japonés.
- **Qué se logra:** instalar y jugar en la consola **cuatro paquetes**, sin publicar nada:

  | Paquete (nombre en la consola) | Proyecto | Qué muestra |
  |---|---|---|
  | Asteroides (original) | `proyectos-unity/Asteroides/asteroide-final` | El juego tal como está hoy (porteado a móvil, **sin cambios para consola**) |
  | Asteroides (consola) | `proyectos-unity/Asteroides-Xbox` | El mismo juego con la **capa de consola** |
  | Platformer (original) | `proyectos-unity/2D-Platformer-Unity-v2` | El Platformer v2 tal como está hoy |
  | Platformer (consola) | `proyectos-unity/2D-Platformer-Xbox` | El Platformer con la capa de consola |

- **Qué NO es:** no es el desarrollo oficial de Xbox (ID@Xbox, GDK, kit de desarrollo bajo NDA), no es certificación y no se puede publicar. Microsoft ya no acepta juegos UWP en la tienda de Xbox. Es una **demo local** sobre una consola comercial.
- **Estado:** PROPUESTO. Los pasos de Microsoft se tomaron de la documentación oficial (fuentes al final). Que estos paquetes corran en la consola es **UNKNOWN** hasta la primera prueba: completá la tabla del paso 8.

---

## 0. Antes de empezar: lo que hace falta

| Qué | Detalle | Estado en la PC de la cátedra |
|---|---|---|
| Consola | Series X con **5 GB libres** como mínimo y un control Xbox | — |
| Cuenta de Microsoft | La que se usará para la cuenta de desarrollador (paso 1) | — |
| Red | PC y consola en la **misma red**. Microsoft recomienda **cable** para instalar | Revisar la red del aula |
| Unity 6000.3.11f1 | Con *Universal Windows Platform Build Support* (`MetroSupport`) | ✅ instalado (verificado) |
| Visual Studio 2022 | Carga de trabajo *Desarrollo de la Plataforma universal de Windows*, *herramientas C++ de UWP* (v143) y Windows SDK 10.0.19041 o posterior | ✅ instalado el 2026-10-26 (ver `PORTEO-XBOX.md` §5) |
| Paquetes generados | `proyectos-unity/Tools-Xbox/generar_builds_xbox.ps1` (paso 5) | ✅ los 4 `.msix` generados el 2026-10-26 (`PORTEO-XBOX.md` §5). Si no cambiaste nada, saltá al paso 6 |

> **Importante:** mientras la consola está en Developer Mode **no corren los juegos y apps comerciales**. Se vuelve al modo normal en un minuto (paso 9), y los juegos instalados y las partidas guardadas en la nube no se pierden.

---

## 0 bis. En otra PC: preparar todo y generar los paquetes

Los paquetes **no viajan por git** (`Builds/` y `Certificados/` están excluidos): en otra PC se generan de nuevo. Si esa PC solo va a **instalar** en la consola, alcanza con copiar las cuatro carpetas `…_Master_Test` con un pendrive y seguir desde el paso 1.

1. **Traer el repo** (`git pull`, o `git clone https://github.com/gameoverplay26-stack/segunplataforma.git C:\Developer\unity\2026\clases-en-vivo`).
2. **Verificar los requisitos** con Unity cerrado:
   ```powershell
   powershell -ExecutionPolicy Bypass -File proyectos-unity\Tools-Xbox\verificar_requisitos_xbox.ps1
   ```
   Muestra una tabla OK / FALTA con lo mismo que se instaló en la PC de la cátedra el 2026-10-26, y cómo resolver cada falta:

   | Requisito | Qué se comprueba |
   |---|---|
   | Unity 6000.3.11f1 | `Unity.exe` en la ruta de Unity Hub (otra ruta: `-Unity "D:\…\Unity.exe"`) |
   | Módulo UWP de Unity | `Data\PlaybackEngines\MetroSupport` (Unity Hub → Add modules → *Universal Windows Platform Build Support*) |
   | Visual Studio 2022 | Cualquier edición; Community alcanza |
   | Carga de trabajo UWP | `Microsoft.VisualStudio.Workload.Universal` |
   | C++ para UWP | `Microsoft.VisualStudio.ComponentGroup.UWP.VC` y `Microsoft.VisualStudio.Component.VC.Tools.x86.x64` (IL2CPP genera C++) |
   | MSBuild | El de Visual Studio 2022 |
   | Windows SDK | 10.0.19041 o posterior en `Windows Kits\10\Include` (en la cátedra: 10.0.26100). **Ojo:** en la cátedra, la carga de trabajo se instaló *sin* el SDK y hubo que agregarlo aparte |
   | Proyectos | Los cuatro, con `Assets/Editor/BuildXbox.cs` |
   | Rutas largas (ENV-01) | En la cátedra hay rutas de **280 caracteres** dentro de `Library` y funciona porque Windows tiene `LongPathsEnabled = 1`. Sin eso, la ruta del repo tiene que ser muy corta |
   | Certificados | `New-SelfSignedCertificate` disponible |
3. **Instalar lo que falte de Visual Studio** (pide permisos de administrador y descarga varios GB):
   ```powershell
   powershell -ExecutionPolicy Bypass -File proyectos-unity\Tools-Xbox\verificar_requisitos_xbox.ps1 -Instalar
   ```
   Unity, el módulo UWP y las rutas largas se resuelven a mano, con la solución que indica la tabla. Para rutas largas, como administrador: `reg add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f` y reiniciar.
4. **Generar** (paso 5 de esta guía): `generar_builds_xbox.ps1` vuelve a correr la verificación y no compila si falta algo. La primera vez tarda bastante, porque Unity importa cada proyecto (`Library` no viaja por git).

## 1. Crear la cuenta de desarrollador (una sola vez, gratis)

1. Entrar a **https://storedeveloper.microsoft.com** y elegir **Get started for free → Individual developer**. Es el único camino sin costo de registro; otros caminos muestran el flujo viejo, que cobraba.
2. Iniciar sesión con la cuenta de Microsoft.
3. Verificar la identidad con un **documento y una selfie** desde el celular, con buena luz.
4. Completar el perfil y entrar al **Partner Center** (*Apps & Games*). Si no aparece enseguida, esperar unos 5 minutos y recargar.

Esta cuenta **no publica nada**: solo habilita la consola. Cada cuenta tiene un número limitado de activaciones de consolas.

## 2. Activar el Developer Mode en la consola

1. Encender la consola y buscar en la tienda la app **Xbox Dev Mode**.
   - **Modelo japonés:** no se verificó si la app aparece con la región de Japón. Si no aparece, cambiar la región en *Configuración → Sistema → Idioma y ubicación* y volver a buscarla.
2. Abrir la app y **anotar el código** que muestra.
3. En la PC, con la cuenta del paso 1, entrar a **https://partner.microsoft.com/xboxconfig/devices**.
4. Escribir el código y elegir **Agree and activate**. La consola muestra una pantalla de progreso.
5. Al terminar, en la app Xbox Dev Mode elegir **Switch and restart**. El reinicio tarda más de lo normal.
6. Al volver, la consola abre **Dev Home**. Esa es la señal de que está en Developer Mode.

## 3. Preparar Dev Home y el Device Portal

1. **Iniciar sesión con un usuario** en la consola. Sin usuario, la instalación falla con el error `0x87e10008`.
2. Anotar la **dirección IP** que muestra Dev Home arriba a la izquierda.
3. En Dev Home, pestaña **Home → Remote Access → Remote Access Settings**:
   - tildar **Enable Xbox Device Portal**;
   - en *Authentication*, **Set username and password** y guardar. Usar un usuario y una contraseña solo para esto.
4. Cerrar y anotar la **URL** que aparece en *Remote Access*: es la dirección del Device Portal.

## 4. Abrir el Device Portal desde la PC

1. En el navegador de la PC, abrir la URL del paso 3.4.
2. Aparece una **advertencia de certificado**. Es esperable, porque la consola usa un certificado propio: *Detalles → Ir a la página web*.
3. Ingresar el usuario y la contraseña del paso 3.3.
4. **Una sola vez:** en **Settings → Preference Settings**, tildar **Treat UWP apps as games by default**. Sin eso, la consola trata los paquetes como *apps*: 1 GB de memoria y una parte de la GPU, en lugar de 5 GB y la GPU completa de un *game*.

## 5. Generar los paquetes en la PC

Con **Unity cerrado** para esos proyectos, en PowerShell desde la raíz del repo:

```powershell
powershell -ExecutionPolicy Bypass -File proyectos-unity\Tools-Xbox\generar_builds_xbox.ps1
```

Por cada uno de los 4 proyectos, el script:
1. Crea un **certificado de prueba** autofirmado en `Certificados/`. No se versiona en git y se regenera solo.
2. Corre Unity en batchmode (`BuildXbox.Build`): UWP, **x64**, familias Xbox + Desktop. El resultado es la solución de Visual Studio en `Builds/UWP/`.
3. Compila con **msbuild** en *Master x64* y arma el paquete para instalación local en `Builds/Xbox-Paquete/`.
4. Al final lista la ruta de cada paquete.

Para uno o varios proyectos: `... generar_builds_xbox.ps1 -Proyectos "Asteroides-Xbox,2D-Platformer-Xbox"`. Cuánto tarda: 1 a 5 minutos de Unity más varios minutos de compilación de C++ por proyecto.

**Dónde quedan:** `Builds/Xbox-Paquete/<Nombre>_1.0.0.0_x64_Master_Test/`. Esa carpeta trae el `.msix`, el `.cer` y `Dependencies/x64/Microsoft.VCLibs.x64.14.00.appx`. Para llevarla a otra PC, copiar la carpeta completa.
Si algo falla, el script indica el log: `Logs/build-xbox.log` (Unity) o `Logs/build-xbox-msbuild.log` (Visual Studio).

## 6. Instalar los paquetes desde el Device Portal

Por cada paquete:
1. En el Device Portal, página **Home**, sección *My games & apps*, elegir **Add** (agregar).
2. Elegir el archivo `.msix` (o `.appx`) de `Builds/Xbox-Paquete/…`.
3. Agregar la **dependencia** `Dependencies/x64/Microsoft.VCLibs.x64.14.00.appx`, que está junto al paquete. Si la consola ya la tiene, la saltea. Si pide un certificado, usar el `.cer` de la misma carpeta.
4. **Install / Start** y esperar a que termine.
5. El juego aparece en *My games & apps* del Device Portal y en **Dev Home** de la consola, con el nombre de la tabla del inicio.

**Plan B de instalación:** abrir con Visual Studio la solución de `Builds/UWP/`, elegir *x64*, *Master* y **Remote Machine** con la IP de la consola, autenticación *Universal (Unencrypted Protocol)*, y apretar F5. La primera vez pide un **PIN**, que se ve en Dev Home con *Show Visual Studio pin*.

**Reinstalar después de cambiar algo:** si el Device Portal se niega porque "ya está instalado", primero quitar el juego (*Actions → Remove*, con el juego cerrado) y volver a agregarlo.

## 7. Jugar

- Lanzar desde Dev Home o desde el Device Portal (*Actions → Launch*).
- Usar **solo el control**: la idea es comprobar qué pasa cuando no hay mouse ni teclado.
- Capturas para la evidencia: Device Portal → **Media capture → Capture Screenshot**.
- Rendimiento: Device Portal → **Performance** (CPU, memoria, GPU y frame rate en vivo).

## 8. Protocolo de prueba (llenar en la consola)

Estados: **PASS / FAIL / UNKNOWN**. La columna "Esperado" es la **hipótesis** que sale del código, no un resultado.

| ID | Prueba | Asteroides original | Asteroides consola | Platformer original | Platformer consola |
|---|---|---|---|---|---|
| XB-00 | El paquete se instala y el juego abre | Esperado: PASS | Esperado: PASS | Esperado: PASS | Esperado: PASS |
| XB-AC-01 | Todo el flujo con el control (menú → partida → fin → menú) | Esperado: **FAIL**. Start no tiene foco y el módulo de UI es el del Input Manager antiguo | Esperado: PASS | Esperado: **FAIL**. El menú no tiene foco inicial (EV-018) | Esperado: PASS |
| XB-AC-02 | Siempre hay un botón con foco visible (amarillo) en los menús | Esperado: FAIL | Esperado: PASS | Esperado: FAIL | Esperado: PASS |
| XB-AC-03 | Texto legible desde el sillón (26 px o más a 1080p) | A medir | Esperado: PASS (en tests) | A medir | Esperado: PASS (en tests) |
| XB-AC-04a | Menu (≡) pausa y reanuda la partida | Esperado: FAIL (no hay pausa) | Esperado: PASS | Esperado: FAIL | Esperado: PASS |
| XB-AC-04b | Al apagar o desconectar el control, el juego se pausa con aviso | Esperado: FAIL | Esperado: PASS | Esperado: FAIL | Esperado: PASS |
| XB-05 | Botón Quit | No tiene | No tiene | Esperado: visible; qué hace en consola es UNKNOWN | Esperado: oculto |
| XB-06 | La nave o el personaje se mueven con el stick y el D-pad, y A dispara o salta | Esperado: PASS (Input System ya lee el gamepad) | Esperado: PASS | Esperado: PASS | Esperado: PASS |
| XB-07 | Frame rate estable (Device Portal → Performance) | A medir | A medir | A medir | A medir |
| XB-08 | Imagen dentro de la TV, sin bordes cortados | A medir | A medir | A medir | A medir |

**Ese contraste es el centro de la demo:** el juego original *compila y corre* en la consola, pero no se puede **usar** como un juego de consola. La versión adaptada cambia la UI y el ciclo de vida, no el gameplay.

Al terminar, pasar los resultados a `PORTEO-XBOX.md` §7, con fecha y capturas.

## 9. Volver al modo normal

- **Para jugar normalmente:** en Dev Home, *Quick Actions → Leave developer mode*. La consola reinicia en modo normal. Para volver a Developer Mode, abrir la app Xbox Dev Mode → *Switch and restart* (no hace falta activar de nuevo).
- **Para salir del programa** (por ejemplo, si se vende la consola): desactivarla desde el Partner Center, en la misma página del paso 2.3.

## 10. Problemas frecuentes

| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| No aparece la app Xbox Dev Mode | Región de la consola | Paso 2.1: cambiar la región |
| Error `0x87e10008` al instalar | No hay usuario con sesión iniciada | Iniciar sesión en la consola |
| El navegador no abre el Device Portal | Otra red o subred, o el Device Portal está apagado | Misma red (cable); revisar el paso 3.3 |
| "Ya está instalado" | Mismo nombre y versión de paquete | Quitar el juego y volver a instalarlo |
| Falta una dependencia | No se agregó `Dependencies/x64` | Repetir el paso 6.3 |
| El juego va lento | Instalado como *app* (1 GB) | Paso 4.4 (*Treat UWP apps as games*) y reinstalar |
| Unity: *Could not find any supported UWP SDK* | Falta el Windows SDK | Instalar el SDK (sección 0) |
| Unity se queja de que el proyecto está abierto | Unity sigue abierto | Cerrarlo y repetir el paso 5 |

## 11. Qué NO demuestra esta prueba

- **No** es cumplir los *Xbox Requirements* ni pasar una certificación: eso exige el programa de partners.
- **No** usa el GDK (logros, partidas en la nube, usuarios de Xbox, PLM real del sistema). La pausa por pérdida de foco es una aproximación con `OnApplicationFocus`.
- En una consola comercial en Developer Mode, un juego UWP tiene **5 GB y 4 núcleos exclusivos**, no el hardware completo de un kit de desarrollo.
- No dice nada sobre PlayStation ni Nintendo: sus requisitos no son públicos.

## Fuentes (consultadas el 2026-10-26)

- Microsoft, *Xbox Developer Mode activation*: https://learn.microsoft.com/en-us/windows/uwp/xbox-apps/devkit-activation
- Microsoft, *Steps to open a Microsoft Store developer account* (sin costo de registro): https://learn.microsoft.com/en-us/windows/apps/publish/partner-center/open-a-developer-account
- Microsoft, *Getting started with UWP app development on Xbox One*: https://learn.microsoft.com/en-us/windows/uwp/xbox-apps/getting-started
- Microsoft, *Device Portal for Xbox*: https://learn.microsoft.com/en-us/windows/uwp/xbox-apps/device-portal-xbox
- Microsoft, *Windows Device Portal overview* (instalar paquetes y certificados): https://learn.microsoft.com/en-us/windows/uwp/debug-test-perf/device-portal
- Microsoft, *System resources for UWP apps and games on Xbox*: https://learn.microsoft.com/en-us/windows/uwp/xbox-apps/system-resource-allocation
- Microsoft, *UWP on Xbox FAQ* (juegos UWP no aceptados en la tienda): https://learn.microsoft.com/en-us/windows/uwp/xbox-apps/frequently-asked-questions
- Unity 6000.3, `PlayerSettings.WSATargetFamily` (familia Xbox): https://docs.unity.com/en-us/engine/6000.3/script-reference/unityeditor/playersettings/wsatargetfamily.md
- Microsoft, Xbox Accessibility Guidelines 101 (texto de 26 px a 1080p): ver SRC-003 en `EVIDENCE-LOG.md`
