# NxdDataUIMenuSortList

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 43
- **Rows:** 33 rows of 16 bytes
- **Keyed by:** two keys: id (1..9) x id2 (0..4)
- **Row layout:** [NxdDataUIMenuSortListRow](../structs/NxdDataUIMenuSortListRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Menu sort option lists keyed by menu and slot. Verdict: designer-data.

## Behavior

- V: 33 rows, two keys id (1..9) x id2 (0..4); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 4 of 4 columns not decoded (see the row layout)
