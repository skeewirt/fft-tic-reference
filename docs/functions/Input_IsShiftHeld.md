# Input_IsShiftHeld

- **Address:** `0x140021F9C`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `char sub_140021F9C(__int64 ctx)`
- **Callers:** `sub_140021A90` (text-edit key handler, four sites), a vtable at `0x143D26AC4`
- **Callees:** GetKeyState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns true when Shift is held and Ctrl is not, no Windows key is down, and the ctx pad bit is clear.

## Behavior

- V: `(GetKeyState(16) & 0x80) == 0` -> 0; `(GetKeyState(17) & 0x80) != 0` -> 0.
- V: Windows keys 91/92 down -> 0; ctx bit 0x20000000 set -> 0; otherwise 1.

## Notes

Text-editor modifier test only, like `Input_IsCtrlHeld`. The gameplay effect of Shift was not found in code (see `docs/reference/battle-ui-state.md` section 2.3).

## Open questions

? the gameplay Shift consumer.
