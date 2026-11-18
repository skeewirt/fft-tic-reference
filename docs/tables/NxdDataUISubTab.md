# NxdDataUISubTab

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 61
- **Rows:** 59 rows of 16 bytes
- **Keyed by:** two keys: id (0..29) x id2 (0..6)
- **Row layout:** [NxdDataUISubTabRow](../structs/NxdDataUISubTabRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sub tabs keyed by tab group and slot (59). Verdict: designer-data.

## Behavior

- V: 59 rows, two keys id (0..29) x id2 (0..6); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 3 of 4 columns not decoded (see the row layout)
