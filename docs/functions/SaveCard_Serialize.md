# SaveCard_Serialize

- **Address:** `0x1400B75A8`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveCard_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveFile_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the memory-card style block header: magic, type, block entry, title, timestamp and icon.

## Behavior

- V: builds 8 descriptors and runs FieldSchema_Run over them.
- V: field names: `magic`, `type`, `blockEntry`, `title`, `timestamp`, `reserve`, `icon`.
- V: used by SaveFile_Serialize.
- I: the `card` section of the save file, inherited from the original console save layout.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
