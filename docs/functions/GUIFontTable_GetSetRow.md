# GUIFontTable_GetSetRow

- **Address:** `0x1403D9908`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 GUIFontTable_GetSetRow(_QWORD *table, unsigned int key)`
- **Callers:** GUITextNode_Layout, GUITextNode_Draw
- **Callees:** UIFontSetRow_Default, sub_1403EEECC

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns a pointer to the 80-byte UIFontSet row for a font-set key; out of range falls back to row 0, creating a default row if the table is empty.

## Behavior

- V: count = (table[3] - table[2]) / 80; if key < count the result is table[2] + 80*key.
- V: otherwise, if the vector is empty (table[2] == table[3]) it builds a UIFontSetRow_Default on the stack and appends it (same grow-or-copy 80-byte append as Load, via sub_1403EEECC when end == table[4]).
- V: out-of-range returns table[2], i.e. row 0.
- V: callers GUITextNode_Layout (0x1403DD0C3) and GUITextNode_Draw (0x1403EA229): the key is the text node's font set field (+300 per the Copy sheet; I).

## State touched

- Calls: [UIFontSetRow_Default](UIFontSetRow_Default.md)

## Referenced by

- Called by: [GUITextNode_Draw](GUITextNode_Draw.md), [GUITextNode_Layout](GUITextNode_Layout.md)

## Notes

Draw and Layout both read per-set parameters (threshold, widths, colours; see UIFontSetRow_Default) from the returned row.

## Open questions

? which row fields Layout vs Draw consume (not read here).
