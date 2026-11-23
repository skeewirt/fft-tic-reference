# OpeningTask_4

- **Address:** `0x14037DEA0`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `char __fastcall OpeningTask_4(_DWORD *frame, unsigned __int64 a2, _BYTE *a3, __int64 a4)`
- **Callers:** SceneLoop_Run (0x140331D2D), SceneLoop_RunAlt (0x14039DE79), both indirect through SceneTaskTable
- **Callees:** Opening_EndToTitle, EventSlot_SetParam, sub_140257384, sub_140257440, sub_140116598, sub_1402B1ED0, sub_1402B1E74, sub_1403325E4, sub_14037FF14, LegacyMenu_InitWorld, sub_14025FC38, VramPage_CopyRect, sub_14037B144, sub_14033E898, sub_14037E1E8, sub_14039DF20

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opening stage 4: the per-frame state machine that turns the opening text/menu into the date selection or the return-to-title shortcut. Its skip tail tears the opening down through `Opening_EndToTitle`.

## Behavior

- V: dispatched through `SceneTaskTable` when task id 4 is on top of the scene stack; both loops reach it at 0x140331D2D (`SceneLoop_Run`) and 0x14039DE79 (`SceneLoop_RunAlt`). The first argument is the 100-byte scene frame.
- V: the stage state is the dword at frame +0x10. `Opening_LoadMessageSprites` pushes task id 4 and writes 0 to that field, so 0 is the entry state.
- V: state 100 waits for the fade: while bit 2 of `dword_141876F00` is set it returns; once the bit is clear it calls `Opening_EndToTitle`.
- V: state 99 stores 100 in the state field, calls `EventSlot_SetParam(0, 96)`, sets bits 1 and 2 of `dword_141876F00`, sets `dword_141876F08` to 32 and clears `dword_141876F04`.
- V: state 5 waits for bit 2 of `dword_141876F00` to clear, then resets the event sound state with `sub_1402B1ED0`, calls the slot-release helper `sub_1402B1E74`, decrements the task depth and calls `sub_1403325E4`. That helper pushes task id 7 and writes its frame: 0 at +0x00, 0 at +0x08, 4 at +0x0C and 0 at +0x10.
- V: state 4 resets the party state with `sub_14037FF14(0)`, initialises the legacy menu world (`LegacyMenu_InitWorld`), copies the background rectangle for the current page into the video page (`sub_14025FC38`, `VramPage_CopyRect`), and passes a language-selected resource and `qword_143C51A30` to the interactive menu loop `sub_14037B144`.
- V: when the menu returns, the stage compares the returned text buffer with a language-selected constant: 14 units for Japanese and 10 units for every other language. If every unit matches, or `dword_142E7FF5C` is non-zero, the state becomes 5 and the EventSlot and fade-timer writes run. Otherwise the task depth is decremented, the byte at `xmmword_1411A7DEC` is set to 0 when `g_ShopModeGate` is non-zero (else left as it was), and `sub_14037E1E8` pushes task id 5. Before either exit, `qword_143C51A38` is released with `sub_14033E898` when it is non-zero.
- V: if the skip flag `g_GlobalWork+100` is set when the menu returns, the state becomes 99 instead of taking either of the two exits above.
- V: when `g_ShopModeGate` is non-zero, state 0 becomes 95 with the EventSlot/fade writes. State 95 moves to 96 when bit 2 of `dword_141876F00` is clear. State 96 selects NXD row 0x15 with `sub_140257384` and commits it with `sub_140257440`, then stores 97. State 97 waits while `qword_143CD9C28` exists, its dword at +0x10 is neither 6 nor 0, and bit 0 of `g_GameUIManager+0xE4` is clear; it then calls `sub_140116598(g_GameUIManager, 0)`, stores 98 and then runs the same EventSlot/fade writes as state 0 (`EventSlot_SetParam(0, 96)`, bits 1 and 2 of `dword_141876F00`, `dword_141876F08` = 32, `dword_141876F04` = 0). State 98, once bit 2 of `dword_141876F00` is clear, stores 5 in the third dword of `xmmword_142E7FC70`, sets the state to 4 and clears `g_ScreenFadeMode`.
- V: with `g_ShopModeGate` zero, any state other than 4, 5, 99 or 100 takes the default path; on entry that is state 0. If bit 2 of `dword_141876F00` is set, it clears `g_ScreenFadeMode` when that word is non-zero and returns. Otherwise it calls `sub_14039DF20`; when that returns 0 it stores 5 in the third dword of `xmmword_142E7FC70` and sets the state to 4. It then tests the skip flag and, when set, stores 5 in the same dword and sets the state to 99.
- V: the state values the body handles are 0, 4, 5, 95, 96, 97, 98, 99 and 100. There is no explicit case for 1, 2, 3 or 6..94; any other value falls to the default path at the bottom.
- I: `g_GlobalWork+100` is a skip or return request (rests on the System agent's event-2 handler writing 1 to bytes +100 and +101, and on every opening handler ending its work when the byte is set).
- I: `qword_143CD9C28` is the movie player; its +0x10 state 6 or 0 is the finished state (rests on `Movie_Start`, `MovieController_UpdateSkip` and `Boot_MovieFrame` using the same field with the same pair of values).
- I: `sub_14039DF20` is a screen-wipe or transition helper (rests on its row counter, the 279-byte row copies into the video page, and the state-0 wait for a zero return).
- I: `sub_14037B144` is the opening's interactive legacy menu (rests on its menu-step loop, its UI script calls and the text buffer it returns).
- ?: what the compared constant string represents and what `dword_142E7FF5C` records; what the states 95..98 do when `g_ShopModeGate` is non-zero; and what `sub_14039DF20` draws.

## State touched

- Calls: [Opening_EndToTitle](Opening_EndToTitle.md), [EventSlot_SetParam](EventSlot_SetParam.md), [LegacyMenu_InitWorld](LegacyMenu_InitWorld.md), [sub_14025FC38](sub_14025FC38.md), [VramPage_CopyRect](VramPage_CopyRect.md), [sub_14037E1E8](sub_14037E1E8.md)
- Reads: [g_GlobalWork](../globals/g_GlobalWork.md), [g_ShopModeGate](../globals/g_ShopModeGate.md), [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Appears in flows: [OpeningStages](../flows/OpeningStages.md)

## Notes

Whole body read (837 bytes), plus the frame initialisation in `Opening_LoadMessageSprites` and the stack pushes in `sub_14037E1E8` and `sub_1403325E4`. `sub_14037B144` was read around its menu loop and return value, not line by line. This is task id 4 of `SceneTaskTable`, not the earlier opening task 1 of the same table.

## Open questions

What the constant text compared after the menu is and what `dword_142E7FF5C` means; what states 95..98 do; what `sub_14039DF20` draws; and what the return value of the frame dispatch means to the loops.
