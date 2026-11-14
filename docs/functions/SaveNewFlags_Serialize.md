# SaveNewFlags_Serialize

- **Address:** `0x1400B73F0`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveNewFlags_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveShopPoach_Serialize, SaveMenuNewLast_Serialize, SaveMenuNewB_Serialize, SaveMenuNewC_Serialize, SaveNewArrivalSub_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes a two-flag record: `is_new` and `is_newarrival`.

## Behavior

- V: builds 2 descriptors and runs FieldSchema_Run over them.
- V: field names: `is_new`, `is_newarrival`.
- V: used by SaveShopPoach_Serialize, SaveMenuNewLast_Serialize, SaveMenuNewB_Serialize, SaveMenuNewC_Serialize, SaveNewArrivalSub_Serialize.
- I: the 'new' and 'new arrival' badges.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveMenuNewB_Serialize](SaveMenuNewB_Serialize.md), [SaveMenuNewC_Serialize](SaveMenuNewC_Serialize.md), [SaveMenuNewLast_Serialize](SaveMenuNewLast_Serialize.md), [SaveNewArrivalSub_Serialize](SaveNewArrivalSub_Serialize.md), [SaveShopPoach_Serialize](SaveShopPoach_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
