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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 3 of 4 columns not decoded (see the row layout)
