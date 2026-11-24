# LocationsListTabIndex

- **Kind:** observed behaviour
- **Scope:** engine (world map Locations list)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [sub_14022F868](../functions/sub_14022F868.md), [BattleCommand_BuildScreen](../functions/BattleCommand_BuildScreen.md), [WorldMapBaseList_SelectTab](../functions/WorldMapBaseList_SelectTab.md), [WorldMapBaseList_RecordAt](../functions/WorldMapBaseList_RecordAt.md), [WorldMapAgent_LocationsListBlocked](../functions/WorldMapAgent_LocationsListBlocked.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The Locations list's current tab is a dword at +1840 of the list addon: three tabs, 0..2, each with its own record list. A value of 3 or more is the no-tab state: every label deselected and no record list. The two generic list tasks that run the list (menu descriptor 154) change it.

## Behavior

- V: sub_14022F868 reads the tab actions 170 / 171 as -1 / +1 and keeps the result within 0..2 (the limit 2 is loaded at 0x1402307B8).
- I: a fresh press wraps and a held key clamps; the branch depends on a call whose meaning is not mapped.
- V: a mouse click on a tab: when the radio menu's click flag (addon +0x698) is set the task takes the clicked index (addon +0x690) as the new tab (0x1402307E6).
- V: a change plays cue 0x5E and the guide icon press, then calls WorldMapBaseList_SelectTab(addon, tab, 0) at 0x14023083D.
- V: BattleCommand_BuildScreen loads the same limit (0x1402E6F48) and calls WorldMapBaseList_SelectTab at 0x1402E6FAF.
- V: WorldMapBaseList_SelectTab takes values up to 3; for 3 it deselects all three labels and counts tab 0's vector. WorldMapBaseList_RecordAt returns null for any value above 2, so no row is drawn and a confirm is skipped (WorldMapAgent_LocationsListBlocked).
- V: when the tab did not change, the list input runs (UIListGadget_ClassicInput, called at 0x14023085A).
- V (seen live): pad RB / keyboard E and pad LB / keyboard Q step the tab (1 -> 2 -> 1 seen).
- V: WorldMap_OpenLocationsList -> sub_14036E5DC builds the records and calls WorldMapBaseList_SelectTab(addon, tab of the current location, 1) at 0x14036EDFC.

## Open questions

None recorded.
