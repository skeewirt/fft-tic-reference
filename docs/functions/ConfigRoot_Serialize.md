# ConfigRoot_Serialize

- **Address:** `0x1400C5E8C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void ConfigRoot_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** a wrapper at `sub_1400C5E80`
- **Callees:** FieldSchema_Run, ConfigFile_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the root of the config file: a single `m_system` record that holds the config body.

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `m_system`.
- V: its nested records use ConfigFile_Serialize.
- V: used by a wrapper at `sub_1400C5E80`.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [ConfigFile_Serialize](ConfigFile_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
