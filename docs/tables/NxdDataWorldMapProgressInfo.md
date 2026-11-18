# NxdDataWorldMapProgressInfo

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 123
- **Rows:** 91 rows of 44 bytes, text in 7 languages
- **Keyed by:** two keys: id (0..1000) x id2 (0..999)
- **Row layout:** [NxdDataWorldMapProgressInfoRow](../structs/NxdDataWorldMapProgressInfoRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

World-map progress steps keyed by group and step: towns, roads, caption and condition links. Verdict: designer-data.

## Behavior

- V: 91 rows, two keys id (0..1000) x id2 (0..999); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 4 of 11 columns not decoded (see the row layout); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
