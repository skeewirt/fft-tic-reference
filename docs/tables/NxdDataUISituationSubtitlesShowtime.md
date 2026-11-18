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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 2 columns not decoded (see the row layout)
