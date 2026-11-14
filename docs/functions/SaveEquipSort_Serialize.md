# SaveEquipSort_Serialize

- **Address:** `0x1400BCB4C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveEquipSort_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveWorld_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the sort orders of the equipment lists for hands, head, armor and accessories, and the order items were obtained in.

## Behavior

- V: builds 5 descriptors and runs FieldSchema_Run over them.
- V: field names: `equip_user_sort_hand`, `equip_user_sort_head`, `equip_user_sort_armor`, `equip_user_sort_accessory`, `item_get_order_sort`.
- V: used by SaveWorld_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
