using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.SceneManagement;

// Carga y descarga de la escena Level para los tests de Play Mode.
public static class LevelScene
{
    public static PlayerController Player { get; private set; }

    public static IEnumerator Load(string sceneName = "Level")
    {
        GameSession.NewGame();
        yield return SceneManager.LoadSceneAsync(sceneName);
        Player = Object.FindFirstObjectByType<PlayerController>();

        float t = 0f;
        while (!Player.IsGroundedNow && t < 3f) { t += Time.deltaTime; yield return null; }
        Assert.IsTrue(Player.IsGroundedNow, "El jugador no llegó a estar en el suelo");
    }

    // Deja una escena vacía: así ningún control en pantalla (dispositivo virtual)
    // sobrevive al test siguiente ni al reset de InputTestFixture.
    public static IEnumerator Unload()
    {
        if (UIManager.instance != null) UIManager.instance.DisableMobileControls();
        Scene level = SceneManager.GetActiveScene();
        Scene empty = SceneManager.CreateScene("Empty_" + Time.frameCount);
        SceneManager.SetActiveScene(empty);
        yield return SceneManager.UnloadSceneAsync(level);
    }
}
