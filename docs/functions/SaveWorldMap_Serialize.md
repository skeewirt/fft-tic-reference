# SaveWorldMap_Serialize

- **Address:** `0x1400C0FDC`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveWorldMap_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveFile_Serialize
- **Callees:** FieldSchema_Run, SaveMenuNewA_Serialize, SaveMenuNewLast_Serialize, SaveUwasaMouke_Serialize, SaveSortie_Serialize, SaveMarkerTown_Serialize, SaveWalkRoute_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the world-map state: map menu, deep dungeon, bar, sortie, map and walk info.

## Behavior

- V: builds 6 descriptors and runs FieldSchema_Run over them.
- V: field names: `map_menu`, `deep_dungeon`, `bar`, `sortie`, `map`, `walk_info`.
- V: its nested records use SaveMenuNewA_Serialize, SaveMenuNewLast_Serialize, SaveUwasaMouke_Serialize, SaveSortie_Serialize, SaveMarkerTown_Serialize, SaveWalkRoute_Serialize.
- V: used by SaveFile_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveMenuNewA_Serialize](SaveMenuNewA_Serialize.md), [SaveMenuNewLast_Serialize](SaveMenuNewLast_Serialize.md), [SaveUwasaMouke_Serialize](SaveUwasaMouke_Serialize.md), [SaveSortie_Serialize](SaveSortie_Serialize.md), [SaveMarkerTown_Serialize](SaveMarkerTown_Serialize.md), [SaveWalkRoute_Serialize](SaveWalkRoute_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
