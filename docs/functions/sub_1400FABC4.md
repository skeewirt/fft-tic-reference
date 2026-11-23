# sub_1400FABC4

- **Address:** `0x1400FABC4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `__int64 sub_1400FABC4(char dirMask, char *geom, int *cursor, int repeatMask)`
- **Callers:** sub_1402C0DB8, sub_1402C1244, ErrandUnitPick_Input (and itself)
- **Callees:** sub_1400F52C8, sub_1400FABC4

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Two-pane grid cursor navigation (5 columns per row): moves a (pane, index) cursor with up / down / left / right and pane switch, and returns the flat index across both panes.

## Behavior

- V: cursor[0] = pane (0 or 1; > 1 returns -1), cursor[1] = index in pane. geom = { int count0, int count1, bool valid0, bool valid1, bool noEmptySkip, ... }: pane counts are used only when geom[8 + pane] != 0, else 0.
- V: dirMask bit 1 = move up a row (index - 5), bit 2 = down a row, bit 4 = left, bit 8 = right, bit 0x10 = previous (index - 1 with pane roll over), bit 0x20 = next. repeatMask < 0 or the matching bit means the key was repeat-fired (wrap allowed, flag v = 1); a non-repeat press stops at pane edges (does not wrap, returns the old pane).
- V: single-axis moves use sub_1400F52C8(index, dx, dy, 0, last, 5, wrap) = move in a 5-wide grid with row / column wrap; moving beyond the last row switches pane (the other pane is entered at the same column, clamped to its length) and empty panes are skipped (up to two tries).
- V: after the move, if the index >= count of the pane: an empty pane with a2[10] clear re-runs itself with dirMask 1 and flag byte 2 set (recursion), else clamps to count - 1.
- V: result = sum of counts of the panes before cursor[0] + cursor[1] when valid, else -1.

## Notes

Not a Job Tree function (item-list style two-pane cursor with 5-wide pages); included because it was live on the screen chunk. The 5-wide row stride is V (constant 5 passed to sub_1400F52C8).

## Open questions

? which screens call it live (callers sub_1402C0DB8 / sub_1402C1244 / ErrandUnitPick_Input not named). ? exact geom layout beyond count0 / count1 / flags at +8 / +9 / +10.
