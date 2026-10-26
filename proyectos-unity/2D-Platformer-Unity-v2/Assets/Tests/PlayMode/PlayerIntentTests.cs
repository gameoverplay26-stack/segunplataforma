using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

// Integration: escena Level real, con el adaptador desactivado para que solo
// la intención mueva al jugador. Cualquier Debug.LogError (p. ej. el parámetro
// "isGrounded" faltante) hace fallar el test.
public class PlayerIntentTests
{
    PlayerController player;
    Rigidbody2D rb;

    [UnitySetUp]
    public IEnumerator LoadLevel()
    {
        yield return LevelScene.Load();
        player = LevelScene.Player;
        rb = player.GetComponent<Rigidbody2D>();
        player.GetComponent<PlayerInputAdapter>().enabled = false;
    }

    [UnityTearDown]
    public IEnumerator UnloadLevel()
    {
        yield return LevelScene.Unload();
    }

    [UnityTest]
    public IEnumerator MoveIntentRight_MovesPlayerRightAndFacesRight()
    {
        float x0 = player.transform.position.x;
        player.SetIntent(1f, false);
        yield return new WaitForSeconds(0.3f);
        Assert.Greater(player.transform.position.x, x0 + 0.5f);
        Assert.AreEqual(1f, player.transform.localScale.x);
    }

    [UnityTest]
    public IEnumerator MoveIntentLeft_FacesLeft()
    {
        player.SetIntent(-1f, false);
        yield return new WaitForSeconds(0.1f);
        Assert.AreEqual(-1f, player.transform.localScale.x);
    }

    [UnityTest]
    public IEnumerator ZeroIntent_StopsHorizontalVelocity()
    {
        player.SetIntent(1f, false);
        yield return new WaitForSeconds(0.2f);
        player.SetIntent(0f, false);
        yield return new WaitForFixedUpdate();
        yield return new WaitForFixedUpdate();
        Assert.AreEqual(0f, rb.linearVelocity.x, 0.001f);
    }

    [UnityTest]
    public IEnumerator JumpIntent_WhenGrounded_GivesUpwardVelocity()
    {
        player.SetIntent(0f, true);
        yield return null;
        yield return new WaitForFixedUpdate();
        Assert.Greater(rb.linearVelocity.y, 1f);
    }

    // R-PLT-09: con el jugador lejos del suelo, IsGrounded() debe ser falso
    // (antes el rayo golpeaba el propio CapsuleCollider2D del jugador).
    [UnityTest]
    public IEnumerator GroundRay_InMidAir_IsNotGrounded()
    {
        yield return null;
        player.transform.position += Vector3.up * 20f;
        Physics2D.SyncTransforms();
        Assert.IsFalse(player.IsGrounded());
    }

    [UnityTest]
    public IEnumerator SecondJumpIntent_InAir_DoubleJumpsOnlyOnce()
    {
        player.SetIntent(0f, true);
        yield return null;
        // El raycast de suelo original puede seguir "tocando suelo" al comienzo del ascenso.
        float t = 0f;
        while (player.IsGroundedNow && t < 1f) { t += Time.deltaTime; yield return null; }
        Assert.IsFalse(player.IsGroundedNow, $"Sigue en el suelo: y={player.transform.position.y}, vy={rb.linearVelocity.y}");

        player.SetIntent(0f, true); // doble salto
        yield return null;
        yield return new WaitForFixedUpdate();
        Assert.Greater(rb.linearVelocity.y, 1f);

        yield return new WaitForSeconds(0.1f);
        float before = rb.linearVelocity.y;
        player.SetIntent(0f, true); // tercer pedido: no debe saltar
        yield return null;
        yield return new WaitForFixedUpdate();
        Assert.LessOrEqual(rb.linearVelocity.y, before);
    }
}
