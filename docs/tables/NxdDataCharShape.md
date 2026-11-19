# NxdDataCharShape

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 174
- **Rows:** 159 rows of 48 bytes
- **Keyed by:** one key: id (0..158)
- **Read by:** [BattleFormation_DrawUnits](../functions/BattleFormation_DrawUnits.md), [CharShape_ApplyClut](../functions/CharShape_ApplyClut.md), [CharaRender_LookupLutParams](../functions/CharaRender_LookupLutParams.md), [SceneUnit_BuildFromQueueEntry](../functions/SceneUnit_BuildFromQueueEntry.md)
- **Row layout:** [NxdDataCharShapeRow](../structs/NxdDataCharShapeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Per body shape: links to shadow size, palette and palette-parameter rows, and a height value. Verdict: engine-data.

## Behavior

- V: 159 rows, one key id (0..158); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 15 columns not decoded (see the row layout)
