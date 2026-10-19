using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.InputSystem.OnScreen;
using UnityEngine.TestTools;

// Integration: botón en pantalla (gamepad virtual) -> adaptador -> jugador.
// Sin InputTestFixture: OnScreenButton crea su propio dispositivo virtual, y
// mezclarlo con el fixture deja punteros de estado inválidos al desactivarlo.
public class OnScreenControlsTests
{
    PlayerController player => LevelScene.Player;
    Rigidbody2D rb => player.GetComponent<Rigidbody2D>();

    [UnityTest]
    public IEnumerator OnScreenRightButton_MovesWhileHeld_StopsOnRelease()
    {
        yield return LevelScene.Load();
        UIManager.instance.EnableMobileControls();
        var right = GameObject.Find("RightButton").GetComponent<OnScreenButton>();
        var pointer = new PointerEventData(EventSystem.current);

        float x0 = player.transform.position.x;
        right.OnPointerDown(pointer);
        yield return new WaitForSeconds(0.3f);
        float x1 = player.transform.position.x;

        right.OnPointerUp(pointer);
        yield return null;
        yield return new WaitForFixedUpdate();
        yield return new WaitForFixedUpdate();
        float vxAfterRelease = rb.linearVelocity.x;

        yield return LevelScene.Unload();
        Assert.Greater(x1, x0 + 0.5f);
        Assert.AreEqual(0f, vxAfterRelease, 0.001f, "Al soltar, el jugador debe detenerse");
    }

    [UnityTest]
    public IEnumerator OnScreenJumpButton_Jumps()
    {
        yield return LevelScene.Load();
        UIManager.instance.EnableMobileControls();
        var jump = GameObject.Find("JumpButton").GetComponent<OnScreenButton>();
        var pointer = new PointerEventData(EventSystem.current);
        jump.OnPointerDown(pointer);
        yield return null;
        yield return new WaitForFixedUpdate();
        float vy = rb.linearVelocity.y;
        jump.OnPointerUp(pointer);
        yield return LevelScene.Unload();
        Assert.Greater(vy, 1f);
    }
}
