# PauseManager_Pop

- **Address:** `0x1400B4760`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `char sub_1400B4760(PauseManager *pm)`
- **Callers:** `sub_1400B467C`, `sub_1400B57FC`
- **Callees:** `sub_1400B47B4`, `sub_1400B4968`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Pops the top pause id and restores the previous pause (or unpauses).

## Behavior

- V: id = byte at `pm+20+depth`; clears that byte; depth--; `sub_1400B47B4(pm, id)` applies the id's "off" controls.
- V: if a new top exists, `sub_1400B4968(pm, newTop)` applies its "on" controls; otherwise sets the word at `g_CharaRenderer+153012` to 0.
- V: returns the depth after the pop.

## Notes

`sub_1400B47B4` also looks up the row and calls `sub_1401D6F9C(qword_143CD9DD8, row[+8], 0, ...)` when row dword +8 is non-zero, which is what removes the pause UI state.

## Open questions

None recorded.
