# NxdDataLauncherGuide

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 277
- **Rows:** 50 rows of 16 bytes, text in 7 languages
- **Keyed by:** two keys: id (1..15) x id2 (0..4)
- **Row layout:** [NxdDataLauncherGuideRow](../structs/NxdDataLauncherGuideRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Launcher guide captions keyed by page and line. Verdict: text.

## Behavior

- V: 50 rows, two keys id (1..15) x id2 (0..4); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

None recorded.
