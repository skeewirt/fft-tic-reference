# Unit_InitJobJp

- **Address:** `0x1402770BC`
- **Area:** [Unit data](../areas/unit-data.md)
- **Prototype:** `void Unit_InitJobJp(UnitWork *c, uint8_t flags, unsigned int jobIndex, int level)`
- **Callers:** Unit_InitAbilitiesFromJob (for job indices 0..19, in pairs)
- **Callees:** Job_GetJpForLevel

Confidence tags: **V** decoded, **M** measured, **I** inferred, **?** unknown.

## Purpose

A new unit's starting JP in one job: the GeneralJob curve's value at the job's level plus a random part.

## Behavior

- V: JP (c + 240 + 2 * index) and total JP (c + 286 + 2 * index) both get base + rand * step >> 15, where base = Job_GetJpForLevel(index, level) (100 at level 0), step = the distance to the next level's value when it is below 100, else 100 (the same at level 8); rand = 15 bits of the game's xorshift128 (xmmword_1408E5FC8).
- V: index 18 with flags bit 7, or index 17 with flags bit 6 (the gender-locked jobs), get 0.
- V (live 2026-11-10, New Game, Orbonne): with the stock curve every human unit's jobs start at level 1 with 100..199 JP; slot 49's save: every stock job a unit may have holds 100 or more total JP.

## State touched

- Calls: [Job_GetJpForLevel](Job_GetJpForLevel.md)

## Referenced by

- Observed behaviours: [NewUnitsGetStartingJpInEveryJob](../behaviors/NewUnitsGetStartingJpInEveryJob.md)

## Notes

The name is ours (IDB: sub_1402770BC).

## Open questions

None recorded.
