# NxdDataTransition

- **Kind:** table
- **Area:** [Display](../areas/display.md)
- **Storage:** NXD file
- **NXD table id:** 100
- **Rows:** 26 rows of 20 bytes
- **Keyed by:** one key: id (1..26)
- **Row layout:** [NxdDataTransitionRow](../structs/NxdDataTransitionRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Screen transition parameters (26). Verdict: engine-data.

## Behavior

- V: 26 rows, one key id (1..26); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 4 of 5 columns not decoded (see the row layout)
