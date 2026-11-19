# StatusLists_BuildOrder

- **Address:** `0x1400F8E94`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `void StatusLists_BuildOrder(void)`
- **Callers:** EquipDetail_BuildCategoryLines
- **Callees:** NxdRegistry_Find, NxdTable_GetEntryByIndex, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Once per run, builds the three display-order key lists the equipment detail lines use.

## Behavior

- V: once (guarded by byte_140C6B2B1): builds unk_140C6B1D0 = up to 40 UIStatusEffect keys ordered by row word +0x20; unk_140C6B270 = up to 40 UIStatusEffectCategory keys ordered by row dword +0x14; unk_140C6B2A8 = up to 8 keys of nxd 55 ordered by row byte +9.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetEntryByIndex](NxdTable_GetEntryByIndex.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Called by: [EquipDetail_BuildCategoryLines](EquipDetail_BuildCategoryLines.md)

## Open questions

None recorded.
