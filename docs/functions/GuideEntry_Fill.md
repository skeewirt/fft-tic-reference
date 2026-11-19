# GuideEntry_Fill

- **Address:** `0x1400F74F4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GuideEntry_Fill(void *window, int row, ...)`
- **Callers:** UIAddonFFTOBattleMain4_vfunc_4, sub_140117270, sub_140127174, sub_14016DB90 and others
- **Callees:** UITable_GetRowByKeys, UIName_Key, GUINode_FindPartByName, UIName_ReleaseKey, sub_14028BC90, sub_14028BE4C, sub_1400F681C, sub_1400F69BC, UIName_Assign

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills a guide entry (label and one or two buttons) of a window from a UIButtonGuide row.

## Behavior

- V: the label node gets the row's title_text (+0xC).
- V: with guide_icon_2 (+0x10) or ui_key_assign_2 (+0x14) non-zero the entry gets two buttons: (icon_2, action_2, variant byte +0x26) and (icon, action, variant byte +0x24); the single-button case uses guide_icon (+4) when non-zero, else the action (+8).
- V: draws through GuideSlot_DrawButtons and GuideIcon_ToGlyph.

## State touched

- Calls: [UITable_GetRowByKeys](UITable_GetRowByKeys.md), [UIName_Key](UIName_Key.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [UIName_ReleaseKey](UIName_ReleaseKey.md), [sub_1400F69BC](sub_1400F69BC.md), [UIName_Assign](UIName_Assign.md)

## Notes

Name is ours.

## Open questions

None recorded.
