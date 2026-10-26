using UnityEngine;
using UnityEngine.InputSystem;

// Reglas de la capa de consola, sin MonoBehaviour para probarlas con unit tests de Edit Mode.
// Tamaño de texto: Xbox Accessibility Guidelines 101, cuerpo de 26 px como mínimo a 1080p.
public static class ConsoleRules
{
    public const float MinBodyTextPxAt1080 = 26f;
    public const string QuitMethod = "Quit";

    // En consola la app la cierra el sistema: un botón que llama a Quit no corresponde.
    public static bool IsQuitMethod(string methodName) => methodName == QuitMethod;

    // Solo un mando físico: los controles en pantalla (OnScreenStick/OnScreenButton) son un gamepad
    // virtual que se agrega y se quita al mostrarlos u ocultarlos, y eso no es "perder el control".
    public static bool ShouldPauseOnDeviceChange(bool isPhysicalGamepad, InputDeviceChange change) =>
        isPhysicalGamepad && (change == InputDeviceChange.Removed || change == InputDeviceChange.Disconnected);

    // Mismo cálculo que CanvasScaler en modo Scale With Screen Size / Match Width Or Height.
    public static float ScaleWithScreenSize(Vector2 screen, Vector2 reference, float match)
    {
        float w = Mathf.Log(screen.x / reference.x, 2f);
        float h = Mathf.Log(screen.y / reference.y, 2f);
        return Mathf.Pow(2f, Mathf.Lerp(w, h, match));
    }

    // Altura equivalente a 1080p de un texto de fontSize en un canvas con esa escala.
    public static float PxAt1080(float fontSize, float canvasScale, float screenHeight) =>
        fontSize * canvasScale * 1080f / screenHeight;

    // Menor fontSize que llega a 26 px a 1080p (con un margen para el redondeo de punto flotante).
    public static int MinFontSize(float canvasScale, float screenHeight) =>
        Mathf.CeilToInt(MinBodyTextPxAt1080 * screenHeight / (1080f * canvasScale) - 0.001f);
}
