# WorldMapBaseList_DrawRow

- **Address:** `0x140160410`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `_BYTE *WorldMapBaseList_DrawRow(int64_t self, int64_t item, int64_t record)`
- **Callers:** WorldMapBaseList_OnEvent
- **Callees:** UITable_GetRowByKey, GUINode_FindPartByName, PlaceName_GetText, GUITextNode_SetTextExpandedTemp, GUINode_FindDescendant, WorldMapNode_PlayTexChange, GUINode_PlayShowHide, sub_1400FD0E4, UITexturePath_FromRow, GUIWidget_EnsureSlotGroup, UIName_Assign, sub_1400FD238

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws one row of the Locations list addon (struct WorldMapBaseList) from a location record: name, icon and the marks.

## Behavior

- V: looks up UI table 52 by the record's location word (+52); without a row it draws nothing.
- V: 'Title' (a text part) gets the place name of row +20 (PlaceName_GetText, GUITextNode_SetTextExpandedTemp).
- V: 'IconBase' byte +416 = row byte +48; a nonzero icon plays its texture change.
- V: 'Next' is shown when record byte +51 is 3, 'MidwayPoint' when it is 2; 'Current' follows record byte +63 and, when shown, its 'Unit' image is set to a texture path from sub_1400FD0E4; 'Facility' follows record byte +62.

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [PlaceName_GetText](PlaceName_GetText.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md), [GUINode_FindDescendant](GUINode_FindDescendant.md), [WorldMapNode_PlayTexChange](WorldMapNode_PlayTexChange.md), [GUINode_PlayShowHide](GUINode_PlayShowHide.md), [UITexturePath_FromRow](UITexturePath_FromRow.md), [GUIWidget_EnsureSlotGroup](GUIWidget_EnsureSlotGroup.md), [UIName_Assign](UIName_Assign.md)

## Referenced by

- Called by: [WorldMapBaseList_OnEvent](WorldMapBaseList_OnEvent.md)

## Open questions

None recorded.
