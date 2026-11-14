# Unit_RollStartingStats

- **Address:** `0x1402757B0`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void Unit_RollStartingStats(uint8_t **accumulators, int row)`
- **Callers:** Recruit_GenerateUnit, Unit_BuildFromRecord
- **Callees:** none (the random generator step is inline)

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

Rolls the five 24-bit stat accumulators (HP, MP, Speed, PA, MA) of a new unit from a base value and a random span taken from the start row; the job is not an input.

## Behavior

- V: `accumulators` is an array of five pointers (HP, MP, SP, PA, MA); `row` selects a row of the start tables (0..3 occur).
- V: for each stat i: accumulator = (base[row][i] << 14) + ((rand15 * span[row][i]) >> 1), where rand15 is the low 15 bits of the next output of the global random generator; three bytes are stored, low byte first. So the raw value in whole units is uniform in [base, base + span).
- V: base[row] is the first five bytes of the 12-byte row at 0x14067F7D0 + 12 * row; span[row] is the five bytes at 0x14067F800 + 5 * row.
- V: base rows (HP, MP, SP, PA, MA): row 0 = 30, 14, 6, 5, 4; row 1 = 28, 15, 6, 4, 5; row 2 = 30, 15, 6, 5, 5; row 3 = 35, 8, 5, 5, 5. Span rows: rows 0, 1 and 2 = 2, 1, 0, 0, 0; row 3 = 3, 1, 0, 1, 1.
- V: one random draw is consumed per stat, five in all; the job row and the unit's flags are not read.

## Referenced by

- Called by: [Recruit_GenerateUnit](Recruit_GenerateUnit.md)
- Resolves registries: [NewUnitStartRows](../registries/NewUnitStartRows.md)

## Notes

The raw value is the stat before the job's multiplier: Unit_ComputeStats shows ((accumulator * M) / 100) >> 14 with M from the job row, and Unit_ApplyLevelGrowth grows the accumulator with the job's C at each level. Rows 0 and 1 are the male and female recruits (Recruit_GenerateUnit passes 0 and 1); Unit_BuildFromRecord picks 0 for a unit flagged special (+6 bit 7), 1 for flag 0x40 and 3 otherwise.

## Open questions

? what the callers of the party-reset and egg paths pass for rows 2 and 3 (row 3 is the spawn default for units that are neither flagged female nor special).
