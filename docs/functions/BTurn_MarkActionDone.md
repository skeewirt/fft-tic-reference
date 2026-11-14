# BTurn_MarkActionDone

- **Address:** `0x1403105B0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int __fastcall BTurn_MarkActionDone(int slot)`
- **Callers:** `sub_14020261C`, `sub_140206CE8`, `sub_14020B90C` (`0x14020BBB9`)
- **Callees:** `BTurn_IsUnitDone`, `BTurn_FinishUnit`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Records that a unit has used its action and ends the turn if the move was already used.

## Behavior

- V: an empty slot (`unit[1] == 0xFF`) returns `-1`.
- V: sets bit 1 of `unit[0x1B9]` (`|= 2`).
- V: then calls `BTurn_IsUnitDone`; when true, `BTurn_FinishUnit(slot)` runs.
- V: called from the post-move handler `sub_14020B90C` at `0x14020BBB9` when the unit also used an action.

## State touched

- Calls: [BTurn_IsUnitDone](BTurn_IsUnitDone.md), [BTurn_FinishUnit](BTurn_FinishUnit.md)

## Referenced by

- Called by: [sub_14020261C](sub_14020261C.md), [sub_140206CE8](sub_140206CE8.md)

## Notes

Together with `BTurn_MarkMoveDone` this implements the "move + action, then turn ends" rule: the turn ends when
`+0x1B9 & 3 == 3`, when the partner has finished, or when `+0x1BA` is set.

## Open questions

None recorded.
