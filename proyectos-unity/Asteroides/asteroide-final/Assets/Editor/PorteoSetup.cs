using UnityEditor;
using UnityEngine;
using UnityEngine.InputSystem.OnScreen;
using UnityEngine.UI;

// Aplica el porteo de entrada a los prefabs de forma reproducible.
// Uso (batchmode):
//   Unity.exe -batchmode -projectPath <ruta> -executeMethod PorteoSetup.Apply -quit -logFile <log>
// Es idempotente: si los componentes ya existen, no los duplica.
public static class PorteoSetup
{
    private const string GamePrefab = "Assets/Resources/Prefabs/Game.prefab";
    private const string UICanvasPrefab = "Assets/Prefabs/UICanvas.prefab";

    public static void Apply()
    {
        AddShipInputAdapter();
        AddMobileControls();
        AssetDatabase.SaveAssets();
        Debug.Log("[PorteoSetup] OK");
    }

    private static void AddShipInputAdapter()
    {
        GameObject root = PrefabUtility.LoadPrefabContents(GamePrefab);
        Ship ship = root.GetComponentInChildren<Ship>(true);
        if (ship.GetComponent<ShipInputAdapter>() == null)
        {
            ship.gameObject.AddComponent<ShipInputAdapter>();
        }
        string shipName = ship.gameObject.name;
        PrefabUtility.SaveAsPrefabAsset(root, GamePrefab);
        PrefabUtility.UnloadPrefabContents(root);
        Debug.Log("[PorteoSetup] ShipInputAdapter en " + shipName);
    }

    private static void AddMobileControls()
    {
        GameObject root = PrefabUtility.LoadPrefabContents(UICanvasPrefab);
        if (root.transform.Find("MobileControls") == null)
        {
            Sprite knob = AssetDatabase.GetBuiltinExtraResource<Sprite>("UI/Skin/Knob.psd");

            RectTransform controls = CreateRect("MobileControls", root.transform);
            controls.anchorMin = Vector2.zero;
            controls.anchorMax = Vector2.one;
            controls.offsetMin = Vector2.zero;
            controls.offsetMax = Vector2.zero;
            controls.gameObject.AddComponent<MobileControlsVisibility>();

            // Joystick virtual: fondo fijo abajo a la izquierda y palanca que se mueve.
            RectTransform stickBase = CreateRect("StickBase", controls);
            Anchor(stickBase, new Vector2(0, 0), new Vector2(220, 220), 300);
            AddImage(stickBase, knob, new Color(1, 1, 1, 0.25f));

            RectTransform stickHandle = CreateRect("StickHandle", stickBase);
            stickHandle.anchorMin = stickHandle.anchorMax = new Vector2(0.5f, 0.5f);
            stickHandle.sizeDelta = new Vector2(140, 140);
            AddImage(stickHandle, knob, new Color(1, 1, 1, 0.6f));
            OnScreenStick stick = stickHandle.gameObject.AddComponent<OnScreenStick>();
            stick.controlPath = "<Gamepad>/leftStick";
            stick.movementRange = 100;

            // Botón de disparo abajo a la derecha.
            RectTransform fire = CreateRect("FireButton", controls);
            Anchor(fire, new Vector2(1, 0), new Vector2(-220, 220), 220);
            AddImage(fire, knob, new Color(1, 0.4f, 0.4f, 0.6f));
            OnScreenButton button = fire.gameObject.AddComponent<OnScreenButton>();
            button.controlPath = "<Gamepad>/buttonSouth";
        }
        PrefabUtility.SaveAsPrefabAsset(root, UICanvasPrefab);
        PrefabUtility.UnloadPrefabContents(root);
        Debug.Log("[PorteoSetup] MobileControls en UICanvas");
    }

    private static RectTransform CreateRect(string name, Transform parent)
    {
        var go = new GameObject(name, typeof(RectTransform));
        go.layer = LayerMask.NameToLayer("UI");
        var rect = (RectTransform)go.transform;
        rect.SetParent(parent, false);
        return rect;
    }

    private static void Anchor(RectTransform rect, Vector2 anchor, Vector2 position, float size)
    {
        rect.anchorMin = rect.anchorMax = anchor;
        rect.pivot = new Vector2(0.5f, 0.5f);
        rect.anchoredPosition = position;
        rect.sizeDelta = new Vector2(size, size);
    }

    private static void AddImage(RectTransform rect, Sprite sprite, Color color)
    {
        Image image = rect.gameObject.AddComponent<Image>();
        image.sprite = sprite;
        image.color = color;
    }
}
