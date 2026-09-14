using UnityEngine;

public class PlayerHealth
{
    public int MaxHealth { get; }
    public int CurrentHealth { get; private set; }
    public bool IsDead => CurrentHealth <= 0;

    public PlayerHealth(int maxHealth)
    {
        MaxHealth = maxHealth;
        CurrentHealth = maxHealth;
    }

    public void TakeDamage(int amount)
    {
        CurrentHealth = CurrentHealth - amount; // sin clamp — bug deliberado
    }

    public void Heal(int amount)
    {
        CurrentHealth = Mathf.Min(MaxHealth, CurrentHealth + amount);
    }
}
