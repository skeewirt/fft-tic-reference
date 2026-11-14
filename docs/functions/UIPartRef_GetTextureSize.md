# UIPartRef_GetTextureSize

- **Address:** `0x1403DCA04`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int *UIPartRef_GetTextureSize(UIPartRef *ref, int out[2])`
- **Callers:** UIDraw_QuadFromTexelRect, UIImageNode_Draw, UIImage_DrawTiled, UIImage_ResolvePart, GUILayer_BuildRecord, sub_1403E2278, sub_1403E9344, sub_1403E9590, sub_1403F3FAC and others (10 functions)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Writes the pixel width and height of the texture a part reference points at (1 x 1 when it has none); the divisor that turns texel rectangles into UVs.

## Behavior

- V: out = (1, 1) first. Resource record R = the first element of the part's resource list when ref[0] is set (small vector at record+112: the single element is inline when (u16 record+120 & 0xFFF8) == 8 and u32 record+124 == 0, otherwise record+112 is a pointer to the array), and then R = *(*(first element + 40) + 16); when ref[0] is null R = ref[1].
- V: when R is non-null: image = *(R + 40); out[0] = u16 image+136 (width), out[1] = u16 image+138 (height). Returns out.

## Referenced by

- Called by: [GUIFontSlotGroup_OnTextureLoaded](GUIFontSlotGroup_OnTextureLoaded.md), [GUIFontSlots_GetTextureRect](GUIFontSlots_GetTextureRect.md), [GUILayer_BuildRecord](GUILayer_BuildRecord.md)

## Notes

The name is ours (IDB: sub_1403DCA04). 16826 hits per 4 s. The part ref layout is {record ptr, fallback R, ...}. u = texelX / width and v = texelY / height are computed in the callers, so an exact simulator must use these integer sizes (as float).

## Open questions

? Which struct the +40 / +16 indirection is (texture slot -> GPU image record); only the +136/+138 sizes were read.
