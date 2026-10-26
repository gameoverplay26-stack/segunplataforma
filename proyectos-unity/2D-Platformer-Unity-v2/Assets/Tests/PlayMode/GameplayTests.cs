using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.TestTools;

// Integration: sonido, vidas, Game Over y nivel 2 en las escenas reales.
public class GameplayTests
{
    PlayerController player => LevelScene.Player;

    [UnityTearDown]
    public IEnumerator Unload()
    {
        yield return LevelScene.Unload();
    }

    static IEnumerator WaitFor(System.Func<bool> condition, float timeout)
    {
        float t = 0f;
        while (!condition() && t < timeout) { t += Time.deltaTime; yield return null; }
    }

    [UnityTest]
    public IEnumerator Death_LosesOneLife_PlaysSound_AndEmptiesOneHeart()
    {
        yield return LevelScene.Load();
        GameManager.instance.Death();
        yield return null;
        Assert.AreEqual(2, GameSession.Lives);
        Assert.AreEqual(Sfx.Kind.Death, Sfx.LastPlayed);
        Assert.IsTrue(LivesHUD.instance.IsFull(0));
        Assert.IsTrue(LivesHUD.instance.IsFull(1));
        Assert.IsFalse(LivesHUD.instance.IsFull(2));
    }

    [UnityTest]
    public IEnumerator Death_WithLivesLeft_ReloadsSameLevel_KeepingLives()
    {
        yield return LevelScene.Load("Level2");
        GameManager.instance.Death();
        yield return WaitFor(() => GameManager.instance != null && !GameManager.instance.IsDead, 4f);
        Assert.AreEqual("Level2", SceneManager.GetActiveScene().name);
        Assert.AreEqual(2, GameSession.Lives);
        yield return null;
        Assert.IsFalse(LivesHUD.instance.IsFull(2), "Tras recargar, el HUD debe seguir mostrando 2 vidas");
    }

    [UnityTest]
    public IEnumerator LastDeath_ShowsGameOver_InsteadOfReloading()
    {
        yield return LevelScene.Load();
        GameSession.LoseLife();
        GameSession.LoseLife();
        GameManager.instance.Death();
        var panel = GameObject.Find("Canvas").transform.Find("GameOverPanel").gameObject;
        yield return WaitFor(() => panel.activeSelf, 4f);
        Assert.IsTrue(panel.activeSelf);
        Assert.IsTrue(GameSession.IsGameOver);
        Assert.AreEqual("Level", SceneManager.GetActiveScene().name);
    }

    [UnityTest]
    public IEnumerator Coin_PlaysCoinSound()
    {
        yield return LevelScene.Load();
        var coin = GameObject.FindGameObjectWithTag("Coin");
        player.GetComponent<PlayerInputAdapter>().enabled = false;
        player.transform.position = coin.transform.position;
        yield return WaitFor(() => Sfx.LastPlayed == Sfx.Kind.Coin, 1f);
        Assert.AreEqual(Sfx.Kind.Coin, Sfx.LastPlayed);
    }

    [UnityTest]
    public IEnumerator Jump_PlaysJumpSound()
    {
        yield return LevelScene.Load();
        player.GetComponent<PlayerInputAdapter>().enabled = false;
        player.SetIntent(0f, true);
        yield return null;
        Assert.AreEqual(Sfx.Kind.Jump, Sfx.LastPlayed);
    }

    [UnityTest]
    public IEnumerator Level1Complete_OffersNextLevel_Level2Complete_DoesNot()
    {
        yield return LevelScene.Load();
        GameManager.instance.LevelComplete();
        Assert.IsTrue(GameObject.Find("NextButton") != null, "Nivel 1: debe verse 'Next Level'");
        yield return LevelScene.Unload();

        yield return LevelScene.Load("Level2");
        GameManager.instance.LevelComplete();
        Assert.IsTrue(GameObject.Find("NextButton") == null, "Nivel 2 (último): no hay siguiente");
    }

    [UnityTest]
    public IEnumerator Level2_Enemy_KillsPlayerOnContact()
    {
        yield return LevelScene.Load("Level2");
        player.GetComponent<PlayerInputAdapter>().enabled = false;
        var enemy = Object.FindFirstObjectByType<PatrolEnemy>();
        player.transform.position = enemy.transform.position + Vector3.up * 1.6f;
        yield return WaitFor(() => GameManager.instance.IsDead, 2f);
        Assert.IsTrue(GameManager.instance.IsDead);
        Assert.AreEqual(2, GameSession.Lives);
    }
}
