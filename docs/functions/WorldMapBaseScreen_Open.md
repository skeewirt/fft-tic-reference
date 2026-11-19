# WorldMapBaseScreen_Open

- **Address:** `0x1401582D0`
- **Area:** [UI framework](../areas/ui-framework.md)
- **Prototype:** `void WorldMapBaseScreen_Open(void *screen, int location)`
- **Callers:** not recorded
- **Callees:** UITable_GetRowByKey, Str_Format

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Opens a location's own world-map screen file.

## Behavior

- V: loads wm_base_<'%02d' of Town base_number (+0x2C)>.uib (UIAddon 137) when Town base (+0x30) is set, else UIAddon row 141.
- I: the name of this function is proposed from the file names it builds.

## State touched

- Calls: [UITable_GetRowByKey](UITable_GetRowByKey.md), [Str_Format](Str_Format.md)

## Referenced by

- Observed behaviours: [WorldMapRoutesAndLocationsFollowProgress](../behaviors/WorldMapRoutesAndLocationsFollowProgress.md)

## Open questions

None recorded.
