# Verifica que esta PC tenga todo lo necesario para generar los paquetes UWP de la demo en Xbox:
# lo mismo que se instaló en la PC de la cátedra el 2026-10-26 (ver PORTEO-XBOX.md §5).
# Uso:
#   powershell -ExecutionPolicy Bypass -File proyectos-unity\Tools-Xbox\verificar_requisitos_xbox.ps1
#   ... -Instalar      # además instala lo que falte de Visual Studio (pide permisos de administrador)
# Código de salida: 0 si está todo, 1 si falta algo. generar_builds_xbox.ps1 lo corre antes de compilar.

param(
    [string]$Unity = "C:\Program Files\Unity\Hub\Editor\6000.3.11f1\Editor\Unity.exe",
    [switch]$Instalar
)
$ErrorActionPreference = "Stop"
$Base = Split-Path $PSScriptRoot -Parent
$SdkMinimo = [version]"10.0.19041.0"
$resultados = @()
function Add-Resultado([string]$que, [bool]$ok, [string]$detalle, [string]$solucion) {
    $script:resultados += [pscustomobject]@{ Estado = $(if ($ok) { "OK" } else { "FALTA" }); Requisito = $que; Detalle = $detalle; Solucion = $(if ($ok) { "" } else { $solucion }) }
}

# 1) Unity 6000.3.11f1 con el módulo de Universal Windows Platform
$unityOk = Test-Path $Unity
Add-Resultado "Unity 6000.3.11f1" $unityOk $Unity "Instalar 6000.3.11f1 desde Unity Hub (no otra versión), o pasar -Unity con la ruta de Unity.exe"
$uwp = if ($unityOk) { Join-Path (Split-Path $Unity -Parent) "Data\PlaybackEngines\MetroSupport" } else { "" }
Add-Resultado "Módulo UWP de Unity" ($unityOk -and (Test-Path $uwp)) "PlaybackEngines\MetroSupport" "Unity Hub → Installs → 6000.3.11f1 → ⚙ → Add modules → Universal Windows Platform Build Support"

# 2) Visual Studio 2022 y sus componentes de UWP
$vswhere = "${env:ProgramFiles(x86)}\Microsoft Visual Studio\Installer\vswhere.exe"
$vsPath = $null
if (Test-Path $vswhere) { $vsPath = & $vswhere -latest -products * -version "[17.0,18.0)" -property installationPath }
Add-Resultado "Visual Studio 2022" ([bool]$vsPath) "$vsPath" "Instalar Visual Studio 2022 (Community alcanza): https://visualstudio.microsoft.com/"
$componentes = [ordered]@{
    "Microsoft.VisualStudio.Workload.Universal"           = "Carga de trabajo: Desarrollo de la Plataforma universal de Windows"
    "Microsoft.VisualStudio.ComponentGroup.UWP.VC"        = "Herramientas de C++ para UWP (IL2CPP genera C++)"
    "Microsoft.VisualStudio.Component.VC.Tools.x86.x64"   = "Compilador de C++ x64/x86 (v143)"
}
$faltanVs = @()
foreach ($id in $componentes.Keys) {
    $tiene = $false
    if ($vsPath) { $tiene = [bool](& $vswhere -latest -products * -version "[17.0,18.0)" -requires $id -property installationPath) }
    if (-not $tiene) { $faltanVs += $id }
    Add-Resultado $componentes[$id] $tiene $id "Visual Studio Installer → Modificar, o correr este script con -Instalar"
}
$msbuild = if ($vsPath) { & $vswhere -latest -products * -requires Microsoft.Component.MSBuild -find "MSBuild\**\Bin\MSBuild.exe" | Select-Object -First 1 } else { $null }
Add-Resultado "MSBuild" ([bool]$msbuild) "$msbuild" "Viene con Visual Studio 2022"

# 3) Windows SDK 10.0.19041 o posterior (sin él, Unity no genera UWP: 'Could not find any supported UWP SDK')
$kits = "${env:ProgramFiles(x86)}\Windows Kits\10\Include"
$sdks = @()
if (Test-Path $kits) { $sdks = Get-ChildItem $kits -Directory | ForEach-Object { try { [version]$_.Name } catch { } } | Where-Object { $_ -ge $SdkMinimo } | Sort-Object -Descending }
if (-not $sdks) { $faltanVs += "Microsoft.VisualStudio.Component.Windows11SDK.26100" }
Add-Resultado "Windows SDK $SdkMinimo o posterior" ([bool]$sdks) ($(if ($sdks) { "Instalados: " + ($sdks -join ", ") } else { "Ninguno en $kits" })) "Visual Studio Installer → Componentes individuales → Windows 11 SDK (10.0.26100), o -Instalar"

# 4) Proyectos, script de build y ruta corta
foreach ($p in "Asteroides\asteroide-final", "2D-Platformer-Unity-v2", "Asteroides-Xbox", "2D-Platformer-Xbox") {
    $build = Join-Path $Base "$p\Assets\Editor\BuildXbox.cs"
    Add-Resultado "Proyecto $p" (Test-Path $build) $build "git pull (el proyecto o BuildXbox.cs no está en esta copia del repo)"
}
# Rutas largas (ENV-01). Medido el 2026-10-26 en la PC de la cátedra: la ruta más larga dentro de los proyectos
# (fuera de Builds/) mide 226 caracteres desde proyectos-unity (Library\PackageCache del Platformer).
# Sin rutas largas de Windows, la base tiene que medir 34 caracteres o menos para no pasar de 260.
$largoMaximo = 226
$rutasLargas = (Get-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name LongPathsEnabled -ErrorAction SilentlyContinue).LongPathsEnabled -eq 1
$total = $Base.Length + $largoMaximo
Add-Resultado "Rutas largas (ENV-01)" ($rutasLargas -or $total -le 260) "LongPathsEnabled = $([int]$rutasLargas); ruta más larga estimada: $total caracteres" "Como administrador: reg add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f (y reiniciar), o acortar la base: subst P: `"$Base`" y correr desde P:\Tools-Xbox"

# 5) Certificado de prueba (lo crea el script de build con New-SelfSignedCertificate)
Add-Resultado "Crear certificados de prueba" ([bool](Get-Command New-SelfSignedCertificate -ErrorAction SilentlyContinue)) "Módulo PKI de Windows" "Usar Windows PowerShell 5.1 en Windows 10 u 11"

$resultados | Format-Table -AutoSize -Wrap Estado, Requisito, Detalle, Solucion
$faltan = @($resultados | Where-Object { $_.Estado -eq "FALTA" })

if ($Instalar -and $faltanVs.Count -gt 0) {
    if (-not $vsPath) { throw "Primero hay que instalar Visual Studio 2022; después volver a correr con -Instalar." }
    Write-Host "Instalando en Visual Studio: $($faltanVs -join ', ')  (pide permisos de administrador; descarga varios GB)"
    $argumentos = @("modify", "--installPath", "`"$vsPath`"") + ($faltanVs | ForEach-Object { "--add", $_ }) + @("--passive", "--norestart")
    $p = Start-Process -FilePath "${env:ProgramFiles(x86)}\Microsoft Visual Studio\Installer\setup.exe" -ArgumentList $argumentos -Verb RunAs -PassThru
    $p.WaitForExit()
    Write-Host "Instalador de Visual Studio: código $($p.ExitCode). Volvé a correr la verificación."
    exit $p.ExitCode
}

if ($faltan.Count -gt 0) {
    Write-Host "Faltan $($faltan.Count) requisito(s). Lo de Visual Studio se instala con: ... verificar_requisitos_xbox.ps1 -Instalar"
    exit 1
}
Write-Host "Todo listo para generar los paquetes: generar_builds_xbox.ps1"
exit 0
