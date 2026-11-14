# g_InventoryCounts

- **Kind:** global
- **Address:** `0x1411A7C00`
- **Area:** [Items and shops](../areas/items.md)
- **Type:** `uint8[261]`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The party's inventory: one count per item id 0..260, saved with the game. Written by Inventory_AddCount, Inventory_AddWithOverflow, Inventory_ReturnItem, the starting items and the event and battle code.

## Behavior

- V: about 47 code operands address it, rip-relative and image-base relative; the save copies 261 bytes.

## Referenced by

- Described by tables: [InventoryCounts](../tables/InventoryCounts.md)
- Observed behaviours: [ItemIdSpace](../behaviors/ItemIdSpace.md)
- Read by: [BattleMsg_Dispatch](../functions/BattleMsg_Dispatch.md), [Battle_SnapshotLiveState](../functions/Battle_SnapshotLiveState.md), [Inventory_AddCount](../functions/Inventory_AddCount.md), [Inventory_AddWithOverflow](../functions/Inventory_AddWithOverflow.md), [Inventory_BuildEquipList](../functions/Inventory_BuildEquipList.md), [Inventory_RebuildOrders](../functions/Inventory_RebuildOrders.md), [Inventory_SellOverflow](../functions/Inventory_SellOverflow.md), [Item_CountTotal](../functions/Item_CountTotal.md), [Item_IsOwned](../functions/Item_IsOwned.md), [Party_AnyItemBelow99](../functions/Party_AnyItemBelow99.md), [Party_ReturnHandItems](../functions/Party_ReturnHandItems.md), [Unit_ListThrowableItems](../functions/Unit_ListThrowableItems.md), [sub_140153CA0](../functions/sub_140153CA0.md), [sub_140206344](../functions/sub_140206344.md), [sub_140278FEC](../functions/sub_140278FEC.md), [sub_1402C8010](../functions/sub_1402C8010.md), [sub_1402C9F78](../functions/sub_1402C9F78.md), [sub_1402CEEE8](../functions/sub_1402CEEE8.md), [sub_1402EA58C](../functions/sub_1402EA58C.md), [sub_140396174](../functions/sub_140396174.md)
- Written by: [BattleMsg_Dispatch](../functions/BattleMsg_Dispatch.md), [Battle_SnapshotLiveState](../functions/Battle_SnapshotLiveState.md), [GameState_ResetParty](../functions/GameState_ResetParty.md), [Inventory_AddCount](../functions/Inventory_AddCount.md), [Inventory_AddWithOverflow](../functions/Inventory_AddWithOverflow.md), [Inventory_ReturnItem](../functions/Inventory_ReturnItem.md), [Inventory_SellOverflow](../functions/Inventory_SellOverflow.md), [Party_ReturnHandItems](../functions/Party_ReturnHandItems.md), [Save_BootClear](../functions/Save_BootClear.md), [sub_1402888E8](../functions/sub_1402888E8.md), [sub_14028916C](../functions/sub_14028916C.md), [sub_1402C60E4](../functions/sub_1402C60E4.md), [sub_1402C8010](../functions/sub_1402C8010.md), [sub_14030BF04](../functions/sub_14030BF04.md), [sub_1403331F8](../functions/sub_1403331F8.md), [sub_140334A48](../functions/sub_140334A48.md), [sub_1403358FC](../functions/sub_1403358FC.md)

## Notes

V: the Item command decrements the count byte of the used item, indexed by the 16-bit item id, after the record's category byte passes the 0x22 gate; the undo path refuses every id of 261 and above before it adds back. V: the one-byte count and the 99 cap are separate rules: the cap is enforced by the add paths, not by the width of the array.

## Open questions

None recorded.
