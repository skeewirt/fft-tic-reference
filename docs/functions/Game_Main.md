# Game_Main

- **Address:** `0x14002BD50`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall Game_Main(unsigned int argc, __int64 argv, __int64 winMainParams)`
- **Callers:** WinMain (0x140010F19)
- **Callees:** IsDebuggerPresent, Startup_SetDataDirectory, sub_14002C1FC, sub_14002C2EC, sub_14002BF70, sub_140026B3C, sub_14002C700, App_RunFrame, App_ProcessMessages, sub_14002F3E0, sub_14002C0BC, sub_14002C6D8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The game's WinMain body: it rejects a debugger at startup, sets the working directory, creates the splash/window objects, runs the application loop until exit, and tears the objects down.

## Behavior

- V: first action is `IsDebuggerPresent()` at `0x14002BD87`; when true the function returns 0 immediately, before any game object is created.
- V: calls `Startup_SetDataDirectory` (`sub_14002EA04`) so the process working directory contains `data`.
- V: zeroes a 0x118-byte configuration block (`sub_14002C1FC`, `sub_14002C2EC`) and a 0x48-byte window object, then installs the `faith::Framework::SplashWindow_1406FB050` and `faith::Framework::Window_1406FB0C8` vtables; `qword_140C69D28` points at the window object.
- V: `sub_14002BF70` creates the application/window; when it fails, `sub_140026B3C` supplies the error code.
- V: `sub_14002C700` initializes the application. On success it runs `while (App_RunFrame(qword_140C6AD30) && App_ProcessMessages(&windowObject))`.
- V: after the loop, calls vtable slot +24 on the application, then pumps `App_RunFrame` in a do/while that also calls the vtable slot +80 on `app+1152` and checks three subsystem counters plus the event flag at `qword_140C69698+392`.
- V: teardown calls `sub_14002F3E0`, the allocator vtable slot +24, clears `qword_143CD9B58`, then `sub_14002C0BC` and `sub_14002C6D8`; the final return code comes from the application result or `sub_140026B3C`.

## State touched

- Calls: [Startup_SetDataDirectory](Startup_SetDataDirectory.md), [App_RunFrame](App_RunFrame.md), [App_ProcessMessages](App_ProcessMessages.md)
- Reads: [g_Application](../globals/g_Application.md)

## Referenced by

- Observed behaviours: [QuitLoopExit](../behaviors/QuitLoopExit.md)

## Notes

The startup check is why a debugger attached before the process reaches this point causes the game to return 0 without a window. The same check exists in the frame loop, but only as the capture/debug gate inside App_RunFrame.

## Open questions

The exact error-code mapping from `sub_140026B3C` and which of the three teardown counters can keep the pump running.
