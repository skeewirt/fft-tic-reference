# NxdDataUISubMenu

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 139
- **Rows:** 3 rows of 20 bytes
- **Keyed by:** one key: id (1..3)
- **Row layout:** [NxdDataUISubMenuRow](../structs/NxdDataUISubMenuRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sub menu definitions (3). Verdict: designer-data.

## Behavior

- V: 3 rows, one key id (1..3); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 4 of 4 columns not decoded (see the row layout)
