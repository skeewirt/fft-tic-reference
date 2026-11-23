# OpeningTransitionTasks

- **Kind:** flow
- **Area:** [Application and startup](../areas/app-startup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The hand-off tasks between the front end's three loops. The title's New Game result pushes task 15, which loads opening row 1 and task 1; the title's idle result pushes task 11, which waits out a demo movie and re-enters the opening start; the alternate loop starts at task 9, which requests PSP movie row 0x10, and task 10 closes its screen and clears the run bit. Task 12 is the opening's skip/continue gate, but no store of id 12 exists, so it does not run in this build.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="0"></a>0 | [TitleScene_Task](../functions/TitleScene_Task.md) | V | Result 1 (New Game): pops task 14, runs `sub_14037FF14(0)` and `LegacyMenu_InitWorld`, loads PSP movie row 0x15 and pushes task 15. |
| <a id="1"></a>1 | [TitleScene_NewGameHandoff](../functions/TitleScene_NewGameHandoff.md) | V | Task 15 waits while `g_MovieRequestId` is 0 or greater, pops itself, sets the page index to 1 and calls `sub_1402F0084`, which loads PSP movie row 1 and pushes task 1. |
| <a id="2"></a>2 | [OpeningTask_1](../functions/OpeningTask_1.md) | V | Task 1 waits for the movie, then either writes hand-over code 0 and toggles bit 0 of `dword_141876EE8` (normally set, so this clears it), or ends to the title through `Opening_EndToTitle` when `g_GlobalWork+100` is set. |
| <a id="3"></a>3 | [TitleScene_DemoReturn](../functions/TitleScene_DemoReturn.md) | V | Result 4 (idle timeout): the title task loads PSP movie row 18, 19 or 20, sets scene flag bit 1 and pushes task 11. Task 11 waits for that movie, pops itself, sets the page index to 1 and re-enters `OpeningScene_Start`. |
| <a id="4"></a>4 | [OpeningScene_Start](../functions/OpeningScene_Start.md) | V | Loads PSP movie row 17 (row 0 when `g_ShopModeGate` is set), sets scene flag bit 1, ends the UI fade and pushes task 0. Task 0 waits for the movie, pops and starts the title scene, so the idle path is a loop back to task 14. |
| <a id="5"></a>5 | [SceneLoop_RunAlt](../functions/SceneLoop_RunAlt.md) | V | The alternate loop resets the scene words inline, loads the 0x8800-byte data run, requests PSP movie row 9, pushes task 9 and runs the same dispatch until scene flag bit 0 clears. |
| <a id="6"></a>6 | [OpeningTask_9](../functions/OpeningTask_9.md) | V | Task 9 clears scene flag bit 1 when no movie is pending, sets bit 6, pops itself, requests PSP movie row 0x10, writes event id 16 and pushes task 10. |
| <a id="7"></a>7 | [OpeningTask_10](../functions/OpeningTask_10.md) | V | Task 10 waits while `g_MovieRequestId` is 0 or greater, fades the +400 UI screen to state 15, waits for its state 4/1, detaches the add-on, releases three pointers and toggles scene flag bit 0, which ends the loop when it runs. |
| <a id="8"></a>8 | [OpeningTask_12](../functions/OpeningTask_12.md) | V | The gate that is not entered: with no fade running it offers cancel (script id 0x1B) or accept (0x1A or 0x1F); cancel refills the scene buffer and calls `TitleScene_Start`, accept calls `Opening_LoadMessageSprites`, which pushes task 4. No store of id 12 exists. |

## Behavior

- V: the title has four result paths: result 1 pushes 15, result 2 ends the scene and writes the hand-over code, result 3 replaces the top id with 13, and result 4 pushes 11.
- V: task 15 -> `sub_1402F0084` -> task 1 is the New Game hand-off; task 11 -> `OpeningScene_Start` -> task 0 is the idle/attract return.
- V: the alternate loop is the only path that starts at task 9; task 9 always pushes 10, and task 10 is the only task in that loop that toggles scene flag bit 0.
- V: ids 8 and 12 have no store site. Ids 2 and 12 are the only table handlers that enter the stage chain 4-7, so that chain is not reached from either loop in this build.
- V: task 10's first test is `g_MovieRequestId`, not the adjacent `dword_142E7FB00` the decompiler prints.
- I: task 10's exit tail is the loop's intended end, but the three pointers it releases are never written and start at -1, so whether the tail runs is open (rests on the -1 initial values and the release helper's pointer use).
- ?: which movies rows 0x10, 1, 17, 18, 19 and 20 are; why the event id is 16; and whether the alternate loop runs for every transition mode 3.

## Notes

Read the six group-B handlers whole, plus `TitleScene_Task`, `TitleScene_Start`, `TitleScene_Update`, `OpeningScene_Start`, `OpeningTask_0`, `OpeningTask_1`, `OpeningTask_4`, `OpeningTask_7`, `SceneLoop_RunAlt`, `sub_1402F0084` and the store sites of the task ids. The title's result meanings rest on the agent state words 0x0101/0x0201/0x0301/0x0401/0x0701 written by the title screens and on the stage switch in `TitleScene_Update`. `OpeningTask_0`, `OpeningTask_1` and `OpeningTask_4` are referenced here only for the hand-off.

## Open questions

Which movie rows the four title hand-offs request; what the `g_GlobalWork+100` byte selects at task 1; and whether the alternate-loop tail is reachable as shipped.
