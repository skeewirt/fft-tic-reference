# UIName_Assign

- **Address:** `0x1403D87F4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `element *UIName_Assign(element *dst, const element *src)`
- **Callers:** about 70: GUICore_SetCursorTarget, GUICore_SetFocusComponent, GUICore_UpdateFrame, JobTreePanel_SetTextKey, GuiImage_SetIconById, GUIComponent_LoadProps, GUINode_BuildFromFile, GUINode_LoadTree, UIAnim_ApplyTrack, GUIComponent_Init and others
- **Callees:** sub_1403D8D1C (release)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copy-assignment of an interned name handle: takes a reference on src's entry, drops dst's old reference and copies pointer and id.

## Behavior

- V: a element is {+0 char* string, +8 u32 id}. If the ids differ: when src.id != 0 the entry in the name table qword_143CDA2A0 (bucket = id & 0xFFFF, 32 bytes per bucket header with a vector of 16-byte entries, entry = id >> 16) gets its u16 refcount at +12 incremented (bounds-checked); then when dst.id != 0 sub_1403D8D1C releases the old entry; finally dst = src (qword and dword).
- V: equal ids are a no-op. Returns dst.

## State touched

- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [FaceWidget_SetFace](FaceWidget_SetFace.md), [GUIComponentProps_Copy](GUIComponentProps_Copy.md), [GUIComponent_LoadProps](GUIComponent_LoadProps.md), [GUINode_NewState](GUINode_NewState.md), [GuideEntry_Fill](GuideEntry_Fill.md), [GuideSlot_DrawButtons](GuideSlot_DrawButtons.md), [StatusScreen_SetEntry](StatusScreen_SetEntry.md), [sub_1401560D0](sub_1401560D0.md)

## Notes

The name is ours (IDB: sub_1403D87F4). This is the one element function that the cursor / focus code calls: GUICore_SetCursorTarget, GUICore_SetFocusComponent and GUICore_UpdateFrame assign the cursor and focus component names with it (and clear them with sub_1403D8870). The name table is a 127-bucket hash (bucket index = hash % 0x7F + 1, see sub_1403D8A24).

## Open questions

-
