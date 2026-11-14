# SaveMarkerTown_Serialize

- **Address:** `0x1400C0698`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveMarkerTown_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveWorldMap_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the marker town record.

## Behavior

- V: builds 1 descriptor and runs FieldSchema_Run over them.
- V: field names: `marker_town`.
- V: used by SaveWorldMap_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveWorldMap_Serialize](SaveWorldMap_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
