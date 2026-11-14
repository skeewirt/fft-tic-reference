# Input_WindowSubclassProc

- **Address:** `0x14001F4B8`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `LRESULT Input_WindowSubclassProc(HWND hWnd, UINT msg, WPARAM wParam, LPARAM lParam, UINT_PTR id, DWORD_PTR input)`
- **Callers:** sub_14001F174, sub_14001F298 (installed as the subclass callback)
- **Callees:** DefSubclassProc, sub_14001CEF4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Window subclass procedure of the game window: turns mouse, keyboard and focus messages into flags and counters on the input object (`input` is the reference data).

## Behavior

- V: WM_MOUSEWHEEL (0x20A) adds the signed high word of wParam to the input object's wheel counter at +92; Input_PollCursor later divides it by 120.
- V: message 0x209 (middle double-click) ORs bit 2 into the words at +40 and +48, and 0x20D (X-button up) ORs 8 or 16 by the button in the high word; message 6 (WM_ACTIVATE) with a zero low word falls into a path that calls sub_14001CEF4 on the input object.
- V: every case ends in DefSubclassProc.
- I: installed as a subclass callback from sub_14001F174 / sub_14001F298 (code references to its address); the SetWindowSubclass call itself was not read.

## Notes

See Input_PollCursor for what consumes the wheel counter.

## Open questions

None recorded.
