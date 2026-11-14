# EventCmd_JumpWait

- **Address:** `0x1402F1B14`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `void EventCmd_JumpWait(void)`
- **Callers:** EventCmd_Run through the class table, class 1
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 1 handler: sets the jump-pending bit and the wait bit together in the status word.

## Behavior

- V: sets bits 1 and 3 (0x2 and 0x8, value 0xA) of the status word unconditionally.
- V: class 1 reads no argument byte (bytes 9, 10 and 11 are not used).
- V: no target value is written by this handler.

## Notes

Compare with class 6, which sets only the jump-pending bit and stores a target.

## Open questions

Where the jump target for a class 1 jump is stored, if any; what the caller does with jump-pending together with wait.
