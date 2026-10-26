using NUnit.Framework;
using UnityEngine;
using UnityEngine.InputSystem;

// Unit tests de la capa de consola (versión Xbox): reglas puras y estado de pausa, sin escena.
public class ConsoleRulesTests
{
    [Test]
    public void QuitMethod_IsDetected()
    {
        Assert.IsTrue(ConsoleRules.IsQuitMethod("Quit"));
        Assert.IsFalse(ConsoleRules.IsQuitMethod("Menu"));
        Assert.IsFalse(ConsoleRules.IsQuitMethod(""));
    }

    [TestCase(true, InputDeviceChange.Removed, true)]
    [TestCase(true, InputDeviceChange.Disconnected, true)]
    [TestCase(true, InputDeviceChange.Added, false)]
    [TestCase(true, InputDeviceChange.Reconnected, false)]
    [TestCase(false, InputDeviceChange.Removed, false)]
    public void DeviceChange_PausesOnlyWhenAPhysicalGamepadIsLost(bool isPhysicalGamepad, InputDeviceChange change, bool expected)
    {
        Assert.AreEqual(expected, ConsoleRules.ShouldPauseOnDeviceChange(isPhysicalGamepad, change));
    }

    [Test]
    public void ScaleWithScreenSize_MatchesReferenceAndDoubles()
    {
        var reference = new Vector2(1920, 1080);
        Assert.AreEqual(1f, ConsoleRules.ScaleWithScreenSize(new Vector2(1920, 1080), reference, 0.5f), 1e-4f);
        Assert.AreEqual(2f, ConsoleRules.ScaleWithScreenSize(new Vector2(3840, 2160), reference, 0f), 1e-4f);
        Assert.AreEqual(2f, ConsoleRules.ScaleWithScreenSize(new Vector2(3840, 2160), reference, 1f), 1e-4f);
    }

    [Test]
    public void MinFontSize_Reaches26pxAt1080()
    {
        Assert.AreEqual(26, ConsoleRules.MinFontSize(1f, 1080f));
        Assert.AreEqual(26, ConsoleRules.MinFontSize(2f, 2160f), "4K con escala 2 equivale a 1080p");
        Assert.AreEqual(52, ConsoleRules.MinFontSize(0.5f, 1080f), "Un canvas a media escala necesita el doble");
        int size = ConsoleRules.MinFontSize(0.7f, 1080f);
        Assert.GreaterOrEqual(ConsoleRules.PxAt1080(size, 0.7f, 1080f), ConsoleRules.MinBodyTextPxAt1080);
        Assert.Less(ConsoleRules.PxAt1080(size - 1, 0.7f, 1080f), ConsoleRules.MinBodyTextPxAt1080);
    }

    [Test]
    public void Menu_PausesOnlyDuringGameplay_AndResumes()
    {
        var pause = new PauseState();
        Assert.IsFalse(pause.MenuPressed(gameplayActive: false), "En un menú, Menu no pausa");
        Assert.IsFalse(pause.IsPaused);

        Assert.IsTrue(pause.MenuPressed(gameplayActive: true));
        Assert.AreEqual(PauseReason.MenuButton, pause.Reason);

        Assert.IsTrue(pause.MenuPressed(gameplayActive: true));
        Assert.IsFalse(pause.IsPaused);
    }

    [Test]
    public void ControllerLost_PausesAndReplacesTheReason_OnlyMenuResumes()
    {
        var pause = new PauseState();
        Assert.IsFalse(pause.Interrupt(PauseReason.ControllerLost, gameplayActive: false), "Fuera de la partida no se pausa");

        Assert.IsTrue(pause.Interrupt(PauseReason.FocusLost, gameplayActive: true));
        Assert.IsTrue(pause.Interrupt(PauseReason.ControllerLost, gameplayActive: true), "El aviso del control tiene prioridad");
        Assert.IsFalse(pause.Interrupt(PauseReason.FocusLost, gameplayActive: true));
        Assert.AreEqual(PauseReason.ControllerLost, pause.Reason);

        Assert.IsTrue(pause.MenuPressed(gameplayActive: true));
        Assert.IsFalse(pause.IsPaused);
    }
}
