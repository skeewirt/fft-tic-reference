# OpeningTask_5

- **Address:** `0x14037E83C`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `char __fastcall OpeningTask_5(int *frame)`
- **Callers:** SceneLoop_Run (0x140331D2D), SceneLoop_RunAlt (0x14039DE79), both indirect through SceneTaskTable
- **Callees:** Opening_EndToTitle, sub_14037E778, EventSlot_SetParam, Input_TestAction, sub_1401D80A8, sub_14037EB50, Input_ActionBit, sub_14037FE58, sub_14037E514

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opening stage 5: the month/day picker. It waits for the date text units to appear, edits the month and day with the directional inputs, and pushes the confirmation stage on accept.

## Behavior

- V: dispatched through `SceneTaskTable` when task id 5 is on top; it is pushed by `sub_14037E1E8` from task 4. The first argument is the 100-byte scene frame.
- V: the date fields are month at frame +0x20, day at +0x24 and the selected field at +0x28. The first date text unit index is +0x0C; `sub_14037E1E8` also fills +0x00 and +0x04 with two menu entry ids, +0x08 with a third unit index, and starts month and day at 1.
- V: it returns at once while the scene unit whose 56-byte record is at `unk_141879070 + 56 * frame[3]` still has bit 0x100 set in its first dword.
- V: when the skip flag `g_GlobalWork+100` is set and bit 4 of `dword_141876EE8` is set, it waits for bit 2 of `dword_141876F00` to clear, subtracts 3 from `dword_14187A3F0`, 2 from `dword_141876EF8` and 5 from `dword_141876F90`, flips bit 4 of `dword_141876EE8` and returns `Opening_EndToTitle`.
- V: with the skip flag set and bit 4 of `dword_141876EE8` clear, it calls `sub_14037E778` on the frame, sets bit 4, calls `EventSlot_SetParam(0, 96)`, sets bits 1 and 2 of `dword_141876F00` and sets `dword_141876F08` to 32.
- V: the two actions that advance the stage are action bit 32 (id 0x1A) and action bit 2048 (id 0x1F). Either one requests UI cue 1 on slot 0xA through `sub_1401D80A8`, calls `sub_14037E778` on the frame, then calls `sub_14037EB50`. That helper pushes task id 6 and fills its frame: two menu ids at +0x00/+0x04, a unit index at +0x08, 0 at +0x0C, 0 at +0x2C and 60 at +0x30.
- V: repeated action index 0xA4 is tested with `Input_ActionBit` and `sub_14037FE58`; when it fires, the selected number is incremented. Repeated action index 0xA5 decrements it.
- V: when +0x28 is 0 the day is edited: incrementing past the month length in `tbl_CalendarDaysPerMonth` sets the day to 1 and advances the month; decrementing below 1 borrows the previous month's length. When +0x28 is non-zero the month is edited: incrementing wraps 12 to 1 and decrementing wraps 1 to 12; the day is clamped to the new month's length.
- V: after a value change it subtracts 2 from `dword_141876F90` and `dword_14187A3F0`, rebuilds the date text with `sub_14037E514` and requests UI cue 3.
- V: the two field-switch actions are action masks 0x8000 (id 0x23) and 0x2000 (id 0x24) through `Input_TestAction`. They toggle the selected field between the two language-dependent values and shift the first menu entry's x position (`dword_1418770B8`) by 32, 42 or 48 units, then request UI cue 3. The shift is 32 when the language word at `g_LanguageInfo+8` is 0, 48 when it is 1 (or `g_LanguageInfo` is null) and 42 otherwise; for language words 2 and above the two selected-field values (0 and 1) are swapped relative to languages 0 and 1.
- I: +0x28 is which date field is selected (rests on the month-only branch when it is non-zero and on the field-switch actions moving it between two values).
- I: flag 0x100 on the date text unit means the unit is still being placed or shown (rests on the early return while it is set and on `sub_14037E1E8` setting it when the units are created).
- ?: what the three unit indices +0x08, +0x0C and +0x10 each draw, and whether actions 0xA4/0xA5 are up/down or left/right on the pad.

## State touched

- Calls: [Opening_EndToTitle](Opening_EndToTitle.md), [EventSlot_SetParam](EventSlot_SetParam.md), [Input_TestAction](Input_TestAction.md), [sub_1401D80A8](sub_1401D80A8.md)
- Reads: [g_GlobalWork](../globals/g_GlobalWork.md), [g_LanguageInfo](../globals/g_LanguageInfo.md)

## Referenced by

- Appears in flows: [OpeningStages](../flows/OpeningStages.md)

## Notes

Whole body read (785 bytes), plus `sub_14037E1E8`, `sub_14037EB50`, `sub_14037E514` and `sub_14037E778` for the frame layout. The unit table at `unk_141879070` is read only through its first dword and its 56-byte stride.

## Open questions

What each of the three date text units is and whether the two value-change actions are up/down or left/right; what flag 0x100 on the unit means.
