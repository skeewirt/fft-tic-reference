# Battle_ScaleByDifficulty

- **Address:** `0x140309FB8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64_t Battle_ScaleByDifficulty(int16_t *hpOut, int16_t *mpOut, int64_t a3, int64_t a4)`
- **Callers:** sub_14030A11C (IDA code references)
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scales the HP and MP damage of a resolved action by the play mode's percentages: the row of the DifficultyLevel table that the configuration names, one percentage for one side of the target and another for the other.

## Behavior

- V: copies the result block's words +6 (HP damage) and +10 (MP damage) to the two outputs; when g_ShopModeGate (the Enhanced edition flag) is 0 it only clamps them to 999.
- V: otherwise it finds the nxd table with registry id 111 (DifficultyLevel; the table pointer is cached at qword_143CDA488) and its row keyed by the configuration byte +196 (g_ConfigData), the play mode.
- V: the percentage is the row's +8 (Unknown8) when bits 0x30 of the target's unit byte +494 (g_BattleActingUnit) are set, else its +12 (UnknownC); for the command byte 21 (g_FormulaBlock +6) outside the battle-state gate the row's +16 / +20 instead. Each output = percentage x word / 100 (unsigned), then clamped to 999.
- V (data): DifficultyLevel rows 0 / 1 / 2 hold 100 / 100, 110 / 50 and 70 / 120 (+8 / +12; +16 / +20 the same except row 2's 35).
- V (seen live 2026-11-17, play mode Squire = row 1): two player strikes whose formula gave 23 and 31 previewed and dealt 25 and 34 (x 110 / 100) to enemies.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Notes

Source: 2026-11-17, read whole (decompile). The side bits at +494 are I (the enemies took the +8 percentage: 110 in Squire mode, so set bits = the enemy side for the player's attacks); which play mode each configuration value names (row 1 = Squire, seen on this install) is I for rows 0 and 2.

## Open questions

? which of 0 / 2 is the middle and which the hard play mode; what command 21 is.
