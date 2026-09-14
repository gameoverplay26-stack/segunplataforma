using NUnit.Framework;

public class PlayerHealthTests
{
    [Test]
    public void TakeDamage_ReducesHealthByAmount()
    {
        // Arrange
        var health = new PlayerHealth(maxHealth: 100);

        // Act
        health.TakeDamage(25);

        // Assert
        Assert.AreEqual(75, health.CurrentHealth);
    }
    [Test]
    public void TakeDamage_NeverGoesBelowZero()
    {
        var health = new PlayerHealth(maxHealth: 100);
        health.TakeDamage(150);
        Assert.AreEqual(0, health.CurrentHealth);
    }
}