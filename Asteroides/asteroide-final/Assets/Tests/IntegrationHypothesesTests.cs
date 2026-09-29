using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

// Casos INT-AST-13, 14 y 15 de la clase "Testing de integración II"
// (docs/clase-integracion-2). Verifican hipótesis hechas leyendo el código:
// el resultado esperado describe la intención de diseño, no el comportamiento actual.
public class IntegrationHypothesesTests
{
    private Game game;

    [SetUp]
    public void Setup()
    {
        GameObject gameGameObject = Object.Instantiate(Resources.Load<GameObject>("Prefabs/Game"));
        game = gameGameObject.GetComponent<Game>();
    }

    [UnityTearDown]
    public IEnumerator Teardown()
    {
        Object.Destroy(game.gameObject);
        foreach (Asteroid a in Object.FindObjectsByType<Asteroid>(FindObjectsSortMode.None))
        {
            Object.Destroy(a.gameObject);
        }
        foreach (Laser l in Object.FindObjectsByType<Laser>(FindObjectsSortMode.None))
        {
            Object.Destroy(l.gameObject);
        }
        yield return null;
    }

    // INT-AST-13: dos láseres impactan el mismo asteroide en el mismo paso de física.
    [UnityTest]
    public IEnumerator TwoLasersHitSameAsteroid_ScoreIncreasesOnce()
    {
        yield return null; // Start() asigna Game.instance

        GameObject asteroid = game.GetSpawner().SpawnAsteroid();
        asteroid.transform.position = Vector3.zero;
        GameObject laser1 = game.GetShip().SpawnLaser();
        laser1.transform.position = Vector3.zero;
        GameObject laser2 = game.GetShip().SpawnLaser();
        laser2.transform.position = Vector3.zero;

        yield return new WaitForFixedUpdate();
        yield return new WaitForFixedUpdate();
        yield return null;

        Debug.Log($"[INT-AST-13] score después del doble impacto: {game.score}");
        Assert.IsTrue(asteroid == null, "El asteroide debería destruirse");
        Assert.AreEqual(1, game.score, "Un asteroide destruido debería sumar un solo punto");
    }

    // INT-AST-14: NewGame elimina los asteroides que quedaron de la partida anterior.
    [UnityTest]
    public IEnumerator NewGame_RemovesLeftoverAsteroids()
    {
        yield return null; // Start() asigna Game.instance

        game.NewGame();
        GameObject leftover = game.GetSpawner().SpawnAsteroid();
        leftover.transform.position = new Vector3(6f, 3f, leftover.transform.position.z);
        Game.GameOver();
        yield return null;

        game.NewGame(); // el jugador reinicia
        yield return null;

        Assert.IsTrue(leftover == null, "NewGame debería eliminar los asteroides previos");
    }

    // INT-AST-15 (línea de base): cuántos asteroides genera una partida normal en 2,1 s.
    [UnityTest]
    public IEnumerator SingleNewGame_SpawnCountBaseline()
    {
        yield return null;

        game.NewGame();
        MoveShipOutOfTheWay();
        yield return new WaitForSeconds(2.1f);

        int count = Object.FindObjectsByType<Asteroid>(FindObjectsSortMode.None).Length;
        Debug.Log($"[INT-AST-15] Una llamada a NewGame: {count} asteroides en 2,1 s (isGameOver={game.isGameOver})");
        Assert.Greater(count, 0, "El spawner debería generar asteroides");
    }

    // INT-AST-15: llamar NewGame dos veces seguidas no debería duplicar la tasa de aparición.
    [UnityTest]
    public IEnumerator DoubleNewGame_DoesNotChangeSpawnRate()
    {
        yield return null;

        game.NewGame();
        game.NewGame();
        MoveShipOutOfTheWay();
        yield return new WaitForSeconds(2.1f);

        int count = Object.FindObjectsByType<Asteroid>(FindObjectsSortMode.None).Length;
        Debug.Log($"[INT-AST-15] Dos llamadas a NewGame: {count} asteroides en 2,1 s (isGameOver={game.isGameOver})");
        Assert.LessOrEqual(count, 6, "Con un solo spawner se esperan ~5 asteroides en 2,1 s (uno cada 0,4 s)");
    }

    // Aleja la nave de la zona de caída: un Game Over detendría el spawner y alteraría el conteo.
    private void MoveShipOutOfTheWay()
    {
        game.GetShip().transform.position = new Vector3(1000f, 1000f, 0f);
    }
}
