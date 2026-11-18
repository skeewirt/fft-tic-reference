# SpriteLayerByteRows

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x1406738F0`
- **Rows:** 3 rows of 24 bytes (80 to the next symbol)
- **Keyed by:** row 0..2, sprite kind 0..23
- **Row layout:** [SpriteLayerByteRow](../structs/SpriteLayerByteRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Three rows of per-kind bytes stored into the sprite object (+18 / +19). Verdict: designer-data.

## Behavior

- V: the set-up copies row b to +18 and row c (or row a, for the first branch) to +19

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: what the bytes at +18 and +19 control
