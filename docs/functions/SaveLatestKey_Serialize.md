# SaveLatestKey_Serialize

- **Address:** `0x1400C1F7C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveLatestKey_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveLibrary_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the latest-key marker.

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `latest_key`.
- V: used by SaveLibrary_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveLibrary_Serialize](SaveLibrary_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
