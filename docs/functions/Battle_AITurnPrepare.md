# Battle_AITurnPrepare

- **Address:** `0x14031F534`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 __fastcall Battle_AITurnPrepare()`
- **Callers:** `sub_14031F130` (`0x14031F262`, the AI turn task)
- **Callees:** `sub_140321740`, `Battle_AITurnRun` (`0x14038A468`)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the per-unit AI table (visibility, HP/MP ratios, flags) and then runs one AI turn.

## Behavior

- V: for all 21 units: `sub_140321740(i)` marks the unit in the AI table at `v1`; units not visible get flag `0x10`.
- V: sets per-unit flags: `v1[1] = 1` for units other than the acting one, `0x20`/`0x40` from `unit[2] & 0x20`,
  `0x01`/`0x02` from HP and MP below half, `0x80` when HP is below 3/4 of max; the low bits of `v1[0]` are cleared
  first.
- V: sets `byte_141872357 |= 1`, `byte_1418716B4 = 1`, `byte_1418716BD = 0` and calls `Battle_AITurnRun`.
- V: returns `-1` when the AI driver aborts (engine state restored), else 0, and clears `byte_141872357` bit 0.

## State touched

- Calls: [Battle_AITurnRun](Battle_AITurnRun.md)

## Referenced by

- Called by: [Ai_UnitTurnStep](Ai_UnitTurnStep.md)

## Notes

The AI table byte layout (`v1[0..4]`) is a scoring input for `Battle_AITurnRun`; it is rebuilt every AI turn.

## Open questions

The meaning of the per-unit bytes `v1[1..4]` used by the scoring code.
