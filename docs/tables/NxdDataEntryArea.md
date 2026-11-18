# NxdDataEntryArea

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 244
- **Rows:** 2519 rows of 8 bytes
- **Keyed by:** two keys: id (256..722) x id2 (0..19)
- **Row layout:** [NxdDataEntryAreaRow](../structs/NxdDataEntryAreaRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Deployment areas: per battle and slot, a position value. Verdict: designer-data.

## Behavior

- V: 2519 rows, two keys id (256..722) x id2 (0..19); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 2 columns not decoded (see the row layout)
