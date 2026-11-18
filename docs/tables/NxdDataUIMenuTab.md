# NxdDataUIMenuTab

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 95
- **Rows:** 6 rows of 8 bytes
- **Keyed by:** two keys: id (1..3) x id2 (0..3)
- **Row layout:** [NxdDataUIMenuTabRow](../structs/NxdDataUIMenuTabRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Menu tabs keyed by menu and slot (6). Verdict: designer-data.

## Behavior

- V: 6 rows, two keys id (1..3) x id2 (0..3); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 2 columns not decoded (see the row layout)
