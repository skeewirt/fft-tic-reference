# SceneTask_Terminate

- **Address:** `0x1402F7EC8`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void SceneTask_Terminate(void)`
- **Callers:** About 130 callers, including EventMessage_Task, EventScript_FindInstruction, SceneVar_Alu and many task bodies.
- **Callees:** ScenePad_UpdateRepeat, EventThread_ReturnToEntry

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Ends the current task in the second task table; the error trap and the normal exit for scene and event-script tasks. The twin of EventTask_Terminate, with about 130 callers.

## Behavior

- V: clears the qwords at +144 and +152 of the current task's block in `off_140783088`, marking it no longer runnable.
- V: advances the current index `dword_140D40948` to the next block whose +144 qword is non-zero, up to 16, wrapping to 0.
- V: calls ScenePad_UpdateRepeat, restores the original index and calls EventThread_ReturnToEntry.
- V: called by SceneVar_Alu and SceneVar_ResolveSlot as their error trap, and by about 130 task bodies as their ending.

## State touched

- Calls: [ScenePad_UpdateRepeat](ScenePad_UpdateRepeat.md), [EventThread_ReturnToEntry](EventThread_ReturnToEntry.md)

## Referenced by

- Called by: [BattleAction_RunScript](BattleAction_RunScript.md), [BattleMenu_ConfirmRow](BattleMenu_ConfirmRow.md), [BattleMenu_RunStep](BattleMenu_RunStep.md), [BattleMsg_UnitTurnScene](BattleMsg_UnitTurnScene.md), [Battle_InitScene](Battle_InitScene.md), [EventCamera_MoveTask](EventCamera_MoveTask.md), [EventChannel_StepTask](EventChannel_StepTask.md), [EventColorPath_Task](EventColorPath_Task.md), [EventColor_Task](EventColor_Task.md), [EventCounter_Task](EventCounter_Task.md), [EventEndSlate_ShowTask](EventEndSlate_ShowTask.md), [EventFlagWait_Task](EventFlagWait_Task.md), [EventMapTitle_SweepTask](EventMapTitle_SweepTask.md), [EventMode_DispatchTask](EventMode_DispatchTask.md), [EventObject_MoveTask](EventObject_MoveTask.md), [EventObject_MoveWorker](EventObject_MoveWorker.md), [EventPanel_PickRow](EventPanel_PickRow.md), [EventPanel_ShowTask](EventPanel_ShowTask.md), [EventPanel_ShowWaitTask](EventPanel_ShowWaitTask.md), [EventScript_Run](EventScript_Run.md), [EventSequence_RecordTask](EventSequence_RecordTask.md), [EventSequencer_TakeTurn](EventSequencer_TakeTurn.md), [EventSprite_LoadTask](EventSprite_LoadTask.md), [EventStateTrack_RunTask](EventStateTrack_RunTask.md), [EventState_MoveTask](EventState_MoveTask.md), [EventSubScript_RunTask](EventSubScript_RunTask.md), [EventUnitBlock_RunTask](EventUnitBlock_RunTask.md), [EventUnitMove_Task](EventUnitMove_Task.md), [EventUnitStatus_ApplyTask](EventUnitStatus_ApplyTask.md), [EventVoice_PlayTask](EventVoice_PlayTask.md), [SceneMsgTask_Run](SceneMsgTask_Run.md), [SceneTask_FindFree](SceneTask_FindFree.md), [SceneVar_Alu](SceneVar_Alu.md), [SceneVar_ResolveSlot](SceneVar_ResolveSlot.md), [sub_14022F868](sub_14022F868.md), [sub_140233588](sub_140233588.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md), [sub_1402F8684](sub_1402F8684.md), [sub_1403015A4](sub_1403015A4.md), [sub_140323D1C](sub_140323D1C.md), [sub_140324658](sub_140324658.md), [sub_140338A28](sub_140338A28.md), [sub_1403980AC](sub_1403980AC.md), [sub_140399A64](sub_140399A64.md)
- Called by event opcodes: [0xDB](../opcodes/README.md), [0xE3](../opcodes/README.md)

## Notes

Same structure as EventTask_Terminate but on the second task table.

## Open questions

None recorded.
