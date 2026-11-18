# NxdDataUnitCommunMessage

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 192
- **Rows:** 72 rows of 12 bytes
- **Keyed by:** two keys: id (1..99) x id2 (0..2)
- **Row layout:** [NxdDataUnitCommunMessageRow](../structs/NxdDataUnitCommunMessageRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Unit common message voice entries keyed by unit and slot. Verdict: designer-data.

## Behavior

- V: 72 rows, two keys id (1..99) x id2 (0..2); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 3 columns not decoded (see the row layout)
