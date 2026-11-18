# NxdDataSystemBonusItemContents

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 296
- **Rows:** 12 rows of 12 bytes
- **Keyed by:** two keys: id (1..2) x id2 (0..6)
- **Row layout:** [NxdDataSystemBonusItemContentsRow](../structs/NxdDataSystemBonusItemContentsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Bonus item contents, keyed by bonus and slot, typed references. Verdict: designer-data.

## Behavior

- V: 12 rows, two keys id (1..2) x id2 (0..6); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
