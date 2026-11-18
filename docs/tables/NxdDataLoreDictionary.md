# NxdDataLoreDictionary

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 237
- **Rows:** 241 rows of 84 bytes, text in 7 languages
- **Keyed by:** two keys: id (1..19200) x id2 (0..150)
- **Row layout:** [NxdDataLoreDictionaryRow](../structs/NxdDataLoreDictionaryRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Lore dictionary entries keyed by entry and part: names, descriptions, sort orders, icons and links. Verdict: designer-data.

## Behavior

- V: 241 rows, two keys id (1..19200) x id2 (0..150); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 10 of 24 columns not decoded (see the row layout); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
