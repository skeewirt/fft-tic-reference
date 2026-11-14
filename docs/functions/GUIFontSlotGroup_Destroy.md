# GUIFontSlotGroup_Destroy

- **Address:** `0x1403F3D28`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIFontSlotGroup_Destroy(__int64 group)`
- **Callers:** sub_1403E6038, GUIFactory_FreeSlotGroup
- **Callees:** GUIFontSlotGroup_ReleaseAll, UIName_ReleaseKey

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Destructor: releases all slot references, frees both vectors, and drops the name key.

## Behavior

- V: GUIFontSlotGroup_ReleaseAll(group) first.
- V: vector B (begin +56): if non-null, freed via allocator (*(group+48)) vtable +24 with size (cap +72 - begin) & ~3; begin/end/cap = 0.
- V: vector A (begin +24): likewise via allocator at +16 with size (cap +40 - begin) & ~0xF; zeroed.
- V: if dword +8 != 0, UIName_ReleaseKey(g_UINameTable, key).
- V: callers sub_1403E6038 (0x1403E6158), GUIFactory_FreeSlotGroup (0x1403FED59).

## State touched

- Calls: [GUIFontSlotGroup_ReleaseAll](GUIFontSlotGroup_ReleaseAll.md), [UIName_ReleaseKey](UIName_ReleaseKey.md)
- Reads: [g_UINameTable](../globals/g_UINameTable.md)

## Notes

Mirror of GUIFontSlotGroup_Init; does not free the object itself.

## Open questions

none.
