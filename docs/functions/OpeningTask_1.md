# OpeningTask_1

- **Address:** `0x1402F00D4`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 OpeningTask_1(void)`
- **Callers:** tbl_OpeningTaskSteps id 1, dispatched by SceneLoop_Run (0x140331D2D) and SceneLoop_RunAlt (0x14039DE79)
- **Callees:** Opening_EndToTitle

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task 1: the opening's exit gate. It waits while scene flag bit 1 is set, then pops itself and either ends to the title (byte `g_GlobalWork+100` non-zero) or writes hand-over code 0 and toggles the scene run bit (bit 0).

## Behavior

- V: reads `dword_141876EE8`; if `g_MovieRequestId` is -1 it clears bit 1 (0x02) in the local copy and in the global. If bit 1 is still set it returns without changing the stack.
- V: with bit 1 clear it sets bit 6 (0x40), decrements the task depth `dword_141877480` (a pop) and writes the flags back.
- V: if the byte at `g_GlobalWork+100` is non-zero it jumps to `Opening_EndToTitle` without further writes.
- V: otherwise it stores 0 in `dword_141876F94` and toggles bit 0 (0x01) of `dword_141876EE8` (XOR; I: the bit is set while the scene loop runs, so this clears it and the loop ends with hand-over code 0).
- I: bit 1 is the same movie wait task 0 uses: `OpeningScene_Start` and case 4 of `TitleScene_Task` set it, and tasks 0, 1 and 11 clear it when no movie is requested (rests on those four sites).
- I: task 1 is entered from the title hand-off, not from task 0: the helper `sub_1402F0084` stores id 1 and is called by task 15 (pushed by case 1 of `TitleScene_Task`) and by task 6 after the date confirm (rests on the store and the two call sites).
- ?: what writes `g_GlobalWork+100`; that byte alone selects the end-to-title branch.

## State touched

- Calls: [Opening_EndToTitle](Opening_EndToTitle.md)
- Reads: [g_MovieRequestId](../globals/g_MovieRequestId.md), [g_GlobalWork](../globals/g_GlobalWork.md)

## Referenced by

- Appears in flows: [OpeningToTitle](../flows/OpeningToTitle.md), [OpeningTransitionTasks](../flows/OpeningTransitionTasks.md)

## Notes

Whole function read (77 bytes). IDB name `OpeningTask_1`. The result register is not set on the wait path; the dispatch ignores it. `sub_1402F0084` (0x1402F0084) clears flag bit 6 and loads row 1 before pushing id 1.

## Open questions

What sets the `g_GlobalWork+100` byte, and whether the date-confirm path (task 6) or the title hand-off (task 15) is the normal entry.
