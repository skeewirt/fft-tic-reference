# NxdDataMapVariationEvent

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** NXD file
- **NXD table id:** 207
- **Rows:** 14 rows of 20 bytes
- **Keyed by:** one key: id (0..13)
- **Row layout:** [NxdDataMapVariationEventRow](../structs/NxdDataMapVariationEventRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Map variations tied to events (14). Verdict: designer-data.

## Behavior

- V: 14 rows, one key id (0..13); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 4 columns not decoded (see the row layout)
