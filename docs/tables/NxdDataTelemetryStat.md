# NxdDataTelemetryStat

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 134
- **Rows:** 52 rows of 32 bytes
- **Keyed by:** one key: id (0..1049)
- **Row layout:** [NxdDataTelemetryStatRow](../structs/NxdDataTelemetryStatRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Telemetry statistics (52). Verdict: engine-data.

## Behavior

- V: 52 rows, one key id (0..1049); measured over every row of the stock file.

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 8 of 8 columns not decoded (see the row layout)
