# NxdDataUnitVoice

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 204
- **Rows:** 10 rows of 28 bytes
- **Keyed by:** one key: id (0..9)
- **Row layout:** [NxdDataUnitVoiceRow](../structs/NxdDataUnitVoiceRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Unit voice type definitions (10). Verdict: designer-data.

## Behavior

- V: 10 rows, one key id (0..9); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 7 of 7 columns not decoded (see the row layout)
