# BTurn_IsUnitDone

- **Address:** `0x140310704`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `bool __fastcall BTurn_IsUnitDone(uint8_t *unit)`
- **Callers:** `BTurn_MarkMoveDone`, `BTurn_MarkActionDone`, `Battle_TurnEngine` (`0x14030F5xx`), `sub_14020B90C`
- **Callees:** `sub_14030DD1C`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Decides whether the active unit has nothing left to do this turn, including the two-unit (partner) case.

## Behavior

- V: reads `unit[0x1B9] & 3` (move + action bits) through the record named by `unit[0x1BC]` (`0x140310738`);
  for normal units that id is the unit's own (V: `sub_140260ABC` compares `unit[0x1BC]` to the requested slot).
- V: `cl` = `(unit[0x65] & 8) != 0` or that record has `+0x1B9 & 3 == 3`; `al` = the same "both bits" test or
  `unit[0x1BA] != 0`.
- V: returns `cl && (unit[0x1BA] || sub_14030DD1C(unit)) && al` — i.e. both move and action done (or the pair
  equivalent), the turn given up flag, and the terrain/actionable check must all agree.

## Referenced by

- Called by: [BTurn_MarkActionDone](BTurn_MarkActionDone.md), [BTurn_MarkMoveDone](BTurn_MarkMoveDone.md), [Battle_TurnEngine](Battle_TurnEngine.md), [sub_14020B90C](sub_14020B90C.md)

## Notes

The function is deliberately conservative: both units of a pair can keep the turn alive.

## Open questions

The exact role of `sub_14030DD1C`'s return value (0/1/2) in the partner test.
