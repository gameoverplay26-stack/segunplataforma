using System.Collections.Generic;
using System.Linq;
using TMPro;
using UnityEditor;
using UnityEditor.Events;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.Events;
using UnityEngine.SceneManagement;
using UnityEngine.Tilemaps;
using UnityEngine.UI;

// Setup reproducible de sonido, vidas y nivel 2 (v2). Idempotente; correr después de PorteoSetup.
// Batchmode: Unity.exe -batchmode -projectPath <v2> -executeMethod GameplaySetup.Apply -quit -logFile <log>
public static class GameplaySetup
{
    const string LevelPath = "Assets/Scenes/Level.unity";
    const string Level2Path = "Assets/Scenes/Level2.unity";
    const string MenuPath = "Assets/Scenes/Menu.unity";

    // Nivel 2: huecos [desde, hasta] en X (celdas). El de 28-36 (9 celdas) exige doble salto.
    static readonly (int a, int b)[] Pits = { (5, 9), (16, 22), (28, 36), (45, 53), (61, 66) };

    [MenuItem("Porteo/Aplicar sonido, vidas y nivel 2")]
    public static void Apply()
    {
        SetupLevel1();
        CreateLevel2();
        EditorBuildSettings.scenes = new[]
        {
            new EditorBuildSettingsScene(MenuPath, true),
            new EditorBuildSettingsScene(LevelPath, true),
            new EditorBuildSettingsScene(Level2Path, true),
        };
        AssetDatabase.SaveAssets();
        Debug.Log("[GameplaySetup] OK");
    }

    // ---------------------------------------------------------------- nivel 1
    static void SetupLevel1()
    {
        Scene scene = EditorSceneManager.OpenScene(LevelPath, OpenSceneMode.Single);
        var all = All(scene);

        // R-PLT-09 (DEC-LAB-015): el suelo está en la capa "ground"; Default se mantiene por la IceBox.
        var player = Comp<PlayerController>(all);
        player.groundLayer = LayerMask.GetMask("Default", "ground");
        EditorUtility.SetDirty(player);

        SetupAudio(scene, all);
        SetupLives(all);

        var gm = Comp<GameManager>(all);
        var so = new SerializedObject(gm);
        GameObject exitPanel = Find(all, "LevelExitPanel");

        // Game Over: copia del panel de nivel completo, antes de agregarle "Next Level".
        GameObject gameOver = all.FirstOrDefault(t => t.name == "GameOverPanel")?.gameObject;
        if (gameOver == null)
        {
            gameOver = Object.Instantiate(exitPanel, exitPanel.transform.parent);
            gameOver.name = "GameOverPanel";
            gameOver.transform.SetSiblingIndex(exitPanel.transform.GetSiblingIndex() + 1);
            Child(gameOver, "Title").GetComponent<TMP_Text>().text = "GAME OVER";
            Child(gameOver, "LevelCompleteCoins").GetComponent<TMP_Text>().text = "NO LIVES LEFT";
            var retry = Child(gameOver, "QuitButton");
            retry.name = "RetryButton";
            retry.GetComponentInChildren<TMP_Text>().text = "Retry";
            Rewire(retry.GetComponent<Button>(), Comp<Events>(all), "Retry");
            gameOver.SetActive(false);
        }
        so.FindProperty("gameOverPanel").objectReferenceValue = gameOver;

        // "Next Level": copia de MenuButton, arriba de él.
        Transform next = exitPanel.transform.Find("NextButton");
        if (next == null)
        {
            var menu = Child(exitPanel, "MenuButton");
            var go = Object.Instantiate(menu, exitPanel.transform);
            go.name = "NextButton";
            var rt = (RectTransform)go.transform;
            rt.anchoredPosition += new Vector2(0, rt.rect.height * 1.25f);
            go.GetComponentInChildren<TMP_Text>().text = "Next Level";
            Rewire(go.GetComponent<Button>(), Comp<Events>(all), "NextLevel");
            next = go.transform;
        }
        so.FindProperty("nextLevelButton").objectReferenceValue = next.gameObject;
        so.ApplyModifiedPropertiesWithoutUndo();

        EditorSceneManager.MarkSceneDirty(scene);
        EditorSceneManager.SaveScene(scene);
    }

    static void SetupAudio(Scene scene, Transform[] all)
    {
        GameObject audio = all.FirstOrDefault(t => t.name == "Audio")?.gameObject;
        if (audio == null)
        {
            audio = new GameObject("Audio", typeof(AudioSource), typeof(Sfx));
            SceneManager.MoveGameObjectToScene(audio, scene);
        }
        var src = audio.GetComponent<AudioSource>();
        src.playOnAwake = false;
        src.spatialBlend = 0f;
        var sfx = audio.GetComponent<Sfx>();
        sfx.coin = AssetDatabase.LoadAssetAtPath<AudioClip>("Assets/Audio/sfx_moneda.wav");
        sfx.jump = AssetDatabase.LoadAssetAtPath<AudioClip>("Assets/Audio/sfx_salto.wav");
        sfx.death = AssetDatabase.LoadAssetAtPath<AudioClip>("Assets/Audio/sfx_muerte.wav");
        if (sfx.coin == null || sfx.jump == null || sfx.death == null)
            throw new System.Exception("[GameplaySetup] Faltan los .wav: correr Tools/generar_sonidos.py");
        EditorUtility.SetDirty(sfx);
    }

    static void SetupLives(Transform[] all)
    {
        GameObject gameUI = Find(all, "GameUI");
        var hud = gameUI.GetComponent<LivesHUD>() ?? gameUI.AddComponent<LivesHUD>();
        var hearts = gameUI.GetComponentsInChildren<Image>(true)
            .Where(i => i.name.StartsWith("Heart"))
            .OrderBy(i => i.transform.position.x).ToArray();
        var so = new SerializedObject(hud);
        var arr = so.FindProperty("hearts");
        arr.arraySize = hearts.Length;
        for (int i = 0; i < hearts.Length; i++) arr.GetArrayElementAtIndex(i).objectReferenceValue = hearts[i];
        so.FindProperty("fullHeart").objectReferenceValue = AssetDatabase.LoadAssetAtPath<Sprite>("Assets/png/Object/heart.png");
        so.FindProperty("emptyHeart").objectReferenceValue = AssetDatabase.LoadAssetAtPath<Sprite>("Assets/png/Object/heart (1).png");
        so.ApplyModifiedPropertiesWithoutUndo();
    }

    // ---------------------------------------------------------------- nivel 2
    static void CreateLevel2()
    {
        AssetDatabase.DeleteAsset(Level2Path); // se regenera siempre desde el nivel 1
        AssetDatabase.CopyAsset(LevelPath, Level2Path);
        Scene scene = EditorSceneManager.OpenScene(Level2Path, OpenSceneMode.Single);
        var all = All(scene);

        var ground = Find(all, "Tilemap").GetComponent<Tilemap>();
        var back = Find(all, "BackGroundTileMap").GetComponent<Tilemap>();

        // Plantillas tomadas del nivel 1: bordes de un hueco, centro del suelo, plataforma flotante, relleno del hueco.
        var leftEdge = Column(ground, 28);   // borde derecho del suelo (antes de un hueco)
        var rightEdge = Column(ground, 35);  // borde izquierdo del suelo (después de un hueco)
        var center = Column(ground, 40);
        TileBase platL = ground.GetTile(new Vector3Int(43, -1, 0)), platR = ground.GetTile(new Vector3Int(45, -1, 0));
        if (platL == null || platR == null) throw new System.Exception("[GameplaySetup] No está la plataforma flotante de referencia (43-45, -1)");
        var fill = new Dictionary<int, TileBase>();
        for (int y = -12; y <= -9; y++) fill[y] = back.GetTile(new Vector3Int(29, y, 0));

        // 1) Desde x = 3 (donde empezaba el bloque grande del nivel 1): sin plataformas ni bloques; suelo continuo.
        for (int x = 3; x <= 80; x++)
        {
            for (int y = -7; y <= 6; y++) ground.SetTile(new Vector3Int(x, y, 0), null);
            for (int y = -12; y <= -8; y++) ground.SetTile(new Vector3Int(x, y, 0), center[y]);
        }
        back.ClearAllTiles();

        // 2) Huecos con sus bordes y el relleno de fondo.
        foreach (var (a, b) in Pits)
        {
            for (int x = a; x <= b; x++)
            {
                for (int y = -12; y <= -8; y++) ground.SetTile(new Vector3Int(x, y, 0), null);
                for (int y = -12; y <= -9; y++) back.SetTile(new Vector3Int(x, y, 0), fill[y]);
            }
            for (int y = -12; y <= -8; y++)
            {
                ground.SetTile(new Vector3Int(a - 1, y, 0), leftEdge[y]);
                ground.SetTile(new Vector3Int(b + 1, y, 0), rightEdge[y]);
            }
        }

        // 3) Plataforma flotante de 2 celdas en el hueco 45-53.
        ground.SetTile(new Vector3Int(48, -5, 0), platL);
        ground.SetTile(new Vector3Int(49, -5, 0), platR);
        ground.GetComponent<CompositeCollider2D>()?.GenerateGeometry();

        // 4) Monedas que quedaban sobre bloques eliminados.
        MoveCoin(all, "dollar (10)", new Vector2(48.5f, -3f));
        MoveCoin(all, "dollar (11)", new Vector2(49.5f, -3f));
        MoveCoin(all, "dollar (12)", new Vector2(51.5f, -2f));

        // 5) Enemigos que patrullan (etiqueta killzone).
        var playerSr = Find(all, "sr").GetComponent<SpriteRenderer>();
        var parent = new GameObject("Enemies");
        SceneManager.MoveGameObjectToScene(parent, scene);
        AddEnemy(parent, playerSr, "Enemy (1)", 38.5f, 43.5f, 2.5f);
        AddEnemy(parent, playerSr, "Enemy (2)", 55.0f, 59.5f, 3.2f);
        AddEnemy(parent, playerSr, "Enemy (3)", 69.0f, 76.0f, 3.6f);

        var number = all.FirstOrDefault(t => t.name == "Level Number");
        if (number != null) number.GetComponent<TMP_Text>().text = "Level 2";

        EditorSceneManager.MarkSceneDirty(scene);
        EditorSceneManager.SaveScene(scene);
    }

    static void AddEnemy(GameObject parent, SpriteRenderer like, string name, float minX, float maxX, float speed)
    {
        var go = new GameObject(name, typeof(SpriteRenderer), typeof(Rigidbody2D), typeof(BoxCollider2D), typeof(PatrolEnemy));
        go.transform.SetParent(parent.transform);
        go.tag = "killzone";
        var sr = go.GetComponent<SpriteRenderer>();
        sr.sprite = AssetDatabase.LoadAssetAtPath<Sprite>("Assets/png/Object/SnowMan.png");
        sr.sortingLayerID = like.sortingLayerID;
        sr.sortingOrder = like.sortingOrder;
        float scale = 1.4f / sr.sprite.bounds.size.y;
        go.transform.localScale = new Vector3(scale, scale, 1);
        float halfH = sr.sprite.bounds.extents.y * scale;
        go.transform.position = new Vector3((minX + maxX) / 2f, -7f + halfH - sr.sprite.bounds.center.y * scale, 0);
        var box = go.GetComponent<BoxCollider2D>();
        box.size = sr.sprite.bounds.size * 0.85f;
        box.offset = sr.sprite.bounds.center;
        var rb = go.GetComponent<Rigidbody2D>();
        rb.bodyType = RigidbodyType2D.Kinematic;
        var p = go.GetComponent<PatrolEnemy>();
        p.minX = minX;
        p.maxX = maxX;
        p.speed = speed;
    }

    // ---------------------------------------------------------------- utilidades
    static Transform[] All(Scene scene) =>
        scene.GetRootGameObjects().SelectMany(r => r.GetComponentsInChildren<Transform>(true)).ToArray();

    static T Comp<T>(Transform[] all) where T : Component =>
        all.Select(t => t.GetComponent<T>()).First(c => c != null);

    static GameObject Find(Transform[] all, string name)
    {
        var t = all.FirstOrDefault(x => x.name == name);
        if (t == null) throw new System.Exception($"[GameplaySetup] No se encontró '{name}'");
        return t.gameObject;
    }

    static GameObject Child(GameObject parent, string name)
    {
        var t = parent.transform.Find(name);
        if (t == null) throw new System.Exception($"[GameplaySetup] '{parent.name}' no tiene '{name}'");
        return t.gameObject;
    }

    static void Rewire(Button button, Events target, string method)
    {
        while (button.onClick.GetPersistentEventCount() > 0)
            UnityEventTools.RemovePersistentListener(button.onClick, 0);
        var action = (UnityAction)System.Delegate.CreateDelegate(typeof(UnityAction), target, method);
        UnityEventTools.AddPersistentListener(button.onClick, action);
    }

    static Dictionary<int, TileBase> Column(Tilemap tm, int x)
    {
        var col = new Dictionary<int, TileBase>();
        for (int y = -12; y <= -8; y++) col[y] = tm.GetTile(new Vector3Int(x, y, 0));
        return col;
    }

    static void MoveCoin(Transform[] all, string name, Vector2 pos)
    {
        var t = all.FirstOrDefault(x => x.name == name);
        if (t != null) t.position = new Vector3(pos.x, pos.y, t.position.z);
    }
}
