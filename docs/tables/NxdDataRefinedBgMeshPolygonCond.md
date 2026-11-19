# NxdDataRefinedBgMeshPolygonCond

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 326
- **Rows:** 78 rows of 20 bytes
- **Keyed by:** one key: id (1..78)
- **Row layout:** [NxdDataRefinedBgMeshPolygonCondRow](../structs/NxdDataRefinedBgMeshPolygonCondRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Polygon condition rows (78). Verdict: engine-data.

## Behavior

- V: 78 rows, one key id (1..78); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 4 of 4 columns not decoded (see the row layout)
