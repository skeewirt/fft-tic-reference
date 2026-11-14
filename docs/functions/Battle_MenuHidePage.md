# Battle_MenuHidePage

- **Address:** `0x140154308`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `int *sub_140154308(UIAddonFFTOBattleCommand *addon, int menuId, int frame)`
- **Callers:** `BUi_BattleMenuWindowsSetPage` (state -1)
- **Callees:** `sub_1401542AC`, `GUIComponent_StopAllStates`, `GUINode_PlayStateAtFrame`, `sub_140155E04`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Hides the page for a menu id (or all six pages when `menuId == -1`).

## Behavior

- V: `menuId == -1`: for each of the six `BattleMenu01..06` nodes, stops all states, plays `Uncheck` on each `RadioButton01..06` at frame -1, then plays `Hide` at `frame`.
- V: otherwise resolves the page with `sub_1401542AC(addon, menuId)`, stops its states, and if the addon is shown (`sub_1400F5828(addon+48, 12, 0, 0)`) calls `sub_140155E04(addon, menuId, -1)`; plays `Hide` at `frame`.
- V: clears `addon+856`, `+1120 = -1` (`0x1401545DD`), `+1124 = -1` (`0x1401545E4`), word `+1128 = 0`, byte `+1130 = 0`, `+1136 = -1` and `+5624 = -1`. The `+1120..+1136` block is the embedded `UIGadgetFFTORadioButtonMenu` at `+840` (its +16 count, +280 selected, +284 hover, +288 flags, +296 page id).

## State touched

- Calls: [GUIComponent_StopAllStates](GUIComponent_StopAllStates.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md)

## Notes

The unconditional `+5624 = -1` is why the page field is the reliable "no page" signal.

## Open questions

? the fields at +856..+1136 (some other menu's state).
