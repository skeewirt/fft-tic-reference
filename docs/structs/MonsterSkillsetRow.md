# MonsterSkillsetRow

- **Kind:** structure
- **Area:** [Job data](../areas/job-data.md)
- **Size:** 5 bytes

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

One 5-byte monster skillset: one flag byte and four low ability id bytes.

## Fields

| Offset | Field | Type | Conf | Meaning |
|---|---|---|---|---|
| <a id="flag_bits"></a>`0x0` | flag_bits | `uint8` | V | Bit 8 of the ability id of each of the four slots (top four bits). |
| <a id="ability_low"></a>`0x1` | ability_low | `uint8[4]` | V | Low byte of the ability id of each of the four slots. |

## Referenced by

- Described by tables: [SkillsetTableMonster](../tables/SkillsetTableMonster.md)

## Open questions

None recorded.
