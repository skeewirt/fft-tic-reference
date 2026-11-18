# NxdDataJingle

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 319
- **Rows:** 11 rows of 12 bytes
- **Keyed by:** one key: id (0..10)
- **Row layout:** [NxdDataJingleRow](../structs/NxdDataJingleRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Eleven jingles pointing at sound resources. Verdict: engine-data.

## Behavior

- V: 11 rows, one key id (0..10); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
