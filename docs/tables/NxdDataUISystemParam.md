# NxdDataUISystemParam

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 23
- **Rows:** 301 rows of 8 bytes
- **Keyed by:** one key: id (0..300)
- **Row layout:** [NxdDataUISystemParamRow](../structs/NxdDataUISystemParamRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

UI system parameter values (301). Verdict: engine-data.

## Behavior

- V: 301 rows, one key id (0..300); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 2 columns not decoded (see the row layout)
