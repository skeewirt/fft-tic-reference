# Event commands

The 4-byte command language: the handlers EventCmd_Run calls through its class table.

Functions: 57.

## Functions (57)

| Name | Address | Purpose |
|---|---|---|
| [EventCmd_ActivateSlotParam](../functions/EventCmd_ActivateSlotParam.md) | `0x1402F26F0` | Class 39 handler. |
| [EventCmd_AddOffsetIfVarMatches](../functions/EventCmd_AddOffsetIfVarMatches.md) | `0x1402F2B28` | Class 51 handler: reads event variable 24 and, when it equals byte 11, adds bytes 9 and 10 plus 0x8000 to the word at 0x141862452. |
| [EventCmd_AddOffsetWord](../functions/EventCmd_AddOffsetWord.md) | `0x1402F2320` | Class 26 event command: adds a 16-bit argument to the word at offset 2 of the global xmmword_141862450. |
| [EventCmd_AllocSlot](../functions/EventCmd_AllocSlot.md) | `0x1402F24C0` | Class 31 event command: calls SoundCue_Play with argument byte 9 minus 1 and returns the slot number that routine reports. |
| [EventCmd_ClearBitArrayA](../functions/EventCmd_ClearBitArrayA.md) | `0x1402F225C` | Class 22 event command: clears one bit in the 256-bit array at qword_1411A7028, selected by argument byte 9, and sets the continue bit of the status word. |
| [EventCmd_ClearBitArrayB](../functions/EventCmd_ClearBitArrayB.md) | `0x1402F22B8` | Class 24 event command: clears one bit in the 256-bit array at dword_140D4CC28, selected by argument byte 9, and sets the continue bit of the status word. |
| [EventCmd_ClearMode](../functions/EventCmd_ClearMode.md) | `0x1402F241C` | Class 29 event command: resets the state object's mode through sub_1401E0210 when the state object is present, clears status bit 7 and sets the continue bit. |
| [EventCmd_Continue](../functions/EventCmd_Continue.md) | `0x1402F1B20` | Class 2 handler: sets the continue bit in the status word and does nothing else. |
| [EventCmd_CountedWait](../functions/EventCmd_CountedWait.md) | `0x1402F1D5C` | Class 9 handler: a counted wait. |
| [EventCmd_FadeIn](../functions/EventCmd_FadeIn.md) | `0x1402F2784` | Class 41 handler. |
| [EventCmd_FadeOut](../functions/EventCmd_FadeOut.md) | `0x1402F273C` | Class 40 handler. |
| [EventCmd_FlushOffsetWord](../functions/EventCmd_FlushOffsetWord.md) | `0x1402F245C` | Class 30 event command: adds the word at offset 2 of xmmword_141862450 to the high dword of qword_141862470, clamps the sum to 0 to 65535, resets that word to zero, and passes the result to sub_1401E02E8 when the stat... |
| [EventCmd_JumpIfAbove](../functions/EventCmd_JumpIfAbove.md) | `0x1402F2674` | Class 37 handler. |
| [EventCmd_JumpIfBelow](../functions/EventCmd_JumpIfBelow.md) | `0x1402F2624` | Class 36 handler. |
| [EventCmd_JumpIfByteFlagClear](../functions/EventCmd_JumpIfByteFlagClear.md) | `0x1402F21C8` | Class 18: jumps to the byte 10 target when the bit for byte 9 is clear in the flag table at qword_1411A7028 (a flag indexed by one byte). |
| [EventCmd_JumpIfByteFlagSet](../functions/EventCmd_JumpIfByteFlagSet.md) | `0x1402F2170` | Class 17: jumps to the byte 10 target when the bit for byte 9 is set in the flag table at qword_1411A7028 (a flag indexed by one byte). |
| [EventCmd_JumpIfClearB](../functions/EventCmd_JumpIfClearB.md) | `0x1402F2228` | Class 20: jumps to the byte 10 target when the bit for byte 9 is clear in flag table B (dword_140D4CC28). |
| [EventCmd_JumpIfEqual](../functions/EventCmd_JumpIfEqual.md) | `0x1402F2584` | Class 34 handler. |
| [EventCmd_JumpIfFlagClear](../functions/EventCmd_JumpIfFlagClear.md) | `0x1402F2168` | Class 16: jumps to the byte 11 target when the bit for the 16-bit id in bytes 9 and 10 is clear in the flag table at dword_1411A7030. |
| [EventCmd_JumpIfFlagSet](../functions/EventCmd_JumpIfFlagSet.md) | `0x1402F2100` | Class 15: jumps to the byte 11 target when the bit for the 16-bit id in bytes 9 and 10 is set in the flag table at dword_1411A7030. |
| [EventCmd_JumpIfNotEqual](../functions/EventCmd_JumpIfNotEqual.md) | `0x1402F25D4` | Class 35 handler. |
| [EventCmd_JumpIfSetB](../functions/EventCmd_JumpIfSetB.md) | `0x1402F21D0` | Class 19: jumps to the byte 10 target when the bit for byte 9 is set in flag table B (dword_140D4CC28). |
| [EventCmd_JumpIfVarEqual](../functions/EventCmd_JumpIfVarEqual.md) | `0x1402F1CF4` | Class 7 handler: jumps (sets jump-pending with the target byte) when event variable 24 equals argument byte 10, and continues otherwise. |
| [EventCmd_JumpIfVarNotEqual](../functions/EventCmd_JumpIfVarNotEqual.md) | `0x1402F1D54` | Class 8 handler: jumps (sets jump-pending with the target byte) when event variable 24 differs from argument byte 10, and continues otherwise. |
| [EventCmd_JumpWait](../functions/EventCmd_JumpWait.md) | `0x1402F1B14` | Class 1 handler: sets the jump-pending bit and the wait bit together in the status word. |
| [EventCmd_PlayDefaultCue](../functions/EventCmd_PlayDefaultCue.md) | `0x1402F2A38` | Class 48 handler: calls sub_14009B2E8 on the object at qword_143CD9B60 with index 0, two float parameters from bytes 9 and 10, and the name "default"; then continues. |
| [EventCmd_PushHistory](../functions/EventCmd_PushHistory.md) | `0x1402F2BD0` | Class 53 handler: shifts four 16-bit words at 0x141862460, 0x141862462, 0x141862464 and 0x141862466 down by one place and stores byte 9 as the newest word at 0x141862466. |
| [EventCmd_RandomJump](../functions/EventCmd_RandomJump.md) | `0x1402F2070` | Class 14: picks one of three command bytes at random and sets it as a pending jump value. |
| [EventCmd_ReleaseSlot](../functions/EventCmd_ReleaseSlot.md) | `0x1402F2A90` | Class 49 handler: when the 16-bit word at 0x14186246A is non-zero, releases the slot whose signed index is the byte at 0x14186246B and clears its entry. |
| [EventCmd_ResetPending](../functions/EventCmd_ResetPending.md) | `0x1402F2998` | Class 45 handler: calls the reset helper sub_1402B20C0 and clears the 16-bit word at 0x141862472. |
| [EventCmd_Run](../functions/EventCmd_Run.md) | `0x1402F146C` | Runs the 4-byte scripted command loop: it services pending requests, fetches the next 32-bit command into the command register, calls the handler for its command class, and repeats until a command stops or yields. |
| [EventCmd_SelectIndexedSet](../functions/EventCmd_SelectIndexedSet.md) | `0x1402F295C` | Class 44 handler: stores a 16-bit value in the event command word at 0x141862472 and selects an indexed set of four values through sub_1402F1868. |
| [EventCmd_ServiceRequests](../functions/EventCmd_ServiceRequests.md) | `0x1402F1784` | Services the three request mailboxes (event variables 0x5C, 0x5D and 0x5E) that event commands use to ask for sounds and music, then clears them. |
| [EventCmd_SetAccumulator](../functions/EventCmd_SetAccumulator.md) | `0x1402F22E8` | Class 25 event command: stores a 16-bit value from the argument in the high dword of qword_141862470 and, when the state object is present, passes that value to the state setter sub_1401E02E8. |
| [EventCmd_SetBackdrop](../functions/EventCmd_SetBackdrop.md) | `0x1402F1C08` | Class 5 handler: switches the backdrop to the one numbered by argument byte 9, loading its texture file when the mode is zero. |
| [EventCmd_SetBitArrayB](../functions/EventCmd_SetBitArrayB.md) | `0x1402F228C` | Class 23 event command: sets one bit in the 256-bit array at dword_140D4CC28, selected by argument byte 9, and sets the continue bit of the status word. |
| [EventCmd_SetFlagA](../functions/EventCmd_SetFlagA.md) | `0x1402F2230` | Class 21: sets the flag bit named by byte 9 in flag table A (qword_1411A7028), the table that classes 17 and 18 test. |
| [EventCmd_SetHold](../functions/EventCmd_SetHold.md) | `0x1402F1F38` | Class 12: sets or clears the hold state (bit 6 of the status word) and the matching bits on the current scene records. |
| [EventCmd_SetIdPrefixed](../functions/EventCmd_SetIdPrefixed.md) | `0x1402F29EC` | Class 47 handler: calls the reset helper, then passes byte 9 plus 0x10000 to sub_1402B2098. |
| [EventCmd_SetJumpTarget](../functions/EventCmd_SetJumpTarget.md) | `0x1402F1CDC` | Class 6 handler: stores argument byte 9 as a jump target in the status register and sets the jump-pending bit. |
| [EventCmd_SetMode](../functions/EventCmd_SetMode.md) | `0x1402F2358` | Class 28 event command: records a mode byte, then, when the state object is present, drives the state object through sub_1401E0068 and sub_1401E02E8; when it is absent, it sets several global words instead. |
| [EventCmd_SetParamBlock](../functions/EventCmd_SetParamBlock.md) | `0x1402F26C4` | Class 38 handler. |
| [EventCmd_SetRecordOffset](../functions/EventCmd_SetRecordOffset.md) | `0x1402F1DB0` | Class 10 handler: loads three argument bytes into the command registers and, in mode zero, writes two offsets into a 14-dword record selected by a word of xmmword_141862450. |
| [EventCmd_SetScreenRgb](../functions/EventCmd_SetScreenRgb.md) | `0x1402F2AE8` | Class 50 handler: when the dword at offset 48 of qword_143CD9E28 is zero, stores bytes 9, 10 and 11 into three dwords, which class 42 sets to 128 or 0 as a group; continues. |
| [EventCmd_SetSlotRecord](../functions/EventCmd_SetSlotRecord.md) | `0x1402F24E0` | Class 32 event command: passes argument byte 9 to sub_1402F2500, which records it against the value of the current record, and sets the continue bit. |
| [EventCmd_SetTimerFrames](../functions/EventCmd_SetTimerFrames.md) | `0x1402F29B8` | Class 46 handler: stores a byte in dword_140D4CC10, sets dword_140D8DBA8 to 60 times a 16-bit count, clears dword_140D4CA04, and returns byte 11. |
| [EventCmd_ShowMessage](../functions/EventCmd_ShowMessage.md) | `0x1402F2000` | Class 13: shows a scripted event message. |
| [EventCmd_SnapFade](../functions/EventCmd_SnapFade.md) | `0x1402F27CC` | Class 42 handler. |
| [EventCmd_StartMessage](../functions/EventCmd_StartMessage.md) | `0x1402F1B2C` | The command handler (class 3) that opens a message window: it starts EventMessage_Scripted as the task in slot 14 and stores which message to show. |
| [EventCmd_Stop](../functions/EventCmd_Stop.md) | `0x1402F1AD8` | Class 0 handler: sets the stop bit in the status word and, depending on the mode flag, either marks the state of the script runner or passes the record to a helper. |
| [EventCmd_StoreByte9Continue](../functions/EventCmd_StoreByte9Continue.md) | `0x1402F256C` | Class 33: stores argument byte 9 in the word at offset 12 of xmmword_141862460 and sets the continue bit. |
| [EventCmd_SubOffsetWord](../functions/EventCmd_SubOffsetWord.md) | `0x1402F233C` | Class 27 event command: subtracts a 16-bit argument from the word at offset 2 of the global xmmword_141862450. |
| [EventCmd_UiDispatch](../functions/EventCmd_UiDispatch.md) | `0x1402B2098` | Event-command helper that forwards an id to the UI dispatcher with the prefixed-id kind 12: it stores the id, resolves the UI object and tail-jumps to the dispatcher. |
| [EventCmd_WaitForFade](../functions/EventCmd_WaitForFade.md) | `0x1402F2B6C` | Class 52 handler: yields the command loop while a fade is running on the GUI node or while a flag bit is set, and continues otherwise. |
| [EventCmd_WaitForFlag](../functions/EventCmd_WaitForFlag.md) | `0x1402F28F8` | Class 43 handler. |
| [EventCmd_WaitIfBusy](../functions/EventCmd_WaitIfBusy.md) | `0x1402F1BD0` | Class 4 handler: sets either the continue bit or the wait bit depending on a state test. |
| [EventCmd_Yield](../functions/EventCmd_Yield.md) | `0x1402F1F00` | Class 11 handler: marks the current record (bit 4 of its first dword, mode zero only), sets the continue and wait bits in the status word, and sets the high word of the second command register to -1. |
