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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 8 of 10 columns not decoded (see the row layout)
