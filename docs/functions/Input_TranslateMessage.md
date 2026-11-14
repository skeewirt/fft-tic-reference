# Input_TranslateMessage

- **Address:** `0x14001EC2C`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `__int64 sub_14001EC2C(Input *in, __int64 unused, UINT msg, WPARAM wParam, LPARAM lParam)`
- **Callers:** `sub_14001EBD0` (window subclass proc)
- **Callees:** `sub_14001EF64`, `sub_14001F040`, `sub_14001CE68`, `sub_14001CEF4`, `sub_14001F0A4`, `sub_14001EE74`, GetAsyncKeyState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Turns game-window messages into the input object's action queue: keyboard press/release, characters, focus changes and keyboard-layout refresh.

## Behavior

- V: WM_KEYDOWN (0x100) and WM_SYSKEYDOWN (0x104) call `sub_14001EF64(in, wParam)` (the press path); WM_KEYUP (0x101) and WM_SYSKEYUP (0x105) call `sub_14001F040` (the release path).
- V: WM_CHAR (0x102) and WM_SYSCHAR (0x106) queue a type-3 record whose payload is the character; keys >= 0x80 are dropped.
- V: WM_ACTIVATE (0x006) with a zero low word clears every action (loop 0..0xA0 via `sub_14001F040`); with a non-zero low word it calls the input object's vtable +56 (device reset). Mode 2 (`wParam` high word) resyncs three keys taken from `unk_1406FA248` with GetAsyncKeyState.
- V: WM_ENTERMENULOOP/WM_ENTERSIZEMOVE (0x211/0x231) clear every action; WM_MOUSEACTIVATE (0x1A) calls `sub_14001EE74`; WM_NCACTIVATE (0x51) falls through to the layout refresh.
- V: after the keyboard cases it calls `sub_14001F0A4`, which reads `GetKeyboardLayoutNameA` and stores the layout id at in+1832.
- V: the virtual-key -> action id map is `byte_14065CE00`; Ctrl (0x11) -> 17, Shift (0x10) -> 16, Space (0x20) -> 32, Esc (0x1B) -> 27.

## Notes

The function is reached for every window message via the subclass proc `sub_14001EBD0`. It is not the main WndProc; `Input_WindowSubclassProc` handles the mouse messages on the same window.

## Open questions

? what the three key codes in `unk_1406FA248` are (read live, or dump the data); ? why the focus-loss path uses 0x51.
