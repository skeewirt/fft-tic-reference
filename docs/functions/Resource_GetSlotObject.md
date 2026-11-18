# Resource_GetSlotObject

- **Address:** `0x1402BACCC`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `void *Resource_GetSlotObject(int slot)`
- **Callers:** sub_14021A030, SaveSlot_BuildClassicTitle, sub_140226208, sub_140227558, sub_14022F868, sub_140242AA8, sub_14025712C, sub_1402B2EB0, sub_1402B2FA4, sub_1402B32D4, sub_1402B340C, sub_1402B7AE8, sub_1402BB0A0, sub_1402BB6B0, Shop_Open, sub_1402C6514, sub_1402C72B8, Battle_InitScene, EventMessage_Scripted, EventText_FindMessage, sub_1402DEBD4, sub_1402E600C, sub_1402EC31C, sub_1402FB4F8, sub_140301ED8, sub_14032A8A0, sub_140332B48, sub_14033D7E4, sub_14033E038, sub_140343770, sub_1403690B0, sub_14036D66C, sub_14036D948, sub_14037ABBC, sub_14037B144, sub_14037C2EC, sub_14037C6C4, sub_14037D6E8, SaveWork_ImportLegacyHeader, sub_14038FE58, sub_140394940
- **Callees:** sub_140010F50, sub_1403D2004, sub_1403D21F0, sub_1403D21C8, sub_14041FB00, MemFile_Read

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the shared twenty-byte wrapper object for a resource slot, creating and constructing it on first use.

## Behavior

- V: the slot table is indexed at 0x14375F8F0 (image base + 0x375F8F0) plus slot times eight; a non-null entry is returned after the slot check.
- V: a null entry means the slot has not been created; the function allocates 0x20 bytes through sub_140010F50.
- V: the object is zeroed, constructed through sub_1403D2004 and initialised by sub_1403D21F0.
- V: an initialise result of 1 is a failure: the object is released and the function returns 0.
- V: on success the object is stored back into the slot table and the slot index is recorded.
- V: the object holds the file handle that MemFile_Read fills; the slot index selects the resource.
- V: the function is called from nearly every screen and text path, so it is the general resource-object cache.
- I: the 0x20-byte object is a file/resource handle, because the constructor pair and the read helper operate on a handle.
- ?: whether a failed construction leaves the slot empty or writes a tombstone; the failure path returns without a store.

## State touched

- Calls: [MemFile_Read](MemFile_Read.md)

## Referenced by

- Called by: [Battle_InitScene](Battle_InitScene.md), [ClassicMenu_LoadPageArtPack](ClassicMenu_LoadPageArtPack.md), [LegacyMenu_InitWorld](LegacyMenu_InitWorld.md), [Shop_Open](Shop_Open.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md)
- Reads tables: [TextPackPaths](../tables/TextPackPaths.md)

## Notes

Whole function read (250 bytes). The forty callers are the resource, text and screen loaders.

## Open questions

None recorded.
