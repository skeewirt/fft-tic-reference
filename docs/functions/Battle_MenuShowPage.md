# Battle_MenuShowPage

- **Address:** `0x140154624`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `__int64 sub_140154624(UIAddonFFTOBattleCommand *addon, int pageId)`
- **Callers:** `BUi_BattleMenuWindowsSetPage` (0x1401015FC) only
- **Callees:** `sub_1401542AC`, `GUIWidget_FindFirstKind1Component2`, `GUINode_FindDescendant`, `GUINode_FindPartByName`, `GUINode_PlayStateAtFrame`, `GUIComponent_StopAllStates`

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Shows one of the six command-menu pages and binds its radio buttons, icon and title.

## Behavior

- V: writes `addon+5624 = pageId` (the page request), hides all six `BattleMenu01..06` nodes (stop states, play `Hide` at frame -1), then resolves the page node with `sub_1401542AC(addon, pageId)`.
- V: for the page, finds parts `RadioButton01..06` (both as direct parts and as descendants) and `Icon`, and plays the `Hide`/`Active` states as appropriate.
- V: clears the embedded `UIGadgetFFTORadioButtonMenu` at +840 when switching pages: entry count `+856 = 0` (`0x140155D2E`), selected `+1120 = -1` (`0x140155D42`), hover `+1124 = -1` (`0x140155D49`), flags `+1128/+1130 = 0`, and stores the applied page id at `+1136` (`0x140155D58`).
- V: reads the acting unit's preview record: `index = SHIWORD(dword_1407DCF98)`; if `index <= 20`, record = `g_BattleUnitTable + 512*index`; it tests bit 8 of record byte +101 to choose the title/flag strings (218 or 3010, dependent on `+160`).
- V: stores the page's title string ids into the page's `TextTitle` (3802 / 2721 at pseudocode lines 217 and 235) and sets the widget ids of `ActionMenu` and `ActionList` into `g_CharaRenderMgr+44504/+44508`.
- V: ends with `sub_140153AD8(addon)` when the page is missing.

## State touched

- Calls: [GUIWidget_FindFirstKind1Component2](GUIWidget_FindFirstKind1Component2.md), [GUINode_FindDescendant](GUINode_FindDescendant.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [GUINode_PlayStateAtFrame](GUINode_PlayStateAtFrame.md), [GUIComponent_StopAllStates](GUIComponent_StopAllStates.md)

## Notes

The function is 1125 pseudocode lines, mostly repeated node binding. The state a reader needs is the radio-menu reset (`+856` count, `+1120` selected) and the applied page id (`+1136`); the rest is presentation. `+5624` is the request id and did not match the live visible menu.

## Open questions

? the meaning of `+156`/`+160`; ? which UI state the `RadioButton` plays on selection.
