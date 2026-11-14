# SceneUnit_Oscillate120

- **Address:** `0x140240A78`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void SceneUnit_Oscillate120(int32_t ref)`
- **Callers:** EventScript_Run (opcode 0x94 case; call at 0x14023DCD9).
- **Callees:** EventRef_ResolveSlot, SceneUnit_CallbackSend19, ScenePreview_IndexOfSlot, `sub_14021F414`, SceneTask_WaitFrame, SceneUnit_ResetAndQueue4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Runs a 120-frame sequence on one unit: a callback, a helper call, two SceneUnit_ResetAndQueue4 calls with +31 and then -31, waits of 10, 50 and 60 frames, and a final clear of two bytes of the unit's preview record. Opcode 0x94 calls it.

## Behavior

- V: `ref` is the sign-extended 16-bit operand 1 passed as 32 bits. It is resolved with EventRef_ResolveSlot. If the result is exactly 2000, the routine returns with nothing done.
- V: it sets dword_140782CAC to 166 when it already is 166, and to 106 otherwise.
- V: it sets the global callback qword_140D40940 to SceneUnit_CallbackSend19. When dword_140D40948 is nonzero it first zeroes the qwords at +96 and +104 of block 0 of off_140783088 and calls through the global pointer; otherwise it calls SceneUnit_CallbackSend19 directly. Both pass the slot.
- V: index = ScenePreview_IndexOfSlot(slot), kept as a sign-extended value.
- V: it calls sub_14021F414 with the slot and the value 27.
- V: waits 10 frames (SceneTask_WaitFrame ten times), then calls SceneUnit_ResetAndQueue4(slot, 2, 31, 31, 31).
- V: waits 50 frames, then calls SceneUnit_ResetAndQueue4(slot, 2, -31, -31, -31).
- V: waits 60 frames.
- V: writes 0xFF to byte +1 and 0 to byte +437 of preview record `index`, at g_BattleUnitTable plus 512 times index. No test is made on index, so index -1 or a value of 21 or more writes outside the 21 records.
- V: the waits total 120 frames (10 + 50 + 60); the callback and the helper call come before the first wait.

## State touched

- Calls: [EventRef_ResolveSlot](EventRef_ResolveSlot.md), [SceneUnit_CallbackSend19](SceneUnit_CallbackSend19.md), [ScenePreview_IndexOfSlot](ScenePreview_IndexOfSlot.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md), [SceneUnit_ResetAndQueue4](SceneUnit_ResetAndQueue4.md)
- Writes: [g_PreviewUnitTable](../globals/g_PreviewUnitTable.md)

## Notes

The name is an inference from the alternating +31 and -31 values; what the sequence looks like in the game is not read.

## Open questions

What the action code 4 queued by SceneUnit_ResetAndQueue4 does with the +31 and -31 values; what the callback does with the value 27 and the slot; whether the final clear can see index -1 or 21 or more, which would write outside the table.
