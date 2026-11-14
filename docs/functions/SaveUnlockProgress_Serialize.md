# SaveUnlockProgress_Serialize

- **Address:** `0x1400C169C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveUnlockProgress_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveFile_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes unlock progress: unlocked and progress values, poach item type, summon, geomancy, song and iaido types and the dance turn count.

## Behavior

- V: builds 8 descriptors and runs FieldSchema_Run over them.
- V: field names: `unlocked`, `progress`, `poach_item_type`, `summon_type`, `geomancy_type`, `song_type`, `iaido_type`, `dance_turns_number`.
- V: used by SaveFile_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
