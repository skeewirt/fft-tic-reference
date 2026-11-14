# SaveSortie_Serialize

- **Address:** `0x1400C03C0`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveSortie_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveWorldMap_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes sortie routing: the town and route to avoid, the last route, the restart goal town, and the reserved last town and route.

## Behavior

- V: builds 6 descriptors and runs FieldSchema_Run over them.
- V: field names: `SortieAvoidTown`, `SortieLastRute`, `RestartGoalTown`, `reserveLastTown`, `reserveLastRute`, `bSortieAvoid`.
- V: used by SaveWorldMap_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveWorldMap_Serialize](SaveWorldMap_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
