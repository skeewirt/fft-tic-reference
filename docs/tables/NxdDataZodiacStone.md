# NxdDataZodiacStone

- **Kind:** table
- **Area:** [Items and shops](../areas/items.md)
- **Storage:** NXD file
- **NXD table id:** 119
- **Rows:** 27 rows of 40 bytes, text in 7 languages
- **Keyed by:** two keys: id (0..12) x id2 (0..3)
- **Row layout:** [NxdDataZodiacStoneRow](../structs/NxdDataZodiacStoneRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Zodiac stones keyed by stone and variant: condition link, owner timeline, name, summary, description and icons. Verdict: designer-data.

## Behavior

- V: 27 rows, two keys id (0..12) x id2 (0..3); measured over every row of the stock file.
- I: the table role and the column roles are inferred from the table and column names and the measured value ranges; not traced to a reader, except where a column line says V.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 4 of 10 columns not decoded (see the row layout)
