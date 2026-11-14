# Input_IsCtrlHeld

- **Address:** `0x140021F2C`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `char sub_140021F2C(__int64 ctx)`
- **Callers:** `sub_140021A90` (text-edit key handler, four sites), a vtable at `0x143D26AB8`
- **Callees:** GetKeyState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns true when Ctrl is held **and** Shift is not, no Windows key is down, and a pad state bit is clear. Used by the text-edit box for Ctrl+A/C/V/X.

## Behavior

- V: `(GetKeyState(17) & 0x80) == 0` -> 0; `(GetKeyState(16) & 0x80) != 0` -> 0.
- V: `GetKeyState(91)` or `GetKeyState(92)` (left/right Windows key) down -> 0.
- V: returns 0 when bit 0x20000000 of the dword reached through the context's pointer at +16 (three levels of indirection) is set (a pad/UI state that suppresses text shortcuts).
- V: otherwise 1.

## Notes

This is **not** the gameplay Ctrl fast-forward path: its callers are the name-entry editor (`sub_140021A90`), and gameplay reads Ctrl from the action state built by `Input_TranslateMessage`. The sibling `0x140021F9C` is the same test for Shift, `0x14002200C` for no modifier.

## Open questions

? the meaning of the 0x20000000 bit in the ctx object.
