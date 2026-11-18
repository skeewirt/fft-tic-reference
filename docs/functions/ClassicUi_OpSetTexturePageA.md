# ClassicUi_OpSetTexturePageA

- **Address:** `0x140390A44`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned char *ClassicUi_OpSetTexturePageA(unsigned char *record)`
- **Callers:** ClassicUi_RunLayoutScript
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opcode 9: sets the texture page and palette word used by the following cells.

## Behavior

- V: the page index is the 9-bit value (+2 << 8) + +4 (wrapped to 0x1FF above 0x1FF); the palette index is the low 6 bits of +3; the combined word is page << 6 | palette.

## Open questions

None recorded.
