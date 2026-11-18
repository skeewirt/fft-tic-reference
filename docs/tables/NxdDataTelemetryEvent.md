# NxdDataTelemetryEvent

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 133
- **Rows:** 8 rows of 20 bytes
- **Keyed by:** one key: id (0..7)
- **Row layout:** [NxdDataTelemetryEventRow](../structs/NxdDataTelemetryEventRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Telemetry event list (8). Verdict: engine-data.

## Behavior

- V: 8 rows, one key id (0..7); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 2 of 4 columns not decoded (see the row layout)
