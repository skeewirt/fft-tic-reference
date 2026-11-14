# SaveShopPoach_Serialize

- **Address:** `0x1400BCDBC`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveShopPoach_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveWorld_Serialize
- **Callees:** FieldSchema_Run, SaveNewFlags_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes shop and poach item bookkeeping: the shop new flag, the poach item count, obtain order, sort order and new flags.

## Behavior

- V: builds 5 descriptors and runs FieldSchema_Run over them.
- V: field names: `shop_new`, `poach_item_num`, `poach_item_get_order`, `poach_item_sort`, `poach_item_new`.
- V: its nested records use SaveNewFlags_Serialize.
- V: used by SaveWorld_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveNewFlags_Serialize](SaveNewFlags_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
