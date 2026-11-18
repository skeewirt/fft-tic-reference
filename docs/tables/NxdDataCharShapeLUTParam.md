# NxdDataCharShapeLUTParam

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 217
- **Rows:** 24 rows of 20 bytes
- **Keyed by:** one key: id (1..36)
- **Read by:** [CharaRender_LookupLutParams](../functions/CharaRender_LookupLutParams.md)
- **Row layout:** [NxdDataCharShapeLUTParamRow](../structs/NxdDataCharShapeLUTParamRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Shape palette parameters: two floats and two shorts per row. Verdict: engine-data.

## Behavior

- V: 24 rows, one key id (1..36); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 4 of 6 columns not decoded (see the row layout)
