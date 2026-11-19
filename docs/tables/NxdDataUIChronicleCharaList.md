# NxdDataUIChronicleCharaList

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 283
- **Rows:** 168 rows of 24 bytes
- **Keyed by:** two keys: id (0..30) x id2 (0..9)
- **Row layout:** [NxdDataUIChronicleCharaListRow](../structs/NxdDataUIChronicleCharaListRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Chronicle character lists keyed by period and slot. Verdict: designer-data.

## Behavior

- V: 168 rows, two keys id (0..30) x id2 (0..9); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 6 of 6 columns not decoded (see the row layout)
