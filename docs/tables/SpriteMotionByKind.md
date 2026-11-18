# SpriteMotionByKind

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x140673830`
- **Rows:** 2 rows of 16 bytes
- **Keyed by:** row A or B, kind class 0..15
- **Row layout:** [SpriteMotionByKindRow](../structs/SpriteMotionByKindRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Motion number per sprite kind class, in two variants chosen by a flag test. Verdict: designer-data.

## Behavior

- V: the class comes from the first byte of a 4-byte record of the sprite kind table at 0x140673300
- V: the number is passed on to the sprite motion starter

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: what each motion number animates
