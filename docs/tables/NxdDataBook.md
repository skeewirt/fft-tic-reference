# NxdDataBook

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** NXD file
- **NXD table id:** 148
- **Rows:** 5 rows of 44 bytes, text in 7 languages
- **Keyed by:** one key: id (0..4)
- **Row layout:** [NxdDataBookRow](../structs/NxdDataBookRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The five lore books: titles, descriptions, icon and sound references. Verdict: designer-data.

## Behavior

- V: 5 rows, one key id (0..4); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 4 of 11 columns not decoded (see the row layout); I: the other six languages share this layout (V by the offline decode in the title records); only the English file was extracted here
