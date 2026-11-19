# NxdDataUserSituation

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 90
- **Rows:** 499 rows of 96 bytes
- **Keyed by:** two keys: id (500..70004) x id2 (0..3)
- **Row layout:** [NxdDataUserSituationRow](../structs/NxdDataUserSituationRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Story situation conditions keyed by situation and slot: up to three check types with indices, values and success flags. Verdict: designer-data.

## Behavior

- V: 499 rows, two keys id (500..70004) x id2 (0..3); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 9 of 20 columns not decoded (see the row layout)
