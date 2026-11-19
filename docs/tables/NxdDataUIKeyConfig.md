# NxdDataUIKeyConfig

- **Kind:** table
- **Area:** [Input](../areas/input.md)
- **Storage:** NXD file
- **NXD table id:** 331
- **Rows:** 12 rows of 16 bytes
- **Keyed by:** one key: id (0..11)
- **Row layout:** [NxdDataUIKeyConfigRow](../structs/NxdDataUIKeyConfigRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Key configuration groups (12). Verdict: engine-data.

## Behavior

- V: 12 rows, one key id (0..11); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 3 of 3 columns not decoded (see the row layout)
