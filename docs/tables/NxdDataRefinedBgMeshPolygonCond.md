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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 4 columns not decoded (see the row layout)
