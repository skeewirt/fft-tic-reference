# SceneTaskTable

- **Kind:** table
- **Area:** [Application and startup](../areas/app-startup.md)
- **Storage:** Executable (constant)
- **Address:** `0x140681C80`
- **Rows:** 16 entries of 8 bytes (scene task ids 0..15)
- **Keyed by:** scene task id
- **Read by:** [SceneLoop_Run](../functions/SceneLoop_Run.md), [SceneLoop_RunAlt](../functions/SceneLoop_RunAlt.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 16-entry table of scene task handlers that the two scene loops call once per frame. Each entry is the handler for one task id; the id at the top of the task stack selects the entry, so the running handler decides what runs next by pushing another id or popping itself.

## Behavior

- V: the table is a constant array in the executable at 0x140681C80 (IDB name tbl_OpeningTaskSteps); its entries are 8 bytes apart and cover ids 0..15.
- V: the table ends at id 15. The next object starts immediately after it at 0x140681D00 and is a different table, tbl_EventSoundGroups; the qword there is not a handler and no dispatch site refers to it.
- V: both scene loops dispatch with tbl_OpeningTaskSteps[dword_1418772E0[dword_141877480 - 1]](), at 0x140331D2D in SceneLoop_Run and 0x14039DE79 in SceneLoop_RunAlt. The id comes from the top of the task stack, not from a direct call.
- I: the handler's first argument is the 100-byte scene frame at unk_1418772F0 + 100 x (depth - 1), where depth is dword_141877480 (rests on the frame writes in OpeningScene_Start; the decompiled dispatch call shows no argument).
- V: only those two sites read the table; a cross-reference scan of 0x140681C80 finds the two dispatch instructions and no writer.
- V: the 16 ids map to: 0 OpeningTask_0, 1 OpeningTask_1, 2 OpeningMenu_Task, 3 OpeningSubmenu_Task, 4 OpeningTask_4, 5 OpeningTask_5, 6 OpeningTask_6, 7 OpeningTask_7, 8 OpeningTask_8, 9 OpeningTask_9, 10 OpeningTask_10, 11 TitleScene_DemoReturn, 12 OpeningTask_12, 13 OpeningScene_Resume, 14 TitleScene_Task, 15 TitleScene_NewGameHandoff.
- V: all 16 entries point at separate function starts.
- V: id 14 is the title scene task. It calls TitleScene_Update and, on the result, replaces the top task id with 15, 13 or 11, or ends the scene with hand-over code 0, 1 or 3.
- V: id 13 is the opening resume task. It sets dword_1418825EC to 0, pops itself and re-enters OpeningScene_Start.
- V: id 4 is the opening text/menu stage, pushed by Opening_LoadMessageSprites. With g_ShopModeGate zero, state 0 waits on sub_14039DF20; state 4 runs the menu loop sub_14037B144 and then either sets state 5 (which pops 4 and pushes 7 through sub_1403325E4) or pops 4 and pushes 5 through sub_14037E1E8. States 99/100 end through Opening_EndToTitle.
- V: id 5 is the month/day picker, pushed by sub_14037E1E8; its accept actions push 6 through sub_14037EB50, and its skip path ends through Opening_EndToTitle.
- V: id 6 is the date confirmation page, pushed by sub_14037EB50; a commit writes event variables 95/96 and the packed date, holds 60 frames, pops two frames and pushes 1 through sub_1402F0084; a back cancels one frame to 5; its skip path ends through Opening_EndToTitle.
- V: id 7 is the return-to-title shortcut, pushed only by sub_1403325E4 from task 4 state 5; it calls TitleScene_Start and clears g_GlobalWork+100.
- V: the stage push sites are Opening_LoadMessageSprites -> 4, sub_14037E1E8 -> 5, sub_14037EB50 -> 6, sub_1402F0084 -> 1 and sub_1403325E4 -> 7 (the task-4 state-5 shortcut).
- V: id 0 (OpeningTask_0) is the mode-0 bridge to the title: while g_MovieRequestId is 0 or greater it returns and stays on top; at -1 it clears scene flag bit 1, pops itself and calls TitleScene_Start, which pushes id 14. It never pushes id 1.
- V: id 2 (OpeningMenu_Task) is a four-row scene menu: frame +0x04..+0x10 are four sprite-row ids, +0x1C the cursor, +0x20 the mode and +0x24 an idle timer. Row 0 pops it and calls Opening_LoadMessageSprites (which pushes id 4); row 1 calls sub_14037FF14 (the party/game reset: argument 1 = no starting units, 0 = one starting unit) and then TitleScene_Start (id 14) or leaves the loop with hand-over 0/1; row 2 leaves with hand-over 2; row 3 has no action; a forced row 99 leaves with hand-over 3. Mode 2 calls sub_14037D848, which pushes id 3; mode 3 sets the page index dword_1418825EC to 1 (the only write of it in this handler), requests NXD row 18, 19 or 20 and pushes id 11.
- V: id 3 (OpeningSubmenu_Task) is a three-row submenu: frame +0x00..+0x08 are the rows, +0x1C the cursor and +0x20 the state. Its only pusher is sub_14037D848, called only by id 2. Confirm or cancel sets state 2; the next frame clears the parent's four row flags, resets the parent's timer, drops the two counters by 3 and pops. It pushes no id.
- V: id 8 (OpeningTask_8) is a wait/skip gate for the opening message task: it tests the runnable flag of event-task block 2, raises the message-skip flag once while the task runs, and when the task stops it pops itself and conditionally restores the 32-entry event text-bank table.
- V: id 9 (OpeningTask_9) is the alternate loop's first task: it clears scene flag bit 1 when no movie is requested, sets bit 6, pops itself, requests PSP movie-file row 0x10, writes event id 16 and pushes id 10.
- V: id 10 (OpeningTask_10) waits while g_MovieRequestId is 0 or greater, then fades the UI agent at +400 to state 15, waits for its state 4/1, detaches its add-on and, in the code path, toggles scene flag bit 0. The three pointers its tail releases start at -1 and have no writer, so the tail's reachability is open.
- V: id 11 (TitleScene_DemoReturn) is pushed by TitleScene_Task result 4 after PSP movie-file row 18, 19 or 20 is loaded: it waits for that movie, pops, sets the page index to 1 and re-enters OpeningScene_Start, which pushes id 0.
- V: id 12 (OpeningTask_12) is the opening's skip/continue gate: accept loads the opening message sprites (pushing id 4); cancel refills the scene buffer from the 0x1E000-byte block at 0x141D3B9E0 and calls TitleScene_Start. No store of id 12 was found.
- V: id 15 (TitleScene_NewGameHandoff) is pushed by TitleScene_Task result 1: it waits for the movie, pops, sets the page index to 1, calls sub_1402F0084 (movie row 1, pushes id 1) and sets the fade mode to 1.
- V: no function stores ids 2, 8 or 12 on the task stack. Ids 2 and 12 are the only handlers that enter the stage chain (id 2 row 0 via Opening_LoadMessageSprites, id 12 accept), so the chain 4 -> 5 -> 6 -> 1 and the task-4 shortcut 4 -> 7 are not reached from either scene loop in this build.
- V: the task stack has no visible bound. Every push stores at the current depth and increments it; every pop decrements it (some by more than one). None of the accesses to dword_141877480 compares it with a limit before indexing.
- V: the first 100-byte scene frame used by the dispatch starts at 0x1418772F0; the depth counter dword_141877480 sits at 0x141877480, immediately after the fourth frame.
- V: the only task ids ever stored on the stack are 0, 1, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14 and 15. No store of 2, 8 or 12 was found in any function that accesses the array.
- I: the id array therefore has room for four ids (0x1418772E0..0x1418772EF) before the first scene frame (rests on the array's 4-byte stride and the adjacent frame base).
- ?: what the game does if the depth leaves 1..4. Nothing in the code guards an overflow (a fifth id would overwrite the first scene frame) or an underflow (depth 0 reads the dword before the id array).

## Notes

Covers the table entries and their names, both dispatch sites, every cross-reference to the table and to the task stack, the object after the table, and the handlers' own pages for the per-handler detail. SceneTaskTable is a project name; tbl_OpeningTaskSteps is the IDB name. The table is a code table, so only names and the dispatch expression are given, not its contents.

## Open questions

? how ids 2, 8 and 12 enter the stack (no store of any was found); ? whether the four-id space is an intended limit or only the room left before the scene frames; ? what task 1 does with the date written by task 6, and what states 95..98 do.
