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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 3 columns not decoded (see the row layout)
