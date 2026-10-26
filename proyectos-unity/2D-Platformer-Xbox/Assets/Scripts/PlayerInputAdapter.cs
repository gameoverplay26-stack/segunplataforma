using UnityEngine;
using UnityEngine.InputSystem;

// Dispositivo -> intención. Traduce teclado, gamepad y botones en pantalla
// (que simulan un gamepad virtual) a PlayerController.SetIntent.
// Corre antes que PlayerController para que el salto se aplique en el mismo frame.
// Versión Xbox: la capa de consola lo apaga mientras el juego está en pausa.
[DefaultExecutionOrder(-10)]
public class PlayerInputAdapter : MonoBehaviour, IConsolePausable
{
    public PlayerController player;
    [Range(0f, 1f)] public float deadZone = 0.2f;

    private InputAction move;
    private InputAction jump;

    private void Awake()
    {
        move = new InputAction("Move", InputActionType.Value);
        move.AddCompositeBinding("1DAxis")
            .With("Negative", "<Keyboard>/leftArrow")
            .With("Positive", "<Keyboard>/rightArrow");
        move.AddCompositeBinding("1DAxis")
            .With("Negative", "<Keyboard>/a")
            .With("Positive", "<Keyboard>/d");
        move.AddBinding("<Gamepad>/leftStick/x");
        move.AddBinding("<Gamepad>/dpad/x");

        jump = new InputAction("Jump", InputActionType.Button);
        jump.AddBinding("<Keyboard>/space");
        jump.AddBinding("<Gamepad>/buttonSouth");
    }

    private void OnEnable()
    {
        move.Enable();
        jump.Enable();
    }

    private void OnDisable()
    {
        move.Disable();
        jump.Disable();
    }

    private void OnDestroy()
    {
        move.Dispose();
        jump.Dispose();
    }

    public void SetConsolePaused(bool paused)
    {
        enabled = !paused;
        if (paused && player != null) player.SetIntent(0f, false);
    }

    private void Update()
    {
        float raw = move.ReadValue<float>();
        float horizontal = Mathf.Abs(raw) < deadZone ? 0f : Mathf.Sign(raw);
        player.SetIntent(horizontal, jump.WasPressedThisFrame());
    }
}
