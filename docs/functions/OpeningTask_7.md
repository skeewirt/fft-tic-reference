# OpeningTask_7

- **Address:** `0x140332704`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `char __fastcall OpeningTask_7(int *frame, __int64 a2)`
- **Callers:** SceneLoop_Run (0x140331D2D), SceneLoop_RunAlt (0x14039DE79), both indirect through SceneTaskTable
- **Callees:** sub_14038F2AC, sub_140380020, EventThread_Yield, TitleScene_Start, sub_14033E898, sub_140273D78, sub_1402B1E74, sub_1402B1D94, MusicSlot_FetchRecord, EventSlot_SetParam, EventSlots_ResetAll, sub_1402B20C0, sub_1402B1ED0, Input_TestAction

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opening stage 7: the return-to-title shortcut. It runs a short text/overlay stage, waits for the overlay to finish, then loads page 0, starts the title scene and clears the skip flag.

## Behavior

- V: dispatched through `SceneTaskTable` when task id 7 is on top. It is pushed only by `sub_1403325E4`, which task 4 calls in state 5; that helper writes 0 at +0x00, 0 at +0x08, 4 at +0x0C and 0 at +0x10.
- V: the stage state is +0x0C; the body uses 4 (entry), 0, 1 and 2. The counter at +0x10 is separate: when non-zero it is incremented and, at 10, bit 0x5000 of `dword_1418825E8` is toggled, `dword_14184B1F0` is cleared and the counter returns to 0.
- V: state 4 clears `g_ScreenFadeMode`; once bit 2 of `dword_141876F00` is clear it calls `sub_14038F2AC` with the two small rectangles (210, 11) and (14, 20), then stores state 0. `sub_14038F2AC` fills a text block and starts event task 12 with `sub_1402B5AE8`.
- V: state 0, when the timer +0x04 is non-zero, decrements it and returns. When it reaches 0 and the id +0x00 is non-zero, it releases the event sound slot +0x08 with `sub_1402B1E74` when that is set, allocates a slot for the id +0x00 with `sub_1402B1D94` and then calls `MusicSlot_FetchRecord`, which activates the event sound slot.
- V: when the latch byte `byte_142FEF6DF` is non-zero, state 0 either moves to state 1 (when +0x00 is 0) or clears +0x00, sets +0x04 to 32 and calls `EventSlot_SetParam(0, 120)`. Moving to state 1 also sets bit 4 of `dword_141876EE8`, writes 1 to the qword at byte offset 24592 of the object behind `off_14078D5D8`, and writes 0 to the qwords at byte offsets 24584 and 24576.
- V: when the skip flag `g_GlobalWork+100` is set, state 0 sets `byte_142FEF6DF` to 1 and returns.
- V: action bit 32 (id 0x1A) sets `dword_14184B1F0` to 1, +0x10 to 1 and bit 0x5000 of `dword_1418825E8`, and reads the byte at index `(__int16)dword_141877720 + 2912` of the IDB-named table `tbl_TextGlyphAdvanceWidths` into +0x00, which is later passed to `sub_1402B1D94` as a sound id (I: the table is probably a sound-id table, not glyph widths; the name comes from the IDB). If the sound slot +0x08 is non-zero it sets +0x04 to 60 and calls `EventSlot_SetParam(0, 120)`; otherwise it allocates a slot for +0x00 with `sub_1402B1D94` and resets the sound state with `sub_1402B1ED0`.
- V: action bit 64 (id 0x1B), when +0x00 is 0, resets the event slots with `sub_1402B20C0` and `EventSlots_ResetAll`, stores state 1 and makes the same writes to `dword_141876EE8` and the `off_14078D5D8` object as the latch path. With +0x00 non-zero it clears +0x00, sets +0x04 to 32 and calls `EventSlot_SetParam(0, 120)`.
- V: state 1 waits until the qword at byte offset 24720 of the object behind `off_14078D5D8` is 0, then stores state 2, sets bits 1 and 2 of `dword_141876F00`, sets `dword_141876F08` to 32 and clears `dword_141876F04`. It does not write `dword_141876EE8` or the `off_14078D5D8` object.
- V: state 2, once bit 2 of `dword_141876F00` is clear, flips bits 4 and 10 of `dword_141876EE8`, loads page 0 with `sub_140380020(0, qword_141876F98)`, waits for the event thread, decrements the task depth and calls `TitleScene_Start`. It then releases `qword_143C51A30` with `sub_14033E898`, clears bit 0 of `dword_143C51A40`, zeroes the high dword of `qword_142E7FB1C`, calls `sub_140273D78(..., 374, 240)`, sets `g_ScreenFadeMode` to 1 and clears `g_GlobalWork+100`.
- I: `byte_142FEF6DF` is an end-request latch shared with task 8 (rests on task 7 setting it when the skip flag is seen and task 8 reading it in its own skip-flag test).
- I: the qword at byte offset 24720 is the completion state of the text overlay (rests on the state 0 writes to the neighbouring byte offsets 24576..24592 and on state 1 waiting for it before the title starts).
- ?: what the text block says and what the two rectangles control; what the byte read from the glyph table represents; and whether state 1 waits for a text overlay or for a movie.

## State touched

- Calls: [EventThread_Yield](EventThread_Yield.md), [TitleScene_Start](TitleScene_Start.md), [MusicSlot_FetchRecord](MusicSlot_FetchRecord.md), [EventSlot_SetParam](EventSlot_SetParam.md), [EventSlots_ResetAll](EventSlots_ResetAll.md), [Input_TestAction](Input_TestAction.md)
- Reads: [g_GlobalWork](../globals/g_GlobalWork.md)
- Writes: [g_GlobalWork](../globals/g_GlobalWork.md)

## Referenced by

- Appears in flows: [OpeningStages](../flows/OpeningStages.md)

## Notes

Whole body read (887 bytes), plus `sub_1403325E4` for the frame initialisation and `sub_14038F2AC` around its text block setup. The only push of task id 7 is in `sub_1403325E4`, called from task 4 state 5; the normal opening path reaches task 1 after task 6 instead. The object behind `off_14078D5D8` is only addressed by byte offset here; no record exists for it.

## Open questions

What the text block and the two rectangles are; what the glyph-table byte at `dword_141877720 + 2912` represents; and what the qword at offset 24720 of the `off_14078D5D8` object tracks.
