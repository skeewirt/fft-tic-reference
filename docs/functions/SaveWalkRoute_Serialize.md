# SaveWalkRoute_Serialize

- **Address:** `0x1400C073C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveWalkRoute_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveWorldMap_Serialize
- **Callees:** FieldSchema_Run, SaveIdPair_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the world-map walking route: flags, route number, step counters and maxima, costs, start and end towns, rotation, a stack buffer and two points.

## Behavior

- V: builds 18 descriptors and runs FieldSchema_Run over them.
- V: field names: `flg`, `r_no`, `t_cnt`, `t_max`, `w_cnt`, `w_max`, `rute`, `wr_cnt`, `wr_max`, `wr_cost`, `town_cost`, `town_st`, `town_en`, `r_rot`, `stk_buf`, `pt0`, `pt1`.
- V: its nested records use SaveIdPair_Serialize.
- V: used by SaveWorldMap_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveIdPair_Serialize](SaveIdPair_Serialize.md)

## Referenced by

- Called by: [SaveWorldMap_Serialize](SaveWorldMap_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
