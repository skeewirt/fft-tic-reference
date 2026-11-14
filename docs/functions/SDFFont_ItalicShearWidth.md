# SDFFont_ItalicShearWidth

- **Address:** `0x1403A942C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `float SDFFont_ItalicShearWidth(SDFFontRenderer *R)`
- **Callers:** GUITextNode_FinishLine, GUITextNode_PlaceGlyph (2 sites), GUITextNode_PlaceIcon
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The horizontal overhang of an italic (sheared) glyph per unit of glyph multiplier: the shear slant times the font's metric unit, the current glyph scale and 48.

## Behavior

- V: returns 0.0 when byte R+189 is 0. Otherwise S = (font.+232 * R+9500) * ((R+9524 * 96.0) * 0.5), where font = the qword at R + 8 * dword(R+9540) + 64 (the current font object), font.+232 is a float, R+9500 is the glyph scale (size / 64, set by GUITextNode_SetRenderScale) and R+9524 is the shear.
- V: the shear R+9524 is initialised to 0.1 (0x3DCCCCCD) by the renderer init sub_1403A8694 and is overwritten per node by GUITextNode_SetRenderScale (and by GUIFontRenderer_UploadPalette) with the dword at UIFontSet row +64 (V, st+24 = the set row, [row + 0x40]).
- V: the same value is used as the shear factor (xmm10 = R+9524 when the italic path is on) in SDFFontRenderer_EmitGlyph.
- I: (96 * 0.5) = 48 is the 1/48 unit of one text size unit (see GUITextNode_SetRenderScale), so S * glyph.f is the width in layout units that the sheared top of a glyph sticks out; font.+232 is the font's metric / scale unit that EmitGlyph also multiplies into every glyph dimension (read at 0x1403A9579).

## Referenced by

- Called by: [GUITextNode_PlaceIcon](GUITextNode_PlaceIcon.md)

## Notes

The name is ours (IDB: sub_1403A942C). Confidence in the name: medium. The arithmetic and its uses (last-glyph width extension, italic transition offsets) are V; calling it a shear 'width' is I because the font field +232 was not identified in the loader. Every use sits behind 'shear > 0 and the glyph's italic byte set', so upright text never reaches it.

## Open questions

? what font+232 is called in the font object (loader not decoded). ? the UIFontSet column that holds the dword at row +64.
