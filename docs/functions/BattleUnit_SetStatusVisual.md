# BattleUnit_SetStatusVisual

- **Address:** `0x1401FB064`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 BattleUnit_SetStatusVisual(int statusPlus1, int on, int16 unitIndex)`
- **Callers:** Battle_StatusApply, Battle_StatusRefresh, Battle_ApplyActionResult, Unit_SetChargeStateBits, Unit_ReloadFromJobRow, sub_140272874
- **Callees:** SceneObject_FindByUnitIndex, sub_1403167E4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets or clears a status's visual bits on the unit's scene object: the tint / pose word or the sprite-change word.

## Behavior

- V: the first argument is the status id + 1 (Battle_StatusApply, Battle_StatusRefresh, Battle_ApplyActionResult, Unit_SetChargeStateBits and Unit_ReloadFromJobRow pass the bit index + 1 of the status sets at +0x61).
- V: it writes the set / clear masks of the scene object (+0x164 / +0x16C for the word at +0x15C, +0x168 / +0x170 for +0x160) that SceneUnit_ApplyStatusVisuals applies; the mask is tbl_BattleStatusIconFlagMasks[status + 1].
- V: special cases (by status id): 1 Crystal, 15 Chest, 21 Chicken and 22 Toad set bits 1, 8, 2, 4 of +0x160 (the effect sprites); 5, 17 and 19 go to +0x160 with the table mask; 9 and 31 do nothing; 22 also calls sub_1403167E4.

## State touched

- Calls: [SceneObject_FindByUnitIndex](SceneObject_FindByUnitIndex.md), [sub_1403167E4](sub_1403167E4.md)
- Reads: [g_StatusIconFlags](../globals/g_StatusIconFlags.md)

## Referenced by

- Called by: [Battle_StatusApply](Battle_StatusApply.md), [Battle_StatusRefresh](Battle_StatusRefresh.md), [Unit_BuildInnateStatuses](Unit_BuildInnateStatuses.md), [Unit_SetChargeStateBits](Unit_SetChargeStateBits.md)
- Observed behaviours: [StatusScreenReadersAndIconPath](../behaviors/StatusScreenReadersAndIconPath.md)
- Reads tables: [BattleStatusIconFlagMasks](../tables/BattleStatusIconFlagMasks.md)

## Notes

Name is ours (was sub_1401FB064; the old sheet read the argument as the status id indexed + 1 inside: the entry code uses it as the index directly, and every caller adds the 1). The offsets +0x15C / +0x160 are reached through the set / clear mask fields (+0x164..+0x170, written here as dword indexes 89..92) and +0x61 is the status set of the callers, so neither appears as a literal in this body. The table index is not bounds-checked; the IDA item is 42 dwords (to 0x140673678) and the game passes 1..40.

## Open questions

None recorded.
