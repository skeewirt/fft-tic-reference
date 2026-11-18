# ItemScreenPalette

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x14080E7F0`
- **Rows:** 256 rows of 2 bytes
- **Keyed by:** colour 0..255
- **Read by:** [sub_1402B2AAC](../functions/sub_1402B2AAC.md), [VramPage_CopyRect](../functions/VramPage_CopyRect.md)
- **Row layout:** [ItemScreenPaletteRow](../structs/ItemScreenPaletteRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

256 colours (15-bit) uploaded to the video page row used by the legacy item and map title textures. Verdict: designer-data.

## Behavior

- V: sub_1402B2AAC passes the rectangle (x 0, y 509, 256 wide, 1 high) and this address to VramPage_CopyRect

## Notes

Our names. Tags: V.

## Open questions

None recorded.
