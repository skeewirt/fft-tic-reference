# TitleScene_Task

- **Address:** `0x1402F0944`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `unsigned __int8 TitleScene_Task(void)`
- **Callers:** SceneLoop_Run (0x140331D2D), SceneLoop_RunAlt (0x14039DE79)
- **Callees:** TitleScene_Update, sub_14037FF14, LegacyMenu_InitWorld, sub_140257384, sub_140257440, UIState_EndTransition, sub_140273D78, sub_14024599C, EventVar_Read, sub_1401DDCFC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Scene task id 14: it runs `TitleScene_Update` once per dispatch and turns the result into the next scene task id, or ends the scene for the outer loop.

## Behavior

- V: dispatched by `SceneLoop_Run` (0x140331D2D) and `SceneLoop_RunAlt` (0x14039DE79) through `tbl_OpeningTaskSteps`; it calls `TitleScene_Update` with the frame at `g_UIStateFade+48`.
- V: result 0 returns without changing the scene stack, so task 14 runs again next frame.
- V: result 1 pops task 14, calls `sub_14037FF14(0)` (whose `GameState_ResetParty(0)` path clears the same tables and then fills one starting unit through `sub_14027528C` / `Recruit_GenerateUnit`, and copies the play-mode selection), calls `LegacyMenu_InitWorld`, clears the byte at `xmmword_1411A7DEC`, loads NXD table-66 row 0x15 through `sub_140257384` and commits it with `sub_140257440`, ends any pending UI fade, pushes task 15 (`TitleScene_NewGameHandoff`), and releases the scene frame.
- V: result 2 calls `sub_140273D78(0, 374, 240)`, clears `g_GlobalWork+102`, and does not push a task. When `dword_142E7FF68` is non-zero it clears the flag, calls `sub_14024599C` (which clears scene variable 50 and leaves 508 unchanged) and sets the loop hand-over code `dword_141876F94` to 3; otherwise it clears `g_ScreenFadeMode`, clears the third dword (+8) of `xmmword_142FF9E24`, sets the low dword of `xmmword_142FF9E14` to 1, and sets `dword_141876F94` to 1 when event variable 85 is non-zero or event variable 100 is zero, else 0. It then toggles bit 0 of `dword_141876EE8` (ending the scene loop) and releases the frame.
- V: result 3 sets the two bytes at `g_UIStateFade+40` and +41 to 1, replaces the top task id with 13 without changing the depth, and releases the frame. Task 13 (`OpeningScene_Resume`) then pops itself and re-enters `OpeningScene_Start`.
- V: result 4 ends any pending fade, pops task 14, sets the page index `dword_1418825EC` to 1, and picks an NXD table-66 row from `dword_141876EFC`: 1 gives row 18, 2 gives 19, 3 gives 20, and any other value resets the counter to 1 and gives 18. It loads and commits that row, sets scene flag bit 1, advances `dword_141876EFC` (wrapping to 1 after 3), pushes task 11 (`TitleScene_DemoReturn`), and releases the frame.
- V: within this function only the result-2 branch writes `dword_141876F94`; I: it is the value `SceneLoop_Run` returns to `Game_MainLoop` (rests on that sheet).
- I: result 1 starts a new game (rests on `GameState_ResetParty(0)` filling one starting unit and task 15 loading opening row 1), result 2 hands the scene back to the outer loop, result 3 returns to the opening scene, and result 4 is the idle-timeout restart that cycles three rows before task 11 returns (rests on the next-task bodies and on `Game_MainLoop`'s hand-over switch).
- ?: what `dword_141876EFC` selects in game terms, and whether rows 18, 19 and 20 are the demo movies task 11 waits for.

## State touched

- Calls: [TitleScene_Update](TitleScene_Update.md), [LegacyMenu_InitWorld](LegacyMenu_InitWorld.md), [UIState_EndTransition](UIState_EndTransition.md), [EventVar_Read](EventVar_Read.md)
- Reads: [g_UIStateFade](../globals/g_UIStateFade.md), [g_GlobalWork](../globals/g_GlobalWork.md)
- Writes: [g_UIStateFade](../globals/g_UIStateFade.md)

## Referenced by

- Appears in flows: [OpeningTransitionTasks](../flows/OpeningTransitionTasks.md), [TitleSceneFlow](../flows/TitleSceneFlow.md), [TitleSceneFlow](../flows/TitleSceneFlow.md)

## Notes

Whole function read (547 bytes). The task ignores the 100-byte scene frame the dispatcher passes and uses the eight-byte frame at `g_UIStateFade+48` instead. The IDB signature has no arguments, which matches the body. The result-2 branch is the only one that writes the loop hand-over code; the other branches write nothing to it.

## Open questions

? what tasks 11 and 15 do after their first pass (not read here); ? what `dword_141876EFC` selects; ? why result 3 writes both bytes at `g_UIStateFade+40`.
