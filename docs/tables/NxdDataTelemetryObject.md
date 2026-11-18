# NxdDataTelemetryObject

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 314
- **Rows:** 109 rows of 20 bytes
- **Keyed by:** one key: id (0..108)
- **Row layout:** [NxdDataTelemetryObjectRow](../structs/NxdDataTelemetryObjectRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Telemetry object list (109). Verdict: engine-data.

## Behavior

- V: 109 rows, one key id (0..108); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 3 of 5 columns not decoded (see the row layout)
