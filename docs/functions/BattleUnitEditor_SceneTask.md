# BattleUnitEditor_SceneTask

- **Address:** `0x140233DA0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64_t BattleUnitEditor_SceneTask(void)`
- **Callers:** the task entry of node 44 of the scene menu node tables
- **Callees:** BattleAction_StartScript, EventSequencer_TakeTurn, sub_1402F7F4C, SceneTask_WaitFrame, BattleUnitEditor_Run, SceneTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task wrapper of the battle unit editor: node 44 of the scene menu node table tbl_UiMenuNodesLang0.

## Behavior

- V: BattleAction_StartScript(0, 255, 255); sets word 0x140D4097C, dword 0x142E7FFF4 and word 0x140D4080C to 1; EventSequencer_TakeTurn(11).
- V: clears scene task slot 8's record and sets its close qword, calls sub_1402F7F4C for slots 8, 13, 12, 11 and 10 (I: stops those tasks), waits two frames and runs BattleUnitEditor_Run.
- V: afterwards clears the flags it set, dword 0x140D40918 and the input word, then SceneTask_Terminate.
- V (data references to it): its references are +48 of node 44 in the four language tables of the scene menu nodes (tbl_UiMenuNodesLang0 at 0x140801370 is the first).

## State touched

- Calls: [BattleAction_StartScript](BattleAction_StartScript.md), [EventSequencer_TakeTurn](EventSequencer_TakeTurn.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [BattleUnitEditor_Run](BattleUnitEditor_Run.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Open questions

None recorded.
