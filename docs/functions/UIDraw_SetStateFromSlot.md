# UIDraw_SetStateFromSlot

- **Address:** `0x1403DFC34`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 UIDraw_SetStateFromSlot(UIDrawState *st, UIDrawState *st2, GUIFontSlot *slot)`
- **Callers:** UIImageNode_Draw, UIImage_DrawTiled, sub_1403E0AC0
- **Callees:** sub_1403DCA6C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the draw-state flag word from a texture slot record: texture pointer, blend/permutation bits and the SDF flag.

## Behavior

- V: state+16 = the slot texture (sub_1403DCA6C); state+24 low nibble = 6 when slot byte 36 is set else 2; bits 0x70: 0x50 when byte 37 is 0 else 0; state+4 bits 0x2C0 when byte 38 is 0; bit 0x800 = slot byte 34 (the texture SDF flag, texture+120 bit 0); bit 0x1000 = slot byte 33.
- V: with no usable slot the texture pointer is cleared.

## Referenced by

- Called by: [UIDraw_QuadTransformed](UIDraw_QuadTransformed.md), [UIImageNode_Draw](UIImageNode_Draw.md), [UIImage_DrawTiled](UIImage_DrawTiled.md)

## Notes

The ring state word reads 0x52 live (low nibble 2, 0x50, no 0x800).

## Open questions

None recorded.
