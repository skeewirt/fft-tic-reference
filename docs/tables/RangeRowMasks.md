# RangeRowMasks

- **Kind:** table
- **Area:** [Battle](../areas/battle.md)
- **Storage:** Executable
- **Address:** `0x140693090`
- **Rows:** 8 rows of 2 bytes
- **Keyed by:** distance 0..7
- **Read by:** [RangeOverlay_BuildRowMasks](../functions/RangeOverlay_BuildRowMasks.md)
- **Row layout:** [RangeRowMasksRow](../structs/RangeRowMasksRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Bit-run masks (a triangle) used to build the diamond of the range overlay; 8 distances. Verdict: engine-data.

## Behavior

- V: reader indexes [distance]; values are symmetric runs; the 0xE0-byte object also holds a zero gap and a small pair list this reader does not use
- V: RangeOverlay_BuildRowMasks (0x140389B50): shifts the mask of each distance to the unit's column to build the 18 row words of the range overlay

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: the pair list at 0x1406930B0 and the object tail (not read by this reader)
