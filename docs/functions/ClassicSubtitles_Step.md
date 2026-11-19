# ClassicSubtitles_Step

- **Address:** `0x1401969CC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void ClassicSubtitles_Step(void *stepper, float movieTime)`
- **Callers:** sub_1401969B4
- **Callees:** NxdRegistry_Find, NxdTable_GetEntryByKeyIndex, NxdEntry_GetRow, sub_140196C80, GUITextNode_SetTextExpandedTemp

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Per-frame step of the classic-movie subtitle window: finds the line whose time window holds the movie time and sets its text and layout state.

## Behavior

- V: the UIClassicSubtitles rows of the movie key are read by line index; a line is current when starts_at (+0xC) <= movie time < ends_at (+0x10); text is +8.
- V: line_layout (+0x14) is mapped 1 to 2, 2 to 3, 3 to 4, 4 to 5, any other value to 1 and stored as the state byte (+24); state 0 means no line (after ends_at).
- V: the keep_shown byte (+0x18) is kept at +25 and passed to ClassicSubtitles_SetState.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetEntryByKeyIndex](NxdTable_GetEntryByKeyIndex.md), [NxdEntry_GetRow](NxdEntry_GetRow.md), [GUITextNode_SetTextExpandedTemp](GUITextNode_SetTextExpandedTemp.md)
- Writes: [ClassicSubtitleStepper.state](../structs/ClassicSubtitleStepper.md#state), [ClassicSubtitleStepper.keep_shown](../structs/ClassicSubtitleStepper.md#keep_shown)

## Referenced by

- Appears in flows: [MovieStart](../flows/MovieStart.md)

## Notes

Name is ours. Cache qword_143CDA558.

## Open questions

None recorded.
