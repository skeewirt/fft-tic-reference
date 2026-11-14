# NewUnitStartRows

- **Kind:** registry
- **Area:** [Unit data](../areas/unit-data.md)
- **Resolved by:** [Unit_RollStartingStats](../functions/Unit_RollStartingStats.md), [Recruit_GenerateUnit](../functions/Recruit_GenerateUnit.md)
- **Values stored in:** [UnitSaveRecord](../structs/UnitSaveRecord.md)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Summary

The four start rows that Unit_RollStartingStats reads: base and random span of the five stat accumulators in whole raw units, and the seven starting equipment words; a new unit's row is its kind (gender), never its job.

## Entries

| Id | Name | Value | Conf | Meaning |
|---|---|---|---|---|
| <a id="male generic"></a>0 | `male generic` | `base 30 / 14 / 6 / 5 / 4, span 2 / 1 / 0 / 0 / 0, equipment 157 186 255 19 255 255 255` | V | Order HP, MP, SP, PA, MA; raw = base + rand * span (rand uniform in [0, 1)); the stored accumulator is raw * 16384. Used for kind 0 of Recruit_GenerateUnit and for a spawn flagged special. |
| <a id="female generic"></a>1 | `female generic` | `base 28 / 15 / 6 / 4 / 5, span 2 / 1 / 0 / 0 / 0, equipment 157 186 255 19 255 255 255` | V | Kind 1 of Recruit_GenerateUnit and a spawn flagged female (+6 bit 6). |
| <a id="story unit"></a>2 | `story unit` | `base 30 / 15 / 6 / 5 / 5, span 2 / 1 / 0 / 0 / 0, equipment 157 186 208 19 255 255 255` | V | Recruit_GenerateUnit turns any kind other than 0, 1 or 3 into 2 (marker 1, job 1, Brave and Faith 70). |
| <a id="marker 0x82"></a>3 | `marker 0x82` | `base 35 / 8 / 5 / 5 / 5, span 3 / 1 / 0 / 1 / 1, equipment all empty` | V | Kind 3 of Recruit_GenerateUnit and the spawn default for a unit neither flagged female nor special. |

## Open questions

None recorded.
