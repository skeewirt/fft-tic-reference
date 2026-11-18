# EventTask_WaitFrame

- **Address:** `0x1402F2C14`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventTask_WaitFrame(void)`
- **Callers:** About 70 callers across the event, world-map and battle code.
- **Callees:** EventPad_UpdateRepeat, EventThread_Yield

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The event system's wait-one-frame primitive: moves on to the next runnable task, refreshes the held-button repeat state, then yields. About 70 routines call it to wait.

## Behavior

- V: increments the current-task index `dword_14184B22C`, then scans forward through the task blocks (2048 bytes each, base `off_14078D5D8`) for the next one whose qword at +144 is non-zero, up to index 17, wrapping to 0.
- V: calls EventPad_UpdateRepeat, then returns EventThread_Yield(0).
- V: used in wait loops such as `sub_1402E9980`, which spins on this call until a request flag clears.
- I: the non-zero qword at +144 marks a task as runnable.

## State touched

- Calls: [EventPad_UpdateRepeat](EventPad_UpdateRepeat.md), [EventThread_Yield](EventThread_Yield.md)

## Referenced by

- Called by: [BattleMsg_SetCellText](BattleMsg_SetCellText.md), [EventMessage_Scripted](EventMessage_Scripted.md), [LegacyOptions_DrawTask](LegacyOptions_DrawTask.md), [LegacyOptions_Open](LegacyOptions_Open.md), [ScreenTaskSet_Run](ScreenTaskSet_Run.md), [WindowRect_AnimateCurve](WindowRect_AnimateCurve.md), [sub_1402DF374](sub_1402DF374.md), [sub_14032B1A4](sub_14032B1A4.md), [sub_14032EDB8](sub_14032EDB8.md), [sub_14032F410](sub_14032F410.md), [sub_14032F9F8](sub_14032F9F8.md), [sub_140364408](sub_140364408.md)

## Notes

EventTask_Terminate uses the same scan with a bound of 16.

## Open questions

The layout of the 2048-byte task block beyond the fields at +144 and +152.
