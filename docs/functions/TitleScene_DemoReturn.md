# TitleScene_DemoReturn

- **Address:** `0x14037F354`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall sub_14037F354(void)`
- **Callers:** SceneLoop_Run (0x140331D2D), SceneLoop_RunAlt (0x14039DE79), both indirect through SceneTaskTable; pushed by TitleScene_Task (0x1402F0A03) and sub_1402F0124 (0x1402F027D)
- **Callees:** OpeningScene_Start

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task 11: the return from the title's attract demo. The title task pushes it after requesting one of three demo movies; it waits for that movie, pops itself, sets the page index to 1 and re-enters `OpeningScene_Start`, which pushes task 0.

## Behavior

- V: it reads `dword_141876EE8`; when `g_MovieRequestId` is below zero it clears bit 1 (0x02) and stores the word back. When a movie is still requested it keeps bit 1.
- V: if bit 1 is still set it returns and leaves the task stack, the flag word and every other global unchanged.
- V: with bit 1 clear it decrements the task depth `dword_141877480` (a pop), sets bit 6 (0x40), stores the word, stores 1 in `dword_1418825EC` (the page index the loops use to pick the page blocks) and calls `OpeningScene_Start`.
- V: `OpeningScene_Start` clears bit 6, sets bit 1, requests PSP movie-file row 17 (row 0 when `g_ShopModeGate` is set), ends any pending UI fade and pushes task 0.
- V: `TitleScene_Task` pushes id 11 at 0x1402F0A03 on result 4, after it has loaded PSP movie-file row 18, 19 or 20 through `sub_140257384`/`sub_140257440` and set scene flag bit 1. `sub_1402F0124` pushes the same id at 0x1402F027D on the same three-row path.
- I: result 4 of `TitleScene_Task` is the title's idle-timeout result: the title agent's event handler is taken to set the agent's state word to 0x0701 when the idle event arrives, and `TitleScene_Update` maps that to stage 5 with result 4 (rests on the three demo-movie rows loaded on this path and the stage switch in `TitleScene_Update`; the agent's handler is not in the code examined here).
- I: the whole path is the attract loop: an idle title plays a demo movie (row 18/19/20), task 11 waits for it, and the opening start plays the opening movie (row 17) before task 0 takes the scene back to the title (rests on the three-row store, the movie test and task 0's `TitleScene_Start`).
- ?: which three movies rows 18/19/20 are, and why the page index is set to 1 rather than 0.

## State touched

- Calls: [OpeningScene_Start](OpeningScene_Start.md)
- Reads: [g_MovieRequestId](../globals/g_MovieRequestId.md)

## Referenced by

- Appears in flows: [OpeningTransitionTasks](../flows/OpeningTransitionTasks.md), [TitleSceneFlow](../flows/TitleSceneFlow.md)

## Notes

Whole body read (67 bytes). This is the same re-entry as `OpeningScene_Resume` with two differences: it sets the page index to 1 instead of 0, and it tests the movie bit first. `TitleScene_Task` case 4 loads the demo row and sets the bit-1 movie wait before the push.

## Open questions

Which movies rows 18/19/20 are; why the page index is 1; and whether the idle timeout is the only way to reach result 4.
