# Opening_EndToTitle

- **Address:** `0x14037DE18`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `char __fastcall Opening_EndToTitle(void)`
- **Callers:** OpeningTask_1 (0x1402F010B), OpeningTask_4 (0x14037DECF), OpeningTask_5 (0x14037E8F6), OpeningTask_6 (0x14037EE6C)
- **Callees:** Scene_Init, sub_14033E898

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Ends the opening and resets the scene into the title path: it releases the three opening objects, clears the scene-object bit, calls `Scene_Init(1)` so `TitleScene_Start` pushes task 14, then clears the two scene words and the qword after `g_ScreenFadeMode`.

## Behavior

- V: for each of `qword_143C51A30`, `qword_143C51A38` and `qword_143C51A48`: if non-null, calls `sub_14033E898` and stores null.
- V: clears bit 0 of `dword_143C51A40`.
- V: calls `Scene_Init` with 1. That resets the scene globals and the task depth, and its non-zero path calls `TitleScene_Start`, which builds the title menu and pushes task 14.
- V: after `Scene_Init` returns, clears `word_141874530` when it is non-zero, always clears `word_141874534`, and clears the qword at `g_ScreenFadeMode+4`.
- V: its callers are the four opening tasks 1, 4, 5 and 6; task 1 reaches it by a tail jump.
- I: the three trailing clears repeat the `SceneLoop_Run` epilogue (same words and qword, written when that loop returns), so this path performs the loop's exit cleanup itself instead of returning to it (rests on the identical write set).
- ?: what the three released objects are and what the two words and the qword track.

## State touched

- Calls: [Scene_Init](Scene_Init.md)

## Referenced by

- Appears in flows: [OpeningStages](../flows/OpeningStages.md), [OpeningToTitle](../flows/OpeningToTitle.md)
- Called by: [OpeningTask_1](OpeningTask_1.md), [OpeningTask_4](OpeningTask_4.md), [OpeningTask_5](OpeningTask_5.md), [OpeningTask_6](OpeningTask_6.md)

## Notes

Whole function read (133 bytes). IDB name `Opening_EndToTitle`. `Scene_Init(1)` is the only scene reset; this function does not edit the task stack directly. The clears after `Scene_Init` are the same ones `SceneLoop_Run` makes after its loop.

## Open questions

What the three objects are, and why the two words and the qword are cleared after the title start rather than before it.
