# TitleSceneFlow

- **Kind:** flow
- **Area:** [Application and startup](../areas/app-startup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How the Enhanced title scene advances from the scene reset to a menu hand-off. `Scene_Init` or another start caller enters `TitleScene_Start`, which resets the game and party state and pushes task 14. Task 14 runs `TitleScene_Update` once per dispatch; the update shows and waits on the title menu, sends the New Game + and Load Game choices through the save/load screen, and writes a result that `TitleScene_Task` turns into task 15, task 13, task 11, or the end of the scene.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="0"></a>0 | [Scene_Init](../functions/Scene_Init.md) | V | A non-zero mode calls `TitleScene_Start`; the mode-0 branch calls `OpeningScene_Start` instead. `Scene_Init` itself does not push a task. |
| <a id="1"></a>1 | [TitleScene_Start](../functions/TitleScene_Start.md) | V | Resets the event/legacy scene state and the game/party state, allocates the eight-byte title scene frame, shows the title menu (or seeds the save-return result 2), and pushes task id 14. |
| <a id="2"></a>2 | [TitleScene_Task](../functions/TitleScene_Task.md) | V | The scene loop dispatches the top id; id 14 is `TitleScene_Task`, which calls `TitleScene_Update` with the frame at `g_UIStateFade+48`. |
| <a id="3"></a>3 | [TitleScene_Update](../functions/TitleScene_Update.md) | V | State 1 waits until the title menu add-on is idle. State 0 re-shows the menu through `UITitle_ShowMenu`. |
| <a id="4"></a>4 | [UITitle_OnMenuAction](../functions/UITitle_OnMenuAction.md) | V | The chosen menu row is carried out: New Game opens the play mode screen, Continue runs inside `UIAgentFFTOTitle_Update`, Load Game and New Game + open the save/load screen, and Music Player and Select Version set their own fade/next-state values. |
| <a id="5"></a>5 | [UISaveLoad_Open](../functions/UISaveLoad_Open.md) | V | Load Game opens the save/load agent in mode 2; New Game + opens the same screen and then switches the agent's mode field to 4. The function only sets the save/load agent's state; it pushes no scene task. |
| <a id="6"></a>6 | [UIAgentFFTOTitle_Update](../functions/UIAgentFFTOTitle_Update.md) | V | Continue loads the newest save inside the title agent (manual-slot scan, resume header, load or resume materialiser) and ends by writing next_state 4. |
| <a id="7"></a>7 | [TitleScene_Update](../functions/TitleScene_Update.md) | V | When the menu or the opened screen reports idle, the update turns the title agent's next_state into a scene result: 1 -> New Game, 2 -> hand-over, 3 -> opening restart, 4 -> idle/attract restart. Load Game also checks `g_GlobalWork+102`; New Game + also checks `g_GlobalWork+128`. |
| <a id="8"></a>8 | [TitleScene_Task](../functions/TitleScene_Task.md) | V | Result 1 pushes task 15 (`TitleScene_NewGameHandoff`), result 2 pushes nothing and ends the scene loop, result 3 replaces task 14 with task 13 (`OpeningScene_Resume`), and result 4 pushes task 11 (`TitleScene_DemoReturn`). The scene loop dispatches the new top id next frame. |
| <a id="8a"></a>8a | [OpeningScene_Resume](../functions/OpeningScene_Resume.md) | V | Task 13 sets scene flag bit 6, clears the page index, pops itself and re-enters `OpeningScene_Start`, which pushes task 0 and restarts the mode-0 opening. |
| <a id="9"></a>9 | [TitleScene_NewGameHandoff](../functions/TitleScene_NewGameHandoff.md) | V | Task 15 waits for the requested movie, pops itself, sets the page index to 1, loads opening row 1 and pushes task 1. |
| <a id="10"></a>10 | [TitleScene_DemoReturn](../functions/TitleScene_DemoReturn.md) | V | Task 11 waits for the demo movie, pops itself, sets the page index to 1 and scene flag 0x40, and re-enters `OpeningScene_Start`, which pushes task 0. |

## Behavior

- V: `Scene_Init` only calls `TitleScene_Start` for a non-zero mode; `TitleScene_Start` is also called by opening task 0, opening task 2, `OpeningTask_7` and `sub_14037F398`, so the title can be re-entered without `Scene_Init`.
- V: the title scene frame is eight bytes at `g_UIStateFade+48`; +0 is the state and +1 is the result. `TitleScene_Update` reads and writes those two bytes; `TitleScene_Start` allocates the buffer, and `TitleScene_Task` calls `sub_1401DDCFC(g_UIStateFade)` at the end of every non-zero result.
- V: state 1 of the update reads the title agent's next_state at +89: 1 = New Game confirmed on the play mode screen, 2 = New Game +, 3 = Load Game, 4 = Continue finished, 5 = Music Player, 6 = Select Version, 7 = title menu idle timeout.
- V: New Game + and Load Game both use the save/load screen but test different fields afterwards: New Game + tests `g_GlobalWork+128` (set to -1 before the screen opens) and Load Game tests `g_GlobalWork+102` (set to 1 when a load is confirmed).
- I: the New Game + -1 value means the screen was backed out, so the menu is shown again; any other value means a source save was chosen and the play mode screen opens (rests on the state-2 branches).
- V: the update's navigation states 2 (play mode screen not chosen), 3 (`g_GlobalWork+102` clear) and 4 return to state 1 without a result; the result 1..4 that task 14 acts on is written by state 1 (from next_state) and by state 3 (result 2 when `g_GlobalWork+102` is non-zero). State 5 has no branch and writes nothing.
- V: result 1 pushes task 15 after `GameState_ResetParty(0)` clears the game tables and fills one starting unit; result 2 writes the loop hand-over code `dword_141876F94` (3 for the save-return path, else 0 or 1 from event variables 85 and 100) and toggles scene flag bit 0 to end the loop; result 3 replaces the top id with 13; result 4 pushes task 11 after selecting one of NXD table-66 rows 18, 19 or 20.
- V: task 15 (`TitleScene_NewGameHandoff`) waits for the requested movie, pops itself, sets page index 1, loads opening row 1 and pushes task 1; task 11 (`TitleScene_DemoReturn`) waits for the demo movie, pops itself, sets page index 1 and scene flag 0x40, and re-enters `OpeningScene_Start`.
- I: the flow is menu-driven and never loads a save in the title task itself: Continue is the only path that loads inside the title agent, while Load Game and New Game + delegate to the save/load agent and come back through `g_GlobalWork` (rests on the update branches and on `UISaveLoad_Open` setting no scene task).
- ?: what event variables 85 and 100 mean, and whether the three NXD rows 18, 19 and 20 are the demo movies task 11 waits for.

## Notes

Covers the four title-scene functions, the title agent's next_state setters, the save/load open and terminal states, and the next-task bodies 11, 13 and 15. Task 13 (`OpeningScene_Resume`), task 11 (`TitleScene_DemoReturn`) and task 15 (`TitleScene_NewGameHandoff`) are linked to their pages. Addresses are build-specific.

## Open questions

? what event variables 85 and 100 mean; ? whether the three NXD rows 18, 19 and 20 are the demo movies task 11 waits for; ? whether the New Game + source-save picker and the Load Game list differ in more than the mode field.
