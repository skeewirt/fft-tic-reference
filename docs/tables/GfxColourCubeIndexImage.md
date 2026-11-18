# GfxColourCubeIndexImage

- **Kind:** table
- **Area:** [Graphics](../areas/graphics.md)
- **Storage:** Executable
- **Address:** `0x14078E2B0`
- **Rows:** 1024 bytes (size inferred)
- **Keyed by:** pixel
- **Row layout:** [PaletteIndexByteRow](../structs/PaletteIndexByteRow.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

8-bit index image drawn with the colour cube palette (size word 32 stored by the set-up). Verdict: engine-data.

## Behavior

- V: the image object points to this image and to the colour cube palette

## Notes

Our names. Tags: V link, I size.

## Open questions

- ?: exact size
- ?: what the image is used for
