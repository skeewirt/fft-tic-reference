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
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 6 columns not decoded (see the row layout); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
