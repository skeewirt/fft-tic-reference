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

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 5 of 5 columns not decoded (see the row layout)
