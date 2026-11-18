# SpriteEffectKindFlags

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x140702BE8`
- **Rows:** 32 rows of 1 byte
- **Keyed by:** kind 0..31
- **Row layout:** [SpriteKindFlagRow](../structs/SpriteKindFlagRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One flag byte per sprite record kind read by the effect placement code. Verdict: engine-data.

## Behavior

- V: the byte at index (record word +4) & 0x1F is compared with zero when the placement decides to copy the three position floats

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: what kinds 4, 5, 20..28 are
