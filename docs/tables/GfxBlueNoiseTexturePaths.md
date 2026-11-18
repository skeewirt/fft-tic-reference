# GfxBlueNoiseTexturePaths

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x1406C5E60`
- **Rows:** 16 rows of 8 bytes
- **Keyed by:** texture 0..15
- **Read by:** [FrequentUtilRenderer_CreateResources](../functions/FrequentUtilRenderer_CreateResources.md)
- **Row layout:** [TextPointerRow](../structs/TextPointerRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

File paths of the sixteen 64 by 64 blue noise textures the renderer loads at set-up. Verdict: pointer-table.

## Behavior

- V: the sixteen strings are not addressed by anything but this list
- V: FrequentUtilRenderer_CreateResources walks the list and creates one texture per path

## Notes

Our names. Tags: V.

## Open questions

None recorded.
