using UnityEngine;

// Efectos de sonido. Un objeto "Audio" por escena (lo crea PorteoSetup) con los clips asignados.
// Se usa con Sfx.Play(Sfx.Kind.Coin): si no hay instancia en la escena, no hace nada.
[RequireComponent(typeof(AudioSource))]
public class Sfx : MonoBehaviour
{
    public enum Kind { Coin, Jump, DoubleJump, Death }

    public static Sfx instance;

    public AudioClip coin;
    public AudioClip jump;
    public AudioClip death;

    // Último efecto pedido: lo leen los tests (el batchmode no tiene salida de audio para medir).
    public static Kind? LastPlayed { get; private set; }

    private AudioSource source;

    private void Awake()
    {
        instance = this;
        source = GetComponent<AudioSource>();
    }

    private void OnDestroy()
    {
        if (instance == this) instance = null;
    }

    public static void Play(Kind kind)
    {
        LastPlayed = kind;
        if (instance != null) instance.PlayClip(kind);
    }

    private void PlayClip(Kind kind)
    {
        switch (kind)
        {
            case Kind.Coin: source.pitch = 1f; source.PlayOneShot(coin); break;
            case Kind.Jump: source.pitch = 1f; source.PlayOneShot(jump); break;
            case Kind.DoubleJump: source.pitch = 1.25f; source.PlayOneShot(jump); break;
            case Kind.Death: source.pitch = 1f; source.PlayOneShot(death); break;
        }
    }
}
