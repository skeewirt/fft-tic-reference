# SaveWork_Serialize

- **Address:** `0x1400C2C40`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveWork_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveFftPsp_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the `saveWork` record.

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `saveWork`.
- V: used by SaveFftPsp_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveFftPsp_Serialize](SaveFftPsp_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
