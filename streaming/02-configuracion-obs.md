# Configuración paso a paso de OBS Studio

## 1. Instalación

1. Descargar desde https://obsproject.com/es
2. Ejecutar el instalador como administrador.
3. Al primer inicio, OBS ofrece un **"Asistente de configuración automática"** (Auto-Configuration Wizard) → elegir **"Optimizar para transmitir en vivo"** y seguir los pasos (detecta tu ancho de banda y hardware).

## 2. Crear la escena base

1. En el panel **Escenas** (abajo a la izquierda), click derecho → **Agregar** → nombrarla, ej. `Clase - Diapositivas`.
2. En el panel **Fuentes**, click en `+` para agregar cada fuente:

### Fuente 1: Captura de pantalla/ventana
- `+` → **Captura de ventana** (recomendado sobre "Captura de pantalla completa" porque evita mostrar notificaciones de Windows u otras apps por error).
- Seleccionar la ventana de PowerPoint, VS Code o Unity Editor.
- Ajustar tamaño arrastrando las esquinas para que ocupe el lienzo completo (Base 1920x1080 recomendado).

### Fuente 2: Webcam
- `+` → **Dispositivo de captura de video** → elegir tu cámara.
- Redimensionar y arrastrar a la esquina deseada (ej. inferior izquierda, como en la referencia).
- Opcional, para bordes redondeados/circulares: click derecho sobre la fuente → **Filtros** → `+` → **Image Mask/Blend** → cargar una imagen PNG con transparencia circular (se puede generar una gratis en https://www.canva.com o buscar "circle mask png transparente").

### Fuente 3: Audio del micrófono
- `+` → **Captura de entrada de audio** → elegir tu micrófono.
- En el **Mezclador de Audio** (abajo), click en el engranaje del canal de mic → **Filtros** → agregar:
  - **Supresor de ruido** (Noise Suppression, método RNNoise da mejor calidad).
  - **Compresor** (opcional, nivela el volumen de la voz).

## 3. Escenas adicionales (recomendado para clases de programación)

Repetir el proceso creando escenas separadas y reutilizando la webcam en todas:
- `Clase - Diapositivas` (PowerPoint + webcam)
- `Clase - Codigo` (VS Code o Unity Editor + webcam)
- `Clase - Solo camara` (para presentarte al inicio/cierre)

Truco para no repetir la fuente de webcam en cada escena: crear la escena de webcam como una fuente independiente y agregarla como **"Escena"** dentro de cada escena nueva (OBS permite anidar escenas como fuentes), así si movés la cámara una vez se actualiza en todas.

## 4. Configurar hotkeys para cambiar de escena

**Configuración (Settings) → Hotkeys** → asignar teclas rápidas tipo `Ctrl+1`, `Ctrl+2`, `Ctrl+3` para cambiar entre las escenas sin tocar el mouse mientras hablás.

## 5. Configurar la transmisión a YouTube

1. Entrar a https://studio.youtube.com → **Crear** → **Ir en vivo**.
2. Si es la primera vez, YouTube pide verificar el canal (puede tardar hasta 24 h la primera vez) — **hacerlo con anticipación, no el día de la clase**.
3. En "Transmitir" → copiar la **Clave de transmisión (Stream Key)**.
4. En OBS: **Configuración → Emisión (Stream)** → Servicio: `YouTube - RTMPS` → pegar la clave.
5. Antes de la clase real, probar con una transmisión en modo **"No listado"** o **"Privado"** para verificar audio/video sin exponerlo públicamente.

## 6. Configurar el video/salida

**Configuración → Video**:
- Resolución base y de salida: 1920x1080 (o 1280x720 si el internet es limitado).
- FPS: 30 (suficiente para clases; 60 solo si vas a mostrar gameplay fluido).

**Configuración → Emisión (Output) → Avanzado**:
- Bitrate de video: 3500–6000 Kbps para 1080p30 (ajustar según tu velocidad de subida real).
- Encoder: `x264` (CPU) o `NVENC` (si tenés GPU NVIDIA, libera CPU).

## 7. Iniciar la transmisión

Botón **"Iniciar transmisión"** en la esquina inferior derecha. Verificar en YouTube Studio que la señal llega (puede tardar 10-20 segundos en aparecer el preview).

## 8. Grabación local simultánea (recomendado)

**Configuración → Salida → Grabación** → definir carpeta de destino. Botón **"Iniciar grabación"** (independiente del streaming) para tener una copia local de la clase en alta calidad, útil para subir después a una plataforma de curso o editar clips.
