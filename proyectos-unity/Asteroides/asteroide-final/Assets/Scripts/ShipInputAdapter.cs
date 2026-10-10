using UnityEngine;
using UnityEngine.InputSystem;

// Capa "dispositivo -> intención": traduce teclado, gamepad y controles
// táctiles (OnScreenStick/OnScreenButton, que simulan un gamepad) en una
// intención de la nave. La nave no sabe qué dispositivo se usó.
[RequireComponent(typeof(Ship))]
public class ShipInputAdapter : MonoBehaviour
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

    private void Update()
    {
        ship.SetIntent(move.ReadValue<float>(), fire.IsPressed());
    }
}
