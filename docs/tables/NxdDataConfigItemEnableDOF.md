# NxdDataConfigItemEnableDOF

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 271
- **Rows:** 3 rows of 12 bytes
- **Keyed by:** one key: id (0..2)
- **Row layout:** [NxdDataConfigItemEnableDOFRow](../structs/NxdDataConfigItemEnableDOFRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Option values for the depth-of-field setting. Verdict: engine-data.

## Behavior

- V: 3 rows, one key id (0..2); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 3 of 3 columns not decoded (see the row layout)
