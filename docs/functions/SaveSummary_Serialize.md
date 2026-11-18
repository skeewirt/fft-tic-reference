# SaveSummary_Serialize

- **Address:** `0x1400B7C4C`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveSummary_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveInfo_Serialize
- **Callees:** FieldSchema_Run, SaveAnimUnit_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the save-slot summary the load menu shows: hero name, job, level, date, play progress, difficulty and new-game-plus state.

## Behavior

- V: builds 16 descriptors and runs FieldSchema_Run over them.
- V: field names: `complete_flag`, `hero_name`, `job`, `level`, `month`, `day`, `pos`, `version`, `language`, `gameCleared`, `situation`, `difficultyLevel`, `nextEventId`, `newGamePlus`, `mainProgress`, `unitChrParam`.
- V: its nested records use SaveAnimUnit_Serialize.
- V: used by SaveInfo_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveAnimUnit_Serialize](SaveAnimUnit_Serialize.md)

## Referenced by

- Called by: [SaveInfo_Serialize](SaveInfo_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

- Correction: the summary is the first 164 bytes of `info`; `hero_name` is unused (zero) and `chk_sum` is unused (0xFF); the slot-list readers are SaveLoadList_BuildEntries (0x140185D1C) and SaveLoadList_FillItem (0x1401864A4).

## Open questions

None recorded.
