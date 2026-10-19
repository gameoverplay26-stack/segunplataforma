using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEngine;

// Batchmode: Unity.exe -batchmode -projectPath <v2> -buildTarget Android -executeMethod BuildAndroid.Build -quit -logFile <log>
public static class BuildAndroid
{
    [MenuItem("Porteo/Build Android (APK)")]
    public static void Build()
    {
        var options = new BuildPlayerOptions
        {
            // Las escenas salen de Build Settings (Menu, Level, Level2), no de una lista fija.
            scenes = System.Array.ConvertAll(System.Array.FindAll(EditorBuildSettings.scenes, s => s.enabled), s => s.path),
            locationPathName = "Builds/Platformer-v2.apk",
            target = BuildTarget.Android,
            options = BuildOptions.None
        };
        BuildReport report = BuildPipeline.BuildPlayer(options);
        Debug.Log($"[BuildAndroid] {report.summary.result} · {report.summary.totalSize / (1024 * 1024)} MB · {report.summary.totalTime}");
        if (report.summary.result != BuildResult.Succeeded && Application.isBatchMode)
            EditorApplication.Exit(1);
    }
}
