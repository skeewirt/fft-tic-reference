# EventAngle_Quantize

- **Address:** `0x140240408`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `void EventAngle_Quantize(int32_t angle)`
- **Callers:** EventScript_Run (opcode 0x1F case).
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stores a copy of an angle rounded down to a multiple of 4096 in a global, for angles from -16384 to 16383.

## Behavior

- V: the argument is the full dword at +120 of the record at the global pointer off_1407830D8, passed by EventScript_Run before each opcode 0x1F.
- V: when the argument is from -16384 to 16383 inclusive, it sets dword_142FEC53C to the largest multiple of 4096 that is not greater than the argument (buckets -16384, -12288, ..., 12288).
- V: otherwise dword_142FEC53C is left unchanged.
- V: it reads and writes no other memory and returns nothing.

## Notes

The global is read by no code in this pass; its readers are not traced.

## Open questions

Which code reads dword_142FEC53C.
