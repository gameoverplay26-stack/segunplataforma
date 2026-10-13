using NUnit.Framework;
using UnityEditor;
using UnityEditor.Build;

// La configuración de plataforma también se prueba (actividad A4.8, Unidad 4).
// Lee los Player Settings del proyecto: si un Build Profile tiene
// Player Settings propios, esos valores no se ven acá.
public class AndroidBuildConfigTests
{
    private static readonly NamedBuildTarget Android = NamedBuildTarget.Android;

    [Test]
    public void ScriptingBackend_EsIL2CPP()
    {
        // ARM64 solo se habilita con IL2CPP
        var backend = PlayerSettings.GetScriptingBackend(Android);
        Assert.AreEqual(ScriptingImplementation.IL2CPP, backend);
    }

    [Test]
    public void Arquitecturas_IncluyenARM64()
    {
        // Hay teléfonos que solo aceptan apps de 64 bits
        var arqs = PlayerSettings.Android.targetArchitectures;
        Assert.IsTrue((arqs & AndroidArchitecture.ARM64) != 0);
    }

    [Test]
    public void ApiMinima_EsAlMenos25()
    {
        // Unity 6.3 soporta Android 7.1 (API 25) o superior
        Assert.GreaterOrEqual((int)PlayerSettings.Android.minSdkVersion, 25);
    }

    [Test]
    public void Build_GeneraApkYNoAab()
    {
        // Para instalar a mano hace falta un .apk
        Assert.IsFalse(EditorUserBuildSettings.buildAppBundle);
    }
}
