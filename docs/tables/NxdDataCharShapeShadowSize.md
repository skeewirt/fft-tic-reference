# NxdDataCharShapeShadowSize

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 176
- **Rows:** 12 rows of 12 bytes
- **Keyed by:** one key: id (0..15)
- **Read by:** [CharaRender_LookupLutParams](../functions/CharaRender_LookupLutParams.md)
- **Row layout:** [NxdDataCharShapeShadowSizeRow](../structs/NxdDataCharShapeShadowSizeRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Twelve shadow sizes (a float per row). Verdict: engine-data.

## Behavior

- V: 12 rows, one key id (0..15); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

None recorded.
