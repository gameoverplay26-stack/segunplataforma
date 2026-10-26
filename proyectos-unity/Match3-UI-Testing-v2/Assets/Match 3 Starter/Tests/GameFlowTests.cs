using System;
using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.TestTools;
using UnityEngine.UI;

// Tests de humo del Match 3 (Play Mode, integración): recorren el flujo real
// Menu → Play → Game → jugadas → Game Over usando los botones de la UI.
public class GameFlowTests
{
    const float Timeout = 10f;

    // Tablero fijo de 4x4 (filas de arriba hacia abajo). B G M P R Y = índices 0..5 de BoardManager.candies.
    static readonly string[,] FixedGrid =
    {
        { "B", "G", "B", "M" },
        { "G", "B", "G", "P" },
        { "R", "Y", "R", "Y" },
        { "Y", "R", "Y", "R" },
    };

    // GameManager sobrevive entre escenas (DontDestroyOnLoad): se elimina para que cada test arranque limpio.
    [UnityTearDown]
    public IEnumerator TearDown()
    {
        if (GameManager.instance != null)
            UnityEngine.Object.Destroy(GameManager.instance.gameObject);
        GameManager.instance = null;
        yield return null;
    }

    static IEnumerator WaitUntilOrFail(Func<bool> condition, string message)
    {
        float t = 0f;
        while (!condition())
        {
            if (t > Timeout) Assert.Fail($"Timeout ({Timeout}s): {message}");
            t += Time.unscaledDeltaTime;
            yield return null;
        }
    }

    // Abre el menú y pulsa Play, como lo haría el jugador.
    static IEnumerator StartGameFromMenu()
    {
        SceneManager.LoadScene("Menu");
        yield return WaitUntilOrFail(() => SceneManager.GetActiveScene().name == "Menu", "no cargó Menu");
        yield return null;

        var play = GameObject.Find("PlayButton");
        Assert.IsNotNull(play, "No se encontró PlayButton en el menú");
        play.GetComponent<Button>().onClick.Invoke();

        yield return WaitUntilOrFail(() => SceneManager.GetActiveScene().name == "Game", "Play no cargó la escena Game");
        yield return WaitUntilOrFail(() => BoardManager.instance != null && BoardManager.instance.tiles != null, "el tablero no se generó");
        yield return null;
    }

    static IEnumerator LoadFixedBoard()
    {
        BoardManager.instance.InitializeBoard(FixedGrid);
        yield return null; // Start() de cada Tile registra el listener del botón
        yield return null;
    }

    static void Click(int x, int y) =>
        BoardManager.instance.tiles[x, y].GetComponent<Button>().onClick.Invoke();

    static IEnumerator Swap(int x1, int y1, int x2, int y2)
    {
        Click(x1, y1);
        Click(x2, y2);
        yield return WaitUntilOrFail(() => !BoardManager.instance.IsPlayingAnim, "la animación de la jugada no terminó");
        yield return null;
    }

    [UnityTest]
    public IEnumerator PlayButton_LoadsGameScene_WithFiveMoves()
    {
        yield return StartGameFromMenu();

        Assert.AreEqual("Game", SceneManager.GetActiveScene().name);
        Assert.AreEqual(5, GUIManager.instance.MoveCounter);
        Assert.AreEqual(0, GUIManager.instance.Score);
    }

    [UnityTest]
    public IEnumerator RandomBoard_HasNoInitialMatches()
    {
        yield return StartGameFromMenu();

        var board = BoardManager.instance;
        Assert.Greater(board.xSize, 0);
        Assert.Greater(board.ySize, 0);
        for (int x = 0; x < board.xSize; x++)
            for (int y = 0; y < board.ySize; y++)
                Assert.IsEmpty(board.FindMatches(new Vector2Int(x, y)), $"Hay un match inicial en ({x},{y})");
    }

    [UnityTest]
    public IEnumerator SwapWithoutMatch_SpendsOneMove_AndKeepsScore()
    {
        yield return StartGameFromMenu();
        yield return LoadFixedBoard();

        yield return Swap(0, 2, 0, 3);

        Assert.AreEqual(4, GUIManager.instance.MoveCounter);
        Assert.AreEqual(0, GUIManager.instance.Score);
    }

    [UnityTest]
    public IEnumerator SwapCreatingTwoMatchesOfThree_Adds300Points()
    {
        yield return StartGameFromMenu();
        yield return LoadFixedBoard();

        // G(1,0) <-> B(1,1): fila 0 queda B B B y fila 1 queda G G G → 2 × 3 × 50 = 300.
        yield return Swap(1, 0, 1, 1);

        Assert.AreEqual(300, GUIManager.instance.Score);
        Assert.AreEqual(4, GUIManager.instance.MoveCounter);
    }

    [UnityTest]
    public IEnumerator FiveMoves_ShowGameOverPanel()
    {
        yield return StartGameFromMenu();
        yield return LoadFixedBoard();

        for (int i = 0; i < 5; i++)
            yield return Swap(0, 2, 0, 3);

        yield return WaitUntilOrFail(() => GUIManager.instance.gameOverPanel.activeInHierarchy, "no apareció el panel de Game Over");
        Assert.AreEqual(0, GUIManager.instance.MoveCounter);
        Assert.IsTrue(GameManager.instance.gameOver);
    }
}
