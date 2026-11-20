# AbilityActionRow

- **Kind:** structure
- **Area:** [Ability data](../areas/ability-data.md)
- **Size:** 20 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One action record of an ability.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="range"></a>`0x0` | range | `uint8` | V | Range in tiles. |
| <a id="effect_area"></a>`0x1` | effect_area | `uint8` | I | Effect area radius. |
| <a id="vertical"></a>`0x2` | vertical | `uint8` | I | Vertical tolerance. |
| <a id="flags_a"></a>`0x3` | flags_a | `uint8[2]` | I | Flag bytes 1 and 2 (range / targeting behaviour flags). |
| <a id="flags_b"></a>`0x5` | flags_b | `uint8[2]` | I | Flag bytes 3 and 4. |
| <a id="element"></a>`0x7` | element | `uint8` | I | Element bit set. |
| <a id="formula"></a>`0x8` | formula | `uint8` | I | Formula id (dispatcher input, 1..106). |
| <a id="param_x"></a>`0x9` | param_x | `uint8` | I | Formula parameter X. |
| <a id="param_y"></a>`0xA` | param_y | `uint8` | I | Formula parameter Y. |
| <a id="inflict"></a>`0xB` | inflict | `uint8` | V | Index of an inflict record (InflictRecords). |
| <a id="charge_time"></a>`0xC` | charge_time | `uint8` | V | Charge time. |
| <a id="mp_cost"></a>`0xD` | mp_cost | `uint8` | V | MP cost. |
| <a id="unknown14"></a>`0xE` | unknown14 | `uint8[2]` | V | Read by no function of the game (bytes +14 and +15; they travel only inside a 16-byte block save and restore of the current action); zero in every record. |
| <a id="unknown16"></a>`0x10` | unknown16 | `uint8[4]` | V | Read by no function of the game (bytes +16..+19; only the block save and restore of the current action copies them, and one dword clear writes them); 0xFF in every record. |

## Referenced by

- Described by tables: [AbilityActionRecords](../tables/AbilityActionRecords.md), [AbilityActionWorking](../tables/AbilityActionWorking.md)
- Observed behaviours: [RecordBytesTheGameNeverReads](../behaviors/RecordBytesTheGameNeverReads.md)

## Open questions

None recorded.
