# JobTree_HandleInput

- **Address:** `0x140133FA4`
- **Area:** [Job tree](../areas/job-tree.md)
- **Prototype:** `void JobTree_HandleInput(JobTreeAddon *addon, int *outCode)`
- **Callers:** sub_140115EA8 (input dispatch on focus event 1409)
- **Callees:** Input_TestAction, GUICore_FocusNode, sub_1400F4BCC (sound)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame pad input for the tree: confirm, back and 8-way cursor movement over the panel grid.

## Behavior

- V: reached from sub_140115EA8 on event 1409 (focus) as a direct call with the focused input object; it is NOT addon vtable slot 26 (that slot is JobTree_ReleaseCharaSlots, slot 27 is JobTree_OnFocusChange).
- V: confirm (Input_TestAction(0, 0, 26)) or the held flag addon+12241: sends message 128 with the selected index (index-1 when >= 18, because of the Bard/Dancer pair) and returns code 1400. Back (Input_TestAction(0, 0, 27)): sound 15, code 1400.
- V: direction = two groups of four pad bytes at qword_143CD9EE8 + 13648..13651 and + 13652..13655, each ordered down, left, up, right; up wins over down and right over left, giving up 0, up-right 1, right 2, down-right 3, down 4, down-left 5, left 6, up-left 7, none -1; the first group is used unless it gives none.
- V: neighbour lookup: panel record +0x1A8 (addressed as addon + 496 + 456 x panel: the record starts at addon + 72) holds a navigation table, 8 directions x 2 candidates x (panel byte, flag byte) = 32 B; a candidate equal to the hidden gender slot (17 or 18 by addon+12240) is skipped; with the second group a candidate whose flag byte is set is skipped too.
- V: the starting panel is addon+12232 (the panel under the cursor) when it is a panel; otherwise addon+12236 when it is below the panel count (at least 0), else the constant 20 at 0x140671F04. The chosen neighbour is focused with GUICore_FocusNode(addon + 72 + 456 * panel) when it is below the panel count.

## State touched

- Calls: [Input_TestAction](Input_TestAction.md), [GUICore_FocusNode](GUICore_FocusNode.md), [sub_1400F4BCC](sub_1400F4BCC.md)
- Reads: [JobTreeAddon.selectedSlot](../structs/JobTreeAddon.md#selectedslot)

## Referenced by

- Appears in flows: [JobScreenFrame](../flows/JobScreenFrame.md)
- Observed behaviours: [JobTreePanelLookups](../behaviors/JobTreePanelLookups.md), [JobTreeViewControl](../behaviors/JobTreeViewControl.md)

## Notes

The navigation table is copied into the panel record at refresh time from the GeneralJob row (JobTree_RefreshAddon loop tail). V (live): the stock rows never name a class panel, so the pad skipped class panels.

## Open questions

? In game: the position step and the scroll on a tree with class panels below the screen (built 2026-11-08, not yet run).
