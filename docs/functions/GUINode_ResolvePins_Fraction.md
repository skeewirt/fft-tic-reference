# GUINode_ResolvePins_Fraction

- **Address:** `0x1403EF890`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GUINode_ResolvePins_Fraction(GUINode *node)`
- **Callers:** UI layout pass (not traced)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resolves a node's edge pins against its parent size when the pins are stored as fractions of the parent (left/top/right/bottom flags in node+140).

## Behavior

- V: node+56/+60 = left/top, +64/+68 = width/height, +72/+76 = pivot (initialised to size/2 by the constructor sub_1403EF3B4 unless +142).
- V: cached pin floats at +116..+136 start as FLT_MAX; the first call derives them as position / parent size; flags: 1 = left, 2 = top, 4 = right, 8 = bottom (5 / 10 = both opposite pins: the node stretches).
- V: the file's `+0xD4` edge flags (bits 0x1, 0x100, 0x10000, 0x1000000) are the same L, T, R, B bits.

## Referenced by

- Called by: [GUIComponent_UpdateNodeTree](GUIComponent_UpdateNodeTree.md), [GUINode_ResolvePinsDispatch](GUINode_ResolvePinsDispatch.md)

## Notes

Explains why line parts keep their offsets to the component edge when a Reference node is drawn larger than its component (docs/reference/arrows.md).

## Open questions

Which node classes use this variant and which use GUINode_ResolvePins_Offset is not traced (?).
