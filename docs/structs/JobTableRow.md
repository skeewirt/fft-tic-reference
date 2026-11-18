# JobTableRow

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 49 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One 49-byte row of the stock job table: skillset, always-on abilities, equipment classes, growth constants, move, jump, evade, status and element sets and three look bytes.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="skillset"></a>`0x0` | skillset | `uint8` | V | Skillset id of the job as a u8 (generic jobs use consecutive ids in job order; one special job uses 224). |
| <a id="innate_abilities"></a>`0x1` | innate_abilities | `uint16[4]` | V | Always-on ability ids (reaction, support or movement kind), 0 = empty slot. |
| <a id="equip_flags"></a>`0x9` | equip_flags | `uint8[5]` | V | Equipable item classes: class n is allowed when bit (7 - n % 8) of byte n / 8 is set; the class is byte +5 of the item record. |
| <a id="hp_c"></a>`0xE` | hp_c | `uint8` | V | HP growth constant C (level-up: raw += raw / (level + C)). |
| <a id="hp_m"></a>`0xF` | hp_m | `uint8` | V | HP multiplier in percent (stat = (raw * M / 100) >> 14). |
| <a id="mp_c"></a>`0x10` | mp_c | `uint8` | V | MP growth constant C. |
| <a id="mp_m"></a>`0x11` | mp_m | `uint8` | V | MP multiplier in percent. |
| <a id="sp_c"></a>`0x12` | sp_c | `uint8` | V | Speed growth constant C. |
| <a id="sp_m"></a>`0x13` | sp_m | `uint8` | V | Speed multiplier in percent. |
| <a id="pa_c"></a>`0x14` | pa_c | `uint8` | V | Physical Attack growth constant C. |
| <a id="pa_m"></a>`0x15` | pa_m | `uint8` | V | Physical Attack multiplier in percent. |
| <a id="ma_c"></a>`0x16` | ma_c | `uint8` | V | Magic Attack growth constant C. |
| <a id="ma_m"></a>`0x17` | ma_m | `uint8` | V | Magic Attack multiplier in percent. |
| <a id="move"></a>`0x18` | move | `uint8` | V | Base Move. |
| <a id="jump_and_flag"></a>`0x19` | jump_and_flag | `uint8` | V | Bits 0..6: base Jump. Bit 7: copied to bit 0x40 of unit byte +81 (meaning not known). |
| <a id="evade"></a>`0x1A` | evade | `uint8` | V | Class evade in percent. |
| <a id="status_permanent"></a>`0x1B` | status_permanent | `uint8[5]` | I | Status set kept permanently (by analogy with the original record layout); zero for all generic jobs. |
| <a id="status_immune"></a>`0x20` | status_immune | `uint8[5]` | I | Status set the job is immune to; zero for all generic jobs. |
| <a id="status_at_start"></a>`0x25` | status_at_start | `uint8[5]` | I | Status set applied at battle start; zero for all generic jobs. |
| <a id="elements"></a>`0x2A` | elements | `uint8[4]` | I | Element sets: absorb, cancel, half, weak (original order); zero for all generic jobs. |
| <a id="look_shape"></a>`0x2E` | look_shape | `uint8` | V | Sprite shape id of the job for units whose marker byte is 130 (monsters and special characters); copied to unit work +399 and returned by the preview shape resolver. 0 for generic jobs, whose shape comes from the marker and job. |
| <a id="look_palette"></a>`0x2F` | look_palette | `uint8` | V | Palette byte for marker-130 units, copied to unit work +400. 0 for generic jobs. |
| <a id="species"></a>`0x30` | species | `uint8` | I | Species or family byte copied to unit +398; the four Dragon formulas accept values 15 and 16. 0 for generic jobs. |

## Referenced by

- Described by tables: [JobTable](../tables/JobTable.md)

## Open questions

None recorded.
