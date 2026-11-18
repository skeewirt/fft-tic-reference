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
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 3 of 5 columns not decoded (see the row layout); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
