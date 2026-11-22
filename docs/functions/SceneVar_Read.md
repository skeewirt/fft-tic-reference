# SceneVar_Read

- **Address:** `0x1402332D8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint32_t SceneVar_Read(uint32_t index)`
- **Callers:** About 250 call sites, including EventScript_Run (15), EventScript_LoadCurrent and many scene and battle routines.
- **Callees:** SceneVar_Alu (twice), SceneVar_Write (index 34 only)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads one event variable by index through the second task group's copy of the variable system. The event interpreter and most scene code use this copy; it is by far the most used accessor.

## Behavior

- V: identical in logic to EventVar_Read, but it works on the store pointer `off_1407830D8` and runs its two steps through SceneVar_Alu.
- V: both pointers (`off_14078DCE8` for the first group and `off_1407830D8` for this one) are set by the task-group init routines to the same storage, `unk_140D40060`, so both copies see the same variables.
- V: about 250 call sites.

## State touched

- Calls: [SceneVar_Alu](SceneVar_Alu.md), [SceneVar_Write](SceneVar_Write.md)

## Referenced by

- Called by: [BattleLoad_StepFresh](BattleLoad_StepFresh.md), [BattleMsg_Dispatch](BattleMsg_Dispatch.md), [Battle_AwardUnitJp](Battle_AwardUnitJp.md), [Battle_MoveRange_WeatherCost](Battle_MoveRange_WeatherCost.md), [Battle_PlaceEntryUnits](Battle_PlaceEntryUnits.md), [Battle_SaveCapture](Battle_SaveCapture.md), [Battle_TurnEngine](Battle_TurnEngine.md), [ClutFade_SetTarget](ClutFade_SetTarget.md), [DeploymentGrid_CommenceCheck](DeploymentGrid_CommenceCheck.md), [Deployment_AreaOfPlacedUnit](Deployment_AreaOfPlacedUnit.md), [Deployment_LoadAreaPlacement](Deployment_LoadAreaPlacement.md), [Deployment_PlaceUnitAtCursor](Deployment_PlaceUnitAtCursor.md), [Deployment_PrepareCandidates](Deployment_PrepareCandidates.md), [Deployment_SelectArea](Deployment_SelectArea.md), [EventMapTitle_LoadTexture](EventMapTitle_LoadTexture.md), [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [EventScript_LoadCurrent](EventScript_LoadCurrent.md), [EventScript_Run](EventScript_Run.md), [EventScript_SkipTick](EventScript_SkipTick.md), [EventSequence_RecordTask](EventSequence_RecordTask.md), [EventSkip_IsViewerEvent](EventSkip_IsViewerEvent.md), [EventState_MoveTask](EventState_MoveTask.md), [EventUnitBlock_RunTask](EventUnitBlock_RunTask.md), [EventUnitStatus_SaveAndHide](EventUnitStatus_SaveAndHide.md), [Formula_SceneVarElemMod](Formula_SceneVarElemMod.md), [Formula_StealGilApply](Formula_StealGilApply.md), [MoveFind_ProbeTile](MoveFind_ProbeTile.md), [MoveFind_TakeItem](MoveFind_TakeItem.md), [SaveHeader_FillBattleFields](SaveHeader_FillBattleFields.md), [SaveSlot_WriteFromLive](SaveSlot_WriteFromLive.md), [SaveWork_PackFromLive](SaveWork_PackFromLive.md), [ScenarioSetup_ApplyRecord](ScenarioSetup_ApplyRecord.md), [SceneUnit_RunPlacement](SceneUnit_RunPlacement.md), [SceneVar_Alu](SceneVar_Alu.md), [Scene_StartMusic](Scene_StartMusic.md), [ShopItemList_DrawRow](ShopItemList_DrawRow.md), [Unit_ApplySpawnRecord](Unit_ApplySpawnRecord.md), [UserSituation_TestCheck](UserSituation_TestCheck.md), [WorldWeather_Update](WorldWeather_Update.md), [sub_14016E7F4](sub_14016E7F4.md), [sub_1401EF0D8](sub_1401EF0D8.md), [sub_1401F3858](sub_1401F3858.md), [sub_14020261C](sub_14020261C.md), [sub_140238444](sub_140238444.md), [sub_14024138C](sub_14024138C.md), [sub_1402A6710](sub_1402A6710.md), [sub_1402C60E4](sub_1402C60E4.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C8010](sub_1402C8010.md), [sub_1402C80D8](sub_1402C80D8.md), [sub_1402C9F78](sub_1402C9F78.md), [sub_14030476C](sub_14030476C.md), [sub_140306C90](sub_140306C90.md), [sub_14030CF38](sub_14030CF38.md)
- Observed behaviours: [BattleMapIdPathsAndTheirWidths](../behaviors/BattleMapIdPathsAndTheirWidths.md)

## Notes

See EventVar_Read for the variable layout and the index 34 rule.

## Open questions

None recorded.
