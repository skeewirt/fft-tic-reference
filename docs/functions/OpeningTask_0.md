# OpeningTask_0

- **Address:** `0x1402F0060`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 OpeningTask_0(void)`
- **Callers:** tbl_OpeningTaskSteps id 0, dispatched by SceneLoop_Run (0x140331D2D) and SceneLoop_RunAlt (0x14039DE79)
- **Callees:** TitleScene_Start

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task 0: the bridge from the mode-0 opening start to the title scene. It leaves the stack untouched while a movie is requested; with no movie requested it clears the opening's wait bit, pops itself and calls `TitleScene_Start`.

## Behavior

- V: tests `g_MovieRequestId` against -1 (no movie). While the value is 0 or greater it returns without writing the task stack, the scene flags or any other global, so the dispatcher runs the same task again next frame.
- V: when the value is -1 it clears bit 1 (0x02) of `dword_141876EE8`, decrements the task depth `dword_141877480` (a pop) and calls `TitleScene_Start`.
- V: `TitleScene_Start` resets the scene state, builds the title menu and pushes task 14 (`TitleScene_Task`); task 0 never stores an opening stage id.
- I: bit 1 is the opening's movie wait: `OpeningScene_Start` sets it and this task clears it only once no movie is requested (rests on the two sites).
- ?: what requests a movie when the mode-0 scene starts; the code here only observes the request.

## State touched

- Calls: [TitleScene_Start](TitleScene_Start.md)
- Reads: [g_MovieRequestId](../globals/g_MovieRequestId.md)

## Referenced by

- Appears in flows: [OpeningToTitle](../flows/OpeningToTitle.md)

## Notes

Whole function read (36 bytes). Named for its slot in the scene task table. The return register is not set on the movie path and the dispatch ignores handler returns. The function has no other caller.

## Open questions

What sets `g_MovieRequestId` to a movie id at opening start, and whether any path clears bit 1 other than tasks 0, 1 and 11.
