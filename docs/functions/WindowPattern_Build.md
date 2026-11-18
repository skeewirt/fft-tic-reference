# WindowPattern_Build

- **Address:** `0x140332330`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char *WindowPattern_Build(int width, int rows, const short *rect, int mode)`
- **Callers:** sub_1402212B4, sub_14022C5E0, sub_14022CBE4, sub_14022F868
- **Callees:** WindowPattern_FillRow, sub_1402202C8, VramPage_CopyRect, SceneTask_WaitFrame, sub_1402203AC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the pixel pattern of a legacy window frame row by row and, in mode 2, uploads it to VRAM.

## Behavior

- V: a width above 244 is taken as 255 pixels (a 16-bit word holds four pixels, so the row is rounded up to whole words); the buffer holds rows x width / 2 bytes (a fixed buffer in mode 2 when a display flag is 2, otherwise a scratch allocation).
- V: each row picks a template base in the window pattern table (0x1407B8260, 64 words per template): modes 0 and 1 use template 64 x row for the first 8 rows, cycle through templates 8..23 for the middle rows and use templates 24..31 for the last 8 rows; modes 2 and 3 use base 54 + 64 x row for the first 16 rows, the same cycle for the middle rows and base 1078 + 64 x (0..15) for the last 16 rows.
- V: writes the two end words of each row from the template (words 8 and 9) and fills the middle with WindowPattern_FillRow.
- V: in mode 2 it copies the buffer to the VRAM rectangle, waits one frame and releases the buffer; it returns the buffer.

## State touched

- Calls: [WindowPattern_FillRow](WindowPattern_FillRow.md), [VramPage_CopyRect](VramPage_CopyRect.md), [SceneTask_WaitFrame](SceneTask_WaitFrame.md)

## Referenced by

- Reads tables: [WindowPatternTiles](../tables/WindowPatternTiles.md)

## Notes

Read: the row template selection and the buffer handling.

## Open questions

?: which template index is which window part.
