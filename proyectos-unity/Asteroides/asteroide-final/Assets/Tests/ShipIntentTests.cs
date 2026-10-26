using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

// Tests de la capa "intención -> nave": no usan dispositivos de entrada.
public class ShipIntentTests
{
    private Game game;

    [SetUp]
    public void Setup()
    {
        GameObject gameGameObject = Object.Instantiate(Resources.Load<GameObject>("Prefabs/Game"));
        game = gameGameObject.GetComponent<Game>();
        // Aislar la nave del adaptador: sin esto, el adaptador pisaría la
        // intención en cada frame con lo que lean los dispositivos (nada).
        game.GetShip().GetComponent<ShipInputAdapter>().enabled = false;
    }

    [TearDown]
    public void Teardown()
    {
        Object.Destroy(game.gameObject);
    }

    [UnityTest]
    public IEnumerator NegativeIntent_MovesLikeMoveLeft()
    {
        Ship ship = game.GetShip();
        ship.isDead = false;
        float initialX = ship.transform.position.x;

        ship.SetIntent(-1f, false);
        yield return new WaitForSeconds(0.2f);
        ship.SetIntent(0f, false);
        float afterIntent = ship.transform.position.x;

        ship.transform.position = new Vector3(initialX, ship.transform.position.y, ship.transform.position.z);
        ship.MoveLeft();
        float afterMoveLeft = ship.transform.position.x;

        Assert.AreNotEqual(initialX, afterIntent, "La intención negativa debería mover la nave");
        Assert.AreEqual(Mathf.Sign(afterMoveLeft - initialX), Mathf.Sign(afterIntent - initialX),
            "La intención negativa debería mover la nave en el mismo sentido que MoveLeft()");
    }

    [UnityTest]
    public IEnumerator FireIntent_ShootsLaser()
    {
        Ship ship = game.GetShip();
        ship.isDead = false;

        ship.SetIntent(0f, true);
        yield return null;
        ship.SetIntent(0f, false);

        Assert.IsFalse(ship.canShoot, "Tras disparar, la nave debería esperar el enfriamiento");
    }

    [UnityTest]
    public IEnumerator DeadShip_IgnoresIntent()
    {
        Ship ship = game.GetShip();
        ship.isDead = true;
        Vector3 initial = ship.transform.position;

        ship.SetIntent(1f, true);
        yield return new WaitForSeconds(0.2f);

        Assert.AreEqual(initial, ship.transform.position, "Una nave destruida no debería moverse");
        Assert.IsTrue(ship.canShoot, "Una nave destruida no debería disparar");
    }
}
