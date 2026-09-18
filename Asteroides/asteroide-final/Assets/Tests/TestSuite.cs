/*
 * Copyright (c) 2023 Kodeco Inc.
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * Notwithstanding the foregoing, you may not use, copy, modify, merge, publish, 
 * distribute, sublicense, create a derivative work, and/or sell copies of the 
 * Software in any work that is designed, intended, or marketed for pedagogical or 
 * instructional purposes related to programming, coding, application development, 
 * or information technology.  Permission for such use, copying, modification,
 * merger, publication, distribution, sublicensing, creation of derivative works, 
 * or sale is expressly withheld.
 *    
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

public class TestSuite
{
    private Game game;

    [SetUp]
    public void Setup()
    {
        GameObject gameGameObject = Object.Instantiate(Resources.Load<GameObject>("Prefabs/Game"));
        game = gameGameObject.GetComponent<Game>();
    }

    [TearDown]
    public void Teardown()
    {
        Object.Destroy(game.gameObject);
    }

    [UnityTest]
    public IEnumerator AsteroidsMoveDown()
    {
        GameObject asteroid = game.GetSpawner().SpawnAsteroid();
        float initialYPos = asteroid.transform.position.y;
        yield return new WaitForSeconds(0.1f);

        Assert.Less(asteroid.transform.position.y, initialYPos);
    }

    [UnityTest]
    public IEnumerator GameOverOccursOnAsteroidCollision()
    {
        GameObject asteroid = game.GetSpawner().SpawnAsteroid();
        asteroid.transform.position = game.GetShip().transform.position;
        yield return new WaitForSeconds(0.1f);

        Assert.True(game.isGameOver);
    }

    [Test]
    public void NewGameRestartsGame()
    {
        game.isGameOver = true;
        game.NewGame();

        Assert.False(game.isGameOver);
    }

    // Test de integracion (a diferencia de los demas tests de esta suite, que en general
    // verifican un unico efecto observable): Game.GameOver() coordina tres colaboradores
    // reales (Game, Spawner, Ship) y este test verifica que los tres queden consistentes
    // entre si, no solo que "isGameOver" se haya puesto en true. Si alguien borrara por
    // error la linea "spawner.StopSpawning()" dentro de Game.GameOver(), este test fallaria
    // aunque GameOverOccursOnAsteroidCollision siguiera pasando sin problemas.
    [UnityTest]
    public IEnumerator GameOverStopsSpawningAndDisablesShip()
    {
        // Arrange: arrancar el spawn automatico, igual que lo hace NewGame() en una partida real
        game.GetSpawner().BeginSpawning();

        // Act: mismo choque que ya dispara GameOverOccursOnAsteroidCollision
        GameObject asteroid = game.GetSpawner().SpawnAsteroid();
        asteroid.transform.position = game.GetShip().transform.position;
        yield return new WaitForSeconds(0.1f);

        // Assert 1 y 2: los dos efectos directos de GameOver() sobre sus colaboradores
        Assert.True(game.isGameOver, "El Game Over deberia haberse activado");
        Assert.True(game.GetShip().isDead, "La nave deberia quedar destruida (Ship.Explode())");

        // Assert 3, la parte de integracion: el Spawner realmente dejo de generar asteroides
        // nuevos (no alcanza con mirar el flag isGameOver para saber si el juego "se detuvo" de verdad)
        int asteroidCountRightAfterGameOver =
            Object.FindObjectsByType<Asteroid>(FindObjectsSortMode.None).Length;

        yield return new WaitForSeconds(0.5f); // mayor al intervalo de spawn automatico (0.4s)

        int asteroidCountAfterWaiting =
            Object.FindObjectsByType<Asteroid>(FindObjectsSortMode.None).Length;

        Assert.AreEqual(asteroidCountRightAfterGameOver, asteroidCountAfterWaiting,
            "El Spawner no deberia seguir generando asteroides despues del Game Over");
    }

    [UnityTest]
    public IEnumerator LaserMovesUp()
    {
        GameObject lazer = game.GetShip().SpawnLaser();
        float initialYPos = lazer.transform.position.y;
        yield return new WaitForSeconds(0.1f);

        Assert.Greater(lazer.transform.position.y, initialYPos);
    }

    [UnityTest]
    public IEnumerator LaserDestroysAsteroid()
    {
        GameObject asteroid = game.GetSpawner().SpawnAsteroid();
        asteroid.transform.position = Vector3.zero;
        GameObject lazer = game.GetShip().SpawnLaser();
        lazer.transform.position = Vector3.zero;
        yield return new WaitForSeconds(0.1f);

        UnityEngine.Assertions.Assert.IsNull(asteroid);
    }

    [UnityTest]
    public IEnumerator DestroyedAsteroidRaisesScore()
    {
        GameObject asteroid = game.GetSpawner().SpawnAsteroid();
        asteroid.transform.position = Vector3.zero;
        GameObject lazer = game.GetShip().SpawnLaser();
        lazer.transform.position = Vector3.zero;
        yield return new WaitForSeconds(0.1f);

        Assert.AreEqual(game.score, 1);
    }
}
