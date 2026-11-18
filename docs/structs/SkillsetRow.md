# SkillsetRow

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 25 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One 25-byte skillset: three bytes of ability bit-9 flags followed by 22 low ability id bytes.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="flag_bits"></a>`0x0` | flag_bits | `uint8[3]` | V | Bit n (from the top of byte 0) is bit 8 of the ability id of slot n; the two lowest bits of byte 2 are unused and zero in every row. |
| <a id="ability_low"></a>`0x3` | ability_low | `uint8[22]` | V | Low byte of the ability id of each slot: slots 0..15 hold actions, 16..21 hold reaction, support and movement abilities (I). A slot is empty when the whole 9-bit id is 0. |

## Behavior

- V: ability id = low byte + 0x100 when the slot flag bit is set.

## Referenced by

- Described by tables: [SkillsetTable](../tables/SkillsetTable.md), [SkillsetTableSpecial](../tables/SkillsetTableSpecial.md)

## Open questions

None recorded.
