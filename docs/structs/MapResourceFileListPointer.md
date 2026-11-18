# MapResourceFileListPointer

- **Kind:** structure
- **Area:** [Resource](../areas/resource.md)
- **Size:** 8 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the MapResourceFilesLanguage0 table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="file_list"></a>`0x0` | file_list | `pointer` | V | pointer to the map's list of {u32 file sector, u32 byte size} pairs (null = no map) |

## Referenced by

- Described by tables: [MapResourceFilesDefault](../tables/MapResourceFilesDefault.md), [MapResourceFilesLanguage0](../tables/MapResourceFilesLanguage0.md)

## Open questions

None recorded.
