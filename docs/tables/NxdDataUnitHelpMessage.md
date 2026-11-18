# NxdDataUnitHelpMessage

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 194
- **Rows:** 572 rows of 44 bytes
- **Keyed by:** two keys: id (1..99) x id2 (1..20)
- **Row layout:** [NxdDataUnitHelpMessageRow](../structs/NxdDataUnitHelpMessageRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Unit help message voice entries keyed by unit and line. Verdict: designer-data.

## Behavior

- V: 572 rows, two keys id (1..99) x id2 (1..20); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 11 columns not decoded (see the row layout)
