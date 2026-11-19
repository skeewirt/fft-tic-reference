# NxdDataScionLabels

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 170
- **Rows:** 3323 rows of 12 bytes
- **Keyed by:** one key: id (302152..357594)
- **Row layout:** [NxdDataScionLabelsRow](../structs/NxdDataScionLabelsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Voice line labels (3323): archive file link and packed entry id. Verdict: engine-data.

## Behavior

- V: 3323 rows, one key id (302152..357594); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 1 of 3 columns not decoded (see the row layout)
