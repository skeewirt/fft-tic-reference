# Input_PollCursor

- **Address:** `0x14001F664`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `void Input_PollCursor(InputState *in)`
- **Callers:** sub_14001F2E4 (input frame update)
- **Callees:** GetCursorPos, ScreenToClient

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads the mouse: drains the mouse device's relative axes (wheel +24, deltas +28/+32) and stores the client-space cursor position.

## Behavior

- V: GetCursorPos then ScreenToClient(window) into in+16 (x) and in+20 (y), whole window pixels; wheel in notches of 120 into in+24.

## Notes

The 48-byte state Input_Update fills is broadcast to the UI listeners; the UI core copies x/y into g_GUICore+1880/+1884.

## Open questions

None recorded.
