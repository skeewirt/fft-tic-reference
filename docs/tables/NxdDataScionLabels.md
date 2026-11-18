# NxdDataScionLabels

- **Kind:** table
- **Area:** [Data access](../areas/data.md)
- **Storage:** NXD file
- **NXD table id:** 170
- **Rows:** 3323 rows of 12 bytes
- **Keyed by:** one key: id (302152..357594)
- **Row layout:** [NxdDataScionLabelsRow](../structs/NxdDataScionLabelsRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Voice line labels (3323): archive file link and packed entry id. Verdict: engine-data.

## Behavior

- V: 3323 rows, one key id (302152..357594); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
