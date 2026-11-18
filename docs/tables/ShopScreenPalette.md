# ShopScreenPalette

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x140811350`
- **Rows:** 16 rows of 2 bytes (first block)
- **Keyed by:** colour 0..15
- **Read by:** [VramPage_CopyRect](../functions/VramPage_CopyRect.md)
- **Row layout:** [ShopScreenPaletteRow](../structs/ShopScreenPaletteRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

16 colours (15-bit) copied into the video page by the shop screen set-up. Verdict: designer-data.

## Behavior

- V: sub_1402BB0A0 copies a 4 by 4 rectangle at (576, 506) from this address

## Notes

Our names. Tags: V used block, ? what follows.

## Open questions

- ?: the blocks that follow the first 32 bytes
