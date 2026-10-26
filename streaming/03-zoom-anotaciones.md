# Zoom y anotaciones en vivo

Esto es lo que en la imagen de referencia se ve cuando la instructora resalta o hace zoom sobre parte de la diapositiva mientras habla.

## Opción principal: ZoomIt

1. Descargar de https://learn.microsoft.com/sysinternals/downloads/zoomit (no requiere instalación, es un `.exe` portable).
2. Ejecutarlo una vez — queda corriendo en la bandeja del sistema (system tray), no hace falta abrirlo cada vez, se le puede poner en inicio automático de Windows.
3. Configurar teclas rápidas (se configuran en la ventana principal de ZoomIt al abrirlo):
   - **Zoom en vivo**: tecla por defecto `Ctrl+1` → la rueda del mouse controla el nivel de zoom, click para fijar.
   - **Modo dibujo**: tecla por defecto `Ctrl+2` → click y arrastrás para dibujar, `R`/`Y`/`G` cambian de color (rojo/amarillo/verde), `Esc` para salir.
   - **Break timer** (opcional): útil para mostrar una cuenta regresiva en pantalla completa si hacés una pausa en la clase.
4. Funciona sobre **cualquier ventana activa** (PowerPoint, VS Code, Unity Editor, navegador) porque actúa a nivel de todo el escritorio — como OBS está capturando la pantalla/ventana, todo lo que hace ZoomIt se transmite automáticamente sin configuración adicional en OBS.

### Importante sobre "Captura de ventana" vs "Captura de pantalla" en OBS
Si en OBS usás **Captura de ventana** (recomendado, ver doc 02), ZoomIt dibuja una capa superpuesta a nivel de todo el escritorio, así que **sigue viéndose igual dentro de la ventana capturada**. Si notás que las anotaciones de ZoomIt no aparecen en el stream, cambiar temporalmente a **Captura de pantalla completa** en esa fuente.

## Opción dentro de PowerPoint (sin herramientas externas)

Si solo necesitás anotar sobre diapositivas (no sobre código), PowerPoint trae herramientas nativas:
- Pestaña **Dibujar** → lápiz/resaltador → dibujás directo sobre la diapositiva en modo Presentación.
- En modo Presentación, click derecho → **Opciones de puntero** → **Bolígrafo/Resaltador/Láser**.
- Limitación: no permite hacer zoom real (solo resalta), y no funciona fuera de PowerPoint (no sirve para anotar sobre VS Code o Unity).

## Alternativa: Epic Pen

Si ZoomIt se siente limitado (por ejemplo, querés dejar anotaciones fijas en pantalla mientras seguís trabajando, no solo un dibujo momentáneo):
- https://www.epicpen.com/
- Permite dibujar sobre cualquier ventana de forma persistente (no se borra automáticamente) y tiene una barra de herramientas con colores/grosores.
- Versión gratuita tiene marca de agua/funciones limitadas; versión Pro es paga.

## Zoom nativo del sistema operativo (respaldo de emergencia)

Si ninguna herramienta externa funciona (por ejemplo, bloqueada por política de la empresa/escuela, ver doc 04):
- **Lupa de Windows**: `Tecla Windows + "+"` para acercar, `Tecla Windows + Esc` para salir. No permite dibujar, pero sirve para hacer zoom rápido sobre código o una parte de la diapositiva.
- Configurar en **Configuración → Accesibilidad → Lupa** el modo "Pantalla completa" o "Lente" (este último crea un recuadro de zoom que sigue al mouse, similar visualmente a ZoomIt).
