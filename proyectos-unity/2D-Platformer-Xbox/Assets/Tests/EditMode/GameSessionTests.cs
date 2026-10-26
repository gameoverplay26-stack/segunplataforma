using NUnit.Framework;

// Unit: reglas de vidas (DEC-LAB-016), sin escenas.
public class GameSessionTests
{
    [SetUp]
    public void Reset() => GameSession.NewGame();

    [Test]
    public void NewGame_StartsWithThreeLives()
    {
        Assert.AreEqual(3, GameSession.Lives);
        Assert.IsFalse(GameSession.IsGameOver);
    }

    [Test]
    public void LoseLife_SubtractsOne()
    {
        Assert.AreEqual(2, GameSession.LoseLife());
        Assert.AreEqual(2, GameSession.Lives);
    }

    [Test]
    public void LosingAllLives_IsGameOver_AndNeverNegative()
    {
        GameSession.LoseLife();
        GameSession.LoseLife();
        Assert.AreEqual(0, GameSession.LoseLife());
        Assert.IsTrue(GameSession.IsGameOver);
        Assert.AreEqual(0, GameSession.LoseLife());
    }

    [Test]
    public void NewGame_AfterGameOver_RestoresLives()
    {
        for (int i = 0; i < 3; i++) GameSession.LoseLife();
        GameSession.NewGame();
        Assert.AreEqual(GameSession.MaxLives, GameSession.Lives);
    }
}
