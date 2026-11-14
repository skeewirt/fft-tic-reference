# Inventory_AddWithOverflow

- **Address:** `0x140101058`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int Inventory_AddWithOverflow(void *unused, uint16_t id, void *report, int delta)`
- **Callers:** sub_1401004B4 (one direct site)
- **Callees:** Item_CountEquippedByParty, Item_SellPrice, sub_140284684, sub_14006635C

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Adds to an item's owned count with the game's 99 cap, sells the excess for gil, and appends a four-field record of the transaction to a caller-supplied vector.

## Behavior

- V: the first argument register (rcx) is not read; the id is the 16-bit value in dx, sign-extended and compared against 260 (0x104) before anything else; above it the function returns 260 and changes nothing.
- V: it adds the delta (the low byte of the fourth argument, r9) to the byte count of that id in the inventory array.
- V: over = count + Item_CountEquippedByParty(id) - 99; when over > 0 the stored count becomes 99 - equipped and over * Item_SellPrice(id) is added to gil (event variable 44, sub_140284684).
- V: the transaction record holds four 32-bit fields (a kind tag 1, the item id, the trimmed amount and the gil amount) and is appended to the vector passed in the third argument (r8): begin at +0x10, end at +0x18, 16 bytes per record.
- V: a full vector goes through sub_14006635C instead of writing in place.
- V: only one direct caller reaches it, and it calls the equipped-count helper, the sell-price helper and the gil-adding helper.
- I: the four-field record looks like an audit/log entry for the UI, not state that the item path reads back.
- I: the sign-extension of the id argument is a hazard for ids above 32767: the 16-bit compare is still safe but later 64-bit indexing uses the sign-extended value.

## State touched

- Calls: [Item_CountEquippedByParty](Item_CountEquippedByParty.md), [Item_SellPrice](Item_SellPrice.md)
- Reads: [g_InventoryCounts](../globals/g_InventoryCounts.md)
- Writes: [g_InventoryCounts](../globals/g_InventoryCounts.md)

## Notes

The name is ours (IDB: sub_140101058). The prototype keeps the unused first pointer argument because the id arrives in dx and the report vector in r8; source-level three-argument forms that put the id first do not match the register use.

## Open questions

None recorded.
