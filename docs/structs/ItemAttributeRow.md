# ItemAttributeRow

- **Kind:** structure
- **Area:** [Items and shops](../areas/items.md)
- **Size:** 26 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Equipment attribute record.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="stat_bonus"></a>`0x0` | stat_bonus | `uint8[3]` | V | Added to unit work +59..+61 (capped 255) and summed with +56..+58 (I: PA, MA and Speed bonuses). |
| <a id="move_bonus"></a>`0x3` | move_bonus | `uint8` | V | Added to unit work +66 (Move, capped 0xFD). |
| <a id="jump_bonus"></a>`0x4` | jump_bonus | `uint8` | V | Added to unit work +67 (Jump, capped 7). |
| <a id="status_a"></a>`0x5` | status_a | `uint8[5]` | V | ORed into unit work +87.. (the job row first status group). |
| <a id="status_b"></a>`0xA` | status_b | `uint8[5]` | V | ORed into unit work +92.. |
| <a id="status_c"></a>`0xF` | status_c | `uint8[5]` | V | ORed into unit work +97.. |
| <a id="elements"></a>`0x14` | elements | `uint8[5]` | V | ORed into unit work +118..+122 (element groups). |
| <a id="flag25"></a>`0x19` | flag25 | `uint8` | ? | Non-zero sets bit 0x800 of unit work +504; meaning not known. |

## Referenced by

- Described by tables: [ItemAttributes](../tables/ItemAttributes.md)

## Open questions

None recorded.
