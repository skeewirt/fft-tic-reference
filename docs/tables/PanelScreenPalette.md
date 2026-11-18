# PanelScreenPalette

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1408F9370`
- **Rows:** 256 rows of 2 bytes
- **Keyed by:** palette entry 0..255 (four rows of 64)
- **Read by:** [PanelScreen_InitVram](../functions/PanelScreen_InitVram.md)
- **Row layout:** [PaletteColour](../structs/PaletteColour.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

UI palette block of the second panel screen; the first 62 bytes equal exe.ui.equip_screen_palette. Verdict: designer-data.

## Behavior

- V: PanelScreen_InitVram (0x14033D88C): uploads 64 x 4 words to VRAM rectangle (256, 250)
- V: the upload rectangle is 64 x 4; compare of the first bytes shows 0x3E equal then different

## Notes

Our names. Tags: V rectangle.

## Open questions

- ?: which colours differ from the other palette
