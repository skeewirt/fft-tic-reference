# Map_LoadBattleData

- **Address:** `0x140251584`
- **Area:** [Battle](../areas/battle.md)
- **Prototype:** `void *Map_LoadBattleData(unsigned short mapId)`
- **Callers:** sub_1402516BC
- **Callees:** MapDrawLists_Load, GameData_ReadSectors, memset

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Loads the per-map data of a battle map: its Move-Find row, its draw-index lists and its 4096-byte map block.

## Behavior

- V: copies the map's 24-byte Move-Find row (0x140783840) into the live copy (0x140D8DC90).
- V: clears the 3000-byte block buffer (0x14114A4F0) and takes the block's file sector from the language-0 or other-language per-map table (0x1407B6F30 / 0x1407B7130); a sector of 0 returns null.
- V: calls MapDrawLists_Load unless a flag is set, records the map id and reads 4096 bytes from the sector.

## State touched

- Calls: [MapDrawLists_Load](MapDrawLists_Load.md), [GameData_ReadSectors](GameData_ReadSectors.md)

## Referenced by

- Appears in flows: [MapRendererBuildPath](../flows/MapRendererBuildPath.md)
- Observed behaviours: [EnhancedBattleMapFilesAreNamedByMapId](../behaviors/EnhancedBattleMapFilesAreNamedByMapId.md), [MapDrawListRowsAreSearchedLinearlyToABoundOfFifty](../behaviors/MapDrawListRowsAreSearchedLinearlyToABoundOfFifty.md), [MapLoaderIndexesThreeTablesByASixteenBitMapId](../behaviors/MapLoaderIndexesThreeTablesByASixteenBitMapId.md)
- Reads tables: [MapBlockSectorsLanguage0](../tables/MapBlockSectorsLanguage0.md), [MapBlockSectorsOtherLanguages](../tables/MapBlockSectorsOtherLanguages.md), [MoveFindItems](../tables/MoveFindItems.md)

## Open questions

?: what the 4096-byte map block holds.
