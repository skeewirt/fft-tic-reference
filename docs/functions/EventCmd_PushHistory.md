# EventCmd_PushHistory

- **Address:** `0x1402F2BD0`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_PushHistory(void)`
- **Callers:** EventCmd_Run through the class table, class 53
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 53 handler: shifts four 16-bit words at 0x141862460, 0x141862462, 0x141862464 and 0x141862466 down by one place and stores byte 9 as the newest word at 0x141862466.

## Behavior

- V: argument layout: byte 9 is the new value; bytes 10 and 11 are not read.
- V: the word at +2 is copied to +0, the word at +4 to +2, the word at +6 to +4 (all offsets from 0x141862460), and the word at +6 is set to byte 9.
- V: sets bit 2 (value 4, continue). Returns byte 9.

## Notes

Four words are kept, not three. Class 53 writes only bytes 0 to 7 of the block; the bytes at 0x14186246A and 0x14186246B belong to classes 38, 39 and 49.

## Open questions

What reads the history words at 0x141862460 to 0x141862466. Who writes the slot index at 0x14186246B.
