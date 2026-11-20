# SaveHeader_FillBattleFields

- **Address:** `0x1402D0108`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `void SaveHeader_FillBattleFields(void *header)`
- **Callers:** sub_140217EF8
- **Callees:** sub_1402D0080, SceneVar_Read, sub_1402CD168, sub_1405DB08C, PreviewUnit_BuildRecord

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the battle-specific fields of the autosave payload header: the kind, the place bytes and the unit preview records the resume screen reads.

## Behavior

- V: the first byte of the header is the payload kind; a zero returns without filling the battle fields.
- V: the header words at +0x2E and +0x30 are cleared before the loop that fills the six unit entries.
- V: each of the six entries is 0x20 bytes at header +0x4C, and sub_1402D0080 fills one entry per turn-list unit.
- V: SceneVar_Read supplies the place byte and the map id; sub_1402CD168 posts the place message after the header is filled.
- V: PreviewUnit_BuildRecord builds the unit preview records from the source list at 0x141855CE0 and the battle unit table.
- V: the routine is called from the header builder sub_140217EF8, so it is the battle branch of the payload header.
- I: the six entries are the six resume-screen unit slots, because the loop is bounded by six and each entry is one 0x20-byte record.
- ?: what the two place bytes select on the resume screen; the consumer was not read.

## State touched

- Calls: [SceneVar_Read](SceneVar_Read.md), [sub_1402CD168](sub_1402CD168.md), [PreviewUnit_BuildRecord](PreviewUnit_BuildRecord.md)

## Referenced by

- Observed behaviours: [BattleMapIdPathsAndTheirWidths](../behaviors/BattleMapIdPathsAndTheirWidths.md), [PartyResultsAreFoundBySaveIndexInAllRecords](../behaviors/PartyResultsAreFoundBySaveIndexInAllRecords.md), [PlaceNameOfABattleComesFromTheMapRowOfTheLoadedId](../behaviors/PlaceNameOfABattleComesFromTheMapRowOfTheLoadedId.md), [PlaceTextOfAMapIdComesFromTheMapRowAndTheTownRow](../behaviors/PlaceTextOfAMapIdComesFromTheMapRowAndTheTownRow.md)

## Notes

Whole function read (717 bytes).

## Open questions

None recorded.
