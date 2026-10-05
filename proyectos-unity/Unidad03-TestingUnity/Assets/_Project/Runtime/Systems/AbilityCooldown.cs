public class AbilityCooldown
{
    public float CooldownDuration { get; }
    public float TimeSinceLastUse { get; private set; }
    public bool IsReady => TimeSinceLastUse >= CooldownDuration;

    public AbilityCooldown(float cooldownDuration)
    {
        CooldownDuration = cooldownDuration;
        TimeSinceLastUse = cooldownDuration;
    }

    public void Use()
    {
        TimeSinceLastUse = 0f;
    }

    public void Tick(float deltaTime)
    {
        TimeSinceLastUse += deltaTime;
    }
}
