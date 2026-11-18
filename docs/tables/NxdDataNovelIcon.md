# NxdDataNovelIcon

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 220
- **Rows:** 131 rows of 20 bytes
- **Keyed by:** one key: id (0..130)
- **Row layout:** [NxdDataNovelIconRow](../structs/NxdDataNovelIconRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Icons of the novel pages (131). Verdict: designer-data.

## Behavior

- V: 131 rows, one key id (0..130); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 3 of 5 columns not decoded (see the row layout)
