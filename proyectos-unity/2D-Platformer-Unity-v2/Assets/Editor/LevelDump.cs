using System.Linq;
using System.Text;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.Tilemaps;
using UnityEngine.UI;

// Diagnóstico: vuelca la geometría y la UI de una escena a texto (no modifica nada).
// Batchmode: -executeMethod LevelDump.Run -quit  (escribe Logs/level-dump.txt)
public static class LevelDump
{
    public static void Run()
    {
        var sb = new StringBuilder();
        foreach (string path in new[] { "Assets/Scenes/Level.unity", "Assets/Scenes/Level2.unity" })
        {
            var scene = EditorSceneManager.OpenScene(path, OpenSceneMode.Single);
            sb.AppendLine("=== " + path);
            var all = scene.GetRootGameObjects().SelectMany(r => r.GetComponentsInChildren<Transform>(true)).ToArray();

            foreach (var tm in all.Select(t => t.GetComponent<Tilemap>()).Where(t => t != null))
            {
                tm.CompressBounds();
                var b = tm.cellBounds;
                sb.AppendLine($"Tilemap {tm.name} layer={LayerMask.LayerToName(tm.gameObject.layer)} bounds={b} cell={tm.layoutGrid.cellSize} pos={tm.transform.position}");
                for (int y = b.yMax - 1; y >= b.yMin; y--)
                {
                    sb.Append($"{y,4} ");
                    for (int x = b.xMin; x < b.xMax; x++)
                        sb.Append(tm.HasTile(new Vector3Int(x, y, 0)) ? '#' : '.');
                    sb.AppendLine();
                }
                sb.AppendLine($"     x desde {b.xMin}");
            }

            foreach (var t in all)
            {
                var go = t.gameObject;
                var cols = go.GetComponents<Collider2D>();
                string colInfo = string.Join(";", cols.Select(c => $"{c.GetType().Name}{(c.isTrigger ? "(T)" : "")} b={c.bounds.min:F1}-{c.bounds.max:F1}"));
                string comps = string.Join(",", go.GetComponents<Component>().Where(c => c != null).Select(c => c.GetType().Name)
                    .Where(n => n != "Transform" && n != "RectTransform"));
                string extra = "";
                var btn = go.GetComponent<Button>();
                if (btn != null)
                    for (int i = 0; i < btn.onClick.GetPersistentEventCount(); i++)
                        extra += $" onClick={btn.onClick.GetPersistentTarget(i)?.name}.{btn.onClick.GetPersistentMethodName(i)}";
                var tmp = go.GetComponent<TMPro.TMP_Text>();
                if (tmp != null) extra += $" text=\"{tmp.text}\"";
                var img = go.GetComponent<Image>();
                if (img != null && img.sprite != null) extra += $" sprite={AssetDatabase.GetAssetPath(img.sprite)}:{img.sprite.name}";
                var sr = go.GetComponent<SpriteRenderer>();
                if (sr != null && sr.sprite != null) extra += $" sprite={AssetDatabase.GetAssetPath(sr.sprite)}:{sr.sprite.name}";
                sb.AppendLine($"{Path(t)} active={go.activeSelf} layer={LayerMask.LayerToName(go.layer)} tag={go.tag} pos={t.position:F1} [{comps}] {colInfo}{extra}");
            }
        }
        System.IO.File.WriteAllText("Logs/level-dump.txt", sb.ToString());
        Debug.Log("[LevelDump] OK");
    }

    static string Path(Transform t) => t.parent == null ? t.name : Path(t.parent) + "/" + t.name;
}
