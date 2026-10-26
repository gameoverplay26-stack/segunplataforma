using System.IO;
using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEngine;

// Build UWP para mostrar el juego en una Xbox en Developer Mode (demo local, sin tienda ni nube).
// Unity genera una solución de Visual Studio; el paquete .msix para instalar por Device Portal
// lo arma Tools/generar_build_xbox.ps1 (msbuild). Ver laboratorio-adaptacion/PORTEO-XBOX.md.
// Batchmode: Unity.exe -batchmode -projectPath <proyecto> -buildTarget WindowsStoreApps -executeMethod BuildXbox.Build -quit -logFile <log>
public static class BuildXbox
{
    public const string OutputPath = "Builds/UWP";

    // Cada versión con su propia identidad de paquete: así la original y la de consola conviven en la Xbox.
    public const string PackageName = "Catedra.Asteroides.Consola";
    public const string DisplayName = "Asteroides (consola)";

    // Certificado de prueba autofirmado que crea el script de PowerShell (no se versiona).
    public const string CertificatePath = "Certificados/xbox-prueba.pfx";
    public const string CertificatePassword = "unity-demo";

    [MenuItem("Porteo/Build Xbox (UWP, Developer Mode)")]
    public static void Build()
    {
        // Xbox solo acepta x64; se deja también Desktop para probar el paquete en la PC.
        EditorUserBuildSettings.wsaUWPBuildType = WSAUWPBuildType.D3D;
        EditorUserBuildSettings.wsaArchitecture = "x64";
        PlayerSettings.WSA.SetTargetDeviceFamily(PlayerSettings.WSATargetFamily.Xbox, true);
        PlayerSettings.WSA.SetTargetDeviceFamily(PlayerSettings.WSATargetFamily.Desktop, true);
        PlayerSettings.WSA.packageName = PackageName;
        if (File.Exists(CertificatePath) && !PlayerSettings.WSA.SetCertificate(CertificatePath, CertificatePassword))
            Debug.LogError($"[BuildXbox] No se pudo usar el certificado {CertificatePath}");

        var options = new BuildPlayerOptions
        {
            scenes = System.Array.ConvertAll(System.Array.FindAll(EditorBuildSettings.scenes, s => s.enabled), s => s.path),
            locationPathName = OutputPath,
            target = BuildTarget.WSAPlayer,
            options = BuildOptions.None
        };
        // El nombre visible en la consola se cambia solo durante la build: el APK y el .exe conservan el suyo.
        string previousName = PlayerSettings.productName;
        PlayerSettings.productName = DisplayName;
        BuildReport report;
        try { report = BuildPipeline.BuildPlayer(options); }
        finally { PlayerSettings.productName = previousName; }
        Debug.Log($"[BuildXbox] {report.summary.result} · {report.summary.totalTime}");
        if (report.summary.result != BuildResult.Succeeded && Application.isBatchMode)
            EditorApplication.Exit(1);
    }
}
