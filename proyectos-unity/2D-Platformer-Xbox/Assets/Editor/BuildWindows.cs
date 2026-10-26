using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEngine;

// Build de PC (Windows 64 bits). El instalador lo arma después Inno Setup (Tools/instalador-windows.iss).
// Batchmode: Unity.exe -batchmode -projectPath <v2> -buildTarget Win64 -executeMethod BuildWindows.Build -quit -logFile <log>
public static class BuildWindows
{
    public const string ExePath = "Builds/Windows/Platformer-v2.exe";

    [MenuItem("Porteo/Build Windows (PC)")]
    public static void Build()
    {
        var options = new BuildPlayerOptions
        {
            scenes = System.Array.ConvertAll(System.Array.FindAll(EditorBuildSettings.scenes, s => s.enabled), s => s.path),
            locationPathName = ExePath,
            target = BuildTarget.StandaloneWindows64,
            options = BuildOptions.None
        };
        BuildReport report = BuildPipeline.BuildPlayer(options);
        Debug.Log($"[BuildWindows] {report.summary.result} · {report.summary.totalSize / (1024 * 1024)} MB · {report.summary.totalTime}");
        if (report.summary.result != BuildResult.Succeeded && Application.isBatchMode)
            EditorApplication.Exit(1);
    }
}
