# SavePageState_Serialize

- **Address:** `0x1400B8698`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SavePageState_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveWorldEvents_Serialize
- **Callees:** FieldSchema_Run

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the state of a scripted page or scene: its data table, address, flags, page and step, work value, book number and page, picture and position, music number, effect mode and ambient sound.

## Behavior

- V: builds 18 descriptors and runs FieldSchema_Run over them.
- V: field names: `dt_tbl`, `dt_adr`, `flg`, `page`, `step`, `work`, `bkno`, `widx`, `pic`, `bkpage`, `paramode`, `musicno`, `effmode`, `pic_x`, `pic_y`, `envsnd`, `para`.
- V: used by SaveWorldEvents_Serialize.
- I: the event-scene state that lets a save resume mid-scene.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md)

## Referenced by

- Called by: [SaveWorldEvents_Serialize](SaveWorldEvents_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
