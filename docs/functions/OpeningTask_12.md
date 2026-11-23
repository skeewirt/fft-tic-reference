# OpeningTask_12

- **Address:** `0x14037F398`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `void __fastcall sub_14037F398(_DWORD *frame, __int64 a2, int a3)`
- **Callers:** SceneLoop_Run (0x140331D2D), SceneLoop_RunAlt (0x14039DE79), both indirect through SceneTaskTable; no direct caller and no id-12 push site
- **Callees:** Input_TestAction, sub_1401D80A8, memmove, TitleScene_Start, Opening_LoadMessageSprites

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Table entry 12: a two-way gate for the opening stage chain. After the fade, accept loads the opening message sprites (which pushes task 4); cancel refills the scene data buffer from a static 0x1E000-byte block and restarts the title scene. No code in this build pushes id 12.

## Behavior

- V: it returns while bit 2 (0x04) of `dword_141876F00` is set, so it waits for the scene fade to finish before it reads input.
- V: with frame dword 0 at zero it tests the pad: action 64 (script id 0x1B, the cancel id) selects the title path; action 32 (script id 0x1A, the accept id) or 2048 (script id 0x1F) selects the opening path.
- V: the cancel branch requests UI sound cue 2 on slot 10 through `sub_1401D80A8`, sets bits 1 and 2 of `dword_141876F00`, writes 32 to `dword_141876F08`, clears `dword_141876F04` and stores 1 in frame dword 0.
- V: the accept branch requests UI sound cue 1 on slot 10, makes the same flag writes and stores 2 in frame dword 0.
- V: on a later frame with frame dword 0 at 1 it decrements `dword_141876EF8`, `dword_141876F90` and the task depth (a pop), sets bit 6 of `dword_141876EE8`, copies 0x1E000 bytes from the static block at 0x141D3B9E0 to the scene data buffer `qword_141876F98`, and calls `TitleScene_Start`.
- V: the copy has two forms: `memmove` when the destination is above 0x141D599DC or its end is below 0x141D3B9E0, and an inline loop of 30720 dwords otherwise; both move the same 0x1E000 bytes.
- V: with frame dword 0 at 2 it makes the same three decrements (it does not set bit 6) and calls `Opening_LoadMessageSprites`, which loads the opening message textures and pushes task 4.
- V: any other non-zero frame value pops and decrements the counters without starting a scene.
- V: no store of task id 12 exists. The complete set of stores to `dword_1418772E0` writes 0, 1, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14 and 15; neither 8 nor 12 appears.
- I: the two choices are skip and continue: cancel leads to the title, accept leads to the opening stages (rests on the cancel/accept action ids and on the two destinations; `Opening_LoadMessageSprites` is the only function that stores task id 4, and its callers are task 2 and this task).
- I: the 0x1E000-byte block at 0x141D3B9E0 is a scene page buffer rather than loaded file data: the opening stage helper `sub_14039DF20` points one of its page pointers at the same block (rests on that reference and on the copy size).
- ?: what pushes id 12, what the block holds, and why the cancel path copies it before the title start.

## State touched

- Calls: [Input_TestAction](Input_TestAction.md), [sub_1401D80A8](sub_1401D80A8.md), [TitleScene_Start](TitleScene_Start.md), [Opening_LoadMessageSprites](Opening_LoadMessageSprites.md)

## Referenced by

- Appears in flows: [OpeningTransitionTasks](../flows/OpeningTransitionTasks.md)

## Notes

Whole body read (375 bytes). The state field is frame dword 0. The two action ids are the same accept/cancel pair `OpeningTask_5` and `OpeningTask_6` use, and slot 10 is the sound-cue slot `sub_1401D80A8` documents. The copy's bounds test and its two forms were checked in the disassembly. Task id 12 has no push site, so the gate is a table entry only.

## Open questions

What enters id 12; what the 0x1E000-byte block holds; and why the cancel path refills the scene data buffer before `TitleScene_Start`.
