# NxdDataLoreNameAlias

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 240
- **Rows:** 52 rows of 12 bytes, text in 7 languages
- **Keyed by:** one key: id (1..52)
- **Row layout:** [NxdDataLoreNameAliasRow](../structs/NxdDataLoreNameAliasRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Lore name aliases (52). Verdict: text.

## Behavior

- V: 52 rows, one key id (1..52); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
