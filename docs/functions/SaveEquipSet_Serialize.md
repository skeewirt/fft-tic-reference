# SaveEquipSet_Serialize

- **Address:** `0x1400B9744`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveEquipSet_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveUnit_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes one saved equipment set: name, item, ability, job and a double-hand flag.

## Behavior

- V: builds 5 descriptors and runs FieldSchema_Run over them.
- V: field names: `name`, `item`, `ability`, `job`, `is_double_hand`.
- V: used by SaveUnit_Serialize.
- I: the per-set record used by the unit schema's equipment-set fields.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Reads tables: [SaveFieldDescriptorLists](../tables/SaveFieldDescriptorLists.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
