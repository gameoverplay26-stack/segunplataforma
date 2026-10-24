# Match 3 UI Testing v2

Copia migrada a **Unity 6000.3.11f1** del proyecto *starter* del tutorial de Kodeco "Unity UI testing" (Match 3, original en Unity 2019.4.21f1). El original quedó sin tocar en `proyectos-unity/unity-ui-testing-tutorial-main/`.

## Qué se cambió (2026-10-24)

- `Packages/manifest.json`: se quitaron `collab-proxy` 1.x, `ide.vscode`, `toolchain.linux-x86_64` y `textmeshpro` (ningún asset lo usa; en Unity 6 está dentro de `ugui` 2.0). Se actualizaron Input System 1.19.0, Test Framework 1.6.0, uGUI 2.0.0, Timeline 1.8.11 e IDEs.
- Se borraron dos escenas temporales del Test Runner (`InitTestScene*.unity`) y los `.DS_Store`.
- **Tests nuevos** (`Assets/Match 3 Starter/Tests/GameFlowTests.cs`, Play Mode, integración): el starter no traía ninguno. Recorren el flujo real con los botones de la UI.
- **Builds**: `Assets/Editor/BuildPlayers.cs` (Android IL2CPP + ARM64 y Windows 64 bits), `Tools/instalador-windows.iss` (Inno Setup 6) y `Tools/generar_builds.ps1`.
- No se modificó el código del juego ni las escenas.

## Evidencia

| Qué | Resultado | Evidencia |
|---|---|---|
| Importación y compilación en 6000.3.11f1 | Sin errores `CS` | `Logs/import.log` |
| Tests Play Mode | **5/5 propios PASS** (+2 del paquete Input System PASS, 2 omitidos por el paquete) | `Logs/evidencia/playmode-results.xml` |
| Build Android | `Succeeded`, APK 23,6 MB con `lib/arm64-v8a/libil2cpp.so` | `Logs/build-android.log` |
| Build Windows | `Succeeded` | `Logs/build-windows.log` |
| Instalador | `Builds/Instaladores/Match3-UI-Testing-Setup.exe` (27,3 MB) | salida de `generar_builds.ps1` |
| Arranque del `.exe` | Proceso vivo a los 8 s, sin excepciones en el log | `Logs/evidencia/player-smoke.log` |
| Prueba en un teléfono real y jugando con mouse en PC | **UNKNOWN** (no se ejecutó de forma interactiva) | — |

`Logs/` y `Builds/` no se versionan.

Tests:

1. `PlayButton_LoadsGameScene_WithFiveMoves`: Play carga `Game` con 5 movimientos y 0 puntos.
2. `RandomBoard_HasNoInitialMatches`: el tablero aleatorio no trae tríos armados.
3. `SwapWithoutMatch_SpendsOneMove_AndKeepsScore`: un intercambio sin trío gasta un movimiento.
4. `SwapCreatingTwoMatchesOfThree_Adds300Points`: dos tríos suman 300 puntos.
5. `FiveMoves_ShowGameOverPanel`: al quinto movimiento aparece el panel de Game Over.

## Cómo regenerar

Abrir siempre desde la ruta corta (junction `C:\Developer\unity\Match3-v2` → esta carpeta), por el límite de 260 caracteres (ENV-01). Con Unity **cerrado**:

```powershell
powershell -ExecutionPolicy Bypass -File C:\Developer\unity\Match3-v2\Tools\generar_builds.ps1
```

Tests:

```bash
"C:/Program Files/Unity/Hub/Editor/6000.3.11f1/Editor/Unity.exe" -batchmode -nographics \
  -projectPath "C:/Developer/unity/Match3-v2" -runTests -testPlatform PlayMode \
  -testResults "C:/Developer/unity/Match3-v2/Logs/evidencia/playmode-results.xml" \
  -logFile "C:/Developer/unity/Match3-v2/Logs/evidencia/playmode.log"
```

## Licencia

Código de Razeware LLC (Kodeco) con licencia de tipo MIT en el encabezado de cada script. Uso para clase.
