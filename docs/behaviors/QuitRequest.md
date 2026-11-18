# QuitRequest

- **Kind:** observed behaviour
- **Scope:** how the game ends itself or hands over to the Classic executable
- **Area:** [Application and startup](../areas/app-startup.md)
- **Affects:** [g_Application](../globals/g_Application.md), [App_LaunchClassic](../functions/App_LaunchClassic.md), [UIAgentFFTOSystem_StateExitGame](../functions/UIAgentFFTOSystem_StateExitGame.md), [App_RunFrame](../functions/App_RunFrame.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The quit request byte of the application object and every path that sets it.

## Behavior

- V: `g_Application` (0x140C6AD30) +1520 (byte) is the quit request. Set to 1 by `App_LaunchClassic` (after starting the Classic exe), by `UILauncher_Update` when its exit fade ends, by `UIAgentFFTOSystem_StateExitGame` (a dialog's answer, event 2), and by `App_RunFrame` (0x14002A442) when `IsDebuggerPresent()` is true or `Debug_DetectCaptureTools` reports a capture tool.
- I: the main loop ends on it (every exit path writes it; the reader was not traced).

## Open questions

None recorded.
