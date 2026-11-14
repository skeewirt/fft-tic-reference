# SaveJobNew_Serialize

- **Address:** `0x1400C138C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveJobNew_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** None found directly (referenced as a sub-schema).
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the saved job-new record: which jobs the player has not yet looked at, and a disable flag.

## Behavior

- V: builds two descriptors and runs FieldSchema_Run(ctx, node, record, table, 2).
- V: `job_new` is a nested record described by the sub-schema `sub_1400B734C` (an `is_new` flag record), with a count field of 0x7D (125).
- V: `disable_flag` is a single byte at offset 0x15 of the record.
- I: the 125 entries suggest one new-job marker per addressable job id, not only the 23 current jobs.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Notes

- Correction (J7 report): `job_new` has count 21 (not 125); `disable_flag` at +21 has count 125.

## Open questions

Which job ids map to which of the 125 slots.
