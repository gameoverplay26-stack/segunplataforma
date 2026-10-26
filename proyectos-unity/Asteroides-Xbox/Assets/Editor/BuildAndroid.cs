using System.Linq;
using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEngine;

// Genera el APK de Android de forma reproducible, sin abrir la ventana Build Profiles.
// Uso (batchmode):
//   Unity.exe -batchmode -projectPath <ruta> -buildTarget Android -executeMethod BuildAndroid.Build -quit -logFile <log>
// Usa los Player Settings del proyecto y las escenas tildadas en la Scene List.
public static class BuildAndroid
{
    private const string ApkPath = "Builds/AsteroideTest.apk";

    [MenuItem("Build/Android APK")]
    public static void Build()
    {
        var options = new BuildPlayerOptions
        {
            scenes = EditorBuildSettings.scenes.Where(s => s.enabled).Select(s => s.path).ToArray(),
            locationPathName = ApkPath,
            target = BuildTarget.Android,
            options = BuildOptions.None
        };

        BuildReport report = BuildPipeline.BuildPlayer(options);
        BuildSummary summary = report.summary;
        Debug.Log("[BuildAndroid] " + summary.result + " · " + summary.totalSize + " bytes · " + summary.totalTime);

        if (Application.isBatchMode && summary.result != BuildResult.Succeeded)
        {
            EditorApplication.Exit(1);
        }
    }
}
