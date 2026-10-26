using System.Collections.Generic;
using System.Linq;
using NUnit.Framework;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.Tilemaps;

// Configuración del nivel 2: está en el build, es más difícil que el nivel 1 y sus huecos
// no superan lo que alcanza un doble salto (≈ 11 unidades con los valores del jugador).
public class Level2LayoutTests
{
    [Test]
    public void BuildSettings_HaveMenuLevelAndLevel2()
    {
        CollectionAssert.AreEqual(
            new[] { "Assets/Scenes/Menu.unity", "Assets/Scenes/Level.unity", "Assets/Scenes/Level2.unity" },
            EditorBuildSettings.scenes.Select(s => s.path).ToArray());
    }

    static List<int> Gaps(string scenePath)
    {
        var scene = EditorSceneManager.OpenScene(scenePath, OpenSceneMode.Single);
        var tm = scene.GetRootGameObjects().SelectMany(r => r.GetComponentsInChildren<Tilemap>(true)).First(t => t.name == "Tilemap");
        var gaps = new List<int>();
        int run = 0;
        for (int x = -21; x <= 80; x++)   // de la pared izquierda a la salida
        {
            if (tm.HasTile(new Vector3Int(x, -8, 0))) { if (run > 0) gaps.Add(run); run = 0; }
            else run++;
        }
        return gaps;
    }

    [Test]
    public void Level2_HasMoreAndWiderPitsThanLevel1_ButJumpable()
    {
        var g1 = Gaps("Assets/Scenes/Level.unity");
        var g2 = Gaps("Assets/Scenes/Level2.unity");
        Assert.Greater(g2.Count, g1.Count, $"Nivel 1: {string.Join(",", g1)} · Nivel 2: {string.Join(",", g2)}");
        Assert.Greater(g2.Max(), g1.Max());
        Assert.LessOrEqual(g2.Max(), 9, "Un hueco de más de 9 celdas no se puede cruzar con doble salto");
    }

    [Test]
    public void Level2_HasThreePatrollingEnemiesTaggedKillzone()
    {
        var scene = EditorSceneManager.OpenScene("Assets/Scenes/Level2.unity", OpenSceneMode.Single);
        var enemies = scene.GetRootGameObjects().SelectMany(r => r.GetComponentsInChildren<PatrolEnemy>(true)).ToArray();
        Assert.AreEqual(3, enemies.Length);
        foreach (var e in enemies)
        {
            Assert.AreEqual("killzone", e.tag);
            Assert.Less(e.minX, e.maxX);
        }
    }

    [TestCase("Assets/Scenes/Level.unity")]
    [TestCase("Assets/Scenes/Level2.unity")]
    public void Levels_HaveAudioWithClips_AndLivesHud(string path)
    {
        var scene = EditorSceneManager.OpenScene(path, OpenSceneMode.Single);
        var roots = scene.GetRootGameObjects();
        var sfx = roots.SelectMany(r => r.GetComponentsInChildren<Sfx>(true)).Single();
        Assert.IsNotNull(sfx.coin);
        Assert.IsNotNull(sfx.jump);
        Assert.IsNotNull(sfx.death);
        Assert.IsNotNull(roots.SelectMany(r => r.GetComponentsInChildren<LivesHUD>(true)).SingleOrDefault());
    }
}
