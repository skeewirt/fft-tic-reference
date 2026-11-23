# Boot_Update

- **Address:** `0x1401DE164`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall Boot_Update(void *bootUI)`
- **Callers:** Boot_Frame (0x1400B5BB8)
- **Callees:** sub_1400ECC5C, sub_14013EE4C, Mem_Alloc, UIAgent_AttachAddon, UIAddon_LoadByRow, UIAgentFFTOLauncher_Open, UIState_BeginTransition, UIState_EndTransition, UIAgentFFTOSystem_OpenConfig, App_LaunchClassic, sub_1401BC2A8, sub_1401BC1FC, UIAgent_DetachAddon, UIAgentCursor_Show, UIGuide_Show, sub_1401B9108, sub_1400366B0, sub_1401D1970, sub_14029C128

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The boot launcher: a local state machine on the boot UI object. It raises the startup screen, the title cushion and the Enhanced/Classic launcher, follows the launcher's selection, and returns 1 when the launcher decides to continue into the game.

## Behavior

- V: the argument is the 8-byte object stored at `g_UIStateFade+32`: byte 0 is the stage and byte 1 the launcher mode (I: filled in by `Boot_SetState`, see that page).
- V: stage 0 first waits for `sub_1400ECC5C(g_CharaRenderMgr)` to return non-zero, then calls `sub_14013EE4C` on the UI agent at +136 when the agent's virtual check passes and the add-on at its +64 has the byte at +73 set.
- V: stage 0 chooses the first UI from `g_UIStateFade+42` and the mode byte: +42 set (then cleared) opens the launcher in mode 3; mode byte 0 opens launcher mode 1; mode byte 1 opens launcher mode 0; any other value allocates a 56-byte `UIAddonFFTOStartup`, attaches it to the UI agent at +24, loads UI row 0xF1 and moves to stage 2.
- V: stage 2 waits for the agent at +24 to report idle through its +16 virtual call and starts a fade to 24 when the save-request manager exists and `sub_1400366B0` returns non-zero, otherwise to 20; stage 3 waits for the fade timer at `g_UIStateFade+16` to reach zero and ends the transition.
- V: stage 4 waits for the fade, then either allocates a 504-byte `UIAddonFFTOTitleCushion` (UI row 0xF7) on the agent at +32 and moves to stage 5, or opens the launcher in mode 0; the choice depends on `sub_1400366B0`, the byte at `g_UIStateFade+43` and the presence of the save-request manager.
- V: stage 5 waits for the agent at +32 to report idle and opens the launcher in mode 0; stage 6 reads the launcher's result byte at agent+74.
- V: result 1 moves to stage 10 (the Enhanced action); 2 calls `App_LaunchClassic`, sets the byte at `g_Application+1520` and moves to stage 9; 3 clears the second system agent's fields at +40 through +63, calls `sub_1401BC2A8(agent+400,1,...)`, ends the fade and moves to stage 7; 4 opens the options screen on the agent at +296, sets `g_UIStateFade+42` and hides the launcher UI, moving to stage 8; 0 stays; any other value moves to stage 10.
- V: stage 7 waits for the agent at +400 to report +40 == 4 and +44 == 1 with the fade at zero, detaches its add-on and opens the launcher in mode 2; stage 8 waits for the agent at +296, restores the cursor and guide, shows the launcher UI and returns to stage 6.
- V: stage 9 does nothing on later frames; stage 10 is the only stage that returns 1.
- V: the result byte at agent+74 is written by `UILauncher_Update` from its pending action byte; the Enhanced action stores 1, the Classic action 2, the load route 3 and the options entry 4.
- I: the startup add-on is the startup/logo screen and the title cushion is the title-screen cushion (rests on the class names and the UI rows they load).
- V: `Boot_Update` never calls `Boot_SetState`; the state change happens in `Boot_Frame` when it returns 1.
- V: the Classic path leaves this executable: `App_LaunchClassic` starts the Classic program and sets the quit byte at `g_Application+1520`, which makes `App_RunFrame` return false and `Game_Main` leave its loop (the quit check is documented on App_RunFrame).

## State touched

- Calls: [Mem_Alloc](Mem_Alloc.md), [UIAgent_AttachAddon](UIAgent_AttachAddon.md), [UIAddon_LoadByRow](UIAddon_LoadByRow.md), [UIState_EndTransition](UIState_EndTransition.md), [UIAgentFFTOSystem_OpenConfig](UIAgentFFTOSystem_OpenConfig.md), [App_LaunchClassic](App_LaunchClassic.md), [UIAgent_DetachAddon](UIAgent_DetachAddon.md), [UIAgentCursor_Show](UIAgentCursor_Show.md), [UIGuide_Show](UIGuide_Show.md), [sub_1400366B0](sub_1400366B0.md)
- Reads: [g_UIStateFade](../globals/g_UIStateFade.md), [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md), [g_Application](../globals/g_Application.md), [g_SaveRequestManager](../globals/g_SaveRequestManager.md), [g_SaveManager](../globals/g_SaveManager.md)
- Writes: [g_UIStateFade](../globals/g_UIStateFade.md), [g_Application](../globals/g_Application.md)

## Referenced by

- Appears in flows: [BootStateMachine](../flows/BootStateMachine.md)
- Called by: [Boot_Frame](Boot_Frame.md)

## Notes

The function is 1401 bytes; the whole body was read. Stage numbers are the local values of the boot UI object's first byte, not the boot state in `dword_140D3AD50`.

## Open questions

The names of the two system agents at +296 and +400 and the UI rows behind them; why stage 0 calls `sub_14013EE4C` only when the +73 byte is set; and what the title cushion is called in the game's own UI data.
