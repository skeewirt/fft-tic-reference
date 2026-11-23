# SceneCallback_Dispatch

- **Address:** `0x1402F7D1C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneCallback_Dispatch(int64_t mode, int64_t arg)`
- **Callers:** 17 routines (25 call sites): EventScript_Run (4), sub_140234990 (3), sub_14024138C (3), sub_1402C538C (2), and about 13 others such as BattleTask_ActorForecastPanel, sub_14022EFF4, sub_140234360, sub_14023987C, sub_140241080, sub_140241BD0, sub_140243330, sub_140243364, sub_1402FC484, sub_1403006B8 and sub_14032437C. Two of the callers, sub_14033D4C0 and the routine named NaptrDnsRecordConvert_1 in the IDB, are outside the event code.
- **Callees:** qword_140D40940 (indirect call through the pointer the caller set)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Calls the callback in the global function pointer `qword_140D40940` for modes 0 to 6. The caller sets that pointer first; the mode decides what the callback receives.

## Behavior

- V: if `dword_140D40948` (the current task index) is not zero, it writes zero to the qwords at +96 and +104 of block 0 of the task table `off_140783088`, whatever the index is.
- V: mode 0 calls qword_140D40940 with the mode (0) as its argument.
- V: modes 1 to 6 call it with `arg`, and its return value is returned.
- V: any other mode returns 0 without calling anything.
- V: the callback pointer is not tested for null. Callers in the visible code use modes 1, 2, 3 and 4. EventScript_Run uses mode 1 three times and mode 3 once.
- V: some callers pass more arguments than the two declared here; the extra values are ignored.

## Referenced by

- Called by: [BattleTask_ActorForecastPanel](BattleTask_ActorForecastPanel.md), [EventPanel_QueueAndWait](EventPanel_QueueAndWait.md), [EventPanel_ShowTask](EventPanel_ShowTask.md), [EventScript_SkipTick](EventScript_SkipTick.md), [EventUnitStatus_DispatchActiveIcons](EventUnitStatus_DispatchActiveIcons.md), [EventUnitStatus_SetBit](EventUnitStatus_SetBit.md), [Music_StartSceneTracks](Music_StartSceneTracks.md), [Scene_StartMusic](Scene_StartMusic.md), [sub_14024138C](sub_14024138C.md)
- Called by event opcodes: [0x28](../opcodes/README.md), [0x44](../opcodes/README.md), [0x45](../opcodes/README.md), [0x87](../opcodes/README.md)

## Notes

About 35 routines reference qword_140D40940, EventScript_Run among them. This pass did not separate its reads from its writes.

## Open questions

Who sets qword_140D40940 for the event system and what each mode does in the callback; why modes 5 and 6 have no callers in the code read; what the two words at block 0 +96 and +104 are used for.
