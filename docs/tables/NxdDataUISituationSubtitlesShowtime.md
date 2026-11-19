# NxdDataUISituationSubtitlesShowtime

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 226
- **Rows:** 7 rows of 8 bytes
- **Keyed by:** one key: id (1..7)
- **Read by:** [EventTable226_FindRecord](../functions/EventTable226_FindRecord.md)
- **Row layout:** [NxdDataUISituationSubtitlesShowtimeRow](../structs/NxdDataUISituationSubtitlesShowtimeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Subtitle display times (7). Verdict: engine-data.

## Behavior

- V: 7 rows, one key id (1..7); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 2 of 2 columns not decoded (see the row layout)
