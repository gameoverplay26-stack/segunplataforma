using UnityEngine;

public class FrameCounter : MonoBehaviour
{
    public int FramesElapsed { get; private set; }

    private void Update()
    {
        FramesElapsed++;
    }
}
