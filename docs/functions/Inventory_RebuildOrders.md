# Inventory_RebuildOrders

- **Address:** `0x1402BB3EC`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `void Inventory_RebuildOrders(void)`
- **Callers:** sub_1401F0C44, sub_1402083B4, sub_140247A4C, sub_1402BC46C, sub_14033E4C4
- **Callees:** sub_1402BB37C, UnitWork_BuildForSlot, ItemOrder_SyncGroup, sub_1402BE694, sub_1400F72F0, sub_1400F7334

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rebuilds the five item order lists and the derived menu state after a load or a party change: it picks the owning unit, syncs every group and refreshes the list globals.

## Behavior

- V: it asks sub_1402BB37C for the current party slot and materialises that unit through UnitWork_BuildForSlot.
- V: the result byte is stored at 0x140D407BB and the five order groups are synced by five calls to ItemOrder_SyncGroup with group 0..4.
- V: sub_1402BE694 rebuilds the derived item lists, and sub_1400F72F0 and sub_1400F7334 refresh the two menu globals.
- V: it clears the words at 0x142FEC52E and 0x142FEC532 and the bytes at 0x142FEC542 before the rebuild.
- V: the group lists are the five item order lists; each is rewritten from the live inventory.
- V: the five callers are the load, party-change and menu-entry paths.
- I: the rebuild is needed because the order lists are saved as indices and must be filtered against the current inventory.
- ?: what sub_1402BB37C returns when no party member is valid; the caller still runs the sync.

## State touched

- Calls: [UnitWork_BuildForSlot](UnitWork_BuildForSlot.md), [ItemOrder_SyncGroup](ItemOrder_SyncGroup.md)
- Reads: [g_InventoryCounts](../globals/g_InventoryCounts.md)

## Notes

Whole function read (436 bytes). The five sync calls are the ItemOrder_SyncGroup call sites.

## Open questions

None recorded.
