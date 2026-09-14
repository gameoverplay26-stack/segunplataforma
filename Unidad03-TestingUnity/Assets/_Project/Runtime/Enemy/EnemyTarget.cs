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

    public PlayerHealth Health { get; private set; }
    public bool IsDead => Health.IsDead;

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

        if (bodyRenderer != null)
        {
            bodyRenderer.material.color = Health.IsDead ? DeadColor : AliveColor;
        }
    }
}
