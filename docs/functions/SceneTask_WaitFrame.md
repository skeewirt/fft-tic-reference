# SceneTask_WaitFrame

- **Address:** `0x1402F7CAC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void SceneTask_WaitFrame(void)`
- **Callers:** Over 100 callers, including EventMessage_Task (14 times).
- **Callees:** ScenePad_UpdateRepeat, EventThread_Yield

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The wait-one-frame primitive for the second task table; over 100 routines call it to wait. It is the twin of EventTask_WaitFrame.

## Behavior

- V: runs only when `byte_140D408EE` is 0, `byte_142FEC54F` is 0, or the current index `dword_140D40948` is non-zero.
- V: increments the index and scans the second table's blocks for the next one whose qword at +144 is non-zero, up to 16, wrapping to 0.
- V: calls ScenePad_UpdateRepeat, then EventThread_Yield(0).

## State touched

- Calls: [ScenePad_UpdateRepeat](ScenePad_UpdateRepeat.md), [EventThread_Yield](EventThread_Yield.md)

## Referenced by

- Called by: [BattleAction_RunScript](BattleAction_RunScript.md), [BattleMenu_RunStep](BattleMenu_RunStep.md), [Battle_InitScene](Battle_InitScene.md), [Deployment_PlaceUnitAtCursor](Deployment_PlaceUnitAtCursor.md), [EventCamera_MoveTask](EventCamera_MoveTask.md), [EventChannel_StepTask](EventChannel_StepTask.md), [EventColorPath_Task](EventColorPath_Task.md), [EventColor_Task](EventColor_Task.md), [EventCounter_Task](EventCounter_Task.md), [EventEndSlate_ShowTask](EventEndSlate_ShowTask.md), [EventFlagWait_Task](EventFlagWait_Task.md), [EventMapTitle_SweepTask](EventMapTitle_SweepTask.md), [EventMessage_Task](EventMessage_Task.md), [EventObject_MoveWorker](EventObject_MoveWorker.md), [EventPanel_PickRow](EventPanel_PickRow.md), [EventPanel_QueueAndWait](EventPanel_QueueAndWait.md), [EventPanel_ShowTask](EventPanel_ShowTask.md), [EventPanel_ShowWaitTask](EventPanel_ShowWaitTask.md), [EventPreviewUnits_RunFrames](EventPreviewUnits_RunFrames.md), [EventScript_LoadCurrent](EventScript_LoadCurrent.md), [EventScript_LoadIntoBuffer](EventScript_LoadIntoBuffer.md), [EventScript_Run](EventScript_Run.md), [EventSequence_RecordTask](EventSequence_RecordTask.md), [EventSequencer_TakeTurn](EventSequencer_TakeTurn.md), [EventSprite_LoadTask](EventSprite_LoadTask.md), [EventStateTrack_RunTask](EventStateTrack_RunTask.md), [EventState_MoveTask](EventState_MoveTask.md), [EventSubScript_RunTask](EventSubScript_RunTask.md), [EventSubquestPanel_Run](EventSubquestPanel_Run.md), [EventUnitBlock_RunTask](EventUnitBlock_RunTask.md), [EventUnitMove_Task](EventUnitMove_Task.md), [EventUnitStatus_ApplyTask](EventUnitStatus_ApplyTask.md), [EventUnitStatus_RunMembers](EventUnitStatus_RunMembers.md), [EventVoice_PlayTask](EventVoice_PlayTask.md), [LegacyTask12_Build](LegacyTask12_Build.md), [SceneMsgTask_Run](SceneMsgTask_Run.md), [SceneUnit_Oscillate120](SceneUnit_Oscillate120.md), [WindowPattern_Build](WindowPattern_Build.md), [sub_1401EA2F0](sub_1401EA2F0.md), [sub_14020A7F0](sub_14020A7F0.md), [sub_140214404](sub_140214404.md), [sub_140214610](sub_140214610.md), [sub_14022F868](sub_14022F868.md), [sub_140233588](sub_140233588.md), [sub_140237CD0](sub_140237CD0.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md), [sub_1402C80D8](sub_1402C80D8.md), [sub_1402F8684](sub_1402F8684.md), [sub_1402F9F20](sub_1402F9F20.md), [sub_140300768](sub_140300768.md), [sub_140300D74](sub_140300D74.md), [sub_1403015A4](sub_1403015A4.md), [sub_140323D1C](sub_140323D1C.md), [sub_140324658](sub_140324658.md), [sub_140338A28](sub_140338A28.md), [sub_14033A37C](sub_14033A37C.md), [sub_1403980AC](sub_1403980AC.md), [sub_140399A64](sub_140399A64.md)
- Called by event opcodes: [0x13](../opcodes/README.md), [0x16](../opcodes/README.md), [0x18](../opcodes/README.md), [0x22](../opcodes/README.md), [0x27](../opcodes/README.md), [0x39](../opcodes/README.md), [0x3A](../opcodes/README.md), [0x3C](../opcodes/README.md), [0x3D](../opcodes/README.md), [0x42](../opcodes/README.md), [0x48](../opcodes/README.md), [0x4B](../opcodes/README.md), [0x4C](../opcodes/README.md), [0x4D](../opcodes/README.md), [0x4F](../opcodes/README.md), [0x50](../opcodes/README.md), [0x51](../opcodes/README.md), [0x56](../opcodes/README.md), [0x57](../opcodes/README.md), [0x58](../opcodes/README.md), [0x60](../opcodes/README.md), [0x64](../opcodes/README.md), [0x65](../opcodes/README.md), [0x6F](../opcodes/README.md), [0x72](../opcodes/README.md), [0x7B](../opcodes/README.md), [0x7E](../opcodes/README.md), [0x80](../opcodes/README.md), [0x82](../opcodes/README.md), [0x8E](../opcodes/README.md), [0x90](../opcodes/README.md), [0x96](../opcodes/README.md), [0xDB](../opcodes/README.md), [0xE3](../opcodes/README.md), [0xE5](../opcodes/README.md), [0xF0](../opcodes/README.md), [0xF1](../opcodes/README.md)
- Observed behaviours: [AFaultInAGameTaskFreezesTheGame](../behaviors/AFaultInAGameTaskFreezesTheGame.md)

## Notes

Same structure as EventTask_WaitFrame, but on `off_140783088` and `dword_140D40948`.

## Open questions

None recorded.
