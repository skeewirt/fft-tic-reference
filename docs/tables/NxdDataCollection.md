# NxdDataCollection

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 121
- **Rows:** 43 rows of 44 bytes, text in 7 languages
- **Keyed by:** one key: id (0..42)
- **Row layout:** [NxdDataCollectionRow](../structs/NxdDataCollectionRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Collection entries (43): name, description and numeric parameters. Verdict: designer-data.

## Behavior

- V: 43 rows, one key id (0..42); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 9 of 11 columns not decoded (see the row layout)
