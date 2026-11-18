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
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 7 of 8 columns not decoded (see the row layout)
