# BTurn_FinishUnit

- **Address:** `0x140310650`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int __fastcall BTurn_FinishUnit(int slot)`
- **Callers:** `BTurn_MarkMoveDone`, `BTurn_MarkActionDone`, `Battle_TurnEngine`, `sub_14020AD64`, `sub_14020B90C`, `sub_14020BCF0`, `Battle_AITurnRun`
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Ends one unit's turn: clears the active flag and applies the post-turn CT bonus.

## Behavior

- V: does nothing when the slot is empty (`unit[1] == 0xFF`) or the unit is not active (`unit[0x1B8] == 0`).
- V: `dl = (unit[0x65] & 8) != 0` or (the record at `unit[0x1BC]` exists and its `+0x1B9 & 1` is set).
  Normally `+0x1BC` is the unit's own id (proved by `sub_140260ABC`), so `dl` = "moved".
- V: `r9 = (unit[0x65] & 4) != 0` or `(unit[0x61] & 1) != 0` or `unit[0x1BA] != 0` ("turn given up").
- V: `unit[0x1B8] = 0`; `ct = unit[0x41] + (dl ? 0 : 20) + (r9 ? 0 : 20)`; `unit[0x41] = min(ct, 60)`.
  So the bonus is 0, 20 or 40, capped at 60 (`0x1403106D9`-`0x1403106F8`, clamp immediate `0x3C`).
- V: returns 1.

## Referenced by

- Called by: [BTurn_MarkActionDone](BTurn_MarkActionDone.md), [BTurn_MarkMoveDone](BTurn_MarkMoveDone.md), [Battle_AITurnRun](Battle_AITurnRun.md), [Battle_TurnEngine](Battle_TurnEngine.md), [sub_14020AD64](sub_14020AD64.md), [sub_14020B90C](sub_14020B90C.md), [sub_14020BCF0](sub_14020BCF0.md)

## Notes

This is the only writer of the "active" byte `+0x1B8` besides the turn engine. The CT bonus explains why a unit that
just acted starts the next round at 20-60 CT rather than 0.

## Open questions

Why the developer chose 20/40: the flags `+0x65 & 8/4` and `+0x61 & 1` select the two "penalty" cases; their status
names are not identified.
