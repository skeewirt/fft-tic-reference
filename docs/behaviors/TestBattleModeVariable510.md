# TestBattleModeVariable510

- **Kind:** observed behaviour
- **Scope:** engine (battle set-up)
- **Area:** [Event system](../areas/event-system.md)
- **Affects:** [LegacyWorldMenu_StartTestBattle](../functions/LegacyWorldMenu_StartTestBattle.md), [LegacyMenu_InitWorld](../functions/LegacyMenu_InitWorld.md), [ScenarioSetup_ApplyRecord](../functions/ScenarioSetup_ApplyRecord.md), [Deployment_PrepareCandidates](../functions/Deployment_PrepareCandidates.md), [GridScreen_Task](../functions/GridScreen_Task.md), [sub_14030476C](../functions/sub_14030476C.md), [BattleMsg_Dispatch](../functions/BattleMsg_Dispatch.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Variable 510 marks a test battle started from the old world menu's map number entry; several battle set-up steps read it and take a shortened path.

## Behavior

- V: LegacyWorldMenu_StartTestBattle writes event variable 510 = 1 (and 39, 48, 34, 35, 36 = 0); LegacyMenu_InitWorld writes it 0.
- V: the battle code reads scene variable 510 (SceneVar_Read): ScenarioSetup_ApplyRecord sets the words 0x140D3FC70 and 0x140D3FC78 to 0x8000 when it is nonzero.
- V: Deployment_PrepareCandidates, when it is nonzero, reads scene variable 51 and searches the 768 placement rows (12 bytes, byte +9) for that value to pick the placement row.
- V: GridScreen_Task, when it is nonzero, sets the placement record's byte +8 (the area's unit count) to 4.
- V: sub_14030476C: in state 7 it skips the palette reload; in the roster step it clears word 0x14114B0B4 and builds team 1 (Battle_BuildRosterTeam(..., 1)) before the common Battle_BuildRosterTeam(..., 0); in state 11 it takes the same path as battle mode 1.
- V: BattleMsg_Dispatch, on the path taken when scene variable 509 is nonzero, writes scene variable 39 = 403 instead of 401 at the end of the battle.
- I: the event variable reaches the scene variable through the copy between the two stores; the copy itself was not traced for 510.

## Open questions

None recorded.
