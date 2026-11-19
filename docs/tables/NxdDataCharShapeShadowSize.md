# NxdDataCharShapeShadowSize

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 176
- **Rows:** 12 rows of 12 bytes
- **Keyed by:** one key: id (0..15)
- **Read by:** [CharaRender_LookupLutParams](../functions/CharaRender_LookupLutParams.md)
- **Row layout:** [NxdDataCharShapeShadowSizeRow](../structs/NxdDataCharShapeShadowSizeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Twelve shadow sizes (a float per row). Verdict: engine-data.

## Behavior

- V: 12 rows, one key id (0..15); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
