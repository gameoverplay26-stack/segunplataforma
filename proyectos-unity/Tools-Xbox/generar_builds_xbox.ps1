# Genera los paquetes UWP para mostrar los juegos en una Xbox en Developer Mode (demo local:
# sin tienda, sin nube). Por cada proyecto: certificado de prueba, build de Unity (solución de
# Visual Studio), msbuild en Master x64 y una carpeta lista para instalar desde el Device Portal.
# Uso (con Unity CERRADO para esos proyectos):
#   powershell -ExecutionPolicy Bypass -File proyectos-unity\Tools-Xbox\generar_builds_xbox.ps1
#   powershell -ExecutionPolicy Bypass -File proyectos-unity\Tools-Xbox\generar_builds_xbox.ps1 -Proyectos Asteroides-Xbox
# Requisitos: Unity 6000.3.11f1 con Universal Windows Platform Build Support; Visual Studio 2022 con
# "Desarrollo de la Plataforma universal de Windows", herramientas C++ de UWP (v143) y Windows SDK 10.0.19041 o posterior.
# Guía completa: diseno-plataformas/laboratorio-adaptacion/GUIA-XBOX-DOCENTE.md

param(
    [string[]]$Proyectos = @("Asteroides\asteroide-final", "2D-Platformer-Unity-v2", "Asteroides-Xbox", "2D-Platformer-Xbox"),
    [string]$Unity = "C:\Program Files\Unity\Hub\Editor\6000.3.11f1\Editor\Unity.exe",
    [string]$Configuracion = "Master"
)
$ErrorActionPreference = "Stop"
# Con -File, una lista "a,b" llega como un solo texto.
$Proyectos = $Proyectos | ForEach-Object { $_ -split "," } | ForEach-Object { $_.Trim() } | Where-Object { $_ }
$Base = Split-Path $PSScriptRoot -Parent
$Password = "unity-demo"   # mismo valor que BuildXbox.CertificatePassword
$Publisher = "CN=Catedra Diseno segun Plataforma"

& (Join-Path $PSScriptRoot "verificar_requisitos_xbox.ps1") -Unity $Unity
if ($LASTEXITCODE -ne 0) { throw "Faltan requisitos (ver la tabla de arriba). Se instalan con verificar_requisitos_xbox.ps1 -Instalar" }

$msbuild = & "${env:ProgramFiles(x86)}\Microsoft Visual Studio\Installer\vswhere.exe" -latest -products * `
    -requires Microsoft.Component.MSBuild -find "MSBuild\**\Bin\MSBuild.exe" | Select-Object -First 1
if (-not $msbuild) { throw "No se encontró MSBuild. Instalar Visual Studio 2022 con la carga de trabajo de UWP." }

function New-TestCertificate([string]$dir) {
    $pfx = Join-Path $dir "xbox-prueba.pfx"
    if (Test-Path $pfx) { return $pfx }
    New-Item -ItemType Directory -Force $dir | Out-Null
    # Certificado de firma de código (EKU 1.3.6.1.5.5.7.3.3) sin restricciones básicas, como pide el empaquetado MSIX.
    $cert = New-SelfSignedCertificate -Type Custom -Subject $Publisher -KeyUsage DigitalSignature `
        -FriendlyName "Catedra Xbox demo" -CertStoreLocation "Cert:\CurrentUser\My" `
        -TextExtension @("2.5.29.37={text}1.3.6.1.5.5.7.3.3", "2.5.29.19={text}")
    Export-PfxCertificate -Cert $cert -FilePath $pfx -Password (ConvertTo-SecureString $Password -AsPlainText -Force) | Out-Null
    Export-Certificate -Cert $cert -FilePath (Join-Path $dir "xbox-prueba.cer") | Out-Null
    Remove-Item $cert.PSPath
    Write-Host "   Certificado de prueba creado: $pfx"
    return $pfx
}

$resumen = @()
foreach ($rel in $Proyectos) {
    $proyecto = Join-Path $Base $rel
    $nombre = Split-Path $rel -Leaf
    if (-not (Test-Path (Join-Path $proyecto "ProjectSettings"))) { throw "No es un proyecto de Unity: $proyecto" }
    $logs = Join-Path $proyecto "Logs"
    New-Item -ItemType Directory -Force $logs | Out-Null
    Write-Host "== $nombre"

    $lock = Join-Path $proyecto "Temp\UnityLockfile"
    if (Test-Path $lock) {
        try { [IO.File]::Open($lock, 'Open', 'ReadWrite', 'None').Close() }
        catch { throw "Unity tiene abierto $nombre. Cerralo y volvé a correr el script." }
    }

    $pfx = New-TestCertificate (Join-Path $proyecto "Certificados")

    # 1) Unity: genera la solución de Visual Studio en Builds\UWP (BuildXbox.Build).
    $logUnity = Join-Path $logs "build-xbox.log"
    # Sin -Wait: en PowerShell 5.1 espera también a los descendientes, y la build UWP deja vivo
    # vctip.exe (telemetría de Visual C++). Se espera solo al proceso de Unity.
    $p = Start-Process -FilePath $Unity -PassThru -ArgumentList @(
        "-batchmode", "-nographics", "-projectPath", "`"$proyecto`"",
        "-buildTarget", "WindowsStoreApps", "-executeMethod", "BuildXbox.Build", "-quit", "-logFile", "`"$logUnity`"")
    $p.WaitForExit()
    $linea = Select-String -Path $logUnity -Pattern "\[BuildXbox\]" | Select-Object -Last 1
    Write-Host "   Unity: $($linea.Line)"
    if ($p.ExitCode -ne 0) { throw "La build de Unity de $nombre falló (código $($p.ExitCode)). Ver $logUnity" }

    # 2) msbuild: compila el C++ de IL2CPP y arma el paquete para instalación local (sideload).
    $sln = Get-ChildItem (Join-Path $proyecto "Builds\UWP") -Filter *.sln | Select-Object -First 1
    if (-not $sln) { throw "Unity no generó la solución en $proyecto\Builds\UWP" }
    $salida = Join-Path $proyecto "Builds\Xbox-Paquete\"
    if (Test-Path $salida) { Remove-Item -Recurse -Force $salida }
    $logMsbuild = Join-Path $logs "build-xbox-msbuild.log"
    & $msbuild $sln.FullName /m /nologo /verbosity:minimal "/flp:LogFile=$logMsbuild;Verbosity=normal" `
        /p:Configuration=$Configuracion /p:Platform=x64 /p:AppxBundle=Never `
        /p:UapAppxPackageBuildMode=SideloadOnly /p:AppxPackageSigningEnabled=true `
        "/p:PackageCertificateKeyFile=$pfx" "/p:PackageCertificatePassword=$Password" `
        "/p:AppxPackageDir=$salida"
    if ($LASTEXITCODE -ne 0) { throw "msbuild falló para $nombre (código $LASTEXITCODE). Ver $logMsbuild" }

    $paquete = Get-ChildItem $salida -Recurse -Include *.msix, *.appx |
        Where-Object { $_.FullName -notmatch "\\Dependencies\\" } | Select-Object -First 1
    if (-not $paquete) { throw "msbuild terminó sin generar el paquete de $nombre en $salida" }
    $resumen += "{0,-26} {1}  ({2:N1} MB)" -f $nombre, $paquete.FullName, ($paquete.Length / 1MB)
}

Write-Host ""
Write-Host "Listo. Instalar cada paquete desde el Device Portal de la Xbox (https://<IP-de-la-Xbox>:11443),"
Write-Host "agregando también los archivos de la carpeta Dependencies\x64 que está junto al paquete:"
$resumen | ForEach-Object { Write-Host "  $_" }
