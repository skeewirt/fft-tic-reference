# UITable_GetRowByKey

- **Address:** `0x1403DBC74`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `void *UITable_GetRowByKey(unsigned int tableId, unsigned int key)`
- **Callers:** JobRecord_FillIconAndGenericFlag, JobTree_RefreshAddon, JobTree_FillJobRecords, PreviewUnit_BuildSpriteRecord, and most other NXD consumers
- **Callees:** sub_1403D325C, sub_1403D3A10, sub_1403D3AE8, sub_1403D2FD8

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the row of an NXD table by table id and row key, or null when the table or row is missing.

## Behavior

- V: the table manager qword_143CD9CD0 must be loaded; table = sub_1403D325C(manager, tableId).
- V: the table state at table+12 must be 2 or 3, and sub_1403D3A10(table) must not report a problem.
- V: row = sub_1403D3AE8(table, key); a missing row returns null and a negative key at row+0 returns the default row unk_1406F5ED0.
- V: otherwise returns sub_1403D2FD8(row), the row data pointer.

## Referenced by

- Called by: [CreditRoll_Step](CreditRoll_Step.md), [EquipDetail_BuildCategoryLines](EquipDetail_BuildCategoryLines.md), [EventPreviewUnits_RunFrames](EventPreviewUnits_RunFrames.md), [Guide_OpenWindow](Guide_OpenWindow.md), [ItemList_GetPossessionIndex](ItemList_GetPossessionIndex.md), [ItemObtainedPanel_Fill](ItemObtainedPanel_Fill.md), [JobChangeAddon_SetState](JobChangeAddon_SetState.md), [JobTable_GetNameText](JobTable_GetNameText.md), [PoachList_Build](PoachList_Build.md), [PreviewUnit_BuildRecord](PreviewUnit_BuildRecord.md), [PreviewUnit_BuildSpriteRecord](PreviewUnit_BuildSpriteRecord.md), [SaveLoadList_FillItem](SaveLoadList_FillItem.md), [ShopItemList_FillRow](ShopItemList_FillRow.md), [TabBar_SetTable](TabBar_SetTable.md), [TavernMenu_OnCommand](TavernMenu_OnCommand.md), [TavernRumourPage_Show](TavernRumourPage_Show.md), [TavernRumour_IsAvailable](TavernRumour_IsAvailable.md), [TavernRumours_BuildList](TavernRumours_BuildList.md), [TextTag_ExpandKeyIcon](TextTag_ExpandKeyIcon.md), [TownMenu_BuildItems](TownMenu_BuildItems.md), [UIText_ResolveCategoryRow](UIText_ResolveCategoryRow.md), [UITexturePath_FromRow](UITexturePath_FromRow.md), [Unit_GetSpriteSetId](Unit_GetSpriteSetId.md), [WorldMapBaseScreen_Open](WorldMapBaseScreen_Open.md), [WorldMapRouteGrow_OnState](WorldMapRouteGrow_OnState.md), [WorldMapRoute_StartGrow](WorldMapRoute_StartGrow.md), [WorldMapScreen_BindNodes](WorldMapScreen_BindNodes.md), [sub_1400F4BCC](sub_1400F4BCC.md), [sub_1400F4C54](sub_1400F4C54.md), [sub_140197BCC](sub_140197BCC.md), [sub_1402A6710](sub_1402A6710.md), [sub_14036E5DC](sub_14036E5DC.md)
- Observed behaviours: [JobTreePanelLookups](../behaviors/JobTreePanelLookups.md)

## Notes

Key-based companion of UITable_GetRow (index-based). Table ids seen: 46 Job, 189 GeneralJob, 41 JobCommand, 0xC8 JobType, 0x112 unit-flag table.

## Open questions

Meaning of the table state values 2/3 and of the default row.
