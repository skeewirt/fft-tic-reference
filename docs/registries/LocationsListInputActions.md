# LocationsListInputActions

- **Kind:** registry
- **Area:** [Input](../areas/input.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The input actions (rows of the game's input action table) that the Locations list and the old menu number entries read, with their keyboard keys from the table.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="ok"></a>26 | `ok` | `F / Enter` | V | Confirm. |
| <a id="cancel"></a>27 | `cancel` | `Backspace / Esc` | V | Back. |
| <a id="menu_up"></a>33 | `menu_up` | `W / Up arrow (mask 0x1000)` | V | Row up; number entry: add the digit step. |
| <a id="menu_down"></a>34 | `menu_down` | `S / Down arrow (mask 0x4000)` | V | Row down; number entry: subtract. |
| <a id="menu_left"></a>35 | `menu_left` | `A / Left arrow (mask 0x8000)` | V | Left: the pair sub_1400F6D58 steps by. |
| <a id="menu_right"></a>36 | `menu_right` | `D / Right arrow (mask 0x2000)` | V | Right. |
| <a id="menu_left"></a>58 | `menu_left` | `1 / Left arrow (mask 0x8000)` | V | List page up (UIListGadget_ClassicInput). |
| <a id="menu_right"></a>59 | `menu_right` | `3 / Right arrow (mask 0x2000)` | V | List page down. |
| <a id="cursor_left"></a>166 | `cursor_left` | `A / Left arrow` | V | Cursor left. |
| <a id="cursor_right"></a>167 | `cursor_right` | `D / Right arrow` | V | Cursor right. |
| <a id="worldmap_tab_left"></a>170 | `worldmap_tab_left` | `Q (pad 11 / 17 / 0)` | V | Previous tab of the Locations list. |
| <a id="worldmap_tab_right"></a>171 | `worldmap_tab_right` | `E (pad 12 / 18 / 0)` | V | Next tab. |

## Behavior

- V (data): key codes are Windows virtual keys: main key, then alternate key.
- V (seen live): on the Locations list pad RB and the keyboard E move to the next tab, pad LB and the keyboard Q to the previous one.
- V (data): the three pad layout columns hold 11 / 17 / 0 for action 170 and 12 / 18 / 0 for 171 (button 18 is the button that also switches units on the job list).
- V (data): rows 35, 58 and 166 carry pad value 11 (left) and rows 36, 59 and 167 pad value 12 (right) in all three columns, so the pad Left / Right raise all of them.

## Open questions

None recorded.
