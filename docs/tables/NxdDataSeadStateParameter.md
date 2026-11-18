# NxdDataSeadStateParameter

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 235
- **Rows:** 41 rows of 12 bytes
- **Keyed by:** one key: id (0..40)
- **Row layout:** [NxdDataSeadStateParameterRow](../structs/NxdDataSeadStateParameterRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Sound state parameters (41). Verdict: engine-data.

## Behavior

- V: 41 rows, one key id (0..40); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 3 columns not decoded (see the row layout)
