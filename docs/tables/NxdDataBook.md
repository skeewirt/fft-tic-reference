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
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 3 of 11 columns not decoded (see the row layout)
