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

## Notes

Column names are our own: a column is named only where its role was read in the code or measured over every stock row; the others are numbered by their offset. The file format is described by the NXD format records.

## Open questions

? 7 of 7 columns not decoded (see the row layout)
