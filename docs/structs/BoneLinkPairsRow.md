# BoneLinkPairsRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 16 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the BoneLinkPairs table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="from_bone_name"></a>`0x0` | from_bone_name | `pointer` | V | name of the first bone of the link |
| <a id="to_bone_name"></a>`0x8` | to_bone_name | `pointer` | V | name of the second bone (next along the chain) |

## Referenced by

- Described by tables: [BoneLinkPairs](../tables/BoneLinkPairs.md)

## Open questions

None recorded.
