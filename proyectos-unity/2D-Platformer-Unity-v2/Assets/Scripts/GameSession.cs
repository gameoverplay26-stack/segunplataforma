using UnityEngine;

// Estado que sobrevive a la recarga de escenas: las vidas (DEC-LAB-016).
// Clase sin MonoBehaviour para poder probarla con unit tests de Edit Mode.
public static class GameSession
{
    public const int MaxLives = 3;
    public const int FirstLevelBuildIndex = 1; // 0 = Menu, 1 = Level, 2 = Level2

    public static int Lives { get; private set; } = MaxLives;
    public static bool IsGameOver => Lives <= 0;

    public static void NewGame()
    {
        Lives = MaxLives;
    }

    // Resta una vida y devuelve las que quedan (nunca menos de 0).
    public static int LoseLife()
    {
        if (Lives > 0) Lives--;
        return Lives;
    }

    // Con "Enter Play Mode Options" sin recarga de dominio, los estáticos sobreviven entre Plays.
    [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]
    private static void ResetOnPlay()
    {
        NewGame();
    }
}
