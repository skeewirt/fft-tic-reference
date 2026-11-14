# StatusScreen_SetEntry

- **Address:** `0x140112E84`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char StatusScreen_SetEntry(int64 screen, int64 item, unsigned int status)`
- **Callers:** sub_140112B48
- **Callees:** sub_1400F5828, UIName_Key, GUINode_FindPartByName, UIName_ReleaseKey, Icon_FormatPath, Str_Format, GUIWidget_EnsureSlotGroup, UIName_Assign, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, GUITextNode_SetTextExpandedTemp, __security_check_cookie

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Sets one entry of the Status screen list: the status icon and the status name.

## Behavior

- V: -1 hides the entry (item +0x1A0 = 0).
- V: the icon: Icon row 0x16 (status/textureparts/s_%03d_uitx) formatted with the status, or for Doom (39) with a counter byte at screen +0x1AB the Icon row 0x18 path with 39 and the counter; the Icon part takes the texture when the path changed.
- V: the name: the UIStatusEffect row whose key is status + 1 (no bound), its Name string, into the TextStatus part.

## State touched

- Calls: [UIName_Key](UIName_Key.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [Icon_FormatPath](Icon_FormatPath.md), [Str_Format](Str_Format.md), [GUIWidget_EnsureSlotGroup](GUIWidget_EnsureSlotGroup.md), [UIName_Assign](UIName_Assign.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md)

## Referenced by

- Observed behaviours: [StatusScreenReadersAndIconPath](../behaviors/StatusScreenReadersAndIconPath.md)

## Notes

Name is ours. I: a status with no UIStatusEffect row would dereference a null row; the list builders only list statuses whose row gives a category.

## Open questions

? whether a missing s_%03d texture would draw nothing (not tried).
