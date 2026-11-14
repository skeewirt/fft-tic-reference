# App_ProcessMessages

- **Address:** `0x14002F728`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `char __fastcall App_ProcessMessages(void *windowObject)`
- **Callers:** Game_Main (0x14002BE65)
- **Callees:** sub_14002FB14, Time_GetTimestamp, PeekMessageW, TranslateMessage, DispatchMessageW

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Drains up to ten Win32 messages per call. Returns 1 while the application should continue, and 0 after a WM_QUIT, storing the quit code in `windowObject+64`.

## Behavior

- V: calls `sub_14002FB14` first; that helper compares the foreground window and clips/releases the mouse cursor.
- V: reads `Time_GetTimestamp` once before the message loop.
- V: loops at most ten times: `PeekMessageW(&msg, NULL, 0, 0, 0)` with no remove; if there is no message, returns 1.
- V: message 18 (WM_QUIT) stores `msg.wParam` at `windowObject+64` and returns 0.
- V: otherwise removes the message with `PeekMessageW(..., PM_REMOVE)`, calls `TranslateMessage` and `DispatchMessageW`.
- V: after each message compares `Time_GetTimestamp` with the starting value; a delta of 300000 (one second in 1/300000-unit ticks) returns 1.
- V: the ten-message cap and the one-second budget prevent the message pump from starving the frame loop.

## State touched

- Calls: [Time_GetTimestamp](Time_GetTimestamp.md)

## Referenced by

- Called by: [Game_Main](Game_Main.md)

## Notes

The return value is used directly as the second condition of Game_Main's loop; 0 means quit.

## Open questions

The fields of the window object other than +64 and the exact clip-cursor conditions in sub_14002FB14.
