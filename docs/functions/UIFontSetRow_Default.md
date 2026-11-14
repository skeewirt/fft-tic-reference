# UIFontSetRow_Default

- **Address:** `0x1403DCAD0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 UIFontSetRow_Default(__int64 row)`
- **Callers:** GUIFontTable_Load, GUIFontTable_GetSetRow, sub_1403E5B84
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills an 80-byte UIFontSet row with engine defaults and returns the row pointer.

## Behavior

- V: floats (decoded from the constants): +4 = 0.5 (0x3F000000, the threshold), +12 = 0.1 (0x3DCCCCCD), +20 = 2.0 (0x40000000, +24 = 0), +32 = 1.0, +36 = 0.5, +44 = 0.25 (0x3E800000), +48 = 0.25, +52 = 0.1, +56 = 1.0, +60 = 1.1 (0x3F8CCCCD), +64 = 0.5, +68 = 0.
- V: colours (ARGB dwords): +8 = 0xFFFFFFFF, +16 = 0xFF000040 (-16777024 as signed), +28 = 0xFFDCDCDC, +40 = 0xFF202020; +0 = 0.
- V: +72 word = 0, +74 byte = 0. The word/byte stores at +9/+17/+29/+41 (0xFFFF) and +11/+19/+31/+43 (0xFF) re-write bytes of the colour dwords with 0xFF (redundant with the dwords).
- I: the field names (threshold, outline widths, colours) come from the earlier sheet; this page confirms the numeric values only.
- V: callers GUIFontTable_Load, GUIFontTable_GetSetRow, sub_1403E5B84.

## Referenced by

- Called by: [GUIFontTable_GetSetRow](GUIFontTable_GetSetRow.md), [GUIFontTable_Load](GUIFontTable_Load.md)

## Notes

Values are exact from the decompile; the semantic of each float (width, softness, outline) is not resolved in this function.

## Open questions

? what +32/+36/+44/+48/+52/+56/+60/+64 each control in the shader (they are SDF width / softness / offset candidates; ?).
