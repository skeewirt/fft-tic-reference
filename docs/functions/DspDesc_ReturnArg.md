# DspDesc_ReturnArg

- **Address:** `0x140608B20`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `__int64 __fastcall DspDesc_ReturnArg(__int64 obj, unsigned int value)`
- **Callers:** only through the table at 0x14065CB00 (slots 5 and 15)
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Slots 5 and 15 of the descriptor table at 0x14065CB00: returns its second argument unchanged.

## Behavior

- V: returns `value`; the first argument is unused.

## Notes

V: whole body read (3 bytes). The name is ours.

## Open questions

?: why two slots share it.
