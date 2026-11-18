# MapLoaderIndexesThreeTablesByASixteenBitMapId

- **Kind:** observed behaviour
- **Scope:** engine (battle map load)
- **Area:** [Battle](../areas/battle.md)
- **Affects:** [Map_LoadBattleData](../functions/Map_LoadBattleData.md), [MapDrawLists_Load](../functions/MapDrawLists_Load.md), [GameData_ReadSectors](../functions/GameData_ReadSectors.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Map_LoadBattleData takes the battle map id as a 16-bit value and uses it, with no bound, as the row of three tables: the Move-Find rows (24 bytes), the map-block file numbers of the two text-language copies (4 bytes), and, through MapDrawLists_Load, a linear search over the draw-list rows.

## Behavior

- V: the id is the argument as an unsigned 16-bit value; the Move-Find row is the 24 bytes at table + 24 x id, copied into a working copy of the battle; no comparison of the id with a row count precedes it.
- V: the file number of the map block is the dword at index id of the table of the current text language (the table for language 0 when the language record says 0, else the other table); a value of 0 means the map has no block and the function returns without reading or loading anything else.
- V: the map block is 4096 bytes read with GameData_ReadSectors(file number, 0, 0x1000, buffer): the locator holds a FILE number of the game's packed data, not a sector.
- V: the draw lists are loaded only when the graphics-mode flag at 0x142E80048 is zero (the classic renderer's data); I: that flag is nonzero in the enhanced renderer, whose mesh load is gated on it being nonzero.
- V (native run on the unmodified image): for each stock map 0..127 the function returns the buffer for the 123 maps that have a locator and null for the five that have none, and the Move-Find working copy equals the stock row.

## Notes

The two locator tables and the Move-Find table have exactly one instruction each that addresses them (census of the whole image).

## Open questions

None recorded.
