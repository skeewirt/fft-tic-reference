# NxdDataMapRouteTable

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 98
- **Rows:** 314 rows of 12 bytes
- **Keyed by:** two keys: id (0..50) x id2 (0..10)
- **Row layout:** [NxdDataMapRouteTableRow](../structs/NxdDataMapRouteTableRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Route points between map entries keyed by route and step. Verdict: designer-data.

## Behavior

- V: 314 rows, two keys id (0..50) x id2 (0..10); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 3 of 3 columns not decoded (see the row layout)
