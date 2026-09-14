using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;

public static class DemoSceneBuilder
{
    private const string ScenePath = "Assets/_Project/Scenes/PlayModeDemo.unity";

    [MenuItem("Tools/Demo/Build PlayerHealth Demo Scene")]
    public static void BuildHealthDemoScene()
    {
        var scene = EditorSceneManager.OpenScene(ScenePath, OpenSceneMode.Single);

        DestroyIfExists("DemoCanvas");
        DestroyIfExists("PlayerHealthDemo");
        DestroyIfExists("EventSystem");

        new GameObject("EventSystem", typeof(EventSystem), typeof(StandaloneInputModule));

        var canvasGO = new GameObject("DemoCanvas", typeof(Canvas), typeof(CanvasScaler), typeof(GraphicRaycaster));
        var canvas = canvasGO.GetComponent<Canvas>();
        canvas.renderMode = RenderMode.ScreenSpaceOverlay;
        var scaler = canvasGO.GetComponent<CanvasScaler>();
        scaler.uiScaleMode = CanvasScaler.ScaleMode.ScaleWithScreenSize;
        scaler.referenceResolution = new Vector2(1920, 1080);

        var font = Resources.GetBuiltinResource<Font>("LegacyRuntime.ttf");

        var labelGO = new GameObject("HealthLabel", typeof(RectTransform), typeof(Text));
        labelGO.transform.SetParent(canvasGO.transform, false);
        var labelRect = (RectTransform)labelGO.transform;
        labelRect.anchorMin = new Vector2(0.5f, 1f);
        labelRect.anchorMax = new Vector2(0.5f, 1f);
        labelRect.pivot = new Vector2(0.5f, 1f);
        labelRect.anchoredPosition = new Vector2(0, -40);
        labelRect.sizeDelta = new Vector2(400, 60);
        var label = labelGO.GetComponent<Text>();
        label.text = "HP: 100/100";
        label.alignment = TextAnchor.MiddleCenter;
        label.fontSize = 32;
        label.color = Color.white;
        label.font = font;

        var sliderGO = new GameObject("HealthSlider", typeof(RectTransform));
        sliderGO.transform.SetParent(canvasGO.transform, false);
        var sliderRect = (RectTransform)sliderGO.transform;
        sliderRect.anchorMin = new Vector2(0.5f, 1f);
        sliderRect.anchorMax = new Vector2(0.5f, 1f);
        sliderRect.pivot = new Vector2(0.5f, 1f);
        sliderRect.anchoredPosition = new Vector2(0, -110);
        sliderRect.sizeDelta = new Vector2(400, 30);

        var bgGO = new GameObject("Background", typeof(RectTransform), typeof(Image));
        bgGO.transform.SetParent(sliderGO.transform, false);
        var bgRect = (RectTransform)bgGO.transform;
        bgRect.anchorMin = Vector2.zero;
        bgRect.anchorMax = Vector2.one;
        bgRect.offsetMin = Vector2.zero;
        bgRect.offsetMax = Vector2.zero;
        bgGO.GetComponent<Image>().color = new Color(0.2f, 0.2f, 0.2f);

        var fillAreaGO = new GameObject("Fill Area", typeof(RectTransform));
        fillAreaGO.transform.SetParent(sliderGO.transform, false);
        var fillAreaRect = (RectTransform)fillAreaGO.transform;
        fillAreaRect.anchorMin = Vector2.zero;
        fillAreaRect.anchorMax = Vector2.one;
        fillAreaRect.offsetMin = new Vector2(5, 5);
        fillAreaRect.offsetMax = new Vector2(-5, -5);

        var fillGO = new GameObject("Fill", typeof(RectTransform), typeof(Image));
        fillGO.transform.SetParent(fillAreaGO.transform, false);
        var fillRect = (RectTransform)fillGO.transform;
        fillRect.anchorMin = Vector2.zero;
        fillRect.anchorMax = new Vector2(1, 1);
        fillRect.offsetMin = Vector2.zero;
        fillRect.offsetMax = Vector2.zero;
        fillGO.GetComponent<Image>().color = new Color(0.2f, 0.8f, 0.2f);

        var slider = sliderGO.AddComponent<Slider>();
        slider.targetGraphic = bgGO.GetComponent<Image>();
        slider.fillRect = fillRect;
        slider.direction = Slider.Direction.LeftToRight;
        slider.minValue = 0;
        slider.maxValue = 100;
        slider.value = 100;
        slider.interactable = false;

        var controllerGO = new GameObject("PlayerHealthDemo", typeof(PlayerHealthDemo));
        var demo = controllerGO.GetComponent<PlayerHealthDemo>();
        var so = new SerializedObject(demo);
        so.FindProperty("healthSlider").objectReferenceValue = slider;
        so.FindProperty("healthLabel").objectReferenceValue = label;
        so.ApplyModifiedPropertiesWithoutUndo();

        EditorSceneManager.MarkSceneDirty(scene);
        var saved = EditorSceneManager.SaveScene(scene);

        Debug.Log(saved
            ? "DemoSceneBuilder: PlayerHealth demo scene built and saved successfully."
            : "DemoSceneBuilder: FAILED to save the scene.");
    }

    private static void DestroyIfExists(string name)
    {
        var go = GameObject.Find(name);
        if (go != null)
        {
            Object.DestroyImmediate(go);
        }
    }
}
