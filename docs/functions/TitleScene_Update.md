# TitleScene_Update

- **Address:** `0x1401DE744`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `unsigned __int8 __fastcall TitleScene_Update(unsigned __int8 *frame)`
- **Callers:** TitleScene_Task (0x1402F0953, one site)
- **Callees:** UITitle_ShowMenu, UISaveLoad_Open, UIState_EndTransition, Mem_Alloc, sub_1401C7634, UIAgent_AttachAddon, UIAddon_LoadByRow, sub_1400FB3B0, UIGuide_Show, UITitle_OpenPlayMode, UIAddonFFTOTitle_Create, UIAddonFFTOTitlePlaymode_Create, sub_1401CA6C4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The title scene's state machine. It drives the title menu, the New Game / New Game + / Continue / Load Game / Music Player / Select Version paths, and writes a state/result word into the eight-byte scene frame that `TitleScene_Task` reads.

## Behavior

- V: the argument is the frame at `g_UIStateFade+48`: +0 is the scene state and +1 is the result. Every return is the result byte.
- V: state 0 calls `UITitle_ShowMenu` on the title agent and sets the frame to state 1.
- V: state 1 waits while the title menu add-on's vtable +16 test is non-zero, then switches on the title agent's byte +89 (`next_state`).
- V: `next_state` 1 sets state 5 / result 1: New Game was confirmed on the play mode screen.
- V: `next_state` 2 is New Game +: when the save/load agent is idle it calls `UISaveLoad_Open`, then clears the low two bits of the save/load agent's mode field at +64, sets bit 2 (mode 4), writes -1 to `g_GlobalWork+128`, and sets state 2.
- V: `next_state` 3 is Load Game: when the save/load agent is idle it calls `UISaveLoad_Open` and sets state 3.
- V: `next_state` 4 sets state 5 / result 2: Continue finished loading the newest save inside `UIAgentFFTOTitle_Update`.
- V: `next_state` 5 is Music Player: when the BGM-mode agent at `[qword_143CD9DA8+16]+56` is idle it allocates a 912-byte block, constructs the BGM-mode add-on with `sub_1401C7634`, attaches it, loads UI add-on row 0xEF, hides the cursor with `sub_1400FB3B0(-1, 0, 0)`, shows the guide, and sets state 4.
- V: `next_state` 6 sets state 5 / result 3: Select Version was chosen.
- V: `next_state` 7 sets state 5 / result 4: the title menu's idle timeout fired.
- V: state 2 waits until the save/load agent's vtable +16 test is zero and the state dword at +96 of that agent object (+24 of its embedded agent at +72) is 0. If `g_GlobalWork+128` is still -1 it shows the title menu again with the cursor target at +90 set to 2 (New Game +) and returns to state 1.
- V: when `g_GlobalWork+128` is not -1, state 2 prepares the play mode screen: with no menu add-on it creates the three title add-ons and sets +92 = 1 and +93 = 1; with a menu add-on whose +41 byte is set it calls `UITitle_OpenPlayMode` and sets +93 = 0; with a menu add-on whose +41 byte is clear it sets +92 = 1 and +93 = 1 without creating anything. All three return to state 1.
- V: state 3 waits on the same save/load agent idle test. If `g_GlobalWork+102` is 0 it shows the title menu again with cursor target +90 = 3 (Load Game); otherwise it sets state 5 / result 2.
- V: state 4 waits until the BGM-mode agent's vtable +16 test is zero, then shows the title menu again with cursor target +90 = 5 (Music Player) and returns to state 1.
- V: state 5 has no branch: it keeps returning the result byte until `TitleScene_Task` acts on it.
- I: the `next_state` values are the menu outcomes rather than scene states; each one is written by the title menu action named above (rests on the setters: `sub_1401C3D88` writes 0x0101, `UITitle_StartNewGamePlus` 0x0201, `UITitle_StartLoadGame` 0x0301, the title agent's state 10 0x0401, `UITitle_OnMenuAction` kinds 4/5 0x0501/0x0601, and the idle timeout 0x0701).
- ?: what supply a zeroed frame (the only route to state 0), and what the save/load agent's other mode bits at +64 select.

## State touched

- Calls: [UITitle_ShowMenu](UITitle_ShowMenu.md), [UISaveLoad_Open](UISaveLoad_Open.md), [UIState_EndTransition](UIState_EndTransition.md), [Mem_Alloc](Mem_Alloc.md), [UIAgent_AttachAddon](UIAgent_AttachAddon.md), [UIAddon_LoadByRow](UIAddon_LoadByRow.md), [UIGuide_Show](UIGuide_Show.md), [UITitle_OpenPlayMode](UITitle_OpenPlayMode.md), [UIAddonFFTOTitle_Create](UIAddonFFTOTitle_Create.md), [UIAddonFFTOTitlePlaymode_Create](UIAddonFFTOTitlePlaymode_Create.md)
- Reads: [UIAgentFFTOTitle](../structs/UIAgentFFTOTitle.md), [g_UIStateFade](../globals/g_UIStateFade.md), [g_GlobalWork](../globals/g_GlobalWork.md)
- Writes: [UIAgentFFTOTitle](../structs/UIAgentFFTOTitle.md), [g_UIStateFade](../globals/g_UIStateFade.md), [g_GlobalWork](../globals/g_GlobalWork.md)

## Referenced by

- Appears in flows: [TitleSceneFlow](../flows/TitleSceneFlow.md), [TitleSceneFlow](../flows/TitleSceneFlow.md)
- Called by: [TitleScene_Task](TitleScene_Task.md)

## Notes

Whole function read (936 bytes). The title menu itself is `UITitle_ShowMenu` / `TitleMenu_Build`; this function only calls the show path and reads the agent's next_state. Every branch that produces a result writes the state/result word as one 16-bit store (state low byte, result high byte); the navigation branches write only the state byte. State 2's New Game + path sets the save/load agent's mode to 4 after `UISaveLoad_Open` has set it to 2; the Load Game path leaves 2.

## Open questions

? what supplies a zeroed frame; ? what the save/load mode bits besides 2 and 4 select; ? what the BGM-mode screen does with its list before it closes.
