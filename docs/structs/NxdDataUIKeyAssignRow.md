# NxdDataUIKeyAssignRow

- **Kind:** structure
- **Area:** [Input](../areas/input.md)
- **Size:** 48 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the nxd.ui_key_assign table (data table). The key is not stored in the row: it is in the file's entry index. Verdict: engine-data.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="unknown00"></a>`0x0` | unknown00 | `int32` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="pad_layout_0"></a>`0x4` | pad_layout_0 | `int32` | V | Read in the code: The pad button of the action (a UIPadDefine row id) in pad layout 0; sub_1400F1A84 copies the column of the current layout into the action's pad binding. Observed in the stock rows: 0 to 24, 25 distinct values. |
| <a id="pad_layout_1"></a>`0x8` | pad_layout_1 | `int32` | V | Read in the code: The pad button of the action (a UIPadDefine row id) in pad layout 1; sub_1400F1A84 copies the column of the current layout into the action's pad binding. Observed in the stock rows: 0 to 60, 28 distinct values. |
| <a id="pad_layout_2"></a>`0xC` | pad_layout_2 | `int32` | V | Read in the code: The pad button of the action (a UIPadDefine row id) in pad layout 2; sub_1400F1A84 copies the column of the current layout into the action's pad binding. Observed in the stock rows: 0 to 24, 20 distinct values. |
| <a id="key"></a>`0x10` | key | `int32` | M | Measured over every stock row: The keyboard key of the action (Windows key number). Observed in the stock rows: 0 to 161, 35 distinct values. |
| <a id="key_2"></a>`0x14` | key_2 | `int32` | V | Read in the code: The second keyboard key of the action. Observed in the stock rows: 0 to 164, 10 distinct values. |
| <a id="name"></a>`0x18` | name | `string (int32 offset)` | V | Read in the code: The action's name: a text tag <keyicon=NAME> finds the action whose +0x18 equals NAME and inserts that action's button glyph. Observed in the stock rows: 86 distinct values, 168 empty. |
| <a id="unknown1c"></a>`0x1C` | unknown1c | `string (int32 offset)` | V | Read in the code: No code of the game reads this column. Observed in the stock rows: empty in every row. |
| <a id="pad_long_press_0"></a>`0x20` | pad_long_press_0 | `uint8` | V | Read in the code: Long press for the pad button of layout 0: the binding gets bit 0x10000, so pressed / held are reported only after 1000 ms down. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="pad_long_press_1"></a>`0x21` | pad_long_press_1 | `uint8` | V | Read in the code: Long press for the pad button of layout 1: the binding gets bit 0x10000, so pressed / held are reported only after 1000 ms down. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="pad_long_press_2"></a>`0x22` | pad_long_press_2 | `uint8` | V | Read in the code: Long press for the pad button of layout 2: the binding gets bit 0x10000, so pressed / held are reported only after 1000 ms down. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="key_shift"></a>`0x23` | key_shift | `uint8` | V | Read in the code: When set, keyboard key 1 of the action (key) counts only while Shift (key 16) is held. Observed in the stock rows: 0 in every row. |
| <a id="key_ctrl"></a>`0x24` | key_ctrl | `uint8` | V | Read in the code: When set, keyboard key 1 of the action (key) counts only while Ctrl (key 17) is held. Observed in the stock rows: 0 in every row. |
| <a id="key_alt"></a>`0x25` | key_alt | `uint8` | V | Read in the code: When set, keyboard key 1 of the action (key) counts only while Alt (key 18) is held. Observed in the stock rows: 0 in every row. |
| <a id="key_long_press"></a>`0x26` | key_long_press | `uint8` | V | Read in the code: When set, the action's first keyboard key (+0x10) counts only as a long press: it reports held and pressed only after the key has been down for 1000 ms. Observed in the stock rows: 0 to 1, 2 distinct values. |
| <a id="key_2_shift"></a>`0x27` | key_2_shift | `uint8` | V | Read in the code: When set, keyboard key 2 of the action (key_2) counts only while Shift (key 16) is held. Observed in the stock rows: 0 in every row. |
| <a id="key_2_ctrl"></a>`0x28` | key_2_ctrl | `uint8` | V | Read in the code: When set, keyboard key 2 of the action (key_2) counts only while Ctrl (key 17) is held. Observed in the stock rows: 0 in every row. |
| <a id="key_2_alt"></a>`0x29` | key_2_alt | `uint8` | V | Read in the code: When set, keyboard key 2 of the action (key_2) counts only while Alt (key 18) is held. Observed in the stock rows: 0 in every row. |
| <a id="context_2"></a>`0x2A` | context_2 | `uint8` | V | Read in the code: Puts the action into input context 2 instead of the default context 1; context 2 is not in the input module's active mask (0x15), so a row with only this flag is never live. Observed in the stock rows: 0 in every row. |
| <a id="context_4"></a>`0x2B` | context_4 | `uint8` | V | Read in the code: Puts the action into input context 4 (active in the stock mask 0x15), alone or with context_2. Observed in the stock rows: 0 in every row. |
| <a id="key_2_long_press"></a>`0x2C` | key_2_long_press | `uint8` | V | Read in the code: As key_long_press, for the second keyboard key (+0x14): bit 0x80000 on key binding 2, reported only after 1000 ms down. Observed in the stock rows: 0 in every row. |
| <a id="unknown2d"></a>`0x2D` | unknown2d | `uint8` | ? | Not decoded. Observed in the stock rows: 0 to 1, 2 distinct values. |

## Referenced by

- Described by tables: [NxdDataUIKeyAssign](../tables/NxdDataUIKeyAssign.md)

## Notes

Offsets are bytes from the row start; strings are stored as offsets into the file string pool, arrays as an offset and a count. Our names; roles of columns not traced to a reader are inferred (I) or open (?).

## Open questions

? 1 of 22 columns not decoded.
