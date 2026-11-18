# NxdDataUnitWarnMessage

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 190
- **Rows:** 59 rows of 12 bytes
- **Keyed by:** two keys: id (3..99) x id2 (0..0)
- **Row layout:** [NxdDataUnitWarnMessageRow](../structs/NxdDataUnitWarnMessageRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Unit warning message voice entries. Verdict: designer-data.

## Behavior

- V: 59 rows, two keys id (3..99) x id2 (0..0); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
