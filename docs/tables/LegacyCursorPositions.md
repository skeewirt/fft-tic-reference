# LegacyCursorPositions

- **Kind:** table
- **Area:** [UI framework](../areas/ui-framework.md)
- **Storage:** Executable
- **Address:** `0x14071F1E0`
- **Rows:** 31 rows of 2 bytes
- **Keyed by:** slot 0..30, (x, y) bytes
- **Row layout:** [CursorPosition](../structs/CursorPosition.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Cursor (x, y) positions of the legacy item pages (from +0x10) and a 5-byte group list at +0; the tail of the 0x90-byte object holds three save file name strings. Verdict: designer-data.

## Behavior

- V: x values 0x50, 0x5C, 0x68 ... step 12 and y 0x80 / 0x8C / 0xA4 form a grid
- V: sub_140393250: loads (x, y) from table[index * 2] at +0x10 for the legacy item page cursor
- V: sub_140394C14: reads the 5-byte list at +0 (0x11, 0x22, 0x31, 0x41, 0x4F) to pick a cell group

## Notes

Our names. Tags: V layout, I meaning.

## Open questions

- ?: the save file name strings at the end
