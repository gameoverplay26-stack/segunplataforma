using System.Linq;
using NUnit.Framework;
using UnityEditor;
using UnityEditor.Build;
using UnityEditor.SceneManagement;
using UnityEngine.EventSystems;
using UnityEngine.InputSystem.OnScreen;
using UnityEngine.InputSystem.UI;

// Configuración del porteo (no gameplay): settings y escenas.
public class MobileConfigTests
{
    [Test]
    public void ActiveInputHandling_IsInputSystemOnly()
    {
        var ps = Unsupported.GetSerializedAssetInterfaceSingleton("PlayerSettings");
        int handler = new SerializedObject(ps).FindProperty("activeInputHandler").intValue;
        Assert.AreEqual(1, handler, "0 = Input Manager, 1 = Input System, 2 = Both");
    }

    [Test]
    public void Orientation_IsLandscapeOnly()
    {
        Assert.IsFalse(PlayerSettings.allowedAutorotateToPortrait);
        Assert.IsFalse(PlayerSettings.allowedAutorotateToPortraitUpsideDown);
        Assert.IsTrue(PlayerSettings.allowedAutorotateToLandscapeLeft || PlayerSettings.allowedAutorotateToLandscapeRight);
    }

    [Test]
    public void AndroidApplicationIdentifier_IsValid()
    {
        string id = PlayerSettings.GetApplicationIdentifier(NamedBuildTarget.Android);
        StringAssert.IsMatch(@"^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z][a-zA-Z0-9_]*)+$", id);
    }

    [TestCase("Assets/Scenes/Menu.unity")]
    [TestCase("Assets/Scenes/Level.unity")]
    public void Scenes_UseInputSystemUIModule(string path)
    {
        var scene = EditorSceneManager.OpenScene(path, OpenSceneMode.Single);
        var systems = scene.GetRootGameObjects().SelectMany(r => r.GetComponentsInChildren<EventSystem>(true)).ToArray();
        Assert.IsNotEmpty(systems);
        foreach (var es in systems)
        {
            Assert.IsNull(es.GetComponent<StandaloneInputModule>());
            Assert.IsNotNull(es.GetComponent<InputSystemUIInputModule>());
        }
    }

    [Test]
    public void Level_HasThreeOnScreenButtons_AndWiredAdapter()
    {
        var scene = EditorSceneManager.OpenScene("Assets/Scenes/Level.unity", OpenSceneMode.Single);
        var roots = scene.GetRootGameObjects();
        var paths = roots.SelectMany(r => r.GetComponentsInChildren<OnScreenButton>(true))
                         .Select(b => b.controlPath).OrderBy(p => p).ToArray();
        CollectionAssert.AreEqual(new[] { "<Gamepad>/buttonSouth", "<Gamepad>/dpad/left", "<Gamepad>/dpad/right" }, paths);

        var adapter = roots.SelectMany(r => r.GetComponentsInChildren<PlayerInputAdapter>(true)).Single();
        Assert.IsNotNull(adapter.player);
    }
}
