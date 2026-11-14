# EventCmd_Continue

- **Address:** `0x1402F1B20`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `void EventCmd_Continue(void)`
- **Callers:** EventCmd_Run through the class table, class 2
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 2 handler: sets the continue bit in the status word and does nothing else.

## Behavior

- V: sets bit 2 (0x4) of the status word unconditionally.
- V: class 2 reads no argument byte (bytes 9, 10 and 11 are not used).
- V: no other memory is touched.

## Open questions

None recorded.
