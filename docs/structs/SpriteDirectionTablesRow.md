# SpriteDirectionTablesRow

- **Kind:** structure
- **Area:** [Graphics](../areas/graphics.md)
- **Size:** 1 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One row of SpriteDirectionTables.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="identity_16"></a>`0x0` | identity_16 | `uint8[16]` | V | bytes 0..15 in order; no reader |
| <a id="direction_flag_words"></a>`0x10` | direction_flag_words | `pointer` | V | four words indexed by facing: bit 1 set = mirror the sprite (0, 0, 2, 2) |
| <a id="frame_flag_masks"></a>`0x18` | frame_flag_masks | `uint8[88]` | I | dword masks of sprite frame flags used by the animation stepper (one bit each, 0x40 up to 0x80000000) |
| <a id="mirror_flags_dir16"></a>`0x70` | mirror_flags_dir16 | `uint8[32]` | V | 16 direction mirror flags (already named SpriteDir16MirrorFlags) |
| <a id="walk_phase_steps"></a>`0x90` | walk_phase_steps | `uint8[32]` | I | 16 words: 1,2,2,3,3,4,4,5,5,4,4,3,3,2,2,1 (a walk bob cycle) |
| <a id="palette_base_words"></a>`0xB0` | palette_base_words | `pointer` | V | four words 0, 1, 1, 0 added to the palette number per facing |

## Referenced by

- Described by tables: [SpriteDirectionTables](../tables/SpriteDirectionTables.md)

## Open questions

None recorded.
