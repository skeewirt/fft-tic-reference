# AbilityAnimRow

- **Kind:** structure
- **Area:** [Ability data](../areas/ability-data.md)
- **Size:** 3 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

Battle presentation of one ability.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="charge"></a>`0x0` | charge | `uint8` | V | Charge or cast effect type: 0 = none (motion 3 is set); otherwise a pair table gives the charging motion. |
| <a id="motion"></a>`0x1` | motion | `uint8` | V | Motion when the action executes: 0 = the weapon attack (a punch bare-handed), 1 = by distance (58 adjacent, else 76), n >= 2 = motion n + 1. |
| <a id="text"></a>`0x2` | text | `uint8` | I | Battle text selector read with the effect word +0x18C; two readers test the values 6 and 0x2B. |

## Referenced by

- Described by tables: [AbilityAnim](../tables/AbilityAnim.md)

## Open questions

None recorded.
