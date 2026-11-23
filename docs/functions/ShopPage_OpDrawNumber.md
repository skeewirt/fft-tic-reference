# ShopPage_OpDrawNumber

- **Address:** `0x140328D54`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `unsigned __int8 *__fastcall ShopPage_OpDrawNumber(unsigned __int8 *record)`
- **Callers:** Table entry only (0x140683938 index 14)
- **Callees:** sub_14032A204, sub_14031DBE4, sub_14031DA24

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opcode 14 of the 20-entry page-script table at 0x140683938: draws a right-aligned number with blank padding and returns the next record.

## Behavior

- V: sets the colour word `dword_140906A58` from the language code (different constants for 0, for 1 or no info, and for the rest).
- V: the value is byte +9, passed through the callback `g_ShopRowCallbacks[record[3]]` when present; it is formatted with %d.
- V: record[4] is the field width: leading blanks (`sub_14031DBE4`) fill the width, then each digit is drawn with `sub_14031DA24` using the glyph offset 8*character-216 where the character is the formatted ASCII digit (48..57); x starts at record[7] and advances 8 per cell, y is record[8] (+4 and +1 for the two kinds).
- V: returns `record + record[1]`.
- I: it is the counterpart of ClassicUi_OpDrawNumber in a separate, older page interpreter (rests on the table entries around it).

## Notes

Whole body read.

## Open questions

Which interpreter walks the table.
