# SectorOnly

- **Kind:** structure
- **Area:** [Resource](../areas/resource.md)
- **Size:** 4 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the MapBlockSectorsLanguage0 table and the tables that share its shape.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="sector"></a>`0x0` | sector | `uint32` | V | file sector of the map's 4096-byte block read into 0x14114A4F0 (0 = none) |

## Referenced by

- Described by tables: [MapBlockSectorsLanguage0](../tables/MapBlockSectorsLanguage0.md), [MapBlockSectorsOtherLanguages](../tables/MapBlockSectorsOtherLanguages.md)

## Open questions

None recorded.
