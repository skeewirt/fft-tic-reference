# SaveLoadList_Refresh

- **Address:** `0x140187BD4`
- **Area:** [Save data](../areas/save-data.md)
- **Prototype:** `int64_t SaveLoadList_Refresh(int64_t addon)`
- **Callers:** UIAddonFFTOSaveLoad_vfunc_4 (0x14018537F), sub_140183C38 (0x140183D50), sub_140183DD4 (0x140183EAB)
- **Callees:** SaveLoadList_BuildEntries (0x140187BF0), UIName_Key (0x140187C23), GUINode_FindState (0x140187C31), GUINode_PlayState (0x140187C42), UIName_ReleaseKey (0x140187C56), sub_14040AEE8 (0x140187C7A), sub_14040B128 (0x140187C81), sub_140187678 (0x140187C98), UIListGadget_Show (0x140187CA6), sub_140187B08 (0x140187CC8)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rebuilds the list for the current tab and presents either the rows or the empty-state text. It also resets the auto/manual filter, updates the three filter buttons and ends by refreshing the guide bar.

## Behavior

- V: calls `SaveLoadList_BuildEntries`, which releases vector A's rows, empties vector C, rebuilds vector A for the tab at +432 and sorts it.
- V: sets +436 to 0 when the tab is 1 and to -1 on tabs 0 and 2. A -1 disables the auto/manual filter and exposes every row; 0 is the 'all rows' filter state of tab 1.
- V: when vector A is empty, it looks up the widget's `ShowTextNone` state, marks and plays it, then applies the selected or normal state to the three filter buttons at +80/+88/+96 (the selected index is +436). This branch does not call `UIListGadget_Show`.
- V: when vector A has rows, it calls `sub_140187678`, which rebuilds vector C through the +436 filter, clears the preview map, sets the list count and cursor, switches between `ShowList` and `ShowTextNone`, and focuses the list; it then shows the gadget at +104.
- V: it always finishes by calling `sub_140187B08`, which chooses a guide id from the tab, the filter and the selected row, and shows the guide bar.
- V: three callers: the add-on bind/refresh virtual (0x14018537F), save state 6 phase 2 (0x140183D50) and erase state 7 phase 2 (0x140183EAB).
- I: the empty branch is the 'no saves' presentation; it relies on the layout's `ShowTextNone` state instead of an empty list (rests on the state it plays and on the missing gadget show).
- ?: what the guide ids selected by `sub_140187B08` are called in the UI table.

## State touched

- Calls: [SaveLoadList_BuildEntries](SaveLoadList_BuildEntries.md), [UIName_Key](UIName_Key.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [UIListGadget_Show](UIListGadget_Show.md)
- Reads: [UIAddonFFTOSaveLoad](../structs/UIAddonFFTOSaveLoad.md)
- Writes: [UIAddonFFTOSaveLoad](../structs/UIAddonFFTOSaveLoad.md)

## Referenced by

- Appears in flows: [SaveLoadScreenFlow](../flows/SaveLoadScreenFlow.md)

## Notes

Whole body read (249 bytes). The empty branch, the filter reset, the gadget show and the guide tail were checked. `sub_140187678` is the row-visibility rebuild; `UIListGadget_Show` is called only on the non-empty branch.

## Open questions

? the UI-table names of the guide ids chosen by `sub_140187B08`; ? whether every tab uses the same guide set.
