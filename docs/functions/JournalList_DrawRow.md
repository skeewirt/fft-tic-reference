# JournalList_DrawRow

- **Address:** `0x14016B0D4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void JournalList_DrawRow(void *row, const void *entry)`
- **Callers:** not recorded
- **Callees:** sub_14016B31C, GUINode_PlayState, GUITextNode_SetTextExpandedTemp

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Draws one row of the Events list.

## Behavior

- V: 'TextName' = title (+0x10); the kind 0 / 1 / 2 plays 'Event' / 'Movie' / 'Battle'; quest_mark (+0x26) plays 'ShowQuest' / 'HideQuest'; sub_14016B31C is called with the entry's new mark (entry +9).

## State touched

- Calls: [GUINode_PlayState](GUINode_PlayState.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md)

## Open questions

None recorded.
