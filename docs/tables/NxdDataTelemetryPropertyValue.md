# NxdDataTelemetryPropertyValue

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 132
- **Rows:** 37 rows of 12 bytes
- **Keyed by:** one key: id (0..36)
- **Row layout:** [NxdDataTelemetryPropertyValueRow](../structs/NxdDataTelemetryPropertyValueRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Telemetry property value lists (37). Verdict: engine-data.

## Behavior

- V: 37 rows, one key id (0..36); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
