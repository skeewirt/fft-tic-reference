# WinRec_PageToVramPoint

- **Address:** `0x140379B8C`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void __fastcall WinRec_PageToVramPoint(unsigned int page, RECT16 rect, int *outPoint)`
- **Callers:** WinRec_SetRect, WinRec_CopyToVram; also a data reference at 0x143D3F274
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Maps a window texture page number and a rectangle to the point in the video page where the window's pixels live.

## Behavior

- V: page 0 or 1: x = rect.x / 4 + (page + 6) * 64 and y = rect.y.
- V: page 2: x = rect.x / 4 + 576 and y = rect.y + 256.
- V: any other page: the output is left untouched and the function returns.

## Referenced by

- Called by: [WinRec_CopyToVram](WinRec_CopyToVram.md), [WinRec_SetRect](WinRec_SetRect.md)

## Notes

V: whole body read (92 bytes). The name is ours. The rectangle argument is a packed 64-bit value of which only x and y are used.

## Open questions

?: why only pages 0..2 exist.
