using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.TestTools;

// Integration: dispositivo simulado (InputTestFixture) -> adaptador -> jugador.
// Cubre teclado y gamepad. El camino táctil está en OnScreenControlsTests.
// Cada test termina con LevelScene.Unload() antes de que el fixture restaure el Input System.
public class InputAdapterTests : InputTestFixture
{
    PlayerController player => LevelScene.Player;
    Rigidbody2D rb => player.GetComponent<Rigidbody2D>();

    [UnityTest]
    public IEnumerator KeyboardRightArrow_MovesPlayerRight()
    {
        yield return LevelScene.Load();
        var keyboard = InputSystem.AddDevice<Keyboard>();
        float x0 = player.transform.position.x;
        Press(keyboard.rightArrowKey);
        yield return new WaitForSeconds(0.3f);
        float x1 = player.transform.position.x;
        Release(keyboard.rightArrowKey);
        yield return LevelScene.Unload();
        Assert.Greater(x1, x0 + 0.5f);
    }

    [UnityTest]
    public IEnumerator GamepadSouth_Jumps()
    {
        yield return LevelScene.Load();
        var gamepad = InputSystem.AddDevice<Gamepad>();
        Press(gamepad.buttonSouth);
        yield return null;
        yield return new WaitForFixedUpdate();
        float vy = rb.linearVelocity.y;
        yield return LevelScene.Unload();
        Assert.Greater(vy, 1f);
    }
}
