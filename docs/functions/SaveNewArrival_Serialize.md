# SaveNewArrival_Serialize

- **Address:** `0x1400B7504`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveNewArrival_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveNewArrivalListA_Serialize, SaveNewArrivalListB_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes a one-flag record: an `is_newarrival` marker.

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `is_newarrival`.
- V: used by SaveNewArrivalListA_Serialize, SaveNewArrivalListB_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveNewArrivalListA_Serialize](SaveNewArrivalListA_Serialize.md), [SaveNewArrivalListB_Serialize](SaveNewArrivalListB_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
