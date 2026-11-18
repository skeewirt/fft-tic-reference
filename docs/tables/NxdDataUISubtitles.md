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
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 9 of 13 columns not decoded (see the row layout); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
