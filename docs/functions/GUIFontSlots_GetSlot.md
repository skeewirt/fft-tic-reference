# GUIFontSlots_GetSlot

- **Address:** `0x1403DB240`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIFontSlots_GetSlot(__int64 slots, int id)`
- **Callers:** sub_1403E3134, sub_1403E9344, GUIFontSlots_GetTextureRect, UIImage_ResolvePart, GUIFontSlotGroup_OnTextureLoaded
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Resolves a texture slot id to its record pointer: ids carry type 0x02 in the top byte and a 1-based index in the low 24 bits.

## Behavior

- V: idx = (id & 0xFFFFFF) - 1; requires (id & 0xFF000000) == 0x02000000.
- V: bounds: idx < (slots[+88] - slots[+80]) >> 5 (32-byte entries; vector begin +80, end +88).
- V: result = the qword at +16 of entry idx (entries are 32 bytes, array begin pointer at slots+80), i.e. the record pointer at entry+16; otherwise returns 0.
- V: callers sub_1403E3134, sub_1403E9344, GUIFontSlots_GetTextureRect, UIImage_ResolvePart, GUIFontSlotGroup_OnTextureLoaded.
- I: id 0 gives idx = -1 which fails the type check, so 0 is the null id.

## Referenced by

- Called by: [GUIFontSlotGroup_OnTextureLoaded](GUIFontSlotGroup_OnTextureLoaded.md), [GUIFontSlots_GetTextureRect](GUIFontSlots_GetTextureRect.md), [UIImage_ResolvePart](UIImage_ResolvePart.md)

## Notes

Type bytes seen in this chunk: 0x02 textures here, 0x03 images (GUIFontSlots_FindImageByName).

## Open questions

none beyond the record field meanings (see GUITextureSlot_Init).
