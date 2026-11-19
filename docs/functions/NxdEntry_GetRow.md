# NxdEntry_GetRow

- **Address:** `0x1403D2FD8`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `char *NxdEntry_GetRow(NxdEntry *entry)`
- **Callers:** about 400 nxd readers (ItemTable_GetRow, UITable_GetRow, UITable_GetRowByKey, ...)
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the row data an entry points to: the entry's pointer plus the offset its kind names.

## Behavior

- V: kind = entry qword 0 without bit 63; 0 returns null.
- V: kind 1: pointer + dword at pointer +4; kind 2: + dword at +8; other kinds: + dword at +16.

## Referenced by

- Appears in flows: [NxdMultiKeyLookup](../flows/NxdMultiKeyLookup.md)
- Called by: [BattleLabel_ShowStatusSignal](BattleLabel_ShowStatusSignal.md), [BattleMsg_ResolveEntry](BattleMsg_ResolveEntry.md), [BattleObjective_ShowsTarget](BattleObjective_ShowsTarget.md), [Battle_AwardUnitJp](Battle_AwardUnitJp.md), [Battle_ScaleByDifficulty](Battle_ScaleByDifficulty.md), [CMesId_GetText](CMesId_GetText.md), [CharaName_GetDisplayName](CharaName_GetDisplayName.md), [EffectNxd_HasFlag24](EffectNxd_HasFlag24.md), [EffectNxd_HasFlag25](EffectNxd_HasFlag25.md), [EffectNxd_HasFlag28](EffectNxd_HasFlag28.md), [EffectNxd_LoadRow](EffectNxd_LoadRow.md), [Effect_TintByNxdScale](Effect_TintByNxdScale.md), [EquipDetail_BuildCategoryLines](EquipDetail_BuildCategoryLines.md), [EventControl_ApplyCarry](EventControl_ApplyCarry.md), [EventControl_PausedTick](EventControl_PausedTick.md), [EventId_TestByte27](EventId_TestByte27.md), [ItemTable_GetName](ItemTable_GetName.md), [ItemTable_GetRowById](ItemTable_GetRowById.md), [Item_IsOwned](Item_IsOwned.md), [OverrideEntry_FillUnitEntry](OverrideEntry_FillUnitEntry.md), [PauseManager_Tick](PauseManager_Tick.md), [PoachTable_GetRowById](PoachTable_GetRowById.md), [ScenarioSetup_ApplyRecord](ScenarioSetup_ApplyRecord.md), [SceneUnit_BuildFromQueueEntry](SceneUnit_BuildFromQueueEntry.md), [StatusLists_BuildOrder](StatusLists_BuildOrder.md), [StatusScreen_SetCaption](StatusScreen_SetCaption.md), [StatusScreen_SetEntry](StatusScreen_SetEntry.md), [Status_ListCategory](Status_ListCategory.md), [Status_ListSortKey](Status_ListSortKey.md), [UITable_GetRowByKeys](UITable_GetRowByKeys.md), [UnitPanel_SetSignalList](UnitPanel_SetSignalList.md), [Unit_ReactionVoiceAllowed](Unit_ReactionVoiceAllowed.md), [UserSituation_IsMet](UserSituation_IsMet.md), [WorldMap_ApplyProgressInfo](WorldMap_ApplyProgressInfo.md), [sub_14020261C](sub_14020261C.md), [sub_14028A8B0](sub_14028A8B0.md), [sub_14028B180](sub_14028B180.md), [sub_14028B354](sub_14028B354.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md), [sub_14036E5DC](sub_14036E5DC.md)
- Observed behaviours: [FirstDwordOfTableRowsIsNeverRead](../behaviors/FirstDwordOfTableRowsIsNeverRead.md), [SpriteLookupFailuresPastTheTables](../behaviors/SpriteLookupFailuresPastTheTables.md)
- Reads file formats: [NxdMultiKeyIndex](../formats/NxdMultiKeyIndex.md), [NxdSingleKeyRows](../formats/NxdSingleKeyRows.md)

## Open questions

None recorded.
