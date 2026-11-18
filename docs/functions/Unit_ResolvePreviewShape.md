# Unit_ResolvePreviewShape

- **Address:** `0x140278EDC`
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Prototype:** `unsigned char Unit_ResolvePreviewShape(unsigned char *unit, unsigned char *outPalette, unsigned char job)`
- **Callers:** JobTree_FillJobRecords, PreviewUnit_BuildRecord, PreviewUnit_ResolveShape and about seven other unit-building functions
- **Callees:** -

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the sprite shape id for a unit/job pair (and a palette byte for special units).

## Behavior

- V: outPalette = 0 first; job 92 and 93 are mapped to 91 and 92 (Dancer/Mime share ids shifted down by one).
- V: unit marker byte unit[0]: 128 (male) and 129 (female) generic job units return marker + 2 * (job + 38) (byte arithmetic): Squire (74) -> 96/97 ... Mime (93 -> 92) -> 132/133; jobs 160, 161 and 164 use marker + 31 / + 33.
- V: marker 130 returns unit[399] with palette unit[400]; markers 165..169 return themselves (the constants -90..-87 are the bytes 166..169); markers 162 and 163 return 163 and 164; any other marker returns itself when it is <= 128, else job + 40.
- V: the marker byte unit[0] is copied from byte +0 of the save record (A+0) when the work record is built.
- V: for marker 130 the shape and palette come from unit+399 and unit+400, which UnitWork_ApplyJobRow fills from the executable job table row bytes 46 and 47 (byte 48 goes to unit+398).

## Referenced by

- Called by: [Battle_BuildRosterTeam](Battle_BuildRosterTeam.md), [Battle_PlaceEntryUnits](Battle_PlaceEntryUnits.md), [JobScreen_UpdateState](JobScreen_UpdateState.md), [JobTree_FillJobRecords](JobTree_FillJobRecords.md), [PreviewUnit_BuildRecord](PreviewUnit_BuildRecord.md), [PreviewUnit_ResolveShape](PreviewUnit_ResolveShape.md), [SceneUnit_FillSpriteRecord](SceneUnit_FillSpriteRecord.md)
- Observed behaviours: [GenericUnitSpriteNumberFromJob](../behaviors/GenericUnitSpriteNumberFromJob.md), [JobChangeTransitionShapeFromTheListEntryByte](../behaviors/JobChangeTransitionShapeFromTheListEntryByte.md), [JobTreePanelSprite](../behaviors/JobTreePanelSprite.md), [NamedCharactersKeepTheirOwnLookWhateverTheirJob](../behaviors/NamedCharactersKeepTheirOwnLookWhateverTheirJob.md), [SceneUnitShapeIsTheQueueWord](../behaviors/SceneUnitShapeIsTheQueueWord.md), [SpriteNumberStoreWidths](../behaviors/SpriteNumberStoreWidths.md)

## Notes

Every tree job (Squire..Mime) maps to a shape in 96..133; all of them use CharShapeLUTParam row 2.

Row bytes 46 and 47 are zero for the generic jobs; they matter for monsters and special units.

## Open questions

The branch for markers above 165 is only partly traced (?).
