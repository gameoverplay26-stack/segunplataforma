using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.UI;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

// Capa de consola de la versión para Xbox (laboratorio-adaptacion/PORTEO-XBOX.md).
// Se instala sola al arrancar y no edita escenas ni prefabs:
// - módulo de UI del Input System, foco inicial y foco visible en los menús (XB-AC-01, XB-AC-02);
// - pausa con Menu (≡), al desconectarse el control o al perder el foco (XB-AC-04);
// - sin botones Quit (en consola, la app la cierra el sistema);
// - texto de 26 px o más a 1080p (XB-AC-03, XAG 101), ver ConsoleText.
public class ConsoleLayer : MonoBehaviour
{
    public static ConsoleLayer Instance { get; private set; }

    private static readonly Color SelectedColor = new Color(1f, 0.82f, 0.2f);

    private readonly PauseState pause = new PauseState();
    private InputAction menu;
    private GameObject overlay;
    private Text overlayText;

    public bool IsPaused => pause.IsPaused;
    public PauseReason Reason => pause.Reason;

    // Se juega cuando no hay ningún menú ni panel con botones a la vista.
    public bool GameplayActive => FirstUsableSelectable() == null;

    [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.AfterSceneLoad)]
    private static void Install()
    {
        if (Instance != null) return;
        var go = new GameObject("ConsoleLayer");
        DontDestroyOnLoad(go);
        go.AddComponent<ConsoleLayer>();
    }

    private void Awake()
    {
        Instance = this;
        menu = new InputAction("Menu", InputActionType.Button);
        menu.AddBinding("<Gamepad>/start");
        menu.AddBinding("<Keyboard>/escape");
        menu.performed += _ => MenuPressed();
        menu.Enable();
        InputSystem.onDeviceChange += OnDeviceChange;
        SceneManager.sceneLoaded += OnSceneLoaded;
        BuildOverlay();
    }

    // La primera escena ya se cargó antes de instalar la capa.
    private void Start() => PrepareScene();

    private void OnDestroy()
    {
        InputSystem.onDeviceChange -= OnDeviceChange;
        SceneManager.sceneLoaded -= OnSceneLoaded;
        menu.Dispose();
        if (Instance == this) Instance = null;
    }

    private void OnSceneLoaded(Scene scene, LoadSceneMode mode)
    {
        if (pause.IsPaused) Resume();
        PrepareScene();
    }

    private void OnDeviceChange(InputDevice device, InputDeviceChange change)
    {
        if (ConsoleRules.ShouldPauseOnDeviceChange(device is Gamepad && device.native, change))
            Interrupt(PauseReason.ControllerLost);
    }

    private void OnApplicationFocus(bool hasFocus)
    {
        if (!hasFocus) Interrupt(PauseReason.FocusLost);
    }

    private void Update()
    {
        if (!pause.IsPaused) KeepMenuFocus();
    }

    public void PrepareScene()
    {
        UseInputSystemUIModule();
        foreach (Button button in FindObjectsByType<Button>(FindObjectsInactive.Include, FindObjectsSortMode.None))
        {
            if (IsQuitButton(button))
            {
                button.gameObject.SetActive(false);
                continue;
            }
            ColorBlock colors = button.colors;
            colors.selectedColor = SelectedColor;
            button.colors = colors;
        }
        ConsoleText.EnforceMinimum();
    }

    public void MenuPressed()
    {
        if (pause.MenuPressed(GameplayActive)) Apply();
    }

    public void Interrupt(PauseReason reason)
    {
        if (pause.Interrupt(reason, GameplayActive)) Apply();
    }

    public void Resume()
    {
        pause.Clear();
        Apply();
    }

    public static bool IsQuitButton(Button button)
    {
        for (int i = 0; i < button.onClick.GetPersistentEventCount(); i++)
            if (ConsoleRules.IsQuitMethod(button.onClick.GetPersistentMethodName(i))) return true;
        return false;
    }

    private void Apply()
    {
        bool paused = pause.IsPaused;
        Time.timeScale = paused ? 0f : 1f;
        AudioListener.pause = paused;
        foreach (MonoBehaviour behaviour in FindObjectsByType<MonoBehaviour>(FindObjectsSortMode.None))
            if (behaviour is IConsolePausable pausable) pausable.SetConsolePaused(paused);
        overlayText.text = pause.Reason == PauseReason.ControllerLost
            ? "Se desconectó el control\n\nReconectalo y presioná Menu (≡)"
            : "PAUSA\n\nMenu (≡) para continuar";
        overlay.SetActive(paused);
    }

    // Escenas pensadas para mouse (Asteroides) traen el StandaloneInputModule del Input Manager.
    private static void UseInputSystemUIModule()
    {
        EventSystem eventSystem = EventSystem.current != null ? EventSystem.current : FindFirstObjectByType<EventSystem>();
        if (eventSystem == null) return;
        StandaloneInputModule legacy = eventSystem.GetComponent<StandaloneInputModule>();
        if (legacy == null) return;
        DestroyImmediate(legacy);
        eventSystem.gameObject.AddComponent<InputSystemUIInputModule>().AssignDefaultActions();
    }

    private static void KeepMenuFocus()
    {
        EventSystem eventSystem = EventSystem.current;
        if (eventSystem == null) return;
        GameObject current = eventSystem.currentSelectedGameObject;
        if (current != null && current.activeInHierarchy && IsUsable(current.GetComponent<Selectable>())) return;
        Selectable first = FirstUsableSelectable();
        if (first != null) eventSystem.SetSelectedGameObject(first.gameObject);
    }

    // El de más arriba (y a la izquierda) en pantalla, como lo leería el jugador.
    private static Selectable FirstUsableSelectable()
    {
        Selectable best = null;
        foreach (Selectable s in Selectable.allSelectablesArray)
        {
            if (!IsUsable(s)) continue;
            if (best == null || s.transform.position.y > best.transform.position.y + 1f ||
                (Mathf.Abs(s.transform.position.y - best.transform.position.y) <= 1f && s.transform.position.x < best.transform.position.x))
                best = s;
        }
        return best;
    }

    private static bool IsUsable(Selectable s) =>
        s != null && s.isActiveAndEnabled && s.IsInteractable() && s.navigation.mode != Navigation.Mode.None;

    private void BuildOverlay()
    {
        overlay = new GameObject("ConsolePauseOverlay", typeof(Canvas), typeof(CanvasScaler));
        overlay.transform.SetParent(transform, false);
        var canvas = overlay.GetComponent<Canvas>();
        canvas.renderMode = RenderMode.ScreenSpaceOverlay;
        canvas.sortingOrder = 1000;
        var scaler = overlay.GetComponent<CanvasScaler>();
        scaler.uiScaleMode = CanvasScaler.ScaleMode.ScaleWithScreenSize;
        scaler.referenceResolution = new Vector2(1920, 1080);
        scaler.matchWidthOrHeight = 1f;

        var background = new GameObject("Fondo", typeof(Image)).GetComponent<Image>();
        background.transform.SetParent(overlay.transform, false);
        background.color = new Color(0f, 0f, 0f, 0.75f);
        Stretch(background.rectTransform);

        overlayText = new GameObject("Mensaje", typeof(Text)).GetComponent<Text>();
        overlayText.transform.SetParent(overlay.transform, false);
        overlayText.font = Resources.GetBuiltinResource<Font>("LegacyRuntime.ttf");
        overlayText.fontSize = 56;
        overlayText.alignment = TextAnchor.MiddleCenter;
        overlayText.color = Color.white;
        Stretch(overlayText.rectTransform);

        overlay.SetActive(false);
    }

    private static void Stretch(RectTransform rect)
    {
        rect.anchorMin = Vector2.zero;
        rect.anchorMax = Vector2.one;
        rect.offsetMin = Vector2.zero;
        rect.offsetMax = Vector2.zero;
    }
}
