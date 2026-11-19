# NxdDataUIFilePathExchange

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 125
- **Rows:** 5 rows of 12 bytes
- **Keyed by:** two keys: id (0..2001) x id2 (0..1)
- **Row layout:** [NxdDataUIFilePathExchangeRow](../structs/NxdDataUIFilePathExchangeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

UI file replacement mapping (5). Verdict: engine-data.

## Behavior

- V: 5 rows, two keys id (0..2001) x id2 (0..1); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 2 columns not decoded (see the row layout)
