# WorldMapScreen_ScrollToProgress

- **Address:** `0x14015DAE4`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMapScreen_ScrollToProgress(void *screen)`
- **Callers:** not recorded
- **Callees:** not recorded

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Computes the map scroll target of the current progress row.

## Behavior

- V: when WorldMapProgressInfo map_x (+0x20) and map_y (+0x24) are both not -1 they are the scroll target; clamped and stored at screen +3324 / +3328.

## Referenced by

- Observed behaviours: [WorldMapRoutesAndLocationsFollowProgress](../behaviors/WorldMapRoutesAndLocationsFollowProgress.md)

## Open questions

None recorded.
