# GlossaryList_DrawRow

- **Address:** `0x140172604`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void GlossaryList_DrawRow(void *row, const void *entry)`
- **Callers:** not recorded
- **Callees:** LoreDictionary_CurrentRow, GUINode_PlayState, GUITextNode_SetTextExpandedTemp

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws one row of the glossary list.

## Behavior

- V: 'Title' = plain_name (+0x3C) of the current row; the 'ListImage' / 'Image' frame = list_image (+0x44; hidden when 0); 'SubQuest' / 'Default' by sub_quest (+0x4D).

## State touched

- Calls: [LoreDictionary_CurrentRow](LoreDictionary_CurrentRow.md), [GUINode_PlayState](GUINode_PlayState.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md)

## Open questions

None recorded.
