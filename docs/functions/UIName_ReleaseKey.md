# UIName_ReleaseKey

- **Address:** `0x1403D8D1C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int64_t UIName_ReleaseKey(NameTable *table, uint32_t keyId)`
- **Callers:** 958 callers (UIName_Key users everywhere)
- **Callees:** sub_140011804 (free), memset, sub_1403EF12C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Drops one reference to an interned UI name; frees the string and shrinks the bucket when the count reaches zero.

## Behavior

- V: `keyId` packs the slot as `bucket | index << 16`; 0 means no key and returns 0 without touching anything.
- V: the bucket is at table + 32*bucket (vector of 16-byte slots); an out-of-range index returns 0.
- V: decrements the 16-bit refcount at slot+12; at zero or below it frees the string (slot+0) when the owned byte (+14) is set, clears the slot and trims trailing empty slots of the bucket.
- V: 958 callers (every code path that built a key with UIName_Key); the standard call is `UIName_ReleaseKey(g_UINameTable, key.id)` with the id taken from the key object (+8).

## Referenced by

- Called by: [BarTop_Setup](BarTop_Setup.md), [Battle_InitScene](Battle_InitScene.md), [FaceWidget_SetFace](FaceWidget_SetFace.md), [GUIFontSlotGroup_Destroy](GUIFontSlotGroup_Destroy.md), [GUIList_SetCount](GUIList_SetCount.md), [JobChange_RunPreviewAnim](JobChange_RunPreviewAnim.md), [ScrollHelper_Bind](ScrollHelper_Bind.md), [StatusScreen_DrawLists](StatusScreen_DrawLists.md), [StatusScreen_SetEntry](StatusScreen_SetEntry.md), [UiNames_InstallCoreNames](UiNames_InstallCoreNames.md), [sub_1401560D0](sub_1401560D0.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md)

## Notes

Pairs with UIName_Intern.

## Open questions

None recorded.
