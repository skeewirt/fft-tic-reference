# NxdTable_GetRowById

- **Address:** `0x1403D3AE8`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `__int64 NxdTable_GetRowById(NxdTable *table, unsigned int id, ...)`
- **Callers:** JobTable_GetRow, AbilityTable_GetRow, ItemTable_GetRow, JobCommandTable_GetRow, Icon_FormatPath, UITable_GetRowByKey, JobTree_FillJobRecords, GuiImage_SetIconById and ~250 more
- **Callees:** NxdTable_GetEntryByIndex, NxdTable_BinarySearchRow, NxdTable_GetEntryByKeyIndex, NxdTable_GetEntryByKeysIndex3

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

The generic row lookup of a loaded Nxd table by id: used by JobTable_GetRow, AbilityTable_GetRow, ItemTable_GetRow, JobCommandTable_GetRow, Icon_FormatPath and over 250 other readers.

## Behavior

- V: mode = *(qword *)(table+56); 0 returns 0. Mode 1: when byte +65 is set and id is in [dword +68, dword +72] the row comes from sub_1403D3BE4; when +65 is clear and the dense cache pointer +24 is 0 the binary search sub_1403D4278(*(table+16), 0, *(table+40), id) runs; with a cache, id in [+68, +72] indexes the cache (*(qword *)(cache + 8 * (id - dword +68))), else 0.
- V: mode 2 calls NxdTable_GetEntryByKeyIndex(table, id, 0) (the first row of set id), any other mode NxdTable_GetEntryByKeysIndex3(table, id, 0, 0) (the first leaf of child (id, 0)).

## State touched

- Calls: [NxdTable_GetEntryByIndex](NxdTable_GetEntryByIndex.md), [NxdTable_BinarySearchRow](NxdTable_BinarySearchRow.md), [NxdTable_GetEntryByKeyIndex](NxdTable_GetEntryByKeyIndex.md), [NxdTable_GetEntryByKeysIndex3](NxdTable_GetEntryByKeysIndex3.md)

## Referenced by

- Appears in flows: [NxdTableLoad](../flows/NxdTableLoad.md)
- Called by: [BattleMsg_ResolveEntry](BattleMsg_ResolveEntry.md), [Battle_AwardUnitJp](Battle_AwardUnitJp.md), [CMesId_GetText](CMesId_GetText.md), [EffectNxd_HasFlag24](EffectNxd_HasFlag24.md), [EffectNxd_HasFlag25](EffectNxd_HasFlag25.md), [EffectNxd_HasFlag28](EffectNxd_HasFlag28.md), [EffectNxd_LoadRow](EffectNxd_LoadRow.md), [Effect_TintByNxdScale](Effect_TintByNxdScale.md), [EventControl_ApplyCarry](EventControl_ApplyCarry.md), [EventControl_PausedTick](EventControl_PausedTick.md), [ItemTable_GetName](ItemTable_GetName.md), [ItemTable_GetRowById](ItemTable_GetRowById.md), [Item_IsOwned](Item_IsOwned.md), [OverrideEntry_FillUnitEntry](OverrideEntry_FillUnitEntry.md), [PauseManager_Tick](PauseManager_Tick.md), [PoachTable_GetRowById](PoachTable_GetRowById.md), [SaveLoadList_FillItem](SaveLoadList_FillItem.md), [ShopEntry_Fill](ShopEntry_Fill.md), [Shop_GetUiRowId](Shop_GetUiRowId.md), [StatusScreen_SetCaption](StatusScreen_SetCaption.md), [StatusScreen_SetEntry](StatusScreen_SetEntry.md), [Status_ListCategory](Status_ListCategory.md), [Status_ListSortKey](Status_ListSortKey.md), [sub_14020261C](sub_14020261C.md), [sub_14026EB74](sub_14026EB74.md), [sub_14028A8B0](sub_14028A8B0.md), [sub_14028B180](sub_14028B180.md), [sub_14028B354](sub_14028B354.md), [sub_1402C1628](sub_1402C1628.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md), [sub_1402FB7C8](sub_1402FB7C8.md), [sub_14036E5DC](sub_14036E5DC.md)
- Observed behaviours: [CharShapeRowMissingFaultsTheFormation](../behaviors/CharShapeRowMissingFaultsTheFormation.md)
- Reads file formats: [NxdSingleKeyHeader](../formats/NxdSingleKeyHeader.md), [NxdSingleKeyRows](../formats/NxdSingleKeyRows.md)
- Reads tables: [Ability](../tables/Ability.md), [C_Mes_Id_Sample](../tables/C_Mes_Id_Sample.md), [Item](../tables/Item.md), [Job](../tables/Job.md), [JobCommand](../tables/JobCommand.md), [PoachItem](../tables/PoachItem.md)

## Notes

The name is ours (IDB: sub_1403D3AE8). The mode is the file's header byte 8: 1 single, 2 double, 3 triple keyed (formats NxdSingleKeyHeader, NxdMultiKeyIndex).

## Open questions

? what +65 (range-dense flag) is exactly and who builds the dense cache at +24.
