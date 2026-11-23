# OpeningTask_6

- **Address:** `0x14037EDD4`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall OpeningTask_6(int *frame, __int64 a2, __int64 a3, __int64 a4)`
- **Callers:** SceneLoop_Run (0x140331D2D), SceneLoop_RunAlt (0x14039DE79), both indirect through SceneTaskTable
- **Callees:** Opening_EndToTitle, sub_14037E778, EventSlot_SetParam, sub_1402F0084, sub_1402B1ED0, sub_1402B1E74, Input_TestAction, sub_1401D80A8, EventVar_Write, sub_14037FF64, Input_ActionBit, sub_14037FE58

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opening stage 6: the date confirmation page. Its two-position cursor either commits the date chosen in stage 5 or returns to the picker; a commit writes the date, holds for 60 frames and hands the scene on to task 1.

## Behavior

- V: dispatched through `SceneTaskTable` when task id 6 is on top; it is pushed by `sub_14037EB50` from task 5. The first argument is the 100-byte scene frame.
- V: the frame holds two menu ids at +0x00/+0x04, a cursor unit index at +0x08, the cursor position at +0x0C, a hold flag at +0x2C and a hold countdown at +0x30. The chosen date is read from the frame below at +0x20 (month) and +0x24 (day), i.e. from task 5's frame.
- V: when the skip flag `g_GlobalWork+100` is set and bit 4 of `dword_141876EE8` is set, it waits for bit 2 of `dword_141876F00` to clear, subtracts 4 from `dword_14187A3F0`, 4 from `dword_141876EF8` and 8 from `dword_141876F90`, decrements the task depth, flips bit 4 of `dword_141876EE8` and returns `Opening_EndToTitle`.
- V: with the skip flag set and bit 4 of `dword_141876EE8` clear, it calls `sub_14037E778`, sets bit 4, calls `EventSlot_SetParam(0, 96)`, sets bits 1 and 2 of `dword_141876F00` and sets `dword_141876F08` to 32.
- V: while the hold flag +0x2C is non-zero it decrements +0x30 and returns until the countdown reaches 0. At 0 it subtracts 4/4/8 from the three counters, subtracts 2 from the task depth, sets `dword_1418825EC` to 1, calls `sub_1402F0084` and sets `g_ScreenFadeMode` to 1. `sub_1402F0084` selects NXD row 1 and pushes task id 1.
- V: when bit 4 of `dword_141876EE8` is set and bit 2 of `dword_141876F00` is clear, it clears bit 4, resets the event sound state with `sub_1402B1ED0`, calls the slot-release helper `sub_1402B1E74`, sets +0x2C to 1 and +0x30 to 60. This is the start of the 60-frame hold after a commit.
- V: action bit 32 (id 0x1A) requests UI cue 1 on slot 0xA. If the cursor +0x0C is 0, it reads month and day from the frame below, writes event variable 95 = month and 96 = day, sums the preceding month lengths and adds the day minus 1 to form a zero-based ordinal day (from the un-normalised month and day), normalises month/day with `sub_14037FF64`, then writes the two bytes at 0x1411A7D15 and 0x1411A7D16: the first gets the low byte of the ordinal day, the second gets 16 x (normalised month - 1) ORed with bit 8 of the ordinal day. It then calls `EventSlot_SetParam(0, 96)`, sets bits 1 and 2 of `dword_141876F00` and bit 4 of `dword_141876EE8`, and moves the first menu entry's second coordinate (`dword_1418770BC`) to 1000.
- V: action bit 32 with the cursor +0x0C non-zero (after its UI cue 1), and action bit 64 (id 0x1B) at any cursor position (after requesting UI cue 2), take the back path. The back path itself subtracts 3 from `dword_141876F90`, 1 from `dword_14187A3F0` and 2 from `dword_141876EF8`, decrements the task depth once, then resets the two menu entries and the three date units of the frame now on top (task 5): the first entry's state becomes 12 with its colour and offset fields zeroed, the second entry's colour word becomes 0x8080 and its byte becomes 0x80, and the three unit records have their dword at `unk_141879088` set to 0.
- V: repeated action index 0xA4 or 0xA5 (through `Input_ActionBit` and `sub_14037FE58`) flips +0x0C and sets the second coordinate of the menu entry indexed by +0x00 to the cursor unit's coordinate plus 16 times the new +0x0C plus 12, requesting UI cue 3.
- I: the two bytes at 0x1411A7D15 are the packed date: the low 9 bits are the zero-based ordinal day and the high four bits are month - 1 (rests on the sum of the month lengths, the shift by 4 and the masks in the commit).
- I: the 60-frame hold is the pause before the scene hand-off (rests on the countdown being started only after the commit and on `sub_1402F0084` running when it expires).
- ?: what task 1 does with the event variables and the packed date; what the two cursor positions are labelled on screen; and why the ordinal day is built from the date before it is normalised.

## State touched

- Calls: [Opening_EndToTitle](Opening_EndToTitle.md), [EventSlot_SetParam](EventSlot_SetParam.md), [Input_TestAction](Input_TestAction.md), [sub_1401D80A8](sub_1401D80A8.md), [EventVar_Write](EventVar_Write.md)
- Reads: [g_GlobalWork](../globals/g_GlobalWork.md)

## Referenced by

- Appears in flows: [OpeningStages](../flows/OpeningStages.md)

## Notes

Whole body read (945 bytes), plus `sub_14037EB50` for the frame layout and `sub_14037FF64` for the date normalisation. The task-depth arithmetic in the back path was checked against the push sites in tasks 4 and 5. The 60-frame hold is a counter, not a state enum; this handler has no state field.

## Open questions

What task 1 does with event variables 95/96 and the packed date; what the two cursor positions mean on screen; and what the date is used for after the opening.
