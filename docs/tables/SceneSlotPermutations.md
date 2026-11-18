# SceneSlotPermutations

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x1406736B0`
- **Rows:** 24 rows of 16 bytes
- **Keyed by:** permutation index 0..23
- **Row layout:** [SlotPermutationRow](../structs/SlotPermutationRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The 24 permutations of the four slots 0..3, walked by a sprite effect update to pick a slot order. Verdict: engine-data.

## Behavior

- V: the row for a record is selected by 16 times a field of the record; the walk stops at a zero entry
- V: the database name DoScreenSave on the reader is a library-style label and does not describe it

## Notes

Our names. Tags: V.

## Open questions

- ?: why the sprite effect needs all orders
