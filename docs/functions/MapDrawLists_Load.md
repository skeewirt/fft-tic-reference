# MapDrawLists_Load

- **Address:** `0x140249CB8`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void MapDrawLists_Load(int mapId)`
- **Callers:** Map_LoadBattleData
- **Callees:** memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Fills the two map draw-index bitsets from the per-map index lists of the current battle map.

## Behavior

- V: clears both bitsets, finds the map's record by linear search over 50 records of the map draw-index table (0x140672780) and sets one bit per listed index (lists end with 0xFFFF).
- V: a map without a record leaves both bitsets empty.

## Referenced by

- Called by: [Map_LoadBattleData](Map_LoadBattleData.md)
- Observed behaviours: [MapDrawListRowsAreSearchedLinearlyToABoundOfFifty](../behaviors/MapDrawListRowsAreSearchedLinearlyToABoundOfFifty.md), [MapLoaderIndexesThreeTablesByASixteenBitMapId](../behaviors/MapLoaderIndexesThreeTablesByASixteenBitMapId.md)
- Reads tables: [MapDrawIndexLists](../tables/MapDrawIndexLists.md)

## Open questions

?: what the two map draw passes do with a marked record.
