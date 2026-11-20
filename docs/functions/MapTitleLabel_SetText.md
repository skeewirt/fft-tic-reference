# MapTitleLabel_SetText

- **Address:** `0x140149148`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `char MapTitleLabel_SetText(void *window, unsigned textId, __int64 arg3, const char *text, char jaState)`
- **Callers:** MapTitle_SetFromMapId, sub_140148DE4
- **Callees:** GUINode_FindDescendant, GUINode_FindPartByName, GUIWidget_FindComponentCached, GUITextNode_SetString, GUITextNode_SetTextById, GUINode_StopState, GUINode_FindState, GUINode_PlayState

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the 'Text' and 'Text00' nodes of the 'TextMapGrade' label of a window and plays its 'En' or 'Ja' state.

## Behavior

- V: acts only when the window's node tree exists: finds the node 'TextMapGrade', its part 'MaskNode00' (a node of kind 9), the component it names, and in it the text parts 'Text' and 'Text00' (kind 3).
- V: each text part gets the passed string when it is non-null, else the text of the id (GUITextNode_SetTextById).
- V: state choice: when the language record is missing, or its language id (record +8) is not 0, 4, 5 or 6, or the flag argument is 0, the 'Ja' state is stopped and 'En' is played; otherwise 'En' is stopped and 'Ja' played.
- V: the state found is marked (byte +104 set to 1) and played.

## State touched

- Calls: [GUINode_FindDescendant](GUINode_FindDescendant.md), [GUINode_FindPartByName](GUINode_FindPartByName.md), [GUIWidget_FindComponentCached](GUIWidget_FindComponentCached.md), [GUITextNode_SetString](GUITextNode_SetString.md), [GUITextNode_SetTextById](GUITextNode_SetTextById.md), [GUINode_StopState](GUINode_StopState.md), [GUINode_FindState](GUINode_FindState.md), [GUINode_PlayState](GUINode_PlayState.md)

## Referenced by

- Called by: [MapTitle_SetFromMapId](MapTitle_SetFromMapId.md)
- Observed behaviours: [MapRowPlaceNameKeys](../behaviors/MapRowPlaceNameKeys.md)

## Notes

With the Map row's title_ja_state at 0 (the ten closing-title rows, M) the label plays 'En' in every language; with 1 (the other 119 rows) it plays 'Ja' for the language ids 0, 4, 5 and 6.

## Open questions

? which language names the ids 0, 4, 5 and 6 stand for, and what the two states look like.
