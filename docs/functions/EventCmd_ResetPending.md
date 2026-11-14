# EventCmd_ResetPending

- **Address:** `0x1402F2998`
- **Area:** [Event commands](../areas/event-commands.md)
- **Prototype:** `int64_t EventCmd_ResetPending(void)`
- **Callers:** EventCmd_Run through the class table, class 45
- **Callees:** sub_1402B20C0 (sub_1402BA96C, sub_1402BAB04, sub_140346600)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Class 45 handler: calls the reset helper sub_1402B20C0 and clears the 16-bit word at 0x141862472.

## Behavior

- V: argument layout: no argument byte is read.
- V: calls sub_1402B20C0 (sets dword_141856AA8 to 0, calls sub_1402BA96C with -1, sub_1402BAB04 and sub_140346600).
- V: sets the 16-bit word at 0x141862472 to 0.
- V: sets bit 2 (value 4) of the status word (continue). Returns 0.

## Notes

This handler is the counterpart of class 44 in that both use the word at 0x141862472.

## Open questions

What the reset helpers sub_1402BA96C, sub_1402BAB04 and sub_140346600 clear; the meaning of the word at 0x141862472.
