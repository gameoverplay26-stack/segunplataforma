using System.Collections;
using UnityEngine;
using UnityEngine.UI;

public class EnemyTarget : MonoBehaviour
{
    [SerializeField] private int maxHealth = 60;
    [SerializeField] private Slider healthSlider;
    [SerializeField] private Text healthLabel;
    [SerializeField] private Renderer bodyRenderer;

    private static readonly Color AliveColor = new Color(0.75f, 0.2f, 0.2f);
    private static readonly Color DeadColor = new Color(0.35f, 0.35f, 0.35f);
    private static readonly Color FlashColor = Color.white;
    private const float FlashDuration = 0.1f;
    private const float FlashScale = 1.15f;

    public PlayerHealth Health { get; private set; }
    public bool IsDead => Health.IsDead;

    private bool isFlashing;

    private void Awake()
    {
        ResetEnemy();
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.R))
        {
            ResetEnemy();
        }

        UpdateUI();
    }

    public void ResetEnemy()
    {
        Health = new PlayerHealth(maxHealth);

        if (healthSlider != null)
        {
            healthSlider.maxValue = maxHealth;
        }

        UpdateUI();
    }

    public void PlayHitFlash()
    {
        if (bodyRenderer == null)
        {
            return;
        }

        StopCoroutine(nameof(HitFlashRoutine));
        StartCoroutine(nameof(HitFlashRoutine));
    }

    private IEnumerator HitFlashRoutine()
    {
        isFlashing = true;
        var originalScale = transform.localScale;

        bodyRenderer.material.color = FlashColor;
        transform.localScale = originalScale * FlashScale;

        yield return new WaitForSeconds(FlashDuration);

        transform.localScale = originalScale;
        isFlashing = false;
    }

    private void UpdateUI()
    {
        if (healthSlider != null)
        {
            healthSlider.value = Health.CurrentHealth;
        }

        if (healthLabel != null)
        {
            healthLabel.text = Health.IsDead
                ? $"Enemigo: {Health.CurrentHealth}/{Health.MaxHealth} (DERROTADO)"
                : $"Enemigo: {Health.CurrentHealth}/{Health.MaxHealth}";
        }

        // Mientras isFlashing, HitFlashRoutine controla el color — si lo pisaramos aca
        // ac cada frame, el flash nunca se llegaria a ver (dura menos que este chequeo).
        if (bodyRenderer != null && !isFlashing)
        {
            bodyRenderer.material.color = Health.IsDead ? DeadColor : AliveColor;
        }
    }
}
