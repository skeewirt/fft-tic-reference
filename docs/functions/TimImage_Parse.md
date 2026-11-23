# TimImage_Parse

- **Address:** `0x140340AE0`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `int TimImage_Parse(const unsigned char *afterMagic, TimImageInfo *out)`
- **Callers:** EventCmd_SetRecordOffset, sub_140344B68 (two sites), sub_140371F68, sub_14037270C, sub_140372990, sub_14037472C
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads the header of a legacy-container image (pixel mode, optional palette block, pixel block) into a small descriptor.

## Behavior

- V: the argument points past the 4-byte magic: its first dword holds the pixel mode in bits 0..2 and a palette-present flag in bit 3.
- V: with a palette: the palette block length is the next dword; its VRAM rectangle (x, y, width, height) is read from +8..+14 and its colour data pointer is +16; the pixel block starts after the palette block (rectangle at +4..+10 of that block, data pointer +12).
- V: without a palette: the pixel block rectangle is read from +8..+14 and its data pointer is +16, the palette fields are zeroed.
- V: writes mode, the pixel rectangle, the pixel data pointer, the palette rectangle and the palette data pointer into the descriptor; returns the palette height.

## Referenced by

- Called by: [BookProgress_ResetConfirmInput](BookProgress_ResetConfirmInput.md), [MenuCtl_Entry25](MenuCtl_Entry25.md), [MenuCtl_Entry27](MenuCtl_Entry27.md)

## Notes

Read in full (one small function).

## Open questions

?: whether the container is used for anything other than UI images.
