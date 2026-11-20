# NxdDataProfit

- **Kind:** table
- **Area:** [Errands](../areas/errands.md)
- **Storage:** NXD file
- **NXD table id:** 182
- **Rows:** 96 rows of 40 bytes, text in 7 languages
- **Keyed by:** one key: id (0..95)
- **Row layout:** [NxdDataProfitRow](../structs/NxdDataProfitRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Errand definitions (96): title, client name link and parameters. Verdict: designer-data.

## Behavior

- V: 96 rows, one key id (0..95); measured over every row of the stock file.
- V: the 53 text tables have the same columns, keys, row size and table id in all seven languages (offline decode of every file).

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

None recorded.
