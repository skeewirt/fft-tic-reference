# NxdDataRefinedBgMeshNode

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 153
- **Rows:** 1429 rows of 28 bytes
- **Keyed by:** three keys: id (0..116) x id2 (0..3) x id3 (0..31)
- **Row layout:** [NxdDataRefinedBgMeshNodeRow](../structs/NxdDataRefinedBgMeshNodeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Remastered background mesh nodes keyed by map, group and node. Verdict: engine-data.

## Behavior

- V: 1429 rows, three keys id (0..116) x id2 (0..3) x id3 (0..31); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 10 of 10 columns not decoded (see the row layout)
