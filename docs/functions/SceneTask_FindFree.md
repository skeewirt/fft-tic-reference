# SceneTask_FindFree

- **Address:** `0x1402424DC`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `int64_t SceneTask_FindFree(int64_t slot)`
- **Callers:** 6 routines (31 call sites): EventScript_Run (23), sub_1402C72B8 (3), sub_1402C6514 (2), sub_1402C7DAC, sub_1402CB9E8 and sub_14038FE58.
- **Callees:** SceneTask_Terminate (only when no slot is free; it takes no argument, so the value left in the register is not used)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds a free slot in the second task table for a task that the caller is about to start with SceneTask_Start. EventScript_Run passes 16, which asks for any free slot from 1 to 16.

## Behavior

- V: reads the high dword of `qword_142FF9EC0` as a 32-bit mask `m`; bit n of `m` marks slot n as taken.
- V: when the argument is 16 or more, or its bit in `m` is set, it searches slots 1 to 16 from the start for one whose bit is clear and whose runnable qword (block +144 in `off_140783088`) is zero.
- V: if that search fails, it searches again from slot 1 for a slot whose runnable qword is zero; this second search does not check the mask.
- V: if the second search fails, it calls SceneTask_Terminate, which ends the current task, and returns 0.
- V: when the argument is below 16 and its bit is clear, it returns the argument at once, without checking its runnable qword.
- V: the bit test uses only the low 8 bits of the argument. Task blocks are 2048 bytes apart in `off_140783088`, so the runnable qword of slot n is at byte offset 2048 * n + 144.
- V: EventScript_Run passes 16 at 22 of its 23 calls. The other call passes a value from ScenePreview_IndexOfSlot.

## State touched

- Calls: [SceneTask_Terminate](SceneTask_Terminate.md)

## Referenced by

- Called by: [EventMode_DispatchTask](EventMode_DispatchTask.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md)

## Notes

The function does not start a task. It is called before SceneTask_Start, and SceneTask_Start is not one of its callers. I: the returned slot is the one the caller then starts.

## Open questions

What sets the high dword of qword_142FF9EC0 and what its bits mean; what the callers do when it returns 0, since only EventScript_Run's calls were read.
