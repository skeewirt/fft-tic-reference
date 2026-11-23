# OpeningToTitle

- **Kind:** flow
- **Area:** [Application and startup](../areas/app-startup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The opening's route to the title and back. A mode-0 scene start loads the opening page and pushes task 0; task 0 waits for any requested movie, then starts the title scene (task 14). The title's New Game hand-off (result 1 -> task 15 -> row 1 -> task 1) leaves through task 1, the exit gate; the scripted stage chain (4 -> 5 -> 6 -> 1) is separate and has no established entry. Task 13, pushed from the title, restarts the mode-0 opening from the same first task.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="0"></a>0 | [Scene_Init](../functions/Scene_Init.md) | V | Mode 0: clears the page index, resets the scene flags and the task depth, and calls `OpeningScene_Start`. |
| <a id="1"></a>1 | [OpeningScene_Start](../functions/OpeningScene_Start.md) | V | Loads opening row 17, or row 0 on the `g_ShopModeGate` path where it may also show the title menu; clears flag bit 6, sets bit 1, ends any pending UI fade, pushes id 0 and writes 86999 and 10261 to the first scene frame. |
| <a id="2"></a>2 | [OpeningTask_0](../functions/OpeningTask_0.md) | V | While `g_MovieRequestId` is 0 or greater the task returns and stays on top. When it is -1 it clears bit 1, pops itself and calls `TitleScene_Start`. |
| <a id="3"></a>3 | [TitleScene_Start](../functions/TitleScene_Start.md) | V | `TitleScene_Start` resets the scene state, builds the title menu and pushes task 14 (`TitleScene_Task`). Task 0 never pushes an opening stage. |
| <a id="4"></a>4 |  | V | The New Game hand-off: the helper `sub_1402F0084` loads opening row 1, clears flag bit 6 and pushes task 1. Task 15 (pushed by case 1 of `TitleScene_Task`) and task 6 call it. |
| <a id="5"></a>5 | [OpeningTask_1](../functions/OpeningTask_1.md) | V | Task 1 clears bit 1 when no movie is requested, pops itself, sets bit 6 and either calls `Opening_EndToTitle` (byte `g_GlobalWork+100` set) or writes hand-over code 0 and toggles the run bit (bit 0). |
| <a id="6"></a>6 | [OpeningStages](OpeningStages.md) | V | The scripted stage chain (separate pages) is 4 -> 5 -> 6 -> 1; task 7 is the return-to-title shortcut from task 4 state 5. The chain has no established entry in this build (no store of id 2 or 12). |
| <a id="7"></a>7 | [Opening_EndToTitle](../functions/Opening_EndToTitle.md) | V | Releases the three opening objects, clears bit 0 of `dword_143C51A40`, calls `Scene_Init(1)` (title start, task 14), then clears the two scene words and the qword after `g_ScreenFadeMode`. |
| <a id="8"></a>8 | [OpeningScene_Resume](../functions/OpeningScene_Resume.md) | V | Task 13, selected by case 3 of `TitleScene_Task`, sets bit 6, clears the page index, pops itself and re-enters `OpeningScene_Start`, which pushes task 0 again. |

## Behavior

- V: the mode-0 start and the stage chain are separate entry paths: task 0 always goes to `TitleScene_Start`, and task 1 is pushed by `sub_1402F0084`, not by task 0.
- V: task 1 and `Opening_EndToTitle` are the two exits: task 1 leaves with hand-over code 0 unless `g_GlobalWork+100` is set, and `Opening_EndToTitle` resets the scene into the title.
- V: `OpeningScene_Resume` does not restore a frame: it resets the page index and re-enters the same start function, which always pushes id 0 and writes the same two frame dwords.
- V: a scan of the stores to `dword_1418772E0` finds ids 0, 1, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14 and 15; no store of 2 or 12 was found. The helper that pushes 4 is called only by tasks 2 and 12, and the helper that pushes 3 only by task 2, so the route into the 4-7 chain is not established in this build.
- I: the title is the hub: the mode-0 start lands there through task 0, the opening stages return there through `Opening_EndToTitle`, and task 13 comes back from it (rests on the three paths).
- ?: what the two frame dwords mean; what `g_GlobalWork+100` selects; and what title action leads to case 3.

## Notes

Read the five assigned functions whole, plus `Scene_Init`, `TitleScene_Start`, `TitleScene_Task`, `sub_14037F354`, `sub_1402F0084`, `sub_1402F0C14` and the stage functions around their pushes and ends. Task 0 does not push task 1; task 1 is pushed by `sub_1402F0084`.

## Open questions

What enters task 2 or 12 (no store found); what the frame dwords and `g_GlobalWork+100` select; which title result is case 3.
