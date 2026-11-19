# BgmMode_BuildLists

- **Address:** `0x1401C850C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void BgmMode_BuildLists(void *screen)`
- **Callers:** UIAddonFFTOBGMMode_vfunc_4
- **Callees:** NxdRegistry_Find, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Builds the two track lists of the music player screen from the BGMMode table.

## Behavior

- V: clears the two lists (screen +840 and +872, 32 bytes apart), then for each BGMMode row appends the row id to the list at screen + 8 + 32 * (tab + 26), that is list 0 or 1 by the row's tab (+8).

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)
- Writes: [BgmModeScreen.track_list_0](../structs/BgmModeScreen.md#track_list_0), [BgmModeScreen.track_list_1](../structs/BgmModeScreen.md#track_list_1)

## Notes

Name is ours. Cache qword_143CDA560.

## Open questions

None recorded.
