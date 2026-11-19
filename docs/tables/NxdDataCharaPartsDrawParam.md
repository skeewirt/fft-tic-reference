# NxdDataCharaPartsDrawParam

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 305
- **Rows:** 2 rows of 12 bytes
- **Keyed by:** one key: id (1..2)
- **Read by:** [SceneUnit_SetFlag12C](../functions/SceneUnit_SetFlag12C.md)
- **Row layout:** [NxdDataCharaPartsDrawParamRow](../structs/NxdDataCharaPartsDrawParamRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Two rows of part-draw switches. Verdict: engine-data.

## Behavior

- V: 2 rows, one key id (1..2); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 3 of 3 columns not decoded (see the row layout)
