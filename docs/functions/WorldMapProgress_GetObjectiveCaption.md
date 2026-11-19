# WorldMapProgress_GetObjectiveCaption

- **Address:** `0x14015E0FC`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `const char *WorldMapProgress_GetObjectiveCaption(void *screen, void *set, int key)`
- **Callers:** WorldMapScreen_SetProgress
- **Callees:** NxdEntry_CopyKeys, NxdSets_Find2

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Returns the world-map objective line for a progress row.

## Behavior

- V: finds the index of the entry (set a2, key a3) in its set (NxdEntry_CopyKeys / NxdSets_Find2/3 paths), then walks backwards to the first row whose sets_objective byte (+0x29) is non-zero and returns its caption (+0x18).
- V: a2 == 0 gives an empty string.

## State touched

- Calls: [NxdEntry_CopyKeys](NxdEntry_CopyKeys.md), [NxdSets_Find2](NxdSets_Find2.md)

## Referenced by

- Called by: [WorldMapScreen_SetProgress](WorldMapScreen_SetProgress.md)
- Observed behaviours: [WorldMapObjectiveLineIsTheNearestCaptionRow](../behaviors/WorldMapObjectiveLineIsTheNearestCaptionRow.md)

## Open questions

None recorded.
