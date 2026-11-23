# SceneLoop_RunAlt

- **Address:** `0x14039DCE8`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void SceneLoop_RunAlt(void)`
- **Callers:** Game_MainLoop (0x1402D49E0)
- **Callees:** EventSlots_ResetAll, sub_14025FE14, GameData_ReadSectors, EventThread_Yield, sub_140380104, sub_14037F5E4, sub_14038ED68, sub_140257384, sub_140257440, sub_14037FB7C, sub_140273D78, sub_14037F854, sub_14037FB30, sub_140257B18

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The alternate scene bootstrap: it performs the scene reset inline (without `Scene_Init`), loads the 0x8800-byte run of data kind 877 starting at sector 101 into the scene buffer, pushes scene task 9, and runs the same per-frame task dispatch until scene flag bit 0 clears. It has no hand-over code.

## Behavior

- V: resets the event slots and the core scene words inline (scene flags 4161, buffer at `unk_141C82E00`, `dword_141876F10` and `dword_141876F14` to 2, `dword_14187A5D4` to 4, `dword_141876EF4` to -1, page index 0 and task stack depth 0), with no title/opening call.
- V: calls `sub_14025FE14` with 960 and 0, then reads 0x8800 bytes of data kind 877 starting at sector 101 into `unk_141C82E00` through `GameData_ReadSectors`, and waits while the high dword of `qword_141856AB0` is non-zero.
- V: calls `sub_140380104` with -1, calls `sub_14037F5E4` and `sub_14038ED68`, resets the task stack depth and page index, and loads NXD row 9 through `sub_140257384(9)`.
- V: clears scene flag 0x40, sets `dword_143807794` to 9, writes 9 at `dword_1418772E0[dword_141877480]`, increments the depth and calls `sub_140257440`.
- V: calls `sub_140273D78` with 480 and 272, then runs the frame loop while scene flag bit 0 is set: calls `sub_14037F854`, dispatches the top task, calls `sub_14037FB7C`, yields when `dword_141877484` is 0 or more and not 1, calls `sub_14037FB30` and `sub_140257B18`, and clears `dword_1437951B0`.
- V: task 9 immediately replaces itself with task 10; task 10 runs a UI fade to state 15 and the movie-host checks, and clears scene flag bit 0 when it ends. Its exit tail releases three pointers that start at -1 and have no writer, so the tail's reachability is open (see `OpeningTask_10`).
- V: after the loop it calls `sub_14025FE14` with 960 and 256 and calls `sub_140273D78` with 374 and 240; it returns nothing.
- I: this is a transitional loop rather than a full scene: it starts at task 9 instead of task 0 or 14, has no `Scene_Init` and no hand-over code, and ends when the fade/movie task clears bit 0 (rests on the call site and the task 9/task 10 bodies).
- ?: what sector group 877/101 contains, and the exact condition that makes `dword_140D3A848` 3.

## State touched

- Calls: [EventSlots_ResetAll](EventSlots_ResetAll.md), [GameData_ReadSectors](GameData_ReadSectors.md), [EventThread_Yield](EventThread_Yield.md)

## Referenced by

- Appears in flows: [ApplicationLifecycle](../flows/ApplicationLifecycle.md), [OpeningTransitionTasks](../flows/OpeningTransitionTasks.md), [SceneTaskDispatch](../flows/SceneTaskDispatch.md)
- Called by: [Game_MainLoop](Game_MainLoop.md)
- Reads tables: [SceneTaskTable](../tables/SceneTaskTable.md)

## Notes

Whole function read (568 bytes). It is not the save/load menu: the save-manager scan and the `off_1408F9570` state machine live in Game_MainLoop. In this build Game_MainLoop calls this loop only when `dword_140D3A848` is 3 (the battle-frame result switch); it is not the SceneLoop_Run return code 3.

## Open questions

The contents and purpose of the 877/101 sector block and whether any value of `dword_140D3A848` other than 3 can reach this loop.
