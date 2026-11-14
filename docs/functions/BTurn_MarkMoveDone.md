# BTurn_MarkMoveDone

- **Address:** `0x140310548`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int __fastcall BTurn_MarkMoveDone(int slot, int moved, int ended)`
- **Callers:** `sub_140206CE8`, `sub_14020A7F0`, `sub_14020AD64` (`0x14020AF17`, the Wait branch), `sub_140210AF0`
- **Callees:** `BTurn_IsUnitDone`, `BTurn_FinishUnit`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Records that a unit has finished its move (and/or given up its action) and ends the turn when everything required
is done.

## Behavior

- V: an empty slot (`unit[1] == 0xFF`) returns `-1`.
- V: `moved != 0` sets bit 0 of `unit[0x1B9]`.
- V: `ended != 0` sets `unit[0x1BA] = 1`; if `unit[0x1B9]` was exactly 1 it becomes 3 (move done + turn given up).
- V: then `BTurn_IsUnitDone(unit)` decides whether `BTurn_FinishUnit(slot)` runs (CT bonus + clear active flag).
- V: the Wait path calls it with `(slot, 0, 1)`.

## State touched

- Calls: [BTurn_IsUnitDone](BTurn_IsUnitDone.md), [BTurn_FinishUnit](BTurn_FinishUnit.md)

## Referenced by

- Called by: [sub_140206CE8](sub_140206CE8.md), [sub_14020A7F0](sub_14020A7F0.md), [sub_14020AD64](sub_14020AD64.md)

## Notes

The name reflects the two call patterns: movement completion uses `moved=1`, Wait/end-of-turn uses `moved=0, ended=1`.
`BTurn_MarkActionDone` (`0x1403105B0`) is the sibling that sets bit 1.

## Open questions

Which caller sets `moved=1, ended=1` (the "move and act then end" path) — `sub_14020A7F0`/`sub_140210AF0` call it but
were not traced.
