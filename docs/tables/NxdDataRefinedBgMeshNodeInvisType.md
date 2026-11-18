# NxdDataRefinedBgMeshNodeInvisType

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** NXD file
- **NXD table id:** 312
- **Rows:** 1 rows of 12 bytes
- **Keyed by:** one key: id (1..1)
- **Row layout:** [NxdDataRefinedBgMeshNodeInvisTypeRow](../structs/NxdDataRefinedBgMeshNodeInvisTypeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Mesh node invisibility type (one row). Verdict: engine-data.

## Behavior

- V: 1 rows, one key id (1..1); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 4 columns not decoded (see the row layout)
