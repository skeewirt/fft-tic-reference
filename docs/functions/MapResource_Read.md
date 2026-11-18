# MapResource_Read

- **Address:** `0x140251640`
- **Area:** [Resource](../areas/resource.md)
- **Prototype:** `void MapResource_Read(const void *request, void *dest)`
- **Callers:** sub_1402516BC, sub_140252214
- **Callees:** GameData_ReadSectors

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Reads one resource file of the current battle map, using the per-map file list when the request carries the marker id.

## Behavior

- V: does nothing when the request's flag byte (+13) is 0.
- V: when the request's sector field holds the marker value, the sector and size come from pair n of the current map's file list (0x140685050 for language 0, 0x140685450 otherwise); otherwise the request's own sector and size are used.
- V: reads only when the size is not 0 and a destination is given.

## State touched

- Calls: [GameData_ReadSectors](GameData_ReadSectors.md)

## Referenced by

- Observed behaviours: [MapResourceFilesAreFileNumberAndSizePairsPerMap](../behaviors/MapResourceFilesAreFileNumberAndSizePairsPerMap.md)
- Reads tables: [MapResourceFilesDefault](../tables/MapResourceFilesDefault.md), [MapResourceFilesLanguage0](../tables/MapResourceFilesLanguage0.md)

## Open questions

None recorded.
