# NxdDataUISubtitles

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 138
- **Rows:** 662 rows of 52 bytes, text in 7 languages
- **Keyed by:** two keys: id (1..22) x id2 (0..435)
- **Row layout:** [NxdDataUISubtitlesRow](../structs/NxdDataUISubtitlesRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Event subtitles keyed by event and line, linked to voice labels. Verdict: text.

## Behavior

- V: 662 rows, two keys id (1..22) x id2 (0..435); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 11 of 13 columns not decoded (see the row layout)
