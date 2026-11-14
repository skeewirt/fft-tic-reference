# SaveWorldEvents_Serialize

- **Address:** `0x1400B9228`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveWorldEvents_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveFile_Serialize
- **Callees:** FieldSchema_Run, SavePageState_Serialize, SaveMoukeState_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes world-map event counters and dates: treasure and unregistered find days, delay and finish days, page and static flags, the year of a person, and the event list.

## Behavior

- V: builds 10 descriptors and runs FieldSchema_Run over them.
- V: field names: `treasure_findday`, `unreg_findday`, `mouke_finishday`, `mouke_delay`, `snpl_inf`, `snpl_pageflg`, `snpl_staticflg`, `person_year`, `mouke_event_cnt`, `mouke_event`.
- V: its nested records use SavePageState_Serialize, SaveMoukeState_Serialize.
- V: used by SaveFile_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SavePageState_Serialize](SavePageState_Serialize.md), [SaveMoukeState_Serialize](SaveMoukeState_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
