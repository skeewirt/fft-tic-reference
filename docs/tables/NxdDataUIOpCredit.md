# NxdDataUIOpCredit

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 316
- **Rows:** 130 rows of 32 bytes
- **Keyed by:** two keys: id (0..1200) x id2 (0..7)
- **Row layout:** [NxdDataUIOpCreditRow](../structs/NxdDataUIOpCreditRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Opening credit rows keyed by credit and part. Verdict: designer-data.

## Behavior

- V: 130 rows, two keys id (0..1200) x id2 (0..7); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 7 of 8 columns not decoded (see the row layout)
