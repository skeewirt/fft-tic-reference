# ConfigGuideFlag_Serialize

- **Address:** `0x1400C4BD4`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void ConfigGuideFlag_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** ConfigFile_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the guide flag.

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `guide_flag`.
- V: used by ConfigFile_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [ConfigFile_Serialize](ConfigFile_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
