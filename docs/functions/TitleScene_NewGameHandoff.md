# TitleScene_NewGameHandoff

- **Address:** `0x1402F0C14`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall sub_1402F0C14(void)`
- **Callers:** SceneLoop_Run (0x140331D2D), SceneLoop_RunAlt (0x14039DE79), both indirect through SceneTaskTable; pushed by TitleScene_Task (0x1402F0B47)
- **Callees:** sub_1402F0084

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task 15: the title's new-game hand-off. It waits for the current movie to end, pops itself, sets the page index to 1 and calls the helper that loads opening row 1 and pushes task 1.

## Behavior

- V: it reads `g_MovieRequestId`; while the value is 0 or greater it returns and leaves the task stack and every global unchanged.
- V: with `g_MovieRequestId` at -1 it decrements the task depth `dword_141877480` (a pop), stores 1 in `dword_1418825EC` (the page index) and calls `sub_1402F0084`.
- V: `sub_1402F0084` calls `sub_140257384(1)` and `sub_140257440()` (PSP movie-file row 1), clears scene flag bit 6, writes 1 to `dword_143807794` and pushes task 1.
- V: it then stores 1 in `g_ScreenFadeMode` (0x142FF9E00).
- V: `TitleScene_Task` pushes id 15 at 0x1402F0B47 on result 1, after `sub_14037FF14(0)` has generated the starting party and `LegacyMenu_InitWorld` has run; this is the only store of 15.
- V: on the task-1 path `OpeningTask_1` waits for the movie, then either writes hand-over code 0 and toggles bit 0 of `dword_141876EE8`, or ends to the title when the byte at `g_GlobalWork+100` is set. I: the bit is normally set, so the toggle clears it and ends the loop.
- I: result 1 is the New Game action: the title task resets the party and the world menu, task 15 switches to opening row 1 and task 1 is the point where the scene loop hands the new game back to `Game_MainLoop` (rests on the reset calls, the row-1 load and task 1's hand-over).
- ?: what row 1 selects, and what the `g_GlobalWork+100` byte selects at task 1.

## State touched

- Reads: [g_MovieRequestId](../globals/g_MovieRequestId.md)

## Referenced by

- Appears in flows: [OpeningTransitionTasks](../flows/OpeningTransitionTasks.md), [TitleSceneFlow](../flows/TitleSceneFlow.md)

## Notes

Whole body read (49 bytes), plus `sub_1402F0084` for the row and the push. The task seeds no frame fields; task 1 does not read the frame either. `g_ScreenFadeMode` has no global record, so it is named only in the text.

## Open questions

What row 1 selects; what the `g_GlobalWork+100` byte selects at task 1; and whether any title path other than result 1 pushes 15.
