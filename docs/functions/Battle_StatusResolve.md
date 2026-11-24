# Battle_StatusResolve

- **Address:** `0x14030C87C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64 Battle_StatusResolve(int slot, unsigned int mode)`
- **Callers:** Battle_ApplyActionResult (three calls), sub_140271AC0; also started through the scene callback slot by sub_14024138C and EventUnitStatus_SetBit
- **Callees:** Mem_CopyChecked, Status_FilterPendingSets, Battle_StatusRefresh, Battle_StatusApply

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Applies the pending status adds and removes of one battle unit: filters them, clears, sets, then settles the effects that depend on the new set.

## Behavior

- V: returns -1 at once when the unit row of slot is empty (row byte +1 equal to 0xFF).
- V: points g_BattleActingUnit at the unit and g_BattleActionBlock at its result block (unit +446), stores the slot in the byte after the first byte of xmmword_1407B0760, and saves both pending sets (block +29 and +34, five bytes each) in locals.
- V: calls Status_FilterPendingSets(mode), Battle_StatusRefresh(slot) and Battle_StatusApply(slot, mode) in that order (Apply filters and refreshes again for each status it applies).
- V: afterwards the effective set (+97): KO (bit 0x20 of byte 0) sets the HP word at +48 to 0; when none of Readying, Jumping and Performing (mask 0x0D of byte 0) is set the charge counter +0x18D becomes 0xFF; one of Confusion, Vampire, Berserk, Chicken or Charmed (bytes 1..2 masks 0x14, 0x0C, byte 4 mask 0x20) clears bit 3 of +5, otherwise +5 takes bit 3 of the side byte +494; unless Charmed, bits 4..5 of +5 are made equal to those of +494.
- V: finally it copies the saved pending sets back into the result block and returns 0.

## State touched

- Calls: [Mem_CopyChecked](Mem_CopyChecked.md), [Battle_StatusRefresh](Battle_StatusRefresh.md), [Battle_StatusApply](Battle_StatusApply.md), [sub_1403052DC](sub_1403052DC.md)
- Reads: [UnitWorkRecord.status_effective](../structs/UnitWorkRecord.md#status_effective)
- Writes: [UnitWorkRecord.charge_counter](../structs/UnitWorkRecord.md#charge_counter)

## Referenced by

- Called by: [Battle_ApplyActionResult](Battle_ApplyActionResult.md), [sub_140271AC0](sub_140271AC0.md)
- Observed behaviours: [AnActionEarnsExpAndJpOnlyWhenItChangedItsTarget](../behaviors/AnActionEarnsExpAndJpOnlyWhenItChangedItsTarget.md), [StatusBitWritersAndTheRemovalPath](../behaviors/StatusBitWritersAndTheRemovalPath.md), [StatusLoopsInflictCopyAndBattleTableLifetime](../behaviors/StatusLoopsInflictCopyAndBattleTableLifetime.md), [StatusesAreFortyBitSetsInEightRegions](../behaviors/StatusesAreFortyBitSetsInEightRegions.md)

## Notes

Name is ours (the sheets of Battle_StatusApply and Battle_StatusRefresh call it the wrapper). It is the one entry that every status change passes through.

## Open questions

? the meaning of the +5 bit 3 (it follows the five statuses above).
