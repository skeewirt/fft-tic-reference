# EventCmd_PlayDefaultCue

- **Address:** `0x1402F2A38`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_PlayDefaultCue(void)`
- **Callers:** EventCmd_Run through the class table, class 48
- **Callees:** sub_14009B2E8 (when the bytes at offsets 8320 and 8321 of the object are both non-zero: reads the id at (object + 64) + 40 + 4 * index, then queues a request through sub_1404FC520 with the name, or sub_1404FC470 without one; otherwise returns an error code.)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 48 handler: calls sub_14009B2E8 on the object at qword_143CD9B60 with index 0, two float parameters from bytes 9 and 10, and the name "default"; then continues.

## Behavior

- V: class 48 argument layout: byte 9 divided by 255.0 is passed as the first float argument; byte 10 divided by 30.0 is passed as the second float argument. Byte 11 is not read.
- V: calls sub_14009B2E8 with qword_143CD9B60, index 0, those two floats and the string "default" as the name.
- V: sets bit 2 (value 4, continue). Returns the value of sub_14009B2E8.
- I: the first float is a 0 to 1 level and the second a time in seconds at 30 per second; the call queues a playback request (it fills a request record of type 3 through sub_1404FC520).

## Notes

The decompiler shows the two floats as untouched integer arguments; the disassembly shows they are converted from bytes 9 and 10. Status bit meanings are the EventCmd_Run loop rules.

## Open questions

What the object at qword_143CD9B60 is, and whether the request is a sound or a music cue. What the "default" name selects.
