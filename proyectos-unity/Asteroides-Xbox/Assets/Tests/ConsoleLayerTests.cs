using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.InputSystem.UI;
using UnityEngine.SceneManagement;
using UnityEngine.TestTools;
using UnityEngine.UI;

// Integration: la capa de consola (versión Xbox) sobre la escena real Game (XB-AC-01 a XB-AC-04).
public class ConsoleLayerTests
{
    private Game game;

    [UnitySetUp]
    public IEnumerator LoadGame()
    {
        yield return SceneManager.LoadSceneAsync("Game");
        yield return null;
        yield return null;
        game = Object.FindFirstObjectByType<Game>();
    }

    [UnityTearDown]
    public IEnumerator Unload()
    {
        if (ConsoleLayer.Instance != null && ConsoleLayer.Instance.IsPaused) ConsoleLayer.Instance.Resume();
        Scene current = SceneManager.GetActiveScene();
        SceneManager.SetActiveScene(SceneManager.CreateScene("Empty_" + Time.frameCount));
        yield return SceneManager.UnloadSceneAsync(current);
    }

    [UnityTest]
    public IEnumerator Start_UsesInputSystemUIModule_AndFocusesStartButton()
    {
        Assert.IsNotNull(ConsoleLayer.Instance, "La capa de consola debe instalarse sola");
        EventSystem eventSystem = EventSystem.current;
        Assert.IsNull(eventSystem.GetComponent<StandaloneInputModule>(), "El módulo del Input Manager no lee el mando en UWP");
        Assert.IsNotNull(eventSystem.GetComponent<InputSystemUIInputModule>());
        GameObject selected = eventSystem.currentSelectedGameObject;
        Assert.IsNotNull(selected, "Con mando, Start tiene que tener el foco al cargar");
        Assert.IsNotNull(selected.GetComponent<Button>());
        yield return null;
    }

    [UnityTest]
    public IEnumerator StartScreen_MenuButtonDoesNotPause()
    {
        ConsoleLayer.Instance.MenuPressed();
        Assert.IsFalse(ConsoleLayer.Instance.IsPaused, "Con el botón Start a la vista no hay partida que pausar");
        yield return null;
    }

    [UnityTest]
    public IEnumerator Playing_MenuButton_PausesTimeAndInput_ThenResumes()
    {
        game.NewGame();
        yield return null;
        var adapter = game.GetShip().GetComponent<ShipInputAdapter>();

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
    public IEnumerator Playing_ControllerLost_PausesWithItsMessage()
    {
        game.NewGame();
        yield return null;
        ConsoleLayer.Instance.Interrupt(PauseReason.ControllerLost);
        Assert.IsTrue(ConsoleLayer.Instance.IsPaused);
        Assert.AreEqual(PauseReason.ControllerLost, ConsoleLayer.Instance.Reason);
    }

    [UnityTest]
    public IEnumerator Text_IsAtLeast26pxAt1080()
    {
        Assert.GreaterOrEqual(ConsoleText.SmallestVisiblePxAt1080(), ConsoleRules.MinBodyTextPxAt1080 - 0.01f);
        game.NewGame();
        yield return null;
        Assert.GreaterOrEqual(ConsoleText.SmallestVisiblePxAt1080(), ConsoleRules.MinBodyTextPxAt1080 - 0.01f, "Durante la partida (puntaje)");
    }
}
