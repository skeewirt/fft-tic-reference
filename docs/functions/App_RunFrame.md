# App_RunFrame

- **Address:** `0x14002A1F0`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `bool __fastcall App_RunFrame(void *app)`
- **Callers:** Game_Main (0x14002BE57, 0x14002BE88), sub_14002C7D4
- **Callees:** sub_140014CF4, Time_GetTimestamp, IsDebuggerPresent, Debug_DetectCaptureTools, SteamAPI_RunCallbacks, sub_14006CEF0, sub_140018A2C, sub_14001CA40, sub_14001F9D8, sub_14001D038, sub_14001F2E4, sub_14001DAAC, sub_14001CC30, sub_1400206FC, sub_140087C50, sub_140087ECC, sub_14001B578, sub_140088280, sub_1400914EC, sub_14009B6B8, sub_1400A53D0, sub_1400AD00C, sub_140032A20

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

One iteration of the game's application loop: frame pacing, the debug/capture gate, Steam callbacks, the UI/render/audio update chain and the secondary frame-rate wait. `Game_Main` calls it in a loop until the window closes.

## Behavior

- V: when `qword_140C69718` is non-null, calls `sub_140014CF4` first.
- V: calls the vtable slots at `app+1152` (+48) and `app+1176` (+64) before timing the frame.
- V: frame limiter: reads `Time_GetTimestamp`, compares the elapsed value against 1/60 s, calls `SleepEx(10)` when the frame is more than 10 ms early, and loops until the elapsed value reaches 1/60 s. The accepted timestamp is stored in `g_FrameTimestamp` (`qword_143CD9B68`).
- V: increments the frame counter at `app+1184`.
- V: debug/capture gate at `0x14002A342`: `IsDebuggerPresent()` true, or a non-null `qword_140C696A8` with `Debug_DetectCaptureTools()` returning 1, sets `app+1520 = 1` and jumps past the normal update block. `app+1520` is therefore a 'suppress the game update' flag (I).
- V: when `app+24` is non-zero, adds the last frame duration at `app+16`; every 30,000 units it calls `SteamAPI_RunCallbacks` and subtracts 30,000.
- V: when `qword_143CD9B90+2304` is set, calls `sub_14006CEF0` and `sub_140018A2C`, performs an address/foreground check, and signals the event at `qword_143CD9B90+2272`.
- V: when `app+430` differs from `app+945`, calls the vtable slot at `app+1152` (+88), then stores `app+430` into `app+945`.
- V: the update block (target `LABEL_42`) computes the frame delta in milliseconds and drives the UI/render object at `qword_140C69680+8`: `sub_14001CA40`, the object's vtable calls, `sub_14001F9D8`, `sub_14001D038`, `sub_14001F2E4`, the transform copies, `sub_14001DAAC`, `sub_14001CC30`, then a ten-entry subsystem update loop (32-byte stride). It finishes with `sub_1400206FC`, vtable cleanup calls, `sub_140087C50`, `sub_140087ECC`, `sub_14001B578`, `sub_140088280`, `sub_1400914EC`, `sub_14009B6B8`, `sub_1400A53D0`, `sub_1400AD00C` and `sub_140032A20`.
- V: when `app+1192` is non-zero, computes a target interval of `300000 / fps` and spins with `Sleep(0)` until `Time_GetTimestamp` reaches it (a second frame-rate cap).
- V: calls `GetActiveWindow`; when it differs from `app+928`, walks the window list at `app+864` and updates the active-window bookkeeping.
- I: the function returns the loop's continue/stop state to `Game_Main`; the exact final expression was not needed to document the update path.

## State touched

- Calls: [Time_GetTimestamp](Time_GetTimestamp.md), [Debug_DetectCaptureTools](Debug_DetectCaptureTools.md)
- Reads: [g_Application](../globals/g_Application.md), [g_FrameTimestamp](../globals/g_FrameTimestamp.md), [g_RenderDevice](../globals/g_RenderDevice.md)
- Writes: [g_FrameTimestamp](../globals/g_FrameTimestamp.md)

## Referenced by

- Appears in flows: [ApplicationLifecycle](../flows/ApplicationLifecycle.md)
- Called by: [Game_Main](Game_Main.md)
- Observed behaviours: [QuitLoopExit](../behaviors/QuitLoopExit.md), [QuitRequest](../behaviors/QuitRequest.md)

## Notes

The 1/60 s target is a floating-point constant in the limiter. `g_FrameTimestamp` is in 1/300000-second units (the same unit returned by Time_GetTimestamp and divided by 300000 in this function to get seconds). The debug/capture gate is the path that makes the game stop updating when an external debugger or a graphics capture layer is present.

## Open questions

The exact meaning of `app+1520` beyond 'skip the update', and whether the second frame cap at `app+1192` is a user setting or a mode.
