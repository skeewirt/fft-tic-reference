# WorldMapObjectiveLineIsTheNearestCaptionRow

- **Kind:** observed behaviour
- **Scope:** engine (world map)
- **Area:** [UI framework](../areas/ui-framework.md)
- **Affects:** [WorldMapProgress_GetObjectiveCaption](../functions/WorldMapProgress_GetObjectiveCaption.md), [WorldMapScreen_SetProgress](../functions/WorldMapScreen_SetProgress.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The objective line of the world map is the caption of the current progress row, or of the nearest earlier row of the same first key whose sets_objective byte is set.

## Behavior

- V: the current progress row is the one named by the GameProgress row's two keys (screen +3308 / +3312).
- V: the search goes backwards from the current row inside its set; no sets_objective row gives the empty line.
- M: every row with sets_objective 0, other than row [0,0], has an earlier row with 1 in its set.

## Open questions

None recorded.
