; Instalador de PC del Match 3 UI Testing v2 (Inno Setup 6).
; Lo compila Tools/generar_builds.ps1 después de la build de Windows de Unity.
; Instala por usuario (sin permisos de administrador), con acceso directo y desinstalador.

#define AppName "Match 3 UI Testing"
#define AppVersion "2.0.0"
#define AppExe "Match3-UI-Testing.exe"

[Setup]
AppId={{3312ADDF-9C46-4284-856A-8D6BBC620396}
AppName={#AppName}
AppVersion={#AppVersion}
AppPublisher=Diseño según Plataformas de Juego (UNJu)
DefaultDirName={localappdata}\Programs\{#AppName}
DefaultGroupName={#AppName}
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
OutputDir=..\Builds\Instaladores
OutputBaseFilename=Match3-UI-Testing-Setup
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
