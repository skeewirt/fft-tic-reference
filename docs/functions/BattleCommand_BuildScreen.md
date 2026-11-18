# BattleCommand_BuildScreen

- **Address:** `0x1402E600C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void BattleCommand_BuildScreen(void)`
- **Callers:** sub_1402B276C, sub_1402DE924, BattleCommand_BuildMenu
- **Callees:** memset, sub_14025FCDC, sub_1402E2C54, sub_1402600BC, sub_140242AFC, sub_1402D7724, sub_140361F74, sub_1402D806C, Ability_GetAuxRecord, sub_1402E5D18, sub_1400E6874, sub_1401EB798, sub_1400E601C, sub_1400E615C, sub_1400E5D84, sub_1400E620C, sub_1402A291C, UnitWork_FindJobBySkillset, sub_140156B40, JobRecord_FromJobId, EquipDetail_Refresh, sub_1400FBA58, sub_140101888, sub_1400E5C00, sub_1400E5CE8, Input_TestAction, sub_1402E2650, sub_1400FB9F0, sub_1402A286C, sub_1400E5EB4, sub_1400F0D4C, sub_1400F0D00, sub_1400F0D98, sub_1400F4BCC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the battle command/ability screen: the unit panels, the job record, the ability list entries and the equip detail panel the player navigates during a turn.

## Behavior

- V: the screen state is indexed by the active unit slot and copied from the battle object at 0x14378D620 with a stride of 0x470.
- V: the unit job is resolved through JobRecord_FromJobId and UnitWork_FindJobBySkillset, and the job record fills the panel.
- V: Ability_GetAuxRecord supplies the ability aux data for each list row, and EquipDetail_Refresh fills the equipment detail.
- V: the list strings include ListAction, which is the action-list heading the screen draws.
- V: the sub_1400E5xx calls (0x1400E5C00, 0x1400E5CE8, 0x1400E5D84, 0x1400E5EB4, 0x1400E601C, 0x1400E615C, 0x1400E620C, 0x1400E6874) build and bind the UI parts and the sprite records; Input_TestAction polls the pad.
- V: the three callers are the battle command task, the second menu and the item/throw menu entry.
- I: this is the ability/command list screen rather than the item list, because it reads the job record and the ability aux record per row.
- ?: which page of the screen each caller asks for; the screen mode field is not decoded.

## State touched

- Calls: [sub_140242AFC](sub_140242AFC.md), [Ability_GetAuxRecord](Ability_GetAuxRecord.md), [sub_1400E615C](sub_1400E615C.md), [sub_1402A291C](sub_1402A291C.md), [UnitWork_FindJobBySkillset](UnitWork_FindJobBySkillset.md), [JobRecord_FromJobId](JobRecord_FromJobId.md), [EquipDetail_Refresh](EquipDetail_Refresh.md), [Input_TestAction](Input_TestAction.md), [sub_1400FB9F0](sub_1400FB9F0.md), [sub_1400F4BCC](sub_1400F4BCC.md)
- Reads: [g_JobTable](../globals/g_JobTable.md), [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md)

## Referenced by

- Called by: [BattleCommand_BuildMenu](BattleCommand_BuildMenu.md), [LegacyMenu_LoadRowList](LegacyMenu_LoadRowList.md)
- Observed behaviours: [BattlePanelsNameTheJobByte](../behaviors/BattlePanelsNameTheJobByte.md)

## Notes

Whole function read (8840 bytes). The 0x470 stride and the list heading are the identifying facts.

## Open questions

None recorded.
