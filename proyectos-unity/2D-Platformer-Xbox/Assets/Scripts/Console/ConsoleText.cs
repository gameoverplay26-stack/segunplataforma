using TMPro;
using UnityEngine;
using UnityEngine.UI;

// Texto legible a distancia de TV: sube a 26 px a 1080p (XAG 101) los textos que quedan por debajo.
// Esta parte cambia según el proyecto: el Platformer usa TextMesh Pro (y Text en la capa de pausa).
public static class ConsoleText
{
    public static Vector2 ScreenSize =>
        Screen.width > 0 && Screen.height > 0 ? new Vector2(Screen.width, Screen.height) : new Vector2(1920, 1080);

    // Devuelve cuántos textos se agrandaron.
    public static int EnforceMinimum()
    {
        int changed = 0;
        foreach (TMP_Text text in Object.FindObjectsByType<TMP_Text>(FindObjectsInactive.Include, FindObjectsSortMode.None))
        {
            float scale = CanvasScale(text);
            if (scale <= 0f) continue;
            int min = ConsoleRules.MinFontSize(scale, ScreenSize.y);
            if (text.enableAutoSizing)
            {
                if (text.fontSizeMin >= min) continue;
                text.fontSizeMin = min;
                text.fontSizeMax = Mathf.Max(text.fontSizeMax, min);
            }
            else
            {
                if (text.fontSize >= min) continue;
                text.fontSize = min;
            }
            changed++;
        }
        foreach (Text text in Object.FindObjectsByType<Text>(FindObjectsInactive.Include, FindObjectsSortMode.None))
        {
            float scale = CanvasScale(text);
            if (scale <= 0f) continue;
            int min = ConsoleRules.MinFontSize(scale, ScreenSize.y);
            if (text.fontSize >= min) continue;
            text.fontSize = min;
            text.horizontalOverflow = HorizontalWrapMode.Overflow;
            text.verticalOverflow = VerticalWrapMode.Overflow;
            changed++;
        }
        return changed;
    }

    // Altura a 1080p del texto más chico que esté a la vista (para los tests y la evidencia).
    public static float SmallestVisiblePxAt1080()
    {
        float smallest = float.MaxValue;
        foreach (TMP_Text text in Object.FindObjectsByType<TMP_Text>(FindObjectsSortMode.None))
        {
            float scale = CanvasScale(text);
            if (scale <= 0f || string.IsNullOrWhiteSpace(text.text)) continue;
            float size = text.enableAutoSizing ? text.fontSizeMin : text.fontSize;
            smallest = Mathf.Min(smallest, ConsoleRules.PxAt1080(size, scale, ScreenSize.y));
        }
        foreach (Text text in Object.FindObjectsByType<Text>(FindObjectsSortMode.None))
        {
            float scale = CanvasScale(text);
            if (scale <= 0f || string.IsNullOrWhiteSpace(text.text)) continue;
            smallest = Mathf.Min(smallest, ConsoleRules.PxAt1080(text.fontSize, scale, ScreenSize.y));
        }
        return smallest;
    }

    // Escala del canvas raíz según su CanvasScaler. 0 = texto fuera de un canvas de pantalla (se ignora).
    public static float CanvasScale(Component text)
    {
        Canvas[] canvases = text.GetComponentsInParent<Canvas>(true);
        if (canvases.Length == 0) return 0f;
        Canvas root = canvases[canvases.Length - 1];
        if (root.renderMode == RenderMode.WorldSpace) return 0f;
        CanvasScaler scaler = root.GetComponent<CanvasScaler>();
        if (scaler == null) return 1f;
        switch (scaler.uiScaleMode)
        {
            case CanvasScaler.ScaleMode.ScaleWithScreenSize when scaler.screenMatchMode == CanvasScaler.ScreenMatchMode.MatchWidthOrHeight:
                return ConsoleRules.ScaleWithScreenSize(ScreenSize, scaler.referenceResolution, scaler.matchWidthOrHeight);
            case CanvasScaler.ScaleMode.ConstantPixelSize:
                return scaler.scaleFactor;
            default:
                return root.scaleFactor;
        }
    }
}
