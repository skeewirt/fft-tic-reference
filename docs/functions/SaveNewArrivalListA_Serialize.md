# SaveNewArrivalListA_Serialize

- **Address:** `0x1400C1B1C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveNewArrivalListA_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveLibrary_Serialize
- **Callees:** FieldSchema_Run, SaveNewArrival_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes a new-arrival list entry.

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `new_arrival`.
- V: its nested records use SaveNewArrival_Serialize.
- V: used by SaveLibrary_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveNewArrival_Serialize](SaveNewArrival_Serialize.md)

## Referenced by

- Called by: [SaveLibrary_Serialize](SaveLibrary_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
