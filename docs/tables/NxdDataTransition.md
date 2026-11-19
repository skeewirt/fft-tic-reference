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

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 5 of 5 columns not decoded (see the row layout)
