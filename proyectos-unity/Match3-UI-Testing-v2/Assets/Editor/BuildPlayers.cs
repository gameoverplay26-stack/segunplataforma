using UnityEditor;
using UnityEditor.Build;
using UnityEditor.Build.Reporting;
using UnityEngine;

// Builds del Match 3 (UI Testing v2): APK de Android y PC (Windows 64 bits).
// El instalador de PC lo arma después Inno Setup (Tools/instalador-windows.iss).
// Batchmode: Unity.exe -batchmode -projectPath <v2> -buildTarget Android -executeMethod BuildPlayers.Android -quit -logFile <log>
//            Unity.exe -batchmode -projectPath <v2> -buildTarget Win64   -executeMethod BuildPlayers.Windows -quit -logFile <log>
public static class BuildPlayers
{
    const string ProductName = "Match 3 UI Testing";
    const string AppId = "ar.edu.unju.match3uitesting";

    static string[] Scenes() =>
        System.Array.ConvertAll(System.Array.FindAll(EditorBuildSettings.scenes, s => s.enabled), s => s.path);

    [MenuItem("Builds/Android (APK)")]
    public static void Android()
    {
        PlayerSettings.productName = ProductName;
        PlayerSettings.SetApplicationIdentifier(NamedBuildTarget.Android, AppId);
        // IL2CPP + ARM64: lo que exigen los teléfonos actuales (Mono solo genera ARMv7).
        PlayerSettings.SetScriptingBackend(NamedBuildTarget.Android, ScriptingImplementation.IL2CPP);
        PlayerSettings.Android.targetArchitectures = AndroidArchitecture.ARM64;
        PlayerSettings.defaultInterfaceOrientation = UIOrientation.AutoRotation;
        Run("BuildPlayers.Android", "Builds/Match3-UI-Testing.apk", BuildTarget.Android);
    }

    [MenuItem("Builds/Windows (PC)")]
    public static void Windows()
    {
        PlayerSettings.productName = ProductName;
        Run("BuildPlayers.Windows", "Builds/Windows/Match3-UI-Testing.exe", BuildTarget.StandaloneWindows64);
    }

    static void Run(string tag, string path, BuildTarget target)
    {
        var report = BuildPipeline.BuildPlayer(new BuildPlayerOptions
        {
            scenes = Scenes(),
            locationPathName = path,
            target = target,
            options = BuildOptions.None
        });
        Debug.Log($"[{tag}] {report.summary.result} · {report.summary.totalSize / (1024 * 1024)} MB · {report.summary.totalTime}");
        if (report.summary.result != BuildResult.Succeeded && Application.isBatchMode)
            EditorApplication.Exit(1);
    }
}
