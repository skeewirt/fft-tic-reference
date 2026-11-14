# GUITextNode_SetRenderScale

- **Address:** `0x1403DD2F0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char GUITextNode_SetRenderScale(GUITextLayout *layout, GUITextLayoutState *st)`
- **Callers:** GUITextNode_Layout
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets the text renderer's per-node state: glyph scale = (int16 size) / 64 and the font slot of the resolved UIFontType.

## Behavior

- V: scale = (float)(int16)node[304] * 0.015625 (= size/64), written as both x and y scale at renderer+9500/+9504.
- V: font slot = signed byte at qword_143CDA288[16*(typeId+9)]; the slot is only set when it is >= 0.
- V: with the font metric unit of 0.75 atlas px (docs/reference/fonts.md) one text size unit is 1/48 of the size in atlas px: output px per atlas px = size * (reference scale) * (screen scale) / 48 for every font. The studio's fontScale() uses exactly this.
- V: when the node's byte +311 is non-zero the layout state's counter at +86 is incremented, and when +312 is non-zero the counter at +87; GUITextNode_Layout's glyph builder (sub_1403DD780) stores those counters as the glyph entry's bold (+86 != 0) and italic (+87 != 0) flags (glyph record bytes +28 / +29, read by GUITextNode_Draw to pick palette +64 = row +60 * row +4 for bold). The loader copies the text block's byte +76 to +311 and byte +77 to +312 (GUINode_BuildFromFile), so the flags are node data: every visible Job Tree text node has byte +76 = 1 (the arrow icon text 0). Live: all glyph records of the title, name plate and chip texts have +28 = 1.

## State touched

- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md), [g_Renderer](../globals/g_Renderer.md)

## Referenced by

- Called by: [GUITextNode_Layout](GUITextNode_Layout.md)

## Notes

The earlier studio rule (divide by each font's ascent) was a fit; it was 5 % off for Zilvertype.

## Open questions

None recorded.
