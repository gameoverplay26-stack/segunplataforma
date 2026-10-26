using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.SceneManagement;
using UnityEngine.TestTools;
using UnityEngine.UI;

// Integration: la capa de consola (versión Xbox) sobre las escenas reales (XB-AC-01 a XB-AC-04).
public class ConsoleLayerTests
{
    [UnityTearDown]
    public IEnumerator Unload()
    {
        if (ConsoleLayer.Instance != null && ConsoleLayer.Instance.IsPaused) ConsoleLayer.Instance.Resume();
        yield return LevelScene.Unload();
    }

    static IEnumerator LoadMenu()
    {
        yield return SceneManager.LoadSceneAsync("Menu");
        yield return null;
        yield return null;
    }

    [UnityTest]
    public IEnumerator Menu_HasFocusOnAButton_WithoutMouse()
    {
        yield return LoadMenu();
        Assert.IsNotNull(ConsoleLayer.Instance, "La capa de consola debe instalarse sola");
        GameObject selected = EventSystem.current.currentSelectedGameObject;
        Assert.IsNotNull(selected, "Con mando, algún botón tiene que tener el foco al cargar el menú");
        Assert.IsNotNull(selected.GetComponent<Selectable>());
    }

    [UnityTest]
    public IEnumerator Menu_HidesQuitButtons()
    {
        yield return LoadMenu();
        foreach (Button button in Object.FindObjectsByType<Button>(FindObjectsSortMode.None))
            Assert.IsFalse(ConsoleLayer.IsQuitButton(button), $"El botón {button.name} llama a Quit y sigue visible");
    }

    [UnityTest]
    public IEnumerator Menu_ButtonDoesNotPause()
    {
        yield return LoadMenu();
        ConsoleLayer.Instance.MenuPressed();
        Assert.IsFalse(ConsoleLayer.Instance.IsPaused, "En el menú principal no hay partida que pausar");
    }

    [UnityTest]
    public IEnumerator Level_MenuButton_PausesTimeAndInput_ThenResumes()
    {
        yield return LevelScene.Load();
        var adapter = Object.FindFirstObjectByType<PlayerInputAdapter>();

        ConsoleLayer.Instance.MenuPressed();
        Assert.IsTrue(ConsoleLayer.Instance.IsPaused);
        Assert.AreEqual(0f, Time.timeScale);
        Assert.IsFalse(adapter.enabled, "En pausa el adaptador no debe leer el mando");

        ConsoleLayer.Instance.MenuPressed();
        Assert.IsFalse(ConsoleLayer.Instance.IsPaused);
        Assert.AreEqual(1f, Time.timeScale);
        Assert.IsTrue(adapter.enabled);
    }

    [UnityTest]
    public IEnumerator Level_ControllerLost_PausesWithItsMessage()
    {
        yield return LevelScene.Load();
        ConsoleLayer.Instance.Interrupt(PauseReason.ControllerLost);
        Assert.IsTrue(ConsoleLayer.Instance.IsPaused);
        Assert.AreEqual(PauseReason.ControllerLost, ConsoleLayer.Instance.Reason);
        Assert.AreEqual(0f, Time.timeScale);
    }

    [UnityTest]
    public IEnumerator Scenes_TextIsAtLeast26pxAt1080()
    {
        yield return LoadMenu();
        Assert.GreaterOrEqual(ConsoleText.SmallestVisiblePxAt1080(), ConsoleRules.MinBodyTextPxAt1080 - 0.01f, "Menu");
        yield return LevelScene.Load();
        Assert.GreaterOrEqual(ConsoleText.SmallestVisiblePxAt1080(), ConsoleRules.MinBodyTextPxAt1080 - 0.01f, "Level");
    }
}
