# NxdDataUIButtonGuideRow

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)
- **Size:** 40 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_button_guide table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: designer-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="guide_icon"></a>`0x4` | guide_icon | `int32` | V | Read in the code: A fixed guide icon number (1..21) shown instead of an action's button; it is drawn by sub_1400F681C (sticks, d-pad and other fixed glyphs). Observed in the stock rows: 0 to 20, 4 distinct values. |
| <a id="ui_key_assign"></a>`0x8` | ui_key_assign | `int32` | V | Read in the code: The action (a UIKeyAssign row, table 25) whose bound button the guide shows; also the action some screens test with Input_IsActionHeld. Observed in the stock rows: 0 to 252, 82 distinct values. |
| <a id="title_text"></a>`0xC` | title_text | `int32` | V | Read in the code: The line of the UI text table shown as the guide entry's label; a row with 0 here is skipped by the guide bars. Observed in the stock rows: 0 to 4043, 188 distinct values. |
| <a id="guide_icon_2"></a>`0x10` | guide_icon_2 | `int32` | V | Read in the code: The fixed guide icon of a second button (a two-button entry), like icon. Observed in the stock rows: 0 in every row. |
| <a id="ui_key_assign_2"></a>`0x14` | ui_key_assign_2 | `int32` | V | Read in the code: The action (UIKeyAssign row) of the second button of a two-button entry. Observed in the stock rows: 0 to 248, 5 distinct values. |
| <a id="unknown18"></a>`0x18` | unknown18 | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="key_texture"></a>`0x1C` | key_texture | `int32` | V | Read in the code: In keyboard mode, a keyboard key texture number (ui/platform/win/textureparts/key_NNN) shown instead of icon. Observed in the stock rows: 0 to 155, 2 distinct values. |
| <a id="key_texture_2"></a>`0x20` | key_texture_2 | `int32` | V | Read in the code: In keyboard mode, the keyboard key texture of the second button, replacing icon_2 (only when keyboard_icon is set). Observed in the stock rows: 0 in every row. |
| <a id="unknown24"></a>`0x24` | unknown24 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="right_aligned"></a>`0x25` | right_aligned | `uint8` | V | Read in the code: Places the entry in the right-aligned group of the guide bar (laid out from the right edge) instead of the left group. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="unknown26"></a>`0x26` | unknown26 | `uint8` | ? | Not decoded. Observed in the stock rows: 0 in every row. |
| <a id="unknown27"></a>`0x27` | unknown27 | `uint8` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 in every row. |

## Referenced by

- Described by tables: [NxdDataUIButtonGuide](../tables/NxdDataUIButtonGuide.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 2 of 13 columns not decoded.
