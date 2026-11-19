# GUIFontRenderer_UploadPalette

- **Address:** `0x1403EDEA4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int GUIFontRenderer_UploadPalette(GUIDrawCtx *ctx, FontPaletteBlock *row)`
- **Callers:** GUITextNode_Draw
- **Callees:** sub_1403C043C, GUIFontSet_FontTypeForLanguage

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds or appends an entry for a font palette block and writes it to the GPU structured buffer SDFPalette (192 bytes per entry) read by shader/SDFFont.tec.

## Behavior

- V (decompile + disassembly): palette +0..63 = a 4x4 matrix (sub_1403C043C); +64/+68/+72 = row floats at +4/+12/+20 (layer widths: UIFontSet.Unknown8 / UnknownC / Unknown10); +80/+84 = row +0x2C/+0x30 times a constant; +88/+92 = row +0x20/+0x24 (UIFontSet.Unknown18 / Unknown1C: the shadow layer's edge and width); +96/+100 = in-memory row +52/+56 (decimal; = UIFontSet.Unknown28 / Unknown2C, 0.1 and 1.0 in every row; live-checked 2026-10-27: every cached palette entry holds 0.1 and 1.0); +128/+144/+160/+112 = colours at row +8/+16/+28/+40 as floats (zeroed when the matching width is <= 0); +176 = (0, 0, 0, row +0x18).
- V: the 80-byte in-memory row is filled by GUIFontTable_Load from the nxd record: +0 ui_font_type, +4 Unknown8, +12 UnknownC, +20 Unknown10, +24 Unknown14, +32 Unknown18, +36 Unknown1C, +44 Unknown20, +48 Unknown24, +60 Unknown30, +64 Unknown34, colours +8/+16/+28/+40 = Unknown54/58/5C/60, type bytes +68 ui_font_type_2, +72/+73/+74 ui_font_type_3/7/8.
- V (decompile; the T values checked against the live palette cache): the row's +60 (UIFontSet.Unknown30, 1.1) multiplies the threshold for runs flagged bold (GUITextNode_Draw: palette +64 = flag ? row+60 * row+4 : row+4), and +64 (UIFontSet.Unknown34, 0.2 / 0.3 / 0.5) is copied to the renderer's +9524 and used by SDFFontRenderer_EmitGlyph as the italic shear of the glyph quad, not as edge softness. [104] is never written here (stays 0, so the outline layer's cap is 0).

## State touched

- Calls: [GUIFontSet_FontTypeForLanguage](GUIFontSet_FontTypeForLanguage.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md), [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Called by: [GUITextNode_Draw](GUITextNode_Draw.md)

## Notes

docs/reference/fonts.md 'SDF text shader' lists the shader maths.

## Open questions

None recorded.
