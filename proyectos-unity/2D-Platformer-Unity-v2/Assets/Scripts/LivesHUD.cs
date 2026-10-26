using UnityEngine;
using UnityEngine.UI;

// Muestra las vidas con los corazones del HUD: lleno = vida disponible, vacío = vida perdida.
public class LivesHUD : MonoBehaviour
{
    public static LivesHUD instance;

    [SerializeField] private Image[] hearts;   // de izquierda a derecha
    [SerializeField] private Sprite fullHeart;
    [SerializeField] private Sprite emptyHeart;

    private void Awake()
    {
        instance = this;
    }

    private void Start()
    {
        Refresh();
    }

    public void Refresh()
    {
        for (int i = 0; i < hearts.Length; i++)
        {
            hearts[i].sprite = i < GameSession.Lives ? fullHeart : emptyHeart;
        }
    }

    public Sprite SpriteAt(int i) => hearts[i].sprite;
    public bool IsFull(int i) => hearts[i].sprite == fullHeart;
}
