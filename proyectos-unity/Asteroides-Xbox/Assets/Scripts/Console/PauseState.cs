// Estado de pausa de la capa de consola. Sin MonoBehaviour para probarlo con unit tests.
public enum PauseReason { None, MenuButton, ControllerLost, FocusLost }

public class PauseState
{
    public PauseReason Reason { get; private set; } = PauseReason.None;
    public bool IsPaused => Reason != PauseReason.None;

    // Botón Menu: en pausa, reanuda (cualquiera sea el motivo); jugando, pausa.
    // Fuera de la partida (menús, paneles) no hace nada. Devuelve true si el estado cambió.
    public bool MenuPressed(bool gameplayActive)
    {
        if (IsPaused)
        {
            Reason = PauseReason.None;
            return true;
        }
        if (!gameplayActive) return false;
        Reason = PauseReason.MenuButton;
        return true;
    }

    // Pausa automática (control desconectado, foco perdido). Solo reanuda el jugador con Menu.
    // Si ya está en pausa, la desconexión del control reemplaza el motivo para mostrar ese mensaje.
    public bool Interrupt(PauseReason reason, bool gameplayActive)
    {
        if (reason == PauseReason.None || !gameplayActive) return false;
        if (IsPaused && (reason != PauseReason.ControllerLost || Reason == reason)) return false;
        Reason = reason;
        return true;
    }

    public void Clear() => Reason = PauseReason.None;
}
