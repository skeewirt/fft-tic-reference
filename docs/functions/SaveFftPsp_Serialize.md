# SaveFftPsp_Serialize

- **Address:** `0x1400C2D5C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveFftPsp_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** a wrapper at `sub_1400C2D50`
- **Callees:** FieldSchema_Run, SaveWork_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the `m_fftpsp` record, which wraps the save work.

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `m_fftpsp`.
- V: its nested records use SaveWork_Serialize.
- V: used by a wrapper at `sub_1400C2D50`.
- I: a carried-over section of the portable-console version.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveWork_Serialize](SaveWork_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
