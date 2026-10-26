// Componentes que deben detenerse mientras la capa de consola tiene el juego en pausa
// (los adaptadores de entrada: con Time.timeScale = 0 seguirían leyendo el mando).
public interface IConsolePausable
{
    void SetConsolePaused(bool paused);
}
