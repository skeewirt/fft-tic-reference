# EventThread_ReturnToEntry

- **Address:** `0x1402F3710`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventThread_ReturnToEntry(void)`
- **Callers:** EventTask_Terminate, `sub_1402F7EC8`
- **Callees:** `longjmp`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Restarts the calling event task thread from its saved entry context.

## Behavior

- V: finds the calling thread in the 17-entry thread table (`qword_143CD9E98`).
- V: for any entry above 0 it clears a dword at +272 and a qword at +8 of the task's 288-byte record at `unk_143791D70` and long-jumps to that record's saved jump buffer with code 1.
- V: if the thread is not in the table, or is entry 0 (the scheduler), it returns without jumping.

## Referenced by

- Called by: [EventTask_Terminate](EventTask_Terminate.md), [SceneTask_Terminate](SceneTask_Terminate.md)

## Notes

Together with EventThread_Yield this is how a task is stopped and restarted without destroying its thread.

## Open questions

None recorded.
