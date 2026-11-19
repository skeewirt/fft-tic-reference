# BgmModeScreen

- **Kind:** structure
- **Area:** [UI framework](../areas/ui-framework.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The music player screen (UIAddonFFTOBGMMode): its two track lists and the state of the list and title language.

## Fields

| Offset | Field | Type | Conf | Meaning | Written by |
|---|---|---|---|---|---|
| <a id="tab_node_0"></a>`0x80` | tab_node_0 | `pointer` | V | First tab node (+128), moved between by actions 43 and 44. |  |
| <a id="tab_node_1"></a>`0x88` | tab_node_1 | `pointer` | V | Second tab node (+136). |  |
| <a id="current_list"></a>`0x338` | current_list | `int32` | V | Index of the current list, 0 or 1 (+824): set from the tab button (id - 100) or by actions 43 / 44. |  |
| <a id="track_list_0"></a>`0x348` | track_list_0 | `vector` | V | List of BGMMode row ids of tab 0 (+840). | [BgmMode_BuildLists](../functions/BgmMode_BuildLists.md) |
| <a id="track_list_1"></a>`0x368` | track_list_1 | `vector` | V | List of BGMMode row ids of tab 1 (+872, 32 bytes after list 0). | [BgmMode_BuildLists](../functions/BgmMode_BuildLists.md) |
| <a id="title_alt"></a>`0x380` | title_alt | `int32` | V | 1 = rows show the alternate title (BGMMode title_alt) instead of the title (+896); toggled by BgmMode_ToggleTitleLanguage. | [BgmMode_ToggleTitleLanguage](../functions/BgmMode_ToggleTitleLanguage.md) |

## Behavior

- V: BgmMode_BuildLists fills the two lists by the tab column of each BGMMode row.

## Notes

Name is ours. Offsets given in decimal in the code: +128, +136, +824, +840, +872, +896.

## Open questions

? the other fields.
