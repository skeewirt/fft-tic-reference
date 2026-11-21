# CharaRender_LoadMapLights

- **Address:** `0x1400CB870`
- **Area:** [Graphics](../areas/graphics.md)
- **Prototype:** `void CharaRender_LoadMapLights(void *block, unsigned map)`
- **Callers:** CharaRenderer_Update
- **Callees:** NxdRegistry_Find, NxdTable_GetSetEntries, NxdTable_GetRowById, NxdEntry_GetRow

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the light-source part of the HD character renderer's per-slot block from the map's light rows when the map (or a reload flag) changes.

## Behavior

- V: when block +325 is set or block +320 differs from the map number: clears the first 0x148 bytes, stores the map at +320, and for each of the map's rows of nxd table 234 (through table 218) writes a 20-byte light record at +20 x n (n from the row's kind 100..103 through qword_140783038).
- V: so the first 16 x 20 bytes of the block are the map's lights, not per drawing slot; called each frame by CharaRenderer_Update.

## State touched

- Calls: [NxdRegistry_Find](NxdRegistry_Find.md), [NxdTable_GetSetEntries](NxdTable_GetSetEntries.md), [NxdTable_GetRowById](NxdTable_GetRowById.md), [NxdEntry_GetRow](NxdEntry_GetRow.md)

## Referenced by

- Observed behaviours: [TwentyOneUnitsNeedSixPerSlotStoresWidened](../behaviors/TwentyOneUnitsNeedSixPerSlotStoresWidened.md)

## Open questions

None recorded.
