# Genera las dos builds del 2D Platformer v2: APK de Android e instalador de PC (Windows).
# Uso (con Unity CERRADO para este proyecto):
#   powershell -ExecutionPolicy Bypass -File Tools\generar_builds.ps1
# Requisitos: Unity 6000.3.11f1 con Android y Windows Build Support; Inno Setup 6 (winget install JRSoftware.InnoSetup).
# Se trabaja desde la ruta corta (junction) por el límite de 260 caracteres de Windows (ENV-01).

param(
    [string]$Proyecto = "C:\Developer\unity\Platformer-v2",
    [string]$Unity = "C:\Program Files\Unity\Hub\Editor\6000.3.11f1\Editor\Unity.exe",
    [string]$Logs = ""
)
$ErrorActionPreference = "Stop"
if (-not $Logs) { $Logs = Join-Path $Proyecto "Logs" }
New-Item -ItemType Directory -Force $Logs | Out-Null

$iscc = @("$env:LOCALAPPDATA\Programs\Inno Setup 6\ISCC.exe",
          "${env:ProgramFiles(x86)}\Inno Setup 6\ISCC.exe",
          "$env:ProgramFiles\Inno Setup 6\ISCC.exe") | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $iscc) { throw "No se encontró Inno Setup 6 (ISCC.exe). Instalar: winget install JRSoftware.InnoSetup" }
if (Test-Path (Join-Path $Proyecto "Temp\UnityLockfile")) {
    try { [IO.File]::Open((Join-Path $Proyecto "Temp\UnityLockfile"), 'Open', 'ReadWrite', 'None').Close() }
    catch { throw "Unity tiene el proyecto abierto. Cerralo y volvé a correr el script." }
}

function Invoke-Unity([string]$target, [string]$method, [string]$log) {
    Write-Host "== $method ($target)"
    $p = Start-Process -FilePath $Unity -Wait -PassThru -ArgumentList @(
        "-batchmode", "-nographics", "-projectPath", "`"$Proyecto`"",
        "-buildTarget", $target, "-executeMethod", $method, "-quit", "-logFile", "`"$log`"")
    $line = Select-String -Path $log -Pattern "\[Build(Android|Windows)\]" | Select-Object -Last 1
    Write-Host "   $($line.Line)"
    if ($p.ExitCode -ne 0) { throw "$method falló (código $($p.ExitCode)). Ver $log" }
}

Invoke-Unity "Android" "BuildAndroid.Build" (Join-Path $Logs "build-android.log")
Invoke-Unity "Win64" "BuildWindows.Build" (Join-Path $Logs "build-windows.log")

Write-Host "== Instalador (Inno Setup)"
& $iscc /Q (Join-Path $Proyecto "Tools\instalador-windows.iss")
if ($LASTEXITCODE -ne 0) { throw "Inno Setup falló (código $LASTEXITCODE)" }

Write-Host ""
Write-Host "Listo:"
Get-Item (Join-Path $Proyecto "Builds\Platformer-v2.apk"), (Join-Path $Proyecto "Builds\Instaladores\Platformer-v2-Setup.exe") |
    ForEach-Object { "  {0}  ({1:N1} MB)" -f $_.FullName, ($_.Length / 1MB) }
