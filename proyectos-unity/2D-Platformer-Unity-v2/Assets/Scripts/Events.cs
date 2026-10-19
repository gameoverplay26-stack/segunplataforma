using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Events : MonoBehaviour
{
    public void Menu()
    {
        SceneManager.LoadScene(0);
    }
    // Jugar desde el menú: partida nueva con todas las vidas.
    public void Level()
    {
        GameSession.NewGame();
        SceneManager.LoadScene(GameSession.FirstLevelBuildIndex);
    }

    // Botón "Next Level" del panel de nivel completo.
    public void NextLevel()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
    }

    // Botón "Retry" del panel de Game Over: vuelve al nivel 1 con 3 vidas (DEC-LAB-016).
    public void Retry()
    {
        GameSession.NewGame();
        SceneManager.LoadScene(GameSession.FirstLevelBuildIndex);
    }
    public void Quit()
    {
        Application.Quit();
    }
}
