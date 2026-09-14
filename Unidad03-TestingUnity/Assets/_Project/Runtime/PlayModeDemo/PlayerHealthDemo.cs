using UnityEngine;
using UnityEngine.UI;

public class PlayerHealthDemo : MonoBehaviour
{
    [SerializeField] private int maxHealth = 100;
    [SerializeField] private int damageAmount = 20;
    [SerializeField] private int healAmount = 15;
    [SerializeField] private Slider healthSlider;
    [SerializeField] private Text healthLabel;

    private PlayerHealth health;

    private void Awake()
    {
        health = new PlayerHealth(maxHealth);

        if (healthSlider != null)
        {
            healthSlider.maxValue = maxHealth;
        }

        UpdateUI();
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            health.TakeDamage(damageAmount);
            UpdateUI();
        }

        if (Input.GetKeyDown(KeyCode.H))
        {
            health.Heal(healAmount);
            UpdateUI();
        }
    }

    private void UpdateUI()
    {
        if (healthSlider != null)
        {
            healthSlider.value = health.CurrentHealth;
        }

        if (healthLabel != null)
        {
            healthLabel.text = health.IsDead
                ? $"HP: {health.CurrentHealth}/{health.MaxHealth} (MUERTO)"
                : $"HP: {health.CurrentHealth}/{health.MaxHealth}";
        }
    }
}
