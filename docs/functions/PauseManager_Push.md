# PauseManager_Push

- **Address:** `0x1400B4618`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `__int64 sub_1400B4618(PauseManager *pm, unsigned id)`
- **Callers:** `sub_1400EB0A4`, `sub_1400EB228`, `sub_140101D0C`, `sub_140122A14`, `sub_140134EC8`, `sub_14014129C`, `sub_140142398`, `sub_140143EA8`, `sub_14014A57C`, `sub_14014A870`, `sub_1401A9000`, `sub_1401DBC24`, `sub_1402037A0`
- **Callees:** `sub_1400B47B4`, `sub_1400B4968`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Pushes a pause id onto the PauseManager's small stack (max depth 3), applying the previous top's "off" controls and the new top's "on" controls.

## Behavior

- V: depth = byte at pm+23; `depth+1 >= 3` returns without pushing.
- V: depth != 0: re-applies the current top (`sub_1400B47B4(pm, topId)`); depth == 0: sets the word at `g_CharaRenderer+153012` to 1.
- V: increments the depth, stores the id at `pm+20+depth`, then calls `sub_1400B4968(pm, id)`.

## Referenced by

- Called by: [EventControl_TryOpenPause](EventControl_TryOpenPause.md), [Guide_OpenWindow](Guide_OpenWindow.md)

## Notes

`sub_1400B4968` reads NXD table 282 row `id` and writes the row's 8 control bytes at `+16..+23` through `sub_1400B4894`, plus the row dword `+8` through `sub_1401D6F9C(qword_143CD9DD8, value, 1)`. The top id gates input (see `Input_TestAction`).

## Open questions

? the meaning of `g_CharaRenderer+153012`; ? the NXD 282 row contents.
