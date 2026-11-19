# NxdDataDebugFIdSound

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 89
- **Rows:** 691 rows of 8 bytes
- **Keyed by:** one key: id (0..690)
- **Row layout:** [NxdDataDebugFIdSoundRow](../structs/NxdDataDebugFIdSoundRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Debug sound id list (691 rows). Verdict: engine-data.

## Behavior

- V: 691 rows, one key id (0..690); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 2 columns not decoded (see the row layout)
