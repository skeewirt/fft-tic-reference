# Game_MainLoop

- **Address:** `0x1402D3FA0`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void __noreturn Game_MainLoop(void)`
- **Callers:** Game_MainLoopReset (0x1402D4A35)
- **Callees:** memset, SaveData_InitHeaderStrings, sub_140245D44, sub_14039D828, sub_14037ABBC, sub_140245C84, EventThread_Yield, CardSlot_IsValid, sub_14021849C, SceneTask_Start, sub_1402F7F4C, SceneState_Reset, Status_BuildFlagMasks, sub_14033FB84, sub_14031EF70, sub_140273D78, EventSlots_ResetAll, sub_14025F7C0, sub_1402B1CD0, sub_140283E24, sub_1402B2124, sub_140283F64, sub_1401D6F9C, sub_1400EC678, sub_1400ECC5C, sub_14013EA54, sub_14013EE4C, sub_14037ADB8, sub_140257354, EventVar_Write, sub_1402F41D0, GameData_ReadSectors, sub_14033D6B0, ClassicMenu_RunScreenStack, sub_140210AF0, sub_1402B20C0, SceneVar_Write, sub_1402BA744, sub_14024599C, sub_1402D38EC, sub_1402BAB04, sub_1400E43B4, UIState_BeginTransition, sub_1401E2D64, sub_1401E3744, SceneLoop_RunAlt

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The game's outer loop. It clears the save images and scans the save data, resets the scene task set, runs a scene through `SceneLoop_Run`, and converts the scene's hand-over code into the next step (new game, load, or a battle/scene transition). It also runs `SceneLoop_RunAlt` for the transition path and never returns.

## Behavior

- V: entry zeroes the three scan outputs and the save-manager state `dword_142E7FADC`, fills `g_SaveSlotCache` (0x1EA488 bytes) and `g_SaveAutoSlot` (0x9CE4 bytes) with 0xFF, then calls `SaveData_InitHeaderStrings` to point the manager at the cache and install the language-dependent save strings.
- I: the fill comes before the scan so no byte from an earlier image can survive as a valid slot header; the scan overwrites only the headers it finds (rests on the fill preceding every scan call).
- V: the first scan loop calls `sub_140245D44(&code, &total, &free)`: 1 = still scanning, 0 = done, -1 = error. While it returns 1 the loop steps the save UI state machine `sub_14039D828(&off_1408F9570)`.
- V: 0 leaves the scan and enters the scene phase. -1 maps the detail code: -13 -> message 0xD829 with `total`, -5 -> 0xD828 with `free`, -4 or -3 -> 0xD826 with `total`, and any other code -> 0xD827 with `total`. The message id goes to `word_1408FBC5C` and the value to the low dword of `xmmword_14078D9C0`.
- V: the error path runs the loading/message panel `sub_14037ABBC`; while it returns non-zero the panel is polled, and when it returns 0 the loop leaves the error path and enters the scene phase. No scan code exits the process.
- V: during the scan a zero manager error returns 0, a non-zero code returns -1 with the code in the first output, except -6 (when the reported total leaves room) and -7, which return 0.
- V: when the scene phase begins, the loop re-clears both save images, resets the manager, and starts a second save-manager scan `sub_140245C84`; it returns 1 (busy) or 0 (ready) only. On 0 it sets the low dword of `xmmword_142E7FB40` to 1, yields until it clears, tests card slots 0..49 with `CardSlot_IsValid`, and sets `dword_141853BCC` from that test or, when all 50 are valid, from `sub_14021849C`. A -1 test exists in the loop and leads to the same `sub_14021849C` branch, but `sub_140245C84` never returns -1.
- V: the scene body starts tasks 1..16 with `SceneTask_Start(i, SceneTask_Terminate)` and `sub_1402F7F4C(i)`, clears `g_GlobalWork+101` when set, calls `SceneState_Reset`, clears `g_BattleState` and `dword_140D3A854`, and sets the low dword of `qword_142FF9EE8` to 1.
- V: when `g_BattleModeFlag` is 5 it writes the default status/config bytes at 0x1407829F8..0x1407829FF and 0x140C6AD77, rebuilds the status masks (`Status_BuildFlagMasks`, `sub_14033FB84`, `sub_14031EF70`), sets the low dword of `xmmword_142FF9E14` to 0, calls `sub_140273D78` with 374 and 240, and sets `dword_142E7FF68` when `dword_142FF9EFC` is non-zero.
- V: otherwise it clears the fade mode and the low dword of `xmmword_142FF9E14`; when `dword_141856718` is set it tears the previous scene UI down (battle bytes, event slots, event counters, `sub_14025F7C0`, `sub_1402B1CD0`, `sub_140283E24`, `sub_1402B2124`, `sub_140283F64`). It then rewrites the default status block, creates the object for slot 5 or 6 of `qword_143CD9DD8` (selected by `g_ShopModeGate`) when that slot is empty, marks `dword_141856718` as 1, calls `sub_1400EC678(g_CharaRenderMgr)` and yields until `sub_1400ECC5C` returns non-zero, performs the shop or field branch (`sub_14013EE4C` / `sub_14013EA54`), and calls `sub_140273D78` with 374 and 240.
- V: it calls `sub_14037ADB8`, which selects the language-dependent resource 876 and tail-calls `SceneLoop_Run`. Assembly read: the mode byte is `g_GlobalWork+100` non-zero and `g_GlobalWork+101` zero, with +101 cleared first.
- V: it clears `g_GlobalWork+100` after the scene and branches on the code `SceneLoop_Run` returned: 0 sets `byte_1407829FA` to 1 and `g_BattleModeFlag` to 0.
- V: code 1 sets `byte_1407829FA` to 0.
- V: code 2 sets `byte_1407829FA` to 0 and clears event variable 85.
- V: code 3 sets `byte_1407829FA` to 0, sets the low dword of `xmmword_142FF9E14` to 1 and, unless `sub_140257354` returns 2, sets the second dword of `xmmword_142FF9E24` to 1.
- V: any other code sets `byte_1407829FA` to 0.
- V: the second dword of `xmmword_142FF9E24` is a small countdown: 1 clears `g_BattleModeFlag` and scene variables 52 and 39; 2 runs `SceneState_Reset` and sets `dword_142FF9EFC` to 2. When `byte_1407829FA` is clear the loop loads data kinds 771 and 772 through `sub_1402F41D0` and `GameData_ReadSectors`, then sets `g_BattleModeFlag` from `ClassicMenu_RunScreenStack`.
- V: with `g_BattleModeFlag` 5 it tears the battle UI down (fade transition, list clear, battle bytes zeroed) and leaves through the scene-result check; otherwise it calls the battle frame update `sub_140210AF0` and switches on `dword_140D3A848`: 2 = fade out; 3 = run `SceneLoop_RunAlt`; 5 = battle teardown into mode 5; 6 or 7 = set the countdown to 3 or 4 and take the teardown; 8 = set the countdown to 2 and reset the scene state; 10 = handle the save-return flag `dword_142E7FF68`, then reload or call `sub_140273D78` with 480 and 272.
- V: the `SceneLoop_RunAlt` branch cleans the UI manager fade/list, resets the event slots, writes scene variables 100 and 39, selects resource 876 again, calls `SceneLoop_RunAlt`, restores resource 0, calls `sub_140283F64`, `sub_140210AF0` and `sub_1402D38EC`, and continues the outer loop.
- V: the function has no return statement and no exit or process-termination call; its last instruction jumps back to the top of the outer dispatch, and IDA marks it `__noreturn`.
- I: the process is ended from the window thread instead: Game_Main's `App_RunFrame` and `App_ProcessMessages` loop returns on WM_QUIT and Game_Main tears the application down while this loop is still running (rests on the Game_Main and App_ProcessMessages pages).
- ?: what hand-over codes 0 and 1 select at the menu level, and what result codes 2, 5, 6, 7, 8 and 10 mean in gameplay terms.

## State touched

- Calls: [SaveData_InitHeaderStrings](SaveData_InitHeaderStrings.md), [sub_140245C84](sub_140245C84.md), [EventThread_Yield](EventThread_Yield.md), [CardSlot_IsValid](CardSlot_IsValid.md), [sub_14021849C](sub_14021849C.md), [SceneTask_Start](SceneTask_Start.md), [SceneState_Reset](SceneState_Reset.md), [sub_14033FB84](sub_14033FB84.md), [sub_14031EF70](sub_14031EF70.md), [EventSlots_ResetAll](EventSlots_ResetAll.md), [sub_140257354](sub_140257354.md), [EventVar_Write](EventVar_Write.md), [GameData_ReadSectors](GameData_ReadSectors.md), [ClassicMenu_RunScreenStack](ClassicMenu_RunScreenStack.md), [sub_140210AF0](sub_140210AF0.md), [SceneVar_Write](SceneVar_Write.md), [SceneLoop_RunAlt](SceneLoop_RunAlt.md)
- Reads: [g_SaveSlotCache](../globals/g_SaveSlotCache.md), [g_SaveAutoSlot](../globals/g_SaveAutoSlot.md), [g_GlobalWork](../globals/g_GlobalWork.md), [g_LanguageInfo](../globals/g_LanguageInfo.md), [g_ShopModeGate](../globals/g_ShopModeGate.md), [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md), [g_BattleState](../globals/g_BattleState.md), [g_UIStateFade](../globals/g_UIStateFade.md), [g_GameUIManager](../globals/g_GameUIManager.md)
- Writes: [g_SaveSlotCache](../globals/g_SaveSlotCache.md), [g_SaveAutoSlot](../globals/g_SaveAutoSlot.md), [g_BattleModeFlag](../globals/g_BattleModeFlag.md), [g_GlobalWork](../globals/g_GlobalWork.md), [g_BattleState](../globals/g_BattleState.md), [g_InventoryCounts](../globals/g_InventoryCounts.md), [g_PoachersDenStock](../globals/g_PoachersDenStock.md), [g_ItemNewFlags](../globals/g_ItemNewFlags.md), [g_UnitSaveData](../globals/g_UnitSaveData.md)

## Referenced by

- Appears in flows: [ApplicationLifecycle](../flows/ApplicationLifecycle.md)
- Called by: [Game_MainLoopReset](Game_MainLoopReset.md)

## Notes

Whole function read (2,697 bytes). Earlier versions of this reference called this function Save_BootClear and described only the entry fill and part of the save-scan state machine; that was a fragment of this body, not a separate function. The save/load menu is the `sub_140245C84` + `off_1408F9570` block inside this loop; the alternate scene loop starts at task 9 and moves immediately to task 10, the UI-fade/movie task. `sub_140245C84` is not a one-shot clear: its first state does the clear and the later states poll the save manager.

## Open questions

The menu-level meaning of hand-over codes 0 and 1; the exact meaning of the save-scan outputs beyond code/total/free; and the missing records for `dword_141876F94`, `dword_141876EE8`, `dword_142FF9EFC` and `dword_140D3A848`.
