# NxdDataRefinedBgMeshPolygon

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 232
- **Rows:** 4037 rows of 24 bytes
- **Keyed by:** two keys: id (1..115) x id2 (0..352)
- **Row layout:** [NxdDataRefinedBgMeshPolygonRow](../structs/NxdDataRefinedBgMeshPolygonRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Remastered background polygons keyed by map and index (4037), linked to conditions. Verdict: engine-data.

## Behavior

- V: 4037 rows, two keys id (1..115) x id2 (0..352); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 4 of 6 columns not decoded (see the row layout)
