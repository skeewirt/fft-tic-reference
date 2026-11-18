# EventThread_Yield

- **Address:** `0x1402F377C`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t EventThread_Yield(int mode)`
- **Callers:** About 31 callers, including EventTask_WaitFrame and many world-map, battle and event routines.
- **Callees:** Windows thread/event APIs (GetCurrentThreadId, SetEvent, WaitForSingleObject), `longjmp`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Hands control from the calling event task back to the scheduler and sleeps until that task is resumed. Each event task runs on its own OS thread, and this is the baton hand-off.

## Behavior

- V: finds the calling thread in a 17-entry thread table (`qword_143CD9E98`, 96 bytes per entry, thread id at +24); index -1 if it is not listed.
- V: stores `(mode != 1) - 2` in `dword_1408115F4` (so -2 for mode 1, otherwise -1), signals the scheduler's event handle (table +1640), then blocks forever on the thread's own event handle (entry +48).
- V: once resumed it clears `dword_142FF9DE8` and `dword_142FF9DD8`, calls the optional hook `qword_14114B738`, and records its own index in `dword_140D40948` and in the current-task index `dword_14184B22C`.
- V: it then checks the task's 288-byte record in the table at `unk_143791D70`: when the pending-target field (+0) is non-null and differs from the field at +8 it long-jumps through the task's saved jump buffer with code 1; when the flag at +280 is set and both fields are non-null it long-jumps with code 2.
- V: SceneTask_Start writes the entry function into the record (+8) and sets the flags at +272 and +280, which is how a freshly started task is steered to its entry point through the code-2 jump.
- I: code 1 restarts a task whose recorded target differs from its requested entry; code 2 starts a newly created task.

## Referenced by

- Called by: [EventCmd_SetBackdrop](EventCmd_SetBackdrop.md), [EventTask_WaitFrame](EventTask_WaitFrame.md), [Opening_LoadMessageSprites](Opening_LoadMessageSprites.md), [Save_BootClear](Save_BootClear.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md)

## Notes

The scheduler side is the main loop thread (entry 0 of the thread table); tasks are entries 1-16.

## Open questions

Which scheduler routine wakes the next task.
