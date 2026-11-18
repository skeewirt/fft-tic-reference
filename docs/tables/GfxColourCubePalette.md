# GfxColourCubePalette

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x14078DEB0`
- **Rows:** 256 rows of 4 bytes
- **Keyed by:** palette index 0..255
- **Row layout:** [RgbaColourRow](../structs/RgbaColourRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

256-colour palette whose entries step by 8 in red, green and blue; the palette of the index image at 0x14078E2B0. Verdict: engine-data.

## Behavior

- V: the three image set-up functions store the palette and the index image addresses in the image object at +68 and +60

## Notes

Our names. Tags: V.

## Open questions

None recorded.
