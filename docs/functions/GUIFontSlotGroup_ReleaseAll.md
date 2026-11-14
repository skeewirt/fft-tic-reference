# GUIFontSlotGroup_ReleaseAll

- **Address:** `0x1403F3DFC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIFontSlotGroup_ReleaseAll(GUIFontSlotGroup *g)`
- **Callers:** GUIFontSlotGroup_Destroy, GuiImage_SetIconById, sub_1402A8EC4, sub_1403D5710
- **Callees:** GUIFontSlots_Release

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Releases every slot id the group holds (+80, +84 and every dword of the vector at +56) with GUIFontSlots_Release and resets the state.

## Behavior

- V: slot id +80: GUIFontSlots_Release(g_GUIFontSlots, id), then +80 = 0; slot id +84: same, +84 = 0; for each dword of the vector +56..+64: Release then the dword = 0.
- V: then word +88 = 0, byte +90 = 0 and +32 = +24 (the 16-byte vector is emptied, its end pointer reset to begin; elements are not individually released here).
- V: returns the old +24.

## State touched

- Calls: [GUIFontSlots_Release](GUIFontSlots_Release.md)
- Reads: [g_GUIFontSlots](../globals/g_GUIFontSlots.md)

## Referenced by

- Called by: [GUIFontSlotGroup_Destroy](GUIFontSlotGroup_Destroy.md)

## Notes

The name is ours (IDB: sub_1403F3DFC). GuiImage_SetIconById calls it before setting a new icon, so changing a Job Tree icon releases the old image slot first.

## Open questions

? what slot +80 holds versus +84 (+84 is the image slot id set by GUIFontSlotGroup_SetImageByName).
