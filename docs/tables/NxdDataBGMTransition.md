# NxdDataBGMTransition

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 306
- **Rows:** 14 rows of 20 bytes
- **Keyed by:** one key: id (0..13)
- **Row layout:** [NxdDataBGMTransitionRow](../structs/NxdDataBGMTransitionRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Music transition parameters: a sound resource reference and two fade-like float values per row. Verdict: engine-data.

## Behavior

- V: 14 rows, one key id (0..13); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 5 columns not decoded (see the row layout)
