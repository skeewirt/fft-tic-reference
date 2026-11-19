# NxdDataUIEndCredit

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 307
- **Rows:** 1201 rows of 20 bytes
- **Keyed by:** one key: id (0..1200)
- **Row layout:** [NxdDataUIEndCreditRow](../structs/NxdDataUIEndCreditRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

End credit script rows (1201). Verdict: designer-data.

## Behavior

- V: 1201 rows, one key id (0..1200); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

None recorded.
