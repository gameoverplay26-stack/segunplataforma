using UnityEngine;
using UnityEngine.UI;

public class PlayerHealthDemo : MonoBehaviour
{
    [SerializeField] private int maxHealth = 100;
    [SerializeField] private int damageAmount = 20;
    [SerializeField] private int healAmount = 15;
    [SerializeField] private Slider healthSlider;
    [SerializeField] private Image healthFill;
    [SerializeField] private Text healthLabel;

    private static readonly Color FullHealthColor = new Color(0.2f, 0.8f, 0.2f);
    private static readonly Color MidHealthColor = new Color(0.9f, 0.85f, 0.1f);
    private static readonly Color LowHealthColor = new Color(0.85f, 0.2f, 0.2f);

    private PlayerHealth health;

    private void Awake()
    {
        ResetHealth();
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            ApplyDamage();
        }

        if (Input.GetKeyDown(KeyCode.H))
        {
            ApplyHeal();
        }
    }

    public void ApplyDamage()
    {
        health.TakeDamage(damageAmount);
        UpdateUI();
    }

    public void ApplyHeal()
    {
        health.Heal(healAmount);
        UpdateUI();
    }

    public void ResetHealth()
    {
        health = new PlayerHealth(maxHealth);

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
            healthSlider.value = health.CurrentHealth;
        }

        float healthFraction = (float)health.CurrentHealth / health.MaxHealth;

        if (healthFill != null)
        {
            healthFill.color = EvaluateHealthColor(healthFraction);
        }

        if (healthLabel != null)
        {
            healthLabel.text = health.IsDead
                ? $"HP: {health.CurrentHealth}/{health.MaxHealth} (MUERTO)"
                : $"HP: {health.CurrentHealth}/{health.MaxHealth}";
            healthLabel.color = health.IsDead ? LowHealthColor : Color.white;
        }
    }

    private static Color EvaluateHealthColor(float healthFraction)
    {
        if (healthFraction > 0.5f)
        {
            float t = (healthFraction - 0.5f) / 0.5f;
            return Color.Lerp(MidHealthColor, FullHealthColor, t);
        }

        return Color.Lerp(LowHealthColor, MidHealthColor, healthFraction / 0.5f);
    }
}
