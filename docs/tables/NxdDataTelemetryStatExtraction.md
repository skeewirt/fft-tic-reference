# NxdDataTelemetryStatExtraction

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 318
- **Rows:** 50 rows of 28 bytes
- **Keyed by:** one key: id (0..49)
- **Row layout:** [NxdDataTelemetryStatExtractionRow](../structs/NxdDataTelemetryStatExtractionRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Telemetry statistic extraction rules (50). Verdict: engine-data.

## Behavior

- V: 50 rows, one key id (0..49); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 6 of 7 columns not decoded (see the row layout)
