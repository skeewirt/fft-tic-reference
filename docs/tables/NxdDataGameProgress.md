# NxdDataGameProgress

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 92
- **Rows:** 307 rows of 20 bytes
- **Keyed by:** two keys: id (0..11) x id2 (0..2040)
- **Row layout:** [NxdDataGameProgressRow](../structs/NxdDataGameProgressRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Story progress steps keyed by progress group and value, linked to world-map progress info rows. Verdict: designer-data.

## Behavior

- V: 307 rows, two keys id (0..11) x id2 (0..2040); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 1 of 5 columns not decoded (see the row layout)
