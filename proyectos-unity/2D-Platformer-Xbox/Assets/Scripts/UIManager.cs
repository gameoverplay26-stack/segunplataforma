using UnityEngine;
using UnityEngine.UI;

public class UIManager : MonoBehaviour
{
    public static UIManager instance;
    public GameObject mobileControls;

    // v2: los controles táctiles se muestran según la plataforma (MOB-PLT-02).
    // UnityEngine.Device respeta el Device Simulator del Editor.
    // forceMobileControls sirve para probarlos en el Game view de PC.
    public bool forceMobileControls = false;
    public bool ShouldShowMobileControls =>
        forceMobileControls || UnityEngine.Device.Application.isMobilePlatform;

    public bool fadeToBlack, fadeFromBlack;
    public Image blackScreen;
    public float fadeSpeed = 2f;

    //player reference

    public PlayerController playerController;


    private void Awake()
    {
        instance = this;
    }

    public void DisableMobileControls()
    {
        mobileControls.SetActive(false);
    }
    public void EnableMobileControls()
    {
        mobileControls.SetActive(true);
    }

    private void Update()
    {
        UpdateFade();
    }

    private void UpdateFade()
    {
        if (fadeToBlack)
        {
            FadeToBlack();
        }
        else if (fadeFromBlack)
        {
            FadeFromBlack();
        }
    }

    private void FadeToBlack()
    {
        FadeScreen(1f);

        if (blackScreen.color.a >= 1f)
        {
            fadeToBlack = false;
        }
    }

    private void FadeFromBlack()
    {
        FadeScreen(0f);

        if (blackScreen.color.a <= 0f)
        {
            if (ShouldShowMobileControls)
            {
                EnableMobileControls();
            }
            fadeFromBlack = false;
        }
    }

    private void FadeScreen(float targetAlpha)
    {
        Color currentColor = blackScreen.color;
        float newAlpha = Mathf.MoveTowards(currentColor.a, targetAlpha, fadeSpeed * Time.deltaTime);
        blackScreen.color = new Color(currentColor.r, currentColor.g, currentColor.b, newAlpha);
    }
}
