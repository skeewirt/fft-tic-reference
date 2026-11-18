# sub_1400FA7AC

- **Address:** `0x1400FA7AC`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void sub_1400FA7AC(void *state, int itemId, uint8_t slot)`
- **Callers:** not enumerated
- **Callees:** Item_GetRecord, sub_1402B8C74, sub_1402B8E04

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Adds an equipped item's attribute record and added-effect statuses to a unit's status state.

## Behavior

- V: the item's attribute index (record +7) selects a 26-byte attribute record when below 0x55, else none.
- V: weapon slots (slot below 5) take the weapon sub-record's added-effect index (+7); slot 5 and above take the chemist sub-record's (+2); the 6-byte added-effect record's flag byte 0x80 ORs its 5 status bytes into state +9.., 0x10 into state +14...
- V: it also ORs the weapon element (+6) and the attribute record's bytes into the state.

## State touched

- Calls: [Item_GetRecord](Item_GetRecord.md), [sub_1402B8C74](sub_1402B8C74.md), [sub_1402B8E04](sub_1402B8E04.md)

## Referenced by

- Observed behaviours: [OutfitterPreviewReadsRecordPastItemBlockWithSessionFlag](../behaviors/OutfitterPreviewReadsRecordPastItemBlockWithSessionFlag.md)
- Reads tables: [InflictRecords](../tables/InflictRecords.md), [ItemAttributes](../tables/ItemAttributes.md)

## Notes

- Only the table reads were studied.

## Open questions

None recorded.
