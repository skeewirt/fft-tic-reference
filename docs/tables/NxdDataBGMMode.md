# NxdDataBGMMode

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 281
- **Rows:** 97 rows of 24 bytes, text in 7 languages
- **Keyed by:** one key: id (0..96)
- **Row layout:** [NxdDataBGMModeRow](../structs/NxdDataBGMModeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Music player list: per entry a tab index, title text and a reference to the sound resource to play. Verdict: designer-data.

## Behavior

- V: 97 rows, one key id (0..96); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 4 of 6 columns not decoded (see the row layout)
