# FontPaletteBlock_Equals

- **Address:** `0x1403DCB8C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `bool FontPaletteBlock_Equals(const FontPaletteBlock *a, const FontPaletteBlock *b)`
- **Callers:** GUIFontRenderer_UploadPalette
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Equality test of two font palette blocks (the first 68 bytes of the 80-byte UIFontSet row) used to find an existing SDFPalette entry before appending a new one.

## Behavior

- V: exact compare of the int at +0 and of the four colour dwords at +8, +16, +28, +40 (compared byte by byte); every float at +4, +12, +20, +24, +32, +36, +44, +48, +52, +56, +60, +64 compares equal when |a - b| <= 1.1920929e-7 (FLT_EPSILON).
- V: bytes 68..79 (ui_font_type_2 and the +72..+74 bytes) are NOT compared.

## Notes

The name is ours (IDB: sub_1403DCB8C). The row layout is the one in GUIFontRenderer_UploadPalette / GUIFontTable_Load.

## Open questions

? Whether two rows that differ only in +68..+79 are meant to share one palette entry (they do, by this test).
