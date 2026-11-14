# SaveGameFlow_Serialize

- **Address:** `0x1400BFD78`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveGameFlow_Serialize(SchemaCtx *ctx, Node *node, void *record)`
- **Callers:** SaveFile_Serialize
- **Callees:** FieldSchema_Run, SaveGameProgress_Serialize, SaveItemOpened_Serialize

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Describes the game-flow record: progress with its flag, and the bonus items.

## Behavior

- V: builds 2 descriptors and runs FieldSchema_Run over them.
- V: field names: `game_flow`, `bonus_item`.
- V: its nested records use SaveGameProgress_Serialize, SaveItemOpened_Serialize.
- V: used by SaveFile_Serialize.

## State touched

- Calls: [FieldSchema_Run](FieldSchema_Run.md), [SaveGameProgress_Serialize](SaveGameProgress_Serialize.md), [SaveItemOpened_Serialize](SaveItemOpened_Serialize.md)

## Notes

A record schema for the save and config files; see FieldSchema_Run for how descriptors are walked.

## Open questions

None recorded.
