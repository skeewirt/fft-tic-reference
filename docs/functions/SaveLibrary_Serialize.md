# SaveLibrary_Serialize

- **Address:** `0x1400C2020`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveLibrary_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveFile_Serialize
- **Callees:** FieldSchema_Run, SaveNewArrivalListA_Serialize, SaveNewArrivalListB_Serialize, SaveKeyNew_Serialize, SaveNewArrivalSub_Serialize, SaveLatestKey_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the library menu state: zodiac stones, books, journal, glossary, world situation and the unlock flag.

## Behavior

- V: builds 6 descriptors and runs FieldSchema_Run over them.
- V: field names: `zodiac_stone`, `book`, `journal`, `glossary`, `world_situation`, `is_unlocked`.
- V: its nested records use SaveNewArrivalListA_Serialize, SaveNewArrivalListB_Serialize, SaveKeyNew_Serialize, SaveNewArrivalSub_Serialize, SaveLatestKey_Serialize.
- V: used by SaveFile_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveNewArrivalListA_Serialize](SaveNewArrivalListA_Serialize.md), [SaveNewArrivalListB_Serialize](SaveNewArrivalListB_Serialize.md), [SaveKeyNew_Serialize](SaveKeyNew_Serialize.md), [SaveNewArrivalSub_Serialize](SaveNewArrivalSub_Serialize.md), [SaveLatestKey_Serialize](SaveLatestKey_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
