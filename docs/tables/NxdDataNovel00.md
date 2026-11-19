# NxdDataNovel00

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 164
- **Rows:** 256 rows of 8 bytes, text in 7 languages
- **Keyed by:** one key: id (0..255)
- **Row layout:** [NxdDataNovel00Row](../structs/NxdDataNovel00Row.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Story novel text pages, book 0 (256 rows). Verdict: text.

## Behavior

- V: 256 rows, one key id (0..255); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

None recorded.
