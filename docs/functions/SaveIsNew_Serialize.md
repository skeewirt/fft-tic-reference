# SaveIsNew_Serialize

- **Address:** `0x1400B734C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveIsNew_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveMenuNewA_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes a one-flag record: an `is_new` marker.

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `is_new`.
- V: used by SaveMenuNewA_Serialize.
- I: the 'new' badge shown on an entry the player has not looked at yet.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveMenuNewA_Serialize](SaveMenuNewA_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
