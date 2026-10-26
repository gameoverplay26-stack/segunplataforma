using UnityEngine;

// Muestra los controles táctiles solo en plataformas móviles
// (incluido el Device Simulator del Editor).
public class MobileControlsVisibility : MonoBehaviour
{
    private void Awake()
    {
        gameObject.SetActive(Application.isMobilePlatform);
    }
}
