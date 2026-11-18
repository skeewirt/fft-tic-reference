# NxdDataUIKeyConfig

- **Kind:** table
- **Area:** [Input](../areas/input.md)
- **Storage:** NXD file
- **NXD table id:** 331
- **Rows:** 12 rows of 16 bytes
- **Keyed by:** one key: id (0..11)
- **Row layout:** [NxdDataUIKeyConfigRow](../structs/NxdDataUIKeyConfigRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Key configuration groups (12). Verdict: engine-data.

## Behavior

- V: 12 rows, one key id (0..11); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 3 columns not decoded (see the row layout)
