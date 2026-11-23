# TitleScene_Start

- **Address:** `0x1402F0864`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `char __fastcall TitleScene_Start(void)`
- **Callers:** Scene_Init (0x14037F5DD), OpeningTask_0 (0x1402F007A), OpeningMenu_Task (0x1402F0457), OpeningTask_7 (0x1403327EB), OpeningTask_12 (0x14037F432)
- **Callees:** SceneState_Reset, Mem_Alloc, sub_1401DDCFC, sub_1402BA744, UITitle_ShowMenu, UI_FrameUpdate, sub_14037FF14

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The title scene's start function: it resets the game and party state for a fresh title session, allocates the eight-byte title scene frame, shows the title menu (or seeds the save-return result), and pushes scene task id 14.

## Behavior

- V: called from `Scene_Init` (non-zero mode, 0x14037F5DD), `OpeningTask_0` (`sub_1402F0060`, 0x1402F007A, only when `g_MovieRequestId < 0`), `OpeningMenu_Task` (`sub_1402F0124`, 0x1402F0457), `OpeningTask_7` (0x1403327EB) and `OpeningTask_12` (`sub_14037F398`, 0x14037F432). It does not call `Scene_Init`.
- V: starts with `SceneState_Reset` (the event/legacy scene reset), clears `g_BattleState` and `dword_140D3A854`, sets the low dword of `qword_142FF9EE8` to 1, calls `sub_1402BA744(0)`, sets `g_ScreenFadeMode` to 1 and calls `sub_1401DDCFC(g_UIStateFade)` before the new frame pointer is stored at `g_UIStateFade+48`.
- I: `sub_1402BA744(0)` (callee body not in this function; rests on a separate read of it) writes the `dword_142E7FC68` block (7, 0, 1), calls `sub_140273D78(0, 374, 240)`, clears the 0x4 flag of the flags dword at `[qword_143CD9DA8+16]+280`, and sets the 0x10 flag.
- V: allocates eight bytes with `Mem_Alloc(8, ...)` and stores the pointer at `g_UIStateFade+48`; the buffer holds the title scene state byte at +0 and the result byte at +1. Only those two bytes are written by this function.
- V: when `dword_142E7FF68` (the save-return flag that `Save_ResumeCheckpoint` sets) is non-zero, the frame is set to state 5 / result 2 (`0x0205`), so the first `TitleScene_Task` pass takes the save-return hand-over branch instead of showing the menu.
- V: otherwise it calls `UITitle_ShowMenu` on the title agent (the agent reached at `[qword_143CD9DA8+16]+48`), sets the frame to state 1, and runs `UI_FrameUpdate(g_CharaRenderMgr, 0.0)` once so the menu add-on exists and has been ticked before the first task pass.
- V: calls `sub_14037FF14(1)`. I: (callee body not in this function; rests on a separate read of it) that sets scene flag bit 0x80 and, when either 0x100 or 0x8000 is clear, rewrites the flags to set 0x100 and 0x8000 (clearing bits 14 and 0x10000) and calls `GameState_ResetParty(1)` and `sub_1402B52E4()`. `GameState_ResetParty(1)` marks the 54 unit save records empty (the presence byte at +1 of each 600-byte record), clears the inventory, poach, move-find and item-new tables, writes event variable 44 (gil) to 7500 and resets the job flags; `sub_1402B52E4` fills the party-name buffer. Mode 1 generates no starting units.
- V: pushes scene task id 14 at `dword_1418772E0[dword_141877480]`, increments the depth, and returns the result of `sub_14037FF14`.
- I: the title start is the fresh-session reset: `Scene_Init` clears the scene layer first, then this function clears the game and party layer and puts the title menu on screen (rests on the reset calls and on `GameState_ResetParty(1)` leaving the unit and inventory tables reset and gil at 7500).
- ?: what sets `dword_142E7FF68` besides `Save_ResumeCheckpoint`, and what the other six bytes of the eight-byte frame are reserved for.

## State touched

- Calls: [SceneState_Reset](SceneState_Reset.md), [Mem_Alloc](Mem_Alloc.md), [UITitle_ShowMenu](UITitle_ShowMenu.md), [UI_FrameUpdate](UI_FrameUpdate.md)
- Reads: [g_UIStateFade](../globals/g_UIStateFade.md), [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md)
- Writes: [g_UIStateFade](../globals/g_UIStateFade.md), [g_BattleState](../globals/g_BattleState.md)

## Referenced by

- Appears in flows: [OpeningToTitle](../flows/OpeningToTitle.md), [TitleSceneFlow](../flows/TitleSceneFlow.md)
- Called by: [OpeningMenu_Task](OpeningMenu_Task.md), [OpeningTask_0](OpeningTask_0.md), [OpeningTask_12](OpeningTask_12.md), [OpeningTask_7](OpeningTask_7.md), [Scene_Init](Scene_Init.md)

## Notes

Whole function read (223 bytes). The IDB signature carries four arguments, but the body reads none of them; the scene dispatch's frame argument goes to `TitleScene_Task`, not here. The function does not call `Scene_Init`; it calls `SceneState_Reset`, which is the event/legacy reset, and then adds the game/party reset of `sub_14037FF14(1)`. The eight-byte frame is the object that `TitleScene_Task` passes to `TitleScene_Update` and frees through `sub_1401DDCFC`.

## Open questions

? what sets `dword_142E7FF68` besides `Save_ResumeCheckpoint`; ? what the remaining frame bytes are for; ? whether any path calls the start with a non-zero scene depth (the push has no bound check).
