# SpriteDirection16MirrorFlags

- **Kind:** table
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Storage:** Executable
- **Address:** `0x140672D58`
- **Rows:** 16 rows of 2 bytes
- **Keyed by:** 16-step direction of the sprite relative to the camera
- **Read by:** [SpriteRecord_Fill](../functions/SpriteRecord_Fill.md)
- **Row layout:** [SpriteDirectionFlag](../structs/SpriteDirectionFlag.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Which of 16 facing directions draw a sprite mirrored. Verdict: engine-data.

## Behavior

- V: part of a block of direction tables 0x140672CF8..0x140672DA0: 4-dir flags (0x140672CF8), 16-dir flags (this), 16-dir frame index (0x140672D78), 4-dir frame index (0x140672D98)
- V: sub_14026CAA4 (event sprite pose setup): attributes |= table[dir16]; pose frame from the next table 0x140672D78
- V: SpriteRecord_Fill / SpriteRecord_SetPaletteBits read the 4-direction tables of the same block (0x140672CF8, 0x140672D7A, 0x140672D98)

## Notes

Our names. Tags: V layout, I direction meaning.

## Open questions

None recorded.
