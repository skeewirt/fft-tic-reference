# Input_TestAction

- **Address:** `0x1400FC598`
- **Area:** [Input](../areas/input.md)
- **Prototype:** `char sub_1400FC598(int mask, int selector, unsigned actionId, char mode)`
- **Callers:** about 90 event/message/battle routines, e.g. `EventMessage_Task`, `EventScript_Run`, `ScenePad_UpdateRepeat`
- **Callees:** `sub_1400FC4E0`, `sub_1400F6C8C`, `sub_1400F0D00`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The event system's "is this action down" test against the current merged button mask.

## Behavior

- V: returns 0 immediately while the PauseManager's current pause row says input is locked: the byte at offset 0x17 of the pause manager (`qword_143CD9E60`) gives the stack depth, which indexes the id stack starting at offset 0x14, and a control value of 2 means paused.
- V: mode 1: returns `(mask & sub_1400FC4E0(selector)) != 0`.
- V: selector 0: returns `sub_1400F0D00(qword_143CD9EE8 + 8, actionId)` (a pure table query, no current state).
- V: otherwise, when `mask != 0`, returns `(mask & sub_1400F6C8C(actionId)) != 0`.
- V: when `mask == 0`, tests two bytes at `qword_143CD9EE8 + 0x56A + 48*actionId` (16 bytes apart) and returns 1 if either is non-zero.

## Referenced by

- Called by: [BattleCommand_BuildScreen](BattleCommand_BuildScreen.md), [Battle_InitScene](Battle_InitScene.md), [EventControl_PausedTick](EventControl_PausedTick.md), [EventControl_RunningTick](EventControl_RunningTick.md), [EventControl_TryOpenPause](EventControl_TryOpenPause.md), [EventMessage_Task](EventMessage_Task.md), [EventScript_SkipTick](EventScript_SkipTick.md), [JobScreen_BuildLearnList](JobScreen_BuildLearnList.md), [JobScreen_FillUnitRows](JobScreen_FillUnitRows.md), [JobScreen_RefreshLearnList](JobScreen_RefreshLearnList.md), [JobTree_HandleInput](JobTree_HandleInput.md), [MovieControl_PausedTick](MovieControl_PausedTick.md), [MovieControl_TryOpenPause](MovieControl_TryOpenPause.md), [Tavern_TopInput](Tavern_TopInput.md), [sub_14021C620](sub_14021C620.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C80D8](sub_1402C80D8.md), [sub_1402D2578](sub_1402D2578.md), [sub_1402D58EC](sub_1402D58EC.md), [sub_1402D5FE4](sub_1402D5FE4.md), [sub_1403015A4](sub_1403015A4.md), [sub_140333974](sub_140333974.md), [sub_1403358FC](sub_1403358FC.md), [sub_1403456D4](sub_1403456D4.md), [sub_140366ABC](sub_140366ABC.md), [sub_140366FE0](sub_140366FE0.md), [sub_140372F9C](sub_140372F9C.md), [sub_140373DE8](sub_140373DE8.md), [sub_14039297C](sub_14039297C.md)
- Observed behaviours: [JobTreePanelLookups](../behaviors/JobTreePanelLookups.md)

## Notes

`mask` is the dword pointed to by `off_1407DCB48` (0x140D407E0) or `off_1407DD348` (0x140D407E4). `sub_1400F6C8C` maps an action id to a 16-bit button bit through the runtime binding table; with identity defaults Ctrl (17) is 0x04 and Shift (16) is 0x20 (I).

## Open questions

? the exact default binding rows; ? who writes 0x140D407E0/E4.
