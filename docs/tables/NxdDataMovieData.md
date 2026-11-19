# NxdDataMovieData

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 65
- **Rows:** 22 rows of 40 bytes
- **Keyed by:** one key: id (1..22)
- **Row layout:** [NxdDataMovieDataRow](../structs/NxdDataMovieDataRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Movie list (22): file path, sound file id and flags. Verdict: designer-data.

## Behavior

- V: 22 rows, one key id (1..22); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

None recorded.
