# NxdRegistry_Find

- **Address:** `0x1403D325C`
- **Area:** [Data access](../areas/data.md)
- **Prototype:** `NxdTable *NxdRegistry_Find(NxdRegistry *reg, int tableId)`
- **Callers:** UITable_GetRow, UITable_GetRowByKey, Job_IsHiddenFromTree, AbilityAction_BuildWorkingCopy, OverrideEntry_LoadBattleEntries, Party_EggUpkeep, and every other by-id table reader (cached into a per-table global after the first lookup)
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the table object registered under a table id, or null when the id is unknown.

## Behavior

- V: hashes the 4 bytes of the id with the 64-bit FNV-1a hash (offset basis and prime of the standard algorithm) and masks the result with the registry's bucket mask (+112).
- V: each bucket holds a first/last node pair in the bucket array (+88); the bucket is walked until a node whose id (+16) equals the argument is found or the last node is passed.
- V: a node is {+0 next, +8 prev, +16 id, +24 table object}; the table object is returned. A miss returns 0 (the registry's end sentinel at +64 is never returned).
- V: does not trigger loading; callers check the table state (+12) and use the row accessors themselves.

## Referenced by

- Called by: [BattleMsg_ResolveEntry](BattleMsg_ResolveEntry.md), [Battle_AwardUnitJp](Battle_AwardUnitJp.md), [CMesId_GetText](CMesId_GetText.md), [EffectNxd_HasFlag24](EffectNxd_HasFlag24.md), [EffectNxd_HasFlag25](EffectNxd_HasFlag25.md), [EffectNxd_HasFlag28](EffectNxd_HasFlag28.md), [EffectNxd_LoadRow](EffectNxd_LoadRow.md), [Effect_TintByNxdScale](Effect_TintByNxdScale.md), [EventControl_ApplyCarry](EventControl_ApplyCarry.md), [EventControl_PausedTick](EventControl_PausedTick.md), [ItemTable_GetName](ItemTable_GetName.md), [ItemTable_GetRowById](ItemTable_GetRowById.md), [Item_IsOwned](Item_IsOwned.md), [OverrideEntry_FillUnitEntry](OverrideEntry_FillUnitEntry.md), [PauseManager_Tick](PauseManager_Tick.md), [PoachTable_GetRowById](PoachTable_GetRowById.md), [ShopEntry_Fill](ShopEntry_Fill.md), [Shop_GetUiRowId](Shop_GetUiRowId.md), [StatusScreen_SetCaption](StatusScreen_SetCaption.md), [StatusScreen_SetEntry](StatusScreen_SetEntry.md), [Status_ListCategory](Status_ListCategory.md), [Status_ListSortKey](Status_ListSortKey.md), [UITable_GetRowByIndex](UITable_GetRowByIndex.md), [UITable_GetRowByKeys](UITable_GetRowByKeys.md), [UITable_GetRowCount](UITable_GetRowCount.md), [UserSituation_IsMet](UserSituation_IsMet.md), [sub_1400F6B5C](sub_1400F6B5C.md), [sub_14020261C](sub_14020261C.md), [sub_1402509E8](sub_1402509E8.md), [sub_1402523B0](sub_1402523B0.md), [sub_14026EB74](sub_14026EB74.md), [sub_14028A8B0](sub_14028A8B0.md), [sub_14028B180](sub_14028B180.md), [sub_14028B354](sub_14028B354.md), [sub_1402C6514](sub_1402C6514.md), [sub_1402C72B8](sub_1402C72B8.md), [sub_1402FB7C8](sub_1402FB7C8.md), [sub_14036E5DC](sub_14036E5DC.md)
- Observed behaviours: [CharShapeRowsANewLookNeeds](../behaviors/CharShapeRowsANewLookNeeds.md)

## Notes

Ids seen at call sites: 19 ui, 39 Ability, 41 JobCommand, 45 Item, 46 Job, 96 OverrideEntryData, 189 GeneralJob, 247 OverrideAbilityActionData, 310 Egg.

## Open questions

None recorded.
