# Posibles bloqueos y cómo resolverlos

## 1. Windows no detecta la webcam o el micrófono

- Verificar en **Configuración → Privacidad y seguridad → Cámara / Micrófono** que el acceso esté habilitado tanto a nivel general como para "Aplicaciones de escritorio" (OBS es una app de escritorio, no de la Store).
- Si OBS no lista el dispositivo: cerrar cualquier otra app que esté usando la cámara/mic (Zoom, Teams, navegador con una pestaña de videollamada abierta) — Windows solo permite un proceso exclusivo sobre la cámara en muchos drivers.
- Actualizar drivers de la cámara/audio desde **Administrador de dispositivos** si el dispositivo aparece con ícono de advertencia.

## 2. OBS no puede capturar Unity Editor o VS Code (pantalla en negro)

Causa común: aceleración por hardware con configuraciones de captura incompatibles (frecuente con apps que usan DirectX/OpenGL como Unity).
- Cambiar la fuente de **Captura de ventana** al modo de captura **"Windows 10 (WGC)"** en vez de "BitBlt" (opción dentro de las propiedades de la fuente).
- Si persiste, ejecutar OBS y Unity **ambos como administrador** (o ambos sin privilegios) — mezclar niveles de privilegio entre procesos suele bloquear la captura.
- Alternativa: usar "Captura de pantalla completa" en vez de "Captura de ventana" para esa escena puntual.

## 3. Antivirus / política corporativa bloquea la instalación de OBS o ZoomIt

- Ambas herramientas son gratuitas y de código abierto/reconocidas (ZoomIt es de Microsoft directamente), pero algunos antivirus corporativos (Windows Defender for Business, ESET gestionado, etc.) bloquean ejecutables no firmados por la organización.
- Solución: pedir al área de sistemas que agregue una excepción para `obs64.exe` y `ZoomIt64.exe`, o descargarlas desde una cuenta con permisos de instalación local.
- Si no se puede instalar nada: ver doc [05-alternativas.md](05-alternativas.md) para opciones basadas en navegador que no requieren instalación.

## 4. Firewall corporativo bloquea la transmisión RTMP a YouTube

- El streaming usa el puerto **1935 (RTMP)** o **443 (RTMPS)**. Si la red bloquea RTMP, usar el servicio configurado como **YouTube - RTMPS** (usa 443, el mismo puerto que HTTPS, mucho menos propenso a bloqueo).
- Si aun así falla: probar la transmisión desde una red distinta (datos móviles/hotspot) para descartar que sea un bloqueo de la red actual.

## 5. Verificación del canal de YouTube demora

- YouTube exige verificar el canal (con teléfono) para habilitar streams en vivo, y la primera habilitación de streaming puede tardar hasta 24 horas en activarse.
- **Hacerlo con al menos 1-2 días de anticipación** a la primera clase, nunca el mismo día.

## 6. Rendimiento: la PC se traba al transmitir + tener Unity/VS Code abiertos

- Bajar la resolución de salida a 720p30 en OBS (Configuración → Video).
- Cambiar el encoder de `x264` a `NVENC` (GPU) si hay GPU NVIDIA — libera CPU para Unity.
- Cerrar pestañas de navegador y apps en segundo plano no usadas durante la clase.
- Revisar en el **Administrador de tareas** si algún proceso está al 100% antes de empezar.

## 7. Internet inestable / corte de conexión durante el vivo

- Activar en OBS: **Configuración → Avanzado → Reconexión automática** (activada por defecto en versiones recientes).
- Tener como respaldo un hotspot del celular ya configurado y probado antes de la clase.
- Bajar el bitrate de subida (ver doc 02, punto 6) si la conexión es de baja velocidad, para evitar cortes por saturación del enlace.

## 8. Audio desincronizado o eco

- Usar auriculares (no parlantes) para evitar que el micrófono capte el audio de salida.
- En el Mezclador de Audio de OBS, verificar que no haya dos fuentes de audio activas capturando lo mismo (ej. audio del sistema + micrófono con eco).
- Si hay delay entre audio y video: click derecho en la fuente de audio → **Propiedades de audio avanzadas** → ajustar "Sync Offset" en milisegundos.

## 9. YouTube Live restringido en cuentas nuevas o de instituciones educativas

- Algunas cuentas de Google gestionadas por instituciones (Google Workspace for Education) tienen YouTube Live deshabilitado por política del administrador.
- Solución: usar una cuenta de YouTube personal/institucional distinta que sí tenga el permiso habilitado, o pedir al administrador de Workspace que habilite el servicio "YouTube" en la consola de administración.
