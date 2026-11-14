# UIName_SetKey

- **Address:** `0x1403D8870`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void UIName_SetKey(UIName *dst, const char *str)`
- **Callers:** GUICore_SetCursorTarget, GUICore_SetFocusComponent, GUICore_UpdateFrame, GUICore_FocusNode, GUIComponent_LoadProps, GUIComponent_LoadDef, GUINode_BuildFromFile, GUIComponent_ResetEffects, GuiImage_SetIconById and about 25 more
- **Callees:** sub_1403D8A24, sub_1403D8D1C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Re-points a name handle at the interned entry for str (adds a reference to the new entry, drops the old one).

## Behavior

- V: saves the old id, sets dst.id = 0 and dst.str = the shared empty string Str, then sub_1403D8A24(table qword_143CDA2A0, dst, str, 0) interns / finds the entry for str and fills dst; finally the saved old id is released with sub_1403D8D1C.

## State touched

- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Referenced by

- Called by: [GUIComponent_LoadProps](GUIComponent_LoadProps.md), [GUIFontSlotGroup_SetImageByName](GUIFontSlotGroup_SetImageByName.md)

## Notes

The name is ours (IDB: sub_1403D8870). sub_1403D8A24 hashes the string with h = (h rol 7) ^ c (seed 0x9C43A61E), bucket = h % 0x7F + 1, then probes the bucket's open-addressed vector (matching hash dword at entry+8, string compare, refcount at entry+12).

## Open questions

? the rest of sub_1403D8A24 (insert / reuse of an empty entry; only the lookup half was read).
