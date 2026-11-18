# NxdDataCharMouseCollision

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** NXD file
- **NXD table id:** 334
- **Rows:** 36 rows of 20 bytes
- **Keyed by:** one key: id (1..36)
- **Row layout:** [NxdDataCharMouseCollisionRow](../structs/NxdDataCharMouseCollisionRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Mouse pick boxes of characters: three size floats per shape id. Verdict: engine-data.

## Behavior

- V: 36 rows, one key id (1..36); measured over every row of the stock file.
- I: column roles not marked V are inferred from names and measured ranges.

## Notes

Our names; the file format is described by the NXD format records.

## Open questions

? 3 of 5 columns not decoded (see the row layout)
