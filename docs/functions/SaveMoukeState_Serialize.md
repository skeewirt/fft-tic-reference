# SaveMoukeState_Serialize

- **Address:** `0x1400B8EDC`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveMoukeState_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveWorldEvents_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes a day-counted record: flag, number, current and maximum day, town and unit count and number.

## Behavior

- V: builds 7 descriptors and runs FieldSchema_Run over them.
- V: field names: `flg`, `mou_no`, `now_day`, `max_day`, `town`, `unit_cnt`, `unit_no`.
- V: used by SaveWorldEvents_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveWorldEvents_Serialize](SaveWorldEvents_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
