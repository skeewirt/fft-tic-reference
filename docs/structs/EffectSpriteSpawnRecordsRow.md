# EffectSpriteSpawnRecordsRow

- **Kind:** structure
- **Area:** [Battle](../areas/battle.md)
- **Size:** 46 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of the EffectSpriteSpawnRecords table.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="sprite_def"></a>`0x0` | sprite_def | `uint8` | V | sprite definition index |
| <a id="frame_lo"></a>`0x2` | frame_lo | `uint8` | V | first frame |
| <a id="frame_hi"></a>`0x3` | frame_hi | `uint8` | V | frame bound |
| <a id="max_live"></a>`0x4` | max_live | `uint8` | V | live sprite limit |
| <a id="sprite_params"></a>`0x5` | sprite_params | `bytes[37]` | ? | parameters of the sprite setup |
| <a id="spawn_count"></a>`0x2A` | spawn_count | `uint8` | V | sprites per call |
| <a id="tail"></a>`0x2B` | tail | `bytes[3]` | ? | flag and padding |

## Referenced by

- Described by tables: [EffectSpriteSpawnRecords](../tables/EffectSpriteSpawnRecords.md)

## Open questions

None recorded.
