# NxdDataMessageWindowAnimationType

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 245
- **Rows:** 9 rows of 28 bytes
- **Keyed by:** one key: id (0..13)
- **Row layout:** [NxdDataMessageWindowAnimationTypeRow](../structs/NxdDataMessageWindowAnimationTypeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Message window animation parameters (nine types). Verdict: engine-data.

## Behavior

- V: 9 rows, one key id (0..13); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 10 of 10 columns not decoded (see the row layout)
