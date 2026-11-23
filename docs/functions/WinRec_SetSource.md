# WinRec_SetSource

- **Address:** `0x140379D34`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `__int16 __fastcall WinRec_SetSource(int rec, __int64 src, __int64 extra, int flags)`
- **Callers:** EventCmd_SetRecordOffset (its call is documented there), Tavern_HasNewEntries, MenuCtl_Entry27, sub_14037270C, sub_140372C10, MenuCtl_Entry25
- **Callees:** none

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills a window record's texture source fields from a packed source descriptor, a flags value and an extra qword.

## Behavior

- V: `rec` indexes the window record array at 0x140D4B9B0 (14 dwords, 0x38 bytes each; records are handed out in order by WorldMenu_AllocWindowRecord, which also pushes the record's address on the allocation stack at qword_140D4C0B0).
- V: clears bits 3 and 4 of the record's first dword and ORs in `flags` (the whole value, not masked), stores `extra` in dwords 8..9, sets dword 12 to 0x8080 (low word) and 0x80 (byte 2), and zeroes dword 4.
- V: dword 1 = `((y >> 4) & 0x10) | (4 * (y & 0x200)) | ((x >> 6) & 0xF)` where x is the low word of `src` and y its second word, folded with `& 0x1FF` when y is 512 or more.
- V: dword 10 low word = 2 * (x & 0x3F); dword 11 low word = 2 * the third word of `src`; dword 10 high word = byte 2 of `src`; dword 11 high word = the top word of `src`. The return value is 2 * the third word.
- I: `src` is a texture-source descriptor in 16-bit units (rests on the doubling of the x and width values, which turns 16-bit pixels into bytes).

## Notes

V: whole body read. The name is ours. The sibling `WinRec_SetRect` builds the same dword 1 word from a point it derives itself.

## Open questions

?: the callers' flag values and the meaning of the third and fourth words of `src`.
