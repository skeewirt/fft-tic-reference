# BattleUnitEditor_EventTask

- **Address:** `0x1402E9DE0`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int64_t BattleUnitEditor_EventTask(void)`
- **Callers:** the task entry of node 44 of the event menu node tables
- **Callees:** sub_1402E9EA4, sub_1402E9980, sub_1402BA718, EventTask_WaitFrame, BattleUnitEditor_Run, EventTask_Terminate

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Event task wrapper of the battle unit editor: node 44 of the event menu node table tbl_EventMenuNodesLanguage0.

## Behavior

- V: the same sequence as BattleUnitEditor_SceneTask on the event side: sub_1402E9EA4(0, 255, 255), flags word 0x141853BC8, dword 0x142E7FFF4 and word 0x14184B240 = 1, sub_1402E9980(11), slot 8 cleared, sub_1402BA718 for slots 8, 13, 12, 11, 10, two frames, BattleUnitEditor_Run, flags cleared, EventTask_Terminate.
- V (data references to it): its references are +48 of node 44 in the four language tables of the event menu nodes (tbl_EventMenuNodesLanguage0 at 0x1408DE240 is the first).
- V (table data): node 56 of the same table lists node 44 as its fifth row (row list 0x14078DA90 = 29, 12, 11, 57, 44).

## State touched

- Calls: [EventTask_WaitFrame](EventTask_WaitFrame.md), [BattleUnitEditor_Run](BattleUnitEditor_Run.md), [EventTask_Terminate](EventTask_Terminate.md)

## Open questions

None recorded.
