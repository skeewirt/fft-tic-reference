# EventCmd_SetSlotRecord

- **Address:** `0x1402F24E0`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_SetSlotRecord(void)`
- **Callers:** EventCmd_Run through the class table, class 32
- **Callees:** sub_1402F2500 (calls sub_1402B1ED0, sub_1402B1E74 and sub_1402B1D58, which were not read)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 32 event command: passes argument byte 9 to sub_1402F2500, which records it against the value of the current record, and sets the continue bit.

## Behavior

- V: class_note: argument byte 9 is passed to sub_1402F2500 as its only argument. Bytes 10 and 11 are not read by this handler. The byte at offset 10 and the signed byte at offset 11 of xmmword_141862460 are read inside sub_1402F2500, and they hold values stored by an earlier run of this command.
- V: calls sub_1402F2500 with byte 9 and returns its result.
- V: sets bit 2 (value 4, continue) of WORD6(xmmword_141862440), the status word, after the call.
- V: inside sub_1402F2500: when the byte at offset 10 of xmmword_141862460 is non-zero it calls sub_1402B1ED0; when the signed byte at offset 11 is non-zero it calls sub_1402B1E74 with it, otherwise that value becomes 2; it then calls sub_1402B1D58 with byte 9 and that value; it stores the word at offset 10 of xmmword_141862460 as byte 9 OR (value shifted left by 8); it stores byte 9 in the dword at index (value + 1) of qword_140D49558; it stores the value in dword_140D49568 and returns it.
- V: does not wait.

## State touched

- Calls: [sub_1402F2500](sub_1402F2500.md)

## Referenced by

- Observed behaviours: [EventSoundGroupAndMusicSlotOperandWidths](../behaviors/EventSoundGroupAndMusicSlotOperandWidths.md), [MusicIdTravelsAsAByteInTheScriptPathAndAsADwordInTheTransitionPath](../behaviors/MusicIdTravelsAsAByteInTheScriptPathAndAsADwordInTheTransitionPath.md)

## Notes

Byte 9 is written into the low byte of the word at offset 10 of xmmword_141862460, which the next run of this command reads back as its check byte.

## Open questions

What byte 9 identifies; what sub_1402B1ED0, sub_1402B1E74 and sub_1402B1D58 do; what the table at qword_140D49558 and dword_140D49568 hold.
