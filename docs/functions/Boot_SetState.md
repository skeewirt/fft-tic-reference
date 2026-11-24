# Boot_SetState

- **Address:** `0x1401E79A0`
- **Area:** [Application and startup](../areas/app-startup.md)
- **Prototype:** `int __fastcall Boot_SetState(int next)`
- **Callers:** Boot_Frame (0x1400B5BC6, 0x1400B5C53), UIAddonFFTOConfig_OnClose (0x14018904B), sub_1401E7C0C (0x1401E7C50), Boot_UpdateVideo (0x1402562D0), Boot_MovieFrame (0x1402F3234)
- **Callees:** sub_1401E6290, sub_14041FB00, sub_1402F3548, Boot_CloseUI, sub_1401E7C58, Video_RefreshState, Mem_Alloc, sub_1400EC678, sub_14003ABD0

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Changes the boot state. It runs the exit actions of the current state, stores the new state in `dword_140D3AD50` and the two mirrors, then runs the entry actions of the new state. Every boot-state change in the game goes through this function.

## Behavior

- V: the exit switch runs only while the current state is at least 2: state 2 clears bit 0 and sets bit 4 in the flags dword at offset 88 of the display object reached through `qword_143CD9DA8+16` and +280, and when the 64-bit value at `dword_142E7FB00` equals 0xFFFFFFFF00000000 (I: low dword `dword_142E7FB00` is 0 and the next dword `g_MovieRequestId` is -1, i.e. no movie requested), destroys the task manager `qword_143CD9E98` and frees the 268-byte object at `qword_140D405B8`; state 3 calls `sub_1402F3548`; state 4 frees the boot UI object at `g_UIStateFade+32` and calls `Boot_CloseUI`.
- V: state 0 and state 1 have no exit action.
- V: writes `dword_1407829E8 = old state`, then `dword_140D3AD50 = next` and `dword_1407829E4 = next`.
- V: entry 0 calls `sub_1401E7C58`; entry 1 has no action; entry 2 calls `Video_RefreshState`; entry 3 releases the three video textures and leaves the sub-state at 0; entry 4 allocates the boot UI object; entries 5..7 have no action.
- V: entry 4 allocates an 8-byte boot UI object (byte 0 set to 0), stores it at `g_UIStateFade+32`, sets the 16-bit field at `g_UIStateFade+40` to 0x00FF, clears the byte at `g_GlobalWork+100`, clears the dword at `g_ScreenFadeMode+4` (0x142FF9E04, and the following dword) when it is non-zero, and sets the display sub-state `dword_140D3A8D4 = 2`.
- I: the object's second byte (the launcher mode that `Boot_Update` reads) comes from the low byte of the field at `g_UIStateFade+40` before it is reset (rests on `Boot_Update`'s use of the byte; the read of +40 is not shown in the decompiled body).
- V: the boot UI object's bytes are then read by `Boot_Update`: the +42 flag on `g_UIStateFade` opens the launcher in mode 3, mode byte 0 opens mode 1, mode byte 1 opens mode 0, and any other value shows the startup add-on first.
- V: entry 3 resets the three video textures at `qword_141862478`, `qword_141862488` and `qword_141862480`, zeroes the two size dwords, and leaves `dword_140D3A8D4 = 0`; entry 0's `sub_1401E7C58` also leaves the sub-state at 0 (I: no other path in this body writes 0 to it; `Video_RefreshState`, whose body is not read here, is the one unchecked callee).
- V: `next` is stored without a range check. States 5 and 6 have no call site; state 7 is written only by `Boot_UpdateVideo`.
- V: `dword_1407829E8` is read only by `Boot_MovieFrame`, which passes it back to return to the state that was current before the movie.
- V: `dword_1407829E4` is written here and read nowhere in this build.
- V: callers are `Boot_Frame` (state 4's completion at 0x1400B5BC6 and state 1's confirm at 0x1400B5C53), `UIAddonFFTOConfig_OnClose` (state 0, after clearing the variable), `sub_1401E7C0C` (state 4), `Boot_UpdateVideo` (state 7) and `Boot_MovieFrame` (the previous state).
- I: `dword_1407829E8` is the previous-state mirror and `dword_1407829E4` the current-state mirror (rests on the write order and the `Boot_MovieFrame` read).

## State touched

- Calls: [Boot_CloseUI](Boot_CloseUI.md), [Video_RefreshState](Video_RefreshState.md), [Mem_Alloc](Mem_Alloc.md)
- Reads: [g_UIStateFade](../globals/g_UIStateFade.md), [g_GlobalWork](../globals/g_GlobalWork.md), [g_CharaRenderMgr](../globals/g_CharaRenderMgr.md)
- Writes: [g_UIStateFade](../globals/g_UIStateFade.md), [g_GlobalWork](../globals/g_GlobalWork.md)

## Referenced by

- Called by: [Boot_EnterState4](Boot_EnterState4.md), [Boot_Frame](Boot_Frame.md), [Boot_MovieFrame](Boot_MovieFrame.md), [Boot_UpdateVideo](Boot_UpdateVideo.md)

## Notes

Whole body read. The exit switch is keyed on the old state and the entry switch on the new one; the two mirrors are written between them. The state values 5 and 6 never appear as a call argument in this build.

## Open questions

Why entry 2 has no action and why states 5 and 6 exist in the numbering; what `dword_142E7FB00` is and who would set it; whether any consumer of `dword_1407829E4` exists in a later build; and the missing global record for `g_ScreenFadeMode` (0x142FF9E00).
