# PauseManager_Tick

- **Address:** `0x1400B467C`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `__int64 sub_1400B467C(PauseManager *pm, ...)`
- **Callers:** `sub_1400B57FC` and the update functions of ~15 other managers
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, `sub_1400B4760`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Ticks the pause overlay: when a pause is on the stack, loads its duration from NXD table 282 into the remaining-time float.

## Behavior

- V: depth `pm+23` == 0 -> return.
- V: id = byte at `pm+20+depth`; 0 -> return.
- V: row = NXD table 282 row `id`; missing row or zero dword at row+4 -> `sub_1400B4760(pm)` (pop).
- V: otherwise `*(float*)(pm+16) = (float)row[+4] / 1000.0` (milliseconds -> seconds).

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [EventControl_PausedTick](EventControl_PausedTick.md)

## Notes

Called at the top of every manager update, so a paused game still ticks the overlay but skips the manager work (the managers return early); `sub_1400B57FC` is the clearest example.

## Open questions

? whether a row with duration 0 means "wait for input" rather than "no pause".
