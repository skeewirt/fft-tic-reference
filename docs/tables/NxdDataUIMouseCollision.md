# NxdDataUIMouseCollision

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 329
- **Rows:** 21 rows of 12 bytes
- **Keyed by:** one key: id (1..21)
- **Row layout:** [NxdDataUIMouseCollisionRow](../structs/NxdDataUIMouseCollisionRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

UI mouse pick boxes (21). Verdict: engine-data.

## Behavior

- V: 21 rows, one key id (1..21); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 3 of 3 columns not decoded (see the row layout)
