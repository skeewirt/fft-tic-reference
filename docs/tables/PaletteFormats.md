# PaletteFormats

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x140672C38`
- **Rows:** 2 rows of 16 bytes
- **Keyed by:** palette kind 0 = 16 colours, 1 = 256 colours
- **Read by:** [Palette_ConvertToRgba](../functions/Palette_ConvertToRgba.md)
- **Row layout:** [PaletteFormat](../structs/PaletteFormat.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Two palette format descriptors (16- and 256-colour palettes). Verdict: engine-data.

## Behavior

- V: index is a kind 0/1 (a1 x 16 bytes); strings follow after two records
- V: sub_14025EB10: converts that many 15-bit palette words to 32-bit colours (0x8000 = opaque black, 0 = clear, top bit selects the semi-transparency alpha)
- V: sub_14025E900: passes +4 to the texture upload

## Notes

Our names. Tags: V layout.

## Open questions

- ?: fields +8, +12
