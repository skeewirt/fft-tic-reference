# EquipScreenPalette

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable (initialised data)
- **Address:** `0x1407B4E60`
- **Rows:** 256 rows of 2 bytes
- **Keyed by:** palette entry 0..255 (four rows of 64)
- **Read by:** [EquipScreen_InitVram](../functions/EquipScreen_InitVram.md)
- **Row layout:** [PaletteColour](../structs/PaletteColour.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

UI palette block (four rows of 64 colours) the equipment screen uploads to the CLUT area of VRAM. Verdict: designer-data.

## Behavior

- V: EquipScreen_InitVram (0x14033DE68): uploads 64 x 4 words to VRAM rectangle (256, 250)
- V: the upload rectangle is 64 wide and 4 high (the call sets y = 250, h = 4); the first 62 bytes equal the first bytes of the twin palette at 0x1408F9370, the rest differs

## Notes

Our names. Tags: V rectangle, I that all 512 bytes belong to this table.

## Open questions

- ?: which colours the two palettes differ in
