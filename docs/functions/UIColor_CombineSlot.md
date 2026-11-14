# UIColor_CombineSlot

- **Address:** `0x1403EE35C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned *UIColor_CombineSlot(unsigned *out, unsigned drawColour, unsigned nodeColour, unsigned rowColour, int mode)`
- **Callers:** GUITextNode_Draw (8 call sites: 4 palette layers x 2 paths)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Colour combiner used by GUITextNode_Draw for each of the four font palette layers: picks or multiplies the draw colour, the node's per-layer colour and the UIFontSet row colour according to a mode.

## Behavior

- V: mode 0: out.r = drawColour.r * nodeColour.r / 255, out.g likewise, out.b likewise (unsigned, truncating), out.a = nodeColour.a (the draw colour's alpha is not used here); the row colour is ignored.
- V: mode 1: out = rowColour (the UIFontSet row colour as is).
- V: mode 2: out.rgb = drawColour * nodeColour * rowColour / 65025 (0xFE01, one divide for the triple product, truncating), out.a = nodeColour.a * rowColour.a / 255.
- V: other modes: out = 0xFFFFFFFF. Returns out.

## Notes

The name is ours (IDB: sub_1403EE35C). In GUITextNode_Draw: drawColour = node colour (+196) times the context colour (per byte / 255), nodeColour = node+280 / +284 / +288 / +292 (the four layer colours), rowColour = UIFontSet row +8 / +16 / +28 / +40, mode = node+264 / +268 / +272 / +276. So the glyph fill colour is only the product drawColour * layer colour in mode 0; which mode the Job Tree nodes use is not read (the mode bytes come from the UIB text block).

## Open questions

The mode values of the Job Tree text nodes (live read of node+264..+276); what the draw alpha does to the palette afterwards.
