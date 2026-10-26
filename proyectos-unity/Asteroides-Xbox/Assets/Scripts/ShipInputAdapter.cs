using UnityEngine;
using UnityEngine.InputSystem;

// Capa "dispositivo -> intención": traduce teclado, gamepad y controles
// táctiles (OnScreenStick/OnScreenButton, que simulan un gamepad) en una
// intención de la nave. La nave no sabe qué dispositivo se usó.
// Versión Xbox: la capa de consola lo apaga mientras el juego está en pausa.
[RequireComponent(typeof(Ship))]
public class ShipInputAdapter : MonoBehaviour, IConsolePausable
{
    private Ship ship;
    private InputAction move;
    private InputAction fire;

    private void Awake()
    {
        ship = GetComponent<Ship>();

        move = new InputAction("Move", InputActionType.Value);
        move.AddCompositeBinding("1DAxis")
            .With("Negative", "<Keyboard>/leftArrow")
            .With("Positive", "<Keyboard>/rightArrow");
        move.AddBinding("<Gamepad>/leftStick/x");
        move.AddBinding("<Gamepad>/dpad/x");

        fire = new InputAction("Fire", InputActionType.Button);
        fire.AddBinding("<Keyboard>/space");
        fire.AddBinding("<Gamepad>/buttonSouth");
    }

    private void OnEnable()
    {
        move.Enable();
        fire.Enable();
    }

    private void OnDisable()
    {
        move.Disable();
        fire.Disable();
    }

    private void OnDestroy()
    {
        move.Dispose();
        fire.Dispose();
    }

    public void SetConsolePaused(bool paused)
    {
        enabled = !paused;
        if (paused && ship != null) ship.SetIntent(0f, false);
    }

    private void Update()
    {
        ship.SetIntent(move.ReadValue<float>(), fire.IsPressed());
    }
}
