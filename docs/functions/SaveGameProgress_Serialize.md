# SaveGameProgress_Serialize

- **Address:** `0x1400BF970`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveGameProgress_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveGameFlow_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes story progress and the game flag.

## Behavior

- V: builds 2 descriptors and runs FieldSchema_Run over them.
- V: field names: `game_progress`, `game_flag`.
- V: used by SaveGameFlow_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveGameFlow_Serialize](SaveGameFlow_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
