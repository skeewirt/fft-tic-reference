# PoachList_Build

- **Address:** `0x1401AFFC4`
- **Area:** [Items and shops](../areas/items.md)
- **Prototype:** `int PoachList_Build(uint8_t *out)`
- **Callers:** the poacher screens
- **Callees:** Item_CountEquippedByParty, Item_CountTotal, UITable_GetRowByKey, sub_140066164

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the poacher shop's list: one 48-byte entry for each poach id (1..96) with a non-zero held count.

## Behavior

- V: for poach ids 1..96 with a non-zero count (unk_1411A7A1B), builds a 48-byte entry (see PoachListEntry): +0 item id (PoachItem +0x2C), +4 equipped count, +8 index, +16 total held, +24 poach id, +28 count, +32 PoachItem +0x24 (price), +36 PoachItem +0x28 (sell price), +40 new flag (unk_1411A7B3F).

## State touched

- Calls: [Item_CountEquippedByParty](Item_CountEquippedByParty.md), [Item_CountTotal](Item_CountTotal.md), [UITable_GetRowByKey](UITable_GetRowByKey.md)

## Referenced by

- Observed behaviours: [PoachListSortOrders](../behaviors/PoachListSortOrders.md)

## Notes

The list is sorted by sub_1401CAFE0 (sort_name strings of the PoachItem rows); the other poach list sorters are sub_1401CAB50 and sub_1401CAC8C, the row label is built by sub_1402A6710.

## Open questions

None recorded.
