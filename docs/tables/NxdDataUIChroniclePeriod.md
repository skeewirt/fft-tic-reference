# NxdDataUIChroniclePeriod

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 275
- **Rows:** 31 rows of 40 bytes, text in 7 languages
- **Keyed by:** one key: id (0..30)
- **Row layout:** [NxdDataUIChroniclePeriodRow](../structs/NxdDataUIChroniclePeriodRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Chronicle periods (31): condition, type, character list, icon, caption and balloon links. Verdict: designer-data.

## Behavior

- V: 31 rows, one key id (0..30); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 5 of 10 columns not decoded (see the row layout)
