# UIImage_ResolvePart

- **Address:** `0x1403E95E0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `GUIFontSlot *UIImage_ResolvePart(UIRenderer *r, UITextureRef *ref, unsigned partId, int *outRect, int a5, int a6)`
- **Callers:** UIImageNode_Draw
- **Callees:** GUIFontSlots_GetSlot, sub_1403DCA04

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Finds the texture slot and part rectangle for an Image node texture reference and part index.

## Behavior

- V: slot id = ref+80 (default) or the entry of the id list at ref+56 chosen by a6 (clamped); the slot comes from GUIFontSlots_GetSlot; the rectangle is the 16-byte entry in the ref part table (+24), doubled in both coordinates when slot byte 35 is set and the part index > 0; with no part table the whole texture rectangle (0, 0, w, h).

## State touched

- Calls: [GUIFontSlots_GetSlot](GUIFontSlots_GetSlot.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md)

## Referenced by

- Called by: [ComponentEffects_Collect](ComponentEffects_Collect.md), [GUINineGridNode_Draw](GUINineGridNode_Draw.md), [GUINode_DrawKind5](GUINode_DrawKind5.md), [GUINode_DrawKind7](GUINode_DrawKind7.md), [UIImageNode_Draw](UIImageNode_Draw.md)

## Open questions

None recorded.
