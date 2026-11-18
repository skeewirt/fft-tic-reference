# ClassicUi_OpSetBlendWord

- **Address:** `0x140390B0C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpSetBlendWord(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opcode 12: composes the blend and mode word of the following cells.

## Behavior

- V: packs the bits of +2, +3 and +4 into one word with a fixed shift scheme (blend mode in the low bits, a page-high bit and a mode field above).

## Open questions

?: the meaning of each packed field.
