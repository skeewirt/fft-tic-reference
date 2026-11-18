# SpriteDirectionFlag

- **Kind:** structure
- **Area:** [Unit rendering](../areas/unit-rendering.md)
- **Size:** 2 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the SpriteDirection16MirrorFlags table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="flags"></a>`0x0` | flags | `int16` | V | bit 1 (0x2) set = draw the sprite mirrored; ORed into the sprite record's attribute word |

## Referenced by

- Described by tables: [SpriteDirection16MirrorFlags](../tables/SpriteDirection16MirrorFlags.md)

## Open questions

None recorded.
