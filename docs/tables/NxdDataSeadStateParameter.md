# NxdDataSeadStateParameter

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 235
- **Rows:** 41 rows of 12 bytes
- **Keyed by:** one key: id (0..40)
- **Row layout:** [NxdDataSeadStateParameterRow](../structs/NxdDataSeadStateParameterRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sound state parameters (41). Verdict: engine-data.

## Behavior

- V: 41 rows, one key id (0..40); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 3 of 3 columns not decoded (see the row layout)
