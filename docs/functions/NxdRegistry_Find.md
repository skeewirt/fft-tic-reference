# NxdRegistry_Find

- **Address:** `0x1403D325C`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdTable *NxdRegistry_Find(NxdRegistry *reg, int tableId)`
- **Callers:** UITable_GetRow, UITable_GetRowByKey, Job_IsHiddenFromTree, AbilityAction_BuildWorkingCopy, OverrideEntry_LoadBattleEntries, Party_EggUpkeep, and every other by-id table reader (cached into a per-table global after the first lookup)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the table object registered under a table id, or null when the id is unknown.

## Behavior

- V: hashes the 4 bytes of the id with the 64-bit FNV-1a hash (offset basis and prime of the standard algorithm) and masks the result with the registry's bucket mask (+112).
- V: each bucket holds a first/last node pair in the bucket array (+88); the bucket is walked until a node whose id (+16) equals the argument is found or the last node is passed.
- V: a node is {+0 next, +8 prev, +16 id, +24 table object}; the table object is returned. A miss returns 0 (the registry's end sentinel at +64 is never returned).
- V: does not trigger loading; callers check the table state (+12) and use the row accessors themselves.

## Referenced by

- Called by: [ActiveUnit_OverheadMark](ActiveUnit_OverheadMark.md), [BattleFormation_DrawUnits](BattleFormation_DrawUnits.md), [BattleLabel_ShowReactionSignal](BattleLabel_ShowReactionSignal.md), [BattleLabel_ShowStatusSignal](BattleLabel_ShowStatusSignal.md), [BattleMsg_ResolveEntry](BattleMsg_ResolveEntry.md), [BattleObjective_ShowsTarget](BattleObjective_ShowsTarget.md), [BattleVoiceGroupRate_Chance](BattleVoiceGroupRate_Chance.md), [BattleVoice_IsSuppressed](BattleVoice_IsSuppressed.md), [BattleVoice_ResolveLine](BattleVoice_ResolveLine.md), [BattleVoice_RollAndPlay](BattleVoice_RollAndPlay.md), [BattleVoice_SetPattern](BattleVoice_SetPattern.md), [BattleVoice_UsesRows2And3](BattleVoice_UsesRows2And3.md), [Battle_AwardUnitJp](Battle_AwardUnitJp.md), [Battle_ScaleByDifficulty](Battle_ScaleByDifficulty.md), [BgmMode_BuildLists](BgmMode_BuildLists.md), [BgmMode_DrawRow](BgmMode_DrawRow.md), [BgmMode_PlaySelected](BgmMode_PlaySelected.md), [BonusEntitlement_IsOwned](BonusEntitlement_IsOwned.md), [BonusEntitlements_Setup](BonusEntitlements_Setup.md), [CMesId_GetText](CMesId_GetText.md), [CMesId_IsErrorBanner](CMesId_IsErrorBanner.md), [CharClut_GetColorSkin](CharClut_GetColorSkin.md), [CharaName_GetDisplayName](CharaName_GetDisplayName.md), [ClassicSubtitles_Step](ClassicSubtitles_Step.md), [CreditRoll_Step](CreditRoll_Step.md), [CursorUnit_TopPoint](CursorUnit_TopPoint.md), [Deployment_LoadAreaPlacement](Deployment_LoadAreaPlacement.md), [EffectNxd_DepthBiasFloat](EffectNxd_DepthBiasFloat.md), [EffectNxd_HasFlag24](EffectNxd_HasFlag24.md), [EffectNxd_HasFlag25](EffectNxd_HasFlag25.md), [EffectNxd_HasFlag28](EffectNxd_HasFlag28.md), [EffectNxd_LoadRow](EffectNxd_LoadRow.md), [Effect_TintByNxdScale](Effect_TintByNxdScale.md), [EquipDetail_BuildCategoryLines](EquipDetail_BuildCategoryLines.md), [EventControl_ApplyCarry](EventControl_ApplyCarry.md), [EventControl_PausedTick](EventControl_PausedTick.md), [EventId_TestByte27](EventId_TestByte27.md), [ItemTable_GetName](ItemTable_GetName.md), [ItemTable_GetRowById](ItemTable_GetRowById.md), [Item_IsOwned](Item_IsOwned.md), [Launcher_DrawPage](Launcher_DrawPage.md), [Launcher_FillControls](Launcher_FillControls.md), [Movie_Start](Movie_Start.md), [OverrideEntry_FillUnitEntry](OverrideEntry_FillUnitEntry.md), [PauseManager_Tick](PauseManager_Tick.md), [PoachTable_GetRowById](PoachTable_GetRowById.md), [ScenarioSetup_ApplyRecord](ScenarioSetup_ApplyRecord.md), [SceneUnit_BuildFromQueueEntry](SceneUnit_BuildFromQueueEntry.md), [Scene_StartMusic](Scene_StartMusic.md), [SettlementEvent_EvaluateConditions](SettlementEvent_EvaluateConditions.md), [ShopEntry_Fill](ShopEntry_Fill.md), [Shop_GetUiRowId](Shop_GetUiRowId.md), [StatusLists_BuildOrder](StatusLists_BuildOrder.md), [StatusScreen_SetCaption](StatusScreen_SetCaption.md), [StatusScreen_SetEntry](StatusScreen_SetEntry.md), [StatusVoice_CacheLines](StatusVoice_CacheLines.md), [StatusVoice_SpeakEvent](StatusVoice_SpeakEvent.md), [Status_ListCategory](Status_ListCategory.md), [Status_ListSortKey](Status_ListSortKey.md), [TileCursor_Draw](TileCursor_Draw.md), [UITable_GetRowByIndex](UITable_GetRowByIndex.md), [UITable_GetRowByKeys](UITable_GetRowByKeys.md), [UITable_GetRowCount](UITable_GetRowCount.md), [UnitList_Compare](UnitList_Compare.md), [UnitList_SortKey](UnitList_SortKey.md), [UnitPanel_SetSignalList](UnitPanel_SetSignalList.md), [Unit_GetVoicePatternId](Unit_GetVoicePatternId.md), [Unit_MouseHitTest](Unit_MouseHitTest.md), [Unit_ReactionVoiceAllowed](Unit_ReactionVoiceAllowed.md), [Unit_ScreenSpan](Unit_ScreenSpan.md), [UserSituation_IsMet](UserSituation_IsMet.md), [WorldMap_ApplyProgressInfo](WorldMap_ApplyProgressInfo.md), [sub_1400F6B5C](sub_1400F6B5C.md), [sub_14016E7F4](sub_14016E7F4.md), [sub_14016FFC8](sub_14016FFC8.md), [sub_14020261C](sub_14020261C.md), [sub_140217A7C](sub_140217A7C.md), [sub_14027032C](sub_14027032C.md), [sub_14028A8B0](sub_14028A8B0.md), [sub_14028B180](sub_14028B180.md), [sub_14028B354](sub_14028B354.md), [sub_1402B89F8](sub_1402B89F8.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md), [sub_14036E5DC](sub_14036E5DC.md)
- Observed behaviours: [CharShapeRowsANewLookNeeds](../behaviors/CharShapeRowsANewLookNeeds.md), [UiTableColumnsNeverRead](../behaviors/UiTableColumnsNeverRead.md)

## Notes

Ids seen at call sites: 19 ui, 39 Ability, 41 JobCommand, 45 Item, 46 Job, 96 OverrideEntryData, 189 GeneralJob, 247 OverrideAbilityActionData, 310 Egg.

## Open questions

None recorded.
