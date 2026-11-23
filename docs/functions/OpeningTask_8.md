# OpeningTask_8

- **Address:** `0x140332A7C`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `__int64 __fastcall sub_140332A7C(_DWORD *frame)`
- **Callers:** SceneLoop_Run (0x140331D2D), SceneLoop_RunAlt (0x14039DE79), both indirect through SceneTaskTable; no direct caller and no id-8 push site
- **Callees:** None (the copy is inline)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Table entry 8: a gate that watches the runnable flag of event-task block 2, can set two skip words once (`word_1437F664C` and the latch `byte_142FEF6DF`) while that task runs, and when the task stops it pops itself and conditionally copies a 256-byte block into the event text-bank pointer table. Inferred (not shown by the code): it belongs to the opening's message sequence. No code found pushes id 8, so it is not reached from either scene loop.

## Behavior

- V: the first test is the qword at `off_14078D5D8 + 0x1090`, i.e. the +0x90 field of the 2048-byte task block at index 2. That is the block's runnable flag: `EventTask_Start` sets +0x90 to 1 for the slot it starts. A non-zero value takes the wait path, zero takes the pop path.
- V: on the wait path, when the byte at `g_GlobalWork+100` is non-zero and `byte_142FEF6DF` is zero, it stores 1 in `word_1437F664C` and 1 in `byte_142FEF6DF`, then returns 1. The frame, the task depth and the flag word are not changed.
- V: on the wait path in every other combination it returns without writing the frame, the task depth or any global; only the two reads above run.
- V: on the pop path it stores frame dword 1 in `dword_1418825E8`, decrements the task depth `dword_141877480`, stores 0 in `word_1437F664C` and returns 1.
- V: when frame dword 0 is non-zero, the pop path also copies 256 bytes from `unk_143789A50` into the 32-entry pointer table at `qword_14184A8A0` and stores 0 in `dword_143789814`. When frame dword 0 is zero it skips that copy.
- V: `qword_14184A8A0` is the event text-bank table that `EventText_FindMessage` indexes by the reference's top five bits; the copy fills 32 qwords. `sub_1402DEB24` performs the reverse copy when `dword_143789814` is 0, and the near-identical scene tasks `PagedText_WaitAndClose` and `HelpMessage_Wait` use the same block, so this is the only family that touches the saved table.
- V: no store of task id 8 exists. The complete set of stores to `dword_1418772E0` in this build writes 0, 1, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14 and 15; neither 8 nor 12 appears.
- I: the gate belongs to the opening message sequence and `word_1437F664C` is the message-skip flag the event windows read (rests on the shared latch `byte_142FEF6DF` with `OpeningTask_7` and on the table restore; the readers of `word_1437F664C` were not examined).
- ?: which code pushes id 8 (none was found), what the two frame dwords select, and whether `unk_143789A50` is a saved text-bank table or a copy of another table.

## State touched

- Reads: [g_GlobalWork](../globals/g_GlobalWork.md)

## Notes

Whole body read (204 bytes) and checked in the disassembly. The decompiler shows the runnable-flag test as a qword compare against zero at `off_14078D5D8 + 0x1090`; the pop is a one-step depth decrement. The copy is two 128-byte halves over a 256-byte source, not a call. Task id 8 has no push site, so the handler is a table entry only.

## Open questions

What enters id 8; what the two frame dwords mean; and whether the saved 256-byte block is the event text-bank table's previous contents.
