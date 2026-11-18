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
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 7 columns not decoded (see the row layout); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
