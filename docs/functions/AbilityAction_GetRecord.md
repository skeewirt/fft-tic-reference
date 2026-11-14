# AbilityAction_GetRecord

- **Address:** `0x1402BB060`
- **Area:** [Ability data](../areas/ability-data.md)
- **Prototype:** `uint8_t *AbilityAction_GetRecord(unsigned int abilityId)`
- **Callers:** about 40 callers: battle formula, range/area, cost and AI code
- **Callees:** AbilityAction_BuildWorkingCopy

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns a pointer to the 20-byte action record of an ability, building the working table on first use.

## Behavior

- V: returns null when the ability id is above 0x16F (367); ids from 368 up (the passive abilities) have no action record.
- V: on the first call, runs AbilityAction_BuildWorkingCopy once and sets a done flag.
- V: returns working table + 20 * id.

## State touched

- Calls: [AbilityAction_BuildWorkingCopy](AbilityAction_BuildWorkingCopy.md)

## Referenced by

- Called by: [Action_BuildCurrentAction](Action_BuildCurrentAction.md), [Action_SetWeaponItem](Action_SetWeaponItem.md), [BattleAct_SetupEffect](BattleAct_SetupEffect.md), [BattleAction_GetRangeInfo](BattleAction_GetRangeInfo.md), [BattlePreview_BuildAction](BattlePreview_BuildAction.md), [BattleRange_MarkArea](BattleRange_MarkArea.md), [BattleRange_MarkRing](BattleRange_MarkRing.md), [Battle_PreviewUnitAction](Battle_PreviewUnitAction.md), [Battle_ResolveAction](Battle_ResolveAction.md), [Battle_TurnEngine](Battle_TurnEngine.md), [TurnList_Build](TurnList_Build.md), [Unit_SetChargeStateBits](Unit_SetChargeStateBits.md), [sub_14027F974](sub_14027F974.md), [sub_140281488](sub_140281488.md), [sub_1402828E4](sub_1402828E4.md), [sub_1403099B0](sub_1403099B0.md), [sub_14030B1A0](sub_14030B1A0.md), [sub_14030B4F0](sub_14030B4F0.md), [sub_14030D1CC](sub_14030D1CC.md), [sub_14030DD8C](sub_14030DD8C.md), [sub_14030E368](sub_14030E368.md), [sub_14030EC48](sub_14030EC48.md), [sub_1403167E4](sub_1403167E4.md), [sub_140316D24](sub_140316D24.md), [sub_140388EB4](sub_140388EB4.md), [sub_14038B34C](sub_14038B34C.md), [sub_14038BF34](sub_14038BF34.md)
- Reads tables: [AbilityActionRecords](../tables/AbilityActionRecords.md)

## Notes

Field layout of the record is on the AbilityAction_BuildWorkingCopy page.

## Open questions

None recorded.
