# NxdDataUIModal

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** NXD file
- **NXD table id:** 333
- **Rows:** 27 rows of 24 bytes
- **Keyed by:** one key: id (1..27)
- **Row layout:** [NxdDataUIModalRow](../structs/NxdDataUIModalRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Modal window definitions (27). Verdict: designer-data.

## Behavior

- V: 27 rows, one key id (1..27); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 5 of 5 columns not decoded (see the row layout)
