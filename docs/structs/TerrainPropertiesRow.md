# TerrainPropertiesRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One byte of a TerrainProperties block (two blocks of 64).

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="value"></a>`0x0` | value | `uint8` | I | block 0: ability id of the terrain; block 1: flag byte (0x80 harmful) |

## Referenced by

- Described by tables: [TerrainProperties](../tables/TerrainProperties.md)

## Open questions

None recorded.
