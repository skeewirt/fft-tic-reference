# SceneVar_Write

- **Address:** `0x140233368`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void SceneVar_Write(int index, int value, char flag, int extra)`
- **Callers:** About 110 call sites, including EventScript_Run (14) and EventMessage_Task.
- **Callees:** SceneVar_Alu (twice)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes one event variable by index through the second task group's copy of the variable system.

## Behavior

- V: the same logic as EventVar_Write (negative values reduced to a byte, variable 44 capped at 99,999,999, variable 0 restored afterwards), on the store pointer `off_1407830D8`, using SceneVar_Alu with operations 190 and 176.
- V: passes two extra values (`extra` and `flag`) through to SceneVar_Alu.
- V: about 110 call sites.

## State touched

- Calls: [SceneVar_Alu](SceneVar_Alu.md)

## Referenced by

- Called by: [BattleLoad_ClearPartyReserve](BattleLoad_ClearPartyReserve.md), [BattleMsg_Dispatch](BattleMsg_Dispatch.md), [Battle_RestoreSceneVars](Battle_RestoreSceneVars.md), [Battle_TurnEngine](Battle_TurnEngine.md), [Deployment_PrepareCandidates](Deployment_PrepareCandidates.md), [EventMessage_Task](EventMessage_Task.md), [EventScript_Run](EventScript_Run.md), [EventScript_SkipTick](EventScript_SkipTick.md), [EventState_MoveTask](EventState_MoveTask.md), [EventSubScript_RunTask](EventSubScript_RunTask.md), [Game_MainLoop](Game_MainLoop.md), [MenuCtl_Entry44](MenuCtl_Entry44.md), [MenuCtl_Entry45](MenuCtl_Entry45.md), [ScenarioSetup_ApplyRecord](ScenarioSetup_ApplyRecord.md), [SceneTransition_CheckTables](SceneTransition_CheckTables.md), [SceneVar_Read](SceneVar_Read.md), [WorldWeather_Update](WorldWeather_Update.md), [sub_1402C60E4](sub_1402C60E4.md), [sub_1402C8010](sub_1402C8010.md), [sub_1402C9F78](sub_1402C9F78.md), [sub_14030CF38](sub_14030CF38.md)
- Called by event opcodes: [0x18](../opcodes/README.md)
- Observed behaviours: [BattleMapIdPathsAndTheirWidths](../behaviors/BattleMapIdPathsAndTheirWidths.md), [ScenarioSetupRecordFeedsTheBattleSceneVariables](../behaviors/ScenarioSetupRecordFeedsTheBattleSceneVariables.md)
- Resolves registries: [EventVariables](../registries/EventVariables.md)

## Notes

See EventVar_Write.

## Open questions

What the two extra arguments carry.
