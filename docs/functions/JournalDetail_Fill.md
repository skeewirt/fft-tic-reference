# JournalDetail_Fill

- **Address:** `0x14016B49C`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void JournalDetail_Fill(void *panel, const void *entry)`
- **Callers:** not recorded
- **Callees:** NxdTable_GetRowById, GUINode_PlayState, GUITextNode_SetTextExpandedTemp

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the Events detail panel.

## Behavior

- V: title (+0x10) and text (+0x14); 'ShowPlace' / 'HidePlace' by place_name (+0x1C: the PlaceName table 85 row, string +0xC into the node at +880); 'Clear' (node at +896, bound in sub_14016A5EC) plays 'Enable' / 'Disable' by clear_mark (+0x25).

## State touched

- Calls: [NxdTable_GetRowById](NxdTable_GetRowById.md), [GUINode_PlayState](GUINode_PlayState.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md)

## Referenced by

- Observed behaviours: [ClearMarkAppearsOnFourScreens](../behaviors/ClearMarkAppearsOnFourScreens.md)

## Open questions

None recorded.
