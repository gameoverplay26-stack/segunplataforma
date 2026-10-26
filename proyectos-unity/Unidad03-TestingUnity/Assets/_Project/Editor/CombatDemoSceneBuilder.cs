using UnityEditor;
using UnityEditor.Events;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;

// Fase 1 (jugable) del demo de combate que ilustra CombatSystem (docs/unidad03/02-caso-practico-testing-videojuego.md,
// Seccion F). El objetivo es ver en pantalla lo mismo que describe el caso practico: un ataque que aplica dano a
// traves de PlayerHealth, con cooldown, y con el bug del "critico" (CRYPT-201) disponible como toggle de Inspector
// en el CombatSystem del Player, para poder mostrar la regresion en vivo sin editar codigo.
public static class CombatDemoSceneBuilder
{
    private const string ScenePath = "Assets/_Project/Scenes/CombatDemo.unity";

    [MenuItem("Tools/Demo/Build Combat Demo Scene")]
    public static void BuildCombatDemoScene()
    {
        var scene = EditorSceneManager.NewScene(NewSceneSetup.EmptyScene, NewSceneMode.Single);

        BuildLightingAndCamera();
        BuildGround();
        var enemy = BuildEnemy();
        var player = BuildPlayer(enemy);
        BuildUI(player, enemy);

        EditorSceneManager.MarkSceneDirty(scene);
        var saved = EditorSceneManager.SaveScene(scene, ScenePath);

        Debug.Log(saved
            ? "CombatDemoSceneBuilder: Combat demo scene built and saved successfully."
            : "CombatDemoSceneBuilder: FAILED to save the scene.");
    }

    private static void BuildLightingAndCamera()
    {
        var lightGO = new GameObject("Directional Light", typeof(Light));
        var light = lightGO.GetComponent<Light>();
        light.type = LightType.Directional;
        lightGO.transform.rotation = Quaternion.Euler(50f, -30f, 0f);

        var cameraGO = new GameObject("Main Camera", typeof(Camera));
        cameraGO.tag = "MainCamera";
        cameraGO.transform.position = new Vector3(0f, 14f, 0f);
        cameraGO.transform.rotation = Quaternion.Euler(90f, 0f, 0f);
        var camera = cameraGO.GetComponent<Camera>();
        camera.orthographic = true;
        camera.orthographicSize = 7f;
    }

    private static void BuildGround()
    {
        var ground = GameObject.CreatePrimitive(PrimitiveType.Plane);
        ground.name = "Ground";
        ground.transform.localScale = new Vector3(2f, 1f, 1.2f);
        ground.GetComponent<Renderer>().material.color = new Color(0.55f, 0.55f, 0.55f);
    }

    private static GameObject BuildPlayer(EnemyTarget enemy)
    {
        var playerGO = GameObject.CreatePrimitive(PrimitiveType.Capsule);
        playerGO.name = "Player";
        playerGO.transform.position = new Vector3(-4f, 1f, 0f);
        playerGO.GetComponent<Renderer>().material.color = new Color(0.2f, 0.45f, 0.9f);

        playerGO.AddComponent<CombatSystem>();
        var controller = playerGO.AddComponent<PlayerController>();

        var so = new SerializedObject(controller);
        so.FindProperty("enemy").objectReferenceValue = enemy;
        so.ApplyModifiedPropertiesWithoutUndo();

        return playerGO;
    }

    private static EnemyTarget BuildEnemy()
    {
        var enemyGO = GameObject.CreatePrimitive(PrimitiveType.Cube);
        enemyGO.name = "Enemy";
        enemyGO.transform.position = new Vector3(4f, 0.5f, 0f);
        return enemyGO.AddComponent<EnemyTarget>();
    }

    private static void BuildUI(GameObject player, EnemyTarget enemy)
    {
        new GameObject("EventSystem", typeof(EventSystem), typeof(StandaloneInputModule));

        var canvasGO = new GameObject("DemoCanvas", typeof(Canvas), typeof(CanvasScaler), typeof(GraphicRaycaster));
        var canvas = canvasGO.GetComponent<Canvas>();
        canvas.renderMode = RenderMode.ScreenSpaceOverlay;
        var scaler = canvasGO.GetComponent<CanvasScaler>();
        scaler.uiScaleMode = CanvasScaler.ScaleMode.ScaleWithScreenSize;
        scaler.referenceResolution = new Vector2(1920, 1080);

        var font = Resources.GetBuiltinResource<Font>("LegacyRuntime.ttf");

        // Enemy health bar (arriba, centro)
        var enemyLabel = CreateText(canvasGO.transform, "EnemyLabel", "Enemigo: 100/100",
            new Vector2(0f, -40f), new Vector2(400f, 40f), 26, Color.white, font);
        var enemySlider = CreateSlider(canvasGO.transform, "EnemyHealthSlider",
            new Vector2(0f, -85f), new Vector2(400f, 24f), new Color(0.75f, 0.2f, 0.2f));

        // Cooldown de ataque (arriba a la izquierda)
        CreateText(canvasGO.transform, "CooldownCaption", "Cooldown de ataque",
            new Vector2(20f, -40f), new Vector2(220f, 30f), 16, new Color(1f, 1f, 1f, 0.7f), font, TextAnchor.MiddleLeft, new Vector2(0f, 1f));
        var cooldownSlider = CreateSlider(canvasGO.transform, "CooldownSlider",
            new Vector2(20f, -70f), new Vector2(220f, 16f), new Color(0.9f, 0.7f, 0.2f), new Vector2(0f, 1f));

        // Boton de reset del enemigo
        var resetButton = CreateButton(canvasGO.transform, "ResetEnemyButton", "Reset enemigo (R)",
            new Vector2(0f, -130f), new Color(0.25f, 0.25f, 0.25f), font);
        UnityEventTools.AddVoidPersistentListener(resetButton.onClick, enemy.ResetEnemy);

        // Instrucciones (abajo)
        CreateText(canvasGO.transform, "Instructions",
            "WASD / Flechas = Mover  |  ESPACIO = Atacar si estas cerca del enemigo  |  R = Reset",
            new Vector2(0f, 40f), new Vector2(900f, 40f), 20, new Color(1f, 1f, 1f, 0.7f), font,
            TextAnchor.MiddleCenter, new Vector2(0.5f, 0f));

        var enemySo = new SerializedObject(enemy);
        enemySo.FindProperty("healthSlider").objectReferenceValue = enemySlider;
        enemySo.FindProperty("healthLabel").objectReferenceValue = enemyLabel;
        enemySo.FindProperty("bodyRenderer").objectReferenceValue = enemy.GetComponent<Renderer>();
        enemySo.ApplyModifiedPropertiesWithoutUndo();

        var playerSo = new SerializedObject(player.GetComponent<PlayerController>());
        playerSo.FindProperty("cooldownSlider").objectReferenceValue = cooldownSlider;
        playerSo.ApplyModifiedPropertiesWithoutUndo();
    }

    private static Text CreateText(Transform parent, string name, string content, Vector2 anchoredPosition,
        Vector2 size, int fontSize, Color color, Font font, TextAnchor alignment = TextAnchor.MiddleCenter, Vector2? anchor = null)
    {
        var go = new GameObject(name, typeof(RectTransform), typeof(Text));
        go.transform.SetParent(parent, false);
        var rect = (RectTransform)go.transform;
        var anchorPoint = anchor ?? new Vector2(0.5f, 1f);
        rect.anchorMin = anchorPoint;
        rect.anchorMax = anchorPoint;
        rect.pivot = anchorPoint;
        rect.anchoredPosition = anchoredPosition;
        rect.sizeDelta = size;

        var text = go.GetComponent<Text>();
        text.text = content;
        text.alignment = alignment;
        text.fontSize = fontSize;
        text.color = color;
        text.font = font;
        return text;
    }

    private static Slider CreateSlider(Transform parent, string name, Vector2 anchoredPosition, Vector2 size,
        Color fillColor, Vector2? anchor = null)
    {
        var anchorPoint = anchor ?? new Vector2(0.5f, 1f);

        var sliderGO = new GameObject(name, typeof(RectTransform));
        sliderGO.transform.SetParent(parent, false);
        var sliderRect = (RectTransform)sliderGO.transform;
        sliderRect.anchorMin = anchorPoint;
        sliderRect.anchorMax = anchorPoint;
        sliderRect.pivot = anchorPoint;
        sliderRect.anchoredPosition = anchoredPosition;
        sliderRect.sizeDelta = size;

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
        fillAreaRect.offsetMin = new Vector2(4f, 4f);
        fillAreaRect.offsetMax = new Vector2(-4f, -4f);

        var fillGO = new GameObject("Fill", typeof(RectTransform), typeof(Image));
        fillGO.transform.SetParent(fillAreaGO.transform, false);
        var fillRect = (RectTransform)fillGO.transform;
        fillRect.anchorMin = Vector2.zero;
        fillRect.anchorMax = Vector2.one;
        fillRect.offsetMin = Vector2.zero;
        fillRect.offsetMax = Vector2.zero;
        fillGO.GetComponent<Image>().color = fillColor;

        var slider = sliderGO.AddComponent<Slider>();
        slider.targetGraphic = bgGO.GetComponent<Image>();
        slider.fillRect = fillRect;
        slider.direction = Slider.Direction.LeftToRight;
        slider.minValue = 0;
        slider.maxValue = 1;
        slider.value = 1;
        slider.interactable = false;

        return slider;
    }

    private static Button CreateButton(Transform parent, string name, string label, Vector2 anchoredPosition,
        Color color, Font font)
    {
        var buttonGO = new GameObject(name, typeof(RectTransform), typeof(Image), typeof(Button));
        buttonGO.transform.SetParent(parent, false);
        var rect = (RectTransform)buttonGO.transform;
        rect.anchorMin = new Vector2(0.5f, 1f);
        rect.anchorMax = new Vector2(0.5f, 1f);
        rect.pivot = new Vector2(0.5f, 1f);
        rect.anchoredPosition = anchoredPosition;
        rect.sizeDelta = new Vector2(180f, 36f);

        var image = buttonGO.GetComponent<Image>();
        image.color = color;

        var button = buttonGO.GetComponent<Button>();
        button.targetGraphic = image;

        var textGO = new GameObject("Text", typeof(RectTransform), typeof(Text));
        textGO.transform.SetParent(buttonGO.transform, false);
        var textRect = (RectTransform)textGO.transform;
        textRect.anchorMin = Vector2.zero;
        textRect.anchorMax = Vector2.one;
        textRect.offsetMin = Vector2.zero;
        textRect.offsetMax = Vector2.zero;
        var text = textGO.GetComponent<Text>();
        text.text = label;
        text.alignment = TextAnchor.MiddleCenter;
        text.fontSize = 16;
        text.color = Color.white;
        text.font = font;

        return button;
    }
}
