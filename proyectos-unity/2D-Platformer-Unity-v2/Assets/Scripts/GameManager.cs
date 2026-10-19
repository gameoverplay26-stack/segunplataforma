using UnityEngine;
using TMPro;
using System.Collections;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    public static GameManager instance;


    [SerializeField] private TMP_Text coinText;

    [SerializeField] private PlayerController playerController;

    private int coinCount = 0;
    private int gemCount = 0;
    private bool isGameOver = false;
    private Vector3 playerPosition;

    //Level Complete

    [SerializeField] GameObject levelCompletePanel;
    [SerializeField] TMP_Text leveCompletePanelTitle;
    [SerializeField] TMP_Text levelCompleteCoins;
    [SerializeField] GameObject nextLevelButton;   // v2: solo si hay un nivel siguiente

    //Game Over (v2, DEC-LAB-016)
    [SerializeField] GameObject gameOverPanel;
    public bool IsDead => isGameOver;




   
    private int totalCoins = 0;
  



    private void Awake()
    {
        instance = this;
        Application.targetFrameRate = 60;
    }

    private void Start()
    {
        UpdateGUI();
        UIManager.instance.fadeFromBlack = true;
        playerPosition = playerController.transform.position;

        FindTotalPickups();
    }

    public void IncrementCoinCount()
    {
        coinCount++;
        UpdateGUI();
    }
    public void IncrementGemCount()
    {
        gemCount++;
        UpdateGUI();
    }

    private void UpdateGUI()
    {
        coinText.text = coinCount.ToString();
  
    }

    public void Death()
    {
        if (!isGameOver)
        {
            Sfx.Play(Sfx.Kind.Death);

            // v2: cada muerte resta una vida (DEC-LAB-016)
            GameSession.LoseLife();
            if (LivesHUD.instance != null) LivesHUD.instance.Refresh();

            // Disable Mobile Controls
            UIManager.instance.DisableMobileControls();
            // Initiate screen fade
            UIManager.instance.fadeToBlack = true;

            // Disable the player object
            playerController.gameObject.SetActive(false);

            // Start death coroutine to wait and then respawn the player
            StartCoroutine(DeathCoroutine());

            // Update game state
            isGameOver = true;

            // Log death message
            Debug.Log("Died");
        }
    }
 
    public void FindTotalPickups()
    {

        pickup[] pickups = GameObject.FindObjectsOfType<pickup>();

        foreach (pickup pickupObject in pickups)
        {
            if (pickupObject.pt == pickup.pickupType.coin)
            {
                totalCoins += 1;
            }
           
        }


      
    }
    public void LevelComplete()
    {
        // v2: los botones táctiles no deben tapar el panel final.
        UIManager.instance.DisableMobileControls();
       


        levelCompletePanel.SetActive(true);
        bool hasNext = HasNextLevel;
        leveCompletePanelTitle.text = hasNext ? "LEVEL COMPLETE" : "GAME COMPLETE!";
        if (nextLevelButton != null) nextLevelButton.SetActive(hasNext);



        levelCompleteCoins.text = "COINS COLLECTED: "+ coinCount.ToString() +" / " + totalCoins.ToString();
 
    }
   
    public IEnumerator DeathCoroutine()
    {
        yield return new WaitForSeconds(1f);
        playerController.transform.position = playerPosition;

        // Wait for 2 seconds
        yield return new WaitForSeconds(1f);

        // Check if the game is still over (in case player respawns earlier)
        if (isGameOver)
        {
            if (GameSession.IsGameOver)
            {
                ShowGameOver();
            }
            else
            {
                // v2: se reinicia el nivel actual (antes, siempre la escena 1)
                SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
            }
        }
    }

    // Hay nivel siguiente si la escena que sigue en el build es otro nivel ("Level…").
    // No alcanza con contar escenas: el Test Runner agrega la suya al final de la lista.
    public bool HasNextLevel
    {
        get
        {
            int next = SceneManager.GetActiveScene().buildIndex + 1;
            if (next >= SceneManager.sceneCountInBuildSettings) return false;
            string path = SceneUtility.GetScenePathByBuildIndex(next);
            return System.IO.Path.GetFileNameWithoutExtension(path).StartsWith("Level");
        }
    }

    private void ShowGameOver()
    {
        gameOverPanel.SetActive(true);
    }

}
