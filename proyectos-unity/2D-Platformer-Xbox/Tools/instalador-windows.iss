; Instalador de PC del 2D Platformer v2 (Inno Setup 6).
; Lo compila Tools/generar_builds.ps1 después de la build de Windows de Unity.
; Instala por usuario (sin permisos de administrador), con acceso directo y desinstalador.

#define AppName "2D Platformer v2"
#define AppVersion "2.0.0"
#define AppExe "Platformer-v2.exe"

[Setup]
AppId={{8C1B6F2E-4D7A-4C2B-9E31-6A0F2D5B7C91}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher=Diseño según Plataformas de Juego (UNJu)
DefaultDirName={localappdata}\Programs\{#AppName}
DefaultGroupName={#AppName}
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
OutputDir=..\Builds\Instaladores
OutputBaseFilename=Platformer-v2-Setup
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\{#AppExe}

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"

[Files]
; Toda la build de Unity, salvo la carpeta de depuración de Burst (no se distribuye).
Source: "..\Builds\Windows\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Excludes: "*_BurstDebugInformation_DoNotShip\*"

[Icons]
Name: "{group}\{#AppName}"; Filename: "{app}\{#AppExe}"
Name: "{group}\Desinstalar {#AppName}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#AppName}"; Filename: "{app}\{#AppExe}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#AppExe}"; Description: "{cm:LaunchProgram,{#AppName}}"; Flags: nowait postinstall skipifsilent
