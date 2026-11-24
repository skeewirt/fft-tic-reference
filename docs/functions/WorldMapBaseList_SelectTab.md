# WorldMapBaseList_SelectTab

- **Address:** `0x140160BE0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `int *WorldMapBaseList_SelectTab(int64_t self, int tab, char fromOpen)`
- **Callers:** sub_14022F868 (0x14023083D), BattleCommand_BuildScreen (0x1402E6FAF), sub_14036E5DC (0x14036EDFC)
- **Callees:** GUITabButton_Select, GUITabButton_Deselect, GUICore_FocusNode, UIListGadget_SetCount, UITable_GetRowByKey, sub_14040C7D8, GUIComponentList_UpdateScrollBars, GUIComponentList_LayoutSlots, UIListGadget_SetCursor, GUINode_PlayShowHide, UIName_Key, GUINode_StopState, UIName_ReleaseKey, GUINode_FindState, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Selects a tab of the Locations list addon (struct WorldMapBaseList): highlights its label, sets the list count from that tab's records, puts the cursor on the current location and swaps the info panels.

## Behavior

- V: callers pass the new tab; a mouse click reaches it through the radio menu's clicked index (addon +0x690) that sub_14022F868 reads.
- V: for tab <= 3 it stores the tab at +1840 and selects label i = tab of the three labels at +360 (GUITabButton_Select), deselecting the others (GUITabButton_Deselect); with tab 3 all three are deselected.
- V: a negative tab sets the list count to 0. Otherwise the count is the record count of vector `tab`; for tab 3 or more it reads +1704 / +1712, tab 0's vector.
- V: the cursor row is the record whose location word (+52) equals +1844, when the UI table 52 row of that location names this tab (row +36); else row 0. It scrolls the list there and sets the cursor (sound flag +1852 off while it does).
- V: panels: FieldInfo (+712) follows tab 2 and TownInfo (+384) follows tab 0, decided from the previous tab, the new tab and the counts (shown only with records); opening on tab 1 forces both; the BaseInfo node (+344) plays its 'TownInfo' or 'FieldInfo' state for tabs 0 and 2.
- V: last, the inner list node (+352) plays 'Default' with records and 'NoItem' without.

## State touched

- Calls: [GUITabButton_Select](GUITabButton_Select.md), [GUITabButton_Deselect](GUITabButton_Deselect.md), [GUICore_FocusNode](GUICore_FocusNode.md), [UIListGadget_SetCount](UIListGadget_SetCount.md), [UITable_GetRowByKey](UITable_GetRowByKey.md), [GUIComponentList_UpdateScrollBars](GUIComponentList_UpdateScrollBars.md), [GUIComponentList_LayoutSlots](GUIComponentList_LayoutSlots.md), [UIListGadget_SetCursor](UIListGadget_SetCursor.md), [GUINode_PlayShowHide](GUINode_PlayShowHide.md), [UIName_Key](UIName_Key.md), [GUINode_StopState](GUINode_StopState.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)

## Referenced by

- Observed behaviours: [LocationsListTabIndex](../behaviors/LocationsListTabIndex.md)

## Open questions

None recorded.
