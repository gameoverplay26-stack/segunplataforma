using System.Collections;
using NUnit.Framework;
using UnityEngine;
using UnityEngine.TestTools;

public class FrameCounterTests
{
    [UnityTest]
    public IEnumerator FrameCounter_IncrementsFramesElapsed_AfterOneFrame()
    {
        // Arrange
        var go = new GameObject("FrameCounter");
        var counter = go.AddComponent<FrameCounter>();

        // Act
        yield return null;

        // Assert
        Assert.Greater(counter.FramesElapsed, 0);

        Object.Destroy(go);
    }
}
