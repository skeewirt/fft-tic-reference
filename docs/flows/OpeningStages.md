# OpeningStages

- **Kind:** flow
- **Area:** [Application and startup](../areas/app-startup.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

How the opening's later stages advance. Task 4 runs the opening text/menu and either pushes the month/day picker (task 5) or takes the return-to-title shortcut (task 7); task 5 pushes the date confirmation page (task 6); task 6 commits the date and hands the scene to task 1, while its back path returns to task 5. The skip paths in tasks 4, 5 and 6 end through `Opening_EndToTitle`; task 7 clears the flag as it starts the title.

## Steps

| Step | Where | Conf | What happens |
|---|---|---|---|
| <a id="0"></a>0 | [OpeningScene_Start](../functions/OpeningScene_Start.md) | V | Mode-0 scene entry: selects UI row 0x11 (row 0 when `g_ShopModeGate` is non-zero), ends any pending fade transition, sets bit 1 and clears bit 6 of `dword_141876EE8`, and pushes task id 0 on the current task stack, initialising the first two dwords of its 100-byte frame. |
| <a id="1"></a>1 | [Opening_LoadMessageSprites](../functions/Opening_LoadMessageSprites.md) | V | Loads the two opening message textures, selects the language's opening sprite list, resets the opening text flags with `sub_14037FC0C`, pushes task id 4 and writes 0 to its state field at frame +0x10. |
| <a id="2"></a>2 | [OpeningTask_4](../functions/OpeningTask_4.md) | V | With `g_ShopModeGate` zero, state 0 waits for `sub_14039DF20`; state 4 runs the opening menu loop `sub_14037B144`. A matching menu result or `dword_142E7FF5C` sets state 5, which pops task 4 and pushes task 7; otherwise task 4 pops itself and `sub_14037E1E8` pushes task 5. A set skip flag moves to state 99 and then 100, ending through `Opening_EndToTitle`. |
| <a id="3"></a>3 | [OpeningTask_5](../functions/OpeningTask_5.md) | V | Month/day picker: waits while the date text unit's 0x100 flag is set, edits month and day with action indices 0xA4/0xA5, and switches the selected field with action masks 0x8000/0x2000. Action 32 or 2048 calls `sub_14037E778` and then `sub_14037EB50`, which pushes task id 6. |
| <a id="4"></a>4 | [OpeningTask_6](../functions/OpeningTask_6.md) | V | Date confirmation page: cursor position 0 commits the date read from task 5's frame, writes event variables 95/96 and the packed date, starts a 60-frame hold, then removes two frames and `sub_1402F0084` pushes task id 1. Action 32 at cursor position 1, or action 64, takes the back path and removes one frame, returning to task 5. |
| <a id="5"></a>5 | [OpeningTask_7](../functions/OpeningTask_7.md) | V | Return-to-title shortcut from task 4 state 5: runs the text block started by `sub_14038F2AC`, waits for the qword at byte offset 24720 of the object behind `off_14078D5D8` to become 0, loads page 0, pops task 7, calls `TitleScene_Start`, clears bit 0 of `dword_143C51A40` and clears `g_GlobalWork+100`. |
| <a id="6"></a>6 | [Opening_EndToTitle](../functions/Opening_EndToTitle.md) | V | Skip and failure exit: releases the three opening objects, clears bit 0 of `dword_143C51A40`, calls `Scene_Init(1)` to start the title scene, clears `word_141874530` and `word_141874534`, and zeroes the qword after `g_ScreenFadeMode`. |

## Behavior

- V: task 4's frame state is the dword at +0x10. The values the body handles are 0 (entry), 4 (opening menu), 5 (shortcut tail), 95..98 (only with `g_ShopModeGate` non-zero), 99 (skip tail start) and 100 (skip tail end). Tasks 5 and 6 have no state field: task 5 is a frame-by-frame picker and task 6 uses the +0x2C hold flag with the +0x30 countdown. Task 7's state is +0x0C and runs 4, 0, 1, 2.
- V: the stack moves are: task 4 pops itself and `sub_14037E1E8` pushes 5; task 5 pushes 6 through `sub_14037EB50`; task 6's back path pops one frame to task 5; task 6's committed path pops two frames and `sub_1402F0084` pushes 1; task 4 state 5 pops itself and `sub_1403325E4` pushes 7; task 7 pops itself before `TitleScene_Start`.
- V: task 7 is pushed only by `sub_1403325E4`, which is reached only from task 4 state 5. The normal opening path after task 6 reaches task 1, not task 7.
- V: the chain has no established entry in this build: task 4 is pushed only by `Opening_LoadMessageSprites`, which is called from id 2 row 0 and id 12 accept; no function stores id 2 or 12. The stages are fully implemented but are not reached from the boot, title or opening paths read here.
- V: `Opening_EndToTitle` is called from tasks 4, 5 and 6 (and from task 1). In task 4 it is the last step of states 99/100; in tasks 5 and 6 it is the second half of a two-phase skip keyed by bit 4 of `dword_141876EE8` and gated by bit 2 of `dword_141876F00`.
- V: task 6's commit writes event variable 95 = month and 96 = day, builds a zero-based ordinal day from the month-length table, normalises month/day, and writes the ordinal day's low byte and (month - 1) x 16 plus its bit 8 into the two bytes at 0x1411A7D15 and 0x1411A7D16.
- V: task 4's state 4 compares the text buffer returned by `sub_14037B144` with a language-selected constant: 10 units for every language except Japanese, 14 units for Japanese. Equality, or a non-zero `dword_142E7FF5C`, takes the task 7 shortcut.
- I: `g_GlobalWork+100` is a skip or return request (rests on the System agent's event-2 handler writing 1 to bytes +100 and +101, and on tasks 4, 5, 6 and 7 all acting on it).
- I: the packed date and the event variables are the date the new party keeps (rests on the month/day picker feeding them and on the commit writing both forms; the consumer was not read).
- ?: what task 1 does with the date and the two event variables; what the compared constant string and `dword_142E7FF5C` are; what the states 95..98 do when `g_ShopModeGate` is non-zero.

## Referenced by

- Appears in flows: [OpeningToTitle](OpeningToTitle.md)

## Notes

Sources: tasks 4, 5, 6 and 7, plus `Opening_LoadMessageSprites`, `sub_14037E1E8`, `sub_14037EB50`, `sub_1403325E4`, `sub_1402F0084`, `Opening_EndToTitle` and `OpeningScene_Start` around their stack pushes and frame writes. Observed scene-frame use, from the frame base: task 4 uses +0x10 for its state. Task 5 uses +0x00 and +0x04 as menu entry ids, +0x08, +0x0C and +0x10 as three scene-unit indices, +0x20 as month, +0x24 as day and +0x28 as the selected field. Task 6 uses +0x00 and +0x04 as menu entry ids, +0x08 as the cursor unit, +0x0C as the cursor position, +0x2C as the hold flag and +0x30 as the hold count, and it reads +0x20/+0x24 from the frame below. Task 7 uses +0x00 as a sound id, +0x04 as a timer, +0x08 as an event sound slot, +0x0C as its state and +0x10 as a blink counter. The layouts differ, so no `SceneFrame` structure is recorded; the offsets stay in this note.

## Open questions

? What task 1 does with event variables 95/96 and the packed date; ? what the compared constant string and `dword_142E7FF5C` represent; ? what the states 95..98 do; ? whether the 60-frame hold in task 6 is a fade or only a delay.
