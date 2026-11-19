# NxdDataProfitClientName

- **Kind:** table
- **Area:** [Errands](../areas/errands.md)
- **Storage:** NXD file
- **NXD table id:** 193
- **Rows:** 85 rows of 8 bytes, text in 7 languages
- **Keyed by:** one key: id (1..85)
- **Row layout:** [NxdDataProfitClientNameRow](../structs/NxdDataProfitClientNameRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Errand client names (85). Verdict: text.

## Behavior

- V: 85 rows, one key id (1..85); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 1 of 2 columns not decoded (see the row layout)
