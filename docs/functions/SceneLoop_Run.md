# SceneLoop_Run

- **Address:** `0x140331C14`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall SceneLoop_Run(int mode)`
- **Callers:** sub_14037ADB8 (0x14037ADFE, tail jump)
- **Callees:** Scene_Init, sub_14037F854, sub_1402F42D0, sub_1402B4710, SpriteAnim_Step, sub_14037F8AC, sub_140257B18, sub_14037FB7C, EventThread_Yield, sub_14037FB30, sub_14033E898, sub_1401DDCFC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The normal scene loop: it seeds the scene from the mode argument, dispatches one scene task per frame until scene flag bit 0 clears, then returns the hand-over code the task left in `dword_141876F94`.

## Behavior

- V: first calls `Scene_Init(mode)`.
- V: clears `word_141874530`, `word_141874534` and the qword after `g_ScreenFadeMode`.
- V: the frame loop runs while bit 0 of `dword_141876EE8` is set (Scene_Init sets the word to 4161, so bit 0 starts set).
- V: per frame it clears `dword_1437951B0` and calls `sub_14037F854` (no argument is visible in the decompiled call); when `dword_143C51A40` bit 0 is set and `g_ShopModeGate` is zero it calls `sub_1402F42D0` on that block; when scene flag 0x400 is set it calls `sub_1402B4710` on the inactive page.
- V: dispatches the top scene task `tbl_OpeningTaskSteps[dword_1418772E0[dword_141877480 - 1]]()`; the id comes from the task stack at `dword_1418772E0` and the depth is `dword_141877480`.
- V: when scene flag 8 is clear, walks the `dword_141876F90` sprite entries at `qword_141876FA0` and steps type-1 animations with `SpriteAnim_Step` and type-2 animations with `sub_14037F8AC` when their 0x18 flag bits are clear.
- V: when `dword_1437F663C` is zero, calls `sub_140257B18` on the current page's block; otherwise it just clears the flag.
- V: calls `sub_14037FB7C`, yields one event tick, clears the low dword of `qword_142FF9EE8`, and when scene flag 2 is clear calls `sub_14037FB30`.
- I: `sub_14037FB7C` latches the pad state into the scene input words, `sub_14037FB30` toggles the page index and signals the page events, and `sub_140257B18` hands the current page to the display (rests on the globals each call writes and the page buffers it takes).
- V: the loop's only end is bit 0 of `dword_141876EE8` clearing; the hand-over code does not end it.
- V: after the loop it releases the objects at `qword_143C51A30`, `qword_143C51A38` and `qword_143C51A48` through `sub_14033E898`, clears bit 0 of `dword_143C51A40`, cleans `g_UIStateFade` through `sub_1401DDCFC`, and returns `dword_141876F94`.
- V: the scene tasks write `dword_141876F94` before clearing bit 0: task 1 writes 0; `OpeningMenu_Task` (id 2, `sub_1402F0124`) writes 0, 1, 2 or 3; `TitleScene_Task` writes 0, 1 or 3 in its result-2 branch.
- I: the code tells Game_MainLoop which post-scene path to take (new game, load, plain continue); the exact menu meanings are not decoded (rests on the branch table in Game_MainLoop and the three task writers).
- ?: what each scene flag bit means, and what hand-over code 1 selects at the menu level.

## State touched

- Calls: [Scene_Init](Scene_Init.md), [SpriteAnim_Step](SpriteAnim_Step.md), [EventThread_Yield](EventThread_Yield.md)

## Referenced by

- Appears in flows: [ApplicationLifecycle](../flows/ApplicationLifecycle.md), [SceneTaskDispatch](../flows/SceneTaskDispatch.md), [SceneTaskDispatch](../flows/SceneTaskDispatch.md)
- Reads tables: [SceneTaskTable](../tables/SceneTaskTable.md)

## Notes

Whole function read (588 bytes). The task table is indexed by the scene task stack, so the loop runs whichever step is on top; it does not call the scene handlers directly. The return word is separate from the loop condition.

## Open questions

The meaning of scene flag bits 0, 1, 2, 3, 0x400 and 0x1000, and the full mapping of the return codes to the title menu choices.
