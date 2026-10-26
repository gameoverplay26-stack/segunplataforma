using UnityEngine;

// Ajusta un RectTransform a Screen.safeArea (notch, barras del sistema).
// UnityEngine.Device.Screen respeta el Device Simulator del Editor.
[RequireComponent(typeof(RectTransform))]
public class SafeAreaFitter : MonoBehaviour
{
    private RectTransform rect;
    private Rect lastSafeArea;
    private Vector2Int lastScreenSize;

    private void Awake()
    {
        rect = GetComponent<RectTransform>();
    }

    private void OnEnable()
    {
        Apply();
    }

    private void Update()
    {
        var size = new Vector2Int(UnityEngine.Device.Screen.width, UnityEngine.Device.Screen.height);
        if (UnityEngine.Device.Screen.safeArea != lastSafeArea || size != lastScreenSize)
        {
            Apply();
        }
    }

    private void Apply()
    {
        Rect safe = UnityEngine.Device.Screen.safeArea;
        int width = UnityEngine.Device.Screen.width;
        int height = UnityEngine.Device.Screen.height;
        lastSafeArea = safe;
        lastScreenSize = new Vector2Int(width, height);
        if (width <= 0 || height <= 0)
        {
            return;
        }

        rect.anchorMin = new Vector2(safe.xMin / width, safe.yMin / height);
        rect.anchorMax = new Vector2(safe.xMax / width, safe.yMax / height);
        rect.offsetMin = Vector2.zero;
        rect.offsetMax = Vector2.zero;
    }
}
