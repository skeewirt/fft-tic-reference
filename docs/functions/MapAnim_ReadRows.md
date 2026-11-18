# MapAnim_ReadRows

- **Address:** `0x1400C795C`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `char MapAnim_ReadRows(void *animSet, unsigned mapId)`
- **Callers:** MapAnim_Load
- **Callees:** NxdTable_GetRowById, NxdTable_GetEntryCount, NxdTable_GetEntryByKeyIndex

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Copies the RefinedBgAnim rows of a map into the anim set's per-entry table; returns 0 when any row's kind is 0.

## Behavior

- V: no table or no row of the map: returns 1 (anim wanted); otherwise for each row of the map's set stores kind (+4) and the byte at +8; a row whose kind is 0 returns 0 at once (no anim file).
- V (data): map 5's only row has kind 0 and the pack holds no anim file for map 5; the other maps with a mesh and a non-zero kind have one.

## State touched

- Calls: [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdTable_GetEntryCount](NxdTable_GetEntryCount.md), [NxdTable_GetEntryByKeyIndex](NxdTable_GetEntryByKeyIndex.md)

## Referenced by

- Called by: [MapAnim_Load](MapAnim_Load.md)
- Observed behaviours: [MapRendererTableRowFallbacks](../behaviors/MapRendererTableRowFallbacks.md)

## Open questions

None recorded.
