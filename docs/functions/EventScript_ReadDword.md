# EventScript_ReadDword

- **Address:** `0x1402F0C48`
- **Area:** [Event system](../areas/event-system.md)
- **Prototype:** `uint32_t EventScript_ReadDword(const uint8_t *operand)`
- **Callers:** 46 call sites in 2 routines: EventScript_Run (42) and sub_1401DEC14 (4).
- **Callees:** None

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads a 4-byte little-endian operand from script memory. EventScript_Run uses it for most of its operands.

## Behavior

- V: reads four bytes from the given address in order and combines them: byte n is shifted left by 8 times n and OR-ed into the result, so the first byte is the lowest.
- V: returns the result as an unsigned 32-bit value, zero-extended to 64 bits.
- V: the code is a four-iteration loop with no branches and no global access. The enhanced-edition flag `dword_1407D453C` is not read here; the disassembly has no reference to that address.
- V: EventScript_Run passes addresses of the form script base (`qword_140D40A90`) + instruction offset + k, with k of 1, 2, 3, 5, 9 or 13 in the calls read.

## Notes

I: any difference between the editions in operand size is handled by the callers, not by this function.

## Open questions

Where dword_1407D453C is read, and whether it changes operand sizes in EventScript_Run or in the callers of this function.
