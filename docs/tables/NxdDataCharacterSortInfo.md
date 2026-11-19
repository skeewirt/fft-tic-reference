# NxdDataCharacterSortInfo

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 44
- **Rows:** 19 rows of 8 bytes
- **Keyed by:** one key: id (0..18)
- **Row layout:** [NxdDataCharacterSortInfoRow](../structs/NxdDataCharacterSortInfoRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sort order data of characters for list screens. Verdict: engine-data.

## Behavior

- V: 19 rows, one key id (0..18); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 4 of 4 columns not decoded (see the row layout)
