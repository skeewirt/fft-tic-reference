# OpeningMenu_Task

- **Address:** `0x1402F0124`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall sub_1402F0124(int *frame)`
- **Callers:** SceneLoop_Run (0x140331D2D dispatch), SceneLoop_RunAlt (0x14039DE79 dispatch); no direct caller and no push of id 2
- **Callees:** sub_140257384, sub_140257440, sub_14037D848, EventThread_Yield, sub_14037F5E4, sub_140116598, sub_1402BA744, sub_14037FF14, sub_140273D78, sub_14021A030, sub_140380020, TitleScene_Start, sub_1401DDD2C, sub_14024599C, EventVar_Read, Opening_LoadMessageSprites, Input_TestAction, Input_ActionBit, sub_14037FE58, sub_1401D80A8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

A four-row scene menu built on sprite rows: it moves a highlighted row, starts the opening text or the title scene on a choice, and leaves the scene loop for the other choices. An idle path requests NXD row 18, 19 or 20.

## Behavior

- V: table entry 2 of `SceneTaskTable` (`sub_1402F0124`, 0x1402F0124). Its only callers are the two dispatch sites, `SceneLoop_Run` at 0x140331D2D and `SceneLoop_RunAlt` at 0x14039DE79. No function in the executable stores id 2 on the scene task stack.
- V: the scene frame is a four-row menu: +0x04, +0x08, +0x0C and +0x10 hold four sprite-entry ids, +0x1C is the cursor (0..3), +0x20 is the mode and +0x24 is an idle timer. The ids index the 36-byte sprite entries at 0x1418770A0.
- V: a cursor move writes 0 to the old row's entry field at +0x14 and 9 to the new row's +0x14. Mode 2 sets bit 0x10 of all four entries; the three-row submenu clears that bit again when it closes.
- V: up is action bit 0xA4 passed through the repeat filter `sub_14037FE58`; down is 0xA5 through the same filter, or a raw `Input_TestAction` of mask 256 on action 0x20. The cursor wraps 3 to 0 and 0 to 3; each move resets the idle timer and calls `sub_1401D80A8` with command 0x0A and value 3.
- V: confirm tests mask 32 on action 0x1A and mask 2048 on action 0x1F. A confirm sets the timer at +0x30 to 50, the pending flag at +0x34, UI fade bits 2 and 4 in `dword_141876F00`, the fade triple at 0x141876F04 / 0x141876F08 / 0x141876F14 to 0 / 32 / 2, and scene bit 0x10; it also calls `sub_1401D80A8` with command 0x0A and value 1.
- V: while +0x34 is set, the handler decrements +0x30 only while scene bit 4 is set; at 1 it clears bit 4, then clears +0x34. The next pass runs the selected row.
- V: running a row first clears scene bit 0x10 (yielding once when bit 4 is still set), clears bit 0x1000, sets the third dword of `xmmword_142E7FB40` to 1, calls `sub_14037F5E4(1)` and `sub_140116598(g_GameUIManager, 0)`, sets the second dword of `xmmword_1437A62B0` to 3, writes zero and 1.0 to the movie host at 0x143CD9C28 (+0x5CC and +0x5D0), and sets `dword_142E7FF6C` to 0.
- V: row 0 pops the handler, drops the counters `dword_141876EF8` and `dword_141876F90` by 6, clears scene bits 0x80 and 0x100, writes row 0 to `dword_141853BCC`, clears `dword_14185670C`, calls `Opening_LoadMessageSprites` (which pushes task 4) and sets the fade mode to 1.
- V: row 1 sets scene bit 0x40, calls `sub_14037FF14(1)` (I: the game/party reset in mode 1; it does not write the page index), yields, sets the screen 374x240 and clears the selection globals. When `g_ShopModeGate` is zero and `sub_14021A030(0)` returns zero, or when the gate is set and `sub_1401DDD2C` with mode 1 returns zero, it drops both counters by 6, pops itself and calls `TitleScene_Start` (which pushes task 14).
- V: in the `g_ShopModeGate` branch, after the save/load helper returns nonzero, the handler clears `g_GlobalWork`+0x66; if the flag at 0x142E7FF68 is set it leaves with hand-over code 3. Otherwise it flips scene bit 0, sets the screen 480x272 and leaves the loop with hand-over code 0 or 1: the code is 1 when event variable 85 is nonzero or event variable 100 is zero, else 0.
- V: row 2 calls `sub_14037FF14(0)` (I: the same reset in mode 0), sets hand-over code 2, pops itself, drops both counters by 6, sets bit 0x80000 in `dword_141D32E14`, flips scene bit 0 and writes row 2 to `dword_141853BCC`.
- V: row 3 does nothing; the handler returns with scene bit 0x10 cleared and the menu keeps running.
- V: row 99 clears the selection, flips scene bit 0, sets hand-over code 3 and calls `sub_14024599C`, which reads scene variable 508, writes 508 = 0 and 50 = 0, then writes the value it read back to 508 (net: variable 50 cleared, 508 unchanged). It does not pop.
- V: when `dword_142E80210` equals 1, a cursor move (after the move itself) also calls `sub_14037FF14(0)`, then pops like row 2's exit (counters down by 6, depth down by one, bit 0x80000 in `dword_141D32E14`, scene bit 0 flipped, cursor row written to `dword_141853BCC`) without setting a hand-over code.
- V: a nonzero flag at 0x142E7FF68 is consumed at entry: the handler clears it, sets `dword_142E7FF6C` to 1, cursor 99, timer 50, the pending flag, scene bit 0x10 and the 0 / 32 / 2 fade values. The menu then leaves with code 3.
- V: idle path: +0x24 increments once per frame. After 600 frames, if the movie host at 0x143CD9C28 is null or its +0x10 dword is 0 or 6, the handler sets mode 3 and starts a 32-frame fade; while the movie is in another state it keeps taking input.
- V: mode 3 drops both counters by 6, pops itself, selects page 1, flips scene bit 0x10, requests NXD row 18, 19 or 20 (cycled by `dword_141876EFC`) through `sub_140257384` and `sub_140257440`, sets scene bit 2 and pushes task 11. Task 11 re-enters `OpeningScene_Start`.
- V: mode 2 sets mode 0, sets bit 0x10 on the four rows and calls `sub_14037D848`, which builds three sprite rows and pushes task 3. Nothing in this function sets mode 2.
- I: the rows are menu choices, not stage state: row 0 hands to the opening loader, row 1 to the title, and the idle path to NXD rows 18-20. The handler is a menu between the title and the opening, not an opening stage (rests on the calls listed above).
- I: because no code stores id 2, the menu is not reached by the boot, title or opening paths read here; it is either unused or entered by a path outside this executable (rests on the complete cross-reference scan of the task stack).
- ?: the labels of the four rows and the three submenu rows; the entry condition and setter of mode 2; what frame +0x18 is (tested only against zero in the fade guard); the owner of the flag at 0x142E80210 (a cursor move pops when it is 1); what the writes at movie host +0x5C8..+0x5DC control.

## State touched

- Calls: [EventThread_Yield](EventThread_Yield.md), [sub_14021A030](sub_14021A030.md), [TitleScene_Start](TitleScene_Start.md), [EventVar_Read](EventVar_Read.md), [Opening_LoadMessageSprites](Opening_LoadMessageSprites.md), [Input_TestAction](Input_TestAction.md), [sub_1401D80A8](sub_1401D80A8.md)
- Reads: [g_ShopModeGate](../globals/g_ShopModeGate.md), [g_GameUIManager](../globals/g_GameUIManager.md)
- Writes: [g_GlobalWork](../globals/g_GlobalWork.md)

## Notes

Whole function read (1,828 bytes) with the push and pop sites and the task-stack cross-references followed. The opening stages 4-7 are outside this page; only their entry points were followed. No store of id 2 was found.

## Open questions

Who stores id 2 on the scene task stack (none found); what the four row labels and the three submenu labels are; what sets mode 2; the meaning of frame +0x18 and of the flag at 0x142E80210. The scene flag word at 0x141876EE8, the UI fade word at 0x141876F00 and the movie host at 0x143CD9C28 have no globals.jsonl record.
