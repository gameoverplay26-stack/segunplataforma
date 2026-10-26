using System.Linq;
using TMPro;
using UnityEditor;
using UnityEditor.Build;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.InputSystem.OnScreen;
using UnityEngine.InputSystem.UI;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

// Setup reproducible e idempotente del porteo a móvil (v2).
// Batchmode: Unity.exe -batchmode -projectPath <v2> -executeMethod PorteoSetup.Apply -quit -logFile <log>
public static class PorteoSetup
{
    const string LevelPath = "Assets/Scenes/Level.unity";
    const string MenuPath = "Assets/Scenes/Menu.unity";

    [MenuItem("Porteo/Aplicar setup móvil")]
    public static void Apply()
    {
        UpgradeTmpEssentials();
        SetupLevel();
        SetupMenu();
        SetupPlayerSettings();
        AssetDatabase.SaveAssets();
        Debug.Log("[PorteoSetup] OK");
    }

    // El "TMP Settings" del proyecto viene del TMP de Unity 2022 (sin assetVersion).
    // Unity 6 abre el importador en cada Play hasta que se importan los recursos nuevos.
    static void UpgradeTmpEssentials()
    {
        const string settings = "Assets/TextMesh Pro/Resources/TMP Settings.asset";
        if (System.IO.File.ReadAllText(settings).Contains("assetVersion: 2")) return;

        var ugui = UnityEditor.PackageManager.PackageInfo.FindForAssetPath("Packages/com.unity.ugui");
        string package = System.IO.Path.Combine(ugui.resolvedPath, "Package Resources", "TMP Essential Resources.unitypackage");
        AssetDatabase.ImportPackage(package, false);
        AssetDatabase.Refresh();

        // Igual que el importador de TMP: marcar la versión de los recursos.
        var asset = AssetDatabase.LoadAssetAtPath<TMP_Settings>(settings);
        var so = new SerializedObject(asset);
        so.FindProperty("assetVersion").stringValue = "2";
        so.ApplyModifiedPropertiesWithoutUndo();
        EditorUtility.SetDirty(asset);
        AssetDatabase.SaveAssets();
        Debug.Log("[PorteoSetup] TMP Essential Resources importados (assetVersion 2)");
    }

    static void SetupLevel()
    {
        Scene scene = EditorSceneManager.OpenScene(LevelPath, OpenSceneMode.Single);

        GameObject player = Find(scene, "Player");
        var controller = player.GetComponent<PlayerController>();
        var adapter = player.GetComponent<PlayerInputAdapter>() ?? player.AddComponent<PlayerInputAdapter>();
        adapter.player = controller;

        GameObject mobile = Find(scene, "MobileControls");
        var rect = (RectTransform)mobile.transform;
        rect.anchorMin = Vector2.zero;
        rect.anchorMax = Vector2.one;
        rect.offsetMin = Vector2.zero;
        rect.offsetMax = Vector2.zero;
        if (mobile.GetComponent<SafeAreaFitter>() == null) mobile.AddComponent<SafeAreaFitter>();

        for (int i = rect.childCount - 1; i >= 0; i--)
            Object.DestroyImmediate(rect.GetChild(i).gameObject);

        // Botones en pantalla = gamepad virtual. ◀ ▶ usan el D-pad; saltar, el botón Sur.
        // Unidades de referencia del Canvas (1920x1080, match 0.5). Tamaño en dp: a medir (QA).
        CreateButton(rect, "LeftButton", "<", "<Gamepad>/dpad/left", new Vector2(0, 0), new Vector2(170, 170), 220);
        CreateButton(rect, "RightButton", ">", "<Gamepad>/dpad/right", new Vector2(0, 0), new Vector2(430, 170), 220);
        CreateButton(rect, "JumpButton", "SALTAR", "<Gamepad>/buttonSouth", new Vector2(1, 0), new Vector2(-210, 190), 280);

        mobile.SetActive(false); // UIManager lo activa si corresponde a la plataforma

        var ui = Object.FindFirstObjectByType<UIManager>();
        ui.mobileControls = mobile;
        EditorUtility.SetDirty(ui);

        ReplaceInputModule(scene);
        EditorSceneManager.MarkSceneDirty(scene);
        EditorSceneManager.SaveScene(scene);
    }

    static void SetupMenu()
    {
        Scene scene = EditorSceneManager.OpenScene(MenuPath, OpenSceneMode.Single);
        ReplaceInputModule(scene);
        EditorSceneManager.MarkSceneDirty(scene);
        EditorSceneManager.SaveScene(scene);
    }

    static void SetupPlayerSettings()
    {
        PlayerSettings.productName = "2D platformer v2";
        // El identificador Standalone tiene un guion, que Android no acepta.
        PlayerSettings.SetApplicationIdentifier(NamedBuildTarget.Android, "com.DefaultCompany.platformerv2");
        // Solo horizontal (MOB-PLT-06).
        PlayerSettings.defaultInterfaceOrientation = UIOrientation.AutoRotation;
        PlayerSettings.allowedAutorotateToPortrait = false;
        PlayerSettings.allowedAutorotateToPortraitUpsideDown = false;
        PlayerSettings.allowedAutorotateToLandscapeLeft = true;
        PlayerSettings.allowedAutorotateToLandscapeRight = true;
    }

    static void CreateButton(RectTransform parent, string name, string label, string controlPath,
                             Vector2 anchor, Vector2 position, float size)
    {
        var go = new GameObject(name, typeof(RectTransform), typeof(Image), typeof(OnScreenButton));
        go.layer = LayerMask.NameToLayer("UI");
        var rt = (RectTransform)go.transform;
        rt.SetParent(parent, false);
        rt.anchorMin = anchor;
        rt.anchorMax = anchor;
        rt.pivot = new Vector2(0.5f, 0.5f);
        rt.anchoredPosition = position;
        rt.sizeDelta = new Vector2(size, size);

        var image = go.GetComponent<Image>();
        image.sprite = AssetDatabase.GetBuiltinExtraResource<Sprite>("UI/Skin/Knob.psd");
        image.color = new Color(1f, 1f, 1f, 0.35f);

        go.GetComponent<OnScreenButton>().controlPath = controlPath;

        var text = new GameObject("Label", typeof(RectTransform), typeof(TextMeshProUGUI));
        text.layer = go.layer;
        var trt = (RectTransform)text.transform;
        trt.SetParent(rt, false);
        trt.anchorMin = Vector2.zero;
        trt.anchorMax = Vector2.one;
        trt.offsetMin = Vector2.zero;
        trt.offsetMax = Vector2.zero;
        var tmp = text.GetComponent<TextMeshProUGUI>();
        tmp.text = label;
        tmp.alignment = TextAlignmentOptions.Center;
        tmp.fontSize = label.Length > 1 ? 48 : 96;
        tmp.color = new Color(0f, 0f, 0f, 0.75f);
        tmp.raycastTarget = false;
    }

    static void ReplaceInputModule(Scene scene)
    {
        foreach (var es in scene.GetRootGameObjects().SelectMany(r => r.GetComponentsInChildren<EventSystem>(true)))
        {
            var old = es.GetComponent<StandaloneInputModule>();
            if (old != null) Object.DestroyImmediate(old);
            if (es.GetComponent<InputSystemUIInputModule>() == null)
                es.gameObject.AddComponent<InputSystemUIInputModule>();
        }
    }

    static GameObject Find(Scene scene, string name)
    {
        var t = scene.GetRootGameObjects()
            .SelectMany(r => r.GetComponentsInChildren<Transform>(true))
            .FirstOrDefault(x => x.name == name);
        if (t == null) throw new System.Exception($"[PorteoSetup] No se encontró '{name}' en {scene.path}");
        return t.gameObject;
    }
}
