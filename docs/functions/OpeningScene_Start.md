# OpeningScene_Start

- **Address:** `0x1402EFF6C`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall OpeningScene_Start(void)`
- **Callers:** Scene_Init (0x14037F5D3), sub_14037F354 (0x14037F38D), OpeningScene_Resume (0x1402F085C)
- **Callees:** sub_140257384, sub_140257440, UITitle_ShowMenu, UIState_EndTransition

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The mode-0 scene entry: it loads the opening scene page (or shows the title menu on the shop-gate path), resets the scene flag bits around a movie wait, ends any pending UI fade, then pushes scene task 0 and seeds the first 100-byte scene frame.

## Behavior

- V: reads `g_ShopModeGate`; when it is zero it calls `sub_140257384` with 17, otherwise with 0, and calls `sub_140257440` in both cases.
- V: on the non-zero path it takes the agent at `*(qword_143CD9DA8 + 16) + 48`; if the agent's byte +91 is zero and its vtable slot 4 (+16) returns zero, it calls `UITitle_ShowMenu` on the agent and sets byte +91 to 1.
- V: clears bit 6 (0x40) and sets bit 1 (0x02) of `dword_141876EE8`, leaving the other bits alone.
- V: writes 1 to the dword at 0x142FF9ED4 (the high dword of the block at 0x142FF9EC8).
- V: when bit 0 of the byte at `g_GameUIManager+172` is set, sets the byte at +192 to 1 and sets bit 0 of the dword at +184.
- V: when `g_UIStateFade+24` is non-zero, calls `UIState_EndTransition(g_UIStateFade, that value)`.
- V: stores 0 in `dword_1418772E0[dword_141877480]`, increments the depth, and writes 86999 at `0x1418772F0 + 100 x depth` and 10261 at the next dword, where depth is the value before the increment.
- I: the `sub_140257384`/`sub_140257440` pair is the scene-page load used with row 9 in `SceneLoop_RunAlt`; here it loads row 17, or row 0 when the shop gate is set (rests on that page's use of the same pair).
- ?: what rows 17 and 0 select, and what the two frame dwords mean; no reader of the two dwords was traced in the opening task bodies read.

## State touched

- Calls: [UITitle_ShowMenu](UITitle_ShowMenu.md), [UIState_EndTransition](UIState_EndTransition.md)
- Reads: [g_ShopModeGate](../globals/g_ShopModeGate.md), [g_GameUIManager](../globals/g_GameUIManager.md), [g_UIStateFade](../globals/g_UIStateFade.md)

## Referenced by

- Appears in flows: [OpeningStages](../flows/OpeningStages.md), [OpeningToTitle](../flows/OpeningToTitle.md), [OpeningTransitionTasks](../flows/OpeningTransitionTasks.md)
- Called by: [OpeningScene_Resume](OpeningScene_Resume.md), [Scene_Init](Scene_Init.md), [TitleScene_DemoReturn](TitleScene_DemoReturn.md)

## Notes

Whole function read (243 bytes). IDB name `OpeningScene_Start`. The push is task id 0. The constant-1 store the decompiler shows on the 16-byte block at 0x142FF9EC8 lands on the dword at 0x142FF9ED4 in the disassembly. The decompiled call shows only the integer first argument of `sub_140257384`.

## Open questions

What rows 17 and 0 load; what the two frame dwords select; the meaning of the `g_GameUIManager` fields at +172, +184 and +192.
