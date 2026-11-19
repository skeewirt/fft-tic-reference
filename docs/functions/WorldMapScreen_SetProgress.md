# WorldMapScreen_SetProgress

- **Address:** `0x14015A754`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMapScreen_SetProgress(void *screen, const int *progress)`
- **Callers:** not recorded
- **Callees:** WorldMapProgress_GetObjectiveCaption, UITable_GetRowByKeys, GUITextNode_SetTextExpandedTemp

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Stores the current story progress on the world-map screen and shows the objective line.

## Behavior

- V: screen +3336 = a2[0]; the GameProgress (92) row (0, a2[1]) gives +8 / +0xC, stored at screen +3308 / +3312 (the keys of the current WorldMapProgressInfo row).
- V: the node 'TextTodo' (+2104) gets WorldMapProgress_GetObjectiveCaption(...).

## State touched

- Calls: [WorldMapProgress_GetObjectiveCaption](WorldMapProgress_GetObjectiveCaption.md), [UITable_GetRowByKeys](UITable_GetRowByKeys.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md)

## Referenced by

- Observed behaviours: [WorldMapObjectiveLineIsTheNearestCaptionRow](../behaviors/WorldMapObjectiveLineIsTheNearestCaptionRow.md)

## Open questions

None recorded.
