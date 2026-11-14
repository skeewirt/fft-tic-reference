# EventCmd_AllocSlot

- **Address:** `0x1402F24C0`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_AllocSlot(void)`
- **Callers:** EventCmd_Run through the class table, class 31
- **Callees:** SoundCue_Play (converts the value with sub_1402BA9C8, scans slots 13 to 19 with sub_1401D7808, and stores with sub_1401D736C)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 31 event command: calls SoundCue_Play with argument byte 9 minus 1 and returns the slot number that routine reports.

## Behavior

- V: class_note: argument byte 9 is read. The value passed on is byte 9 minus 1 as an unsigned 32-bit number, so byte 9 equal to 0 gives 0xFFFFFFFF. Bytes 10 and 11 are not read.
- V: calls SoundCue_Play with that value and returns its result.
- V: sets bit 2 (value 4, continue) of WORD6(xmmword_141862440), the status word, after the call.
- V: does not wait.
- V: SoundCue_Play converts the value with sub_1402BA9C8 and returns 0xFFFFFFFF when the result is above 0x2B1; otherwise it scans slots 13 to 19 (index 0 to 6, plus 13) with sub_1401D7808 on qword_143CD9DD8 for a free one, stores the converted value there with sub_1401D736C and in dword_14375F8C4[index], and returns the slot number; 0xFFFFFFFF when all seven are used.

## State touched

- Calls: [SoundCue_Play](SoundCue_Play.md)

## Notes

The return value is the slot number 13 to 19, or 0xFFFFFFFF when the converted value is too large or no slot is free.

## Open questions

What the byte 9 value means (it is shifted by minus one before use); what the table at qword_143CD9DD8 and the array dword_14375F8C4 hold.
