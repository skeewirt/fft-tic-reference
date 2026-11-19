# BgmMode_DrawRow

- **Address:** `0x1401C7DAC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void BgmMode_DrawRow(void *screen, int row)`
- **Callers:** UIAddonFFTOBGMMode_vfunc_2
- **Callees:** GUIComponentList_GetItemComponent, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, UIName_Key, GUINode_FindPartByName, GUITextNode_SetTextExpandedTemp, GUINode_FindState, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws one row of the music player list.

## Behavior

- V: takes the track id from the current list (+824) and reads its BGMMode row; the title is the alternate title (+0xC) when the screen's title-language dword (+896) is 1, else the title (+0x10).

## State touched

- Calls: [GUIComponentList_GetItemComponent](GUIComponentList_GetItemComponent.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [UIName_Key](UIName_Key.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)

## Notes

Name is ours.

## Open questions

None recorded.
