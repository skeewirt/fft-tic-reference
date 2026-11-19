# NxdDataUIClassicSubtitles

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 128
- **Rows:** 93 rows of 28 bytes, text in 7 languages
- **Keyed by:** two keys: id (13..19) x id2 (0..42)
- **Row layout:** [NxdDataUIClassicSubtitlesRow](../structs/NxdDataUIClassicSubtitlesRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Classic-mode movie subtitles keyed by movie and line, with start and end seconds. Verdict: text.

## Behavior

- V: 93 rows, two keys id (13..19) x id2 (0..42); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

None recorded.
