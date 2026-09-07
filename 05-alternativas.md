# Alternativas si OBS/ZoomIt no son viables

## Si no se puede instalar OBS Studio

| Alternativa | Por qué considerarla | Enlace |
|---|---|---|
| **Streamlabs Desktop** | Mismo motor que OBS pero con overlays prearmados y configuración guiada más simple; misma política de instalación (puede toparse con el mismo bloqueo corporativo) | https://streamlabs.com/ |
| **Restream Studio** (basado en navegador) | Corre 100% desde el navegador (Chrome/Edge), sin instalar nada — permite compartir pantalla, cámara y transmitir a YouTube. Útil si hay bloqueo total de instalación de software | https://restream.io/studio |
| **YouTube Studio → "Ir en vivo" con webcam directo** | La opción más básica: YouTube permite transmitir directo desde el navegador con cámara+pantalla compartida (sin escenas ni superposición de cámara en esquina personalizable) | https://studio.youtube.com |
| **Zoom / Google Meet con grabación** | Si el objetivo es dar la clase a un grupo cerrado (no público), Zoom/Meet permiten compartir pantalla + verse en cámara simultáneamente y grabar la sesión, sin necesidad de configurar streaming | https://zoom.us / https://meet.google.com |

## Si no se puede instalar ZoomIt

| Alternativa | Por qué considerarla | Enlace |
|---|---|---|
| **Lupa de Windows (nativa)** | Ya viene instalada en Windows, no requiere descarga ni permisos especiales (ver doc 03, sección final) | Integrada en Windows |
| **PowerPoint Draw/Ink** | Nativo de PowerPoint, cubre el caso de anotar sobre diapositivas sin instalar nada extra | Integrado en Microsoft 365 |
| **Herramienta de recortes + zoom del navegador** | Para código: usar `Ctrl` + rueda del mouse para hacer zoom nativo en VS Code, o `Ctrl+"+"` para zoom del navegador — no es "zoom visual en vivo" pero logra el mismo efecto de legibilidad sin herramientas externas | N/A |

## Si el problema es la plataforma de streaming (no YouTube)

| Alternativa | Notas |
|---|---|
| **Twitch** | Alternativa a YouTube Live, muy usada para contenido de programación/videojuegos, no requiere verificación de canal tan estricta | https://twitch.tv |
| **Facebook Live / LinkedIn Live** | Si el público objetivo está más en esas redes | — |
| **Vimeo Livestream** | Opción de pago orientada a instituciones educativas, con mejor soporte y analíticas | https://vimeo.com/live |

## Si el hardware es muy limitado (PC de gama baja)

- Bajar a resolución 720p15-20 en OBS.
- Usar solo audio + diapositivas (sin webcam) como primer paso, agregar cámara cuando el rendimiento lo permita.
- Considerar transmitir solo el audio explicando sobre una grabación de pantalla pre-hecha del código, en vez de programar en vivo (reduce carga de CPU).
