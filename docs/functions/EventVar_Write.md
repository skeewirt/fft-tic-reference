# EventVar_Write

- **Address:** `0x1402E9918`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventVar_Write(uint32_t index, int32_t value)`
- **Callers:** About 47 callers across the battle, world-map and event code.
- **Callees:** EventVar_Alu (twice)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes one event variable by index. The shared write accessor for the packed variable space, called from about 47 places.

## Behavior

- V: a negative value is reduced to its low byte (`(uint8_t)value`); a non-negative value is used as is.
- V: variable 44 is capped at 99,999,999 before the write.
- V: saves variable 0, then runs EventVar_Alu twice: op 190 clears the target variable, then op 176 adds the literal value, which stores it. Variable 0 is then restored.
- V: because variable 0 is the scratch cell and is restored at the end, writing index 0 has no lasting effect.
- V: variable 44 is the party's gil (live 2026-11-04: it read 3,200 while the owner had 3,200 gil; `EventVar_Write(44, 99999)` made the shop show 99,999 and the purchases were paid from it). The variables are dwords at the pointer `*0x14078DCE8` (variable n at +4n).

## State touched

- Calls: [EventVar_Alu](EventVar_Alu.md)

## Referenced by

- Called by: [ClassicMenu_RunScreenStack](ClassicMenu_RunScreenStack.md), [Errand_ApplyResult](Errand_ApplyResult.md), [Errand_Recall](Errand_Recall.md), [Errand_Start](Errand_Start.md), [EventCmd_ServiceRequests](EventCmd_ServiceRequests.md), [EventMessage_Scripted](EventMessage_Scripted.md), [EventVarEditor_ValueInput](EventVarEditor_ValueInput.md), [EventVar_Read](EventVar_Read.md), [EventViewer_EntryPage](EventViewer_EntryPage.md), [EventViewer_StartReplay](EventViewer_StartReplay.md), [GameState_ResetParty](GameState_ResetParty.md), [Game_MainLoop](Game_MainLoop.md), [LegacyMenu_InitWorld](LegacyMenu_InitWorld.md), [LegacyMenu_PickLocation](LegacyMenu_PickLocation.md), [LegacyWorldMenu_FrameStep](LegacyWorldMenu_FrameStep.md), [LegacyWorldMenu_StartTestBattle](LegacyWorldMenu_StartTestBattle.md), [MenuCtl_Entry45](MenuCtl_Entry45.md), [MenuCtl_Entry53](MenuCtl_Entry53.md), [OpeningTask_6](OpeningTask_6.md), [SaveWork_UnpackToLive_Repair](SaveWork_UnpackToLive_Repair.md), [TavernMenu_OnCommand](TavernMenu_OnCommand.md), [WorldEncounter_StartBattle](WorldEncounter_StartBattle.md), [WorldMap_InitLocations](WorldMap_InitLocations.md), [sub_1402CCEE0](sub_1402CCEE0.md), [sub_14033F8C0](sub_14033F8C0.md), [sub_1403456D4](sub_1403456D4.md), [sub_140373DE8](sub_140373DE8.md), [sub_14039DA58](sub_14039DA58.md)
- Observed behaviours: [StoryProgressEventVariable110DecidesWhichStoryBattleAWorldMapSiteLoads](../behaviors/StoryProgressEventVariable110DecidesWhichStoryBattleAWorldMapSiteLoads.md)

## Notes

The store itself is subject to the write lock inside EventVar_Alu: while variable 508 is non-zero only a whitelist of variables can change.

## Open questions

Which shop function writes variable 44 on a purchase (not needed for the meaning, which is confirmed live).
