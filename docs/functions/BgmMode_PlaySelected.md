# BgmMode_PlaySelected

- **Address:** `0x1401C811C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void BgmMode_PlaySelected(void *screen)`
- **Callers:** UIAddonFFTOBGMMode_vfunc_2
- **Callees:** GUIComponentList_GetItemComponent, NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow, sub_1401C87A4, EventSoundEntry_Append, UIListGadget_RefreshVisible

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Plays the track under the cursor of the music player.

## Behavior

- V: takes the track id from the current list (+824), reads the BGMMode row and passes its sound (+0x14) to EventSoundEntry_Append.

## State touched

- Calls: [GUIComponentList_GetItemComponent](GUIComponentList_GetItemComponent.md), [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [EventSoundEntry_Append](EventSoundEntry_Append.md), [UIListGadget_RefreshVisible](UIListGadget_RefreshVisible.md)

## Notes

Name is ours.

## Open questions

None recorded.
