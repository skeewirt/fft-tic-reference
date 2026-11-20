# MapTablesBytesAndTablesNothingReads

- **Kind:** observed behaviour
- **Scope:** engine (Map, MapVariationEvent, MapVariationRandomBattle)
- **Area:** [Data access](../areas/data.md)
- **Affects:** [MapRow_SelectVariation](../functions/MapRow_SelectVariation.md), [MapRenderer_ApplyMapRow](../functions/MapRenderer_ApplyMapRow.md), [MapVariationStruct](../structs/MapVariationStruct.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Columns and a whole table of the battle map tables that no code reads, found by listing every fetch of each table and every use of the fetched rows, so the stored values decide nothing.

## Behavior

- V: the Map table (id 60) is fetched in exactly eight functions (found by scanning every registry lookup of id 60, immediate or computed); together they read only row +0x8, +0xC, +0x10, +0x14, +0x18 and +0x1C. Row +0x0 and +0x4 are read by none (0 and empty on every one of the 129 stock rows).
- V: the MapVariationEvent table (id 207) is fetched in one place (MapRow_SelectVariation), which reads +0x8, the array offset at +0xC and its count at +0x10. Row +0x0 and +0x4 are never read (0 and empty on all 14 rows).
- V: the MapVariationRandomBattle table (id 208) is never fetched: no registry lookup of id 208 exists and no table wrapper is called with it; the random-battle choice uses the Map row's own elements.
- V: no function reads byte +0x44 of a variation element (0 on every element); the members +0x30, +0x34 and +0x47 are stored but their stored copies have no reader that was found, and +0x45 has one reader whose effect was not followed.
- V: the array offsets of a Map row and of a MapVariationEvent row are added to the start of the ROW, not to their own position, and the counts are the dword after the offset (+0x18 and +0x10); neither count is a column of its own.
- I: absence of a reader in the code is what is established; a use through a table pointer computed at run time is not excluded.

## Open questions

None recorded.
