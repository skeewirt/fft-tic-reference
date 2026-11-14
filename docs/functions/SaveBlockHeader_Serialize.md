# SaveBlockHeader_Serialize

- **Address:** `0x140032318`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveBlockHeader_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** a routine outside the schema set (`sub_14003395C`)
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the header of a stored data block: its size, checksum and version.

## Behavior

- V: builds 3 descriptors and runs FieldSchema_Run over them.
- V: field names: `size`, `crc`, `version`.
- V: used by a routine outside the schema set (`sub_14003395C`).
- I: an integrity header placed in front of saved blocks.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
