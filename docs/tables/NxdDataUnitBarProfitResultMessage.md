# NxdDataUnitBarProfitResultMessage

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 205
- **Rows:** 240 rows of 12 bytes
- **Keyed by:** two keys: id (21..50) x id2 (0..7)
- **Row layout:** [NxdDataUnitBarProfitResultMessageRow](../structs/NxdDataUnitBarProfitResultMessageRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Errand result message voice entries keyed by errand and slot. Verdict: designer-data.

## Behavior

- V: 240 rows, two keys id (21..50) x id2 (0..7); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
